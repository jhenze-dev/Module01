---
title: House Administration
template: pset.html
week: 5
level: more

understanding:
  - python.lists
  - python.list-indexes
  - python.adding-list-items
  - python.list-information
---

# House Administration

--8<-- "includes/badges.html:more-comfortable"
--8<-- "includes/badges.html:python-lists"
--8<-- "includes/badges.html:visual-datastructuurdiagram"
--8<-- "includes/badges.html:ct-data"
--8<-- "includes/badges.html:process-formulating"
--8<-- "includes/badges.html:process-expressing"
--8<-- "includes/badges.html:process-reflecting-solution"

## Waar werk je aan?

In deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **gegevens ordenen in een bruikbare structuur**.
- Ik kan **informatie presenteren in een datastructuurdiagram**.
- Ik kan **uitleggen waarom een gekozen datastructuur geschikt is voor een probleem**.

## Probleem

Op Hogwarts worden ieder jaar nieuwe leerlingen verdeeld over Gryffindor, Ravenclaw, Hufflepuff en Slytherin.

Naarmate er meer leerlingen worden ingeschreven, groeit ook de hoeveelheid informatie die Hogwarts moet beheren. De administratie moet overzichtelijk blijven en gegevens moeten later weer kunnen worden teruggevonden.

**Hoe ontwerp je een programma dat meerdere gegevens overzichtelijk kan opslaan en terugvinden?**

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **House Administration** op te lossen.

Ontwerp en programmeer een administratie voor alle vier de Hogwarts-huizen waarmee leerlingen kunnen worden opgeslagen en verschillende gegevens uit de administratie kunnen worden opgevraagd.

Maak voordat je programmeert een **datastructuurdiagram** van de volledige administratie.

Werk daarna de stappen van je programma uit in **pseudocode** als genummerde comments in je `.py`-bestand. Bouw vervolgens de Python-code bij deze stappen.

### Specificatie

Gebruik in je administratie de vier Hogwarts-huizen:

- Gryffindor
- Ravenclaw
- Hufflepuff
- Slytherin

Je programma moet:

- voor ieder huis meerdere leerlingnamen kunnen bewaren;
- beginnen met minimaal twee leerlingen per huis;
- nieuwe leerlingen aan ieder van de vier huizen kunnen toevoegen;
- na iedere toevoeging het nieuwe aantal leerlingen van dat huis kunnen tonen;
- voor ieder huis kunnen controleren of een opgegeven leerling daar voorkomt;
- leerlingen op verschillende geldige indexes kunnen terugvinden;
- meerdere leerlingen achter elkaar kunnen toevoegen zonder eerder opgeslagen gegevens te verliezen;
- kunnen bepalen welk van twee gekozen huizen op dat moment de meeste leerlingen bevat.

Wanneer beide gekozen huizen evenveel leerlingen bevatten, moet je programma dat ook kunnen aangeven.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Modelleer eerst de volledige administratie"

    Begin bij je **datastructuurdiagram**.

    Laat zien:

    - welke gegevens bij elkaar horen;
    - welke groepen van elkaar gescheiden moeten blijven;
    - welke delen van de structuur tijdens het gebruik kunnen groeien.

??? hint "2 — Wat moet na een toevoeging hetzelfde blijven?"

    Wanneer je één list verandert, mogen de gegevens in de andere lists niet verdwijnen of veranderen.

    Controleer na een toevoeging daarom niet alleen het gewijzigde huis.

??? hint "3 — Hoe vergelijk je twee huizen?"

    Je hoeft daarvoor niet alle leerlingen één voor één te bekijken.

    Welke informatie over een list kun je rechtstreeks opvragen?

??? hint "4 — Welke verschillende uitkomsten zijn mogelijk?"

    Bij het vergelijken van twee aantallen zijn meer situaties mogelijk dan alleen:

    - het eerste aantal is groter;
    - het tweede aantal is groter.

    Denk ook aan de situatie waarin beide aantallen gelijk zijn.

### Testen

Test de volledige administratie met meerdere wijzigingen en opvragingen.

Maak minimaal zes testgevallen.

| Test | Handeling | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | --------- | ------------------ | ------------------- |
| 1 | Voeg een leerling toe aan Gryffindor | | |
| 2 | Voeg daarna een leerling toe aan een ander huis | | |
| 3 | Controleer of beide nieuwe leerlingen in het juiste huis voorkomen | | |
| 4 | Vraag een bestaande leerling op via een geldige index | | |
| 5 | Vergelijk twee huizen met verschillende aantallen leerlingen | | |
| 6 | Vergelijk twee huizen met evenveel leerlingen | | |

Controleer daarnaast na meerdere toevoegingen of leerlingen die **al vóór de toevoegingen** waren opgeslagen nog steeds aanwezig zijn.

Bepaal voor iedere test vooraf:

- welke gegevens vóór de handeling zijn opgeslagen;
- welke verandering je uitvoert;
- welke uitkomst je verwacht;
- welke uitkomst het programma werkelijk geeft.

**Kun je met je testgevallen aantonen dat de administratie ook na meerdere wijzigingen correcte gegevens bewaart en correcte informatie teruggeeft?**

Als de werkelijke resultaten niet overeenkomen met je voorspellingen, onderzoek dan waardoor het verschil ontstaat en pas je programma aan.

## Reflectie op de oplossing

Bekijk je **datastructuurdiagram** en je uiteindelijke **Python-programma**.

Waarom is de datastructuur die je hebt gekozen geschikt om de gegevens van de vier Hogwarts-huizen op te slaan en terug te vinden?

Onderbouw je antwoord met concrete voorbeelden uit je eigen datastructuurdiagram en programma.

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je datastructuurdiagram is toegevoegd;
- je pseudocode staat als genummerde comments in je `.py`-bestand;
- je administratie met verschillende leerlingen en huizen is getest;
- je reflectie is uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.
