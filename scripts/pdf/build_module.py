from pathlib import Path
import os
import subprocess
import sys
import tempfile

import yaml
from bs4 import BeautifulSoup
from bs4.element import Tag
from jinja2 import Environment, FileSystemLoader
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


from helpers.qr import (
    build_qr_assets,
    create_qr_resource,
    inventory_qr_resources,
    normalize_qr_target,
)

from helpers.mermaid import (
    replace_mermaid_blocks_for_pdf,
)

from helpers.resources import (
    get_resource_qr_data,
)


BUILD_DIR = ROOT / "build"
ASSETS_DIR = BUILD_DIR / "assets"
PDF_OUTPUT_ROOT = BUILD_DIR / "pdf"

OUTPUT_DIR = PDF_OUTPUT_ROOT
PDF_MKDOCS_DIR = OUTPUT_DIR / "mkdocs"

TEMPLATE_DIR = ROOT / "render" / "pdf" / "module"
MODULE_TEMPLATE = "module.html"

PDF_RENDERER = (
    ROOT
    / "scripts"
    / "pdf"
    / "render_pdf.mjs"
)


def build_mkdocs():
    """
    Bouw een afzonderlijke MkDocs-weergave voor de Module-PDF.

    De normale website blijft staan in:

        site/

    De PDF-weergave wordt gebouwd in:

        build/pdf/mkdocs/

    Daardoor overschrijft een PDF-build de normale website nooit.
    """

    env = os.environ.copy()
    env["RENDER_MODE"] = "module_pdf"

    PDF_MKDOCS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    subprocess.run(
        [
            "mkdocs",
            "build",
            "--site-dir",
            str(PDF_MKDOCS_DIR),
        ],
        cwd=ROOT,
        env=env,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

def _load_main_content(path: Path) -> Tag:
    """
    Laad alleen de daadwerkelijke inhoud van een door MkDocs
    gebouwde pagina.
    """

    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    content = soup.select_one("article.md-content__inner")

    if not isinstance(content, Tag):
        raise RuntimeError(
            f"Geen MkDocs content gevonden in: {path}"
        )

    return content


def _classes(element: Tag) -> list[str]:
    """
    Geef de CSS-classes van een BeautifulSoup Tag altijd
    terug als een gewone lijst strings.

    Tags die eerder met decompose() zijn verwijderd kunnen
    geen attrs meer hebben. In dat geval behandelen we ze
    alsof ze geen classes hebben.
    """

    if element.attrs is None:
        return []

    value = element.get("class")

    if value is None:
        return []

    if isinstance(value, str):
        return [value]

    return [str(item) for item in value]


def _has_class_fragment(
    element: Tag,
    fragment: str,
) -> bool:
    """
    Controleer of een element een CSS-class bevat waarin
    fragment voorkomt.
    """

    return any(
        fragment in class_name
        for class_name in _classes(element)
    )


def transform_pdf_hints(
    html: str,
) -> str:
    """
    Zet uitklapbare web-hints om naar altijd zichtbare
    hintblokken voor de Module-PDF.
    """

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    hints = soup.select(
        "details.hint"
    )

    for hint in hints:

        summary = hint.find(
            "summary"
        )

        if not isinstance(
            summary,
            Tag,
        ):
            continue

        hint_block = soup.new_tag(
            "div",
            attrs={
                "class": "pdf-hint",
            },
        )

        hint_title = soup.new_tag(
            "div",
            attrs={
                "class": "pdf-hint-title",
            },
        )

        hint_title.string = summary.get_text(
            " ",
            strip=True,
        )

        hint_block.append(
            hint_title
        )

        for child in list(
            hint.contents
        ):

            if child is summary:
                continue

            hint_block.append(
                child.extract()
            )

        hint.replace_with(
            hint_block
        )

    return soup.decode_contents()


def extract_content(path: Path) -> str:
    language = os.environ.get(
        "LANGUAGE",
        "nl",
    ).strip().lower()

    """
    Generieke extractor.

    Voor onderdelen die voorlopig volledig in de
    PDF-compositie mogen worden opgenomen.

    Mermaid-diagrammen worden vervangen door de
    bestaande gedeelde PNG-assets.
    """

    content = _load_main_content(path)

    html = content.decode_contents()

    html = transform_pdf_hints(
        html
    )

    return replace_mermaid_blocks_for_pdf(
        html=html,
        docs_root=ROOT / "docs" / language,
        assets_root=ASSETS_DIR,
        pdf_output_dir=OUTPUT_DIR,
    )


def extract_week_opening(
    path: Path,
    video: dict | None = None,
) -> str:
    """
    Bouw de weekopening voor de Module-PDF.

    We nemen uit de weekindex mee:

    - de H1 van de week;
    - de badge-regel.

    Het bestaande web-video-blok wordt NIET overgenomen.

    Wanneer videodata beschikbaar is, bouwen we voor de PDF
    een apart videoblok met:

    - videotitel;
    - YouTube-thumbnail;
    - QR-code;
    - korte type- en labeltekst.

    De uiteindelijke vormgeving wordt volledig door PDF-CSS
    bepaald.
    """

    content = _load_main_content(path)

    week_page = content.select_one(
        ".module-page.week-page"
    )

    if not isinstance(week_page, Tag):
        raise RuntimeError(
            f"Geen .module-page.week-page gevonden in: {path}"
        )

    output_soup = BeautifulSoup(
        "",
        "html.parser",
    )

    result = output_soup.new_tag("div")

    # ---------------------------------------------------------
    # 1. Weektitel
    # ---------------------------------------------------------

    title = week_page.find("h1")

    if isinstance(title, Tag):
        result.append(title)

    # ---------------------------------------------------------
    # 2. Badge-regel
    # ---------------------------------------------------------

    badge_paragraph = None

    for paragraph in week_page.find_all(
        "p",
        recursive=False,
    ):
        if not isinstance(paragraph, Tag):
            continue

        if paragraph.find(
            class_=lambda value: (
                isinstance(value, str)
                and "badge" in value
            )
        ):
            badge_paragraph = paragraph
            break

    if isinstance(badge_paragraph, Tag):
        result.append(badge_paragraph)

    # ---------------------------------------------------------
    # 3. PDF-video
    # ---------------------------------------------------------

    if video is not None:

        video_block = output_soup.new_tag(
            "div",
            attrs={
                "class": "pdf-video",
            },
        )

        # Titel
        video_title = output_soup.new_tag(
            "div",
            attrs={
                "class": "pdf-video__title",
            },
        )

        video_title.string = str(
            video["title"]
        )

        video_block.append(video_title)

        # Container voor thumbnail + QR
        video_content = output_soup.new_tag(
            "div",
            attrs={
                "class": "pdf-video__content",
            },
        )

        # Thumbnail
        thumbnail = output_soup.new_tag(
            "img",
            attrs={
                "class": "pdf-video__thumbnail",
                "src": str(
                    video["thumbnail_url"]
                ),
                "alt": str(
                    video["title"]
                ),
            },
        )

        video_content.append(thumbnail)

        # QR-blok
        qr_block = output_soup.new_tag(
            "div",
            attrs={
                "class": "pdf-video__qr",
            },
        )

        qr_type = output_soup.new_tag(
            "div",
            attrs={
                "class": "pdf-video__qr-type",
            },
        )

        qr_type.string = "VIDEO"

        qr_block.append(qr_type)

        qr_image = output_soup.new_tag(
            "img",
            attrs={
                "class": "pdf-video__qr-code",
                "src": str(
                    video["qr_path"]
                ),
                "alt": (
                    "QR-code naar de video"
                ),
            },
        )

        qr_block.append(qr_image)

        qr_label = output_soup.new_tag(
            "div",
            attrs={
                "class": "pdf-video__qr-label",
            },
        )

        qr_label.string = str(
            video["label"]
        )

        qr_block.append(qr_label)

        video_content.append(qr_block)

        video_block.append(video_content)

        result.append(video_block)

    return result.decode_contents()


def extract_tset(path: Path) -> str:
    language = os.environ.get(
        "LANGUAGE",
        "nl",
    ).strip().lower()

    """
    Haal de Thinking Set op voor de Module-PDF.

    De volledige TSET blijft voorlopig behouden, behalve
    de badges.

    De relevante badges zijn namelijk al zichtbaar in de
    weekopening.
    """

    content = _load_main_content(path)

    # Eerst alleen de bovenliggende badge-elementen verzamelen.
    # Daarna pas verwijderen. Zo lopen we niet opnieuw door
    # children van reeds gedecomponeerde Tags.
    badge_elements: list[Tag] = []

    for element in content.find_all(True):

        if not isinstance(element, Tag):
            continue

        if _has_class_fragment(
            element,
            "badge",
        ):

            # Als een bovenliggende badge al geselecteerd is,
            # hoeft een child niet nogmaals verwijderd te worden.
            has_badge_parent = False

            for parent in element.parents:

                if not isinstance(parent, Tag):
                    continue

                if parent in badge_elements:
                    has_badge_parent = True
                    break

            if not has_badge_parent:
                badge_elements.append(
                    element
                )

    for element in badge_elements:

        if element.attrs is not None:
            element.decompose()

    html = content.decode_contents()

    return replace_mermaid_blocks_for_pdf(
        html=html,
        docs_root=ROOT / "docs" / language,
        assets_root=ASSETS_DIR,
        pdf_output_dir=OUTPUT_DIR,
    )


def _load_page_frontmatter(
    markdown_path: Path,
) -> dict:
    """
    Lees de YAML-frontmatter van een Markdown-pagina.
    """

    markdown = markdown_path.read_text(
        encoding="utf-8"
    )

    markdown = markdown.lstrip(
        "\ufeff"
    )

    if not markdown.startswith("---"):
        return {}

    parts = markdown.split(
        "---",
        2,
    )

    if len(parts) < 3:
        raise RuntimeError(
            "Frontmatter is niet afgesloten:\n"
            f"  {markdown_path}"
        )

    data = yaml.safe_load(
        parts[1]
    )

    if data is None:
        return {}

    if not isinstance(
        data,
        dict,
    ):
        raise RuntimeError(
            "Ongeldige frontmatter:\n"
            f"  {markdown_path}"
        )

    return data


def load_resource_build_config() -> tuple[dict, str]:
    """
    Laad de resourcecatalogus en publieke site-URL
    die nodig zijn voor PDF-resource-QR's.
    """

    resources_path = (
        ROOT
        / "docs"
        / "data"
        / "general-resources.yml"
    )

    mkdocs_path = (
        ROOT
        / "mkdocs.yml"
    )

    with resources_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        resources_catalog = yaml.safe_load(
            file
        )

    if not isinstance(
        resources_catalog,
        dict,
    ):
        raise RuntimeError(
            "Ongeldige resourcecatalogus:\n"
            f"  {resources_path}"
        )

    site_url = None

    for line in mkdocs_path.read_text(
        encoding="utf-8"
    ).splitlines():

        stripped = line.strip()

        if not stripped.startswith(
            "site_url:"
        ):
            continue

        site_url = stripped.split(
            ":",
            1,
        )[1].strip()

        break

    if not site_url:
        raise RuntimeError(
            "'site_url' ontbreekt in:\n"
            f"  {mkdocs_path}"
        )

    return (
        resources_catalog,
        site_url.strip(),
    )


def _youtube_id_from_resource(
    resource,
) -> str:
    """
    Haal de YouTube-video-ID uit de genormaliseerde QR-target.
    """

    qr_target = normalize_qr_target(
        resource
    )

    marker = "watch?v="

    if marker not in qr_target:
        raise RuntimeError(
            "Video-resource heeft geen ondersteunde "
            "YouTube watch-URL:\n"
            f"  {resource.resource_id}\n"
            f"  {qr_target}"
        )

    return (
        qr_target
        .split(marker, 1)[1]
        .split("&", 1)[0]
    )


def build_video_resource(
    resource_id: str,
    resources: list,
) -> dict:
    """
    Bouw de PDF-data voor één video-resource.

    De resource zelf komt volledig uit de centrale QR-inventory.
    """

    matches = [
        resource
        for resource in resources
        if (
            resource.resource_id == resource_id
            and resource.resource_type == "qr"
        )
    ]

    if not matches:
        raise RuntimeError(
            "Video-resource ontbreekt in QR-inventory:\n"
            f"  {resource_id}"
        )

    resource = matches[0]

    video_qr_asset = resource.output_path

    video_qr_path = Path(
        os.path.relpath(
            video_qr_asset,
            OUTPUT_DIR,
        )
    ).as_posix()

    youtube_id = _youtube_id_from_resource(
        resource
    )

    return {
        "resource_id": resource.resource_id,
        "title": resource.label,
        "label": resource.label,
        "thumbnail_url": (
            "https://img.youtube.com/vi/"
            f"{youtube_id}/maxresdefault.jpg"
        ),
        "qr_path": video_qr_path,
    }


def get_week_video(
    week_number: int,
    resources: list,
) -> dict | None:
    """
    Bepaal automatisch of een week een video-resource gebruikt.

    De weekpagina declareert resources in de frontmatter.
    Er staat geen week-specifieke resource-ID in deze builder.
    """

    week_key = f"{week_number:02d}"

    markdown_path = (
        ROOT
        / "docs"
        / "nl"
        / "weeks"
        / week_key
        / "index.md"
    )

    if not markdown_path.exists():
        return None

    frontmatter = _load_page_frontmatter(
        markdown_path
    )

    declared = frontmatter.get(
        "resources",
        [],
    )

    if declared is None:
        return None

    if not isinstance(
        declared,
        list,
    ):
        raise RuntimeError(
            "'resources' moet een lijst zijn:\n"
            f"  {markdown_path}"
        )

    video_ids: list[str] = []

    for resource_id in declared:

        if not isinstance(
            resource_id,
            str,
        ):
            continue

        resource_id = resource_id.strip().lower()

        for resource in resources:
            if (
                resource.resource_id == resource_id
                and resource.resource_type == "qr"
                and resource_id.startswith("video.")
            ):
                video_ids.append(
                    resource_id
                )
                break

    if not video_ids:
        return None

    if len(video_ids) > 1:
        raise RuntimeError(
            "Meer dan één video-resource op een weekpagina "
            "wordt nog niet ondersteund:\n"
            f"  week: {week_number}\n"
            f"  resources: {video_ids}"
        )

    return build_video_resource(
        resource_id=video_ids[0],
        resources=resources,
    )


def get_pset_resource_ids(
    week_number: int,
) -> list[str]:
    """
    Lees de gedeclareerde resources uit de PSET-index
    van een week.
    """

    week_key = f"{week_number:02d}"

    markdown_path = (
        ROOT
        / "docs"
        / "nl"
        / "psets"
        / week_key
        / "index.md"
    )

    if not markdown_path.exists():
        return []

    frontmatter = _load_page_frontmatter(
        markdown_path
    )

    declared = frontmatter.get(
        "resources",
        [],
    )

    if declared is None:
        return []

    if not isinstance(
        declared,
        list,
    ):
        raise RuntimeError(
            "'resources' moet een lijst zijn:\n"
            f"  {markdown_path}"
        )

    resource_ids: list[str] = []

    for resource_id in declared:

        if not isinstance(
            resource_id,
            str,
        ):
            continue

        normalized_id = (
            resource_id
            .strip()
            .lower()
        )

        if normalized_id:
            resource_ids.append(
                normalized_id
            )

    return resource_ids


def build_pset_qr_resources(
    week_number: int,
    resources_catalog: dict,
    site_url: str,
) -> list:
    """
    Bouw QR-resources voor de externe resources
    die in de PSET-index van een week zijn gedeclareerd.
    """

    resource_ids = get_pset_resource_ids(
        week_number=week_number,
    )

    qr_resources = []

    for resource_id in resource_ids:

        qr_data = get_resource_qr_data(
            item=resource_id,
            catalog=resources_catalog,
            site_url=site_url,
            source_path=(
                ROOT
                / "docs"
                / "nl"
                / "psets"
                / f"{week_number:02d}"
                / "index.md"
            ),
        )

        qr_resources.append(
            create_qr_resource(
                resource_id=qr_data[
                    "resource_id"
                ],
                label=qr_data[
                    "label"
                ],
                target=qr_data[
                    "target"
                ],
                source_path=qr_data[
                    "source_path"
                ],
                assets_root=ASSETS_DIR,
            )
        )

    return qr_resources


def _find_single_tset(
    week_key: str,
) -> Path | None:
    """
    Zoek de gebouwde Thinking Set van een week.
    """

    week_dir = (
        PDF_MKDOCS_DIR
        / "nl"
        / "tsets"
        / week_key
    )

    if not week_dir.exists():
        return None

    candidates = sorted(
        path
        for path in week_dir.glob(
            "*/index.html"
        )
        if path.is_file()
    )

    if not candidates:
        return None

    if len(candidates) > 1:
        raise RuntimeError(
            "Meer dan één Thinking Set gevonden voor week "
            f"{week_key}:\n"
            + "\n".join(
                f"  {path}"
                for path in candidates
            )
        )

    return candidates[0]


def _find_psets(
    week_key: str,
) -> list[dict]:
    """
    Verzamel alle gebouwde PSET-pagina's van een week.

    Er worden geen concrete PSET-namen in Python hardcoded.
    """

    week_dir = (
        PDF_MKDOCS_DIR
        / "nl"
        / "psets"
        / week_key
    )

    if not week_dir.exists():
        return []

    psets: list[dict] = []

    for path in sorted(
        week_dir.glob(
            "*/index.html"
        )
    ):
        slug = path.parent.name

        if slug.endswith("-less"):
            variant = "less"
        elif slug.endswith("-more"):
            variant = "more"
        else:
            variant = slug

        psets.append(
            {
                "variant": variant,
                "slug": slug,
                "html": extract_content(
                    path
                ),
            }
        )

    return psets


def rewrite_pset_index_links(
    html: str,
    week_number: int,
    psets: list[dict],
) -> str:
    """
    Herschrijf in de Module-PDF alleen links naar PSETs van deze week
    naar de stabiele interne PDF-ankers.

    Andere links in de PSET-index blijven ongewijzigd.
    """

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    pset_slugs = {
        str(pset["slug"])
        for pset in psets
        if "slug" in pset
    }

    for link in soup.find_all("a", href=True):
        if not isinstance(link, Tag):
            continue

        href = str(link.get("href", ""))
        slug = href.rstrip("/")

        if slug not in pset_slugs:
            continue

        target_id = (
            f"pset-{week_number:02d}-{slug}"
        )

        link["href"] = f"#{target_id}"

        link["class"] = (
            "pdf-pset-choice-title"
        )

        strong = link.find_next_sibling(
            "strong"
        )

        if strong is not None:
            strong["class"] = (
                "pdf-pset-choice-variant"
            )

        page_reference = soup.new_tag(
            "span"
        )
        page_reference["class"] = (
            "pdf-page-reference"
        )
        page_reference["data-pdf-target"] = (
            target_id
        )
        page_reference.string = " p. 000"

        if strong is not None:
            strong.insert_after(
                page_reference
            )
        else:
            link.insert_after(
                page_reference
            )

    return soup.decode_contents()


def replace_resource_markers(
    html: str,
    resources: list,
) -> str:
    """
    Vervang PDF-resource-markers door het bijbehorende
    QR-blok.

    De marker bevat alleen de resource-ID.
    De QR-resource zelf komt uit de centrale QR-inventory.
    """

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    markers = soup.select(
        ".pdf-resource-marker[data-resource-id]"
    )

    for marker in markers:

        resource_id = marker.get(
            "data-resource-id"
        )

        if not resource_id:
            continue

        matches = [
            resource
            for resource in resources
            if (
                resource.resource_id
                == resource_id
                and resource.resource_type
                == "qr"
            )
        ]

        if not matches:
            raise RuntimeError(
                "PDF-resource ontbreekt in QR-inventory:\n"
                f"  {resource_id}"
            )

        resource = matches[0]

        qr_path = Path(
            os.path.relpath(
                resource.output_path,
                OUTPUT_DIR,
            )
        ).as_posix()

        qr_block = soup.new_tag(
            "div",
            attrs={
                "class": "pdf-resource",
            },
        )

        qr_image = soup.new_tag(
            "img",
            attrs={
                "class": "pdf-resource__qr-code",
                "src": qr_path,
                "alt": (
                    f"QR-code naar {resource.label}"
                ),
            },
        )

        qr_block.append(
            qr_image
        )

        marker.replace_with(
            qr_block
        )

    return soup.decode_contents()


def build_week(
    week_number: int,
    resources: list,
) -> dict:
    """
    Bouw één week generiek uit de Module-PDF MkDocs-weergave.

    De functie bevat geen week-specifieke titels, TSET-namen,
    PSET-namen of resource-ID's.
    """

    week_key = f"{week_number:02d}"

    week_index = (
        PDF_MKDOCS_DIR
        / "nl"
        / "weeks"
        / week_key
        / "index.html"
    )

    if not week_index.exists():
        raise RuntimeError(
            "Weekpagina ontbreekt in Module-PDF MkDocs-build:\n"
            f"  {week_index}"
        )

    video = get_week_video(
        week_number=week_number,
        resources=resources,
    )

    tset_path = _find_single_tset(
        week_key
    )

    tset_slug = (
        tset_path.parent.name
        if tset_path is not None
        else None
    )

    pset_index_path = (
        PDF_MKDOCS_DIR
        / "nl"
        / "psets"
        / week_key
        / "index.html"
    )

    psets = _find_psets(
        week_key
    )

    return {
        "number": week_number,
        "tset_slug": tset_slug,
        "video": video,
        "week_intro_html": extract_week_opening(
            week_index,
            video=video,
        ),
        "tset_html": (
            extract_tset(
                tset_path
            )
            if tset_path is not None
            else ""
        ),
        "pset_index_html": (
            replace_resource_markers(
                html=rewrite_pset_index_links(
                    html=extract_content(
                        pset_index_path
                    ),
                    week_number=week_number,
                    psets=psets,
                ),
                resources=resources,
            )
            if pset_index_path.exists()
            else ""
        ),
        "psets": psets,
    }


def discover_week_numbers() -> list[int]:
    """
    Ontdek automatisch welke weken in de Module-PDF MkDocs-build bestaan.
    """

    weeks_dir = (
        PDF_MKDOCS_DIR
        / "nl"
        / "weeks"
    )

    if not weeks_dir.exists():
        return []

    week_numbers: list[int] = []

    for path in weeks_dir.iterdir():

        if (
            not path.is_dir()
            or not path.name.isdigit()
        ):
            continue

        if (
            path
            / "index.html"
        ).exists():

            week_numbers.append(
                int(path.name)
            )

    return sorted(
        week_numbers
    )


def build_understanding() -> list[dict]:
    """
    Verzamel de centrale Understanding-content voor de Module-PDF.

    De volgorde en selectie worden bepaald door understanding.yml.
    De content wordt gelezen uit de gerenderde MkDocs-PDF-build.
    """

    understanding_path = (
        ROOT
        / "docs"
        / "data"
        / "understanding.yml"
    )

    if not understanding_path.exists():
        raise RuntimeError(
            "Understanding-catalogus ontbreekt:\n"
            f"  {understanding_path}"
        )

    with understanding_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        catalog = yaml.safe_load(file)

    if not isinstance(catalog, dict):
        raise RuntimeError(
            "Understanding-catalogus heeft een "
            "ongeldige structuur."
        )

    entries: list[dict] = []

    for domain_entries in catalog.values():

        if not isinstance(
            domain_entries,
            dict,
        ):
            continue

        for entry in domain_entries.values():

            if not isinstance(
                entry,
                dict,
            ):
                continue

            item_id = entry.get("id")
            source = entry.get("source")
            title = entry.get("title")

            if not item_id or not source or not title:
                raise RuntimeError(
                    "Onvolledige Understanding-entry:\n"
                    f"  {entry}"
                )

            source_path = Path(source)

            parts = list(
                source_path.parts
            )

            if "_content" not in parts:
                raise RuntimeError(
                    "Understanding-source bevat geen "
                    f"'_content'-map: {source}"
                )

            parts.remove("_content")

            rendered_path = (
                PDF_MKDOCS_DIR
                / Path(*parts).with_suffix("")
                / "index.html"
            )

            if not rendered_path.exists():
                raise RuntimeError(
                    "Gerenderde Understanding-pagina "
                    "ontbreekt:\n"
                    f"  {rendered_path}\n"
                    f"  Bron: {source}"
                )

            content = extract_content(
                rendered_path
            )

            entries.append(
                {
                    "id": item_id,
                    "title": title,
                    "html": content,
                }
            )

    return entries


def build_weeks(
    resources: list,
) -> list[dict]:
    language = os.environ.get(
        "LANGUAGE",
        "nl",
    ).strip().lower()
    """
    Bouw alle beschikbare weken zonder week-specifieke Python-code.
    """

    week_numbers = discover_week_numbers()

    if not week_numbers:
        raise RuntimeError(
            "Geen weken gevonden in de Module-PDF MkDocs-build:\n"
            f"  {PDF_MKDOCS_DIR / language / 'weeks'}"
        )

    return [
        build_week(
            week_number=week_number,
            resources=resources,
        )
        for week_number in week_numbers
    ]

def render_module(
    weeks: list[dict],
) -> str:
    """
    Vul render/pdf/module/module.html met de verzamelde
    HTML-fragmenten.
    """

    environment = Environment(
        loader=FileSystemLoader(
            TEMPLATE_DIR
        ),
        autoescape=False,
    )

    template = environment.get_template(
        MODULE_TEMPLATE
    )

    return template.render(
        document_title="Module 01",
        weeks=weeks,
        understanding=build_understanding(),
        pdf_css="mkdocs/assets/css/badges.css",
    )


def read_pdf_page_map(
    pdf_path: Path,
) -> dict[str, int]:
    """
    Lees de named destinations uit een gerenderde PDF.

    De PDF gebruikt intern nul-gebaseerde pagina-indexen.
    Voor leerlingzichtbare paginanummers tellen we vanaf 1.
    """

    reader = PdfReader(
        str(pdf_path)
    )

    page_map: dict[str, int] = {}

    for name, destination in reader.named_destinations.items():
        clean_name = str(name).lstrip("/")

        page_index = reader.get_destination_page_number(
            destination
        )

        if page_index is None:
            continue

        page_map[clean_name] = page_index + 1

    return page_map


def read_understanding_page_map(
    pdf_path: Path,
) -> dict[str, int]:
    """
    Zoek de tijdelijke Understanding-markers in de gerenderde PDF
    en bepaal op welke pagina ieder Understanding-item begint.
    """

    reader = PdfReader(
        str(pdf_path)
    )

    page_map: dict[str, int] = {}

    marker_prefix = "UNDERSTANDING-"

    for page_index, page in enumerate(
        reader.pages
    ):
        text = page.extract_text() or ""

        for line in text.splitlines():

            if marker_prefix not in line:
                continue

            marker_start = line.find(
                marker_prefix
            )

            marker = line[
                marker_start:
            ].strip()

            item_id = marker[
                len(marker_prefix):
            ]

            if item_id.startswith(
                (
                    "python.",
                    "visual-first.",
                )
            ):
                page_map[item_id] = (
                    page_index + 1
                )

    return page_map


def write_understanding_page_map(
    page_map: dict[str, int],
) -> None:
    """
    Schrijf de actuele PDF-paginamap van de centrale
    Understanding-sectie naar understanding-pages.yml.
    """

    language = os.environ.get(
        "LANGUAGE",
        "nl",
    ).strip().lower()

    if language not in {"nl", "en"}:
        raise RuntimeError(
            f"Ongeldige LANGUAGE: {language}"
        )

    output_path = (
        ROOT
        / "docs"
        / "data"
        / "generated"
        / language
        / "understanding-pages.yml"
    )

    understanding_pages: dict[str, dict[str, int]] = {}

    for target_id, page_number in page_map.items():

        if not target_id.startswith(
            (
                "python.",
                "visual-first.",
            )
        ):
            continue

        understanding_pages[target_id] = {
            "page": page_number,
        }

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as file:
        yaml.safe_dump(
            understanding_pages,
            file,
            allow_unicode=True,
            sort_keys=False,
        )


def apply_pdf_page_map(
    html_path: Path,
    page_map: dict[str, int],
) -> None:
    """
    Vul de leerlingzichtbare paginaverwijzingen in
    op basis van de eerste PDF-render.
    """

    html = html_path.read_text(
        encoding="utf-8"
    )

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    references = soup.select(
        ".pdf-page-reference[data-pdf-target]"
    )

    for reference in references:

        target_id = reference.get(
            "data-pdf-target"
        )

        if not target_id:
            continue

        page_number = page_map.get(
            str(target_id)
        )

        if page_number is None:
            raise RuntimeError(
                "PDF-paginaverwijzing heeft geen "
                "gevonden doelpagina:\n"
                f"  {target_id}"
            )

        reference.string = (
            f" p. {page_number}"
        )

    html_path.write_text(
        str(soup),
        encoding="utf-8",
    )


def render_pdf(
    html_path: Path,
    pdf_path: Path,
) -> None:
    """
    Render de samengestelde Module-HTML naar PDF via Puppeteer.
    """

    subprocess.run(
        [
            "node",
            str(PDF_RENDERER),
            str(html_path),
            str(pdf_path),
        ],
        cwd=ROOT,
        check=True,
    )


def build_module(verbose: bool = False) -> Path:
    global OUTPUT_DIR, PDF_MKDOCS_DIR

    language = os.environ.get(
        "LANGUAGE",
        "nl",
    ).strip().lower()

    if language not in {"nl", "en"}:
        raise RuntimeError(
            f"Ongeldige LANGUAGE: {language}"
        )

    OUTPUT_DIR = (
        PDF_OUTPUT_ROOT
        / language
    )

    PDF_MKDOCS_DIR = (
        OUTPUT_DIR
        / "mkdocs"
    )

    def log(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    """
    Bouw de volledige Module-PDF.

    De webbuild en PDF-MkDocs-build zijn volledig gescheiden:

        site/
            normale website

        build/pdf/mkdocs/
            MkDocs-weergave voor de Module-PDF
    """

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    log(
        "1. Module-PDF MkDocs-build maken..."
    )

    build_mkdocs()

    log(
        "2. Resources inventariseren..."
    )

    resources = inventory_qr_resources(
        docs_root=ROOT / "docs",
        assets_root=ASSETS_DIR,
    )

    resources_catalog, site_url = (
        load_resource_build_config()
    )

    for week_number in discover_week_numbers():
        resources.extend(
            build_pset_qr_resources(
                week_number=week_number,
                resources_catalog=resources_catalog,
                site_url=site_url,
            )
        )

    log(
        "3. QR-assets bouwen..."
    )

    build_qr_assets(
        resources=resources,
        assets_root=ASSETS_DIR,
    )

    log(
        "4. Weken verzamelen..."
    )

    weeks = build_weeks(
        resources=resources,
    )

    log(
        f"   {len(weeks)} weken gevonden."
    )

    log(
        "5. Module-wrapper renderen..."
    )

    html = render_module(
        weeks
    )

    output = (
        OUTPUT_DIR
        / "module.html"
    )

    output.write_text(
        html,
        encoding="utf-8",
    )

    pdf_output = (
        OUTPUT_DIR
        / "module.pdf"
    )

    log(
        "6. Tijdelijke index-pass renderen..."
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        index_pdf = (
            Path(temp_dir)
            / "module-index-pass.pdf"
        )

        render_pdf(
            html_path=output,
            pdf_path=index_pdf,
        )

        page_map = read_pdf_page_map(
            index_pdf
        )

        understanding_page_map = (
            read_understanding_page_map(
                index_pdf
            )
        )

    log(
        "7. Paginamap gevonden:"
    )

    for target_id, page_number in sorted(
        page_map.items()
    ):
        if target_id.startswith(
            (
                "week-",
                "tset-",
                "pset-",
            )
        ):
            log(
                f"   {target_id} -> {page_number}"
            )

    log(
        "   Understanding:"
    )

    for target_id, page_number in sorted(
        understanding_page_map.items()
    ):
        log(
            f"   {target_id} -> {page_number}"
        )

    write_understanding_page_map(
        page_map=understanding_page_map,
    )

    log(
        "8. MkDocs-build opnieuw maken met actuele Understanding-paginamap..."
    )

    build_mkdocs()

    log(
        "9. Weken opnieuw verzamelen..."
    )

    weeks = build_weeks(
        resources=resources,
    )

    log(
        f"   {len(weeks)} weken gevonden."
    )

    log(
        "10. Module-wrapper opnieuw renderen..."
    )

    html = render_module(
        weeks
    )

    output.write_text(
        html,
        encoding="utf-8",
    )

    log(
        "11. Paginaverwijzingen toepassen..."
    )

    apply_pdf_page_map(
        html_path=output,
        page_map=page_map,
    )

    log(
        "12. Definitieve PDF genereren..."
    )

    render_pdf(
        html_path=output,
        pdf_path=pdf_output,
    )

    log()

    return pdf_output


def main():
    build_module()


if __name__ == "__main__":
    main()




