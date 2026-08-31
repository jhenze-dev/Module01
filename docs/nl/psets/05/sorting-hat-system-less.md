---
title: Sorting Hat System
template: pset.html
week: 5
level: less

understanding:
  - python.lists-and-conditions
---

# Sorting Hat System

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-lists"
--8<-- "includes/badges.html:visual-datastructuurdiagram"
--8<-- "includes/badges.html:ct-abstractie"
--8<-- "includes/badges.html:process-formulating"
--8<-- "includes/badges.html:process-expressing"
--8<-- "includes/badges.html:process-reflecting-solution"

## Waar werk je aan?

In deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **analyseren welke informatie relevant is** voor een probleem.
- Ik kan **relevante informatie representeren in een abstract model**.
- Ik kan **een proces of systeem construeren op basis van een model**.
- Ik kan **uitleggen waarom een gekozen datastructuur geschikt is voor een probleem**.

## Probleem

De Sorting Hat heeft leerlingen over de vier huizen van Hogwarts verdeeld.

Een computersysteem moet deze leerlingen kunnen opslaan en later kunnen bepalen in welk huis een leerling is ingedeeld.

Het systeem moet daarvoor de opgeslagen gegevens kunnen gebruiken om een beslissing te nemen.

**Hoe ontwerp je een systeem dat opgeslagen gegevens kan doorzoeken en gebruiken om een beslissing te nemen?**

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je de opgeslagen gegevens gebruiken om het probleem van het **Sorting Hat System** op te lossen.

Ontwerp en programmeer een systeem dat de naam van een leerling ontvangt en op basis van opgeslagen gegevens bepaalt in welk Hogwarts-huis deze leerling zit.

Maak voordat je programmeert een **datastructuurdiagram** waarin zichtbaar is welke gegevens het systeem nodig heeft om deze beslissing te nemen.

Werk daarna de stappen van je systeem uit in **pseudocode** als genummerde comments in je `.py`-bestand. Bouw vervolgens de Python-code bij deze stappen.

### Specificatie

Je systeem gebruikt vier lists met minimaal twee opgeslagen leerlingen per huis:

- Gryffindor
- Ravenclaw
- Hufflepuff
- Slytherin

Je programma moet:

- de gebruiker om de naam van een leerling vragen;
- controleren of deze leerling in Gryffindor voorkomt;
- controleren of deze leerling in Ravenclaw voorkomt;
- controleren of deze leerling in Hufflepuff voorkomt;
- controleren of deze leerling in Slytherin voorkomt;
- precies het juiste huis tonen wanneer de leerling wordt gevonden;
- `Leerling niet gevonden` tonen wanneer de naam in geen van de vier huizen voorkomt.

Per zoekopdracht moet het programma precies één uitkomst geven.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke informatie bepaalt de uitkomst?"

    Kijk naar je datastructuurdiagram.

    Het programma kent een naam en beschikt over vier verzamelingen met gegevens.

    Welke vraag kan het systeem aan iedere verzameling stellen?

??? hint "2 — Hoe wordt een zoekvraag een beslissing?"

    Een expression met `in` wordt `True` of `False`.

    Zo'n Boolean expression kan worden gebruikt als condition.

??? hint "3 — Wanneer gebruik je de laatste branch?"

    Denk aan een leerling die in geen enkele opgeslagen list voorkomt.

    Welke uitkomst hoort alleen bij die situatie?

??? hint "4 — Hoe voorkom je meerdere antwoorden?"

    Voor één ingevoerde leerling hoort het systeem precies één resultaat te geven.

    Kijk naar de samenhang tussen je conditions en branches.

### Testen

Het Sorting Hat System is pas betrouwbaar wanneer **iedere mogelijke soort zoekuitkomst** correct wordt afgehandeld.

Gebruik voor je tests namen waarvan je vooraf weet in welke list ze staan.

| Test | Invoer | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | ------ | ------------------ | ------------------- |
| 1 | leerling uit Gryffindor | Gryffindor | |
| 2 | leerling uit Ravenclaw | Ravenclaw | |
| 3 | leerling uit Hufflepuff | Hufflepuff | |
| 4 | leerling uit Slytherin | Slytherin | |
| 5 | onbekende naam | Leerling niet gevonden | |

Bepaal **vooraf** welke concrete naam je voor iedere test gebruikt.

Voer daarna iedere test afzonderlijk uit en controleer:

- of het juiste huis wordt getoond;
- of er precies één uitkomst verschijnt;
- of een onbekende leerling niet ten onrechte aan een huis wordt gekoppeld.

**Kun je met deze vijf testgevallen aantonen dat iedere mogelijke uitkomst van het systeem correct werkt?**

Als de werkelijke uitvoer niet overeenkomt met je voorspelling, onderzoek dan waardoor het verschil ontstaat en pas je programma aan.

## Reflectie op de oplossing

Bekijk je **datastructuurdiagram** en je uiteindelijke **Python-programma**.

Waarom is de gekozen datastructuur geschikt om een ingevoerde leerling terug te vinden en te bepalen bij welk huis deze leerling hoort?

Onderbouw je antwoord met een concreet voorbeeld uit je eigen datastructuurdiagram en programma.

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je datastructuurdiagram is toegevoegd;
- je pseudocode staat als genummerde comments in je `.py`-bestand;
- je systeem met verschillende leerlingen en een onbekende naam is getest;
- je reflectie is uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.