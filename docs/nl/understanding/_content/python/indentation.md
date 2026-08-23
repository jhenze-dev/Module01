### Indentation

Bij een `if statement` horen een dubbele punt `:` en **indentation**:

```python
if condition:
    action
```

De indentation geeft aan welke instructies bij het `if statement` horen.

Bijvoorbeeld:

```python
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
