<!--
============================================================
UNDERSTANDING — PYTHON CONTENT — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------
Deze template legt het gerealiseerde ontwerp vast van de
inhoud van een Python Understanding.

Dit bestand staat in:

    docs/understanding/_content/python/[BESTAND].md

Het bevat de daadwerkelijke, herbruikbare onderwijsinhoud
over een Python-concept of een logisch samenhangend cluster
van Python-concepten.

Dezelfde content kan worden gebruikt:

1. via een zelfstandige Understanding-pagina:

   understanding/python/[ONDERWERP].md

2. als include binnen bijvoorbeeld een Problem Set:

   --8<-- "understanding/_content/python/[BESTAND].md"

Daarom bevat dit bestand GEEN:

- frontmatter;
- H1-paginatitel;
- template-instelling;
- weeknummer;
- PSET-nummer;
- opdracht-specifieke instructies.


============================================================
1. BELANGRIJKE REGEL VOOR DEZE TEMPLATE
============================================================

Deze template beschrijft en borgt de gerealiseerde
didactische stijl van Python Understanding.

Tijdens het maken van nieuwe content worden GEEN nieuwe
onderwijsinhoudelijke of leerlingzichtbare ontwerpkeuzes
ingevoerd alleen omdat die op dat moment nuttig lijken.

Dat betekent onder andere:

- geen extra Python-concepten toevoegen omdat ze technisch
  bij het onderwerp horen;
- geen toekomstige leerstof naar voren halen;
- geen PSET-specifieke oplossing verwerken;
- geen andere terminologie kiezen;
- geen vaste nieuwe secties introduceren;
- geen kunstmatige afsluiting of samenvatting toevoegen;

zonder dat daarvoor een inhoudelijke aanleiding vanuit het
moduleframework en de leerlijn bestaat.


============================================================
2. ONDERWIJSINHOUDELIJKE HIËRARCHIE
============================================================

Gebruik bij het ontwerpen altijd deze volgorde:

1. MODULEFRAMEWORK
   Bepaalt welke Python-kennis leerlingen nodig hebben en
   waar deze in de leerlijn voorkomt.

2. CONCEPTUELE LEERLIJN
   Bepaalt welke voorkennis op dit moment beschikbaar is en
   waarop de nieuwe kennis kan voortbouwen.

3. PYTHON CONTENT-TEMPLATE
   Bepaalt hoe de conceptuele uitleg didactisch wordt
   opgebouwd.

4. EERDERE UNDERSTANDING-CONTENT
   Is referentie voor stijl, terminologie en niveau, maar
   nooit bron voor nieuwe onderwijsinhoud.

Bij een inhoudelijk conflict is het MODULEFRAMEWORK leidend.


============================================================
3. FUNCTIE VAN PYTHON UNDERSTANDING
============================================================

Python Understanding beantwoordt vooral:

    "Hoe werkt dit Python-concept en wat betekent het?"

De content is bedoeld als:

- centrale conceptuele uitleg;
- herbruikbare kennisbron;
- ondersteuning tijdens Problem Sets;
- zelfstandig naslagwerk.

De content is GEEN:

- Problem Set;
- Thinking Set;
- opdracht;
- stappenplan voor een specifieke oplossing;
- volledige Python-documentatie.


============================================================
4. SOURCE OF TRUTH — MODULEFRAMEWORK
============================================================

Bepaal vóór het schrijven minimaal:

- welk Python-concept centraal staat;
- welke onderdelen daarvan volgens het framework nodig zijn;
- welke begrippen leerlingen moeten kennen;
- welke syntax leerlingen moeten kunnen gebruiken;
- welke voorkennis beschikbaar is;
- welke complexiteit op dit punt in de leerlijn passend is.

Vraag expliciet:

    "Wat moeten leerlingen NU over dit concept begrijpen?"

Niet:

    "Wat valt er allemaal over dit Python-onderwerp te
    vertellen?"

Scopebewaking is essentieel.

Een Understanding behandelt precies wat nodig is voor deze
plaats in de leerlijn.


============================================================
5. ONTWERPANALYSE VÓÓR HET SCHRIJVEN
============================================================

Bepaal eerst:

CONCEPT
- Wat is het centrale nieuwe concept?
- Welke onderliggende begrippen zijn noodzakelijk?
- Welke begrippen zijn al bekend?
- Welke onderdelen horen pas later in de leerlijn?

AANSLUITING
- Op welke eerdere kennis kan worden voortgebouwd?
- Welke bekende situatie kan het nieuwe concept logisch
  introduceren?
- Welke terminologie is al geïntroduceerd?

VOORBEELDEN
- Wat is het kleinste voorbeeld waarmee het concept zichtbaar
  wordt?
- Welke invoer/waarden maken de werking duidelijk?
- Is uitvoer nodig om het gedrag zichtbaar te maken?
- Is het voorbeeld voldoende generiek?

OPBOUW
- Welke conceptuele stap moet eerst komen?
- Welke uitbreiding kan daarna volgen?
- Welke verschillen of relaties moeten expliciet worden
  gemaakt?

Schrijf pas daarna de content.


============================================================
6. GEEN VERPLICHTE VASTE INHOUDELIJKE STRUCTUUR
============================================================

Niet iedere Python Understanding krijgt dezelfde headings.

De structuur volgt uit het CONCEPT.

Een eenvoudige Understanding kan bijvoorbeeld bestaan uit:

### [Concept]

uitleg

voorbeeld

betekenis


Een uitgebreider onderwerp kan meerdere opeenvolgende
concepten bevatten:

### [Concept A]

...

### [Concept B]

...

### [Concept C]

...


Gebruik alleen tussenkoppen die inhoudelijk nodig zijn.

Maak dus NIET automatisch secties zoals:

- Definitie
- Syntax
- Voorbeeld
- Samenvatting
- Oefening

wanneer de conceptuele uitleg daar niet om vraagt.


============================================================
7. CONCEPTUELE OPBOUW
============================================================

Bouw nieuwe kennis stapsgewijs op.

Een veelgebruikte beweging is:

    bestaande kennis / herkenbare situatie
                    ↓
              nieuw concept
                    ↓
         klein generiek voorbeeld
                    ↓
        uitleg van wat er gebeurt
                    ↓
          syntax / algemene vorm
                    ↓
       uitbreiding of nieuw geval
                    ↓
      relatie tussen de begrippen

Dit is een ONTWERPPRINCIPE, geen verplicht format.

Laat de logica van het concept bepalen welke stappen
daadwerkelijk nodig zijn.


============================================================
8. AANSLUITEN OP VOORKENNIS
============================================================

Nieuwe uitleg sluit waar mogelijk aan op iets dat leerlingen
al kennen.

Bijvoorbeeld:

    Tot nu toe ...

    Soms ...

    Wanneer ...

Hiermee ontstaat een inhoudelijke reden voor het nieuwe
concept.

Een introductie kan bijvoorbeeld de beweging maken:

    bestaand gedrag
          ↓
    beperking / nieuwe situatie
          ↓
    nieuw Python-concept

Gebruik dit alleen wanneer de aansluiting werkelijk bestaat.

Schrijf geen kunstmatige context alleen om een introductie
te hebben.


============================================================
9. NIEUWE BEGRIPPEN INTRODUCEREN
============================================================

Introduceer een nieuw begrip op het moment dat de leerling
het nodig heeft.

Maak duidelijk:

- hoe het begrip heet;
- wat het betekent;
- welke functie het heeft.

Gebruik daarna dezelfde term consequent.

Belangrijke begrippen mogen vet worden weergegeven wanneer
ze worden geïntroduceerd.

Bijvoorbeeld:

    Een **Boolean expression** is ...

Gebruik code-opmaak voor letterlijke Python-elementen:

    `if`
    `else`
    `True`
    `False`
    `==`


============================================================
10. TERMINOLOGIE
============================================================

Behoud de afgesproken terminologie van de module.

Wanneer programmeerbegrippen bewust in het Engels worden
gebruikt, vertaal ze niet per nieuwe Understanding opnieuw
naar Nederlandse alternatieven.

Voorbeelden uit het gerealiseerde ontwerp zijn:

- sequential execution;
- Boolean expression;
- Boolean value;
- comparison operator;
- assignment;
- comparison;
- condition;
- branch;
- logical operator.

Gebruik bestaande termen consequent wanneer daarop wordt
voortgebouwd.

Introduceer geen synoniemen zonder didactische reden.


============================================================
11. VOORTBOUWEN OP EERDERE UNDERSTANDING
============================================================

Herhaal eerder uitgelegde kennis niet volledig.

Wanneer een begrip al onderdeel van de leerlijn is, mag een
nieuwe Understanding dat begrip gebruiken.

Bijvoorbeeld:

    Soms hangt een beslissing af van meer dan één
    **condition**.

Daarmee kan nieuwe uitleg voortbouwen op het bestaande begrip
condition zonder conditionals opnieuw vanaf het begin uit te
leggen.

Herhaal alleen zoveel als nodig is om de nieuwe uitleg
begrijpelijk te houden.


============================================================
12. CODEVOORBEELDEN
============================================================

Codevoorbeelden zijn:

- klein;
- generiek;
- uitvoerbaar;
- gericht op het concept dat wordt uitgelegd;
- passend bij de reeds beschikbare Python-kennis.

Gebruik:

```python
[CODE]
```

Een voorbeeld moet zo weinig mogelijk afleiding bevatten.

Voeg geen:
- extra functies;
- complexe datastructuren;
- syntactische trucs;
- toekomstige leerstof;

toe wanneer deze niet nodig zijn om het concept te begrijpen.


============================================================
13. GENERIEKE VOORBEELDEN
============================================================

De content moet herbruikbaar blijven.

Gebruik daarom generieke contexten zoals:

- temperatuur;
- dag;
- leeftijd;
- eenvoudige getallen;
- eenvoudige strings;
- andere kleine herkenbare situaties.

Gebruik NIET het concrete probleem uit een actuele PSET of
TSET wanneer daarmee een deel van de oplossing wordt
weggegeven.

De Understanding legt het GEREEDSCHAP uit.

De leerling gebruikt dat gereedschap daarna zelf om een
probleem op te lossen.


============================================================
14. CODE EN BETEKENIS
============================================================

Codevoorbeelden worden waar nodig gevolgd door uitleg over
wat Python daadwerkelijk doet.

Bijvoorbeeld:

    Python evalueert eerst de condition.

    Is de condition `True`, dan ...

    Is de condition `False`, dan ...

De leerling moet niet alleen syntax herkennen, maar begrijpen
welke computationele betekenis de constructie heeft.

Vraag bij een codevoorbeeld daarom:

    "Wat moet de leerling uit dit voorbeeld begrijpen?"

Als het antwoord niet vanzelfsprekend is, leg dat expliciet
uit.


============================================================
15. EXPRESSIONS EXPLICIET ZICHTBAAR MAKEN
============================================================

Wanneer een deel van een regel code het centrale concept is,
mag dat deel afzonderlijk worden getoond.

Bijvoorbeeld:

```python
temperature > 20
```

Hierdoor kan de uitleg zich richten op de expression zelf in
plaats van op het volledige programma.

Gebruik deze techniek wanneer dit helpt om:

- expressions;
- conditions;
- operators;
- andere relevante constructies;

conceptueel te isoleren.


============================================================
16. UITVOER TONEN
============================================================

Wanneer de uitvoer noodzakelijk is om het gedrag te begrijpen,
toon deze apart:

```text
[UITVOER]
```

Maak vervolgens expliciet waarom deze uitvoer ontstaat.

Gebruik geen uitvoerblok wanneer het niets toevoegt aan het
begrip.


============================================================
17. ABSTRACTE STRUCTUUR
============================================================

Wanneer leerlingen na een concreet voorbeeld de algemene
structuur moeten herkennen, kan deze abstract worden gemaakt.

Bijvoorbeeld:

```python
if condition:
    action_a
else:
    action_b
```

of:

```python
condition_1 and condition_2
```

Gebruik betekenisvolle generieke placeholders:

- condition;
- condition_1;
- action;
- action_a;
- value.

Abstractie helpt leerlingen het programmeerpatroon los te
zien van één specifieke context.

Introduceer abstracte structuur alleen wanneer die
didactisch iets toevoegt.


============================================================
18. GELEIDELIJK UITBREIDEN
============================================================

Wanneer een concept meerdere niveaus heeft, introduceer deze
in een logische volgorde.

Bijvoorbeeld:

    eenvoudige condition
          ↓
    twee branches
          ↓
    meerdere branches

of:

    één condition
          ↓
    conditions combineren
          ↓
    meerdere logical operators combineren

Iedere uitbreiding bouwt voort op wat daarvoor is uitgelegd.

Introduceer niet meerdere varianten tegelijk wanneer een
stapsgewijze opbouw duidelijker is.


============================================================
19. VERGELIJKEN EN CONTRASTEREN
============================================================

Maak verschillen expliciet wanneer twee constructies
gemakkelijk met elkaar kunnen worden verward.

Bijvoorbeeld:

    `=`  tegenover  `==`

Leg niet alleen uit DAT ze verschillen.

Leg uit wat beide doen:

    assignment
        versus
    comparison

Gebruik deze aanpak alleen bij relevante conceptuele
verwarring.


============================================================
20. TABELLEN
============================================================

Gebruik tabellen wanneer informatie daardoor compacter en
duidelijker wordt.

Bijvoorbeeld voor operators:

| Operator | Betekenis |
| -------- | --------- |
| `[OPERATOR]` | [BETEKENIS] |

Een tabel ondersteunt de uitleg.

De tabel vervangt geen conceptuele uitleg wanneer betekenis
of gedrag nog moet worden uitgelegd.


============================================================
21. OPSOMMINGEN
============================================================

Gebruik opsommingen wanneer meerdere mogelijkheden,
eigenschappen of stappen naast elkaar moeten worden gezet.

Bijvoorbeeld:

- situatie A;
- situatie B.

Gebruik een genummerde lijst wanneer de VOLGORDE belangrijk
is.

Bijvoorbeeld wanneer Python een constructie stap voor stap
evalueert:

1. eerst ...;
2. daarna ...;
3. als ...;
4. anders ....

Gebruik lijsten functioneel, niet als standaardvorm voor
alle uitleg.


============================================================
22. PYTHON-GEDRAG EXPLICIET BESCHRIJVEN
============================================================

Wanneer volgorde of evaluatie belangrijk is, beschrijf wat
Python doet in de juiste volgorde.

Bijvoorbeeld:

    Python controleert de conditions van boven naar beneden.

Daarna kan de volgorde expliciet worden gemaakt.

Dit helpt leerlingen een mentaal model van de uitvoering te
ontwikkelen.

Beperk dit tot gedrag dat binnen de huidige leerstof
relevant is.


============================================================
23. RELATIE TUSSEN BEGRIPPEN
============================================================

Een Understanding kan afsluiten door belangrijke begrippen
met elkaar in verband te brengen wanneer dit nodig is voor
het conceptuele begrip.

Bijvoorbeeld:

    condition
        ↓
    True / False
        ↓
    branch

of:

    meerdere conditions
        ↓
    logical operator
        ↓
    één Boolean expression

Een dergelijke afsluiting is functioneel wanneer zij de
conceptuele structuur verduidelijkt.

Voeg niet automatisch een samenvatting toe aan iedere
Understanding.


============================================================
24. PROBLEEMOPLOSSEN BLIJFT BIJ DE LEERLING
============================================================

Understanding legt uit hoe Python-gereedschap werkt.

Understanding bepaalt NIET voor de leerling hoe dat
gereedschap in een concreet probleem moet worden ingezet.

Een belangrijke grens is daarom:

WEL:

    Met `and` kun je aangeven dat meerdere conditions
    tegelijk moeten gelden.

NIET:

    Voor opdracht X moet je hier condition A en condition B
    met `and` combineren.

Welke:

- conditions;
- branches;
- variabelen;
- algoritmische stappen;

nodig zijn, blijft onderdeel van het probleemoplossen.


============================================================
25. RELATIE MET COMPUTATIONAL THINKING
============================================================

Python Understanding ondersteunt het uitdrukken van een
oplossing in programmeercode.

De content hoeft daarom niet telkens expliciet CT-theorie te
benoemen.

Wel moet de uitleg ruimte laten voor de leerling om zelf:

- het probleem te analyseren;
- relevante informatie te bepalen;
- conditions te formuleren;
- branches te ontwerpen;
- algoritmes te construeren;
- andere probleemafhankelijke keuzes te maken.

De Understanding levert programmeerkennis.

Zij neemt het computationele denkwerk niet over.


============================================================
26. RELATIE MET PSET
============================================================

Dezelfde `_content` kan rechtstreeks in een PSET worden
opgenomen.

Daarom bevat dit bestand geen verwijzingen zoals:

- "in deze Problem Set";
- "voor Jellybeans";
- "voor opdracht 3";
- "gebruik dit nu om ... te maken".

De PSET legt zelf de verbinding tussen algemene kennis en het
concrete probleem.

De content blijft contextonafhankelijk en herbruikbaar.


============================================================
27. RELATIE MET TSET
============================================================

Wanneer deze content vanuit een Thinking Set bereikbaar is,
mag zij niet onbedoeld het relevante denkwerk uit de Thinking
Task overnemen.

Controleer daarom extra zorgvuldig:

- geeft een voorbeeld geen oplossing van de challenge?
- wordt een probleemafhankelijke structuur niet al ingevuld?
- blijft de keuze hoe het concept wordt toegepast bij de
  leerling?

De TSET bepaalt WANNEER en HOE naar Understanding wordt
verwezen.


============================================================
28. GEEN OEFENOPDRACHTEN IN _CONTENT
============================================================

De gerealiseerde Python-content is primair uitleg en naslag.

Voeg daarom niet automatisch:

- oefenvragen;
- mini-opdrachten;
- quizvragen;
- reflectievragen;

toe.

Oefenen vindt plaats binnen de daarvoor ontworpen onderdelen
van de module, zoals PSET's.

Alleen wanneer we bewust besluiten de functie van
Understanding uit te breiden, wordt deze afspraak aangepast.


============================================================
29. GEEN LEERDOELEN IN _CONTENT
============================================================

Leerdoelen worden niet opnieuw boven iedere Python
Understanding geplaatst.

De leerdoelen horen bij de onderwijscontext waarin de
Understanding wordt gebruikt, zoals de PSET of TSET.

De content begint rechtstreeks met de conceptuele uitleg.


============================================================
30. EERSTE H3 EN GEEN PAGINATITEL IN _CONTENT
============================================================

Gebruik in `_content` geen H1:

    # [Titel]

De zelfstandige wrapper bevat de paginatitel.

Ieder `_content`-bestand begint direct met een inhoudelijke H3:

    ### [ONDERWERP]

Deze eerste H3 blijft ALTIJD in `_content` staan.

De zelfstandige Understanding-wrapper plaatst direct vóór de
include de marker:

    <div class="understanding-article-start"></div>

De Understanding-CSS verbergt daardoor alleen op de
zelfstandige Understanding-pagina de eerste H3.

Wanneer dezelfde `_content` in een PSET, TSET, ander document
of samengestelde PDF wordt opgenomen, blijft die eerste H3
juist zichtbaar en geeft zij het ingevoegde kennisdeel een
duidelijke inhoudelijke kop.

Plaats de marker `understanding-article-start` NOOIT in
`_content`; die hoort uitsluitend in de wrapper.

Gebruik `####` voor een logisch subonderdeel binnen zo'n
sectie wanneer dat nodig is.


============================================================
31. BESTANDSENCODING
============================================================

Sla alle `_content`-bestanden op als:

    UTF-8 zonder BOM

Dit is een technische ontwerpregel.

Een UTF-8 BOM vóór de eerste `###` kan ervoor zorgen dat
Markdown die eerste regel niet als heading herkent. Daardoor
kan bijvoorbeeld letterlijk `### Decisions` of `### elif`
op de pagina verschijnen.

Controleer daarom bij automatisch genereren of herschrijven van
bestanden expliciet dat geen BOM wordt toegevoegd.


============================================================
32. LEESBAARHEID
============================================================

Schrijf voor leerlingen die het concept nog niet beheersen.

Gebruik:

- korte alinea's;
- duidelijke tussenkoppen;
- kleine codeblokken;
- voldoende witruimte;
- één inhoudelijke stap tegelijk;
- concrete formuleringen.

Vermijd:

- lange theoretische uiteenzettingen;
- onnodig formele definities;
- technisch jargon buiten de leerlijn;
- grote codevoorbeelden;
- meerdere nieuwe concepten tegelijk zonder noodzaak.

De tekst mag inhoudelijk precies zijn zonder academisch
zwaar te worden.


============================================================
33. REFERENTIE-ONTWERP
============================================================

De gerealiseerde Python-content vormt de referentie voor
stijl en toepassing.

Daaruit volgen onder andere:

- content begint direct inhoudelijk;
- nieuwe kennis sluit aan op bestaande kennis;
- begrippen worden expliciet geïntroduceerd;
- terminologie blijft consequent;
- voorbeelden zijn klein en generiek;
- code en uitvoer worden waar nodig apart getoond;
- abstracte syntax volgt waar functioneel uit concrete
  voorbeelden;
- Python-gedrag wordt expliciet gemaakt;
- complexiteit wordt geleidelijk opgebouwd;
- eerder geleerde begrippen worden gebruikt zonder volledige
  herhaling;
- probleemafhankelijke keuzes blijven bij de leerling.

De voorbeelden uit eerdere Understandings bepalen NIET welke
inhoud in een nieuwe Understanding hoort.

Daarvoor blijft het MODULEFRAMEWORK leidend.
-->


<!--
============================================================
CONTENT
============================================================

Vanaf hier komt uitsluitend de daadwerkelijke
leerlingzichtbare Understanding-content.

Verwijder deze instructiecomments wanneer het bestand wordt
ingevuld.

Gebruik GEEN H1.

Begin met het eerste inhoudelijk noodzakelijke onderdeel.
-->


### [EERSTE CONCEPT / ONDERWERP]

<!--
OPTIONELE INTRODUCTIE

Sluit waar mogelijk aan op bestaande kennis of een bekende
situatie.

Introduceer vervolgens het nieuwe concept.

Verwijder deze comment.
-->

[Conceptuele introductie.]


<!--
KLEIN CONCREET VOORBEELD — ALLEEN WANNEER FUNCTIONEEL
-->

```python
[GENERIEK VOORBEELD]
```

[Leg uit wat Python hier doet en waarom.]


<!--
UITVOER — ALLEEN WANNEER DEZE NODIG IS VOOR BEGRIP

```text
[UITVOER]
```

[Leg de relatie tussen code en uitvoer uit.]
-->


<!--
ABSTRACTE STRUCTUUR — ALLEEN WANNEER FUNCTIONEEL

```python
[ALGEMENE STRUCTUUR]
```

Leg uit wat de onderdelen betekenen.
-->


<!--
============================================================
VOLGENDE CONCEPTUELE STAP — ALLEEN WANNEER NODIG
============================================================

Voeg alleen een volgende sectie toe wanneer het onderwerp
inhoudelijk uit meerdere opeenvolgende concepten bestaat.

Bijvoorbeeld:

### [VOLGEND CONCEPT]

of, wanneer het een subonderdeel is:

#### [SUBONDERDEEL]

Herhaal dit niet volgens een vast format; laat de
conceptuele structuur bepalen wat nodig is.
============================================================
-->


<!--
============================================================
LAATSTE ONTWERPCONTROLE
============================================================

Voer deze controle uit vóór publicatie.


FRAMEWORK EN SCOPE
------------------
[ ] Komt het Python-concept uit het moduleframework?
[ ] Past de inhoud bij deze plaats in de leerlijn?
[ ] Behandelt de content precies wat leerlingen nu nodig
    hebben?
[ ] Is toekomstige leerstof buiten de content gebleven?
[ ] Is geen extra Python-inhoud toegevoegd alleen omdat die
    technisch bij het onderwerp hoort?


VOORKENNIS EN OPBOUW
--------------------
[ ] Is vastgesteld welke voorkennis beschikbaar is?
[ ] Sluit nieuwe kennis daar waar mogelijk op aan?
[ ] Wordt het concept stapsgewijs opgebouwd?
[ ] Is de volgorde conceptueel logisch?
[ ] Worden eerder behandelde begrippen niet onnodig volledig
    herhaald?


TERMINOLOGIE
------------
[ ] Wordt bestaande moduleterminologie consequent gebruikt?
[ ] Worden nieuwe begrippen expliciet geïntroduceerd?
[ ] Worden geen onnodige synoniemen geïntroduceerd?
[ ] Staat letterlijke Python-syntax in code-opmaak?


VOORBEELDEN
-----------
[ ] Is ieder voorbeeld functioneel?
[ ] Is ieder codevoorbeeld zo klein mogelijk?
[ ] Is het voorbeeld generiek?
[ ] Gebruikt het alleen beschikbare Python-kennis?
[ ] Geeft het geen PSET- of TSET-oplossing weg?
[ ] Is eventuele uitvoer alleen opgenomen wanneer die helpt
    bij het begrip?


CODE EN BETEKENIS
-----------------
[ ] Wordt niet alleen syntax maar ook betekenis uitgelegd?
[ ] Is duidelijk wat Python evalueert of uitvoert?
[ ] Is relevante uitvoeringsvolgorde expliciet wanneer dat
    nodig is?
[ ] Helpt de uitleg een correct mentaal model op te bouwen?


ABSTRACTIE
----------
[ ] Wordt abstracte syntax alleen gebruikt wanneer deze
    functioneel is?
[ ] Zijn placeholders begrijpelijk en consequent?
[ ] Helpt de abstractie het concept los te zien van één
    concreet voorbeeld?


PROBLEEMOPLOSSEN
----------------
[ ] Legt de content het Python-gereedschap uit?
[ ] Blijven probleemafhankelijke keuzes bij de leerling?
[ ] Worden geen conditions, branches, algoritmes of andere
    oplossingen voor een concrete opdracht ingevuld?
[ ] Blijft computationeel denkwerk bij de leerling?


HERBRUIKBAARHEID
----------------
[ ] Is de content onafhankelijk van één specifieke week?
[ ] Is de content onafhankelijk van één specifieke PSET?
[ ] Is de content onafhankelijk van één specifieke TSET?
[ ] Kan dezelfde content zowel zelfstandig als via een
    include worden gebruikt?


STRUCTUUR
--------
[ ] Staat er geen frontmatter in _content?
[ ] Staat er geen H1 in _content?
[ ] Is de eerste H3 in _content behouden en niet naar de wrapper verplaatst?
[ ] Staat er geen `understanding-article-start` marker in _content?
[ ] Is het bestand UTF-8 zonder BOM?
[ ] Begint het bestand direct met een inhoudelijke H3 (`###`)?
[ ] Zijn alleen inhoudelijk noodzakelijke tussenkoppen
    gebruikt?
[ ] Is geen kunstmatig vast hoofdstukformat afgedwongen?


LEESBAARHEID
------------
[ ] Zijn alinea's kort en functioneel?
[ ] Wordt één inhoudelijke stap tegelijk behandeld?
[ ] Zijn codeblokken overzichtelijk?
[ ] Is onnodige technische complexiteit verwijderd?
[ ] Is de tekst begrijpelijk voor een leerling die dit
    concept voor het eerst leert?


REFERENTIE-ONTWERP
------------------
[ ] Sluit de stijl aan op de gerealiseerde Understandings?
[ ] Is geen nieuwe leerlingzichtbare structuur ingevoerd?
[ ] Is geen automatische samenvatting toegevoegd?
[ ] Zijn geen automatische oefeningen toegevoegd?
[ ] Zijn geen leerdoelen toegevoegd?


EINDCONTROLE
------------
[ ] Zijn alle placeholders verwijderd?
[ ] Werken alle codevoorbeelden?
[ ] Klopt eventuele uitvoer?
[ ] Zijn tabellen alleen gebruikt waar ze meerwaarde hebben?
[ ] Verwijst hergebruik naar `understanding/_content/python/[BESTAND].md`?
[ ] Kan het bestand zonder aanpassing via een wrapper én via
    een andere pagina worden geïncludeerd?
============================================================
-->