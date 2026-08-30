### List information

Je kunt informatie over een list opvragen zonder de items zelf te veranderen.

#### Aantal items

Met `len()` kun je bepalen hoeveel items een list bevat.

```python
names = ["Alex", "Sam", "Robin"]

print(len(names))
```

De uitvoer is:

```text
3
```

`len(names)` wordt geëvalueerd tot het aantal items in de list.

Ook bij een lege list werkt `len()`:

```python
names = []

print(len(names))
```

De uitvoer is:

```text
0
```

#### Controleren of een item voorkomt

Met de membership operator `in` kun je controleren of een waarde in een list voorkomt.

```python
names = ["Alex", "Sam", "Robin"]

print("Sam" in names)
```

De uitvoer is:

```text
True
```

De expression:

```python
"Sam" in names
```

is een **Boolean expression**. Python controleert of `"Sam"` als item in `names` voorkomt en levert `True` of `False` op.

Met `not in` kun je controleren of een waarde juist niet in een list voorkomt:

```python
print("Jamie" not in names)
```

De uitvoer is:

```text
True
```

`len()` geeft dus informatie over **hoeveel items** een list bevat. Met `in` en `not in` kun je bepalen **of een bepaalde waarde** als item in een list voorkomt.
