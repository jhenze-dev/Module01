### Invoer omzetten naar een getal

Met `input()` kan een programma informatie van een gebruiker ontvangen.

Bijvoorbeeld:

```python
age = input("Leeftijd: ")
```

De informatie die `input()` ontvangt, kan niet direct als getal worden gebruikt.

Met `int()` kun je invoer omzetten naar een integer:

```python
age = int(input("Leeftijd: "))
```

Met `float()` kun je invoer omzetten naar een floating-point getal:

```python
temperature = float(input("Temperatuur: "))
```

Gebruik `int()` wanneer de waarde een geheel getal moet zijn.

Gebruik `float()` wanneer de waarde ook een decimaal deel kan bevatten.
