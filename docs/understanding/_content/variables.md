Tot nu toe heb je Python instructies laten uitvoeren en informatie op het scherm laten zien.

Soms moet een programma informatie **bewaren**, zodat deze later opnieuw kan worden gebruikt. Daarvoor gebruikt Python **variables**.


### Variables

Een **variable** is een naam die verwijst naar een waarde.

Bijvoorbeeld:

```python
age = 16
```

Hier wordt de waarde `16` toegekend aan de variable `age`.

Dit noemen we een **assignment**.

Na deze assignment kan Python de naam `age` gebruiken om naar de waarde `16` te verwijzen:

```python
age = 16

print(age)
```

De uitvoer is:

```text
16
```

De waarde hoeft daardoor niet iedere keer opnieuw in de code te worden geschreven.


### Variable names

Een variable name maakt duidelijk welke informatie een waarde voorstelt.

Bijvoorbeeld:

```python
age = 16
temperature = 18
price = 4
```

Variable names mogen letters, cijfers en `_` bevatten, maar mogen niet met een cijfer beginnen en geen spaties bevatten.

Dit zijn geldige variable names:

```python
temperature
room_temperature
temperature2
```

Dit zijn geen geldige variable names:

```text
2temperature
room temperature
```

Python maakt ook onderscheid tussen hoofdletters en kleine letters. `temperature` en `Temperature` zijn dus verschillende variable names.

Gebruik namen die duidelijk maken **welke informatie** een variable voorstelt.


### `int` en `float`

Waarden hebben in Python een bepaald **type**.

Voor getallen gebruiken we onder andere `int` en `float`.

Een geheel getal heeft het type `int`:

```python
age = 16
```

Een getal met een decimaal deel heeft het type `float`:

```python
temperature = 18.5
```

De waarden `16` en `18.5` zijn dus allebei getallen, maar hebben in Python een verschillend type.


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