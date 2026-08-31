---
title: Rock Paper Scissors Lizard Spock
template: pset.html
week: 3
level: more

resources:
  - video.rpsls

understanding:
  - python.and
  - python.or
---

# Rock Paper Scissors Lizard Spock

--8<-- "includes/badges.html:more-comfortable"
--8<-- "includes/badges.html:python-if"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"

--8<-- "includes/videos.html:rpsls"

## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** hoe stappen en beslissingen logisch met elkaar samenhangen.
- Ik kan **een algoritmische oplossing ontwerpen** voor een probleem met een groot aantal mogelijke combinaties.
- Ik kan **een oplossing automatiseren** door een complexer stelsel van spelregels vast te leggen als conditions en bijbehorende branches.
- Ik kan **een algoritmische oplossing programmeren** met `if`, `elif` en `else`.

## Probleem

Bij Rock Paper Scissors Lizard Spock maken twee spelers ieder één keuze:

- **Rock**
- **Paper**
- **Scissors**
- **Lizard**
- **Spock**

De spelregels bepalen welke keuze wint:

- Scissors verslaat Paper.
- Paper verslaat Rock.
- Rock verslaat Lizard.
- Lizard verslaat Spock.
- Spock verslaat Scissors.
- Scissors verslaat Lizard.
- Lizard verslaat Paper.
- Paper verslaat Spock.
- Spock verslaat Rock.
- Rock verslaat Scissors.

Wanneer beide spelers dezelfde keuze maken, is het gelijkspel.

Een computersysteem moet op basis van de twee gemaakte keuzes automatisch bepalen welke speler wint volgens de spelregels.

Een computer kan complexe beslissingen alleen correct nemen wanneer **alle regels en mogelijke uitkomsten expliciet zijn vastgelegd**.

**Hoe ontwerp je een beslissysteem dat op basis van spelregels automatisch de juiste uitkomst bepaalt?**

## Demo

<!--
PAS LATER INVULLEN.

Wordt gemaakt wanneer de solution gereed is.

Doel:
- leerling kan het gewenste gedrag ervaren;
- laat zien WAT het programma doet;
- laat niet zien HOE het programma is gebouwd.
-->

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Rock Paper Scissors Lizard Spock** op te lossen.

### Specificatie

Je programma moet:

- de keuze van speler 1 vragen;
- de keuze van speler 2 vragen;
- de twee keuzes met elkaar vergelijken;
- de vijf mogelijke keuzes Rock, Paper, Scissors, Lizard en Spock ondersteunen;
- gelijkspel herkennen wanneer beide spelers dezelfde keuze maken;
- op basis van de spelregels bepalen wanneer speler 1 wint;
- op basis van de spelregels bepalen wanneer speler 2 wint;
- de juiste uitkomst tonen.

Gebruik voor de beslisstructuur `if`, `elif` en `else`.

Je programma moet voor **iedere mogelijke combinatie van keuzes** steeds precies één juiste uitkomst geven:

- speler 1 wint;
- speler 2 wint;
- gelijkspel.

Gebruik voor beide spelers als invoer één van deze vijf keuzes:

- `Rock`;
- `Paper`;
- `Scissors`;
- `Lizard`;
- `Spock`.

Dit zijn in deze Problem Set de geldige keuzes.

Andere invoer hoef je in deze Problem Set niet af te handelen.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Hoeveel mogelijke combinaties zijn er?"

    Begin nog niet met programmeren.

    Twee spelers maken ieder één keuze uit Rock, Paper, Scissors, Lizard en Spock.

    Bedenk hoeveel verschillende combinaties van keuzes daarmee mogelijk zijn.

    Controleer vervolgens of je voor iedere combinatie kunt bepalen welke van deze uitkomsten hoort:

    - speler 1 wint;
    - speler 2 wint;
    - gelijkspel.

??? hint "2 — Welke regels bepalen de winnaar?"

    Kijk naar de tien spelregels en bepaal welke combinaties ervoor zorgen dat speler 1 wint.

    Denk daarna na over de omgekeerde combinaties: wat gebeurt er wanneer de keuzes van speler 1 en speler 2 worden omgedraaid?

    Controleer of je hiermee alle combinaties waarin één van de spelers wint kunt beschrijven.

??? hint "3 — Kun je meerdere conditions combineren?"

    Sommige verschillende combinaties leiden tot dezelfde uitkomst. Je hoeft deze niet altijd als afzonderlijke branches te programmeren.

    Kijk naar de **logical operators** uit de Understanding:

    - met `and` kun je conditions combineren die **tegelijk** moeten gelden;
    - met `or` kun je verschillende situaties combineren die tot **dezelfde uitkomst** leiden.

    Bedenk welke conditions samen één combinatie van twee keuzes beschrijven en welke van deze combinaties je vervolgens kunt samenbrengen omdat ze dezelfde winnaar hebben.

    Gebruik haakjes om duidelijk te maken welke conditions bij elkaar horen.

??? hint "4 — Hoe kun je de beslissingen zichtbaar maken?"

    Zet je beslissingen om in een **flowchart**.

    Begin bij de twee gemaakte keuzes en laat vervolgens zien welke conditions het programma moet controleren om tot één van deze uitkomsten te komen:

    - speler 1 wint;
    - speler 2 wint;
    - gelijkspel.

    Door de extra keuzes zijn er veel meer mogelijke routes dan bij Rock Paper Scissors. Controleer daarom systematisch of iedere mogelijke combinatie via één route bij de juiste uitkomst uitkomt.

??? hint "5 — Hoe zet je je flowchart om in pseudocode?"

    Beschrijf dezelfde oplossing nu als **pseudocode**.

    Gebruik je flowchart om de beslissingen en routes om te zetten in een geordende reeks stappen.

    Door het grote aantal mogelijke combinaties is het belangrijk dat je systematisch werkt. Situaties die tot dezelfde uitkomst leiden, kun je ook in je pseudocode bij elkaar brengen.

    Controleer daarna of je pseudocode alle mogelijke combinaties uit je flowchart beschrijft.

??? hint "6 — Hoe vertaal je je pseudocode naar Python?"

    Gebruik je pseudocode als ontwerp voor je programma.

    Met `if`, `elif` en `else` kun je de verschillende combinaties en uitkomsten in Python vastleggen. Gebruik `and` wanneer meerdere conditions tegelijk moeten gelden en `or` wanneer verschillende situaties tot dezelfde uitkomst leiden.

    Kijk naar je eigen pseudocode:

    - welke condition controleer je als eerste?
    - welke combinaties leiden tot dezelfde uitkomst?
    - welke volgende mogelijkheden moeten daarna worden gecontroleerd?
    - welke branches horen bij de verschillende uitkomsten?

    Programmeer vanuit je ontwerp verder.

### Testen

Een programma is pas betrouwbaar als je controleert of **iedere mogelijke combinatie van keuzes correct wordt afgehandeld**.

Met vijf keuzes per speler zijn er **25 mogelijke combinaties**.

Maak zelf een systematische verzameling testgevallen waarin iedere combinatie precies één keer voorkomt.

| Test | Speler 1 | Speler 2 | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | -------- | -------- | ------------------ | ------------------- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| ... | | | | |
| 25 | | | | |

Bepaal **vooraf** bij iedere combinatie welke uitkomst je volgens de spelregels verwacht.

Voer daarna alle 25 tests uit.

Controleer met je testgevallen:

- of iedere mogelijke combinatie van de vijf keuzes voorkomt;
- of alle gelijkspelen correct worden herkend;
- of de combinaties waarin speler 1 wint correct worden afgehandeld;
- of de omgekeerde combinaties waarin speler 2 wint correct worden afgehandeld;
- of iedere combinatie **precies één** uitkomst oplevert.

Vergelijk bij iedere test de werkelijke uitkomst met de verwachte uitkomst.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan welke condition of branch in je algoritme niet doet wat je had verwacht en pas je programma waar nodig aan.

**Kun je met je 25 testgevallen aantonen dat iedere mogelijke combinatie correct wordt afgehandeld en steeds precies één uitkomst oplevert?**

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt alle **25 mogelijke combinaties** getest;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit de spelregels tot je **beslisstructuur** bent gekomen;
- je kunt uitleggen hoe je vanuit je flowchart via pseudocode tot `if`, `elif` en `else` bent gekomen;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 3** bij.

