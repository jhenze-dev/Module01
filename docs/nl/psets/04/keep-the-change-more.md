---
title: Keep the Change
template: pset.html
week: 4
level: more

understanding:
  - python.while-loops
---

# Keep the Change

--8<-- "includes/badges.html:more-comfortable"
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

De pizzabezorger moet het juiste wisselgeld teruggeven. Een computersysteem moet daarbij niet alleen het eindresultaat bepalen, maar het volledige wisselproces kunnen uitvoeren en zichtbaar maken.

Het systeem moet steeds opnieuw bepalen welke munt kan worden gebruikt en hoeveel wisselgeld daarna nog over is.

De eigenaar van Little Nero's wil bovendien kunnen zien hoe het systeem tot het uiteindelijke wisselgeld komt.

**Hoe ontwerp je een systeem dat wisselgeld stap voor stap teruggeeft en het verloop van het proces zichtbaar maakt?**

## Demo

[DEMO LATER TOEVOEGEN]

## Understanding

{{ understanding_reference(understanding) }}

## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Keep the Change** op te lossen.

Ontwerp en programmeer een systeem dat het volledige wisselproces uitvoert en zichtbaar maakt.

Werk je oplossing eerst uit als een **loop-flowchart**.

Zet daarna dezelfde oplossing om in **pseudocode**. Schrijf je pseudocode als genummerde comments in je `.py`-bestand en bouw daarna de Python-code bij deze stappen.

### Specificatie

Je programma moet:

- een bedrag aan wisselgeld vragen;
- het wisselgeld teruggeven met Nederlandse munten van **5 cent, 10 cent, 20 cent, 50 cent, 1 euro en 2 euro**;
- steeds opnieuw bepalen welke munt gebruikt kan worden;
- na iedere munt het resterende bedrag aanpassen;
- doorgaan zolang er nog wisselgeld over is;
- stoppen wanneer het resterende bedrag `0` is;
- iedere gebruikte munt tonen op het moment dat deze wordt teruggegeven;
- na iedere gebruikte munt tonen hoeveel wisselgeld nog over is;
- aan het einde tonen hoeveel munten van iedere soort zijn gebruikt;
- aan het einde tonen hoeveel munten er in totaal zijn gebruikt.

Gebruik voor de herhaling een `while`-loop.

Het programma moet het wisselgeld teruggeven met **zo groot mogelijke munten**.

Gebruik als invoer een **positief geheel aantal centen dat een veelvoud van 5 is**. Dat is in deze Problem Set een geldig bedrag.

Andere bedragen hoef je in deze Problem Set niet af te handelen.

Je oplossing moet voor ieder geldig bedrag zelfstandig het volledige wisselproces uitvoeren.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Welke informatie moet je tijdens het proces bijhouden?"

    Kijk naar het volledige wisselproces.

    Aan het begin weet je hoeveel wisselgeld moet worden teruggegeven. Na iedere munt verandert deze informatie.

    Bepaal welke informatie je tijdens het proces nodig hebt om de volgende stap te kunnen uitvoeren.

??? hint "2 — Hoe weet je wanneer je klaar bent?"

    Het proces bestaat uit meerdere herhalingen.

    Zoek naar een waarde die tijdens het proces verandert.

    **Welke waarde vertelt je dat er nog werk te doen is?**

    En welke waarde vertelt je dat het proces klaar is?

??? hint "3 — Hoe kun je het proces zichtbaar maken?"

    Maak een **loop-flowchart** waarin je niet alleen het begin en einde laat zien.

    Laat ook zien:

    - welke toestand wordt bekeken;
    - welke handeling wordt uitgevoerd;
    - hoe de toestand verandert;
    - wanneer het proces opnieuw begint.

    Controleer of je flowchart iedere herhaling van het proces kan beschrijven.

??? hint "4 — Hoe zet je je flowchart om in pseudocode?"

    Beschrijf dezelfde oplossing nu in gewone taal.

    Maak zichtbaar:

    - welke stappen worden herhaald;
    - wanneer de herhaling doorgaat;
    - wat tijdens iedere herhaling verandert;
    - wanneer het proces stopt.

    Schrijf deze stappen als genummerde comments in je `.py`-bestand.

    Beschrijf **wat** er moet gebeuren. Schrijf hier nog geen Python-syntax.

??? hint "5 — Hoe vertaal je het proces naar Python?"

    Gebruik je pseudocode als ontwerp.

    Een `while`-loop herhaalt code zolang een voorwaarde waar is:

    ```python
    while voorwaarde:
        actie
    ```

    Kijk naar je eigen ontwerp:

    - welke waarde bepaalt of de loop doorgaat?
    - waar verandert die waarde?
    - welke handelingen horen bij één herhaling?

    Programmeer vanuit je eigen ontwerp verder.

### Testen

Test je programma met minimaal vijf verschillende geldige bedragen.

Zorg dat je testgevallen samen de volgende situaties bevatten:

- een bedrag waarvoor één munt voldoende is;
- een bedrag waarvoor verschillende muntwaarden nodig zijn;
- een bedrag waarbij dezelfde munt meerdere keren wordt gebruikt;
- een bedrag waarbij het wisselproces meerdere stappen bevat;
- een bedrag waarbij meerdere verschillende muntsoorten worden gebruikt.

Kies zelf passende bedragen voor deze vijf situaties.

Bepaal **vooraf** wat je bij iedere test verwacht.

| Test | Wisselgeld | Verwachte uitkomst | Werkelijke uitkomst |
| ---- | ---------- | ------------------ | ------------------- |
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

Leg bij iedere test in zowel de **verwachte uitkomst** als de **werkelijke uitkomst** vast:

- welke munten worden gebruikt en in welke volgorde;
- hoe het resterende bedrag na iedere munt verandert;
- hoeveel munten van iedere soort worden gebruikt;
- hoeveel munten in totaal worden gebruikt;
- dat het resterende bedrag uiteindelijk `0` wordt en het programma daarna stopt.

Controleer daarna of:

- steeds de grootst mogelijke munt wordt gebruikt;
- de gebruikte munten samen precies het gevraagde bedrag vormen;
- het getoonde resterende bedrag na iedere stap klopt;
- de aantallen per muntsoort overeenkomen met de werkelijk gebruikte munten;
- het totale aantal munten klopt;
- het proces alleen doorgaat zolang er wisselgeld over is;
- het programma stopt wanneer het resterende bedrag `0` is.

**Kun je met je vijf testgevallen aantonen dat je programma voor verschillende geldige bedragen het volledige wisselproces correct uitvoert en zichtbaar maakt?**

Als een werkelijke uitkomst niet overeenkomt met je verwachting, onderzoek dan waar in het wisselproces het verschil ontstaat en pas je programma waar nodig aan.

### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- je gebruikt een `while`-loop voor de herhaling;
- je maakt het verloop van het wisselproces zichtbaar;
- het resterende wisselgeld verandert na iedere stap;
- je programma stopt wanneer het wisselgeld volledig is teruggegeven;
- je hebt verschillende bedragen en procesverlopen getest;
- je verwachte en werkelijke testresultaten zijn vastgelegd;
- je pseudocode staat als genummerde comments in je `.py`-bestand;
- je kunt uitleggen hoe je flowchart via pseudocode is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna je portfolio bij.
