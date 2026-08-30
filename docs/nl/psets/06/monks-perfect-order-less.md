---
title: Monk's Perfect Order
template: pset.html
week: 6
level: less

understanding:
  - python.changing-list-items
---

# Monk's Perfect Order

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-for"
--8<-- "includes/badges.html:visual-trace-table"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"
--8<-- "includes/badges.html:process-reflecting-solution"

## Waar werk je aan?

In deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren hoe opeenvolgende stappen logisch samenhangen in een algoritme**.
- Ik kan **een algoritmische oplossing uitdrukken in pseudocode en Python**.
- Ik kan **met een Trace Table zichtbaar maken hoe een verzameling stap voor stap wordt geordend**.
- Ik kan **met testresultaten uitleggen waarom mijn gekozen strategie werkt**.

## Probleem

Monk wil zijn volledige verzameling tijdschriften op nummer ordenen.

Hij gebruikt daarvoor een vaste werkwijze: hij bekijkt steeds **twee tijdschriften die naast elkaar staan**. Staan ze in de verkeerde volgorde, dan verwisselt hij ze. Daarna gaat hij verder met het volgende paar.

Eén ronde langs de verzameling is niet altijd genoeg. Een tijdschrift kan meerdere rondes nodig hebben om uiteindelijk op de juiste plaats terecht te komen.

Een computer moet deze werkwijze systematisch kunnen uitvoeren totdat de volledige verzameling van klein naar groot staat.

**Hoe ontwerp je een algoritme dat een verzameling systematisch ordent?**

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Maak **Monk's Perfect Order**.

Gebruik dezelfde verzameling tijdschriftnummers:

```python
magazines = [9, 4, 7, 1, 6, 0, 8, 3, 5, 2]
```

Ontwerp eerst in **pseudocode** hoe één ronde door de verzameling verloopt en hoe meerdere rondes samen tot een volledig geordende list leiden.

Laat je pseudocode daarna als comments in je `.py`-bestand staan.

Voordat je programmeert, traceer je de strategie met deze kleinere list:

```text
[4, 1, 3, 2]
```

Maak een **Trace Table** waarin je per vergelijking minimaal noteert:

- de ronde;
- de twee indexes die worden vergeleken;
- de twee waarden vóór de vergelijking;
- of er wordt gewisseld;
- de list na deze stap.

Gebruik je Trace Table daarna als ontwerp voor je Python-programma.

### Specificatie

Je programma gebruikt als eerste verzameling:

```python
magazines = [9, 4, 7, 1, 6, 0, 8, 3, 5, 2]
```

Je programma moet:

- de verzameling ordenen van het kleinste naar het grootste nummer;
- de ordening uitvoeren door de list in meerdere rondes systematisch te verwerken;
- binnen iedere ronde met een `for`-loop, `range()` en indexes steeds twee **naast elkaar staande** items vergelijken;
- binnen een ronde de paren van links naar rechts verwerken;
- twee items alleen verwisselen wanneer het linker nummer groter is dan het rechter nummer;
- voor een list met `n` items `n - 1` volledige rondes uitvoeren;
- bij het verwisselen de waarden in de bestaande list aanpassen;
- na de laatste ronde de volledig geordende list tonen;
- dezelfde code blijven gebruiken wanneer alleen de inhoud van `magazines` wordt vervangen door een andere niet-lege list met getallen.

Je mag voor het ordenen **geen** `.sort()` of `sorted()` gebruiken.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Wat gebeurt er in één ronde?"

    Kijk eerst alleen naar één ronde.

    Welke paren worden achtereenvolgens vergeleken wanneer je van links naar rechts door een list gaat?

??? hint "2 — Welke indexes horen bij één vergelijking?"

    Wanneer de linker positie index `i` heeft, welke index heeft het item dat er direct rechts naast staat?

??? hint "3 — Wat gebeurt er na een wisseling?"

    Twee waarden veranderen van positie, maar de lengte van de list verandert niet.

    Bekijk in de Understanding hoe je twee bestaande list-items met behulp van een tijdelijke variable kunt verwisselen.

??? hint "4 — Waarom zijn meerdere rondes nodig?"

    Gebruik je Trace Table van `[4, 1, 3, 2]`.

    Kijk na de eerste ronde welke waarden al goed staan en welke waarde nog meer dan één positie moet opschuiven.

### Testen

Voorspel eerst voor iedere test hoe de list er na alle rondes uit moet zien.

| Test | List | Verwachte geordende list | Werkelijke geordende list |
| ---- | ---- | ------------------------ | ------------------------- |
| 1 | `[9, 4, 7, 1, 6, 0, 8, 3, 5, 2]` | | |
| 2 | `[0, 1, 2, 3, 4]` | | |
| 3 | `[4, 3, 2, 1, 0]` | | |
| 4 | `[3, 1, 3, 2]` | | |

Controleer daarnaast met je Trace Table van `[4, 1, 3, 2]`:

- of binnen iedere ronde alleen naast elkaar staande items worden vergeleken;
- of alleen wordt gewisseld wanneer het linker nummer groter is;
- of de list na iedere stap overeenkomt met je voorspelling;
- of de volledige list na de laatste ronde geordend is.

**Kun je met deze tests aantonen dat dezelfde strategie ook werkt voor een al geordende list, een omgekeerd geordende list en een list waarin een waarde vaker voorkomt?**

Als een werkelijke uitkomst niet overeenkomt met je voorspelling, onderzoek dan in welke vergelijking of ronde het verschil ontstaat en pas je pseudocode en programma waar nodig aan.

## Reflectie op de oplossing

Bekijk je **pseudocode**, je **Trace Table** en je testresultaten.

Kies één concrete wisseling uit je Trace Table en leg uit waarom die wisseling volgens jouw algoritme nodig was.

Leg daarna uit waarom meerdere rondes nodig kunnen zijn om de volledige verzameling te ordenen en gebruik daarbij een concreet voorbeeld uit je eigen Trace Table of testresultaten.

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je pseudocode als comments in je `.py`-bestand staat;
- je Trace Table van `[4, 1, 3, 2]` is toegevoegd;
- alle vier de tests zijn uitgevoerd;
- je verwachte en werkelijke testresultaten zijn vastgelegd;
- je reflectie is uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.
