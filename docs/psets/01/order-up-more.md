---
title: Order Up! — meer vertrouwd
template: pset.html
---

# Order Up!

--8<-- "includes/badges.html:more-comfortable"
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

Een restaurant wil een digitale bestelzuil gebruiken voor tafels met meerdere personen.

Aan een tafel zitten vier personen. Iedere persoon moet zelfstandig dezelfde vaste bestelroute kunnen doorlopen.

De bestelzuil moet steeds duidelijk maken wie aan de beurt is en iedere persoon stap voor stap door het bestelproces leiden.

**Hoe ontwerp en programmeer je een bestelzuil waarmee vier personen achter elkaar zelfstandig dezelfde bestelroute kunnen doorlopen?**


## Demo

[DEMO LATER TOEVOEGEN]


## Understanding

--8<-- "understanding/_content/sequential-programs.md"


## Opdracht

Nu ga je deze kennis gebruiken om het probleem van **Order Up!** op te lossen.

Ontwerp en programmeer een digitale bestelzuil voor een tafel van vier personen.


### Specificatie

Je programma moet:

- duidelijk maken wanneer de bestelroute begint;
- vier personen achter elkaar dezelfde vaste bestelroute laten doorlopen;
- steeds duidelijk maken welke persoon aan de beurt is;
- iedere persoon stap voor stap duidelijk maken welke informatie moet worden ingevoerd;
- met `input()` wachten op een reactie voordat het programma verdergaat;
- na iedere invoer logisch doorgaan naar de volgende stap;
- duidelijk maken wanneer de bestelroute van een persoon is afgerond;
- daarna doorgaan met de volgende persoon;
- aan het einde duidelijk maken dat de volledige tafel klaar is met bestellen.

De volledige interactie verloopt in een **vaste en logische volgorde**.

Gebruik in Python `print()` en `input()`.


### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.


??? hint "1 — Eén persoon eerst"

    Kijk nog niet naar alle vier de personen tegelijk.

    Ontwerp eerst één volledige bestelroute.

    Welke stappen doorloopt één persoon vanaf het begin tot het einde?

    Controleer of iedere stap logisch volgt op de vorige.


??? hint "2 — Van één persoon naar vier"

    Bekijk nu wat er moet gebeuren nadat de eerste persoon klaar is.

    Welke delen van de interactie komen terug voor persoon 2, 3 en 4?

    Zorg dat het systeem steeds duidelijk maakt wie aan de beurt is en wanneer iemand klaar is.


??? hint "3 — Controleer de volledige volgorde"

    Loop de volledige interactie van begin tot eind door.

    Controleer:

    - begint iedere persoon op het juiste moment;
    - is steeds duidelijk wie aan de beurt is;
    - krijgt iedere persoon dezelfde bestelroute;
    - gaat het programma pas naar de volgende persoon als de vorige klaar is;
    - eindigt het programma pas nadat alle vier personen klaar zijn?


??? hint "4 — Van ontwerp naar Python"

    Bekijk je ontworpen gebruikersflow stap voor stap.

    Met `print()` kan het systeem informatie tonen:

    ```python
    print("Persoon 1")
    ```

    Met `input()` kan het programma wachten op een reactie:

    ```python
    input("Maak een keuze: ")
    ```

    Vertaal nu je eigen ontwerp in dezelfde volgorde naar Python.


### Testen

Je bestelzuil werkt pas goed als alle vier personen de volledige bestelroute in de juiste volgorde kunnen doorlopen.

Laat daarom vier gebruikersrollen door het programma lopen. Dit kunnen vier verschillende personen zijn, of één tester die achter elkaar vier verschillende bestellingen invoert.

Bepaal voor iedere test **vooraf** welke volgorde je verwacht.

| Test | Invoer / antwoorden | Verwachte route | Werkelijke route |
| ---- | ------------------- | --------------- | ---------------- |
| 1    |                     |                 |                  |
| 2    |                     |                 |                  |
| 3    |                     |                 |                  |

Controleer daarbij:

- komt persoon 1 als eerste;
- doorloopt iedere persoon de volledige bestelroute;
- komt daarna steeds de juiste volgende persoon;
- stopt de interactie pas nadat persoon 4 klaar is.

Bepaal vooraf welke stappen je verwacht. Voer daarna de test uit en vergelijk wat werkelijk gebeurt met je verwachting.

**Kunnen vier personen de bestelroute achter elkaar zonder uitleg doorlopen en leidt iedere stap logisch naar de volgende?**


### Inleveren

Controleer voordat je de Problem Set afrondt:

- je programma voldoet aan de **specificatie**;
- vier personen doorlopen achter elkaar dezelfde vaste bestelroute;
- steeds is duidelijk wie aan de beurt is;
- de interactie verloopt in een **vaste en logische volgorde**;
- je gebruikt `print()` en `input()` om met de gebruikers te communiceren;
- je hebt de volledige route met verschillende antwoorden getest;
- je kunt uitleggen hoe je ontworpen volgorde is vertaald naar Python;
- je hebt tijdens het werken regelmatig gecommit;
- je laatste versie staat in Git.

Werk daarna **Portfolio 1** bij.