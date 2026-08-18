Tot nu toe heb je gezien dat een computer instructies precies uitvoert zoals
ze zijn geschreven.

Wanneer meerdere instructies na elkaar worden uitgevoerd, noemen we dit
**sequential execution**.

### Output

Met `print()` kan een programma informatie tonen.

```python
print("Hello")
```

De uitvoer is:

```text
Hello
```

De tekst die moet worden weergegeven staat tussen aanhalingstekens.

Je kunt meerdere `print()`-instructies gebruiken:

```python
print("Good morning")
print("Have a nice day")
```

De uitvoer is:

```text
Good morning
Have a nice day
```

### Input

Een programma kan ook wachten op informatie van een gebruiker.

Daarvoor gebruikt Python `input()`:

```python
input("What is your name? ")
```

Python toont de tekst en wacht vervolgens totdat de gebruiker iets invoert
en op Enter drukt.

Pas daarna gaat het programma verder.

Bijvoorbeeld:

```python
print("Ready")
input("Press Enter to continue ")
print("Go")
```

Eerst wordt `Ready` getoond.

Daarna wacht het programma bij `input()` op de gebruiker. Pas wanneer de
gebruiker op Enter drukt, wordt `Go` getoond.

### Statements

Een volledige instructie die Python kan uitvoeren noemen we een **statement**.

Bijvoorbeeld:

```python
print("Hello")
```

Dit is één statement. Het statement gebruikt de functie `print()` om de tekst `"Hello"` te tonen.

Ook:

```python
input("Press Enter ")
```

is één statement. Het statement gebruikt de functie `input()` om op invoer van de gebruiker te wachten.

`print()` en `input()` zijn dus functies. De volledige regels waarin deze functies worden gebruikt, zijn **statements**.

Een programma kan uit meerdere statements bestaan. Python voert deze statements uit in de volgorde waarin ze in het programma staan.

### Sequential execution

Python voert statements standaard uit in de volgorde waarin ze in het
programma staan: van boven naar beneden.

Bijvoorbeeld:

```python
print("First")
print("Second")
print("Third")
```

De uitvoer is:

```text
First
Second
Third
```

Deze uitvoering van statements in een vaste volgorde noemen we
**sequential execution**.

Ook wanneer `print()` en `input()` worden gecombineerd, blijft deze
volgorde bestaan:

```python
print("First")
input("Press Enter to continue ")
print("Second")
```

Python:

1. voert het eerste statement uit;
2. wacht bij het tweede statement op invoer;
3. gaat daarna verder met het derde statement.

De volgorde van statements bepaalt dus de volgorde waarin het programma
wordt uitgevoerd.

Welke statements nodig zijn en in welke volgorde ze moeten staan, hangt af
van het probleem dat je probeert op te lossen.

### Comments

Met een **comment** kun je informatie in je code schrijven die Python niet
uitvoert.

Een comment begint met `#`:

```python
# Show a message
print("Hello")
```

Python negeert de tekst achter `#`.

Comments kunnen helpen om zichtbaar te maken wat een deel van een programma
doet of waarom een bepaalde keuze is gemaakt.

Bijvoorbeeld:

```python
# Start
print("Ready")

# Wait for input
input("Press Enter ")

# Continue
print("Go")
```

De comments maken de opbouw van het programma zichtbaar, maar veranderen
de uitvoering van het programma niet.