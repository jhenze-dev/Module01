---
title: Jellybeans in a Jar
template: pset.html
week: 3
level: more

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

--8<-- "includes/badges.html:more-comfortable"
--8<-- "includes/badges.html:python-if"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"

## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** hoe stappen en beslissingen logisch met elkaar samenhangen.
- Ik kan **een algoritmische oplossing ontwerpen** voor een probleem met verschillende mogelijke situaties en beslissingen binnen beslissingen.
- Ik kan **een oplossing automatiseren** door voorwaarden en bijbehorende acties vast te leggen.
- Ik kan **een algoritmische oplossing programmeren** met `if`, `elif`, `else` en nested conditionals.

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

{% if render_mode == "module_pdf" %}

{{ understanding_reference(understanding) }}

{% else %}

--8<-- "understanding/_content/python/boolean-expressions.md"

--8<-- "understanding/_content/python/comparison-operators.md"

--8<-- "understanding/_content/python/conditions.md"

--8<-- "understanding/_content/python/if.md"

--8<-- "understanding/_content/python/else.md"

--8<-- "understanding/_content/python/elif.md"

--8<-- "understanding/_content/python/indentation.md"

--8<-- "understanding/_content/python/branches.md"

{% endif %}

## Opdracht

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Jellybeans in a Jar** op te lossen.

### Specificatie

Je programma moet:

- het geheime aantal jellybeans in een variabele bewaren;
- de gebruiker vragen om een geheel getal;
- de ingevoerde gok vergelijken met het geheime aantal;
- `Precies goed` tonen wanneer de gok gelijk is aan het geheime aantal;
- wanneer de gok te laag is, bepalen of de gok **dichtbij** of **ver weg** is;
- wanneer de gok te hoog is, bepalen of de gok **dichtbij** of **ver weg** is;
- een gok als **dichtbij** beschouwen wanneer het verschil met het geheime aantal 10 of minder is;
- passende feedback tonen voor iedere mogelijke situatie.

Gebruik voor de beslisstructuur `if`, `elif` en `else`. Gebruik daarnaast een **nested conditional** om binnen een situatie een volgende beslissing te nemen.

Voor iedere mogelijke gok moet het programma **precies één** passende reactie geven.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke beslissingen moet je programma nemen?"

    Begin nog niet met programmeren. Kijk eerst naar de relatie tussen de **gok** en het **geheime aantal**.

    Welke hoofdsituaties zijn mogelijk?

    Bedenk daarna bij welke hoofdsituaties het programma nog niet genoeg weet om de juiste feedback te geven. Waar is een **volgende beslissing** nodig?

    Schrijf de verschillende situaties op en controleer of je daarmee alle mogelijke uitkomsten van het programma hebt beschreven.

??? hint "2 — Hoe bepaal je of een gok dichtbij is?"

    Om te bepalen of een gok **dichtbij** of **ver weg** is, moet je weten hoeveel de gok van het geheime aantal verschilt.

    Daarvoor heb je het **verschil tussen de gok en het geheime aantal** nodig.

    Bedenk:

    - welke berekening je nodig hebt om dit verschil te bepalen;
    - wanneer het verschil betekent dat de gok **dichtbij** is;
    - wanneer het verschil betekent dat de gok **ver weg** is.

    Denk daarbij zowel aan een gok die **lager** is dan het geheime aantal als aan een gok die **hoger** is.

??? hint "3 — Hoe kun je de beslissingen zichtbaar maken?"

    Zet je beslissingen om in een **flowchart**. Begin bij de ingevoerde gok en laat zien welke beslissing het programma als eerste moet nemen.

    Sommige routes hebben daarna nog een **volgende beslissing** nodig. Laat ook deze beslissingen en de bijbehorende branches zichtbaar worden in je flowchart.

    Noteer bij iedere beslissing welke **condition** wordt gecontroleerd en laat zien welke route bij iedere mogelijke uitkomst wordt gevolgd.

    Controleer je ontwerp: kan iedere mogelijke gok via één route bij de juiste feedback uitkomen?

??? hint "4 — Hoe vertaal je je flowchart naar Python?"

    Gebruik je flowchart als ontwerp voor je programma. Met `if`, `elif` en `else` kun je de hoofdsituaties uitdrukken.

    Als binnen een branch nog een volgende condition moet worden gecontroleerd, kun je binnen die branch opnieuw een `if` statement plaatsen.

    Kijk naar je eigen flowchart:

    - welke beslissingen vormen de hoofdsituaties?
    - binnen welke branches is nog een volgende beslissing nodig?
    - welke condition hoort bij iedere beslissing?

    Bepaal op basis daarvan waar een **nested conditional** nodig is en programmeer vanuit je ontwerp verder.

### Testen

Een programma is pas betrouwbaar als je controleert of **alle mogelijke routes** door je beslisstructuur correct worden afgehandeld. Gebruik daarom je flowchart om je testgevallen te bepalen.

Bedenk voor iedere route:

- welke **invoer** je gebruikt;
- welke **uitkomst je verwacht**;
- welke **uitkomst je programma werkelijk geeft**.

Gebruik bijvoorbeeld een tabel als deze:

| Test | Invoer | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | ------ | ------------------ | ------------------- |
| 1    |        |                    |                     |
| 2    |        |                    |                     |
| 3    |        |                    |                     |
| 4    |        |                    |                     |
| 5    |        |                    |                     |

Zorg dat je minimaal iedere mogelijke soort feedback test. Test daarnaast zorgvuldig de **grens** tussen dichtbij en ver weg.

Bepaal **vooraf** wat de verwachte uitkomst van iedere test is. Voer daarna je programma uit en vergelijk de werkelijke uitkomst met je verwachting.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan welke condition of branch in je algoritme niet doet wat je had verwacht.

**Kun je met je testgevallen aantonen dat iedere mogelijke route door je beslisstructuur correct wordt afgehandeld?**

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt voor iedere mogelijke situatie een **testgeval** uitgevoerd;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit het probleem tot je **beslisstructuur** bent gekomen;
- je kunt uitleggen hoe je flowchart is vertaald naar `if`, `elif`, `else` en een nested conditional;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 3** bij.

