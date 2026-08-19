### `and`

Soms hangt een beslissing af van meer dan één **condition**.

Met **logical operators** kun je meerdere conditions combineren tot één **Boolean expression**.

Met de logical operator `and` kun je aangeven dat meerdere conditions tegelijk moeten gelden:

```python
condition_1 and condition_2
```

De volledige Boolean expression is alleen `True` wanneer **beide conditions** `True` zijn.

Bijvoorbeeld:

```python
temperature > 20 and sun == "yes"
```

Deze Boolean expression is alleen `True` wanneer de temperatuur hoger is dan `20` **en** de waarde van `sun` gelijk is aan `"yes"`.

Je kunt `and` gebruiken wanneer meerdere conditions tegelijk moeten gelden om een bepaalde **branch** uit te voeren.
