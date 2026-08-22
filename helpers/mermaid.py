from pathlib import Path
import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass

import yaml
from bs4 import BeautifulSoup
from bs4.element import Tag
from PIL import Image


PROJECT_ROOT = Path(__file__).resolve().parents[1]

PUPPETEER_CONFIG = (
    PROJECT_ROOT
    / "puppeteer-config.json"
)

MERMAID_RENDER_SCALE = 3

MERMAID_ID_PATTERN = re.compile(
    r"^%%\s*id:\s*([a-z0-9-]+)\s*$",
    re.MULTILINE,
)

MERMAID_BLOCK_PATTERN = re.compile(
    r"```mermaid\s*\n"
    r"(.*?)"
    r"\n```",
    re.DOTALL,
)


@dataclass
class MermaidBlock:
    mermaid_id: str
    source: str
    source_path: Path
    category: str
    output_path: Path


def _find_npx() -> str:
    """
    Zoek de npx executable op Windows, macOS of Linux.
    """

    executable = shutil.which("npx")

    if executable is None:
        executable = shutil.which("npx.cmd")

    if executable is None:
        raise RuntimeError(
            "npx is niet gevonden. Installeer Node.js en npm."
        )

    return executable


def extract_mermaid_id(
    source: str,
) -> str:
    """
    Lees de stabiele Mermaid-ID uit de broncode.
    """

    match = MERMAID_ID_PATTERN.search(
        source
    )

    if match is None:
        raise RuntimeError(
            "Mermaid-blok bevat geen geldige "
            "'%% id: ...'-regel."
        )

    return match.group(1)


def determine_mermaid_category(
    source_path: str | Path,
) -> str:
    """
    Bepaal of een Mermaid-diagram onder sets
    of understanding valt.
    """

    source_path = Path(
        source_path
    )

    parts = {
        part.lower()
        for part in source_path.parts
    }

    if (
        "understanding" in parts
        and "_content" in parts
    ):
        return "understanding"

    return "sets"


def mermaid_hash(
    source: str,
) -> str:
    """
    Bereken een SHA-256 hash van de Mermaid-broncode.
    """

    return hashlib.sha256(
        source.encode("utf-8")
    ).hexdigest()


def _normalize_mermaid_source(
    source: str,
) -> str:
    """
    Normaliseer Mermaid-bron zodat Markdown- en HTML-versies
    betrouwbaar met elkaar vergeleken kunnen worden.

    Alleen technisch irrelevante verschillen worden verwijderd:

    - Windows/macOS/Linux line endings;
    - trailing whitespace per regel;
    - lege ruimte aan begin en einde van het hele blok.
    """

    source = source.replace(
        "\r\n",
        "\n",
    )

    source = source.replace(
        "\r",
        "\n",
    )

    lines = [
        line.rstrip()
        for line in source.strip().split(
            "\n"
        )
    ]

    return "\n".join(
        lines
    )


def inventory_mermaid_blocks(
    docs_root: str | Path,
    assets_root: str | Path,
) -> list[MermaidBlock]:
    """
    Inventariseer alle Mermaid-blokken.

    Er wordt in deze fase nog niets gegenereerd.
    """

    docs_root = Path(
        docs_root
    )

    assets_root = Path(
        assets_root
    )

    blocks: list[MermaidBlock] = []

    for markdown_path in docs_root.rglob(
        "*.md"
    ):

        markdown = markdown_path.read_text(
            encoding="utf-8",
        )

        for match in MERMAID_BLOCK_PATTERN.finditer(
            markdown
        ):

            source = match.group(
                1
            ).strip()

            mermaid_id = extract_mermaid_id(
                source
            )

            category = determine_mermaid_category(
                markdown_path
            )

            output_path = (
                assets_root
                / "mermaid"
                / category
                / f"{mermaid_id}.png"
            )

            blocks.append(
                MermaidBlock(
                    mermaid_id=mermaid_id,
                    source=source,
                    source_path=markdown_path,
                    category=category,
                    output_path=output_path,
                )
            )

    return blocks


def validate_mermaid_blocks(
    blocks: list[MermaidBlock],
) -> None:
    """
    Valideer alle Mermaid-blokken vóór rendering.

    Een ID mag alleen meerdere keren voorkomen wanneer
    categorie én broncode exact gelijk zijn.
    """

    seen: dict[
        str,
        MermaidBlock,
    ] = {}

    for block in blocks:

        key = (
            f"{block.category}:"
            f"{block.mermaid_id}"
        )

        if key not in seen:
            seen[key] = block
            continue

        previous = seen[
            key
        ]

        if (
            _normalize_mermaid_source(
                previous.source
            )
            !=
            _normalize_mermaid_source(
                block.source
            )
        ):
            raise RuntimeError(
                "\nMermaid-ID wordt gebruikt voor "
                "verschillende diagrammen:\n"
                f"  ID: {block.mermaid_id}\n"
                f"  Eerste bestand: "
                f"{previous.source_path}\n"
                f"  Tweede bestand: "
                f"{block.source_path}\n"
            )


def _unique_blocks(
    blocks: list[MermaidBlock],
) -> list[MermaidBlock]:
    """
    Verwijder dubbele blokken met dezelfde ID
    en dezelfde bron.
    """

    unique: dict[
        str,
        MermaidBlock,
    ] = {}

    for block in blocks:

        key = (
            f"{block.category}:"
            f"{block.mermaid_id}"
        )

        if key not in unique:
            unique[key] = block

    return list(
        unique.values()
    )


def _load_manifest(
    manifest_path: Path,
) -> dict:
    """
    Lees het bestaande Mermaid-manifest.

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
    blocks: list[MermaidBlock],
) -> None:
    """
    Schrijf het Mermaid-manifest opnieuw op basis
    van de actuele inventarisatie.
    """

    manifest: dict[
        str,
        dict[
            str,
            dict[str, str],
        ],
    ] = {}

    for block in blocks:

        category = manifest.setdefault(
            block.category,
            {},
        )

        category[
            block.mermaid_id
        ] = {
            "hash": mermaid_hash(
                block.source
            ),
            "file": (
                f"{block.mermaid_id}.png"
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
    block: MermaidBlock,
    manifest: dict,
) -> bool:
    """
    Bepaal of een diagram opnieuw gerenderd moet worden.

    Render wanneer:

    - de PNG niet bestaat;
    - de ID niet in het manifest staat;
    - de opgeslagen hash niet overeenkomt.
    """

    if not block.output_path.exists():
        return True

    category_data = manifest.get(
        block.category
    )

    if not isinstance(
        category_data,
        dict,
    ):
        return True

    entry = category_data.get(
        block.mermaid_id
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
        != mermaid_hash(
            block.source
        )
    )


def _remove_obsolete_assets(
    blocks: list[MermaidBlock],
    manifest: dict,
    assets_root: Path,
) -> int:
    """
    Verwijder PNG's die nog in het oude manifest staan
    maar niet meer in de actuele Markdown voorkomen.
    """

    current_keys = {
        (
            f"{block.category}:"
            f"{block.mermaid_id}"
        )
        for block in blocks
    }

    removed = 0

    for category, entries in manifest.items():

        if not isinstance(
            entries,
            dict,
        ):
            continue

        for mermaid_id in entries:

            key = (
                f"{category}:"
                f"{mermaid_id}"
            )

            if key in current_keys:
                continue

            obsolete_path = (
                assets_root
                / "mermaid"
                / category
                / f"{mermaid_id}.png"
            )

            if obsolete_path.exists():

                obsolete_path.unlink()

                removed += 1

    return removed


def render_mermaid_batch(
    blocks: list[MermaidBlock],
) -> list[Path]:
    """
    Render alle opgegeven Mermaid-blokken
    in één Mermaid CLI-run.
    """

    if not blocks:
        return []

    if not PUPPETEER_CONFIG.exists():
        raise RuntimeError(
            "Puppeteer-config niet gevonden:\n"
            f"  {PUPPETEER_CONFIG}"
        )

    with tempfile.TemporaryDirectory(
        prefix="onc-mermaid-"
    ) as temp_dir_str:

        temp_dir = Path(
            temp_dir_str
        )

        input_path = (
            temp_dir
            / "mermaid-batch.md"
        )

        output_markdown = (
            temp_dir
            / "mermaid-output.md"
        )

        artefacts_dir = (
            temp_dir
            / "artefacts"
        )

        artefacts_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        batch_parts: list[str] = []

        for block in blocks:

            batch_parts.append(
                "```mermaid\n"
                f"{block.source}\n"
                "```\n"
            )

        input_path.write_text(
            "\n".join(
                batch_parts
            ),
            encoding="utf-8",
        )

        startupinfo = None
        creationflags = 0

        if os.name == "nt":

            startupinfo = (
                subprocess.STARTUPINFO()
            )

            startupinfo.dwFlags |= (
                subprocess.STARTF_USESHOWWINDOW
            )

            startupinfo.wShowWindow = (
                subprocess.SW_HIDE
            )

            creationflags = (
                subprocess.CREATE_NO_WINDOW
            )

        print(
            "Mermaid: batch renderen..."
        )

        subprocess.run(
            [
                _find_npx(),
                "mmdc",
                "-i",
                str(
                    input_path
                ),
                "-o",
                str(
                    output_markdown
                ),
                "-a",
                str(
                    artefacts_dir
                ),
                "-e",
                "png",
                "-s",
                "3",
                "-b",
                "white",
                "-j",
                "1",
                "-q",
                "-p",
                str(
                    PUPPETEER_CONFIG
                ),
            ],
            check=True,
            startupinfo=startupinfo,
            creationflags=creationflags,
        )

        generated_files = sorted(
            artefacts_dir.glob(
                "mermaid-output-*.png"
            ),
            key=lambda path: int(
                path.stem.rsplit(
                    "-",
                    1,
                )[1]
            ),
        )

        if (
            len(generated_files)
            != len(blocks)
        ):

            raise RuntimeError(
                "Aantal door Mermaid gegenereerde "
                "afbeeldingen komt niet overeen met "
                "de inventarisatie.\n"
                f"Verwacht: {len(blocks)}\n"
                f"Gevonden: {len(generated_files)}"
            )

        final_paths: list[
            Path
        ] = []

        for (
            block,
            generated_file,
        ) in zip(
            blocks,
            generated_files,
            strict=True,
        ):

            block.output_path.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            shutil.copyfile(
                generated_file,
                block.output_path,
            )

            final_paths.append(
                block.output_path
            )

        print(
            f"Mermaid: {len(final_paths)} "
            "afbeeldingen bijgewerkt."
        )

        return final_paths


def build_mermaid_assets_from_markdown(
    docs_root: str | Path,
    assets_root: str | Path,
) -> list[Path]:
    """
    Volledige Mermaid-build.

    1. inventariseren;
    2. valideren;
    3. duplicaten verwijderen;
    4. manifest lezen;
    5. alleen nieuwe/gewijzigde diagrammen renderen;
    6. obsolete assets verwijderen;
    7. manifest actualiseren.
    """

    docs_root = Path(
        docs_root
    )

    assets_root = Path(
        assets_root
    )

    manifest_path = (
        assets_root
        / "mermaid"
        / "manifest.yml"
    )

    blocks = inventory_mermaid_blocks(
        docs_root=docs_root,
        assets_root=assets_root,
    )

    print(
        f"Mermaid: {len(blocks)} "
        "blokken gevonden."
    )

    validate_mermaid_blocks(
        blocks
    )

    unique_blocks = _unique_blocks(
        blocks
    )

    manifest = _load_manifest(
        manifest_path
    )

    render_blocks = [
        block
        for block in unique_blocks
        if _needs_render(
            block,
            manifest,
        )
    ]

    unchanged = (
        len(unique_blocks)
        - len(render_blocks)
    )

    print(
        f"Mermaid: {unchanged} "
        "ongewijzigd."
    )

    print(
        f"Mermaid: {len(render_blocks)} "
        "afbeeldingen te genereren."
    )

    generated = render_mermaid_batch(
        render_blocks
    )

    removed = _remove_obsolete_assets(
        blocks=unique_blocks,
        manifest=manifest,
        assets_root=assets_root,
    )

    if removed:

        print(
            f"Mermaid: {removed} "
            "verouderde afbeeldingen verwijderd."
        )

    _write_manifest(
        manifest_path=manifest_path,
        blocks=unique_blocks,
    )

    print(
        "Mermaid: gereed."
    )

    return generated


def _find_matching_block(
    source: str,
    blocks: list[MermaidBlock],
) -> MermaidBlock:
    """
    Zoek het oorspronkelijke MermaidBlock bij een Mermaid-blok
    dat uit de gebouwde HTML komt.

    Daarbij gebruiken we:

    - de stabiele %% id;
    - de genormaliseerde Mermaid-bron.

    Hierdoor blijft bijvoorbeeld Understanding-content die via
    een include in een PSET verschijnt gekoppeld aan de categorie
    'understanding'.
    """

    normalized_source = (
        _normalize_mermaid_source(
            source
        )
    )

    mermaid_id = extract_mermaid_id(
        normalized_source
    )

    matches = [
        block
        for block in blocks
        if (
            block.mermaid_id
            == mermaid_id
            and
            _normalize_mermaid_source(
                block.source
            )
            == normalized_source
        )
    ]

    if not matches:

        raise RuntimeError(
            "Gerenderd Mermaid-blok kan niet worden "
            "gekoppeld aan de broninventarisatie:\n"
            f"  ID: {mermaid_id}"
        )

    categories = {
        block.category
        for block in matches
    }

    if len(
        categories
    ) != 1:

        raise RuntimeError(
            "Mermaid-blok komt met dezelfde ID en "
            "broncode in meerdere categorieën voor:\n"
            f"  ID: {mermaid_id}\n"
            f"  Categorieën: "
            f"{sorted(categories)}"
        )

    return matches[0]


def publish_mermaid_assets(
    assets_root: str | Path,
    site_dir: str | Path,
) -> Path:
    """
    Publiceer de gegenereerde Mermaid-PNG's naar de website.

    Bron:

        build/assets/mermaid/
            sets/
            understanding/

    Doel:

        site/assets/generated/mermaid/
            sets/
            understanding/

    manifest.yml wordt niet gepubliceerd.
    """

    assets_root = Path(
        assets_root
    )

    site_dir = Path(
        site_dir
    )

    source_root = (
        assets_root
        / "mermaid"
    )

    target_root = (
        site_dir
        / "assets"
        / "generated"
        / "mermaid"
    )

    if not source_root.exists():

        raise RuntimeError(
            "Mermaid asset-map bestaat niet:\n"
            f"  {source_root}"
        )

    target_root.mkdir(
        parents=True,
        exist_ok=True,
    )

    for category in (
        "sets",
        "understanding",
    ):

        source_dir = (
            source_root
            / category
        )

        if not source_dir.exists():
            continue

        target_dir = (
            target_root
            / category
        )

        if target_dir.exists():

            shutil.rmtree(
                target_dir
            )

        shutil.copytree(
            source_dir,
            target_dir,
        )

    return target_root


def _extract_mermaid_source_from_html(
    element: Tag,
) -> str:
    """
    Lees de Mermaid-bron uit een door MkDocs gebouwd
    HTML-element.

    Ondersteunt onder andere:

        <pre class="mermaid">...</pre>

    en:

        <pre class="mermaid">
            <code>...</code>
        </pre>

    en vergelijkbare elementen met class="mermaid".
    """

    code = element.find(
        "code"
    )

    if isinstance(
        code,
        Tag,
    ):

        return code.get_text()

    return element.get_text()


def replace_mermaid_blocks_in_site(
    site_dir: str | Path,
    docs_root: str | Path,
    assets_root: str | Path,
) -> int:
    """
    Vervang na de MkDocs-build alle Mermaid-elementen in de
    gebouwde HTML door verwijzingen naar de gegenereerde PNG's.

    De Markdown-bronnen blijven volledig ongemoeid.

    De afbeeldingen zijn eerder gepubliceerd naar:

        site/assets/generated/mermaid/

    Vanuit iedere HTML-pagina wordt automatisch een relatief
    pad naar het juiste asset berekend.

    Returns
    -------
    int
        Aantal vervangen Mermaid-diagrammen.
    """

    site_dir = Path(
        site_dir
    )

    docs_root = Path(
        docs_root
    )

    assets_root = Path(
        assets_root
    )

    blocks = inventory_mermaid_blocks(
        docs_root=docs_root,
        assets_root=assets_root,
    )

    validate_mermaid_blocks(
        blocks
    )

    replacements = 0

    for html_path in site_dir.rglob(
        "*.html"
    ):

        html = html_path.read_text(
            encoding="utf-8",
        )

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        mermaid_elements = [
            element
            for element in soup.select(
                ".mermaid"
            )
            if isinstance(
                element,
                Tag,
            )
        ]

        if not mermaid_elements:
            continue

        page_changed = False

        for element in mermaid_elements:

            source = (
                _extract_mermaid_source_from_html(
                    element
                )
            )

            block = _find_matching_block(
                source=source,
                blocks=blocks,
            )

            published_asset = (
                site_dir
                / "assets"
                / "generated"
                / "mermaid"
                / block.category
                / f"{block.mermaid_id}.png"
            )

            if not published_asset.exists():

                raise RuntimeError(
                    "Gepubliceerd Mermaid-asset "
                    "ontbreekt:\n"
                    f"  {published_asset}"
                )

            with Image.open(published_asset) as image_file:
                pixel_width, pixel_height = image_file.size

            display_width = round(
                pixel_width / MERMAID_RENDER_SCALE
            )

            display_height = round(
                pixel_height / MERMAID_RENDER_SCALE
            )            

            relative_path = os.path.relpath(
                published_asset,
                html_path.parent,
            )

            image_url = Path(
                relative_path
            ).as_posix()

            image = soup.new_tag("img")

            image["class"] = "mermaid-image"

            image["src"] = image_url

            image["width"] = str(
                display_width
            )

            image["height"] = str(
                display_height
            )

            image["alt"] = (
                f"Diagram "
                f"{block.mermaid_id}"
            )

            image["data-mermaid-id"] = block.mermaid_id

            element.replace_with(
                image
            )

            replacements += 1
            page_changed = True

        if page_changed:

            html_path.write_text(
                str(
                    soup
                ),
                encoding="utf-8",
            )

    print(
        f"Mermaid: {replacements} "
        "diagrammen in website vervangen."
    )

    return replacements


def replace_mermaid_blocks_for_pdf(
    html: str,
    docs_root: str | Path,
    assets_root: str | Path,
    pdf_output_dir: str | Path,
) -> str:
    """
    Vervang Mermaid-elementen in een HTML-fragment voor de Module-PDF
    door verwijzingen naar de bestaande gegenereerde PNG-assets.

    Er wordt hier niets opnieuw gerenderd.

    De Mermaid-bron blijft in Markdown staan en de gedeelde PNG's
    staan onder:

        build/assets/mermaid/
            sets/
            understanding/

    De gegenereerde <img>-src wordt relatief gemaakt ten opzichte
    van de map waarin de samengestelde PDF-HTML wordt geschreven,
    bijvoorbeeld:

        build/pdf/

    De weergavegrootte is gelijk aan de webversie: de PNG wordt met
    MERMAID_RENDER_SCALE gerenderd en in HTML op 1 / die schaal
    weergegeven.
    """

    docs_root = Path(
        docs_root
    )

    assets_root = Path(
        assets_root
    )

    pdf_output_dir = Path(
        pdf_output_dir
    )

    blocks = inventory_mermaid_blocks(
        docs_root=docs_root,
        assets_root=assets_root,
    )

    validate_mermaid_blocks(
        blocks
    )

    soup = BeautifulSoup(
        html,
        "html.parser",
    )

    mermaid_elements = [
        element
        for element in soup.select(
            ".mermaid"
        )
        if isinstance(
            element,
            Tag,
        )
    ]

    for element in mermaid_elements:

        source = (
            _extract_mermaid_source_from_html(
                element
            )
        )

        block = _find_matching_block(
            source=source,
            blocks=blocks,
        )

        asset_path = (
            assets_root
            / "mermaid"
            / block.category
            / f"{block.mermaid_id}.png"
        )

        if not asset_path.exists():

            raise RuntimeError(
                "Mermaid-asset voor PDF ontbreekt:\n"
                f"  {asset_path}"
            )

        with Image.open(asset_path) as image_file:
            pixel_width, pixel_height = image_file.size

        display_width = round(
            pixel_width / MERMAID_RENDER_SCALE
        )

        display_height = round(
            pixel_height / MERMAID_RENDER_SCALE
        )

        relative_path = os.path.relpath(
            asset_path,
            pdf_output_dir,
        )

        image_url = Path(
            relative_path
        ).as_posix()

        image = soup.new_tag(
            "img"
        )

        image["class"] = "mermaid-image"

        image["src"] = image_url

        image["width"] = str(
            display_width
        )

        image["height"] = str(
            display_height
        )

        image["alt"] = (
            f"Diagram "
            f"{block.mermaid_id}"
        )

        image["data-mermaid-id"] = block.mermaid_id

        element.replace_with(
            image
        )

    return str(
        soup
    )

