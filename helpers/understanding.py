from pathlib import Path
import os


def _get_entry(
    item: str,
    catalog: dict,
) -> dict:
    """
    Haal één Understanding-item op uit understanding.yml.
    """

    domain, key = item.split(
        ".",
        1,
    )

    return catalog[
        domain
    ][
        key
    ]


def _build_pdf_reference(
    items: list[str],
    catalog: dict,
    pages: dict,
) -> str:
    """
    Bouw voor de complete Module-PDF een verwijzing
    naar de Understanding-pagina's.
    """

    entries = []

    for item in items:

        entry = _get_entry(
            item=item,
            catalog=catalog,
        )

        entries.append(
            {
                "id": item,
                "title": entry["title"],
                "page": pages[item]["page"],
            }
        )

    if not entries:
        return ""

    first = entries[0]
    last = entries[-1]

    if len(entries) == 1:
        return (
            f"{first['title']}, "
            f"p. {first['page']}."
        )

    return (
        f"{first['title']} t/m "
        f"{last['title']}, "
        f"p. {first['page']}–{last['page']}."
    )


def _understanding_page_path(
    entry: dict,
) -> Path:
    """
    Bepaal vanuit de centrale _content-bron het pad
    naar de zelfstandige Understanding-pagina.

    Bijvoorbeeld:

        understanding/_content/visual-first/
        flowcharts/decisions-branches.md

    wordt:

        understanding/visual-first/
        flowcharts/decisions-branches.md
    """

    source = Path(
        entry["source"]
    )

    parts = list(
        source.parts
    )

    if "_content" not in parts:
        raise RuntimeError(
            "Understanding-source bevat geen "
            f"'_content'-map: {source}"
        )

    parts.remove(
        "_content"
    )

    return Path(
        *parts
    )


def _build_web_links(
    items: list[str],
    catalog: dict,
    current_source_path: str | Path,
) -> str:
    """
    Bouw voor web een lijst links naar de zelfstandige
    Understanding-pagina's.

    Wordt onder andere gebruikt vanuit Thinking Sets.
    """

    current_source_path = Path(
        current_source_path
    )

    links = []

    for item in items:

        entry = _get_entry(
            item=item,
            catalog=catalog,
        )

        target = _understanding_page_path(
            entry
        )

        relative_path = os.path.relpath(
            target,
            current_source_path.parent,
        )

        relative_path = Path(
            relative_path
        ).as_posix()

        links.append(
            f"[{entry['title']}]"
            f"({relative_path})"
        )

    return "\n\n".join(
        links
    )


def _build_web_inline(
    items: list[str],
    catalog: dict,
    docs_root: str | Path,
) -> str:
    """
    Neem voor web de centrale Understanding-_content
    rechtstreeks op.

    Wordt gebruikt vanuit Problem Sets.
    """

    docs_root = Path(
        docs_root
    )

    sections = []

    for item in items:

        entry = _get_entry(
            item=item,
            catalog=catalog,
        )

        source_path = (
            docs_root
            / entry["source"]
        )

        if not source_path.exists():
            raise RuntimeError(
                "Understanding-bron ontbreekt:\n"
                f"  {source_path}"
            )

        content = source_path.read_text(
            encoding="utf-8"
        ).strip()

        sections.append(
            content
        )

    return "\n\n".join(
        sections
    )


def understanding_reference(
    items,
    catalog,
    pages,
    render_mode: str = "web",
    page_template: str = "",
    docs_root: str | Path | None = None,
    current_source_path: str | Path | None = None,
) -> str:
    """
    Render Understanding afhankelijk van uitvoervorm.

    Complete Module-PDF:
        titel + paginanummer(s)

    Website / Problem Set:
        centrale _content inline opnemen

    Website / Thinking Set:
        link naar zelfstandige Understanding-pagina

    Voor andere webpagina's gebruiken we eveneens links,
    zodat Understanding-content niet onverwacht wordt
    gedupliceerd.
    """

    if not items:
        return ""

    if render_mode == "module_pdf":
        return _build_pdf_reference(
            items=items,
            catalog=catalog,
            pages=pages,
        )

    if page_template == "pset.html":

        if docs_root is None:
            raise RuntimeError(
                "docs_root is vereist voor "
                "inline Understanding-content."
            )

        return _build_web_inline(
            items=items,
            catalog=catalog,
            docs_root=docs_root,
        )

    if current_source_path is None:
        raise RuntimeError(
            "current_source_path is vereist voor "
            "Understanding-links."
        )

    return _build_web_links(
        items=items,
        catalog=catalog,
        current_source_path=current_source_path,
    )