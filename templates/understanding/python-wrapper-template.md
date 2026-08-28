---
title: [ONDERWERP]
template: understanding.html
---

# Python *[ONDERWERP]*

<!--
============================================================
UNDERSTANDING — PYTHON WRAPPER — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------

Deze template legt het gerealiseerde ontwerp vast van een
zelfstandige Python Understanding-pagina.

De pagina zelf blijft bewust DUN.

De daadwerkelijke leerlingzichtbare onderwijsinhoud staat in:

    docs/nl/understanding/_content/python/[BESTAND].md

De wrapper maakt die centrale content zelfstandig toegankelijk
binnen de Understanding-wiki.


============================================================
1. BELANGRIJKE REGEL
============================================================

Plaats in deze wrapper GEEN aanvullende onderwijsinhoud.

Dus geen:

- introductietekst;
- leerdoelen;
- badges;
- voorbeelden;
- codevoorbeelden;
- uitleg van het Python-concept;
- opdrachten;
- tips;
- PSET- of TSET-specifieke uitleg;
- samenvatting.

Alle onderwijsinhoud wordt uitsluitend onderhouden in _content.

De wrapper bepaalt alleen HOE deze inhoud als zelfstandige
wiki-pagina wordt aangeboden.


============================================================
2. ARCHITECTUUR
============================================================

De structuur is:

    nl/understanding/python/[ONDERWERP].md
                    ↓
    nl/understanding/_content/python/[BESTAND].md

Dezelfde _content wordt centraal hergebruikt in verschillende
uitvoervormen.

De normale koppeling vanuit PSETs en TSETs verloopt via stabiele
Understanding-ID's. Daardoor hoeven deze onderwijsbronnen geen vaste
Understanding-URL, bestandslocatie of PDF-paginanummer te kennen.

Op de website kan de centrale _content inline worden weergegeven waar
de pagina-architectuur dat voorschrijft.

In de complete Module-PDF wordt Understanding centraal opgenomen.
PSETs en TSETs kunnen daar via `understanding_reference(understanding)`
naar de relevante Understanding-pagina('s) verwijzen. De paginanummers
worden tijdens de PDF-build automatisch bepaald.

De wrapper mag daarom geen inhoud dupliceren of wijzigen.


CENTRALE UNDERSTANDING-REGISTRATIE
---------------------------------
Iedere zelfstandige Understanding heeft een stabiele Understanding-ID.

Deze ID verbindt:

- de centrale _content;
- de zelfstandige Understanding-pagina;
- PSETs en TSETs die deze Understanding gebruiken;
- de centrale Understanding-sectie in de Module-PDF;
- automatisch gegenereerde PDF-paginaverwijzingen.

De Understanding-ID is niet hetzelfde als een Mermaid `%% id:`.
Een Understanding-ID identificeert inhoud; een Mermaid-ID identificeert
een diagramasset.

De wrapper bevat zelf geen vaste PDF-paginanummers. Die worden tijdens
de PDF-build bepaald en centraal als build-data beheerd.


============================================================
3. FUNCTIE VAN DE WRAPPER
============================================================

De wrapper heeft vier functies:

1. frontmatter leveren;
2. de zelfstandige paginatitel tonen;
3. de centrale _content als wiki-artikel presenteren;
4. navigatie naar verwante Understanding-artikelen bieden.

De wrapper is GEEN onderwijsinhoudelijke laag.


============================================================
4. PAGINATITEL
============================================================

Gebruik altijd:

    # Python *[ONDERWERP]*

Voorbeelden:

    # Python *elif*

    # Python *Variables*

    # Python *Logical Operators*

Hiermee wordt de bestaande modulebrede H1-styling gebruikt:

- Python = zwart / vet;
- onderwerp = grijs / lichter.

Introduceer hiervoor GEEN eigen titelcomponent of extra CSS.

De frontmatter-title bevat alleen de naam van het onderwerp:

    title: elif

niet:

    title: Python elif


============================================================
5. GEEN BADGE ONDER DE TITEL
============================================================

Plaats geen Python-badge op de zelfstandige Understanding-pagina.

Een badge op een week-, TSET- of PSET-pagina geeft aan welke
kennis daar wordt gebruikt.

Op een Understanding-artikel bevindt de leerling zich al bij
één specifiek kennisartikel.

Een extra badge voegt daar geen noodzakelijke informatie toe.


============================================================
6. CONTENT INCLUDE
============================================================

Plaats de include altijd binnen:

    <div class="understanding-article-start"></div>

    --8<-- "nl/understanding/_content/python/[BESTAND].md"


De marker understanding-article-start staat direct vóór de include.
Understanding-CSS gebruikt deze marker om de eerste inhoudelijke H3
uit _content uitsluitend op de zelfstandige wiki-pagina te verbergen
wanneer deze dezelfde naam heeft als het onderwerp in de paginatitel.

De heading blijft WEL in _content staan.

Dat is noodzakelijk omdat dezelfde _content buiten de zelfstandige
wrapper opnieuw kan worden gebruikt.

Op de website kan de content inline worden weergegeven waar de
pagina-architectuur dat voorschrijft. In samengestelde uitvoervormen,
waaronder de Module-PDF, blijft de inhoudelijke heading onderdeel van
de centrale Understanding-content.


============================================================
7. EERSTE H3 IN _CONTENT
============================================================

De wrapper verwijdert of verandert GEEN headings in _content.

Wanneer de eerste H3 dezelfde inhoud heeft als de zelfstandige
paginatitel, wordt deze uitsluitend via Understanding-CSS
verborgen.

Bijvoorbeeld:

Wrapper:

    # Python *elif*

_content:

    ### `elif`

Op de zelfstandige Understanding-pagina ziet de leerling alleen
de paginatitel.

Wanneer dezelfde _content elders wordt geïncludeerd, blijft:

    ### `elif`

wel zichtbaar.


============================================================
8. NAVIGATIE ONDER HET ARTIKEL
============================================================

Na de _content staat een horizontale scheiding:

    ---

Daaronder staat de navigatie binnen het kenniscluster.

Gebruik:

    [← [VORIGE]]([VORIGE-LINK]) · [Terug naar [CLUSTER]]([INDEX-LINK]) · [[VOLGENDE] →]([VOLGENDE-LINK])

Bijvoorbeeld:

    [← else](else.md) · [Terug naar Conditionals](../index.md#conditionals) · [Branches →](branches.md)

Gebruik in de navigatietekst GEEN inline-code-opmaak.

Dus:

    [← else](else.md)

en niet:

    [← `else`](else.md)

De navigatie heeft drie functies:

- vorige artikel;
- terug naar het kenniscluster;
- volgende artikel.


============================================================
9. VOLGORDE VAN ARTIKELEN
============================================================

De vorige/volgende-navigatie volgt de inhoudelijk logische
volgorde van de Understanding-wiki.

Deze volgorde is NIET automatisch hetzelfde als:

- weekvolgorde;
- volgorde waarin concepten toevallig zijn toegevoegd;
- alfabetische volgorde.

De volgorde moet ook bruikbaar zijn wanneer _content later
achter elkaar wordt samengesteld tot een doorlopende PDF.


============================================================
10. INDEX EN CLUSTER
============================================================

De centrale Understanding-index bepaalt:

- onder welk hoofddomein het artikel valt;
- in welke card / welk kenniscluster het artikel staat;
- welke artikelen samen één inhoudelijk cluster vormen.

De wrapper herhaalt deze structuur niet bovenaan de pagina.

Plaats dus geen extra regel zoals:

    Python · Conditionals

onder de H1.

De paginatitel en de navigatie zijn voldoende.


============================================================
11. TEMPLATE
============================================================

Gebruik altijd:

    template: understanding.html

Hierdoor gebruikt de pagina dezelfde algemene module-styling
als de overige Understanding-pagina's.


============================================================
LAATSTE ONTWERPCONTROLE
============================================================

[ ] Bevat frontmatter alleen de onderwerpstitel?
[ ] Wordt template understanding.html gebruikt?
[ ] Is de H1 geschreven als: # Python *[ONDERWERP]*?
[ ] Staat er geen badge onder de H1?
[ ] Staat er geen extra clusterregel boven de inhoud?
[ ] Staat understanding-article-start direct vóór de include?
[ ] Verwijst de include naar het juiste _content-bestand?
[ ] Is de wrapper gekoppeld aan de juiste centrale Understanding?
[ ] Worden geen vaste Understanding-URL's of PDF-paginanummers toegevoegd?
[ ] Blijft de koppeling vanuit PSET/TSET gebaseerd op stabiele Understanding-ID's?
[ ] Is geen onderwijsinhoud in de wrapper toegevoegd?
[ ] Is de eerste H3 alleen via CSS verborgen en niet verwijderd?
[ ] Staat onder de content een horizontale scheiding?
[ ] Zijn vorige, cluster en volgende correct gelinkt?
[ ] Ontbreekt een vorige- of volgende-link volledig wanneer het artikel
    het eerste of laatste artikel van een cluster is?
[ ] Worden geen lege of uitgeschakelde navigatielinks gebruikt?
[ ] Bevat navigatietekst geen inline-code-opmaak?
[ ] Is de navigatievolgorde inhoudelijk logisch?
[ ] Zijn alle placeholders vervangen?
============================================================
-->

<div class="understanding-article-start"></div>

--8<-- "nl/understanding/_content/python/[BESTAND].md"


---

<!--
NAVIGATIE

Standaard, wanneer zowel vorige als volgende bestaan:

[← [VORIGE]]([VORIGE-LINK]) · [Terug naar [CLUSTER]]([INDEX-LINK]) · [[VOLGENDE] →]([VOLGENDE-LINK])

Eerste artikel van een cluster:

[Terug naar [CLUSTER]]([INDEX-LINK]) · [[VOLGENDE] →]([VOLGENDE-LINK])

Laatste artikel van een cluster:

[← [VORIGE]]([VORIGE-LINK]) · [Terug naar [CLUSTER]]([INDEX-LINK])

Wanneer een vorige of volgende niet bestaat:
- laat die link volledig weg;
- gebruik geen lege placeholder;
- gebruik geen uitgeschakelde link.
-->

[← [VORIGE]]([VORIGE-LINK]) · [Terug naar [CLUSTER]]([INDEX-LINK]) · [[VOLGENDE] →]([VOLGENDE-LINK])