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

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Jellybeans in a Jar** op te lossen.

### Specificatie

Je programma moet:

- het geheime aantal jellybeans in een variabele bewaren;
- de gebruiker vragen om een geheel getal;
- de ingevoerde gok vergelijken met het geheime aantal;
- `Precies goed` tonen wanneer de gok gelijk is aan het geheime aantal;
- `Te laag — dichtbij` tonen wanneer de gok lager is dan het geheime aantal en het verschil 10 of minder is;
- `Te laag — ver weg` tonen wanneer de gok lager is dan het geheime aantal en het verschil groter dan 10 is;
- `Te hoog — dichtbij` tonen wanneer de gok hoger is dan het geheime aantal en het verschil 10 of minder is;
- `Te hoog — ver weg` tonen wanneer de gok hoger is dan het geheime aantal en het verschil groter dan 10 is.

Gebruik voor de beslisstructuur `if`, `elif` en `else`. Gebruik daarnaast een **nested conditional** om binnen een situatie een volgende beslissing te nemen.

Voor iedere mogelijke gok moet het programma **precies één** passende reactie geven.

Gebruik als invoer een **geheel getal**. Dat is in deze Problem Set geldige invoer.

Andere invoer hoef je in deze Problem Set niet af te handelen.

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

??? hint "4 — Hoe zet je je flowchart om in pseudocode?"

    Gebruik je flowchart als ontwerp en beschrijf dezelfde oplossing nu als **pseudocode**.

    Schrijf de logica als een geordende reeks stappen en beslissingen.

    Let vooral op de beslissingen binnen beslissingen:

    - nummer de hoofdstappen;
    - gebruik subnummers en inspringing voor stappen die binnen een beslissing horen;
    - laat duidelijk zien wanneer binnen een route nog een volgende beslissing nodig is;
    - beschrijf **wat** er logisch moet gebeuren, zonder Python-code te schrijven.

    Controleer daarna: beschrijven je flowchart en pseudocode dezelfde routes en beslissingen?

??? hint "5 — Hoe vertaal je je pseudocode naar Python?"

    Gebruik je pseudocode als ontwerp voor je programma. Met `if`, `elif` en `else` kun je de hoofdsituaties uitdrukken.

    Als binnen een situatie nog een volgende beslissing nodig is, kijk dan naar de ingesprongen stappen in je pseudocode. Daar moet je programma binnen die branch opnieuw een condition controleren.

    Kijk naar je eigen pseudocode:

    - welke beslissingen vormen de hoofdsituaties?
    - binnen welke situaties staat nog een volgende beslissing?
    - welke condition hoort bij iedere beslissing?

    Bepaal op basis daarvan waar een **nested conditional** nodig is en programmeer vanuit je ontwerp verder.

### Testen

Een programma is pas betrouwbaar als je controleert of **alle mogelijke routes door je beslisstructuur correct worden afgehandeld**.

Noteer eerst welk geheime aantal je in je programma gebruikt.

Kies daarna zelf voor iedere onderstaande situatie een passende gok.

| Test | Situatie | Gok | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | -------- | --- | ------------------ | ------------------- |
| 1 | lager, verschil 10 | | `Te laag — dichtbij` | |
| 2 | lager, verschil 11 | | `Te laag — ver weg` | |
| 3 | precies gelijk | | `Precies goed` | |
| 4 | hoger, verschil 10 | | `Te hoog — dichtbij` | |
| 5 | hoger, verschil 11 | | `Te hoog — ver weg` | |

Bepaal **vooraf** welke concrete gok bij iedere situatie hoort en controleer of de verwachte uitkomst daarbij klopt.

Voer daarna iedere test uit.

Controleer met deze testgevallen:

- of iedere mogelijke soort feedback wordt bereikt;
- of een verschil van precies `10` als **dichtbij** wordt behandeld;
- of een verschil van `11` als **ver weg** wordt behandeld;
- of de grens zowel onder als boven het geheime aantal correct werkt;
- of iedere gok **precies één** reactie oplevert.

Vergelijk bij iedere test de werkelijke uitkomst met de verwachte uitkomst.

Een test is geslaagd wanneer:

**werkelijke uitkomst = verwachte uitkomst**

Als dat niet zo is, onderzoek dan welke condition of branch in je algoritme niet doet wat je had verwacht en pas je programma waar nodig aan.

**Kun je met deze vijf testgevallen aantonen dat iedere mogelijke route en de grens tussen dichtbij en ver weg correct worden afgehandeld?**

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je hebt voor iedere mogelijke situatie een **testgeval** uitgevoerd;
- de werkelijke uitkomst van je tests komt overeen met de **verwachte uitkomst**;
- je kunt uitleggen hoe je vanuit het probleem tot je **beslisstructuur** bent gekomen;
- je kunt uitleggen hoe je vanuit je flowchart via pseudocode tot `if`, `elif`, `else` en een nested conditional bent gekomen;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 3** bij.

