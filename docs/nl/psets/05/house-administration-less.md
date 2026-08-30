---
title: House Administration
template: pset.html
week: 5
level: less

understanding:
  - python.lists
  - python.list-indexes
  - python.adding-list-items
  - python.list-information
---

# House Administration

--8<-- "includes/badges.html:less-comfortable"
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

Op Hogwarts worden ieder jaar nieuwe leerlingen over verschillende huizen verdeeld.

Wanneer er steeds meer leerlingen bijkomen, moet Hogwarts kunnen bijhouden welke leerlingen bij welk huis horen. Nieuwe leerlingen moeten kunnen worden toegevoegd en opgeslagen gegevens moeten later weer kunnen worden teruggevonden.

**Hoe ontwerp je een programma dat meerdere gegevens overzichtelijk kan opslaan en terugvinden?**

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **House Administration** op te lossen.

Ontwerp en programmeer een administratie waarmee Hogwarts leerlingen per huis kan bewaren en informatie over de opgeslagen leerlingen kan opvragen.

Maak voordat je programmeert een **datastructuurdiagram** waarin zichtbaar is welke gegevens je bewaart en welke gegevens bij elkaar horen.

### Specificatie

Gebruik in je administratie de vier Hogwarts-huizen:

- Gryffindor
- Ravenclaw
- Hufflepuff
- Slytherin

Je programma moet:

- voor ieder huis meerdere leerlingnamen kunnen bewaren;
- beginnen met minimaal twee leerlingen per huis;
- een nieuwe leerling aan een gekozen huis kunnen toevoegen;
- na het toevoegen kunnen tonen hoeveel leerlingen in dat huis zijn opgeslagen;
- kunnen controleren of een opgegeven leerling in een gekozen huis voorkomt;
- een leerling op een opgegeven geldige index uit een gekozen huis kunnen tonen.

Nieuwe leerlingen moeten aan de bestaande gegevens worden toegevoegd. Eerder opgeslagen leerlingen mogen daarbij niet verdwijnen.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke gegevens moet je organiseren?"

    Begin nog niet met programmeren.

    Maak eerst je **datastructuurdiagram**.

    Laat daarin zien:

    - welke vier groepen gegevens er zijn;
    - welke gegevens bij iedere groep horen;
    - waar nieuwe gegevens later kunnen worden toegevoegd.

??? hint "2 — Hoe groeit een verzameling?"

    Kijk naar de list waaraan je een leerling wilt toevoegen.

    Welke list-bewerking voegt één nieuw item toe zonder de bestaande items te vervangen?

??? hint "3 — Welke vraag stel je aan de gegevens?"

    Niet iedere vraag over een list is hetzelfde.

    Bedenk welke Python-expressie past bij:

    - hoeveel items er zijn;
    - of een bepaalde naam voorkomt;
    - welk item op een bepaalde index staat.

??? hint "4 — Controleer je index"

    Python begint bij index `0`.

    Een list met drie items heeft dus de geldige indexes `0`, `1` en `2`.

### Testen

Een administratie werkt pas betrouwbaar wanneer **toevoegen, tellen, controleren en terugvinden** de juiste resultaten geven.

Voer minimaal de volgende tests uit.

| Test | Handeling | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | --------- | ------------------ | ------------------- |
| 1 | Vraag het aantal leerlingen van een huis vóórdat je iemand toevoegt | | |
| 2 | Voeg één nieuwe leerling aan dat huis toe en vraag opnieuw het aantal | | |
| 3 | Controleer of de zojuist toegevoegde leerling in dat huis voorkomt | | |
| 4 | Controleer een naam die niet in dat huis voorkomt | | |
| 5 | Vraag een leerling op via een geldige index | | |

Zorg dat je tests samen aantonen dat:

- een nieuwe leerling echt aan de bestaande gegevens wordt toegevoegd;
- `len()` daarna het juiste aantal geeft;
- een opgeslagen leerling als aanwezig wordt herkend;
- een niet-opgeslagen leerling als afwezig wordt herkend;
- een index het verwachte item oplevert.

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

**Kun je met je testgevallen aantonen dat leerlingen correct worden opgeslagen en later correct kunnen worden teruggevonden?**

Als de werkelijke uitvoer niet overeenkomt met je voorspelling, onderzoek dan waardoor het verschil ontstaat en pas je programma aan.

## Reflectie op de oplossing

Bekijk je **datastructuurdiagram** en je uiteindelijke **Python-programma**.

Waarom is de datastructuur die je hebt gekozen geschikt om de gegevens van dit probleem op te slaan en terug te vinden?

Gebruik in je antwoord een concreet voorbeeld uit je eigen datastructuurdiagram of programma.

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je datastructuurdiagram is toegevoegd;
- je programma met verschillende gegevens is getest;
- je reflectie is uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.
