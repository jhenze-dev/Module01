---
title: Monk's Magazine Check
template: pset.html
week: 6
level: more

understanding:
  - python.for-loops
  - python.iterating-lists
  - python.range
  - python.list-indexes
  - algorithms-efficiency.counting-operations-basics
---

# Monk's Magazine Check

--8<-- "includes/badges.html:more-comfortable"
--8<-- "includes/badges.html:python-for"
--8<-- "includes/badges.html:visual-trace-table"
--8<-- "includes/badges.html:ct-patroonherkenning"
--8<-- "includes/badges.html:process-formulating"
--8<-- "includes/badges.html:process-reflecting-solution"

## Waar werk je aan?

In deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **een volledige verzameling systematisch verwerken zonder elementen over te slaan**.
- Ik kan **tijdens een herhaling meerdere soorten informatie over een verzameling bijhouden**.
- Ik kan **met een Trace Table zichtbaar maken hoe de toestand tijdens de verwerking verandert**.
- Ik kan **patronen in verschillende verwerkingen vergelijken, interpreteren en gebruiken om mijn oplossing te verantwoorden**.

## Probleem

Monk heeft een verzameling tijdschriften die op dit moment nog niet op volgorde staat.

Ieder tijdschrift heeft een nummer. Voordat Monk de verzameling kan ordenen, wil hij weten welk tijdschrift het kleinste nummer heeft, welk tijdschrift het grootste nummer heeft en op welke positie beide tijdschriften nu staan.

Monk wil bovendien onderzoeken wat er tijdens die verwerking gebeurt wanneer dezelfde tijdschriftnummers in een andere volgorde liggen.

Een computersysteem moet daarvoor de volledige verzameling systematisch kunnen verwerken zonder tijdschriften over te slaan of dubbel te behandelen.

**Hoe ontwerp je een algoritme dat een volledige gegevensverzameling systematisch verwerkt?**

## Understanding

{{ understanding_reference(understanding) }}

Wil je verder onderzoeken hoe je het aantal bewerkingen als functie van `n` kunt beschrijven?

Lees dan [Aantal bewerkingen als functie van n](../../understanding/algorithms-efficiency/describing-with-n/operation-count-function.md).

## Opdracht

Nu ga je deze kennis gebruiken om **Monk's Magazine Check** te maken en het gedrag van je verwerking verder te onderzoeken.

Gebruik eerst dezelfde verzameling als bij de Thinking Set:

```text
9 4 7 1 6 0 8 3 5 2
```

Sla deze nummers in Python op in een list.

Schrijf **voordat je programmeert** pseudocode waarin je beschrijft hoe je de volledige verzameling systematisch gaat verwerken, welke informatie je tijdens dat proces moet onthouden en welke veranderingen je wilt tellen.

Laat deze pseudocode daarna als comments in je `.py`-bestand staan en bouw je Python-code eronder of ernaast.

Maak een **Trace Table** waarin zichtbaar wordt hoe de onthouden informatie tijdens de verwerking verandert. Gebruik de Trace Table daarna om het gedrag van dezelfde verwerking bij verschillende volgordes te vergelijken.

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
- bepalen welk tijdschrift het kleinste nummer heeft en op welke index het staat;
- bepalen welk tijdschrift het grootste nummer heeft en op welke index het staat;
- bijhouden hoe vaak tijdens de verwerking een **nieuw minimum** wordt onthouden;
- bijhouden hoe vaak tijdens de verwerking een **nieuw maximum** wordt onthouden;
- deze aantallen samen met het uiteindelijke minimum, maximum en de bijbehorende indexes tonen;
- de resultaten uit de werkelijke inhoud van de list bepalen en dus geen uitkomsten hardcoderen.

Een wijziging telt alleen wanneer een eerder onthouden minimum of maximum daadwerkelijk door een nieuwe waarde wordt vervangen.

Wanneer je alleen de inhoud van `magazines` vervangt door dezelfde getallen in een andere volgorde, moet dezelfde verwerking blijven werken.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke toestand verandert tijdens de verwerking?"

    In deze versie houd je niet alleen het minimum, maximum en hun posities bij.

    Welke extra informatie heb je nodig om achteraf te kunnen vergelijken hoe vaak de onthouden waarden veranderden?

??? hint "2 — Welke stappen horen bij hetzelfde patroon?"

    Kijk naar de kolom in je Trace Table waarin je noteert wat er tijdens een stap verandert.

    Welke stappen kun je bij elkaar groeperen als:

    - nieuw minimum;
    - nieuw maximum;
    - geen verandering?

??? hint "3 — Wat verandert als de volgorde verandert?"

    De verzameling kan exact dezelfde getallen bevatten terwijl de volgorde anders is.

    Bedenk vóór het uitvoeren welke resultaten altijd hetzelfde moeten blijven en welke resultaten juist kunnen veranderen.

??? hint "4 — Gebruik dezelfde verwerking"

    Voor de verschillende testlijsten mag je alleen de inhoud van `magazines` veranderen.

    Als je daarnaast de rest van je programma moet aanpassen, onderzoek dan of je verwerking werkelijk algemeen voor een list is ontworpen.

### Testen

Onderzoek je programma met dezelfde tien getallen in drie verschillende volgordes.

| Test | List | Verwacht kleinste + index | Verwacht grootste + index | Verwachte wijzigingen minimum | Verwachte wijzigingen maximum | Werkelijke uitkomst |
| ---- | ---- | ------------------------- | ------------------------- | ----------------------------- | ----------------------------- | ------------------- |
| 1 | `[9, 4, 7, 1, 6, 0, 8, 3, 5, 2]` | | | | | |
| 2 | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` | | | | | |
| 3 | `[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]` | | | | | |

Bepaal **vooraf** alle verwachte uitkomsten.

Maak een volledige Trace Table voor test 1 en voor minimaal één van de twee andere volgordes. Controleer daarin ook of iedere index precies één keer als verwerkte positie voorkomt.

Vergelijk daarna de drie tests en controleer:

- welke eindwaarden gelijk blijven;
- welke indexes veranderen;
- hoe vaak het onthouden minimum verandert;
- hoe vaak het onthouden maximum verandert;
- of iedere positie tijdens iedere verwerking precies één keer wordt behandeld.

**Kun je met je testresultaten aantonen welke delen van de verwerking onafhankelijk zijn van de volgorde en welke delen juist door de volgorde worden beïnvloed?**

Als de werkelijke resultaten niet overeenkomen met je voorspellingen, onderzoek dan waardoor het verschil ontstaat en pas je pseudocode en programma waar nodig aan.

## Reflectie op de oplossing

Bekijk je **pseudocode**, je **Trace Tables** en de resultaten van de drie volgordes.

Beschrijf een patroon dat je in de drie verwerkingen hebt gevonden. Leg met concrete resultaten uit wat ondanks de veranderde volgorde hetzelfde bleef, wat veranderde en waarom jouw oplossingsrichting geschikt is om iedere verzameling met dezelfde werkwijze te verwerken.

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je pseudocode als comments in je `.py`-bestand staat;
- je Trace Tables zijn toegevoegd;
- de drie volgordes zijn getest;
- je verwachte en werkelijke testresultaten zijn vastgelegd;
- je vergelijking en reflectie zijn uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.
