### Branches

Bij een conditional kunnen verschillende mogelijke uitvoerpaden ontstaan.

Zo'n mogelijk uitvoerpad noemen we een **branch**.

Bijvoorbeeld:

```python
if condition:
    action_a
else:
    action_b
```

Hier zijn twee branches:

- wanneer de condition `True` is, wordt de eerste branch uitgevoerd;
- wanneer de condition `False` is, wordt de tweede branch uitgevoerd.

Van deze twee branches wordt dus precies één uitgevoerd.

Met `elif` kunnen meer branches worden toegevoegd:

```python
if condition_1:
    action_1
elif condition_2:
    action_2
else:
    action_3
```

Python controleert de conditions van boven naar beneden. Zodra een
condition `True` is, wordt de bijbehorende branch uitgevoerd.

Bij het werken met conditionals zijn dus twee begrippen belangrijk:

- een **condition** die Python kan evalueren als `True` of `False`;
- een **branch** met instructies die afhankelijk van een condition
  wordt uitgevoerd.

Met `if`, `elif` en `else` kun je deze conditions en branches in Python
uitdrukken.

Welke conditions nodig zijn, hoeveel branches er zijn en welke actions
daarbij horen, hangt af van het probleem dat je probeert op te lossen.
