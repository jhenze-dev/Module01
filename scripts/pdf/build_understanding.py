import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from scripts.pdf.build_module import (
    build_understanding,
    read_understanding_page_map,
    render_pdf,
    write_understanding_page_map,
)


ROOT = Path(__file__).resolve().parents[2]

PDF_OUTPUT_ROOT = (
    ROOT
    / "build"
    / "pdf"
)

TEMPLATE_DIR = (
    ROOT
    / "render"
    / "pdf"
    / "understanding"
)


def render_understanding(
    understanding: list[dict],
) -> str:

    environment = Environment(
        loader=FileSystemLoader(
            TEMPLATE_DIR
        )
    )

    template = environment.get_template(
        "understanding.html"
    )

    return template.render(
        document_title="Understanding",
        understanding=understanding,
        pdf_css="mkdocs/assets/css/badges.css",
    )


def build_understanding_pdf() -> Path:
    language = os.environ.get(
        "LANGUAGE",
        "nl",
    ).strip().lower()

    if language not in {"nl", "en"}:
        raise RuntimeError(
            f"Ongeldige LANGUAGE: {language}"
        )

    output_dir = (
        PDF_OUTPUT_ROOT
        / language
        / "understanding"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    understanding = build_understanding()

    html = render_understanding(
        understanding
    )

    html_path = (
        output_dir
        / "understanding.html"
    )

    html_path.write_text(
        html,
        encoding="utf-8",
    )

    pdf_path = (
        output_dir
        / "understanding.pdf"
    )

    render_pdf(
        html_path=html_path,
        pdf_path=pdf_path,
    )

    page_map = read_understanding_page_map(
        pdf_path
    )

    write_understanding_page_map(
        page_map
    )

    return pdf_path


def main():
    build_understanding_pdf()


if __name__ == "__main__":
    main()
