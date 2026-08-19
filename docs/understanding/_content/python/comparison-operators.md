### Comparison operators

Om waarden met elkaar te vergelijken gebruikt Python **comparison
operators**.

| Operator | Betekenis |
| -------- | --------- |
| `==` | gelijk aan |
| `!=` | niet gelijk aan |
| `<` | kleiner dan |
| `>` | groter dan |
| `<=` | kleiner dan of gelijk aan |
| `>=` | groter dan of gelijk aan |

Bijvoorbeeld:

```python
x = 8

print(x > 5)
print(x == 8)
print(x < 3)
```

De uitvoer is:

```text
True
True
False
```

Let goed op het verschil tussen `=` en `==`.

Met:

```python
x = 8
```

ken je de waarde `8` toe aan de variable `x`. Dit is een **assignment**.

Met:

```python
x == 8
```

vergelijk je twee waarden. Dit is een **comparison** en levert `True` of
`False` op.
