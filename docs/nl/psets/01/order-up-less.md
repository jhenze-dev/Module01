---
title: Order Up!
template: pset.html
week: 1
level: less

understanding:
  - python.sequential-execution
---

# Order Up!

--8<-- "includes/badges.html:less-comfortable"
--8<-- "includes/badges.html:python-input-output"
--8<-- "includes/badges.html:visual-flowchart"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"


## Waar werk je aan?

Met deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **een geordende reeks instructies formuleren** om een probleem op te lossen.
- Ik kan **een interactie tussen gebruiker en systeem structureren**.
- Ik kan **een geordende reeks instructies uitdrukken in Python**.


## Probleem

Een restaurant wil klanten zelfstandig een bestelling laten plaatsen met een digitale bestelzuil.

Een klant moet zonder hulp van een medewerker kunnen begrijpen wat het systeem van hem vraagt. De bestelzuil moet daarom duidelijk communiceren en de klant stap voor stap door een vaste bestelroute leiden.

**Hoe ontwerp en programmeer je een bestelzuil waarmee één klant zelfstandig een volledige bestelroute kan doorlopen?**


## Demo

[DEMO LATER TOEVOEGEN]


## Understanding

{{ understanding_reference(understanding) }}


## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Order Up!** op te lossen.

Ontwerp en programmeer een digitale bestelzuil voor één klant.


### Specificatie

Je programma moet:

- de klant duidelijk welkom heten;
- de klant stap voor stap door een volledige bestelroute leiden;
- bij iedere stap duidelijk maken welke informatie de klant moet invoeren;
- met `input()` wachten op een reactie van de klant voordat het programma verdergaat;
- na iedere invoer logisch doorgaan naar de volgende stap;
- aan het einde duidelijk maken dat de bestelling is afgerond.

De volledige interactie verloopt in een **vaste en logische volgorde**.

Gebruik in Python `print()` en `input()`.


### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.


??? hint "1 — Wat moet de klant meemaken?"

    Kijk nog niet naar Python.

    Stel je voor dat jij de klant bent.

    Welke stappen moet je doorlopen vanaf het moment dat je bij de bestelzuil begint totdat je bestelling klaar is?

    Zorg dat iedere stap logisch volgt op de vorige.


??? hint "2 — Controleer de communicatie"

    Bekijk iedere stap van je bestelroute.

    Is voor de klant steeds duidelijk:

    - wat het systeem vertelt;
    - wanneer de klant iets moet invoeren;
    - wat daarna gebeurt?

    Iemand die jouw ontwerp niet kent, moet de route zonder extra uitleg kunnen volgen.


??? hint "3 — Van ontwerp naar Python"

    Bekijk je ontworpen bestelroute stap voor stap.

    Met `print()` kan het systeem informatie tonen:

    ```python
    print("Welkom!")
    ```

    Met `input()` kan het programma wachten op een reactie:

    ```python
    input("Maak een keuze: ")
    ```

    Vertaal nu je eigen bestelroute in dezelfde volgorde naar Python.


### Testen

Je bestelzuil werkt pas goed als een gebruiker de volledige bestelroute zelfstandig kan doorlopen.

Laat daarom iemand anders je programma gebruiken zonder vooraf uit te leggen wat diegene moet doen.

Controleer:

- is steeds duidelijk wat de gebruiker moet doen;
- wacht het programma op de juiste momenten op invoer;
- volgt iedere stap logisch op de vorige;
- komt de gebruiker zonder hulp bij het einde van de bestelroute.

Test je programma met verschillende antwoorden op de vragen.

| Test | Invoer / antwoorden | Verwachte route | Werkelijke route |
| ---- | ------------------- | --------------- | ---------------- |
| 1    |                     |                 |                  |
| 2    |                     |                 |                  |
| 3    |                     |                 |                  |

Bepaal **vooraf** welke route je programma bij iedere test moet doorlopen en wat je verwacht dat het programma doet. Voer daarna de test uit en vergelijk de werkelijke route met je verwachting.

**Kan iemand anders de volledige bestelroute zonder uitleg doorlopen en leidt iedere stap logisch naar de volgende?**


### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- de interactie verloopt in een **vaste en logische volgorde**;
- je gebruikt `print()` en `input()` om met de gebruiker te communiceren;
- een andere gebruiker kan de volledige bestelroute zonder uitleg doorlopen;
- je hebt verschillende antwoorden getest;
- je kunt uitleggen hoe je ontworpen volgorde is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 1** bij.


