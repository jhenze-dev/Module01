### `range()`

`range()` beschrijft een reeks gehele getallen die een `for`-loop achtereenvolgens kan gebruiken.

Bijvoorbeeld:

```python
for i in range(4):
    print(i)
```

De uitvoer is:

```text
0
1
2
3
```

`range(4)` begint dus bij `0` en stopt **vóór** `4`.

### Een begin- en eindwaarde

Je kunt ook aangeven waar de reeks moet beginnen:

```python
for i in range(2, 5):
    print(i)
```

De uitvoer is:

```text
2
3
4
```

De algemene vormen zijn:

```python
range(stop)
```

en:

```python
range(start, stop)
```

De `stop`-waarde zelf hoort niet meer bij de reeks.

### `range()` en indexes

Indexes van een list beginnen bij `0`.

Bij:

```python
cities = ["Oslo", "Lima", "Tokyo"]
```

zijn de geldige indexes:

```text
0 1 2
```

De lengte van de list is:

```python
len(cities)
```

en heeft de waarde `3`.

Daarom geeft:

```python
range(len(cities))
```

precies de geldige indexes:

```text
0 1 2
```

Dit kan worden gebruikt in een `for`-loop:

```python
cities = ["Oslo", "Lima", "Tokyo"]

for i in range(len(cities)):
    print(i, cities[i])
```

De uitvoer is:

```text
0 Oslo
1 Lima
2 Tokyo
```

### Niet altijd bij `0` beginnen

Soms hoeft een verwerking niet bij de eerste positie te beginnen.

Met:

```python
range(1, len(cities))
```

worden bij dezelfde list de indexes:

```text
1 2
```

doorlopen.

Welke beginwaarde passend is, hangt af van het probleem dat je oplost.

### `range()` geeft posities, niet de items zelf

Vergelijk:

```python
for city in cities:
    print(city)
```

met:

```python
for i in range(len(cities)):
    print(i, cities[i])
```

In het eerste voorbeeld bevat de loop variable direct een item uit de list.

In het tweede voorbeeld bevat de loop variable een index. Met die index kun je vervolgens het bijbehorende item opvragen.

Gebruik `range()` dus wanneer een reeks getallen of de posities in een verzameling onderdeel zijn van de verwerking.
