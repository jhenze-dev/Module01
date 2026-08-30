### List indexes

De items in een list hebben ieder een positie.

Python gebruikt daarvoor een **index**.

```python
names = ["Alex", "Sam", "Robin"]
```

Python begint bij index `0`.

| Index | Item |
| ---: | --- |
| `0` | `"Alex"` |
| `1` | `"Sam"` |
| `2` | `"Robin"` |

Je kunt een item uit een list opvragen door de index tussen vierkante haken achter de naam van de list te schrijven:

```python
print(names[1])
```

De uitvoer is:

```text
Sam
```

Python gebruikt `1` hier als index en haalt het item op dat op die positie in de list staat.

Omdat de eerste index `0` is, geldt voor deze list:

```python
names[0]
names[1]
names[2]
```

voor respectievelijk `"Alex"`, `"Sam"` en `"Robin"`.

De index hoort dus bij de **positie van een item in de list**, niet bij het aantal waarmee mensen normaal beginnen te tellen.
