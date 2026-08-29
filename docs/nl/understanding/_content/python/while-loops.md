### `while`

Soms moet een programma een handeling meerdere keren uitvoeren.

Een `if` controleert een condition en voert de bijbehorende code hoogstens één keer uit. Met `while` kan Python dezelfde code blijven uitvoeren zolang een condition `True` is.

Bijvoorbeeld:

```python
count = 1

while count <= 3:
    print(count)
    count = count + 1
```

Python begint met:

```python
count = 1
```

Daarna wordt de condition:

```python
count <= 3
```

geëvalueerd.

Omdat de condition `True` is, voert Python de ingesprongen code uit:

```python
print(count)
count = count + 1
```

Daardoor verandert de waarde van `count`.

Python gaat daarna terug naar de `while` en evalueert de condition opnieuw.

De uitvoer is:

```text
1
2
3
```

Na iedere uitvoering verandert de waarde van `count`:

- eerst is `count` gelijk aan `1`;
- daarna wordt `count` gelijk aan `2`;
- daarna wordt `count` gelijk aan `3`;
- daarna wordt `count` gelijk aan `4`.

Wanneer Python vervolgens:

```python
count <= 3
```

evalueert, is de uitkomst `False`.

De code binnen de `while` wordt dan niet opnieuw uitgevoerd.


### Iteration

Een enkele uitvoering van de code binnen een `while` noemen we een **iteration**.

Bij iedere iteration:

1. evalueert Python de condition;
2. als de condition `True` is, wordt de ingesprongen code uitgevoerd;
3. daarna wordt de condition opnieuw geëvalueerd;
4. dit gaat door totdat de condition `False` is.

De condition bepaalt dus of de volgende iteration plaatsvindt.


### Toestand veranderen

Bij een `while` kan de situatie tijdens het uitvoeren van het programma veranderen.

In het voorbeeld verandert de waarde van `count` iedere keer:

```python
count = count + 1
```

De volgende evaluatie van de condition gebruikt daardoor een nieuwe waarde.

De variable die bepaalt of de `while` verdergaat, moet daarom op een bepaald moment kunnen veranderen.

Zonder zo'n verandering kan een condition `True` blijven en blijft de `while` doorgaan.


### Algemene structuur

De algemene vorm van een `while` is:

```python
while condition:
    action
```

Python evalueert steeds dezelfde `condition`.

Zolang deze `True` is, wordt `action` uitgevoerd.

Wanneer de condition `False` wordt, gaat Python verder met de code na de `while`.


### `if` en `while`

Een `while` gebruikt, net als een `if`, een condition.

Bijvoorbeeld:

```python
if condition:
    action
```

en:

```python
while condition:
    action
```

Het verschil zit in wat Python daarna doet.

Bij een `if` wordt de condition gecontroleerd om te bepalen of `action` wordt uitgevoerd.

Bij een `while` wordt de condition steeds opnieuw gecontroleerd om te bepalen of de volgende iteration wordt uitgevoerd.

Dezelfde code kan daardoor meerdere keren worden uitgevoerd.
