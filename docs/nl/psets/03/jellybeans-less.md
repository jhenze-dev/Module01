---
title: Jellybeans in a Jar
template: pset.html
week: 3
level: less

understanding:
  - python.boolean-expressions
  - python.comparison-operators
  - python.conditions
  - python.if
  - python.else
  - python.elif
  - python.indentation
  - python.branches
---

# Jellybeans in a Jar

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-if"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"

## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** hoe stappen en beslissingen logisch met elkaar samenhangen.
- Ik kan **een algoritmische oplossing ontwerpen** voor een probleem met verschillende mogelijke situaties.
- Ik kan **een oplossing automatiseren** door voorwaarden en bijbehorende acties vast te leggen.
- Ik kan **een algoritmische oplossing programmeren** met `if`, `elif` en `else`.

## Probleem

In een pot zit een onbekend aantal jellybeans.

De gebruiker voert een gok in. Een computersysteem moet deze ingevoerde gok vergelijken met het geheime aantal en op basis daarvan automatisch bepalen welke terugkoppeling aan de gebruiker wordt gegeven:

- **te laag**;
- **te hoog**;
- **precies goed**.

Een computer kan alleen de juiste beslissing nemen wanneer **alle mogelijke situaties expliciet zijn beschreven met voorwaarden en bijbehorende acties**.

**Hoe ontwerp je een systeem dat op basis van voorwaarden automatisch bepaalt welke feedback aan een gebruiker wordt gegeven?**

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

Nu ga je deze kennis gebruiken om het probleem van **Jellybeans in a Jar** op te lossen.

### Specificatie

Je programma moet:

- het geheime aantal jellybeans in een variabele bewaren;
- de gebruiker vragen om een geheel getal;
- de ingevoerde gok vergelijken met het geheime aantal;
- `Te laag` tonen wanneer de gok lager is dan het geheime aantal;
- `Te hoog` tonen wanneer de gok hoger is dan het geheime aantal;
- `Precies goed` tonen wanneer de gok gelijk is aan het geheime aantal.

Gebruik voor de beslisstructuur `if`, `elif` en `else`.

Voor iedere mogelijke gok moet het programma **precies één** van de drie mogelijke reacties geven.

Gebruik als invoer een **geheel getal**. Dat is in deze Problem Set geldige invoer.

Andere invoer hoef je in deze Problem Set niet af te handelen.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke situaties moet je programma herkennen?"

    Begin nog niet met programmeren. Kijk naar de relatie tussen de **gok** en het **geheime aantal**.

    Welke verschillende situaties zijn mogelijk? Schrijf voor iedere situatie op:

    - welke **voorwaarde** geldt;
    - welke **actie** het programma dan moet uitvoeren.

    Controleer daarna of je hiermee **alle mogelijke situaties** hebt beschreven.

??? hint "2 — Hoe kun je de beslissingen zichtbaar maken?"

    Zet je voorwaarden en acties om in een **flowchart**. Begin bij de ingevoerde gok en laat daarna zien welke beslissingen het programma moet nemen.

    Denk bij iedere beslissing na over twee vragen:

    - Welke voorwaarde wordt hier gecontroleerd?
    - Waar gaat het algoritme verder als de voorwaarde wel of niet waar is?

    Controleer je flowchart voordat je verdergaat: kan iedere mogelijke gok via één route bij de juiste feedback uitkomen?

??? hint "3 — Hoe zet je je flowchart om in pseudocode?"

    Gebruik je flowchart als ontwerp en beschrijf dezelfde oplossing nu als **pseudocode**.

    Schrijf de logica als een geordende reeks stappen en beslissingen.

    Let erop dat:

    - iedere regel één logische actie beschrijft;
    - je de stappen nummert;
    - stappen die bij een beslissing horen duidelijk zijn ingesprongen;
    - je beschrijft **wat** er moet gebeuren, zonder Python-code te schrijven.

    Controleer daarna: beschrijven je flowchart en pseudocode dezelfde oplossing?

??? hint "4 — Hoe vertaal je je pseudocode naar Python?"

    Gebruik nu je pseudocode als ontwerp voor je programma. Een beslissing uit je pseudocode kun je in Python uitdrukken met een voorwaarde:

    ```python
    if voorwaarde:
        actie
    ```

    Voor meerdere mogelijke situaties kun je beslissingen combineren met `if`, `elif` en `else`.

    Kijk opnieuw naar je eigen pseudocode:

    - welke beslissing hoort bij `if`?
    - welke volgende mogelijkheid hoort bij `elif`?
    - welke situatie blijft daarna over voor `else`?

    Programmeer vanuit je ontwerp verder.

### Testen

Een programma is pas betrouwbaar als je controleert of **alle mogelijke situaties correct worden afgehandeld**.

Noteer eerst welk geheime aantal je in je programma gebruikt.

Kies daarna voor iedere situatie een passende gok en bepaal **vooraf** welke uitkomst je verwacht.

| Test | Situatie | Gok | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | -------- | --- | ------------------ | ------------------- |
| 1 | lager dan het geheime aantal | | `Te laag` | |
| 2 | hoger dan het geheime aantal | | `Te hoog` | |
| 3 | gelijk aan het geheime aantal | | `Precies goed` | |

Voer daarna iedere test uit.

Controleer bij iedere test:

- of de werkelijke uitkomst overeenkomt met de verwachte uitkomst;
- of de juiste situatie wordt herkend;
- of het programma **precies één** reactie toont.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan welke stap of beslissing in je algoritme niet doet wat je had verwacht en pas je programma waar nodig aan.

**Kun je met deze drie testgevallen aantonen dat iedere mogelijke situatie correct wordt afgehandeld en iedere gok precies één reactie oplevert?**

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt voor iedere mogelijke situatie een **testgeval** uitgevoerd;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit het probleem tot je **beslisstructuur** bent gekomen;
- je kunt uitleggen hoe je vanuit je flowchart via pseudocode tot `if`, `elif` en `else` bent gekomen;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 3** bij.
