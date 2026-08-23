from pathlib import Path

def _get_entry(
    item: str,
    catalog: dict,
) -> dict:
    """
    Haal één resourcegroep op uit resources.yml.

    Bijvoorbeeld:

        w3schools.week3
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


def get_resource_page_path(
    item: str,
    language: str = "nl",
) -> str:
    """
    Bepaal het publieke pad van de zelfstandige
    resourcepagina voor een resourcegroep.

    Bijvoorbeeld:

        w3schools.week3

    wordt voor Nederlands:

        nl/pdf-resources/03/w3schools/
    """

    domain, key = item.split(
        ".",
        1,
    )

    if not (
        key.startswith("week")
        and key[4:].isdigit()
    ):
        raise RuntimeError(
            "Resource-ID heeft geen geldige week:\n"
            f"  {item}"
        )

    week_number = int(
        key[4:]
    )

    week_key = f"{week_number:02d}"

    return (
        f"{language}/"
        f"pdf-resources/"
        f"{week_key}/"
        f"{domain}/"
    )


def _build_web_group(
    entry: dict,
) -> str:
    """
    Bouw een resourcegroep voor de website.

    Iedere bron wordt als gewone klikbare Markdown-link
    weergegeven.
    """

    links = []

    for link in entry.get(
        "links",
        [],
    ):

        links.append(
            f"- [{link['label']}]"
            f"({link['url']})"
        )

    return "\n".join(
        links
    )


def resource_group(
    item: str,
    catalog: dict,
    render_mode: str = "web",
) -> str:
    """
    Render één externe resourcegroep afhankelijk
    van de uitvoervorm.

    Website:
        alle links afzonderlijk weergeven.

    Module-PDF:
        wordt later vervangen door één QR-verwijzing
        naar de gegenereerde bronnenpagina.
    """

    if not item:
        return ""

    entry = _get_entry(
        item=item,
        catalog=catalog,
    )

    if entry.get(
        "type"
    ) != "group":
        raise RuntimeError(
            "Resource is geen groep:\n"
            f"  {item}"
        )

    if render_mode == "module_pdf":
        return (
            '<div class="pdf-resource-marker" '
            f'data-resource-id="{item}"></div>'
        )

    return _build_web_group(
        entry=entry,
    )
def resources_index(
    catalog: dict,
) -> str:
    """
    Bouw de centrale Resources-pagina uit resources.yml.

    Iedere resourcegroep krijgt:
    - een herkenbare titel;
    - een stabiele anchor;
    - de links uit de centrale catalogus.
    """

    sections = []

    for domain, groups in catalog.items():

        if not isinstance(
            groups,
            dict,
        ):
            continue

        for key, entry in groups.items():

            if not isinstance(
                entry,
                dict,
            ):
                continue

            if entry.get(
                "type"
            ) != "group":
                continue

            label = entry.get(
                "label",
                domain,
            )

            if (
                key.startswith("week")
                and key[4:].isdigit()
            ):
                title = (
                    f"{label} — "
                    f"Week {int(key[4:])}"
                )
            else:
                title = label

            anchor = (
                f"{domain}-{key}"
            )

            links = _build_web_group(
                entry=entry,
            )

            sections.append(
                f"## {title} "
                f"{{#{anchor}}}\n\n"
                f"{links}"
            )

    return "\n\n".join(
        sections
    )

def resource_page(
    item: str,
    catalog: dict,
) -> str:
    """
    Bouw één zelfstandige resourcepagina uit resources.yml.

    Bijvoorbeeld:

        w3schools.week3
    """

    entry = _get_entry(
        item=item,
        catalog=catalog,
    )

    if entry.get(
        "type"
    ) != "group":
        raise RuntimeError(
            "Resource is geen groep:\n"
            f"  {item}"
        )

    return _build_web_group(
        entry=entry,
    )

def get_resource_target_url(
    item: str,
    site_url: str,
    language: str = "nl",
) -> str:
    """
    Bouw de publieke URL van de zelfstandige
    resourcepagina.

    Bijvoorbeeld:

        w3schools.week3

    wordt voor Nederlands:

        https://jhenze-dev.github.io/Module01/
        nl/pdf-resources/03/w3schools/
    """

    base_url = site_url.rstrip("/")

    path = get_resource_page_path(
        item=item,
        language=language,
    ).lstrip("/")

    return f"{base_url}/{path}"

def get_resource_qr_data(
    item: str,
    catalog: dict,
    site_url: str,
    source_path: str | Path,
    language: str = "nl",
) -> dict:
    """
    Bouw de gegevens waarmee een QR-resource kan worden gemaakt.

    helpers.resources begrijpt de resourcecatalogus en bepaalt
    de publieke target-URL. De daadwerkelijke QrResource en
    QR-generatie blijven de verantwoordelijkheid van helpers.qr.
    """

    entry = _get_entry(
        item=item,
        catalog=catalog,
    )

    if entry.get(
        "type"
    ) != "group":
        raise RuntimeError(
            "Resource is geen groep:\n"
            f"  {item}"
        )

    label = entry.get(
        "label"
    )

    if not label:
        raise RuntimeError(
            "Resourcegroep heeft geen label:\n"
            f"  {item}"
        )

    return {
        "resource_id": item,
        "label": label,
        "target": get_resource_target_url(
            item=item,
            site_url=site_url,
            language=language,
        ),
        "source_path": Path(
            source_path
        ),
    }

