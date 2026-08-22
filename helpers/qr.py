from pathlib import Path
import hashlib
import re
from dataclasses import dataclass

import qrcode
import yaml
from qrcode.constants import ERROR_CORRECT_M

QR_MARKER_PATTERN = re.compile(
    r"<!--\s*"
    r"(qr)"
    r"\s*:\s*"
    r"([a-z0-9]+(?:[.-][a-z0-9-]+)*)"
    r"\s*-->",
    re.IGNORECASE,
)


@dataclass
class QrResource:
    resource_id: str
    resource_type: str
    label: str
    target: str
    source_path: Path
    source_line: int
    output_path: Path


def create_qr_resource(
    resource_id: str,
    label: str,
    target: str,
    source_path: str | Path,
    assets_root: str | Path,
) -> QrResource:
    """
    Maak een QrResource van reeds bekende resourcegegevens.

    Deze functie bepaalt geen resource-inhoud en genereert
    geen QR-code. De caller levert de ID, het label en de
    uiteindelijke target-URL aan.
    """

    source_path = Path(
        source_path
    )

    assets_root = Path(
        assets_root
    )

    return QrResource(
        resource_id=resource_id,
        resource_type="qr",
        label=label,
        target=target,
        source_path=source_path,
        source_line=0,
        output_path=(
            assets_root
            / "qr"
            / f"{resource_id}.png"
        ),
    )


def _extract_frontmatter(
    markdown: str,
    source_path: str | Path,
) -> dict:
    """
    Lees YAML-frontmatter uit een Markdown-bestand.

    Wanneer er geen frontmatter aanwezig is,
    wordt een lege dictionary teruggegeven.
    """

    source_path = Path(
        source_path
    )

    markdown = markdown.lstrip(
        "\ufeff"
    )

    lines = markdown.splitlines()

    if (
        not lines
        or lines[0].strip() != "---"
    ):
        return {}

    end_index = None

    for index in range(
        1,
        len(lines),
    ):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        raise RuntimeError(
            "Frontmatter is niet afgesloten:\n"
            f"  {source_path}"
        )

    frontmatter = "\n".join(
        lines[1:end_index]
    )

    data = yaml.safe_load(
        frontmatter
    )

    if data is None:
        return {}

    if not isinstance(
        data,
        dict,
    ):
        raise RuntimeError(
            "Ongeldige YAML-frontmatter:\n"
            f"  {source_path}"
        )

    return data


def extract_declared_resources(
    markdown: str,
    source_path: str | Path,
) -> set[str]:
    """
    Lees de resource-ID's uit de frontmatter.

    Voorbeeld:

        resources:
          - video.jellybeans
          - w3schools.week3
    """

    source_path = Path(
        source_path
    )

    frontmatter = _extract_frontmatter(
        markdown=markdown,
        source_path=source_path,
    )

    resources = frontmatter.get(
        "resources",
        [],
    )

    if resources is None:
        return set()

    if not isinstance(
        resources,
        list,
    ):
        raise RuntimeError(
            "'resources' moet een lijst zijn:\n"
            f"  {source_path}"
        )

    declared: set[str] = set()

    for resource_id in resources:

        if not isinstance(
            resource_id,
            str,
        ):
            raise RuntimeError(
                "Resource-ID in frontmatter moet tekst zijn:\n"
                f"  {source_path}"
            )

        normalized_id = (
            resource_id
            .strip()
            .lower()
        )

        if not normalized_id:
            raise RuntimeError(
                "Lege resource-ID in frontmatter:\n"
                f"  {source_path}"
            )

        declared.add(
            normalized_id
        )

    return declared


def normalize_qr_target(
    resource: QrResource,
) -> str:
    """
    Geef de URL terug die daadwerkelijk in de QR-code moet komen.

    YouTube-video's staan op de website als embed-URL.
    Voor een QR-code gebruiken we de normale watch-URL.
    Andere resources blijven ongewijzigd.
    """

    target = resource.target.strip()

    if "youtube.com/embed/" in target:
        video_id = (
            target
            .split("youtube.com/embed/", 1)[1]
            .split("?", 1)[0]
            .split("#", 1)[0]
            .strip("/")
        )

        if not video_id:
            raise RuntimeError(
                "YouTube-video-ID ontbreekt:\n"
                f"  ID: {resource.resource_id}\n"
                f"  Target: {resource.target}"
            )

        return (
            "https://www.youtube.com/"
            f"watch?v={video_id}"
        )

    return target


def qr_hash(
    resource: QrResource,
) -> str:
    """
    Bereken een SHA-256 hash van de QR-resource.

    Voor een directe QR bepaalt de target-URL de QR-inhoud.

    """

    source = (
        f"{resource.resource_type}\n"
        f"{resource.resource_id}\n"
        f"{resource.label}\n"
        f"{normalize_qr_target(resource)}"
    )

    return hashlib.sha256(
        source.encode("utf-8")
    ).hexdigest()


def _inventory_html_qr_resources(
    docs_root: Path,
    assets_root: Path,
) -> list[QrResource]:
    """
    Inventariseer directe QR-resources uit HTML-includes.

    Bedoeld voor video-resources met een marker zoals:

        <!-- qr: video.jellybeans -->

    gevolgd door een videoblok met een iframe.
    """

    resources: list[QrResource] = []

    for html_path in docs_root.rglob("*.html"):

        html = html_path.read_text(
            encoding="utf-8",
        )

        for match in QR_MARKER_PATTERN.finditer(
            html
        ):

            resource_type = (
                match.group(1)
                .lower()
            )

            if resource_type != "qr":
                continue

            resource_id = (
                match.group(2)
                .lower()
            )

            remainder = html[
                match.end():
            ]

            iframe_match = re.search(
                r'<iframe\b[^>]*\bsrc="([^"]+)"[^>]*\btitle="([^"]+)"',
                remainder,
                re.IGNORECASE,
            )

            if iframe_match is None:
                raise RuntimeError(
                    "QR-video marker wordt niet gevolgd door "
                    "een geldig iframe:\n"
                    f"  ID: {resource_id}\n"
                    f"  Bestand: {html_path}"
                )

            target = iframe_match.group(
                1
            ).strip()

            label = iframe_match.group(
                2
            ).strip()

            source_line = (
                html.count(
                    "\n",
                    0,
                    match.start(),
                )
                + 1
            )

            output_path = (
                assets_root
                / "qr"
                / f"{resource_id}.png"
            )

            resources.append(
                QrResource(
                    resource_id=resource_id,
                    resource_type=resource_type,
                    label=label,
                    target=target,
                    source_path=html_path,
                    source_line=source_line,
                    output_path=output_path,
                )
            )

    return resources


def inventory_qr_resources(
    docs_root: str | Path,
    assets_root: str | Path,
) -> list[QrResource]:
    """
    Inventariseer alle QR-resources in Markdown en HTML-includes.

    Markdown:
        - resources: uit frontmatter

    HTML-includes:
        - qr voor video's
    """

    docs_root = Path(
        docs_root
    )

    assets_root = Path(
        assets_root
    )

    resources: list[
        QrResource
    ] = []

    declared_resources: set[
        str
    ] = set()

    # ---------------------------------------------------------
    # 1. Alle gedeclareerde resources uit Markdown verzamelen
    # ---------------------------------------------------------

    markdown_files = list(
        docs_root.rglob("*.md")
    )

    for markdown_path in markdown_files:

        markdown = markdown_path.read_text(
            encoding="utf-8",
        )

        declared_resources.update(
            extract_declared_resources(
                markdown=markdown,
                source_path=markdown_path,
            )
        )


    # ---------------------------------------------------------
    # 2. qr video-resources uit HTML-includes inventariseren
    # ---------------------------------------------------------

    resources.extend(
        _inventory_html_qr_resources(
            docs_root=docs_root,
            assets_root=assets_root,
        )
    )

    # ---------------------------------------------------------
    # 3. Valideren tegen frontmatter resources
    # ---------------------------------------------------------

    for resource in resources:

        if resource.resource_id not in declared_resources:
            raise RuntimeError(
                "\nQR-resource ontbreekt in frontmatter "
                "'resources':\n"
                f"  ID: {resource.resource_id}\n"
                f"  Bestand: {resource.source_path}\n"
                f"  Regel: {resource.source_line}"
            )

    return resources


def validate_qr_resources(
    resources: list[QrResource],
) -> None:
    """
    Valideer alle QR-resources vóór generatie.

    Dezelfde resource-ID mag meerdere keren voorkomen
    wanneer label en target gelijk zijn.
    """

    seen: dict[
        str,
        QrResource,
    ] = {}

    for resource in resources:

        if resource.resource_type != "qr":
            raise RuntimeError(
                "\nOnbekend QR-resource-type:\n"
                f"  ID: {resource.resource_id}\n"
                f"  Type: {resource.resource_type}\n"
                f"  Bestand: {resource.source_path}"
            )

        previous = seen.get(
            resource.resource_id
        )

        if previous is None:
            seen[
                resource.resource_id
            ] = resource
            continue

        if (
            previous.target
            != resource.target
            or previous.label
            != resource.label
        ):
            raise RuntimeError(
                "\nQR-resource-ID wordt gebruikt voor "
                "verschillende resources:\n"
                f"  ID: {resource.resource_id}\n"
                f"  Eerste bestand: "
                f"{previous.source_path}\n"
                f"  Tweede bestand: "
                f"{resource.source_path}"
            )


def _unique_resources(
    resources: list[QrResource],
) -> list[QrResource]:
    """
    Verwijder dubbele QR-resources op basis van resource-ID.
    """

    unique: list[
        QrResource
    ] = []

    seen: set[
        str
    ] = set()

    for resource in resources:

        if resource.resource_id in seen:
            continue

        seen.add(
            resource.resource_id
        )

        unique.append(
            resource
        )

    return unique


def _direct_resources(
    resources: list[QrResource],
) -> list[QrResource]:
    """
    Geef de resources terug waarvoor een QR-PNG nodig is.
    """

    return [
        resource
        for resource in resources
        if resource.resource_type == "qr"
    ]


def _load_manifest(
    manifest_path: Path,
) -> dict:
    """
    Lees het bestaande QR-manifest.

    Wanneer het manifest nog niet bestaat,
    wordt een lege structuur teruggegeven.
    """

    if not manifest_path.exists():
        return {}

    with manifest_path.open(
        "r",
        encoding="utf-8",
    ) as file:

        data = yaml.safe_load(
            file
        )

    if not isinstance(
        data,
        dict,
    ):
        return {}

    return data


def _write_manifest(
    manifest_path: Path,
    resources: list[QrResource],
) -> None:
    """
    Schrijf het QR-manifest opnieuw op basis
    van de actuele resource-inventory.
    """

    manifest: dict = {
        "direct": {},
    }

    for resource in resources:

        manifest[
            "direct"
        ][
            resource.resource_id
        ] = {
            "type": resource.resource_type,
            "hash": qr_hash(
                resource
            ),
            "file": (
                f"{resource.resource_id}.png"
            ),
            "label": resource.label,
            "target": resource.target,
            "qr_target": normalize_qr_target(
                resource
            ),
        }

    manifest_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with manifest_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        yaml.safe_dump(
            manifest,
            file,
            sort_keys=True,
            allow_unicode=True,
        )


def _needs_render(
    resource: QrResource,
    manifest: dict,
) -> bool:
    """
    Bepaal of een directe QR-code opnieuw gegenereerd moet worden.

    Render wanneer:

    - de PNG niet bestaat;
    - de ID niet in het manifest staat;
    - de opgeslagen hash niet overeenkomt.
    """

    if not resource.output_path.exists():
        return True

    direct = manifest.get(
        "direct"
    )

    if not isinstance(
        direct,
        dict,
    ):
        return True

    entry = direct.get(
        resource.resource_id
    )

    if not isinstance(
        entry,
        dict,
    ):
        return True

    old_hash = entry.get(
        "hash"
    )

    return (
        old_hash
        != qr_hash(
            resource
        )
    )


def _remove_obsolete_assets(
    resources: list[QrResource],
    manifest: dict,
    assets_root: Path,
) -> int:
    """
    Verwijder directe QR-PNG's die nog in het oude manifest staan
    maar niet meer in de actuele Markdown voorkomen.
    """

    current_ids = {
        resource.resource_id
        for resource in resources
    }

    direct = manifest.get(
        "direct"
    )

    if not isinstance(
        direct,
        dict,
    ):
        return 0

    removed = 0

    for resource_id in direct:

        if resource_id in current_ids:
            continue

        obsolete_path = (
            assets_root
            / "qr"
            / f"{resource_id}.png"
        )

        if obsolete_path.exists():

            obsolete_path.unlink()

            removed += 1

    return removed


def generate_qr(
    url: str,
    output_path: str | Path,
) -> Path:
    """
    Genereer één kale QR-code als PNG.

    Opmaak, labels en positionering worden door HTML/CSS geregeld.
    """

    output_path = Path(
        output_path
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(
        url
    )

    qr.make(
        fit=True
    )

    image = qr.make_image(
        fill_color="black",
        back_color="white",
    )

    with output_path.open(
        "wb"
    ) as file:

        image.save(
            file
        )

    return output_path


def render_qr_resources(
    resources: list[QrResource],
) -> list[Path]:
    """
    Render alle opgegeven directe QR-resources.
    """

    if not resources:
        return []

    generated: list[
        Path
    ] = []

    for resource in resources:

        generate_qr(
            url=normalize_qr_target(
                resource
            ),
            output_path=resource.output_path,
        )

        generated.append(
            resource.output_path
        )

    print(
        f"QR: {len(generated)} "
        "afbeeldingen bijgewerkt."
    )

    return generated


def build_qr_assets(
    resources: list[QrResource],
    assets_root: str | Path,
) -> list[Path]:
    """
    Bouw QR-assets uit een reeds samengestelde resource-inventory.

    De herkomst van de resources is hierbij niet relevant.
    Daardoor kunnen Markdown/HTML-resources en extern
    samengestelde resources dezelfde QR-pipeline gebruiken.
    """

    assets_root = Path(
        assets_root
    )

    manifest_path = (
        assets_root
        / "qr"
        / "manifest.yml"
    )

    print(
        f"QR: {len(resources)} "
        "resource-verwijzingen gevonden."
    )

    validate_qr_resources(
        resources
    )

    unique_resources = _unique_resources(
        resources
    )

    direct_resources = _direct_resources(
        unique_resources
    )

    manifest = _load_manifest(
        manifest_path
    )

    render_resources = [
        resource
        for resource in direct_resources
        if _needs_render(
            resource,
            manifest,
        )
    ]

    unchanged = (
        len(direct_resources)
        - len(render_resources)
    )

    print(
        f"QR: {unchanged} "
        "directe resources ongewijzigd."
    )

    print(
        f"QR: {len(render_resources)} "
        "afbeeldingen te genereren."
    )

    generated = render_qr_resources(
        render_resources
    )

    removed = _remove_obsolete_assets(
        resources=unique_resources,
        manifest=manifest,
        assets_root=assets_root,
    )

    if removed:
        print(
            f"QR: {removed} "
            "verouderde afbeeldingen verwijderd."
        )

    _write_manifest(
        manifest_path=manifest_path,
        resources=unique_resources,
    )

    print(
        "QR: gereed."
    )

    return generated
