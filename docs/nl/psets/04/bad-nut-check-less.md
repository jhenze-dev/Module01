---
title: Bad Nut Check
template: pset.html
week: 4
level: less

resources:
  - video.bad-nut-check

understanding:
  - python.input-validation
---

# PSET 4B *Bad Nut Check*

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-input-validation"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-reflecting-solution"

## Charlie and the Chocolate Factory — Squirrel Attack

--8<-- "includes/videos.html:bad-nut-check"

## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** wanneer invoer wel of niet bruikbaar is.
- Ik kan **een algoritmische oplossing ontwerpen** waarin invoer wordt gecontroleerd voordat het systeem verdergaat.
- Ik kan **een oplossing automatiseren** door voorwaarden voor geldige invoer vast te leggen.
- Ik kan **een controlesysteem programmeren** dat invoer afwijst wanneer deze niet aan de voorwaarden voldoet.

## Probleem

In *Charlie and the Chocolate Factory* controleren de eekhoorns de noten van Willy Wonka.

Een noot die niet voldoet aan de voorwaarden wordt afgekeurd.

Een computersysteem moet invoer controleren voordat het deze accepteert.

Wanneer de invoer niet bruikbaar is, moet het systeem de invoer afwijzen en opnieuw om invoer vragen. Wanneer de invoer wel bruikbaar is, stopt het controleproces.

**Hoe ontwerp je een systeem dat invoer controleert en pas stopt wanneer bruikbare invoer is gegeven?**

## Demo

[DEMO LATER TOEVOEGEN]

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Bad Nut Check** op te lossen.

Ontwerp en programmeer een controlesysteem dat invoer blijft controleren totdat bruikbare invoer wordt gegeven.

Werk je oplossing eerst uit als een **flowchart**.

Zet daarna dezelfde oplossing om in **pseudocode**. Schrijf je pseudocode als genummerde comments in je `.py`-bestand en bouw daarna de Python-code bij deze stappen.

### Specificatie

Je programma moet:

- de gebruiker om een noot vragen;
- `amandel`, `hazelnoot` en `walnoot` accepteren als geldige invoer;
- andere invoer afwijzen;
- feedback geven wanneer de invoer niet voldoet;
- opnieuw om invoer vragen na een afwijzing;
- stoppen zodra een geldige noot wordt ingevoerd.

Het programma moet dus niet vooraf bepalen hoeveel pogingen nodig zijn.

De gebruiker kan net zo lang ongeldige invoer geven als nodig is.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke invoer is bruikbaar?"

    Begin nog niet met programmeren.

    Bedenk eerst aan welke voorwaarden invoer moet voldoen voordat het systeem deze kan accepteren.

??? hint "2 — Wat moet er gebeuren wanneer invoer niet voldoet?"

    Kijk naar het gedrag van het systeem.

    - Wat moet het programma laten weten?
    - Wat moet er daarna gebeuren?
    - Wanneer kan het programma verdergaan?

??? hint "3 — Hoe maak je het controlesysteem zichtbaar?"

    Maak eerst een **flowchart**.

    Laat daarin zien:

    - waar invoer wordt ontvangen;
    - waar de invoer wordt gecontroleerd;
    - wat er gebeurt wanneer de invoer niet voldoet;
    - hoe een nieuwe poging ontstaat;
    - wanneer het programma stopt.

    Controleer of je flowchart ook werkt wanneer meerdere pogingen nodig zijn.

??? hint "4 — Hoe zet je je flowchart om in pseudocode?"

    Beschrijf dezelfde oplossing nu in gewone taal.

    Maak zichtbaar:

    - waar invoer wordt ontvangen;
    - welke controles worden uitgevoerd;
    - wat er gebeurt wanneer invoer niet voldoet;
    - welke stappen daarna opnieuw worden uitgevoerd;
    - wanneer het controleproces stopt.

    Schrijf deze stappen als genummerde comments in je `.py`-bestand.

    Beschrijf **wat** het systeem moet doen. Schrijf hier nog geen Python-syntax.

??? hint "5 — Hoe vertaal je je ontwerp naar Python?"

    Gebruik je pseudocode als ontwerp voor je programma.

    Kijk naar de controles en de waarden die tijdens het proces nodig zijn.

    Bepaal daarna welke Python-instructies je nodig hebt om je ontwerp uit te voeren.

### Testen

Een programma is pas betrouwbaar als je controleert of **geldige en ongeldige invoer correct worden afgehandeld en het controleproces op het juiste moment stopt**.

Voer minimaal de volgende tests uit:

| Test | Invoerreeks | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | ----------- | ------------------ | ------------------- |
| 1 | `amandel` | | |
| 2 | `hazelnoot` | | |
| 3 | `walnoot` | | |
| 4 | `pinda` → `amandel` | | |
| 5 | `pinda` → `cashew` → `walnoot` | | |

Bepaal **vooraf** wat je bij iedere test verwacht.

Controleer met deze tests:

- of `amandel`, `hazelnoot` en `walnoot` worden geaccepteerd;
- of andere invoer wordt afgewezen;
- of het programma feedback geeft bij iedere afgewezen invoer;
- of het programma na iedere afwijzing opnieuw om invoer vraagt;
- of meerdere ongeldige pogingen achter elkaar kunnen worden afgehandeld;
- of het programma blijft doorgaan zolang de invoer ongeldig is;
- of het programma stopt zodra geldige invoer wordt gegeven.

Leg bij iedere test de **verwachte uitkomst** en de **werkelijke uitkomst** vast.

**Kun je met deze testgevallen aantonen dat het programma iedere ongeldige invoer blijft afwijzen, opnieuw om invoer vraagt en pas stopt wanneer geldige invoer is gegeven?**

Als de werkelijke uitkomst niet overeenkomt met je verwachting, onderzoek dan waar het verschil ontstaat en pas je programma waar nodig aan.

## Reflectie op de oplossing

Beschrijf na het testen:

1. **Hoe heb je gecontroleerd of je oplossing bleef werken wanneer meerdere ongeldige invoeren achter elkaar werden gegeven?**

2. **Welke situatie heeft je het meest geholpen om een fout in je oplossing te ontdekken?**

3. **Hoe weet je dat je programma precies op het juiste moment stopt?**

4. **Wat heb je veranderd nadat je je oplossing had getest?**

## Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je flowchart laat het controlesysteem duidelijk zien;
- je pseudocode staat als genummerde comments in je `.py`-bestand;
- je kunt uitleggen hoe je flowchart via pseudocode is vertaald naar Python;
- je hebt verschillende soorten invoer getest;
- je hebt getest met meerdere ongeldige pogingen achter elkaar;
- je hebt getest met geldige invoer na meerdere pogingen;
- je verwachte en werkelijke testresultaten zijn vastgelegd;
- je hebt je antwoorden op de reflectievragen uitgewerkt;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna je portfolio bij.
