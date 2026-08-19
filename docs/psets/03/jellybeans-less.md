---
title: Jellybeans in a Jar — minder vertrouwd
template: pset.html
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

--8<-- "understanding/_content/python/boolean-expressions.md"

--8<-- "understanding/_content/python/comparison-operators.md"

--8<-- "understanding/_content/python/conditions.md"

--8<-- "understanding/_content/python/if.md"

--8<-- "understanding/_content/python/else.md"

--8<-- "understanding/_content/python/elif.md"

--8<-- "understanding/_content/python/indentation.md"

--8<-- "understanding/_content/python/branches.md"

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

??? hint "3 — Hoe vertaal je je flowchart naar Python?"

    Gebruik nu je flowchart als ontwerp voor je programma. Een beslissing uit je flowchart kun je in Python uitdrukken met een voorwaarde:

    ```python
    if voorwaarde:
        actie
    ```

    Voor meerdere mogelijke situaties kun je beslissingen combineren met `if`, `elif` en `else`.

    Kijk opnieuw naar je eigen flowchart:

    - welke beslissing hoort bij `if`?
    - welke volgende mogelijkheid hoort bij `elif`?
    - welke situatie blijft daarna over voor `else`?

    Programmeer vanuit je ontwerp verder.

### Testen

Een programma is pas betrouwbaar als je controleert of **alle mogelijke situaties** correct worden afgehandeld. Kijk daarom naar je flowchart en je beslisstructuur: iedere mogelijke route door je programma vraagt om een eigen testgeval.

Bedenk voor iedere situatie:

- welke **invoer** je gebruikt;
- welke **uitkomst je verwacht**;
- welke **uitkomst je programma werkelijk geeft**.

Gebruik bijvoorbeeld een tabel als deze:

| Test | Invoer | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | ------ | ------------------ | ------------------- |
| 1    |        |                    |                     |
| 2    |        |                    |                     |
| 3    |        |                    |                     |

Zorg dat je minimaal test:

- een gok die lager is dan het geheime aantal;
- een gok die hoger is dan het geheime aantal;
- een gok die precies gelijk is aan het geheime aantal.

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan welke stap of beslissing in je algoritme niet doet wat je had verwacht.

**Kun je met je testgevallen aantonen dat iedere mogelijke situatie correct wordt afgehandeld?**

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt voor iedere mogelijke situatie een **testgeval** uitgevoerd;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit het probleem tot je **beslisstructuur** bent gekomen;
- je kunt uitleggen hoe je flowchart is vertaald naar `if`, `elif` en `else`;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 3** bij.

