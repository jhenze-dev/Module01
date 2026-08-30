### Adding list items

Een list kan tijdens het uitvoeren van een programma worden uitgebreid.

Met de list method `append()` voeg je een nieuw item toe aan het einde van een bestaande list.

```python
names = ["Alex", "Sam"]

names.append("Robin")
```

Na `append()` bevat `names`:

```python
["Alex", "Sam", "Robin"]
```

Het nieuwe item wordt achter de bestaande items geplaatst.

Je kunt ook een waarde uit een variable toevoegen:

```python
names = ["Alex", "Sam"]
new_name = "Robin"

names.append(new_name)
```

Ook nu wordt `"Robin"` als nieuw item aan de list toegevoegd.

`append()` verandert dus de bestaande list. Je hoeft het resultaat niet opnieuw aan de variable toe te kennen.

```python
names.append("Robin")
```

voegt het item toe aan `names`.
