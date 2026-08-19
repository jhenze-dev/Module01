---
title: Rock Paper Scissors — minder vertrouwd
template: pset.html
---

# Rock Paper Scissors

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-if"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"

## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** hoe stappen en beslissingen logisch met elkaar samenhangen.
- Ik kan **een algoritmische oplossing ontwerpen** voor een probleem met meerdere mogelijke combinaties.
- Ik kan **een oplossing automatiseren** door spelregels vast te leggen als conditions en bijbehorende branches.
- Ik kan **een algoritmische oplossing programmeren** met `if`, `elif` en `else`.

## Probleem

Bij Rock Paper Scissors maken twee spelers ieder één keuze:

- **Rock**
- **Paper**
- **Scissors**

De spelregels bepalen welke keuze wint:

- Rock verslaat Scissors.
- Scissors verslaat Paper.
- Paper verslaat Rock.

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

--8<-- "understanding/_content/python/and.md"

--8<-- "understanding/_content/python/or.md"

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Rock Paper Scissors** op te lossen.

### Specificatie

Je programma moet:

- de keuze van speler 1 vragen;
- de keuze van speler 2 vragen;
- de twee keuzes met elkaar vergelijken;
- gelijkspel herkennen wanneer beide spelers dezelfde keuze maken;
- bepalen wanneer speler 1 wint;
- bepalen wanneer speler 2 wint;
- de juiste uitkomst tonen.

Gebruik voor de beslisstructuur `if`, `elif` en `else`.

Je programma moet voor **iedere mogelijke combinatie van keuzes** steeds precies één juiste uitkomst geven:

- speler 1 wint;
- speler 2 wint;
- gelijkspel.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke mogelijke uitkomsten zijn er?"

    Begin nog niet met programmeren.

    Twee spelers maken ieder één keuze uit Rock, Paper en Scissors.

    Bedenk welke verschillende combinaties van keuzes mogelijk zijn en welke uitkomst bij iedere combinatie hoort.

    Controleer of je daarbij ook de situaties hebt meegenomen waarin beide spelers dezelfde keuze maken.

??? hint "2 — Welke regels bepalen de winnaar?"

    Kijk naar de drie spelregels:

    - Rock verslaat Scissors.
    - Scissors verslaat Paper.
    - Paper verslaat Rock.

    Bedenk voor iedere spelregel welke combinatie van keuzes daarbij hoort.

    Denk daarna na over de omgekeerde combinatie: wie wint wanneer de keuzes van speler 1 en speler 2 worden omgedraaid?

??? hint "3 — Hoe kun je de beslissingen zichtbaar maken?"

    Zet je beslissingen om in een **flowchart**.

    Begin bij de twee gemaakte keuzes en laat vervolgens zien welke conditions het programma moet controleren om tot één van deze uitkomsten te komen:

    - speler 1 wint;
    - speler 2 wint;
    - gelijkspel.

    Controleer je flowchart: kan iedere mogelijke combinatie van keuzes via één route bij de juiste uitkomst uitkomen?

??? hint "4 — Hoe vertaal je je flowchart naar Python?"

    Gebruik je flowchart als ontwerp voor je programma.

    Met `if`, `elif` en `else` kun je verschillende combinations en uitkomsten in Python vastleggen.

    Kijk naar je eigen flowchart:

    - welke condition controleer je als eerste?
    - welke volgende mogelijkheden moeten daarna worden gecontroleerd?
    - welke branches horen bij de verschillende uitkomsten?

    Programmeer vanuit je ontwerp verder.

### Testen

Een programma is pas betrouwbaar als je controleert of **iedere mogelijke combinatie van keuzes** correct wordt afgehandeld.

Bedenk voor iedere test:

- welke keuze **speler 1** maakt;
- welke keuze **speler 2** maakt;
- welke **uitkomst je verwacht**;
- welke **uitkomst je programma werkelijk geeft**.

Gebruik bijvoorbeeld een tabel als deze:

| Test | Speler 1 | Speler 2 | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | -------- | -------- | ------------------ | ------------------- |
| 1    |          |          |                    |                     |
| 2    |          |          |                    |                     |
| 3    |          |          |                    |                     |
| ...  |          |          |                    |                     |
| 9    |          |          |                    |                     |

Zorg dat je testgevallen samen alle verschillende soorten uitkomsten controleren:

- speler 1 wint;
- speler 2 wint;
- gelijkspel.

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan welke condition of branch in je algoritme niet doet wat je had verwacht.

**Kun je met je testgevallen aantonen dat je programma iedere mogelijke combinatie correct afhandelt?**

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt de verschillende mogelijke combinaties getest;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit de spelregels tot je **beslisstructuur** bent gekomen;
- je kunt uitleggen hoe je flowchart is vertaald naar `if`, `elif` en `else`;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 3** bij.

