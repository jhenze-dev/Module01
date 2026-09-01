---
title: Monk's Perfect Order
template: pset.html
week: 6
level: more

understanding:
  - python.changing-list-items
  - algorithms-efficiency.repeated-processing-with-n-basics
---

# Monk's Perfect Order

--8<-- "includes/badges.html:more-comfortable"
--8<-- "includes/badges.html:python-for"
--8<-- "includes/badges.html:visual-trace-table"
--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:ae-repeated-processing-with-n"
--8<-- "includes/badges.html:process-expressing"
--8<-- "includes/badges.html:process-reflecting-solution"

## Waar werk je aan?

In deze Problem Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren hoe opeenvolgende stappen logisch samenhangen in een algoritme**.
- Ik kan **een algoritmische oplossing ontwerpen en programmeren**.
- Ik kan **het gedrag van een sorteeralgoritme onderzoeken met een Trace Table en meetgegevens**.
- Ik kan **mogelijke oplossingsstrategieën analyseren en mijn gekozen strategie verantwoorden met resultaten uit mijn eigen tests**.

## Probleem

Monk wil zijn volledige verzameling tijdschriften op nummer ordenen.

Hij gebruikt daarvoor een vaste werkwijze: hij bekijkt steeds **twee tijdschriften die naast elkaar staan**. Staan ze in de verkeerde volgorde, dan verwisselt hij ze. Daarna gaat hij verder met het volgende paar.

Monk wil niet alleen dat de verzameling uiteindelijk goed staat. Hij wil ook kunnen zien hoeveel werk zijn strategie nodig heeft en herkennen wanneer een volgende ronde niets meer verandert.

Een computer moet de verzameling daarom systematisch ordenen, het verloop van het algoritme zichtbaar maken en stoppen zodra een volledige ronde geen wisseling meer oplevert.

**Hoe ontwerp je een algoritme dat een verzameling systematisch ordent en hoe onderzoek je de gekozen strategie?**

## Understanding

{{ understanding_reference(understanding) }}

Wil je ook onderzoeken hoe je het aantal bewerkingen algemeen kunt beschrijven wanneer een verwerking meerdere keren wordt herhaald?

Lees dan [Aantal bewerkingen bij herhaling](../../understanding/algorithms-efficiency/repeated-processing-with-n/operation-count-with-repetition.md).

## Opdracht

Maak de uitgebreide versie van **Monk's Perfect Order**.

Gebruik eerst:

```python
magazines = [9, 4, 7, 1, 6, 0, 8, 3, 5, 2]
```

Ontwerp vóór het programmeren je algoritme in **pseudocode**.

Beschrijf daarin niet alleen hoe aangrenzende items worden vergeleken en eventueel verwisseld, maar ook:

- hoe een nieuwe ronde begint;
- welke informatie je tijdens de verwerking bijhoudt;
- hoe je vaststelt dat een volledige ronde niets meer heeft veranderd;
- wanneer het algoritme daarom kan stoppen.

Laat je pseudocode daarna als comments in je `.py`-bestand staan.

Maak daarnaast een **Trace Table** waarin je voor minimaal één test zichtbaar maakt hoe de list per vergelijking en per ronde verandert.

Ontwerp nadat je programma werkt ook **een tweede mogelijke strategie** voor hetzelfde ordeningsprobleem. Werk deze tweede strategie alleen uit in pseudocode; je hoeft haar niet te programmeren. Gebruik de vergelijking met je werkende strategie later in je reflectie.

### Specificatie

Je programma gebruikt als eerste verzameling:

```python
magazines = [9, 4, 7, 1, 6, 0, 8, 3, 5, 2]
```

Je programma moet:

- de verzameling ordenen van het kleinste naar het grootste nummer;
- de ordening uitvoeren in volledige rondes van links naar rechts;
- binnen iedere ronde met een `for`-loop, `range()` en indexes steeds twee naast elkaar staande items vergelijken;
- twee items alleen verwisselen wanneer het linker nummer groter is dan het rechter nummer;
- bij het verwisselen de waarden in de bestaande list aanpassen;
- bijhouden hoeveel **vergelijkingen** in totaal zijn uitgevoerd;
- bijhouden hoeveel **wisselingen** in totaal zijn uitgevoerd;
- bijhouden hoeveel volledige **rondes** zijn uitgevoerd;
- na iedere ronde de huidige toestand van de list tonen;
- doorgaan met een nieuwe ronde zolang in de vorige ronde minstens één wisseling plaatsvond;
- stoppen nadat een volledige ronde geen enkele wisseling heeft opgeleverd;
- aan het einde de geordende list en het totale aantal rondes, vergelijkingen en wisselingen tonen;
- dezelfde code blijven gebruiken wanneer alleen de inhoud van `magazines` wordt vervangen door een andere niet-lege list met getallen.

Iedere volledige ronde vergelijkt alle aangrenzende paren van links naar rechts.

Je mag voor het ordenen **geen** `.sort()` of `sorted()` gebruiken.

### Hints

Kom je niet verder? Open dan eerst alleen de hint die je nodig hebt.

??? hint "1 — Wat moet je per ronde weten?"

    Aan het einde van een ronde moet je kunnen bepalen of er nog een volgende ronde nodig is.

    Welke informatie uit de huidige ronde heb je daarvoor nodig?

??? hint "2 — Welke tellers veranderen wanneer?"

    Een vergelijking vindt plaats iedere keer dat je twee aangrenzende waarden controleert.

    Een wisseling vindt alleen plaats wanneer die twee waarden daadwerkelijk van plaats veranderen.

    Welke tellers horen dus bij welke momenten in je algoritme?

??? hint "3 — Wanneer is de verzameling klaar?"

    Bekijk een volledige ronde waarin geen enkele wisseling nodig is.

    Wat zegt dat over alle aangrenzende paren in de list?

??? hint "4 — Welke herhaling hoort waar?"

    Binnen één ronde weet je welke aangrenzende paren systematisch moeten worden verwerkt.

    Tussen de rondes hangt doorgaan af van wat er in de vorige ronde is gebeurd.

    Welke eerder geleerde vorm van herhaling past bij zo'n voorwaarde?

### Testen

Gebruik minimaal de volgende situaties.

Voorspel **vooraf** de uiteindelijke geordende list en de aantallen rondes, vergelijkingen en wisselingen.

| Test | List | Verwachte geordende list | Verwachte rondes | Verwachte vergelijkingen | Verwachte wisselingen | Werkelijke uitkomst |
| ---- | ---- | ------------------------ | ----------------- | ----------------------- | --------------------- | ------------------- |
| 1 | `[9, 4, 7, 1, 6, 0, 8, 3, 5, 2]` | | | | | |
| 2 | `[0, 1, 2, 3, 4]` | | | | | |
| 3 | `[4, 3, 2, 1, 0]` | | | | | |
| 4 | `[3, 1, 3, 2]` | | | | | |

Maak voor test 1 of test 3 een volledige Trace Table. Noteer daarin minimaal:

- ronde;
- linker en rechter index;
- beide waarden vóór de vergelijking;
- wel of geen wisseling;
- toestand van de list na de vergelijking.

Controleer met je tests:

- of iedere volledige ronde alle aangrenzende paren verwerkt;
- of het aantal vergelijkingen overeenkomt met het aantal daadwerkelijk uitgevoerde vergelijkingen;
- of het aantal wisselingen alleen toeneemt wanneer twee items werkelijk worden verwisseld;
- of een al geordende list na de eerste volledige ronde stopt;
- of een omgekeerd geordende list meerdere rondes nodig heeft;
- of het algoritme pas stopt nadat een volledige ronde geen wisseling meer oplevert;
- of de uiteindelijke list in alle gevallen correct is geordend.

**Welke verschillen zie je tussen de tests in het aantal rondes, vergelijkingen en wisselingen, terwijl het algoritme zelf hetzelfde blijft?**

Als een werkelijke uitkomst niet overeenkomt met je voorspelling, gebruik je Trace Table om te bepalen in welke ronde of vergelijking het verschil ontstaat en pas je pseudocode en programma waar nodig aan.

## Reflectie op de oplossing

Gebruik je **pseudocode**, **Trace Table** en **testresultaten** als bewijs.

Beantwoord:

1. Welke van je tests vergde volgens jouw meetgegevens het minste werk en welke het meeste? Onderbouw dit met je aantallen rondes, vergelijkingen en wisselingen.
2. Waarom weet je dat de verzameling correct geordend is wanneer een volledige ronde geen wisseling meer oplevert?
3. Vergelijk je geprogrammeerde strategie met de tweede strategie die je in pseudocode hebt ontworpen. Welke oplossingsrichting vind je op basis van je eigen analyse het meest kansrijk en waarom?

## Inleveren

Controleer voordat je inlevert of:

- je programma voldoet aan de specificatie;
- je pseudocode als comments in je `.py`-bestand staat;
- je tweede strategie in pseudocode is uitgewerkt;
- je Trace Table is toegevoegd;
- alle vier de tests zijn uitgevoerd;
- je verwachte en werkelijke testresultaten zijn vastgelegd;
- je aantallen rondes, vergelijkingen en wisselingen correct worden getoond;
- je reflectie met concrete resultaten uit je eigen werk is uitgewerkt;
- je laatste wijzigingen zijn gecommit en gepusht naar Git.
