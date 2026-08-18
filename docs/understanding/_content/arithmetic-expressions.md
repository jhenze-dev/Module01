### Arithmetic operators

Met numerieke waarden kan Python berekeningen uitvoeren.

Daarvoor gebruikt Python **arithmetic operators**.

| Operator | Betekenis |
| -------- | --------- |
| `+` | optellen |
| `-` | aftrekken |
| `*` | vermenigvuldigen |
| `/` | delen |

Bijvoorbeeld:

```python
print(8 + 2)
print(8 - 2)
print(8 * 2)
print(8 / 2)
```

De uitvoer is:

```text
10
6
16
4.0
```

Bij delen met `/` is het resultaat in Python een `float`. Daarom wordt `8 / 2` weergegeven als `4.0`.


### Expressions

Een **expression** is code die Python evalueert om een waarde te krijgen.

Bijvoorbeeld:

```python
8 * 2
```

Python evalueert deze expression. Het resultaat is de waarde `16`.

Een expression kan ook variables bevatten:

```python
price = 4
amount = 3

print(price * amount)
```

Python gebruikt de waarden waarnaar `price` en `amount` verwijzen en evalueert:

```python
price * amount
```

De uitvoer is:

```text
12
```


### Het resultaat bewaren

Het resultaat van een expression kan zelf weer in een variable worden bewaard.

Bijvoorbeeld:

```python
price = 4
amount = 3

total = price * amount
```

Python evalueert eerst:

```python
price * amount
```

Het resultaat is `12`.

Met:

```python
total = price * amount
```

wordt deze berekende waarde vervolgens toegekend aan de variable `total`.

Je kunt die waarde daarna opnieuw gebruiken:

```python
print(total)
```

De uitvoer is:

```text
12
```


### Berekende waarden opnieuw gebruiken

Een berekende waarde kan ook onderdeel worden van een volgende berekening.

Bijvoorbeeld:

```python
length = 5
width = 3

area = length * width
double_area = area * 2
```

Python voert deze instructions op volgorde uit.

Eerst worden de waarden van `length` en `width` bewaard.

Daarna evalueert Python:

```python
length * width
```

Het resultaat wordt als `area` bewaard.

Pas daarna wordt `area` gebruikt in:

```python
area * 2
```

Het resultaat daarvan wordt als `double_area` bewaard.

Zo kunnen verschillende berekeningen op elkaar voortbouwen: het resultaat van de ene berekening kan informatie opleveren die in een volgende berekening opnieuw wordt gebruikt.