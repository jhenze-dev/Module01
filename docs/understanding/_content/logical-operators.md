### Logical operators

Soms hangt een beslissing af van meer dan één **condition**.

Met **logical operators** kun je meerdere conditions combineren tot één **Boolean expression**.

#### `and`

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

#### `or`

Soms kunnen verschillende situaties tot dezelfde branch leiden. Met de logical operator `or` kun je aangeven dat één van meerdere conditions voldoende is:

```python
condition_1 or condition_2
```

De volledige Boolean expression is `True` wanneer **minimaal één van de conditions** `True` is.

Bijvoorbeeld:

```python
day == "saturday" or day == "sunday"
```

Deze Boolean expression is `True` wanneer `day` gelijk is aan `"saturday"` **of** aan `"sunday"`.

Je kunt `or` gebruiken wanneer verschillende conditions tot dezelfde branch mogen leiden.

#### `and` en `or` combineren

`and` en `or` kunnen ook samen in één Boolean expression voorkomen.

Gebruik haakjes om duidelijk te maken welke conditions bij elkaar horen:

```python
(condition_1 and condition_2) or (condition_3 and condition_4)
```

In dit voorbeeld zijn er twee mogelijke situaties:

- `condition_1` en `condition_2` zijn beide `True`;
- `condition_3` en `condition_4` zijn beide `True`.

Als één van deze twee situaties geldt, is de volledige Boolean expression `True`.

Bedenk bij het ontwerpen van een condition daarom steeds:

- moeten meerdere conditions **tegelijk** gelden? Gebruik dan `and`;
- kunnen verschillende situaties tot dezelfde branch leiden? Dan kan `or` worden gebruikt.