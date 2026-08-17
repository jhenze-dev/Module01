---
title: [TITEL]
template: understanding.html
---

# [TITEL]

<!--
============================================================
UNDERSTANDING — VISUAL FIRST WRAPPER — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------
Deze template legt het gerealiseerde ontwerp vast van een
zelfstandige Visual First Understanding-pagina.

De pagina zelf is bewust DUN.

De daadwerkelijke leerlingzichtbare onderwijsinhoud staat in:

    docs/understanding/_content/[BESTAND].md

De wrapper maakt die centrale content als zelfstandige
Understanding-pagina beschikbaar.


============================================================
1. BELANGRIJKE REGEL
============================================================

Plaats in deze wrapper GEEN aanvullende onderwijsinhoud.

Dus geen:

- introductietekst;
- leerdoelen;
- badges;
- voorbeelden;
- Mermaid-diagrammen;
- opdrachten;
- tips;
- PSET- of TSET-specifieke uitleg;
- samenvatting.

De wrapper bevat uitsluitend:

1. frontmatter;
2. H1;
3. include van de centrale content.


============================================================
2. ARCHITECTUUR
============================================================

De structuur is:

understanding/visual-first/[ONDERWERP].md
        ↓
understanding/_content/[ONDERWERP].md

De wrapper bepaalt alleen HOE de content zelfstandig wordt
aangeboden.

De onderwijsinhoud wordt uitsluitend onderhouden in
_content.

Hierdoor kan dezelfde content:

- zelfstandig worden geopend;
- vanuit een TSET worden gelinkt;
- in een PSET worden geïntegreerd;
- elders in de module worden hergebruikt.


============================================================
3. ONDERWIJSINHOUDELIJKE HIËRARCHIE
============================================================

Gebruik altijd deze volgorde:

1. MODULEFRAMEWORK
   Bepaalt welke Visual First-representatie onderdeel is van
   de leerlijn en welke functie deze heeft.

2. VISUAL FIRST CONTENT
   Legt de representatie en het gebruik ervan uit.

3. WRAPPER
   Maakt deze content zelfstandig toegankelijk.

4. TSET / PSET
   Bepalen wanneer en hoe leerlingen de representatie
   daadwerkelijk gebruiken.

Bij een conflict is het MODULEFRAMEWORK inhoudelijk leidend.


============================================================
4. TITEL
============================================================

Gebruik als titel de naam van de representatie.

Bijvoorbeeld:

    Flowcharts

De H1 moet overeenkomen met de frontmatter-title.

Controleer dit expliciet bij kopiëren van een bestaande
wrapper.


============================================================
5. TEMPLATE
============================================================

Gebruik altijd:

    template: understanding.html

Hierdoor krijgt de zelfstandige Understanding dezelfde
algemene module-styling als de andere Understanding-pagina's.


============================================================
6. CONTENT INCLUDE
============================================================

Gebruik uitsluitend:

    --8<-- "understanding/_content/[BESTAND].md"

Plaats geen aanvullende leerlinginhoud boven of onder deze
include.


============================================================
LAATSTE ONTWERPCONTROLE
============================================================

[ ] Klopt de frontmatter-title?
[ ] Komt de H1 exact overeen met de titel?
[ ] Wordt template understanding.html gebruikt?
[ ] Verwijst de include naar het juiste _content-bestand?
[ ] Staat buiten de include geen onderwijsinhoud?
[ ] Bevat de wrapper geen PSET- of TSET-specifieke tekst?
[ ] Zijn alle placeholders vervangen?
============================================================
-->

--8<-- "understanding/_content/[BESTAND].md"