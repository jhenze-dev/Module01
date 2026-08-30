### Trace Table

Een proces bestaat vaak uit meerdere stappen.

Tijdens die stappen kunnen gegevens of waarden veranderen. Wanneer een proces langer wordt, is het moeilijk om alleen in je hoofd bij te houden **wat er na iedere stap is veranderd**.

Daarvoor kun je een **Trace Table** gebruiken.

Een Trace Table laat stap voor stap zien:

* welke stap wordt uitgevoerd;
* welke gegevens op dat moment worden gebruikt;
* wat er tijdens die stap verandert;
* wat de toestand na die stap is.

Een Trace Table beschrijft daarmee niet alleen het eindresultaat, maar maakt **het verloop van een proces** zichtbaar.

### Toestand

De **toestand** is de informatie die op een bepaald moment belangrijk is om het proces te kunnen volgen.

Stel dat een score begint op `10`.

Daarna gebeuren achtereenvolgens drie dingen:

* er komen `3` punten bij;
* er gaan `2` punten af;
* er komen `5` punten bij.

Een Trace Table kan dat proces zo zichtbaar maken:

| Stap | Actie | Score |
| ---: | --- | ---: |
| 0 | beginstand | 10 |
| 1 | +3 | 13 |
| 2 | -2 | 11 |
| 3 | +5 | 16 |

Iedere rij laat de toestand op een nieuw moment zien.

Daardoor kun je niet alleen zien dat de eindscore `16` is, maar ook **hoe die waarde stap voor stap is ontstaan**.

### De beginstand

Een Trace Table begint vaak met **stap 0**.

Daarin noteer je de toestand voordat het proces begint.

Dat is belangrijk, omdat je daardoor iedere verandering kunt vergelijken met de toestand ervoor.

In het voorbeeld is:

```text
stap 0 → score = 10
```

Daarna kun je per stap volgen hoe die waarde verandert.

### Kolommen kiezen

Een Trace Table heeft geen vaste set kolommen.

Je kiest de kolommen op basis van **wat je tijdens het proces moet kunnen volgen**.

Bij het voorbeeld met de score waren drie kolommen voldoende:

* de stap;
* de uitgevoerde actie;
* de huidige score.

Bij een ander proces kan het bijvoorbeeld nodig zijn om ook bij te houden:

* welk item wordt bekeken;
* welke keuze wordt gemaakt;
* de waarde van één of meer variabelen;
* de inhoud van een verzameling;
* de uitvoer die ontstaat.

Neem alleen informatie op die helpt om het proces te begrijpen.

### Iedere stap vastleggen

Wanneer je een proces zelf uitvoert, kun je de Trace Table gebruiken als een **logboek van wat er werkelijk gebeurt**.

Voeg na iedere betekenisvolle stap een nieuwe rij toe.

Zo ontstaat tijdens het werken een volledig spoor van het proces.

Bijvoorbeeld:

```text
beginstand
    ↓
stap uitvoeren
    ↓
nieuwe toestand noteren
    ↓
volgende stap uitvoeren
    ↓
nieuwe toestand noteren
```

Als er later iets onverwachts gebeurt, kun je terugkijken **bij welke stap de toestand veranderde**.

### Een proces volgen

Een Trace Table kan ook worden gebruikt wanneer het proces al is beschreven.

Je voert de stappen dan niet eerst fysiek uit, maar volgt ze één voor één en voorspelt wat iedere stap met de toestand doet.

Stel dat een proces als pseudocode is beschreven:

```text
1. Maak een totaal met waarde 0

2. Voor ieder getal in de lijst:
   2.1 Tel het huidige getal op bij het totaal

3. Toon het totaal
```

Stap 2 beschrijft een **herhaling**.

De woorden `voor ieder getal in de lijst` betekenen dat stap 2.1 opnieuw wordt uitgevoerd voor ieder getal dat aan de beurt komt.

Voor de lijst:

```text
4, 7, 2
```

betekent dat:

```text
getal 4 → voer stap 2.1 uit
getal 7 → voer stap 2.1 uit
getal 2 → voer stap 2.1 uit
```

Het proces keert dus tijdens de herhaling steeds terug naar stap 2 om het volgende getal te verwerken.

Daarom komen stap 2 en stap 2.1 meerdere keren terug in de Trace Table:

| Pseudocode-stap | Huidig getal | Totaal | Output |
| --- | ---: | ---: | ---: |
| 1 | — | 0 | |
| 2 | 4 | 0 | |
| 2.1 | 4 | 4 | |
| 2 | 7 | 4 | |
| 2.1 | 7 | 11 | |
| 2 | 2 | 11 | |
| 2.1 | 2 | 13 | |
| 3 | — | 13 | 13 |

Hier laat iedere rij zien **waar het proces zich bevindt en wat de toestand op dat moment is**.

Je kunt daardoor ook zien dat dezelfde pseudocode-stap meerdere keren kan worden uitgevoerd wanneer die stap onderdeel is van een herhaling.

### Van uitvoeren naar voorspellen

Dezelfde Trace Table kan dus op twee manieren worden gebruikt:

```text
proces uitvoeren
        ↓
vastleggen wat er werkelijk gebeurt
```

of:

```text
proces lezen
        ↓
stap voor stap voorspellen wat er gebeurt
```

Later kun je dezelfde werkwijze gebruiken om Python-code te volgen.

Je voorspelt dan eerst hoe waarden tijdens de uitvoering veranderen en vergelijkt die voorspelling daarna met wat het programma werkelijk doet.

### Controleren met een Trace Table

Een Trace Table helpt je controleren of een proces doet wat je verwacht.

Controleer daarbij bijvoorbeeld:

* is iedere relevante stap opgenomen?
* verandert de toestand zoals verwacht?
* wordt geen stap overgeslagen?
* wordt een stap niet onbedoeld dubbel uitgevoerd?
* klopt de uiteindelijke toestand met wat je verwachtte?

Wanneer iets niet klopt, kun je in de tabel terugzoeken **bij welke stap het verschil ontstaat**.

### Van Trace Table naar code

Een Trace Table schrijft niet voor hoe een programma moet worden geprogrammeerd.

De tabel maakt eerst zichtbaar **wat er tijdens de uitvoering gebeurt**.

Wanneer je later code schrijft of onderzoekt, kunnen kolommen uit de Trace Table bijvoorbeeld overeenkomen met:

* variabelen;
* het huidige item uit een verzameling;
* tussentijdse resultaten;
* output.

Daarmee vormt een Trace Table een brug tussen **een proces stap voor stap begrijpen** en **begrijpen wat code tijdens de uitvoering doet**.
