import argparse
import io
import os
import subprocess
import sys
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.pdf.build_module import build_module
from scripts.pdf.build_understanding import build_understanding_pdf


def build_site(language: str, clean: bool = False) -> None:
    env = os.environ.copy()
    env["LANGUAGE"] = language

    command = [
        sys.executable,
        "-m",
        "mkdocs",
        "build",
    ]

    if clean:
        command.append("--clean")

    subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def build_language(language: str) -> None:
    os.environ["LANGUAGE"] = language

    print()
    print("=" * 40)
    print(f" BUILD {language.upper()}")
    print("=" * 40)

    print()
    print("[1/4] Website")
    build_site(language, clean=(language == "nl"))
    print("      ✓ Gereed: site/")

    print()
    print("[2/4] Understanding PDF")
    with redirect_stdout(io.StringIO()):
        understanding_pdf = build_understanding_pdf()
    print(f"      ✓ Gereed: {understanding_pdf}")

    print()
    print("[3/4] Module PDF")
    with redirect_stdout(io.StringIO()):
        module_pdf = build_module()
    print(f"      ✓ Gereed: {module_pdf}")

    print()
    print("[4/4] Standalone PDF")
    print("      ○ Nog niet geïmplementeerd")

    print()
    print("=" * 40)
    print(f" BUILD {language.upper()} GEREED")
    print("=" * 40)


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "languages",
        nargs="+",
        choices=("nl", "en"),
    )

    args = parser.parse_args()

    for language in args.languages:
        build_language(language)


if __name__ == "__main__":
    main()