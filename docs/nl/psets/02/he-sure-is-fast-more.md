---
title: How Fast Is Forrest?
template: pset.html
week: 2
level: more

understanding:
  - python.variables
  - python.arithmetic-expressions
---

# How Fast Is Forrest?

--8<-- "includes/badges.html:more-comfortable"
--8<-- "includes/badges.html:python-variables"
--8<-- "includes/badges.html:visual-ipo"
--8<-- "includes/badges.html:ct-data"
--8<-- "includes/badges.html:process-formulating"
--8<-- "includes/badges.html:process-expressing"


## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan de benodigde **gegevens verzamelen** voor een analyse.
- Ik kan gegevens **ordenen in een bruikbare structuur**.
- Ik kan de **betekenis van geordende gegevens interpreteren**.
- Ik kan informatie **presenteren in de gekozen representatievorm**.


## Probleem

In *Forrest Gump* zien we dat Forrest snel rent.

Maar hoe snel rent hij eigenlijk?

Een computersysteem moet een loopprestatie verwerken en op basis van ingevoerde gegevens automatisch betekenisvolle resultaten berekenen en presenteren.

Een computer kan alleen berekeningen uitvoeren wanneer informatie uit de werkelijkheid eerst wordt gemodelleerd als gegevens waarmee gerekend kan worden.

**Hoe ontwerp je een systeem dat een loopprestatie omzet naar gegevens waarmee een computer snelheid en andere prestaties automatisch kan berekenen en presenteren?**


## Demo

[DEMO LATER TOEVOEGEN]


## Understanding

{{ understanding_reference(understanding) }}

[Meer over IPO-diagrammen](../../understanding/visual-first/ipo.md)


## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **How Fast Is Forrest?** op te lossen.

Ontwerp en programmeer een systeem dat verschillende gegevens over een loopprestatie combineert en daaruit een overzichtelijk prestatierapport maakt.


### Specificatie

Een looptest bestaat uit een aantal ronden van dezelfde lengte.

Je programma vraagt de gebruiker om:

- de **lengte van één ronde in meters**;
- het **aantal gelopen ronden**;
- de **totale looptijd in seconden**.

Met deze gegevens berekent het programma informatie over de loopprestatie.

Het resultaat bevat in ieder geval:

- de **totale afstand in meters**;
- de **totale afstand in kilometers**;
- de gemiddelde snelheid in **meter per seconde**;
- de gemiddelde snelheid in **kilometer per uur**;
- de gemiddelde tijd per kilometer.

Presenteer de ingevoerde gegevens en de berekende resultaten in een duidelijk en overzichtelijk prestatierapport.

Gebruik bij het ontwerpen van je oplossing een **IPO-diagram**.

Gebruik in je programma **variabelen**, `int` en `float`.

Gebruik als invoer:

- een **positieve rondelengte**;
- een **positief geheel aantal ronden**;
- een **positieve totale looptijd**.

Waarden groter dan `0` zijn in deze Problem Set geldig.

Andere invoer hoef je in deze Problem Set niet af te handelen.


### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.


??? hint "1 — Welke informatie kun je afleiden?"

    Kijk naar de drie gegevens die het programma krijgt:

    - de lengte van één ronde;
    - het aantal gelopen ronden;
    - de totale looptijd.

    Niet alle informatie uit het prestatierapport wordt dus rechtstreeks ingevoerd.

    Bedenk welke informatie eerst uit deze gegevens moet worden **berekend** en welke berekende informatie daarna weer gebruikt kan worden voor andere resultaten.


??? hint "2 — Breng de informatiestroom in kaart"

    Werk je oplossing uit als een **IPO-diagram**.

    Laat daarin zien:

    - welke gegevens als **Input** binnenkomen;
    - welke berekeningen en omzettingen bij **Verwerking** plaatsvinden;
    - welke informatie uiteindelijk als **Output** wordt gepresenteerd.

    Controleer vooral of sommige berekende waarden later opnieuw nodig zijn.

    [Meer over IPO-diagrammen](../../understanding/visual-first/ipo.md)


??? hint "3 — Van model naar Python"

    Gebruik je IPO-diagram als ontwerp voor je programma.

    Bepaal welke ingevoerde en berekende waarden tijdens het programma bewaard moeten blijven en geef deze betekenisvolle **variabelenamen**.

    Kijk daarna naar de relaties tussen de gegevens in je eigen model en vertaal deze naar berekeningen met Python.


### Testen

Een programma is pas betrouwbaar als het voor verschillende loopprestaties steeds de juiste berekeningen en een overzichtelijke presentatie van de resultaten oplevert.

Ontwerp zelf minimaal drie testgevallen.

Kies je testgegevens zo dat je verschillende:

- rondelengtes;
- aantallen ronden;
- totale looptijden

gebruikt.

| Test | Ronde (m) | Ronden | Tijd (s) | Verwachte resultaten | Werkelijke resultaten |
| ---- | --------- | ------ | -------- | --------------------- | --------------------- |
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

Leg bij iedere test **vooraf** bij de verwachte resultaten vast:

- de totale afstand in meter;
- de totale afstand in kilometer;
- de gemiddelde snelheid in meter per seconde;
- de gemiddelde snelheid in kilometer per uur;
- de gemiddelde tijd per kilometer.

Voer daarna iedere test uit en leg dezelfde vijf werkelijke resultaten vast.

Controleer bij iedere test:

- of de ingevoerde rondelengte correct in het prestatierapport staat;
- of het ingevoerde aantal ronden correct in het prestatierapport staat;
- of de ingevoerde totale looptijd correct in het prestatierapport staat;
- of de totale afstand in meter en kilometer klopt;
- of de gemiddelde snelheid in meter per seconde en kilometer per uur klopt;
- of de gemiddelde tijd per kilometer klopt;
- of de juiste eenheden bij de gegevens en resultaten staan.

Vergelijk daarna de werkelijke resultaten met de verwachte resultaten.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan welke invoer, berekening of omzetting in je informatiemodel iets anders doet dan je had verwacht en pas je programma waar nodig aan.

**Kun je met je drie testgevallen aantonen dat je programma verschillende loopprestaties correct verwerkt en alle ingevoerde en berekende gegevens in het prestatierapport toont?**


### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma verwerkt de **rondelengte**, het **aantal ronden** en de **totale looptijd**;
- je programma berekent de totale afstand in **meter** en **kilometer**;
- je programma berekent de gemiddelde snelheid in **meter per seconde** en **kilometer per uur**;
- je programma berekent de gemiddelde tijd per kilometer;
- je programma presenteert de ingevoerde gegevens en berekende resultaten overzichtelijk;
- je hebt je oplossing uitgewerkt in een **IPO-diagram**;
- je hebt verschillende combinaties van invoergegevens systematisch getest;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen welke informatie rechtstreeks werd ingevoerd en welke informatie door het programma werd berekend;
- je kunt uitleggen hoe berekende informatie opnieuw is gebruikt voor andere resultaten;
- je kunt uitleggen hoe je IPO-diagram is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 2** bij.
