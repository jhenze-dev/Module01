### `else`

Soms moet een programma iets anders doen wanneer de condition bij een
`if` niet `True` is.

Daarvoor gebruikt Python `else`:

```python
if condition:
    action_a
else:
    action_b
```

Python controleert eerst de condition bij `if`.

Is de condition `True`, dan wordt `action_a` uitgevoerd.

Is de condition `False`, dan wordt `action_b` uitgevoerd.

Een `else` heeft zelf geen condition. De code bij `else` wordt uitgevoerd
wanneer de condition bij de bijbehorende `if` `False` is.
