---
title: Sorting Hat System
template: pset.html
week: 5
level: more

understanding:
  - python.lists-and-conditions
---

# Sorting Hat System

--8<-- "includes/badges.html:more-comfortable"
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

De Sorting Hat verdeelt nieuwe Hogwarts-leerlingen over Gryffindor, Ravenclaw, Hufflepuff en Slytherin.

Een computersysteem moet meerdere leerlingen kunnen opslaan en de opgeslagen gegevens vervolgens kunnen gebruiken om te bepalen in welk huis een leerling is ingedeeld.

Terwijl het systeem wordt gebruikt, komen er bovendien nieuwe leerlingen bij. De opgeslagen informatie verandert dus tijdens het gebruik.

**Hoe ontwerp je een systeem dat opgeslagen gegevens kan doorzoeken en gebruiken om een beslissing te nemen?**

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je de opgeslagen gegevens gebruiken in een interactief **Sorting Hat System**.

Ontwerp en programmeer een systeem waarin de gebruiker nieuwe leerlingen kan registreren en opgeslagen leerlingen kan opzoeken.

Nieuwe gegevens moeten tijdens het gebruik bewaard blijven, zodat een nieuw geregistreerde leerling later in dezelfde uitvoering weer kan worden teruggevonden.

Het programma blijft actief totdat de gebruiker ervoor kiest om te stoppen.

Maak voordat je programmeert een **datastructuurdiagram** waarin zichtbaar is welke gegevens worden opgeslagen en gebruikt.

### Specificatie

Je systeem gebruikt de vier Hogwarts-huizen:

- Gryffindor
- Ravenclaw
- Hufflepuff
- Slytherin

Het programma moet steeds één van deze keuzes aanbieden:

1. leerling registreren;
2. leerling opzoeken;
3. stoppen.

Bij **leerling registreren** moet het programma:

- om de naam van de leerling vragen;
- om één van de vier geldige huizen vragen;
- de leerling aan het gekozen huis toevoegen;
- bevestigen bij welk huis de leerling is opgeslagen.

Bij **leerling opzoeken** moet het programma:

- om de naam van de leerling vragen;
- de opgeslagen gegevens doorzoeken;
- het juiste huis tonen wanneer de leerling wordt gevonden;
- `Leerling niet gevonden` tonen wanneer de leerling in geen van de vier huizen voorkomt.

Daarnaast moet het programma:

- na registreren of opzoeken opnieuw het menu tonen;
- nieuw geregistreerde leerlingen tijdens dezelfde uitvoering blijven onthouden;
- een ongeldige menukeuze afwijzen en opnieuw een keuze vragen;
- alleen stoppen wanneer de gebruiker optie `3` kiest.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke gegevens veranderen tijdens het gebruik?"

    Nieuwe leerlingen worden tijdens het programma toegevoegd.

    Bedenk welke gegevens daarom vóór de volgende menuactie beschikbaar moeten blijven.

??? hint "2 — Welke drie processen bevat het systeem?"

    Bekijk iedere menukeuze afzonderlijk.

    Beschrijf eerst zonder Python:

    - wat registreren moet doen;
    - wat opzoeken moet doen;
    - wat stoppen moet doen.

??? hint "3 — Hoe wordt opgeslagen informatie gebruikt?"

    Bij het opzoeken moet het programma beslissen welk huis bij een naam hoort.

    Bedenk welke Boolean expressions je daarvoor met de bestaande lists kunt maken.

??? hint "4 — Waarom moet het programma terug naar het menu?"

    Na registreren of opzoeken is het systeem nog niet klaar.

    Welke condition bepaalt of het volledige proces doorgaat?

??? hint "5 — Wat gebeurt er bij ongeldige invoer?"

    Test niet alleen de drie geldige menuopties.

    Bedenk wat het programma moet doen wanneer de gebruiker bijvoorbeeld `7` invoert.

### Testen

Test het systeem niet alleen met losse handelingen, maar ook met een **volledige reeks handelingen binnen dezelfde uitvoering**.

Voer minimaal het volgende testscenario uit:

| Stap | Handeling | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | --------- | ------------------ | ------------------- |
| 1 | Zoek een bestaande leerling op | juiste huis wordt getoond | |
| 2 | Zoek een onbekende leerling op | `Leerling niet gevonden` | |
| 3 | Registreer een nieuwe leerling | juiste huis wordt bevestigd | |
| 4 | Zoek dezelfde nieuwe leerling op | dezelfde leerling wordt in het juiste huis gevonden | |
| 5 | Voer een ongeldige menukeuze in | keuze wordt afgewezen en menu verschijnt opnieuw | |
| 6 | Registreer nog een leerling in een ander huis | juiste huis wordt bevestigd | |
| 7 | Zoek de eerste nieuw geregistreerde leerling opnieuw op | deze leerling is nog steeds opgeslagen | |
| 8 | Kies stoppen | programma stopt | |

Bepaal **vooraf** welke namen en huizen je bij het scenario gebruikt.

Controleer tijdens het testen niet alleen de afzonderlijke uitkomsten, maar ook of gegevens tussen de verschillende handelingen bewaard blijven.

Een belangrijke test is daarom:

> registreer leerling → voer andere handelingen uit → zoek die leerling opnieuw op

De leerling moet dan nog steeds worden gevonden.

**Kun je met dit testscenario aantonen dat je systeem correct beslist, nieuwe gegevens bewaart en alleen stopt wanneer de gebruiker daarvoor kiest?**

Als de werkelijke resultaten niet overeenkomen met je voorspellingen, onderzoek dan waardoor het verschil ontstaat en pas je programma aan.

## Reflectie op de oplossing

Bekijk je **datastructuurdiagram** en je uiteindelijke **Python-programma**.

Waarom is de gekozen datastructuur geschikt voor een systeem waarin gegevens tijdens het gebruik worden toegevoegd én later worden gebruikt om beslissingen te nemen?

Onderbouw je antwoord met concrete voorbeelden uit je eigen datastructuurdiagram en programma.

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je datastructuurdiagram is toegevoegd;
- registreren, opzoeken en stoppen zijn getest;
- nieuw toegevoegde leerlingen daarna correct kunnen worden teruggevonden;
- je reflectie is uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.