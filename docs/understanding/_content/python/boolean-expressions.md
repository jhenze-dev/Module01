### Boolean expressions

Een **Boolean expression** is een expression die als resultaat één van
twee **Boolean values** heeft:

```python
True
False
```

Een Boolean expression kun je bijvoorbeeld maken door twee waarden met
elkaar te vergelijken:

```python
temperature = 18

print(temperature > 20)
```

De uitvoer is:

```text
False
```

De expression:

```python
temperature > 20
```

wordt door Python geëvalueerd. Omdat `18` niet groter is dan `20`, is
het resultaat `False`.

Wanneer we de waarde veranderen:

```python
temperature = 24

print(temperature > 20)
```

is de uitvoer:

```text
True
```

Een Boolean expression beschrijft dus iets waarvan Python kan bepalen of
het `True` of `False` is.
