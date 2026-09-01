### Beschrijven met n

Het aantal bewerkingen beschrijven in relatie tot de hoeveelheid gegevens n.
### Beschrijven met n

Bij **Bewerkingen tellen** heb je onderzocht hoe vaak een gekozen bewerking tijdens één concrete uitvoering van een algoritme plaatsvindt.

Wanneer vier items één voor één worden verwerkt en ieder item precies één keer dezelfde bewerking veroorzaakt, wordt die bewerking vier keer uitgevoerd.

Maar een algoritme moet meestal niet alleen voor vier items werken. Een verzameling kan ook twee, tien, honderd of nog veel meer items bevatten.

Om het aantal bewerkingen onafhankelijk van één concrete verzameling te beschrijven, gebruiken we de letter **n**.

#### Wat betekent n?

`n` staat voor de **hoeveelheid gegevens die door het algoritme wordt verwerkt**.

Bij een lijst kan `n` bijvoorbeeld het aantal items in de lijst zijn.

| Aantal items | n |
| ---: | ---: |
| 2 | 2 |
| 4 | 4 |
| 10 | 10 |
| 100 | 100 |

De letter `n` is dus geen vast getal. De waarde van `n` hangt af van de hoeveelheid gegevens waarop het algoritme wordt uitgevoerd.

#### Van een concreet aantal naar n

Stel dat ieder item precies één keer wordt verwerkt.

Bij vier items:

$$
1 + 1 + 1 + 1 = 4
$$

Bij tien items wordt dezelfde bewerking tien keer uitgevoerd.

In plaats van voor iedere mogelijke hoeveelheid gegevens een nieuwe berekening te maken, kunnen we het aantal bewerkingen algemeen beschrijven:

$$
\text{aantal verwerkingen} = n
$$

Deze beschrijving geldt niet alleen voor één concrete verzameling. De waarde verandert mee wanneer de hoeveelheid gegevens verandert.

#### Een beschrijving met n controleren

Een beschrijving met `n` moet overeenkomen met concrete uitvoeringen van het algoritme.

Als:

$$
\text{aantal verwerkingen} = n
$$

dan hoort daarbij bijvoorbeeld:

| n | Aantal verwerkingen |
| ---: | ---: |
| 1 | 1 |
| 3 | 3 |
| 6 | 6 |
| 10 | 10 |

Door concrete aantallen te vergelijken met de beschrijving in `n`, kun je controleren of de wiskundige beschrijving bij het algoritme past.

#### Van uitvoering naar algemeen patroon

Een Trace Table kan zichtbaar maken **hoeveel bewerkingen tijdens één concrete uitvoering plaatsvinden**.

Een beschrijving met `n` gaat een stap verder. Daarmee beschrijf je **hoe het aantal bewerkingen samenhangt met de hoeveelheid gegevens**.

Zo kun je van:

$$
4 \text{ items} \rightarrow 4 \text{ verwerkingen}
$$

overgaan naar:

$$
n \text{ items} \rightarrow n \text{ verwerkingen}
$$

Daarmee beschrijf je een algemeen patroon in plaats van alleen één uitvoering.