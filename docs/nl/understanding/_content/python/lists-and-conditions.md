### Lists and conditions

Met `in` en `not in` kun je controleren of een waarde in een list voorkomt.

```python
products = ["bread", "milk", "cheese"]
```

De expression:

```python
"milk" in products
```

wordt geëvalueerd tot `True` of `False`.

Omdat dit een **Boolean expression** is, kun je deze ook gebruiken als condition bij `if`:

```python
if "milk" in products:
    print("Product found")
```

De code in de `if` branch wordt alleen uitgevoerd wanneer `"milk"` in de list `products` voorkomt.

Je kunt ook een waarde uit een variable gebruiken:

```python
search = input("Product: ")

if search in products:
    print("Product found")
else:
    print("Product not found")
```

Het programma gebruikt hier gegevens uit de list om te bepalen welke branch wordt uitgevoerd.

Met `not in` kun je juist controleren of een waarde niet voorkomt:

```python
if search not in products:
    print("Product not found")
```

Een list kan zo niet alleen worden gebruikt om meerdere gegevens te bewaren. De opgeslagen gegevens kunnen ook worden gebruikt in de conditions waarmee een programma beslissingen neemt.
