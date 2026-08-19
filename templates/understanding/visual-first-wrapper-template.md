---
title: [ONDERWERP]
template: understanding.html
---

# Visual First *[ONDERWERP]*

<!--
============================================================
UNDERSTANDING — VISUAL FIRST WRAPPER — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------

Deze template legt het gerealiseerde ontwerp vast van een
zelfstandige Visual First Understanding-pagina.

De pagina zelf blijft bewust DUN.

De daadwerkelijke leerlingzichtbare onderwijsinhoud staat in:

    docs/understanding/_content/visual-first/[PAD]/[BESTAND].md

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
- uitleg van de representatie;
- Mermaid-diagrammen;
- voorbeelden;
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

De structuur kan bijvoorbeeld zijn:

    understanding/visual-first/flowcharts/basics.md
                         ↓
    understanding/_content/visual-first/flowcharts/basics.md

of:

    understanding/visual-first/ipo.md
                         ↓
    understanding/_content/visual-first/ipo.md

De exacte submap volgt de afgesproken Understanding-filetree.

Verzin geen extra mappen alleen voor de wrapper.

Dezelfde _content kan daarnaast:

- vanuit een TSET worden geopend;
- waar passend in een PSET worden opgenomen;
- vanuit andere modulepagina's worden gelinkt;
- later onderdeel zijn van een samengestelde PDF.


============================================================
3. FUNCTIE VAN DE WRAPPER
============================================================

De wrapper heeft vier functies:

1. frontmatter leveren;
2. de zelfstandige paginatitel tonen;
3. de centrale _content als wiki-artikel presenteren;
4. navigatie naar verwante Understanding-artikelen bieden.

De wrapper bevat zelf geen uitleg van de representatie.


============================================================
4. PAGINATITEL
============================================================

Gebruik altijd:

    # Visual First *[ONDERWERP]*

Voorbeelden:

    # Visual First *Flowcharts*

    # Visual First *IPO Diagram*

    # Visual First *Decisions & Branches*

Hiermee wordt dezelfde bestaande H1-styling gebruikt als op
de overige modulepagina's:

- Visual First = zwart / vet;
- onderwerp = grijs / lichter.

Introduceer hiervoor GEEN eigen titelcomponent.

De frontmatter-title bevat alleen het onderwerp:

    title: Flowcharts

niet:

    title: Visual First Flowcharts


============================================================
5. GEEN BADGE ONDER DE TITEL
============================================================

Plaats geen Visual First-badge op de zelfstandige
Understanding-pagina.

Een badge op een week-, TSET- of PSET-pagina laat zien welke
representatie daar wordt gebruikt.

Op de zelfstandige Understanding-pagina bevindt de leerling
zich al in die representatiekennis.


============================================================
6. CONTENT INCLUDE
============================================================

Plaats de include altijd binnen:

    <div class="understanding-article-start"></div>

    --8<-- "understanding/_content/visual-first/[PAD]/[BESTAND].md"


De marker understanding-article-start staat direct vóór de include.
Understanding-CSS gebruikt deze marker om de eerste inhoudelijke H3
alleen op de zelfstandige wiki-pagina te verbergen wanneer deze
dezelfde naam heeft als de paginatitel.

De heading blijft in _content behouden zodat dezelfde inhoud:

- in een PSET;
- in een ander document;
- in een samengestelde PDF;

een natuurlijke inhoudelijke structuur houdt.


============================================================
7. EERSTE H3 IN _CONTENT
============================================================

Verwijder geen inhoudelijke heading uit _content alleen omdat
de zelfstandige wrapper al een paginatitel heeft.

Bijvoorbeeld:

Wrapper:

    # Visual First *Flowcharts*

_content:

    ### Flowcharts

Op de zelfstandige Understanding-pagina kan deze eerste H3
via CSS verborgen worden.

Bij een include elders blijft de heading zichtbaar.


============================================================
8. NAVIGATIE ONDER HET ARTIKEL
============================================================

Na de content:

    ---

Daaronder staat de navigatie binnen het betreffende
Visual First-cluster.

Gebruik:

    [← [VORIGE]]([VORIGE-LINK]) · [Terug naar [CLUSTER]]([INDEX-LINK]) · [[VOLGENDE] →]([VOLGENDE-LINK])

Bijvoorbeeld:

    [← Basics](basics.md) · [Terug naar Flowcharts](../../index.md#flowcharts) · [Loops →](loops.md)

Gebruik geen inline-code-opmaak in deze navigatie.


============================================================
9. VOLGORDE VAN ARTIKELEN
============================================================

Vorige/volgende volgt de inhoudelijk logische volgorde binnen
de representatie.

Deze volgorde moet ook geschikt zijn voor:

- zelfstandig terugzoeken;
- doorlopend lezen;
- latere PDF-samenstelling.

De volgorde is dus niet automatisch de volgorde waarin de
bestanden zijn aangemaakt.


============================================================
10. INDEX EN CLUSTER
============================================================

De Understanding-index bepaalt hoe Visual First-artikelen zijn
gegroepeerd.

Voorbeelden:

    Visual First
        IPO Diagram

        Flowcharts
            Basics
            Decisions & Branches

De wrapper herhaalt het cluster niet als extra regel boven de
inhoud.

Dus geen:

    Visual First · Flowcharts

onder de H1.


============================================================
11. TEMPLATE
============================================================

Gebruik altijd:

    template: understanding.html


============================================================
12. PAD TIJDENS REFACTOR
============================================================

Tijdens de bouwfase kan een include tijdelijk beginnen met:

    understanding_new/

Na de definitieve omschakeling wordt dit:

    understanding/

Deze tijdelijke naam hoort niet bij het uiteindelijke
architectuurcontract.


============================================================
LAATSTE ONTWERPCONTROLE
============================================================

[ ] Bevat frontmatter alleen de onderwerpstitel?
[ ] Wordt template understanding.html gebruikt?
[ ] Is de H1 geschreven als: # Visual First *[ONDERWERP]*?
[ ] Staat er geen badge onder de H1?
[ ] Staat er geen extra clusterregel boven de inhoud?
[ ] Staat understanding-article-start direct vóór de include?
[ ] Verwijst de include naar het juiste Visual First _content-bestand?
[ ] Is geen onderwijsinhoud toegevoegd aan de wrapper?
[ ] Is een dubbele eerste H3 alleen via CSS verborgen?
[ ] Staat onder de content een horizontale scheiding?
[ ] Kloppen vorige, cluster en volgende?
[ ] Ontbreekt een vorige- of volgende-link volledig wanneer het artikel
    het eerste of laatste artikel van een cluster is?
[ ] Worden geen lege of uitgeschakelde navigatielinks gebruikt?
[ ] Is de navigatievolgorde inhoudelijk logisch?
[ ] Zijn alle placeholders vervangen?
============================================================
-->

<div class="understanding-article-start"></div>

--8<-- "understanding/_content/visual-first/[PAD]/[BESTAND].md"


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