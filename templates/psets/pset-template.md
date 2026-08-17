---
title: [TITEL] — [minder vertrouwd / meer vertrouwd]
template: pset.html
---

# [Titel Problem Set]

<!--
============================================================
PSET ONTWERPREGELS
============================================================

SOURCE OF TRUTH
---------------
De inhoudelijke keuzes komen uit het moduleframework.

Neem daaruit voor deze PSET minimaal:
- probleemsituatie / context;
- computationeel probleem;
- ontwerpprincipe;
- ontwerpvraag;
- CT-domein;
- Python-focus;
- testcriterium;
- SLO-domein en leerdoel;
- CT-procesdimensie;
- CT-leerdoel.

Formuleringen uit het framework zijn bewust gekozen.
Parafraseer of vereenvoudig deze daarom niet zonder
inhoudelijke/didactische reden.


CT-PROCES
----------
Iedere PSET bevat de beweging:

    Formulating the Problem
            ↓
    Expressing the Solution

Beide zijn dus altijd aanwezig.

Per week ligt voor de leerling de expliciete focus op één
van deze twee processen, zoals vastgelegd in het framework.

De andere procesdimensie verdwijnt NIET.


CONTEXT
-------
De context is onderdeel van het probleemontwerp en niet
alleen een verhaaltje om de programmeeropdracht heen.

De leerling moet vanuit een concrete probleemsituatie naar
een computationeel oplosbaar probleem bewegen.


CS50 ALS DIDACTISCHE INSPIRATIE
--------------------------------
Van CS50 nemen we vooral principes over voor begeleiding:

- probleem eerst;
- niet onmiddellijk de oplossingsroute geven;
- kleine, functionele tekstblokken;
- scaffolding op aanvraag via hints;
- probleem decomponeren wanneer nodig;
- hulp stapsgewijs opbouwen;
- leerling steeds weer zelf verder laten denken;
- testen behandelen als onderdeel van probleemoplossen.

CS50 bepaalt NIET de inhoud van onze PSET.
Het moduleframework blijft daarvoor leidend.


LESS / MORE
------------
Less Comfortable betekent niet automatisch een ander of
inhoudelijk eenvoudiger leerdoel.

Het verschil kan vooral zitten in de hoeveelheid scaffolding:
- meer tussenstappen;
- uitgebreidere hints;
- meer ondersteuning bij representeren;
- kleinere denkstappen.

More Comfortable kan dezelfde kernconcepten gebruiken met
minder ondersteuning en/of een complexere toepassing.


TEKST EN LEESBAARHEID
----------------------
Schrijf in samenhangende, functionele tekstblokken.

Gebruik niet na iedere losse zin een lege Markdown-regel.
Een lege regel maakt doorgaans een nieuwe paragraaf en
veroorzaakt daardoor ook extra visuele ruimte.

Nieuwe alinea = nieuwe inhoudelijke gedachte.
-->


<!-- ========================================================
     BADGES
     ========================================================

     Kies badges vanuit het framework:
     - Less / More Comfortable
     - Python-focus
     - Visual First-representatie
     - CT-domein
     - CT-procesdimensie
     ======================================================== -->

--8<-- "includes/badges.html:[VARIANT]"
--8<-- "includes/badges.html:[PYTHON]"
--8<-- "includes/badges.html:[VISUAL]"
--8<-- "includes/badges.html:[CT-DOMEIN]"
--8<-- "includes/badges.html:[CT-PROCES]"


## Waar werk je aan?

<!--
============================================================
WAAR WERK JE AAN?
============================================================

FUNCTIE
-------
Deze sectie maakt expliciet waaraan de leerling werkt.

Heeft drie functies:
1. transparantie voor de leerling;
2. zichtbaarheid van de samenhang in de leerlijn;
3. verantwoording richting schoolexamen en landelijke eisen.

ONTWERPREGELS
--------------
- Baseer doelen rechtstreeks op het moduleframework.
- Behoud de zorgvuldig gekozen terminologie.
- Laat de verschillende lagen van de leerlijn terugkomen.
- Formuleer als wat de leerling na/door deze PSET kan.
- Maak er geen lijst losse Python-commando's van.
-->

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **[...]** ...
- Ik kan **[...]** ...
- Ik kan **[...]** ...
- Ik kan **[...]** ...


## Probleem

<!--
============================================================
PROBLEEM
============================================================

FUNCTIE
-------
Van betekenisvolle context naar een computationeel probleem.

De sectie moet de basis leggen voor:

    Formulating the Problem
            ↓
    Expressing the Solution

BRON
----
Gebruik rechtstreeks uit het framework:

1. Probleemsituatie
2. Computationeel probleem
3. Ontwerpprincipe
4. Ontwerpvraag

ONTWERPREGELS
--------------
- Begin vanuit de concrete context.
- Maak duidelijk wat het computersysteem moet bereiken.
- Gebruik de zorgvuldig geformuleerde probleemstelling uit
  het framework.
- Eindig waar mogelijk met de ontwerpvraag.
- Geef nog GEEN oplossingsroute.
- Geef nog GEEN algoritme.
- Geef nog GEEN complete voorwaarden of code als de leerling
  die juist zelf moet formuleren.

De leerling moet na deze sectie begrijpen:
"Wat is het probleem dat ik moet oplossen?"

Niet noodzakelijk:
"Hoe ga ik het oplossen?"
-->

[Concrete probleemsituatie uit het framework.]

[Computationeel probleem uit het framework.]

**[Ontwerpvraag uit het framework.]**


## Demo

<!--
============================================================
DEMO
============================================================

FUNCTIE
-------
De leerling kan ervaren wat het uiteindelijke programma doet
voordat duidelijk wordt hoe het programma is gebouwd.

ONTWERPREGELS
--------------
- Maak de demo pas wanneer de solution gereed is.
- Demo toont WAT het systeem doet.
- Demo toont NIET HOE het systeem is geïmplementeerd.
- Gebruik exact gedrag dat overeenkomt met de uiteindelijke
  specificatie/solution.
- Laat de relevante context herkenbaar terugkomen.

Een demo is gewenst wanneer het eindproduct interactief of
anderszins zinvol demonstreerbaar is.
-->

[DEMO LATER TOEVOEGEN]


## Background

<!--
============================================================
BACKGROUND — ALLEEN INDIEN NODIG
============================================================

DIT IS EEN OPTIONELE SECTIE.

Gebruik Background alleen wanneer de leerling context of een
bestaande technische omgeving moet begrijpen voordat het
probleem zinvol kan worden opgelost.

Bijvoorbeeld:
- startercode;
- meerdere bestanden;
- een dataset;
- API;
- bestaand computersysteem;
- bestandsstructuur;
- domeinkennis die noodzakelijk is voor de opdracht.

NIET gebruiken om de probleemomschrijving nogmaals te
vertellen.

Vraag:
"Heeft de leerling kennis over de omgeving/context nodig die
noodzakelijk is om het probleem te begrijpen, maar niet tot
de oplossing zelf behoort?"

Nee -> verwijder deze hele sectie.
-->

[Alleen invullen indien nodig.]


## Understanding

<!--
============================================================
UNDERSTANDING
============================================================

FUNCTIE
-------
De leerling bouwt voldoende begrip op om zelf aan de
oplossing te kunnen werken.

Understanding is NIET automatisch:
"hier is de Python-theorie die je nodig hebt."

Het moet probleemgericht zijn.

MOGELIJKE VRAGEN
-----------------
- Welke informatie speelt een rol?
- Welke situaties kunnen ontstaan?
- Wat moet een computer expliciet weten?
- Welke relaties zijn belangrijk?
- Welke concepten zijn nodig?
- Welke bestaande kennis kan worden toegepast?
- Welke nieuwe Python-kennis is nodig?

CT
--
Bewaak hier de relatie met Formulating the Problem en
Expressing the Solution.

De focusdimensie van deze week krijgt extra nadruk, maar
beide processen blijven aanwezig.

ALGEMENE UNDERSTANDING-PAGINA'S
--------------------------------
Verwijs waar nuttig naar bestaande kennisbronnen.
Kopieer algemene theorie niet onnodig in iedere PSET.

De PSET moet de algemene kennis verbinden met DIT probleem.
-->

[Probleemgerichte Understanding.]

[Eventuele link naar algemene Understanding-pagina.]


## Specificatie

<!--
============================================================
SPECIFICATIE
============================================================

FUNCTIE
-------
Exact vastleggen waaraan de uiteindelijke oplossing moet
voldoen.

WEL
---
- vereist gedrag;
- invoer;
- uitvoer;
- grenzen;
- technische eisen wanneer deze onderdeel zijn van het
  leerdoel;
- toetsbare criteria;
- eventueel verplichte Python-concepten.

NIET
----
- stap-voor-stap oplossingsroute;
- compleet algoritme;
- complete code;
- denkwerk uitvoeren dat volgens het framework bij de
  leerling hoort.

TEST
----
Iedere eis moet in principe controleerbaar zijn.

Vraag:
"Beschrijven we hier WAT de oplossing moet kunnen, of zijn
we al aan het vertellen HOE de leerling haar moet bouwen?"

Het eerste hoort hier.
-->

Je programma moet:

- [...];
- [...];
- [...].

[Eventuele technische eis.]

[Belangrijk eindcriterium.]


## Hints

<!--
============================================================
HINTS
============================================================

FUNCTIE
-------
Scaffolding op aanvraag.

De leerling hoeft niet alle hints te lezen.
Iedere hint neemt één obstakel weg en geeft het probleem
daarna weer terug aan de leerling.

BASISPRINCIPE
--------------
Bouw hulp op van abstract naar concreet:

    denken
       ↓
    structureren / decomponeren
       ↓
    representeren (Visual First)
       ↓
    vertalen naar programmeren

Niet iedere PSET hoeft exact drie hints te hebben.
Het probleem bepaalt hoeveel ondersteuning nodig is.

LESS COMFORTABLE
----------------
Hier mag de ladder uitgebreider zijn:
- kleinere denkstappen;
- meer decompositie;
- meer ondersteuning bij representatie;
- eventueel kleine syntaxvoorbeelden.

MORE COMFORTABLE
----------------
Minder scaffolding.
Laat grotere delen van de oplossingsroute bij de leerling.

BELANGRIJK
-----------
Een hint mag een obstakel verkleinen, maar moet bij voorkeur
niet de complete oplossing prijsgeven.
-->

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.


??? hint "1 — [DENKVRAAG / FORMULATING]"

    [Help de leerling het probleem te structureren.]

    [Nog geen complete oplossingsroute of code.]


??? hint "2 — [REPRESENTATIE / VISUAL FIRST]"

    [Help de leerling de oplossing zichtbaar te maken.]

    [Gebruik de Visual First-representatie die bij deze week hoort.]


??? hint "3 — [BRUG NAAR PROGRAMMEREN]"

    [Geef alleen de noodzakelijke programmeerkennis/syntax.]

    ```python
    # eventueel een klein GENERIEK voorbeeld
    ```

    [Laat de leerling het eigen ontwerp zelf verder vertalen.]


## Testen

<!--
============================================================
TESTEN
============================================================

FUNCTIE
-------
Testen is onderdeel van probleemoplossen, niet alleen een
controle achteraf.

De leerling leert denken in:

    testgeval
        ↓
    invoer
        ↓
    verwachte uitkomst
        ↓
    werkelijke uitkomst
        ↓
    vergelijken

LANGERE LEERLIJN
-----------------
Deze werkwijze bereidt conceptueel voor op later
geautomatiseerd testen en pytest.

Wanneer pytest later wordt geïntroduceerd, moet herkenbaar
zijn dat Python dezelfde vergelijking automatiseert die de
leerling eerder handmatig uitvoerde.

ONTWERPREGELS
--------------
- Baseer tests op mogelijke routes/situaties uit het algoritme.
- Laat leerlingen VOORAF de verwachte uitkomst bepalen.
- Test niet alleen het standaardgeval.
- Gebruik het testcriterium uit het framework.
- Laat waar passend grensgevallen en uitzonderingen testen.
- Een test moet een reden hebben.

Laat de leerling uiteindelijk kunnen beantwoorden:
"Waarom tonen deze testgevallen aan dat mijn oplossing
voldoet?"
-->

Een programma is pas betrouwbaar als je controleert of **[relevant criterium uit het framework]**.

Bedenk voor iedere relevante situatie:

- welke **invoer** je gebruikt;
- welke **uitkomst je verwacht**;
- welke **uitkomst je programma werkelijk geeft**.

Gebruik bijvoorbeeld een tabel als deze:

| Test | Invoer | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | ------ | ------------------ | ------------------- |
| 1    |        |                    |                     |
| 2    |        |                    |                     |
| 3    |        |                    |                     |

[Benoem eventueel minimale/verplichte testcategorieën.]

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan waar je algoritme of programma iets anders doet dan je had verwacht.

**[Afsluitende vraag gekoppeld aan het testcriterium uit het framework.]**


## Inleveren

<!--
============================================================
INLEVEREN
============================================================

FUNCTIE
-------
Korte eindcontrole. Hier wordt geen nieuwe leerstof meer
geïntroduceerd.

Controleer:
- specificatie;
- testen;
- relevante CT-/ontwerpkeuzes kunnen uitleggen;
- relatie tussen representatie en code kunnen uitleggen;
- Git;
- portfolio.

PLANNING
--------
Geen deadline op de individuele PSET-pagina.

Deadlines staan uitsluitend op de PSET-index.
Daarmee bestaat voor planning één source of truth.
-->

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt de relevante situaties met **testgevallen** gecontroleerd;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit het probleem tot je **oplossing** bent gekomen;
- je kunt uitleggen hoe je ontwerp/representatie is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio [NUMMER]** bij.