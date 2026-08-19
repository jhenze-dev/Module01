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
