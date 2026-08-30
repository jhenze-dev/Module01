### `for`

Een `for`-loop gebruikt Python om dezelfde code uit te voeren voor ieder item uit een verzameling.

Bijvoorbeeld:

```python
colors = ["red", "blue", "green"]

for color in colors:
    print(color)
```

De uitvoer is:

```text
red
blue
green
```

Python verwerkt de list van links naar rechts.

Bij de eerste iteration krijgt `color` de waarde `"red"`, daarna `"blue"` en daarna `"green"`.

### De loop variable

In:

```python
for color in colors:
    print(color)
```

is `color` de **loop variable**.

Tijdens iedere iteration verwijst deze variable naar het item dat op dat moment wordt verwerkt.

De algemene vorm is:

```python
for item in collection:
    action
```

Hierbij gebeurt steeds hetzelfde:

1. Python neemt het volgende item uit `collection`;
2. dat item wordt tijdelijk opgeslagen in `item`;
3. de ingesprongen code wordt uitgevoerd;
4. Python gaat verder met het volgende item;
5. wanneer er geen items meer zijn, gaat Python verder met de code na de `for`.

### Iteration

Eén uitvoering van de ingesprongen code noemen we een **iteration**.

Bij:

```python
numbers = [4, 7, 2]

for number in numbers:
    print(number)
```

zijn er drie iterations:

| Iteration | `number` |
| ---: | ---: |
| 1 | 4 |
| 2 | 7 |
| 3 | 2 |

Een list met vijf items levert op deze manier vijf iterations op.

Een lege list levert geen iterations op.

### Indentation

De code die bij de `for` hoort, staat ingesprongen:

```python
for number in numbers:
    print(number)

print("klaar")
```

`print(number)` wordt tijdens iedere iteration uitgevoerd.

`print("klaar")` staat niet meer binnen de loop en wordt pas uitgevoerd nadat alle items zijn verwerkt.

### `for` en `while`

Zowel `for` als `while` kunnen code herhalen, maar ze gebruiken een ander uitgangspunt.

Bij een `while` bepaalt een condition of de volgende iteration plaatsvindt:

```python
while condition:
    action
```

Bij een `for` bepaalt de verzameling welke items achtereenvolgens worden verwerkt:

```python
for item in collection:
    action
```

Een `for` is daarom geschikt wanneer je een verzameling systematisch item voor item wilt verwerken.
