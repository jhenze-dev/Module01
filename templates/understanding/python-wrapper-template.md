---
title: [TITEL]
template: understanding.html
---

# [TITEL]

<!--
============================================================
UNDERSTANDING — PYTHON WRAPPER — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------
Deze template legt het gerealiseerde ontwerp vast van een
zelfstandige Python Understanding-pagina.

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
- codevoorbeelden;
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

understanding/python/[ONDERWERP].md
        ↓
understanding/_content/[ONDERWERP].md

De wrapper bepaalt alleen HOE de content zelfstandig wordt
aangeboden.

De onderwijsinhoud wordt uitsluitend onderhouden in
_content.

Hierdoor kan dezelfde content:

- zelfstandig worden geopend;
- vanuit een PSET worden geïntegreerd;
- vanuit andere modulepagina's worden gelinkt;
- elders in de module worden hergebruikt.


============================================================
3. ONDERWIJSINHOUDELIJKE HIËRARCHIE
============================================================

Gebruik altijd deze volgorde:

1. MODULEFRAMEWORK
   Bepaalt welke Python-concepten onderdeel zijn van de
   leerlijn en wanneer deze relevant worden.

2. PYTHON CONTENT
   Legt het Python-concept inhoudelijk en didactisch uit.

3. WRAPPER
   Maakt deze content zelfstandig toegankelijk.

4. PSET / TSET
   Bepalen wanneer en hoe leerlingen de Python Understanding
   gebruiken of raadplegen.

Bij een conflict is het MODULEFRAMEWORK inhoudelijk leidend.


============================================================
4. TITEL
============================================================

Gebruik als titel de naam van het Python-concept of het
afgesproken conceptcluster.

Bijvoorbeeld:

    Conditionals

of:

    Logical Operators

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