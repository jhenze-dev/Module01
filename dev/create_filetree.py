# Path: dev/create_filetree.py
# Project: ONCT Module
# Creator: Jack Henze
# Contact: j.henze@unicoz.nl
# Version: 2627_0.1.1
# Copyright (c) 2026 Jack Henze

import os
from datetime import datetime
from fnmatch import fnmatch


# Namen en patronen die niet in de filetree worden opgenomen.
#
# Voorbeelden:
#   ".git"       -> sluit een bestand of map met exact deze naam uit
#   "*.pyc"      -> sluit alle bestanden met de extensie .pyc uit
#   "filetree*"  -> sluit alle namen uit die beginnen met filetree
IGNORE_PATTERNS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    "site",
    ".DS_Store",
    "Thumbs.db",
    "*.pyc",
    "*.pyo",
    "*.log",
    "filetree.txt",
}


def should_ignore(name):
    """Controleer of een bestands- of mapnaam overeenkomt met een ignore-patroon."""
    return any(fnmatch(name, pattern) for pattern in IGNORE_PATTERNS)


def generate_tree(start_path, output_file="filetree.txt"):
    """Genereer een tekstbestand met de mappen- en bestandenstructuur."""

    start_path = os.path.abspath(start_path)
    output_path = os.path.abspath(output_file)
    lines = []

    def tree(dir_path, prefix=""):
        try:
            entries = []

            for entry in os.listdir(dir_path):
                full_path = os.path.join(dir_path, entry)

                if should_ignore(entry):
                    continue

                # Voorkom dat het gegenereerde outputbestand zichzelf opneemt.
                if os.path.abspath(full_path) == output_path:
                    continue

                entries.append(entry)

            entries.sort(
                key=lambda entry: (
                    not os.path.isdir(os.path.join(dir_path, entry)),
                    entry.lower(),
                )
            )

            for index, entry in enumerate(entries):
                full_path = os.path.join(dir_path, entry)
                is_last = index == len(entries) - 1

                connector = "└── " if is_last else "├── "
                lines.append(f"{prefix}{connector}{entry}")

                if os.path.isdir(full_path):
                    extension = "    " if is_last else "│   "
                    tree(full_path, prefix + extension)

        except PermissionError:
            lines.append(f"{prefix}└── [geen toegang]")

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines.append(f"File tree generated on: {now}")
    lines.append("")
    lines.append(os.path.basename(start_path))

    tree(start_path)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

    return output_path


if __name__ == "__main__":
    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    output_path = generate_tree(
        start_path=project_root,
        output_file=os.path.join(project_root, "dev", "filetree.txt"),
    )

    print(f"Tree saved to {output_path}")