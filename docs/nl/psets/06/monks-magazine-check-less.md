---
title: Monk's Magazine Check
template: pset.html
week: 6
level: less

understanding:
  - python.for-loops
  - python.iterating-lists
  - python.range
  - python.list-indexes
  - algorithms-efficiency.describing-with-n-basics
---

# Monk's Magazine Check

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-for"
--8<-- "includes/badges.html:visual-trace-table"
--8<-- "includes/badges.html:ct-patroonherkenning"
--8<-- "includes/badges.html:ae-describing-with-n"
--8<-- "includes/badges.html:process-formulating"
--8<-- "includes/badges.html:process-reflecting-solution"

## Waar werk je aan?

In deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **een volledige verzameling systematisch verwerken zonder elementen over te slaan**.
- Ik kan **tijdens een herhaling relevante informatie over een verzameling bijhouden**.
- Ik kan **met een Trace Table zichtbaar maken hoe de toestand tijdens de verwerking verandert**.
- Ik kan **patronen in de verwerking herkennen en uitleggen wat deze betekenen voor mijn oplossing**.

## Probleem

Monk heeft een verzameling tijdschriften die op dit moment nog niet op volgorde staat.

Ieder tijdschrift heeft een nummer. Voordat Monk de verzameling kan ordenen, wil hij weten welk tijdschrift het kleinste nummer heeft, welk tijdschrift het grootste nummer heeft en op welke positie beide tijdschriften nu staan.

Een computersysteem moet daarvoor de volledige verzameling systematisch kunnen verwerken zonder tijdschriften over te slaan of dubbel te behandelen.

**Hoe ontwerp je een algoritme dat een volledige gegevensverzameling systematisch verwerkt?**

## Understanding

{{ understanding_reference(understanding) }}

Wil je verder onderzoeken hoe je het aantal bewerkingen als functie van `n` kunt beschrijven?

Lees dan [Aantal bewerkingen als functie van n](../../understanding/algorithms-efficiency/describing-with-n/operation-count-function.md).

## Opdracht

Nu ga je deze kennis gebruiken om **Monk's Magazine Check** te maken.

Gebruik dezelfde verzameling als bij de Thinking Set:

```text
9 4 7 1 6 0 8 3 5 2
```

Sla deze nummers in Python op in een list.

Schrijf **voordat je programmeert** pseudocode waarin je beschrijft hoe je de volledige verzameling systematisch gaat verwerken en welke informatie je tijdens dat proces moet onthouden.

Laat deze pseudocode daarna als comments in je `.py`-bestand staan en bouw je Python-code eronder of ernaast.

Maak ook een **Trace Table** waarmee je vóór het uitvoeren van je programma voorspelt hoe de verwerking stap voor stap verloopt. Laat daarin minimaal zien:

- welke index wordt verwerkt;
- welk nummer op die index staat;
- welk kleinste nummer tot dat moment is onthouden en op welke index het staat;
- welk grootste nummer tot dat moment is onthouden en op welke index het staat;
- of deze stap een nieuw minimum, een nieuw maximum of geen verandering oplevert.

### Specificatie

Je programma gebruikt als eerste verzameling:

```python
magazines = [9, 4, 7, 1, 6, 0, 8, 3, 5, 2]
```

Je programma moet:

- de volledige list met een `for`-loop systematisch verwerken;
- `range()` en de indexes van de list gebruiken om de posities tijdens de verwerking te kunnen volgen;
- ieder element uit de verzameling precies één keer als onderdeel van de systematische verwerking behandelen;
- bepalen hoeveel tijdschriften in de verzameling staan;
- bepalen welk tijdschrift het kleinste nummer heeft;
- de index van dit kleinste nummer onthouden en tonen;
- bepalen welk tijdschrift het grootste nummer heeft;
- de index van dit grootste nummer onthouden en tonen;
- de resultaten uit de werkelijke inhoud van de list bepalen en dus geen uitkomsten hardcoderen.

Wanneer je voor een test alleen de inhoud van `magazines` vervangt door een andere niet-lege list met getallen, moet dezelfde verwerking blijven werken.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke informatie moet je onthouden?"

    Kijk naar wat je aan het einde van de verwerking moet kunnen tonen.

    Welke informatie moet tijdens het doorlopen van de verzameling beschikbaar blijven om dat eindresultaat te kunnen bepalen?

??? hint "2 — Waaraan herken je een verandering?"

    Vergelijk in je Trace Table de huidige waarde met wat op dat moment al is onthouden.

    Wanneer moet de onthouden informatie veranderen en wanneer juist niet?

??? hint "3 — Welke positie hoort bij een waarde?"

    Een waarde en de plaats waar die waarde staat zijn twee verschillende soorten informatie.

    Welke informatie geeft de huidige index je wanneer een nieuw minimum of maximum wordt gevonden?

??? hint "4 — Hoe doorloop je alle posities?"

    Je hebt niet alleen de waarden uit de list nodig, maar ook hun indexes.

    Bekijk in de Understanding hoe `range()` kan worden gecombineerd met de lengte van een list.

### Testen

Je programma werkt pas betrouwbaar wanneer het voor verschillende verzamelingen de juiste waarden én de juiste indexes oplevert.

Voer minimaal de volgende tests uit.

| Test | List | Verwacht aantal | Verwacht kleinste + index | Verwacht grootste + index | Werkelijke uitkomst |
| ---- | ---- | --------------- | ------------------------- | ------------------------- | ------------------- |
| 1 | `[9, 4, 7, 1, 6, 0, 8, 3, 5, 2]` | | | | |
| 2 | `[6, 2, 9, 4, 1, 7]` | | | | |
| 3 | `[1, 5, 3, 8]` | | | | |

Bepaal **vooraf** de verwachte uitkomst van iedere test.

Maak voor test 1 een volledige Trace Table en controleer daarin ook of iedere index van `0` tot en met `9` precies één keer als verwerkte positie voorkomt.

Controleer na iedere test:

- of het juiste aantal items wordt getoond;
- of het juiste kleinste nummer met de juiste index wordt getoond;
- of het juiste grootste nummer met de juiste index wordt getoond;
- of geen positie tijdens de systematische verwerking wordt overgeslagen of dubbel behandeld.

**Kun je met deze testgevallen aantonen dat je programma ieder element systematisch verwerkt en voor verschillende verzamelingen de juiste resultaten oplevert?**

Als de werkelijke uitvoer niet overeenkomt met je voorspelling, onderzoek dan waardoor het verschil ontstaat en pas je pseudocode en programma waar nodig aan.

## Reflectie op de oplossing

Bekijk je **pseudocode**, je **Trace Table** en je uiteindelijke **Python-programma**.

Kies één stap uit je Trace Table waarin het onthouden minimum of maximum verandert. Leg met dit concrete voorbeeld uit welke informatie je programma tijdens de verwerking moet onthouden en waarom jouw oplossingsrichting geschikt is om de volledige verzameling systematisch te verwerken.

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je pseudocode als comments in je `.py`-bestand staat;
- je Trace Table is toegevoegd;
- je programma met verschillende lists is getest;
- je verwachte en werkelijke testresultaten zijn vastgelegd;
- je reflectie is uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.
