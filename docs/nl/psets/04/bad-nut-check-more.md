---
title: Bad Nut Check
template: pset.html
week: 4
level: more

resources:
  - video.bad-nut-check

understanding:
  - python.input-validation
---

# PSET 4B *Bad Nut Check*

--8<-- "includes/badges.html:more-comfortable"
--8<-- "includes/badges.html:python-while"
--8<-- "includes/badges.html:python-input-validation"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-reflecting-solution"

## Charlie and the Chocolate Factory — Squirrel Attack

--8<-- "includes/videos.html:bad-nut-check"

## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** hoe verschillende controles samen bepalen of invoer bruikbaar is.
- Ik kan **een algoritmische oplossing ontwerpen** waarin invoer wordt bewerkt, gecontroleerd en opnieuw gevraagd wanneer deze niet voldoet.
- Ik kan **een oplossing automatiseren** door meerdere voorwaarden en een stopvoorwaarde vast te leggen.
- Ik kan **een controlesysteem programmeren** dat invoer blijft controleren totdat aan alle voorwaarden is voldaan.

## Probleem

In *Charlie and the Chocolate Factory* worden de controles van de eekhoorns steeds strenger.

Invoer is niet automatisch bruikbaar omdat deze er op het eerste gezicht goed uitziet. Het systeem moet invoer eerst geschikt maken voor controle en daarna bepalen of deze aan alle voorwaarden voldoet.

De controle wordt herhaald totdat een bruikbare invoer wordt gevonden.

**Hoe ontwerp je een controlesysteem dat verschillende schrijfwijzen kan verwerken en pas stopt wanneer aan alle voorwaarden is voldaan?**

## Demo

[DEMO LATER TOEVOEGEN]

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Bad Nut Check** op te lossen.

Breid je controlesysteem uit zodat het invoer robuuster kan controleren.

Werk je oplossing eerst uit als een **flowchart**.

Zet daarna dezelfde oplossing om in **pseudocode**. Schrijf je pseudocode als genummerde comments in je `.py`-bestand en bouw daarna de Python-code bij deze stappen.

### Specificatie

Je programma moet:

- de gebruiker om een noot vragen;
- `amandel`, `hazelnoot` en `walnoot` accepteren als geldige invoer;
- hoofdletters en kleine letters op dezelfde manier behandelen;
- overbodige spaties voor en na de invoer kunnen verwerken;
- andere invoer afwijzen;
- feedback geven wanneer de invoer niet voldoet;
- bijhouden hoeveel pogingen de gebruiker nodig heeft en dit aantal na geldige invoer tonen;
- opnieuw om invoer vragen na een afwijzing;
- stoppen zodra een geldige noot wordt ingevoerd.

Je bepaalt zelf welke **string methods** nodig zijn om de invoer te onderzoeken of te bewerken.

Gebruik niet automatisch dezelfde bewerkingen voor iedere invoer. Bedenk per controle welke informatie je nodig hebt en welke bewerking daarbij past.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke controles moet je uitvoeren?"

    Begin nog niet met programmeren.

    Bepaal eerst welke voorwaarden samen bepalen of invoer geaccepteerd kan worden.

    Kijk daarna welke controles altijd nodig zijn en welke alleen in bepaalde situaties nodig zijn.

??? hint "2 — Hoe maak je verschillende schrijfwijzen vergelijkbaar?"

    Dezelfde informatie kan op verschillende manieren worden ingevoerd.

    Denk na over hoofdletters en kleine letters en overbodige spaties.

    Bepaal welke bewerkingen nodig zijn voordat je de invoer betrouwbaar kunt vergelijken.

??? hint "3 — Hoe maak je het volledige proces zichtbaar?"

    Maak of verbeter je **flowchart**.

    Laat zien:

    - waar invoer wordt ontvangen;
    - welke bewerkingen op de invoer plaatsvinden;
    - welke controles worden uitgevoerd;
    - hoe meerdere voorwaarden samen bepalen of de invoer geldig is;
    - wat er gebeurt bij afgekeurde invoer;
    - hoe een nieuwe poging ontstaat;
    - wanneer het systeem stopt.

??? hint "4 — Hoe zet je je flowchart om in pseudocode?"

    Beschrijf dezelfde oplossing nu in gewone taal.

    Maak zichtbaar:

    - welke bewerkingen op de invoer plaatsvinden;
    - welke controles worden uitgevoerd;
    - wat er gebeurt wanneer invoer niet voldoet;
    - welke stappen daarna opnieuw worden uitgevoerd;
    - wanneer het controleproces stopt.

    Schrijf deze stappen als genummerde comments in je `.py`-bestand.

    Beschrijf **wat** het systeem moet doen. Schrijf hier nog geen Python-syntax.

??? hint "5 — Hoe vertaal je het proces naar Python?"

    Gebruik je pseudocode als ontwerp.

    Kijk naar iedere bewerking en iedere controle in je ontwerp.

    Bepaal daarna welke string methods en conditions je nodig hebt om het ontworpen gedrag in Python uit te voeren.

??? hint "6 — Hoe weet je dat je oplossing robuust is?"

    Denk niet alleen aan een invoer die precies volgens jouw verwachting wordt geschreven.

    Bedenk verschillende manieren waarop een gebruiker dezelfde informatie kan invoeren.

    Test vervolgens of jouw systeem deze invoer op dezelfde manier behandelt wanneer dat volgens jouw ontwerp hoort.

### Testen

Een programma is pas betrouwbaar als je controleert of **verschillende schrijfwijzen en verschillende ongeldige situaties correct worden afgehandeld**.

Voer minimaal de volgende tests uit:

| Test | Invoerreeks | Verwachte uitkomst | Verwachte pogingen | Werkelijke uitkomst | Werkelijke pogingen |
| ---- | ----------- | ------------------ | ------------------- | ------------------- | ------------------- |
| 1 | `amandel` | | | | |
| 2 | `HAZELNOOT` | | | | |
| 3 | `  walnoot  ` | | | | |
| 4 | `pinda` → `AMANDEL` | | | | |
| 5 | `cashew` → `pinda` → `  WALNOOT  ` | | | | |

Bepaal **vooraf** wat je bij iedere test verwacht.

Controleer met deze tests:

- of `amandel`, `hazelnoot` en `walnoot` als geldige invoer worden geaccepteerd;
- of hoofdletters en kleine letters op dezelfde manier worden behandeld;
- of overbodige spaties voor en na geldige invoer correct worden verwerkt;
- of andere invoer wordt afgewezen;
- of het programma feedback geeft bij iedere afgewezen invoer;
- of het programma na iedere afwijzing opnieuw om invoer vraagt;
- of meerdere ongeldige pogingen achter elkaar kunnen worden afgehandeld;
- of het getoonde aantal pogingen overeenkomt met het werkelijke aantal invoerpogingen;
- of het programma blijft doorgaan zolang de invoer ongeldig is;
- of het programma stopt zodra geldige invoer wordt gegeven.

Leg bij iedere test de **verwachte uitkomst**, het **verwachte aantal pogingen**, de **werkelijke uitkomst** en het **werkelijke aantal pogingen** vast.

**Kun je met deze testgevallen aantonen dat je controlesysteem verschillende schrijfwijzen correct behandelt, iedere ongeldige invoer blijft afwijzen en pas stopt wanneer geldige invoer is gegeven?**

Als de werkelijke uitkomst niet overeenkomt met je verwachting, onderzoek dan waar het verschil ontstaat en pas je programma waar nodig aan.

## Reflectie op de oplossing

Beschrijf na het testen:

1. **Welke controle bleek het lastigst om goed te laten werken, en waarom?**

2. **Welke string methods heb je gekozen en waarom pasten deze bij jouw controles?**

3. **Hoe heb je getest of verschillende schrijfwijzen van dezelfde invoer op de juiste manier werden behandeld?**

4. **Wat heb je aan je oplossing veranderd nadat je het gedrag van het programma had onderzocht?**

5. **Hoe weet je dat je validatieproces niet te vroeg stopt en ook niet onnodig doorgaat?**

## Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je flowchart laat de bewerkingen, controles en herhaling duidelijk zien;
- je pseudocode staat als genummerde comments in je `.py`-bestand;
- je kunt uitleggen hoe je flowchart via pseudocode is vertaald naar Python;
- je hebt verschillende schrijfwijzen van invoer getest;
- je hebt meerdere ongeldige situaties getest;
- je hebt getest met meerdere ongeldige pogingen achter elkaar;
- je hebt getest met geldige invoer na meerdere pogingen;
- je verwachte en werkelijke testresultaten en aantallen pogingen zijn vastgelegd;
- je kunt uitleggen waarom je gekozen string methods passen bij je controles;
- je hebt je antwoorden op de reflectievragen uitgewerkt;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna je portfolio bij.
