
Tot nu toe werden de instructies in je programma's vooral na elkaar
uitgevoerd. Dit noemen we **sequential execution**.

Soms moet een programma op basis van een bepaalde situatie bepalen welke
instructies wel of niet worden uitgevoerd. Hiervoor gebruikt Python
**conditionals**.

### Boolean expressions

Een **Boolean expression** is een expressie die als resultaat één van
twee **Boolean values** heeft:

``` python
True
False
```

Een Boolean expression kun je bijvoorbeeld maken door twee waarden met
elkaar te vergelijken:

``` python
temperature = 18

print(temperature > 20)
```

De uitvoer is:

``` text
False
```

De expression:

``` python
temperature > 20
```

wordt door Python geëvalueerd. Omdat `18` niet groter is dan `20`, is
het resultaat `False`.

Wanneer we de waarde veranderen:

``` python
temperature = 24

print(temperature > 20)
```

is de uitvoer:

``` text
True
```

Een Boolean expression beschrijft dus iets waarvan Python kan bepalen of
het `True` of `False` is.

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

``` python
x = 8

print(x > 5)
print(x == 8)
print(x < 3)
```

De uitvoer is:

``` text
True
True
False
```

Let goed op het verschil tussen `=` en `==`.

Met:

``` python
x = 8
```

ken je de waarde `8` toe aan de variable `x`. Dit is een **assignment**.

Met:

``` python
x == 8
```

vergelijk je twee waarden. Dit is een **comparison** en levert `True` of
`False` op.

### Conditions

Een Boolean expression kan als **condition** worden gebruikt.

Een condition bepaalt of bepaalde code wel of niet wordt uitgevoerd.

Met een `if statement` kan Python een condition controleren:

``` python
temperature = 18

if temperature < 20:
    print("Neem een jas mee")
```

Python evalueert eerst de condition:

``` python
temperature < 20
```

Is de condition `True`, dan wordt de ingesprongen code uitgevoerd.

Is de condition `False`, dan wordt deze code overgeslagen.

### Indentation

Bij een `if statement` horen een dubbele punt `:` en **indentation**:

``` python
if condition:
    action
```

De indentation geeft aan welke instructies bij het `if statement` horen.

Bijvoorbeeld:

``` python
temperature = 18

if temperature < 20:
    print("Neem een jas mee")
    print("Het is buiten fris.")

print("Fijne dag!")
```

De eerste twee `print()` statements horen bij de `if` en worden alleen
uitgevoerd wanneer de condition `True` is.

De laatste `print()` staat niet meer binnen de `if` en wordt daarom
altijd uitgevoerd.

### Alternative execution

Soms zijn er twee mogelijke **branches**.

Wanneer de condition `True` is, moet de ene branch worden uitgevoerd.
Wanneer de condition `False` is, moet een andere branch worden
uitgevoerd.

Daarvoor gebruiken we `if` en `else`:

``` python
if condition:
    action_a
else:
    action_b
```

Python controleert eerst de condition bij `if`.

-   Is de condition `True`, dan wordt de eerste branch uitgevoerd.
-   Is de condition `False`, dan wordt de `else` branch uitgevoerd.

Van de twee branches wordt dus precies één uitgevoerd.

### Chained conditionals

Een probleem kan meer dan twee mogelijke situaties bevatten. Met `elif`
kun je na een `if` een volgende condition laten controleren.

De algemene structuur is:

``` python
if condition_1:
    action_1
elif condition_2:
    action_2
else:
    action_3
```

Python controleert de conditions van boven naar beneden.

1.  Eerst wordt `condition_1` geëvalueerd.
2.  Als deze `True` is, wordt `action_1` uitgevoerd.
3.  Als deze `False` is, wordt `condition_2` geëvalueerd.
4.  Als deze `True` is, wordt `action_2` uitgevoerd.
5.  Als geen van de eerdere conditions `True` is, wordt de `else` branch
    uitgevoerd.

Zodra Python een branch heeft gevonden waarvan de condition `True` is,
wordt die branch uitgevoerd en worden de volgende branches van dezelfde
conditional niet meer gecontroleerd.

Een `else` heeft zelf geen condition. Deze branch wordt uitgevoerd
wanneer geen van de voorafgaande conditions `True` is.

### Van condition naar branch

Bij het werken met conditionals zijn twee begrippen belangrijk:

-   een **condition** die Python kan evalueren als `True` of `False`;
-   een **branch** met instructies die afhankelijk van die condition
    wordt uitgevoerd.

Met `if`, `elif` en `else` kun je deze conditions en branches in Python
uitdrukken.

Welke conditions nodig zijn, hoeveel branches er zijn en welke actions
daarbij horen, hangt af van het probleem dat je probeert op te lossen.
