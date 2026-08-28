---
title: Problem Set [NUMMER]
template: pset-index.html
week: [NUMMER]

resources:
  - [RESOURCE-GROEP]
---

# Problem Set [NUMMER]

<!--
============================================================
PSET-INDEX — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------
Deze template legt het gerealiseerde ontwerp van de
PSET-index vast.

De PSET-index is de centrale startpagina voor de individuele
Problem Sets van één week.

De pagina maakt voor de leerling zichtbaar:

- hoe het werken aan de Problem Set is georganiseerd;
- welke opdrachten gemaakt moeten worden;
- welke Less/More-keuzes beschikbaar zijn;
- welke aanvullende uitleg en bronnen beschikbaar zijn;
- wanneer de volledige Problem Set af moet zijn;
- wanneer extra ondersteuning beschikbaar is.

De PSET-index bepaalt NIET zelfstandig de onderwijsinhoud.



============================================================
0. METADATA-CONTRACT
============================================================

Gebruik in de frontmatter:

    title: Problem Set [NUMMER]
    template: pset-index.html
    week: [NUMMER]

    resources:
      - [RESOURCE-GROEP]

`resources` bevat de stabiele ID van de resourcegroep die deze
PSET gebruikt. Deze technische declaratie wordt door de
PDF-renderpipeline gebruikt om de resources voor de PDF-build
te inventariseren.

`title` is hier bewust de volledige HTML-paginatitel.

`week` is daarnaast de structurele metadata waarmee web- en
PDF-rendering de PSET-index aan de juiste week kunnen koppelen.

Het weeknummer in `title` en `week` moet altijd gelijk zijn.


============================================================
1. BELANGRIJKE REGEL VOOR DEZE TEMPLATE
============================================================

De template beschrijft en borgt het gerealiseerde ontwerp.

Tijdens het abstraheren of invullen van deze template worden
GEEN nieuwe leerlingzichtbare ontwerpkeuzes ingevoerd.

Dat betekent onder andere:

- geen headings toevoegen of veranderen;
- geen secties toevoegen of verplaatsen;
- geen vaste leerlingtekst herschrijven;
- geen andere presentatievorm kiezen;
- geen nieuwe badges introduceren;
- geen andere Less/More-formulering kiezen;

alleen omdat dat op dat moment beter lijkt.

Een nieuwe ontwerpkeuze wordt eerst apart besproken.

Pas wanneer die keuze bewust is gemaakt, wordt zij indien
nodig zowel in de gerealiseerde referentiepagina als in de
template doorgevoerd.


============================================================
2. ONDERWIJSINHOUDELIJKE HIËRARCHIE
============================================================

Gebruik bij het ontwerpen altijd deze volgorde:

1. MODULEFRAMEWORK
   Bepaalt de onderwijsinhoud en de plaats in de leerlijn.

2. WEEKONTWERP / PSET-ONTWERP
   Bepaalt de concrete opdrachten en Less/More-varianten.

3. PSET-INDEX-TEMPLATE
   Bepaalt hoe deze inhoud voor de leerling wordt ontsloten.

4. EERDERE PSET-INDEXEN
   Zijn voorbeelden van toepassing, maar nooit bron voor
   nieuwe onderwijsinhoud.

Bij een inhoudelijk conflict is het MODULEFRAMEWORK leidend.

Voeg dus geen:
- Python-concepten;
- CT-doelen;
- Visual First-representaties;
- procesdimensies;
- opdrachten;
- Less/More-uitbreidingen;

toe omdat deze in een eerdere week voorkwamen.


============================================================
3. FUNCTIE VAN DE PSET-INDEX
============================================================

De individuele PSET beantwoordt vooral:

    "Welk probleem ga ik oplossen en hoe werk ik eraan?"

De PSET-index beantwoordt vooral:

    "Wat moet ik voor deze Problem Set doen?"

De index is daarom een ROUTEKAART.

Het is geen:
- extra theorieles;
- samenvatting van de individuele opdrachten;
- plaats voor uitgebreide specificaties;
- plaats voor oplossingsstrategieën.


============================================================
4. SOURCE OF TRUTH — MODULEFRAMEWORK
============================================================

Bepaal vóór het invullen uit het framework minimaal:

- weeknummer / PSET-nummer;
- Python-focus;
- Visual First-representatie;
- CT-domein;
- CT-procesdimensie;
- plaats van de PSET in de leerlijn.

Bepaal uit het concrete PSET-ontwerp:

- welke opdrachten bij deze Problem Set horen;
- welke Less/More-varianten bestaan;
- welke opdrachten de leerling moet maken;
- in welke volgorde deze worden aangeboden.

Bepaal voor aanvullende bronnen:

- welke resourcegroepen bij deze Problem Set horen;
- welke resources daarin beschikbaar zijn;
- of deze resources werkelijk aansluiten op de inhoud van deze week.

De concrete resourcegegevens worden centraal beheerd en worden
niet opnieuw in de PSET-index opgeslagen.

Planning komt NIET uit het framework of uit deze template.

Daarvoor is schedule.yml de source of truth.


============================================================
5. ONTWERPANALYSE VÓÓR HET SCHRIJVEN
============================================================

Controleer eerst:

INHOUD
- Wat is volgens het framework de Python-focus?
- Welke Visual First-representatie hoort hierbij?
- Welk CT-domein staat centraal?
- Welke CT-procesdimensie heeft de focus?

ORGANISATIE
- Welke individuele PSET's horen bij deze week?
- Welke daarvan moet de leerling maken?
- Waar bestaat een Less/More-keuze?
- Welke volgorde is bedoeld?

LESS / MORE
- Welke varianten zijn daadwerkelijk ontworpen?
- Is voor de leerling alleen een keuze nodig, zonder de
  inhoudelijke verschillen hier al uit te leggen?

BRONNEN
- Welke resourcegroepen sluiten werkelijk aan?
- Zijn de juiste resource-ID's centraal aan deze groepen gekoppeld?
- Zijn deze aanvullend en niet noodzakelijk om ontbrekende
  uitleg in de module te compenseren?

PLANNING
- Wordt de deadline uit schedule.yml gehaald?
- Worden Vakflexmomenten uit schedule.yml gehaald?

Schrijf/vul pas daarna de index.


============================================================
6. VASTE LEERLINGZICHTBARE STRUCTUUR
============================================================

De gerealiseerde structuur is:

# Problem Set [NUMMER]

badges

Verantwoord leren

## Wat moet je doen?

## Aanvullende uitleg en bronnen

{{ resource_group("[RESOURCE-GROEP]") }}

## Wanneer moet het af zijn?

## Hulp nodig?

Deze structuur wordt niet tijdens het invullen van een nieuwe
week opnieuw ontworpen.


============================================================
7. TEKST EN LEESBAARHEID
============================================================

De index moet snel scanbaar blijven.

De leerling moet eenvoudig kunnen vinden:

- wat moet ik doen?
- welke variant kies ik?
- waar vind ik aanvullende uitleg en bronnen?
- wanneer moet het af zijn?
- waar kan ik extra hulp krijgen?

Gebruik korte, functionele tekstblokken.

Dupliceer geen theorie of specificaties uit individuele
PSET's.
-->


<!-- ========================================================
     BADGES
     ========================================================

     De badges beschrijven de inhoudelijke positie van de
     volledige Problem Set in de leerlijn.

     Kies ze vanuit het MODULEFRAMEWORK:

     - Python-focus
     - Visual First-representatie
     - CT-domein
     - CT-procesdimensie

     Gebruik op de index GEEN Less/More-badge.

     Less/More hoort bij de individuele PSET-variant.

     Voeg alleen badges toe die voor de volledige Problem Set
     gelden.
     ======================================================== -->

--8<-- "includes/badges.html:[PYTHON]"
--8<-- "includes/badges.html:[VISUAL]"
--8<-- "includes/badges.html:[CT-DOMEIN]"
--8<-- "includes/badges.html:[CT-PROCES]"


<!--
============================================================
VERANTWOORD LEREN
============================================================

FUNCTIE
-------
Dit is vaste modulebrede leerlingtekst.

Het blok maakt duidelijk:

- PSET's worden individueel gemaakt;
- overleggen, vragen stellen en hulp gebruiken mag;
- het leerproces is belangrijker dan alleen een werkend
  programma;
- AI moet niet worden gebruikt om het denkwerk uit te
  besteden;
- het portfolio maakt het leerproces zichtbaar;
- tijdens het schoolexamen moet de leerling zelfstandig
  kunnen laten zien wat hij/zij beheerst.

ONTWERPREGEL
------------
Deze tekst wordt niet per week opnieuw geschreven.

Wijzig hem alleen wanneer daarvoor een bewuste modulebrede
ontwerpbeslissing wordt genomen.
-->

!!! learning "Verantwoord leren"

    De opdrachten in een Problem Set maak je individueel. Je mag overleggen, vragen stellen en gebruikmaken van de aangeboden bronnen en hulp.

    Problem Sets zijn bedoeld om **zelf te leren programmeren en problemen op te lossen**. Het gaat niet alleen om een werkend programma, maar vooral om begrijpen welke keuzes je maakt en hoe je tot een oplossing komt.

    Gebruik AI daarom liever niet om opdrachten voor je uit te werken. Daarmee sla je een belangrijk deel van het leerproces over.

    In je portfolio laat je zien hoe je hebt gewerkt, welke keuzes je hebt gemaakt en wat je daarvan hebt geleerd. In week 11 moet je tijdens het schoolexamen zelfstandig laten zien dat je deze kennis en vaardigheden beheerst.


## Wat moet je doen?

<!--
============================================================
WAT MOET JE DOEN?
============================================================

FUNCTIE
-------
Geeft de leerling de concrete route door de Problem Set.

De beweging is:

    Git voorbereiden
          ↓
    opdracht(en) maken
          ↓
    Portfolio bijwerken

Gebruik hiervoor een genummerde lijst.


GIT
---
De leerling werkt vóór de PSET de lokale repository bij.

Tijdens het werken wordt regelmatig gecommit en gepusht,
zodat de ontwikkeling van het werk zichtbaar blijft.

Verwijs naar de centrale Git-Understanding.

Als deze Understanding nog niet bestaat, kan de geplande
link bewust tijdelijk blijven staan.


LESS / MORE
-----------
Wanneer een opdracht Less en More heeft, gebruik de
gerealiseerde formulering:

- "als je je minder vertrouwd voelt met de stof";
- "als je je meer vertrouwd voelt met de stof".

Maak hier geen:
- makkelijk/moeilijk;
- basis/gevorderd;
- zwak/sterk;

van.

De index hoeft de inhoudelijke verschillen tussen beide
varianten niet uit te leggen.

De leerling kiest hier de route; de individuele PSET bepaalt
de inhoud.


OPDRACHTEN
----------
Neem uitsluitend opdrachten op die daadwerkelijk voor deze
week zijn ontworpen.

Het aantal stappen is dus variabel.

Heeft de week:
- één opdracht -> één opdrachtstap;
- twee opdrachten -> twee opdrachtstappen;
- meer opdrachten -> overeenkomstig uitbreiden.

Heeft een opdracht geen Less/More-variant, introduceer dan
niet kunstmatig een keuze.


PORTFOLIO
---------
De laatste stap is het bijwerken van het bijbehorende
Portfolio.

Gebruik hetzelfde nummer als de PSET/week.
-->

1. Werk je lokale repository bij met Git voordat je begint.  
   Commit en push tijdens het werken regelmatig, zodat in je Git-history zichtbaar wordt hoe je werk zich ontwikkelt.  
   [Werken met Git](../../understanding/git/update.md)

2. Maak één van de volgende versies:
    - [Deze versie van [PSET 1]]([PSET-1]-less.md), als je je minder vertrouwd voelt met de stof.
    - [Deze versie van [PSET 1]]([PSET-1]-more.md), als je je meer vertrouwd voelt met de stof.

<!--
VOEG ALLEEN TOE WANNEER ER EEN VOLGENDE OPDRACHT IS:

3. Maak één van de volgende versies:
    - [Deze versie van [PSET 2]]([PSET-2]-less.md), als je je minder vertrouwd voelt met de stof.
    - [Deze versie van [PSET 2]]([PSET-2]-more.md), als je je meer vertrouwd voelt met de stof.

Herhaal indien nodig.

Pas daarna het nummer van de Portfolio-stap aan.
-->

[LAATSTE STAP]. Werk **Portfolio [NUMMER]** bij.  
   [Werken aan je portfolio](../../understanding/portfolio/index.md)


## Aanvullende uitleg en bronnen

<!--
============================================================
AANVULLENDE UITLEG EN BRONNEN
============================================================

FUNCTIE
-------
Biedt aanvullende bronnen voor:

- uitgebreidere bestudering;
- extra oefening;
- naslag tijdens het programmeren.

BELANGRIJK
----------
De uitleg in de PSET's zelf bevat de kennis die nodig is om
aan de opdrachten te kunnen werken.

Externe bronnen zijn dus AANVULLEND.

Gebruik ze niet om noodzakelijke module-inhoud naar externe
websites of boeken te verplaatsen.


CENTRAAL RESOURCEBEHEER
-----------------------
Resources worden centraal beheerd.

De PSET-index bevat daarom niet opnieuw handmatig:

- boektitels;
- hoofdstukken of paragrafen;
- oefeningen;
- externe URL's;
- resourcebeschrijvingen.

Gebruik op de PSET-index alleen de resourcegroep die voor deze
Problem Set is samengesteld.

Dezelfde ID staat in de frontmatter bij `resources` en wordt op
de pagina gebruikt met:

    {{ resource_group("[RESOURCE-GROEP]") }}

De renderer bepaalt vervolgens hoe de resources voor web en
PDF worden weergegeven.


GEBRUIK
-------
Gebruik:

    {{ resource_group("[RESOURCE-GROEP]") }}

Vervang [RESOURCE-GROEP] door de stabiele ID van de
resourcegroep voor deze Problem Set.
-->

{{ resource_group("[RESOURCE-GROEP]") }}


## Wanneer moet het af zijn?

<!--
============================================================
WANNEER MOET HET AF ZIJN?
============================================================

FUNCTIE
-------
De PSET-index is de centrale leerlingzichtbare plaats voor
de deadline van de volledige Problem Set.

SOURCE OF TRUTH
---------------
De datum komt UITSLUITEND uit:

docs/data/schedule.yml

Gebruik daarom:

{{ schedule.weeks[NUMMER].pset.deadline }}

Voer hier nooit handmatig een datum in.

Individuele PSET-pagina's bevatten geen eigen deadline.

Zo bestaat voor planning één source of truth.
-->

Lever Problem Set [NUMMER] uiterlijk **{{ schedule.weeks[NUMMER].pset.deadline }}** in.


## Hulp nodig?

<!--
============================================================
HULP NODIG? / VAKFLEX
============================================================

FUNCTIE
-------
Laat zien wanneer aanvullende uitleg en ondersteuning
beschikbaar is.

SOURCE OF TRUTH
---------------
De Vakflexmomenten komen uit schedule.yml.

Voer data en onderwerpen dus niet handmatig in deze pagina
in.

Gebruik het nummer van de betreffende week.
-->

Tijdens de Vakflexuren kun je extra uitleg en ondersteuning krijgen.

{% for moment in schedule.weeks[NUMMER].vakflex %}
**{{ moment.date }}**  
{{ moment.topic }}

{% endfor %}


<!--
============================================================
LAATSTE ONTWERPCONTROLE
============================================================

Voer deze controle uit vóór publicatie.


FRAMEWORK
---------
[ ] Komt de onderwijsinhoud uit het moduleframework?
[ ] Klopt de Python-focus?
[ ] Klopt de Visual First-representatie?
[ ] Klopt het CT-domein?
[ ] Klopt de CT-procesdimensie?
[ ] Is geen nieuwe onderwijsinhoud vanuit de template bedacht?


REFERENTIE-ONTWERP
------------------
[ ] Is de bestaande leerlingzichtbare structuur behouden?
[ ] Zijn geen nieuwe headings of secties geïntroduceerd?
[ ] Is vaste leerlingtekst niet zonder ontwerpbesluit herschreven?
[ ] Is de centrale resourcepresentatie behouden?


BADGES
------
[ ] Gelden alle badges voor de volledige Problem Set?
[ ] Staat er geen Less/More-badge op de index?


WERKWIJZE
---------
[ ] Begint de route met Git?
[ ] Staan alle opdrachten van deze PSET op de index?
[ ] Klopt de volgorde?
[ ] Heeft iedere ontworpen Less/More-keuze beide links?
[ ] Is geen Less/More-keuze bedacht waar die niet bestaat?
[ ] Wordt "minder/meer vertrouwd" consequent gebruikt?
[ ] Eindigt de route met Portfolio?
[ ] Klopt het Portfolio-nummer?


LINKS
-----
[ ] Kloppen alle PSET-bestandsnamen?
[ ] Kloppen Less/More-links?
[ ] Klopt de Git-link of is deze bewust nog toekomstig?
[ ] Klopt de Portfolio-link of is deze bewust nog toekomstig?


BRONNEN
-------
[ ] Is de juiste resourcegroep voor deze Problem Set gebruikt?
[ ] Staat deze resourcegroep ook in `resources:` in de frontmatter?
[ ] Wordt dezelfde ID gebruikt in `resource_group(...)`?
[ ] Zijn geen resourcegegevens handmatig in de index gedupliceerd?
[ ] Sluiten de centraal beheerde resources aan op de inhoud van deze week?
[ ] Zijn externe bronnen aanvullend en niet noodzakelijk om
    ontbrekende module-uitleg te compenseren?


PLANNING
--------
[ ] Komt de deadline uit schedule.yml?
[ ] Klopt schedule.weeks[NUMMER]?
[ ] Staat nergens op een individuele PSET een dubbele deadline?
[ ] Worden Vakflexmomenten uit schedule.yml geladen?


EINDCONTROLE
------------
[ ] Zijn alle placeholders vervangen?
[ ] Is de pagina snel scanbaar?
[ ] Is de index een routekaart gebleven?
[ ] Is geen theorie uit individuele PSET's onnodig gedupliceerd?
============================================================
-->