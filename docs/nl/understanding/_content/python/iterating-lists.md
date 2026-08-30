### Een list systematisch doorlopen

Een list bevat meerdere items.

Met een `for`-loop kun je ieder item uit die list één voor één verwerken.

Bijvoorbeeld:

```python
scores = [12, 18, 15, 9]

for score in scores:
    print(score)
```

Python verwerkt achtereenvolgens:

```text
12
18
15
9
```

Dit noemen we het **doorlopen** of **itereren over** een list.

### Dezelfde bewerking voor ieder item

Een belangrijk patroon bij gegevensverwerking is dat ieder item volgens dezelfde werkwijze wordt behandeld.

Bijvoorbeeld:

```python
temperatures = [17, 21, 19]

for temperature in temperatures:
    print(temperature * 2)
```

Dezelfde bewerking wordt uitgevoerd voor ieder item uit de list.

De code binnen de `for` hoeft dus niet voor ieder item opnieuw te worden geschreven.

### Informatie tijdens het doorlopen bijhouden

Tijdens een `for`-loop kunnen variables veranderen.

Daardoor kan een programma informatie onthouden over de items die al zijn verwerkt.

Bijvoorbeeld:

```python
numbers = [3, 5, 2]
total = 0

for number in numbers:
    total = total + number

print(total)
```

De waarde van `total` verandert tijdens de iterations:

| Verwerkt item | `total` daarna |
| ---: | ---: |
| 3 | 3 |
| 5 | 8 |
| 2 | 10 |

Na de loop bevat `total` informatie over de volledige verzameling.

Dit soort variables beschrijven de **toestand** van het programma tijdens de verwerking.

### Alleen de waarde nodig

Wanneer je alleen het huidige item nodig hebt, kun je rechtstreeks over de list itereren:

```python
names = ["Ava", "Noah", "Mila"]

for name in names:
    print(name)
```

De loop variable bevat dan steeds de huidige waarde.

### Ook de positie nodig

Soms is niet alleen de waarde belangrijk, maar ook **waar** die waarde in de list staat.

Een list gebruikt indexes:

```text
index:   0      1      2
waarde: "Ava" "Noah" "Mila"
```

Wanneer je tijdens het itereren ook deze posities nodig hebt, kun je de geldige indexes systematisch doorlopen.

Daarvoor worden `range()` en `len()` gecombineerd:

```python
names = ["Ava", "Noah", "Mila"]

for i in range(len(names)):
    print(i, names[i])
```

De uitvoer is:

```text
0 Ava
1 Noah
2 Mila
```

Hier is `i` tijdens iedere iteration de huidige index.

Met `names[i]` lees je het item dat op die positie staat.

### Waarde of index?

Gebruik:

```python
for item in collection:
```

wanneer je vooral de **waarden** wilt verwerken.

Gebruik:

```python
for i in range(len(collection)):
```

wanneer je tijdens de verwerking ook de **positie** van ieder item nodig hebt.

In beide gevallen kan een volledige list systematisch worden doorlopen.
