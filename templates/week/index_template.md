---
title: Week [NUMMER] — [TITEL]
template: week.html
---

# Week [NUMMER] *[TITEL]*

<!--
============================================================
WEEK INDEX — ONTWERPCONTRACT
============================================================

DOEL VAN DEZE TEMPLATE
----------------------
Deze template legt het gerealiseerde ontwerp van de
week-index vast.

De week-index is de korte inhoudelijke ingang naar een week.

De pagina moet de leerling:

- onmiddellijk in de context van de week brengen;
- zichtbaar maken welke inhoudelijke focus de week heeft;
- nieuwsgierig maken naar het probleem;
- daarna rechtstreeks toegang geven tot de Thinking Set en
  Problem Set.

De week-index is GEEN overzichtspagina waarop alle theorie,
leerdoelen, planning of opdrachten opnieuw worden uitgelegd.

De inhoudelijke bron blijft het MODULEFRAMEWORK.


============================================================
1. BELANGRIJKE REGEL VOOR DEZE TEMPLATE
============================================================

De template beschrijft en borgt het gerealiseerde ontwerp.

Tijdens het invullen van een nieuwe week worden GEEN nieuwe
leerlingzichtbare ontwerpkeuzes ingevoerd.

Dat betekent onder andere:

- geen nieuwe headings toevoegen;
- geen extra secties toevoegen;
- geen leerdoelenblok toevoegen;
- geen planning toevoegen;
- geen uitgebreide theorie toevoegen;
- geen beschrijving van de PSET/TSET toevoegen;
- geen andere videopresentatie kiezen;

alleen omdat dat op dat moment handig lijkt.

Een nieuwe ontwerpkeuze wordt eerst apart besproken.

Pas daarna wordt deze eventueel in zowel de gerealiseerde
referentie als de template verwerkt.


============================================================
2. ONDERWIJSINHOUDELIJKE HIËRARCHIE
============================================================

Gebruik bij het ontwerpen altijd deze volgorde:

1. MODULEFRAMEWORK
   Bepaalt de onderwijsinhoud en de plaats in de leerlijn.

2. WEEKONTWERP
   Bepaalt de concrete context, Thinking Set en Problem Set.

3. WEEK-INDEX-TEMPLATE
   Bepaalt hoe de leerling de week binnenkomt.

4. EERDERE WEEKINDEXEN
   Zijn voorbeelden van toepassing, maar nooit bron voor
   nieuwe onderwijsinhoud.

Bij een inhoudelijk conflict is het MODULEFRAMEWORK leidend.

Voeg dus geen:
- Python-concepten;
- CT-doelen;
- Visual First-representaties;
- procesdimensies;
- context;
- video;

toe omdat deze in een eerdere week voorkwamen.


============================================================
3. FUNCTIE VAN DE WEEK-INDEX
============================================================

De week-index beantwoordt vooral:

    "Waar gaat deze week over en waar begin ik?"

De pagina doet dat met zo weinig mogelijk tekst.

De globale beweging is:

    titel / inhoudelijke focus
            ↓
    korte context / launch
            ↓
    Thinking Set
            ↓
    Problem Set

De leerling moet snel van de weekpagina naar het daadwerkelijke
denken en werken kunnen gaan.


============================================================
4. SOURCE OF TRUTH — MODULEFRAMEWORK
============================================================

Bepaal vóór het schrijven uit het framework minimaal:

- weeknummer;
- weektitel;
- Python-focus;
- Visual First-representatie;
- CT-domein;
- CT-procesdimensie;
- probleemsituatie / context;
- centrale inhoudelijke beweging van de week.

Bepaal uit het weekontwerp:

- welke Thinking Set bij deze week hoort;
- welke Problem Set bij deze week hoort;
- of er een functioneel passende video bestaat;
- welke korte launchtekst de context introduceert.


============================================================
5. ONTWERPANALYSE VÓÓR HET SCHRIJVEN
============================================================

Bepaal eerst:

BADGES
- Welke Python-focus geldt voor de volledige week?
- Welke Visual First-representatie geldt?
- Welk CT-domein staat centraal?
- Welke CT-procesdimensie heeft de focus?

CONTEXT
- Welke concrete situatie draagt de week?
- Wat is het minimale dat de leerling moet weten om
  nieuwsgierig te worden naar het probleem?
- Welke informatie moet juist nog NIET worden uitgelegd?

VIDEO
- Is er een video die functioneel bij de context hoort?
- Ondersteunt deze de launch?
- Geeft deze niet de oplossingsroute weg?
- Bestaat hiervoor een include in includes/videos.html?

ROUTES
- Wat is het juiste TSET-bestand?
- Wat is de juiste PSET-index?
- Kloppen de relatieve paden?

Schrijf pas daarna de week-index.


============================================================
6. VASTE LEERLINGZICHTBARE STRUCTUUR
============================================================

De gerealiseerde structuur is:

# Week [NUMMER] *[TITEL]*

badges

[optioneel: video]

[korte launchtekst]

---

[Thinking Set]

[Problem Set]

Deze structuur wordt niet tijdens het invullen van een nieuwe
week opnieuw ontworpen.


============================================================
7. BADGES
============================================================

De badges beschrijven de inhoudelijke focus van de VOLLEDIGE
week.

Gebruik vanuit het framework:

- Python-focus;
- Visual First-representatie;
- CT-domein;
- CT-procesdimensie.

Gebruik hier geen:
- Less/More-badge;
- PSET-specifieke uitbreiding;
- concept dat slechts in één deelopdracht voorkomt.

De week-index geeft de gemeenschappelijke inhoudelijke
positie van de week weer.


============================================================
8. VIDEO — OPTIONEEL
============================================================

Een video is geen verplicht onderdeel van iedere week.

Gebruik alleen een video wanneer deze functioneel bij de
context/launch hoort.

De video kan bijvoorbeeld:
- de probleemsituatie introduceren;
- nieuwsgierigheid oproepen;
- een herkenbare context geven.

De video mag niet:
- de oplossing uitleggen;
- het algoritme voordoen;
- noodzakelijke theorieles vervangen.

VIDEO-INFRASTRUCTUUR
--------------------
Gebruik de centrale video-component uit:

    docs/includes/videos.html

Neem geen los iframe rechtstreeks in de week-index op.

Gebruik:

    --8<-- "includes/videos.html:[VIDEO-ID]"

Zo blijft de vormgeving van video's centraal beheerd via
videos.html en video.css.

Als de week geen functionele video heeft, verwijder de
videoregel volledig.


============================================================
9. LAUNCHTEKST
============================================================

De launchtekst is bewust kort.

Functie:
- leerling in de context brengen;
- relevante situatie neerzetten;
- spanning/probleem zichtbaar maken;
- nog NIET uitleggen hoe het probleem wordt opgelost.

De launchtekst mag bestaan uit:
- enkele korte zinnen;
- een kleine opsomming;
- noodzakelijke contextinformatie.

Vermijd:
- uitgebreide achtergrond;
- leerdoelen;
- Python-theorie;
- stappenplannen;
- oplossingsstrategieën;
- uitleg die in de TSET of PSET thuishoort.

De leerling moet na deze tekst voldoende context hebben om
door te gaan, maar nog steeds zelf moeten denken.


============================================================
10. RELATIE MET THINKING SET
============================================================

De Thinking Set is de Thinking Task van de week.

De week-index legt de TSET niet opnieuw uit.

Gebruik alleen de vaste link:

    [Thinking Set](...){ .week-resource }

De inhoudelijke uitleg begint pas op de TSET-pagina.

Dit voorkomt dat de Thinking Task op de week-index al wordt
voorgestructureerd.


============================================================
11. RELATIE MET PROBLEM SET
============================================================

De Problem Set wordt eveneens niet op de week-index
samengevat.

Gebruik alleen de vaste link:

    [Problem Set](...){ .week-resource }

De PSET-index bevat vervolgens:
- werkwijze;
- Less/More-keuzes;
- aanvullende bronnen;
- planning;
- ondersteuning.

De week-index dupliceert dat niet.


============================================================
12. TEKST EN LEESBAARHEID
============================================================

De week-index moet zeer compact blijven.

Gebruik:
- korte zinnen;
- functionele witruimte;
- eventueel een kleine opsomming;
- weinig tekst vóór de links.

Vermijd:
- lange paragrafen;
- uitleg van badges;
- uitleg van TSET/PSET;
- planning;
- externe bronnen;
- portfolio-instructies;
- Git-instructies.

De week-index is een ingang, geen dashboard.


============================================================
13. REFERENTIE-ONTWERP
============================================================

Week 3 is het gerealiseerde referentievoorbeeld.

Daar is de leerlingzichtbare volgorde:

1. titel;
2. vier inhoudelijke badges;
3. video;
4. korte contexttekst;
5. horizontale scheiding;
6. Thinking Set-link;
7. Problem Set-link.

Een nieuwe week mag inhoudelijk anders zijn, maar de template
wordt niet stilzwijgend aangepast omdat een andere structuur
op dat moment aantrekkelijk lijkt.
-->


<!-- ========================================================
     BADGES
     ========================================================

     Kies uitsluitend vanuit het MODULEFRAMEWORK.

     Gebruik dezelfde badgevolgorde als het gerealiseerde
     weekontwerp:

     1. Python
     2. Visual First
     3. CT-domein
     4. CT-proces
     ======================================================== -->

--8<-- "includes/badges.html:[PYTHON]"
--8<-- "includes/badges.html:[VISUAL]"
--8<-- "includes/badges.html:[CT-DOMEIN]"
--8<-- "includes/badges.html:[CT-PROCES]"


<!--
============================================================
VIDEO — OPTIONEEL
============================================================

Gebruik alleen wanneer deze week een functioneel passende
video heeft.

De video moet al als snippet in includes/videos.html bestaan.

Voorbeeld:

--8<-- "includes/videos.html:jellybeans"

Verwijder de regel volledig wanneer er geen video wordt
gebruikt.
-->

--8<-- "includes/videos.html:[VIDEO-ID]"


<!--
============================================================
LAUNCHTEKST
============================================================

Schrijf hier de korte inhoudelijke ingang naar de week.

Gebruik het MODULEFRAMEWORK en weekontwerp.

De launchtekst:
- introduceert de context;
- bevat alleen noodzakelijke informatie;
- blijft compact;
- geeft geen oplossingsstrategie.

Behoud de rustige vorm van het gerealiseerde Week-3-ontwerp.

Geen extra heading boven deze tekst.
-->

[Korte contextzin.]

[Korte contextzin.]

[Korte contextzin.]

[Eventueel:]

- [mogelijkheid / situatie];
- [mogelijkheid / situatie];
- [mogelijkheid / situatie].

---

<!--
============================================================
THINKING SET
============================================================

Link rechtstreeks naar de TSET van deze week.

Geen beschrijving of samenvatting toevoegen.

Controleer:
- weeknummer;
- mapnaam;
- bestandsnaam;
- relatief pad.
-->

[Thinking Set](../../tsets/[WEEK-MAP]/[TSET-BESTAND].md){ .week-resource }


<!--
============================================================
PROBLEM SET
============================================================

Link rechtstreeks naar de PSET-index van deze week.

Geen beschrijving van de individuele PSET's toevoegen.

Controleer:
- weeknummer;
- mapnaam;
- relatief pad.
-->

[Problem Set](../../psets/[WEEK-MAP]/index.md){ .week-resource }


<!--
============================================================
LAATSTE ONTWERPCONTROLE
============================================================

Voer deze controle uit vóór publicatie.


FRAMEWORK
---------
[ ] Komt de onderwijsinhoud uit het moduleframework?
[ ] Klopt het weeknummer?
[ ] Klopt de weektitel?
[ ] Klopt de Python-focus?
[ ] Klopt de Visual First-representatie?
[ ] Klopt het CT-domein?
[ ] Klopt de CT-procesdimensie?
[ ] Is geen nieuwe onderwijsinhoud vanuit de template bedacht?


BADGES
------
[ ] Gelden alle badges voor de volledige week?
[ ] Staan ze in de vaste volgorde?
[ ] Staat er geen Less/More-badge?
[ ] Staat er geen PSET-specifieke uitbreiding tussen?


VIDEO
-----
[ ] Heeft de video een duidelijke functie?
[ ] Hoort hij bij de context van de week?
[ ] Geeft hij de oplossing niet weg?
[ ] Is de video opgenomen via includes/videos.html?
[ ] Is geen rechtstreeks iframe in de week-index geplaatst?
[ ] Is de videoregel verwijderd als er geen video nodig is?


LAUNCH
------
[ ] Is de context snel te begrijpen?
[ ] Is de tekst compact?
[ ] Staat alleen noodzakelijke informatie op de pagina?
[ ] Is geen theorie toegevoegd?
[ ] Is geen oplossingsroute toegevoegd?
[ ] Staat er geen onnodige heading boven de launch?


THINKING SET
------------
[ ] Verwijst de link naar de juiste TSET?
[ ] Is de TSET niet op de week-index uitgelegd?
[ ] Klopt het relatieve pad?


PROBLEM SET
-----------
[ ] Verwijst de link naar de juiste PSET-index?
[ ] Is de PSET niet op de week-index samengevat?
[ ] Klopt het relatieve pad?


REFERENTIE-ONTWERP
------------------
[ ] Is de leerlingzichtbare hoofdstructuur behouden?
[ ] Zijn geen nieuwe headings of secties geïntroduceerd?
[ ] Is geen leerlingtekst uit andere pagina's gedupliceerd?
[ ] Is de index compact gebleven?


EINDCONTROLE
------------
[ ] Zijn alle placeholders vervangen?
[ ] Werken alle links?
[ ] Werkt de eventuele video?
[ ] Werken alle badges?
[ ] Kan de leerling vrijwel direct van de week-index naar
    denken en werken?
============================================================
-->