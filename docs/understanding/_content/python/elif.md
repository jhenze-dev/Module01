### `elif`

Een probleem kan meer dan twee mogelijke situaties bevatten.

Met `elif` kun je na een `if` een volgende condition laten controleren.

Bijvoorbeeld:

```python
if condition_1:
    action_1
elif condition_2:
    action_2
else:
    action_3
```

Python controleert de conditions van boven naar beneden.

1. Eerst wordt `condition_1` geëvalueerd.
2. Als deze `True` is, wordt `action_1` uitgevoerd.
3. Als deze `False` is, wordt `condition_2` geëvalueerd.
4. Als deze `True` is, wordt `action_2` uitgevoerd.
5. Als geen van de eerdere conditions `True` is, wordt de `else` uitgevoerd.

Zodra Python een condition vindt die `True` is, wordt de bijbehorende
code uitgevoerd. De volgende conditions van dezelfde conditional worden
dan niet meer gecontroleerd.

Je kunt meerdere `elif` statements gebruiken wanneer er meer situaties
onderscheiden moeten worden.
