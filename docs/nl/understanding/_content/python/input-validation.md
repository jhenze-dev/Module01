### Input validation

Een programma krijgt niet altijd bruikbare invoer van een gebruiker.

Een gebruiker kan bijvoorbeeld:

- een onverwachte waarde invoeren;
- hoofdletters gebruiken waar kleine letters worden verwacht;
- extra spaties typen;
- een waarde invoeren die niet aan de voorwaarden voldoet.

Een programma kan daarom controleren of invoer bruikbaar is voordat het verdergaat.


### Invoer controleren

Bij input validation wordt invoer beoordeeld aan de hand van één of meer voorwaarden.

Bijvoorbeeld:

```python
answer = input("Type yes or no: ")

if answer == "yes":
    print("Accepted")
else:
    print("Rejected")
```

Het programma vergelijkt de invoer met een verwachte waarde.

De invoer kan echter op verschillende manieren worden geschreven.

Deze invoer:

```text
yes
```

is bijvoorbeeld niet hetzelfde als:

```text
Yes
```

Ook extra spaties kunnen ervoor zorgen dat een vergelijking niet het verwachte resultaat geeft.


### Invoer bewerken

Een string kan worden bewerkt voordat deze wordt gecontroleerd.

Python heeft verschillende **string methods** waarmee je een string kunt onderzoeken of bewerken.

Bijvoorbeeld:

```python
answer = input("Type yes or no: ")
answer = answer.strip()
```

`strip()` verwijdert overbodige spaties aan het begin en einde van een string.

Ook kan de schrijfwijze van tekst worden aangepast:

```python
answer = answer.lower()
```

Daarna bevat `answer` alleen nog kleine letters.

Het is belangrijk om onderscheid te maken tussen:

**invoer bewerken**

en

**invoer controleren**.

Een string method kan de invoer veranderen of informatie over de invoer geven. Een condition bepaalt vervolgens wat het programma met die informatie doet.


### Verschillende manieren van controleren

Niet iedere controle vraagt om dezelfde bewerking.

Python heeft bijvoorbeeld string methods waarmee je kunt onderzoeken:

- of een string met bepaalde tekens begint;
- of een string met bepaalde tekens eindigt;
- hoe vaak een bepaalde waarde voorkomt;
- of een bepaalde waarde in een string voorkomt;
- of een string alleen letters bevat;
- of een string alleen cijfers bevat.

Welke controle nodig is, hangt af van het probleem en van wat als geldige invoer wordt beschouwd.


### Meerdere voorwaarden

Een invoer kan aan meerdere voorwaarden tegelijk moeten voldoen.

Bijvoorbeeld:

```python
if condition1 and condition2:
    print("Accepted")
```

Hier wordt de invoer alleen geaccepteerd wanneer beide voorwaarden `True` zijn.

Bij meerdere voorwaarden moet daarom duidelijk zijn:

- welke eigenschappen worden gecontroleerd;
- welke voorwaarden nodig zijn;
- en wanneer de volledige invoer als geldig wordt beschouwd.


### Opnieuw vragen

Input validation wordt vaak gecombineerd met een `while`-loop.

Het programma kan dan invoer blijven vragen zolang de invoer niet geldig is.

De algemene structuur is:

```python
while not valid:
    input = ...
    valid = ...
```

De invoer wordt iedere keer opnieuw gecontroleerd.

Zodra de invoer geldig is, wordt de condition van de `while` `False` en stopt het herhalende proces.

Hierdoor hoeft het programma niet vooraf te weten hoeveel pogingen de gebruiker nodig heeft.


### Pogingen bijhouden

Een programma kan ook bijhouden hoe vaak de gebruiker invoer heeft gegeven.

Daarvoor kan een teller worden gebruikt:

```python
attempts = 0

while not valid:
    attempts = attempts + 1
    ...
```

De teller verandert iedere keer dat een nieuwe poging wordt gedaan.

Na afloop bevat `attempts` het aantal uitgevoerde pogingen.


### Een validatieproces

Input validation kan worden gezien als een proces:

```text
invoer ontvangen
      ↓
invoer controleren
      ↓
voldoet aan de voorwaarden?
    ↙          ↘
  nee           ja
   ↓             ↓
opnieuw       accepteren
vragen
```

Bij iedere nieuwe poging begint het proces opnieuw.

De voorwaarden bepalen uiteindelijk wanneer het proces mag stoppen.
