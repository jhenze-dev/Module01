import os
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# PAS HIERNA lokale imports
from helpers.mermaid import (
    build_mermaid_assets_from_markdown,
    publish_mermaid_assets,
    replace_mermaid_blocks_in_site,
)

from helpers.understanding import (
    understanding_reference as build_understanding_reference,
)

from helpers.resources import (
    resource_group as build_resource_group,
    resource_page as build_resource_page,
    resources_index as build_resources_index,
)


# ---------------------------------------------------------
# Projectstructuur
# ---------------------------------------------------------

DOCS_DIR = PROJECT_ROOT / "docs"
BUILD_DIR = PROJECT_ROOT / "build"
ASSETS_DIR = BUILD_DIR / "assets"
SITE_DIR = PROJECT_ROOT / "site"


# ---------------------------------------------------------
# Build-state
# ---------------------------------------------------------

# on_pre_page_macros wordt voor iedere pagina aangeroepen.
# Mermaid-assets hoeven echter maar één keer per MkDocs-build
# geïnventariseerd en eventueel gegenereerd te worden.
_mermaid_assets_built = False


# ---------------------------------------------------------
# MkDocs environment
# ---------------------------------------------------------

def define_env(env):
    """
    Registreer custom variabelen en macros voor MkDocs.

    main.py bevat alleen de koppeling tussen MkDocs en de
    losse helpermodules. De daadwerkelijke logica staat
    in helpers/.
    """

    render_mode = os.getenv(
        "RENDER_MODE",
        "web",
    )

    env.variables["render_mode"] = render_mode

    @env.macro
    def understanding_reference(items):
        """
        MkDocs-macro voor Understanding.

        De helper bepaalt op basis van render-mode en
        paginatype welke presentatie nodig is.
        """

        page = env.page

        return build_understanding_reference(
            items=items,
            catalog=env.variables[
                "understanding_catalog"
            ],
            pages=env.variables[
                "understanding_pages"
            ],
            render_mode=render_mode,
            page_template=page.meta.get(
                "template",
                "",
            ),
            docs_root=DOCS_DIR,
            current_source_path=page.file.src_path,
        )

    @env.macro
    def resource_group(item):
        """
        MkDocs-macro voor externe resourcegroepen.

        De helper bepaalt op basis van render-mode
        welke presentatie nodig is.
        """

        return build_resource_group(
            item=item,
            catalog=env.variables[
                "resources_catalog"
            ],
            render_mode=render_mode,
        )

    @env.macro
    def resource_page(item):
        """
        MkDocs-macro voor één zelfstandige resourcepagina.
        """

        return build_resource_page(
            item=item,
            catalog=env.variables[
                "resources_catalog"
            ],
        )

    @env.macro
    def resources_page():
        """
        MkDocs-macro voor de centrale Resources-pagina.
        """

        return build_resources_index(
            catalog=env.variables[
                "resources_catalog"
            ],
        )

# ---------------------------------------------------------
# Voor paginarendering
# ---------------------------------------------------------

def on_pre_page_macros(env):
    """
    Controleer en genereer de gedeelde Mermaid-assets.

    Deze hook wordt voor iedere pagina aangeroepen, maar de
    Mermaid-build wordt per MkDocs-build slechts één keer
    uitgevoerd.

    De Mermaid-helper gebruikt hashes, waardoor alleen nieuwe
    of gewijzigde diagrammen daadwerkelijk worden gerenderd.
    """

    global _mermaid_assets_built

    if _mermaid_assets_built:
        return

    build_mermaid_assets_from_markdown(
        docs_root=DOCS_DIR,
        assets_root=ASSETS_DIR,
    )

    _mermaid_assets_built = True


# ---------------------------------------------------------
# Na volledige MkDocs-build
# ---------------------------------------------------------

def on_post_build(env):
    """
    Voer acties uit nadat MkDocs alle HTML-pagina's heeft gebouwd.

    Voor de gewone website worden de gedeelde Mermaid-assets
    gepubliceerd onder site/assets/generated/mermaid/.

    In andere render-modes blijven de centrale assets alleen
    onder build/assets/ beschikbaar.
    """

    render_mode = os.getenv(
        "RENDER_MODE",
        "web",
    )

    if render_mode == "web":
        publish_mermaid_assets(
            assets_root=ASSETS_DIR,
            site_dir=SITE_DIR,
        )

        replace_mermaid_blocks_in_site(
            site_dir=SITE_DIR,
            docs_root=DOCS_DIR,
            assets_root=ASSETS_DIR,
        )