---
title: [TITEL]
template: pset.html
week: [NUMMER]
level: [less / more]

understanding:
  - [UNDERSTANDING-ID]
---

# [Titel Problem Set]

<!--
============================================================
PSET — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------
Deze template is niet alleen een Markdown-skelet.

De template legt vast HOE een Problem Set binnen deze module
wordt ontworpen.

De onderwijsinhoud wordt NIET door deze template bepaald.
Daarvoor is het moduleframework leidend.



============================================================
0. METADATA-CONTRACT
============================================================

Gebruik in de frontmatter:

    title: [TITEL]
    template: pset.html
    week: [NUMMER]
    level: [less / more]

    understanding:
      - [UNDERSTANDING-ID]

`title` bevat alleen de inhoudelijke titel van de opdracht.
Zet `minder vertrouwd` of `meer vertrouwd` NIET in `title`.

`week` koppelt de PSET structureel aan de juiste week.

`level` bevat uitsluitend:

    less

of:

    more

De leerlingzichtbare formulering `minder vertrouwd` /
`meer vertrouwd` blijft presentatie en wordt niet in `title`
opgeslagen.

`understanding` bevat de stabiele IDs van de Understanding-
onderdelen die deze PSET gebruikt. Laat het veld weg wanneer
geen Understanding-verwijzingen nodig zijn.

De renderpipeline gebruikt deze IDs afhankelijk van de
uitvoervorm.

In de complete Module-PDF wordt `understanding_reference(...)`
gebruikt om een verwijzing naar de centrale Understanding-
pagina's met paginanummer(s) op te bouwen.

Op de website blijft de centrale Understanding-content inline
in de PSET beschikbaar.


============================================================
1. ONDERWIJSINHOUDELIJKE HIËRARCHIE
============================================================

Gebruik bij het ontwerpen altijd deze volgorde:

1. MODULEFRAMEWORK
   Bepaalt de onderwijsinhoud en de plaats in de leerlijn.

2. WEEKONTWERP / PSET-OMSCHRIJVING
   Bepaalt het concrete probleem en, indien van toepassing,
   de Less/More-variant.

3. PSET-TEMPLATE
   Bepaalt hoe deze inhoud didactisch wordt uitgewerkt en
   gepresenteerd.

4. EERDERE PSETS
   Zijn voorbeelden van stijl en toepassing, maar zijn nooit
   bron voor nieuwe onderwijsinhoud.

Bij een conflict is het MODULEFRAMEWORK inhoudelijk leidend.

Vul ontbrekende onderwijsinhoud niet zelfstandig in omdat
een onderdeel toevallig in deze template voorkomt.

Als een essentiële ontwerpkeuze niet uit het framework of
weekontwerp volgt, moet die keuze eerst expliciet worden
gemaakt voordat de leerlingtekst wordt geschreven.


============================================================
2. SOURCE OF TRUTH — MODULEFRAMEWORK
============================================================

Bepaal vóór het schrijven minimaal:

- probleemsituatie / context;
- computationeel probleem;
- ontwerpprincipe;
- ontwerpvraag;
- CT-domein;
- Python-focus;
- Visual First-representatie;
- testcriterium;
- SLO-domein en leerdoel;
- CT-procesdimensie;
- CT-leerdoel.

Gebruik de formuleringen uit het framework zorgvuldig.

Parafraseer of vereenvoudig deze niet zonder
inhoudelijke/didactische reden.


============================================================
3. ONTWERPANALYSE VÓÓR HET SCHRIJVEN
============================================================

Bepaal eerst:

PROBLEEM
- Wat is de concrete probleemsituatie?
- Wat maakt dit een computationeel probleem?
- Wat moet het computersysteem uiteindelijk bereiken?
- Welke ontwerpvraag staat centraal?

LEERLIJN
- Welke bestaande kennis mag bekend worden verondersteld?
- Welke nieuwe kennis hoort bij deze week?
- Welke Python-concepten zijn aan de beurt?
- Welke CT-kennis en -vaardigheden staan centraal?
- Welke Visual First-representatie hoort hierbij?

CT-PROCES
- Wat moet de leerling zelf formuleren?
- Wat moet de leerling als oplossing uitdrukken?
- Welke procesdimensie heeft deze week expliciete focus?

SCAFFOLDING
- Welk denkwerk MOET bij de leerling blijven?
- Welke kennis moet Understanding beschikbaar maken?
- Welke ondersteuning hoort alleen in Hints?
- Welke informatie zou de oplossing te vroeg weggeven?

TESTEN
- Welke routes, gevallen, combinaties, grenzen of andere
  relevante situaties ontstaan uit het probleem?
- Wat zegt het testcriterium uit het framework?
- Hoe kan een leerling aantonen dat de oplossing voldoet?

Schrijf pas daarna de PSET.


============================================================
4. CT-PROCES
============================================================

Iedere PSET bevat de beweging:

    Formulating the Problem
            ↓
    Expressing the Solution

Beide procesdimensies zijn altijd aanwezig.

Per week ligt voor de leerling de expliciete focus op één
van deze twee processen, zoals vastgelegd in het framework.

De andere procesdimensie verdwijnt NIET.

De PSET moet zichtbaar maken hoe de leerling vanuit een
probleem naar een uitdrukbare en uiteindelijk programmeerbare
oplossing beweegt.


============================================================
5. CONTEXT
============================================================

De context is onderdeel van het probleemontwerp.

Het is geen verhaaltje dat achteraf om een programmeeropdracht
heen wordt gezet.

De leerling moet vanuit een concrete probleemsituatie naar
een computationeel oplosbaar probleem bewegen.

De context moet daarom functioneel noodzakelijk of betekenisvol
zijn voor het probleem dat wordt opgelost.


============================================================
6. CS50 ALS DIDACTISCHE INSPIRATIE
============================================================

Gebruik vooral deze principes:

- probleem eerst;
- niet onmiddellijk de oplossingsroute geven;
- kleine, functionele tekstblokken;
- scaffolding op aanvraag;
- decomponeren wanneer nodig;
- hulp stapsgewijs opbouwen;
- leerling steeds weer zelf verder laten denken;
- testen behandelen als onderdeel van probleemoplossen.

CS50 bepaalt NIET de onderwijsinhoud.

Het moduleframework blijft daarvoor leidend.


============================================================
7. LESS / MORE COMFORTABLE
============================================================

Less en More zijn twee routes binnen dezelfde leerlijn.

LESS COMFORTABLE
kan meer ondersteuning bieden door:
- kleinere denkstappen;
- meer decompositie;
- uitgebreidere hints;
- meer ondersteuning bij representeren;
- kleinere bruggen naar programmeren.

MORE COMFORTABLE
kan meer zelfstandigheid en/of computationele complexiteit
vragen door bijvoorbeeld:
- minder scaffolding;
- een grotere probleemruimte;
- meer mogelijke situaties;
- diepere beslisstructuren;
- een complexere toepassing van dezelfde kernconcepten.

BELANGRIJK:

More betekent NIET automatisch:
"dezelfde opdracht maar moeilijker".

More mag ook GEEN toekomstige leerstof naar voren halen
alleen om de opdracht moeilijker te maken.

De gekozen uitbreiding moet passen bij het framework en
de plaats van de PSET in de leerlijn.


============================================================
8. VASTE HOOFDSTRUCTUUR
============================================================

Gebruik in beginsel:

# Titel

Badges
[optioneel: video]

## Waar werk je aan?

## Probleem

## Demo

## Background
[alleen indien functioneel noodzakelijk]

## Understanding

## Opdracht

### Specificatie

### Hints

### Testen

### Inleveren



<!--
============================================================
CONTENT-ELEMENTEN — OPTIONEEL
============================================================

Binnen de bestaande secties mogen functionele content-elementen
worden toegevoegd wanneer het PSET-ontwerp daar aanleiding toe geeft.

Denk bijvoorbeeld aan:

- codeblokken;
- tabellen;
- afbeeldingen;
- Mermaid-diagrammen;
- andere representaties die binnen de bestaande infrastructuur
  worden ondersteund.

Zo'n element maakt GEEN nieuwe vaste sectie van de PSET.

Gebruik een content-element alleen wanneer het inhoudelijk nodig is
op de plek waar het staat. Voeg dus niet automatisch een diagram,
afbeelding of tabel toe omdat de template die mogelijkheid biedt.

MERMAID

Wanneer Mermaid wordt gebruikt, bevat ieder Mermaid-blok direct na
de opening een stabiele ID:

```mermaid
%% id: [HERKENBARE-NAAM]-01

flowchart TD
    [DIAGRAM]
```

Regels:

- gebruik lowercase letters, cijfers en koppeltekens;
- gebruik een herkenbare inhoudelijke naam;
- nummer meerdere diagrammen met -01, -02, enzovoort;
- dezelfde afbeelding in Less en More mag bewust dezelfde ID hebben;
- dezelfde ID mag nooit voor verschillende Mermaid-broncode worden
  gebruikt;
- de buildpipeline maakt hieruit automatisch:

      build/assets/mermaid/sets/[MERMAID-ID].png

De Markdown verwijst NIET zelf naar de gegenereerde PNG.
De renderpipeline bepaalt hoe het diagram op web en in PDF wordt
weergegeven.
-->


============================================================
9. TEKST EN LEESBAARHEID
============================================================

Schrijf in samenhangende, functionele tekstblokken.

Gebruik niet na iedere losse zin een lege Markdown-regel.

Nieuwe alinea = nieuwe inhoudelijke gedachte.

Schrijf rechtstreeks voor de leerling.

Vermijd:
- overbodige uitleg;
- herhaling;
- docententaal;
- abstracte formuleringen zonder functie;
- informatie die pas later nodig is.

Gebruik Engelse vaktermen wanneer deze bewust onderdeel zijn
van de leerlijn, bijvoorbeeld condition, branch of logical
operator. Gebruik terminologie consequent.
-->


<!-- ========================================================
     BADGES
     ========================================================

     Kies badges vanuit het framework/weekontwerp:

     - Less / More Comfortable
     - Python-focus
     - Visual First-representatie
     - CT-domein
     - CT-procesdimensie

     Voeg geen badge toe alleen omdat deze in een eerdere
     PSET voorkwam.
     ======================================================== -->

--8<-- "includes/badges.html:[VARIANT]"
--8<-- "includes/badges.html:[PYTHON]"
--8<-- "includes/badges.html:[VISUAL]"
--8<-- "includes/badges.html:[CT-DOMEIN]"
--8<-- "includes/badges.html:[CT-PROCES]"


<!-- ========================================================
     VIDEO — OPTIONEEL
     ========================================================

     Voeg alleen een video toe wanneer deze functioneel bij
     deze PSET hoort.

     De video ondersteunt context of begrip, maar mag niet
     voortijdig de oplossingsroute prijsgeven.

     Gebruik een bestaande video-include uit videos.html.
     ======================================================== -->

<!-- --8<-- "includes/videos.html:[VIDEO]" -->


## Waar werk je aan?

<!--
============================================================
WAAR WERK JE AAN?
============================================================

FUNCTIE
-------
Maakt voor de leerling expliciet waaraan wordt gewerkt.

Heeft drie functies:

1. transparantie voor de leerling;
2. zichtbaarheid van de samenhang in de leerlijn;
3. verantwoording richting schoolexamen en landelijke eisen.

BRON
----
Baseer de leerdoelen rechtstreeks op het moduleframework en
de concrete functie van deze PSET.

Laat waar relevant verschillende lagen terugkomen:
- computationeel denken;
- ontwerpen / representeren;
- automatiseren;
- programmeren.

ONTWERPREGELS
--------------
- Behoud zorgvuldig gekozen terminologie.
- Formuleer als wat de leerling kan.
- Maak er geen lijst Python-commando's van.
- Voeg geen leerdoelen toe die niet door het framework of
  weekontwerp worden gedragen.
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

De sectie legt de basis voor:

    Formulating the Problem
            ↓
    Expressing the Solution

BRON
----
Gebruik uit het framework/weekontwerp:

1. Probleemsituatie
2. Computationeel probleem
3. Ontwerpprincipe
4. Ontwerpvraag

ONTWERPREGELS
--------------
- Begin vanuit de concrete context.
- Maak duidelijk wat het computersysteem moet bereiken.
- Maak zichtbaar waarom expliciete instructies/regels/data/
  beslissingen/etc. nodig zijn wanneer dat bij het probleem
  hoort.
- Eindig waar mogelijk met de ontwerpvraag.
- Geef nog GEEN oplossingsroute.
- Geef nog GEEN compleet algoritme.
- Geef nog GEEN code die het relevante denkwerk uitvoert.
- Geef geen voorwaarden, stappen of structuur cadeau wanneer
  de leerling die volgens het framework zelf moet formuleren.

Na deze sectie moet de leerling kunnen beantwoorden:

"Wat is het probleem dat ik moet oplossen?"

Niet noodzakelijk:

"Hoe ga ik het oplossen?"
-->

[Concrete probleemsituatie.]

[Computationeel probleem.]

[Eventueel noodzakelijke verduidelijking van het probleem.]

**[Ontwerpvraag.]**


## Demo

<!--
============================================================
DEMO
============================================================

FUNCTIE
-------
De leerling kan ervaren wat het uiteindelijke programma doet
zonder te zien hoe het programma is gebouwd.

ONTWERPREGELS
--------------
- Maak de demo pas wanneer de solution gereed is.
- Demo toont WAT het systeem doet.
- Demo toont NIET HOE het systeem is geïmplementeerd.
- Gebruik gedrag dat exact overeenkomt met de uiteindelijke
  specificatie/solution.
- Laat de relevante context herkenbaar terugkomen.

Een demo is gewenst wanneer het eindproduct interactief of
anderszins zinvol demonstreerbaar is.

Als een demo geen didactische functie heeft, kan deze sectie
worden verwijderd.
-->

[DEMO LATER TOEVOEGEN]


## Background

<!--
============================================================
BACKGROUND — OPTIONEEL
============================================================

VERWIJDER DEZE HELE SECTIE ALS HIJ NIET NODIG IS.

FUNCTIE
-------
Background geeft noodzakelijke informatie over een bestaande
omgeving of context die de leerling moet begrijpen voordat
het probleem zinvol kan worden opgelost.

Bijvoorbeeld:
- startercode;
- meerdere bestanden;
- dataset;
- API;
- bestaand computersysteem;
- bestandsstructuur;
- noodzakelijke domeinkennis.

Background is NIET:
- een herhaling van het probleem;
- een theorieles;
- Understanding;
- een verborgen oplossingsroute.

Beslisvraag:

"Heeft de leerling kennis over de omgeving/context nodig die
noodzakelijk is om het probleem te begrijpen, maar niet tot
de oplossing zelf behoort?"

Nee -> verwijder deze hele sectie.
-->

[Alleen invullen indien functioneel noodzakelijk.]


## Understanding

<!--
============================================================
UNDERSTANDING
============================================================

FUNCTIE
-------
Understanding maakt precies genoeg conceptuele en/of
technische kennis beschikbaar zodat de leerling ZELF verder
kan werken aan het probleem.

Understanding is GEEN uitgewerkte oplossing.

Understanding is ook niet automatisch:
"hier is alle Python-theorie die je nodig hebt."

PROBLEEMGERICHT
---------------
Vraag:

"Welke kennis ontbreekt nog om de leerling zelfstandig over
DIT probleem te kunnen laten denken?"

Dat kan bijvoorbeeld gaan over:
- welke informatie een rol speelt;
- mogelijke situaties;
- relaties tussen gegevens;
- relevante concepten;
- bestaande kennis;
- nieuwe Python-kennis;
- een Visual First-representatie.

GRENZEN
-------
Understanding mag:
- concepten uitleggen;
- generieke voorbeelden geven;
- syntax uitleggen;
- bestaande kennis activeren.

Understanding mag NIET:
- het algoritme voor deze PSET geven;
- de beslissingen voor deze PSET volledig invullen;
- een complete flowchart voor deze PSET geven;
- code geven die feitelijk de PSET oplost;
- denkwerk overnemen dat volgens het framework bij de
  leerling hoort.

ALGEMENE UNDERSTANDING
----------------------
Algemene kennis wordt centraal onderhouden.

De PSET registreert in de frontmatter welke stabiele
Understanding-ID's zij gebruikt.

Dezelfde centrale Understanding-content kan vervolgens in
verschillende uitvoervormen anders worden gepresenteerd:

WEBSITE
-------
De benodigde `_content` wordt inline in de PSET opgenomen.

COMPLETE MODULE-PDF
-------------------
De PSET neemt de Understanding niet opnieuw volledig op.
Gebruik daar:

    {{ understanding_reference(understanding) }}

De renderer bouwt daarmee een verwijzing naar de centrale
Understanding-pagina's en de bijbehorende paginanummers.

Schrijf nooit vaste paginanummers in de PSET zelf.

Kopieer algemene theorie niet opnieuw naar verschillende
PSET's wanneer een bestaande Understanding kan worden
hergebruikt.

De PSET verbindt algemene kennis met het probleem; de
algemene Understanding hoeft het specifieke probleem niet
op te lossen.

CT
--
Bewaak de relatie met:

Formulating the Problem
        ↓
Expressing the Solution

De focusdimensie van de week krijgt extra nadruk, maar beide
processen blijven aanwezig.
-->

{{ understanding_reference(understanding) }}


## Opdracht

<!--
============================================================
OPDRACHT
============================================================

FUNCTIE
-------
Markeert de overgang van:

    begrijpen / voorbereiden
             ↓
    zelf construeren en controleren

Vanaf hier gebruikt de leerling het opgebouwde begrip om
zelf het probleem op te lossen.

De korte introductiezin verbindt Understanding opnieuw met
de concrete PSET.
-->

Nu ga je deze kennis gebruiken om het probleem van **[TITEL]** op te lossen.


### Specificatie

<!--
============================================================
SPECIFICATIE
============================================================

FUNCTIE
-------
Leg exact vast WAT de uiteindelijke oplossing moet kunnen.

WEL
---
- vereist gedrag;
- invoer;
- uitvoer;
- functionele grenzen;
- technische eisen wanneer deze onderdeel zijn van het
  leerdoel;
- toetsbare criteria;
- verplichte Python-concepten wanneer inhoudelijk nodig.

NIET
----
- stap-voor-stap oplossingsroute;
- compleet algoritme;
- complete flowchart;
- complete code;
- denkwerk dat volgens het framework bij de leerling hoort.

CONTROLE
--------
Iedere eis moet in principe controleerbaar zijn.

Vraag bij iedere regel:

"Beschrijven we WAT de oplossing moet kunnen, of vertellen
we al HOE de leerling haar moet bouwen?"

Alleen het eerste hoort hier.
-->

Je programma moet:

- [...];
- [...];
- [...];
- [...].

[Eventuele technische eis.]

[Belangrijk eindcriterium.]


### Hints

<!--
============================================================
HINTS
============================================================

FUNCTIE
-------
Scaffolding op aanvraag.

De leerling hoeft niet alle hints te lezen.

Iedere hint neemt één concreet cognitief obstakel weg en
geeft het probleem daarna weer terug aan de leerling.

PROGRESSIVE DISCLOSURE
----------------------
Bouw ondersteuning waar passend op van:

    denken over het probleem
             ↓
    structureren / decomponeren
             ↓
    representeren (Visual First)
             ↓
    brug naar programmeren

Dit is GEEN verplicht vierstappenmodel.

Het aantal hints volgt uit de cognitieve obstakels van de
specifieke PSET.

Gebruik dus 2, 3, 4, 5 of een ander passend aantal hints
wanneer het probleem daarom vraagt.

Iedere volgende hint mag meer prijsgeven wanneer dat nodig
is om een nieuw obstakel weg te nemen, maar laat daarna
opnieuw zoveel mogelijk denkwerk bij de leerling.

LESS COMFORTABLE
----------------
Mag een uitgebreidere ladder bevatten:
- kleinere denkstappen;
- meer decompositie;
- meer ondersteuning bij representeren;
- kleine generieke syntaxvoorbeelden.

MORE COMFORTABLE
----------------
Gebruik in beginsel minder scaffolding en laat grotere delen
van de oplossingsroute bij de leerling.

Een complexer More-probleem kan desondanks méér hints nodig
hebben wanneer er meer verschillende cognitieve obstakels
bestaan.

BELANGRIJK
----------
Een hint mag een obstakel verkleinen.

Een hint mag niet ongemerkt de volledige oplossing worden.

UITVOERVORM
-----------
De inhoud en volgorde van hints blijven in iedere uitvoervorm
gelijk.

Website:
- hints blijven uitklapbaar;
- de leerling kiest welke hint wordt geopend.

PDF:
- alle hints worden zichtbaar opgenomen;
- de renderer markeert ze als herkenbare HINT-blokken;
- er wordt geen aparte PDF-versie van de hintinhoud onderhouden.
-->

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.


??? hint "1 — [EERSTE COGNITIEVE OBSTAKEL]"

    [Help de leerling verder zonder de oplossing over te nemen.]

    [Geef het probleem daarna weer terug aan de leerling.]


??? hint "2 — [VOLGEND COGNITIEF OBSTAKEL]"

    [Passende scaffolding.]


??? hint "3 — [BIJVOORBEELD VISUAL FIRST]"

    [Help de leerling de eigen oplossing zichtbaar te maken.]

    [Gebruik de Visual First-representatie uit het framework.]


??? hint "4 — [EVENTUELE BRUG NAAR PROGRAMMEREN]"

    [Geef alleen noodzakelijke programmeerkennis/syntax.]

    ```python
    # alleen een klein GENERIEK voorbeeld indien nodig
    ```

    [Laat de leerling het eigen ontwerp zelf vertalen.]

<!--
Verwijder, voeg toe en herschik hints op basis van het
daadwerkelijke probleem.
-->


### Testen

<!--
============================================================
TESTEN
============================================================

FUNCTIE
-------
Testen is onderdeel van probleemoplossen.

Het is niet alleen een controle nadat het programmeren klaar
is.

De leerling leert denken in:

    testgeval
        ↓
    invoer / beginsituatie
        ↓
    verwachte uitkomst
        ↓
    werkelijke uitkomst
        ↓
    vergelijken
        ↓
    analyseren / verbeteren


TESTSTRATEGIE
-------------
Ontwerp deze sectie NIET vanuit een standaardtabel.

Leid de teststrategie eerst af uit:

1. het computationele probleem;
2. het algoritme / oplossingsmodel;
3. relevante routes, gevallen, combinaties, grenzen of
   uitzonderingen;
4. het testcriterium uit het framework.

Bepaal DAARNA welke testvorm of tabel daarbij past.

Voorbeelden:

- beslisstructuur
  -> relevante routes/situaties;

- combinatorisch probleem
  -> relevante of alle combinaties;

- numerieke grens
  -> waarden onder, op en boven de grens;

- invoerverwerking
  -> relevante invoercategorieën;

- herhaling
  -> begin-, tussen- en eindsituaties.

ONTWERPREGELS
--------------
- Laat leerlingen VOORAF de verwachte uitkomst bepalen.
- Test niet alleen het standaardgeval.
- Gebruik het testcriterium uit het framework.
- Test grensgevallen wanneer die inhoudelijk relevant zijn.
- Streef naar systematisch testen in plaats van willekeurige
  voorbeelden.
- Iedere test moet een reden hebben.

De leerling moet uiteindelijk kunnen beantwoorden:

"Waarom tonen deze testgevallen aan dat mijn oplossing
voldoet?"

LANGERE LEERLIJN
----------------
Deze werkwijze bereidt conceptueel voor op later
geautomatiseerd testen en pytest.

Wanneer pytest later wordt geïntroduceerd, moet herkenbaar
zijn dat Python dezelfde vergelijking automatiseert die de
leerling eerder handmatig uitvoerde.
-->

Een programma is pas betrouwbaar als je controleert of **[testcriterium uit het framework / probleem]**.

[Bepaal hier de probleemafhankelijke teststrategie.]

Bedenk voor iedere test:

- welke **invoer/beginsituatie** je gebruikt;
- welke **uitkomst je verwacht**;
- welke **uitkomst je programma werkelijk geeft**.

<!--
PAS DE TABEL AAN HET PROBLEEM AAN.

Onderstaande tabel is uitsluitend een mogelijke basis.
-->

| Test | Invoer | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | ------ | ------------------ | ------------------- |
| 1    |        |                    |                     |
| 2    |        |                    |                     |
| 3    |        |                    |                     |

[Benoem minimale testcategorieën, routes, combinaties,
grensgevallen of andere noodzakelijke gevallen.]

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan waar je algoritme of programma iets anders doet dan je had verwacht.

**[Afsluitende vraag gekoppeld aan het testcriterium.]**


### Inleveren

<!--
============================================================
INLEVEREN
============================================================

FUNCTIE
-------
Korte eindcontrole.

Hier wordt GEEN nieuwe leerstof geïntroduceerd.

De controle verbindt:
- specificatie;
- testen;
- relevante CT-/ontwerpkeuzes;
- representatie;
- code;
- Git;
- portfolio.

MAATWERK
--------
Pas de inhoudelijke bullets aan de PSET aan.

Noem bijvoorbeeld expliciet:
- beslisstructuur;
- algoritme;
- flowchart;
- datarepresentatie;
- decompositie;

wanneer dit voor deze PSET daadwerkelijk centraal stond.

PLANNING
--------
Plaats GEEN deadline op de individuele PSET-pagina.

Deadlines staan uitsluitend op de PSET-index.

Daarmee bestaat voor planning één source of truth.
-->

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt de relevante situaties systematisch met **testgevallen** gecontroleerd;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit het probleem tot je **oplossing** bent gekomen;
- je kunt uitleggen hoe je ontwerp/representatie is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio [NUMMER]** bij.


<!--
============================================================
LAATSTE ONTWERPCONTROLE
============================================================

Controleer vóór publicatie:

FRAMEWORK
[ ] Komt alle onderwijsinhoud uit het framework/weekontwerp?
[ ] Zijn geen nieuwe leerdoelen of concepten toegevoegd?
[ ] Is de juiste CT-procesfocus zichtbaar?

PROBLEEM
[ ] Is de context functioneel?
[ ] Is het computationele probleem duidelijk?
[ ] Blijft relevant denkwerk bij de leerling?
[ ] Is de ontwerpvraag herkenbaar?

UNDERSTANDING
[ ] Geeft Understanding noodzakelijke kennis?
[ ] Voorkomt Understanding dat de oplossing wordt weggegeven?
[ ] Is bestaande algemene Understanding hergebruikt?
[ ] Staan de juiste stabiele Understanding-ID's in de frontmatter?
[ ] Gebruikt de Module-PDF `understanding_reference(understanding)`?
[ ] Bevat de PSET geen hardcoded Understanding-paginanummers?

LESS / MORE
[ ] Past de variant bij dezelfde plaats in de leerlijn?
[ ] Komt eventuele extra complexiteit inhoudelijk ergens vandaan?
[ ] Is More niet kunstmatig moeilijk gemaakt?

HINTS
[ ] Heeft iedere hint een duidelijke functie?
[ ] Is ondersteuning progressief?
[ ] Kan een leerling na iedere hint weer zelfstandig verder?
[ ] Wordt nergens onnodig de volledige oplossing gegeven?
[ ] Blijven inhoud en volgorde van hints gelijk tussen web en PDF?

TESTEN
[ ] Volgt de teststrategie uit het probleem?
[ ] Zijn relevante routes/gevallen/combinaties/grenzen gedekt?
[ ] Bepaalt de leerling verwachtingen vóór uitvoering?
[ ] Sluit de afsluitende vraag aan op het testcriterium?

PAGINA
[ ] Kloppen badges?
[ ] Is Background verwijderd wanneer deze niet nodig is?
[ ] Is Demo ingevuld of bewust nog als ontwikkelonderdeel gemarkeerd?
[ ] Zijn ongebruikte placeholders en ontwerpcomments voor zover
    gewenst verwijderd?
[ ] Staat er geen individuele deadline op deze pagina?
============================================================
-->