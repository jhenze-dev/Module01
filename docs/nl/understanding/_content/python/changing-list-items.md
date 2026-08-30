### Een bestaand list-item veranderen

Een item dat al in een list staat, kan worden vervangen door een nieuwe waarde.

Daarvoor gebruik je de index van dat item.

Bijvoorbeeld:

```python
numbers = [4, 7, 2]

numbers[1] = 9

print(numbers)
```

De uitvoer is:

```text
[4, 9, 2]
```

De waarde op index `1` was eerst `7`.

Door:

```python
numbers[1] = 9
```

wordt die bestaande waarde vervangen door `9`.

De lengte van de list verandert daarbij niet.

### Lezen en veranderen gebruiken dezelfde index

Met:

```python
numbers[1]
```

lees je de waarde op index `1`.

Met:

```python
numbers[1] = 9
```

verander je de waarde op index `1`.

De index bepaalt dus op welke positie in de list Python werkt.

### Een waarde bewaren voordat je haar vervangt

Soms wil je twee waarden in een list van plaats laten wisselen.

Daarbij is de volgorde van de assignments belangrijk.

Bekijk deze list:

```python
colors = ["red", "blue", "green"]
```

Stel dat de waarden op index `0` en index `2` moeten wisselen.

Als je meteen schrijft:

```python
colors[0] = colors[2]
```

dan wordt `"red"` vervangen door `"green"`.

De oorspronkelijke waarde `"red"` is dan niet meer op index `0` beschikbaar.

Daarom kun je die waarde eerst tijdelijk bewaren:

```python
temporary = colors[0]

colors[0] = colors[2]
colors[2] = temporary
```

Daarna bevat de list:

```text
["green", "blue", "red"]
```

De variable `temporary` bewaart dus een waarde terwijl de twee posities worden aangepast.

### Twee posities verwisselen

Het algemene patroon is:

```python
temporary = collection[first_index]
collection[first_index] = collection[second_index]
collection[second_index] = temporary
```

Na deze drie assignments:

- staat de oorspronkelijke waarde van `second_index` op `first_index`;
- staat de oorspronkelijke waarde van `first_index` op `second_index`;
- blijven de andere items in de list hetzelfde.

Welke twee indexes je gebruikt, hangt af van het probleem dat je oplost.
