---
title: How Fast Is Forrest? — minder vertrouwd
template: pset.html
---

# How Fast Is Forrest?

--8<-- "includes/badges.html:less-comfortable"
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

--8<-- "understanding/_content/python/variables.md"

--8<-- "understanding/_content/python/arithmetic-expressions.md"

[Meer over IPO-diagrammen](../../understanding/visual-first/ipo.md)


## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **How Fast Is Forrest?** op te lossen.

Ontwerp en programmeer een systeem dat informatie over een loopprestatie verwerkt en daaruit een overzichtelijk prestatierapport maakt.


### Specificatie

Je programma vraagt de gebruiker om:

- de **afstand in meters**;
- de **tijd in seconden**.

Met deze gegevens berekent het programma informatie over de loopprestatie.

Het resultaat bevat in ieder geval:

- de gemiddelde snelheid in **meter per seconde**;
- de gemiddelde snelheid in **kilometer per uur**.

Presenteer de ingevoerde gegevens en de berekende resultaten in een duidelijk en overzichtelijk prestatierapport.

Gebruik bij het ontwerpen van je oplossing een **IPO-diagram**.

Gebruik in je programma **variabelen**, `int` en `float`.


### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.


??? hint "1 — Welke informatie gaat erin en komt eruit?"

    Je programma krijgt twee gegevens:

    - een afstand in meters;
    - een tijd in seconden.

    Welke informatie moet het programma uiteindelijk uit deze gegevens kunnen afleiden?

    Maak onderscheid tussen informatie die het programma **krijgt** en informatie die het programma zelf moet **berekenen**.


??? hint "2 — Maak de informatiestroom zichtbaar"

    Gebruik een **IPO-diagram** om je oplossing te structureren.

    Denk na over:

    - welke gegevens het systeem binnenkomen;
    - wat met deze gegevens moet gebeuren;
    - welke informatie het systeem uiteindelijk moet opleveren.

    [Meer over IPO-diagrammen](../../understanding/visual-first/ipo.md)


??? hint "3 — Deel de verwerking op"

    Bekijk de resultaten die je programma moet opleveren afzonderlijk.

    Welke ingevoerde gegevens heb je voor ieder resultaat nodig?

    Welke berekening moet met die gegevens worden uitgevoerd?

    Vul hiermee het onderdeel **Verwerking** van je IPO-diagram verder aan.


??? hint "4 — Van je model naar Python"

    Kijk naar je IPO-diagram.

    Welke waarden moeten tijdens het uitvoeren van het programma worden bewaard?

    Geef deze waarden betekenisvolle **variabelenamen**.

    Bedenk ook welke waarden als `int` en welke als `float` moeten worden gebruikt zodat Python ermee kan rekenen.


### Testen

Een programma is pas betrouwbaar als het bij verschillende afstanden en tijden de juiste resultaten berekent en presenteert.

Test je programma daarom met verschillende loopprestaties.

Bedenk voor iedere test **vooraf**:

- welke afstand en tijd je invoert;
- welke snelheid in meter per seconde je verwacht;
- welke snelheid in kilometer per uur je verwacht.

| Test | Afstand (m) | Tijd (s) | Verwachte m/s | Verwachte km/h | Werkelijke m/s | Werkelijke km/h |
| ---- | ----------- | -------- | -------------- | --------------- | --------------- | ---------------- |
| 1    |             |          |                |                 |                 |                  |
| 2    |             |          |                |                 |                 |                  |
| 3    |             |          |                |                 |                 |                  |

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan waar je informatiemodel, berekening of programma iets anders doet dan je had verwacht.

**Levert je programma bij verschillende afstanden en tijden steeds de verwachte snelheden op?**


### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma vraagt om een **afstand in meters** en een **tijd in seconden**;
- je programma berekent de gemiddelde snelheid in **meter per seconde** en **kilometer per uur**;
- je programma presenteert de ingevoerde gegevens en berekende resultaten overzichtelijk;
- je hebt je oplossing uitgewerkt in een **IPO-diagram**;
- je hebt verschillende afstanden en tijden met **testgevallen** gecontroleerd;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit de twee ingevoerde gegevens tot de berekende informatie bent gekomen;
- je kunt uitleggen hoe je IPO-diagram is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 2** bij.
