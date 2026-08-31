---
title: Keep the Change
template: pset.html
week: 4
level: less

understanding:
  - python.while-loops
---

# Keep the Change

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-while"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"

## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** hoe een herhalend proces stap voor stap verandert.
- Ik kan **een algoritmische oplossing ontwerpen** waarin een proces doorgaat zolang het doel nog niet is bereikt.
- Ik kan **een oplossing automatiseren** door herhalende stappen en een stopvoorwaarde vast te leggen.
- Ik kan **een algoritmische oplossing programmeren** met een `while`-loop.

## Probleem

In *Home Alone* betaalt een klant meer voor zijn pizza dan nodig is.

De pizzabezorger moet het juiste wisselgeld teruggeven. Daarbij moet het systeem bepalen welke munten samen het bedrag vormen.

Een computersysteem moet het wisselgeld niet in één keer bepalen. Het moet het proces stap voor stap uitvoeren en na iedere stap opnieuw bepalen hoeveel wisselgeld nog over is.

Het proces gaat door totdat het volledige bedrag is teruggegeven.

**Hoe ontwerp je een systeem dat stap voor stap wisselgeld teruggeeft en weet wanneer het klaar is?**

## Demo

[DEMO LATER TOEVOEGEN]

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Keep the Change** op te lossen.

Ontwerp en programmeer een systeem dat wisselgeld stap voor stap teruggeeft.

Werk je oplossing eerst uit als een **loop-flowchart**.

Zet daarna dezelfde oplossing om in **pseudocode**. Schrijf je pseudocode als genummerde comments in je `.py`-bestand en bouw daarna de Python-code bij deze stappen.

### Specificatie

Je programma moet:

- een bedrag aan wisselgeld vragen;
- het wisselgeld teruggeven met Nederlandse munten van **5 cent, 10 cent, 20 cent, 50 cent, 1 euro en 2 euro**;
- steeds opnieuw bepalen welke munt gebruikt kan worden;
- na iedere munt het resterende bedrag aanpassen;
- doorgaan zolang er nog wisselgeld over is;
- stoppen wanneer het volledige bedrag is teruggegeven;
- de gebruikte munten duidelijk tonen.

Gebruik voor de herhaling een `while`-loop.

Het programma moet het wisselgeld teruggeven met **zo groot mogelijke munten**.

Gebruik voor je programma bedragen in hele centen.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Wat verandert er tijdens het proces?"

    Kijk niet meteen naar Python.

    Beschrijf eerst wat er verandert nadat je één munt hebt teruggegeven.

    - Welk bedrag heb je aan het begin?
    - Wat gebeurt er nadat je een munt hebt gekozen?
    - Welke informatie heb je nodig om verder te kunnen?

??? hint "2 — Wanneer moet het proces doorgaan?"

    Een herhalend proces heeft iets nodig waarmee je kunt bepalen of er nog een volgende stap nodig is.

    Kijk naar het bedrag dat na iedere stap overblijft.

    **Wanneer moet het systeem doorgaan en wanneer is het klaar?**

??? hint "3 — Hoe maak je het herhalende proces zichtbaar?"

    Maak eerst een **loop-flowchart**.

    Laat daarin zien:

    - welke toestand je aan het begin hebt;
    - welke handeling wordt herhaald;
    - hoe de toestand daarna verandert;
    - wanneer het proces doorgaat;
    - wanneer het proces stopt.

    Controleer daarna of je flowchart ook werkt wanneer er meerdere munten nodig zijn.

??? hint "4 — Hoe zet je je flowchart om in pseudocode?"

    Beschrijf dezelfde oplossing nu in gewone taal.

    Maak zichtbaar:

    - welke stappen worden herhaald;
    - wanneer de herhaling doorgaat;
    - wat tijdens iedere herhaling verandert;
    - wanneer het proces stopt.

    Schrijf deze stappen als genummerde comments in je `.py`-bestand.

    Beschrijf **wat** er moet gebeuren. Schrijf hier nog geen Python-syntax.

??? hint "5 — Hoe vertaal je de herhaling naar Python?"

    Gebruik je pseudocode als ontwerp voor je programma.

    Een `while`-loop herhaalt een blok code zolang een voorwaarde waar is.

    ```python
    while voorwaarde:
        actie
    ```

    Kijk naar je eigen flowchart:

    - welke voorwaarde bepaalt of het proces doorgaat?
    - welke waarde verandert tijdens iedere herhaling?
    - welke handelingen horen binnen de `while`-loop?

    Programmeer vanuit je eigen ontwerp verder.

### Testen

Een programma is pas betrouwbaar als je controleert of **het wisselgeld voor verschillende bedragen correct en volledig wordt teruggegeven**.

Test minimaal de volgende situaties:

| Test | Wisselgeld | Verwachte munten | Werkelijke munten |
| ---- | ---------- | ---------------- | ----------------- |
|  1   |    50      |                  |                   |
|  2   |    135     |                  |                   |
|  3   |    285     |                  |                   |

Zorg dat je testgevallen samen controleren:

- een bedrag waarvoor één munt voldoende is;
- een bedrag waarvoor meerdere munten nodig zijn;
- een bedrag waarbij verschillende muntwaarden worden gebruikt;
- een bedrag waarbij het proces meerdere keren moet herhalen.

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

**Kun je met je testgevallen aantonen dat je programma het volledige wisselgeld correct teruggeeft en stopt wanneer het klaar is?**

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je gebruikt een `while`-loop voor de herhaling;
- het resterende wisselgeld wordt na iedere stap aangepast;
- je programma stopt wanneer het wisselgeld volledig is teruggegeven;
- je hebt verschillende bedragen getest;
- je pseudocode staat als genummerde comments in je `.py`-bestand;
- je kunt uitleggen hoe je flowchart via pseudocode is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna je portfolio bij.
