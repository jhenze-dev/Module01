# PDF / Render Contract — Module 01

<!--
============================================================
DOEL VAN DIT CONTRACT
============================================================

Dit document legt de afspraken vast voor het renderen van dezelfde
onderwijsinhoud naar verschillende uitvoervormen:

1. website;
2. losse PSET- of TSET-PDF;
3. complete Module-PDF;
4. Understanding-PDF.

Het doel is dat onderwijsinhoud slechts één keer wordt onderhouden,
terwijl de presentatie per medium mag verschillen.

Dit contract beschrijft dus NIET de inhoud van een specifieke week,
Thinking Set, Problem Set of Understanding, maar de regels voor
hergebruik en rendering.
-->


## 1. Uitgangspunt: één bron, meerdere uitvoervormen

Onderwijsinhoud wordt zo veel mogelijk één keer opgeslagen.

De renderer bepaalt vervolgens hoe die inhoud wordt aangeboden in:

- de website;
- een losse PSET-PDF;
- een losse TSET-PDF;
- de complete Module-PDF;
- de Understanding-PDF.

Er worden geen aparte inhoudsversies onderhouden voor web en PDF
wanneer alleen de presentatie verschilt.


## 2. Functie van de uitvoervormen

### Website

De website is de interactieve hoofdvorm.

De website mag gebruikmaken van:

- interne links;
- uitklapbare hints;
- embedded video;
- embedded demo's;
- interactieve elementen;
- directe Understanding-includes;
- webnavigatie.


### Losse PSET- of TSET-PDF

Een losse PDF moet zelfstandig bruikbaar zijn.

Daarom bevat deze waar nodig ook de relevante Understanding-content.

Een leerling moet een losse PSET- of TSET-PDF kunnen gebruiken zonder
eerst een tweede document te moeten openen voor noodzakelijke uitleg.


### Complete Module-PDF

De complete Module-PDF bevat de volledige module als samenhangend
document.

Understanding-content wordt daarin niet telkens opnieuw bij iedere
PSET of TSET afgedrukt.

Wanneer een PSET of TSET Understanding nodig heeft, wordt in de
Module-PDF verwezen naar de betreffende Understanding-pagina of het
betreffende paginabereik.


### Understanding in de complete Module-PDF

Understanding wordt in de complete Module-PDF één keer als centrale,
doorlopende kennisbank opgenomen.

PSETs en TSETs verwijzen vanuit hun eigen positie naar deze centrale
Understanding-pagina's.

De paginaposities worden tijdens de build bepaald en vormen de bron voor
de automatisch gegenereerde verwijzingen.


## 3. Renderingmatrix

| Onderdeel | Website | Losse PSET/TSET-PDF | Module-PDF |
|---|---|---|---|
| Titel | tonen | tonen | tonen |
| Badges | tonen | tonen | tonen |
| Leerdoelen | tonen | tonen | tonen |
| Probleem/context | tonen | tonen | tonen |
| Demo | embed | QR-code | QR-code |
| Video | embed | QR-code | QR-code |
| Mermaid-diagram | gegenereerde PNG | gegenereerde PNG | gegenereerde PNG |
| Understanding | inline | inline | centrale sectie + verwijzing |
| Resources | webweergave | PDF-weergave | PDF-weergave |
| Opdracht | tonen | tonen | tonen |
| Hints | uitklapbaar | zichtbaar | zichtbaar |
| Testen | tonen | tonen | tonen |
| Inleveren | tonen | tonen | tonen |
| Webnavigatie | tonen | niet tonen | niet tonen |


## 4. Understanding-verwijzingen

PSETs en TSETs verwijzen inhoudelijk naar Understanding-concepten,
niet naar vaste paginanummers.

Gebruik daarvoor stabiele concept-ID's, bijvoorbeeld:

    python.conditions
    python.if
    python.elif
    visual-first.ipo
    visual-first.flowcharts.basics

De presentatie bepaalt daarna de uitvoervorm.

Voorbeeld:

Website:

    /understanding/python/conditions/

Losse PSET/TSET-PDF:

    volledige Understanding-content opnemen

Module-PDF:

    Zie Understanding — Conditions, p. 27

Paginanummers worden NOOIT handmatig in een PSET of TSET geschreven.


## 5. Paginanummers en cross-references

Paginanummers worden centraal beheerd en tijdens de PDF-build bepaald.

De gerealiseerde richting is:

    Understanding-secties opbouwen
            ↓
    beginpagina per Understanding-ID bepalen
            ↓
    generated/understanding-pages.yml
            ↓
    PSET/TSET-verwijzingen opbouwen
            ↓
    Module-PDF renderen

Een gegenereerd YAML-bestand kan bijvoorbeeld bevatten:

```yaml
understanding:
  python.conditions:
    title: Conditions
    page: 27

  python.if:
    title: if
    page: 29

  visual-first.flowcharts.basics:
    title: Flowcharts — Basics
    page: 46
```

De gegenereerde paginadata is build-data en wordt niet handmatig in
PSETs of TSETs onderhouden.

Bij één Understanding-item wordt één titel met één paginanummer getoond.
Bij meerdere opeenvolgende items wordt een bereik opgebouwd van het eerste
tot en met het laatste item.

De PSET- en TSET-bronnen blijven daarvan onafhankelijk.


## 6. Resources

Resources worden via stabiele IDs centraal geregistreerd.

De onderwijsbestanden bevatten dus niet opnieuw handmatig:

- URL's;
- boektitels;
- hoofdstuk- of paginagegevens;
- resourcebeschrijvingen;
- PDF-specifieke verwijzingen.

Resourcegegevens worden centraal beheerd in de resource-data.

Een pagina kan in de frontmatter aangeven welke resources zij gebruikt:

```yaml
resources:
  - video.jellybeans
```

Een PSET-index kan een samengestelde resourcegroep tonen via:

```jinja
{{ resource_group("[RESOURCE-GROEP]") }}
```

De renderer bepaalt hoe dezelfde resource in web en PDF verschijnt.

Website:
- passende link, embed of resourcepresentatie.

PDF:
- printvriendelijk resourceblok;
- waar passend een QR-code;
- geen afhankelijkheid van klikbare webnavigatie.

De onderwijsbron blijft onafhankelijk van de concrete presentatie.


## 7. Multimedia

Multimedia wordt via een stabiele ID opgenomen.

Voorbeelden:

    demo.jellybeans-less
    video.conditionals

De concrete URL staat centraal in data, niet verspreid door meerdere
onderwijsbestanden.

Bijvoorbeeld:

```yaml
media:
  demo.jellybeans-less:
    type: asciinema
    url: https://...

  video.conditionals:
    type: youtube
    url: https://...
```

Rendering:

Website:

- YouTube → embedded video;
- asciinema → embedded terminaldemo;
- andere ondersteunde media → passende embed.

PDF:

- QR-code;
- korte omschrijving;
- eventueel zichtbare korte URL wanneer dat functioneel is.

De QR-code verwijst naar dezelfde URL als de web-embed.


## 8. Mermaid en gegenereerde diagrammen

Mermaid-broncode blijft onderdeel van de Markdown en is de
source of truth voor het diagram.

Ieder Mermaid-blok bevat direct na de opening een stabiele ID:

```mermaid
%% id: guess-the-number-01

flowchart TD
    A([Start]) --> B[Stap]
```

De ID bepaalt rechtstreeks de bestandsnaam:

    guess-the-number-01.png

Gebruik voor IDs:

- lowercase letters;
- cijfers;
- koppeltekens;
- een herkenbare inhoudelijke naam;
- een volgnummer `-01`, `-02`, enzovoort.

Er zijn twee assetcategorieën:

    build/assets/mermaid/sets/
    build/assets/mermaid/understanding/

TSET- en PSET-diagrammen worden opgeslagen onder `sets`.

Understanding-diagrammen worden opgeslagen onder `understanding`.

Less en More vormen GEEN afzonderlijke Mermaid-categorie. Wanneer
Less en More exact hetzelfde diagram gebruiken, mogen zij bewust
dezelfde Mermaid-ID gebruiken en daarmee dezelfde PNG delen.

Dezelfde Mermaid-ID mag binnen één categorie nooit naar verschillende
Mermaid-broncode verwijzen. De build moet in dat geval stoppen met
een duidelijke foutmelding.

De Markdown bevat GEEN handmatige verwijzing naar de gegenereerde
PNG. De renderpipeline:

    leest Mermaid-bron + ID
        ↓
    genereert / overschrijft de PNG
        ↓
    vervangt het Mermaid-blok in de uitvoervorm door de afbeelding

Dezelfde gegenereerde PNG wordt gebruikt voor web en PDF. Hierdoor
is de weergave niet afhankelijk van Mermaid-rendering in de browser
en blijft de visuele output tussen uitvoervormen gelijk.

De gegenereerde PNG is build-output en wordt niet als afzonderlijke
onderwijsbron onderhouden.


## 9. Demo's

Een demo laat zien WAT het gewenste product of programma doet.

Een demo laat niet zien HOE de oplossing is gebouwd wanneer dat het
probleemoplossen van de leerling zou overnemen.

Demo's worden pas definitief gemaakt wanneer de gewenste solution en
het gewenste gedrag vaststaan.

De inhoud van de PSET of TSET mag niet afhankelijk worden van een
specifieke embed-techniek.


## 10. Video

Video ondersteunt uitleg of demonstratie, maar vervangt noodzakelijke
geschreven instructie niet.

Een leerling moet uit de tekst nog steeds kunnen begrijpen wat van hem
of haar wordt verwacht.

Video is aanvullende ondersteuning.

Website:

    embed

PDF:

    QR-code + titel / korte omschrijving


## 11. Hints

Hints blijven onderdeel van de onderwijsinhoud.

Website:

- hints zijn uitklapbaar;
- de leerling kiest bewust welke hint wordt geopend.

PDF:

- alle hints worden volledig zichtbaar opgenomen;
- zij worden als herkenbare HINT-blokken gepresenteerd;
- de volgorde en inhoud blijven gelijk aan de webversie.

Er wordt geen aparte inhoudelijke hintversie voor PDF onderhouden.


## 12. Thinking Sets en productieve worsteling

Een TSET blijft een thinking task, ongeacht het medium.

De PDF-rendering mag daarom geen extra uitleg, Understanding of
oplossingsstructuur vóór de thinking task plaatsen wanneer dit de
productieve worsteling vermindert.

De kernregels blijven:

- korte launch;
- geen strategie-uitleg;
- geen voorgeschreven representatie tenzij die onderdeel van de task is;
- meerdere instappunten;
- context, constraints en doel;
- geen spoilers of stappenplan voor de oplossing.

Web en PDF mogen visueel verschillen, maar niet didactisch van functie.


## 13. Problem Sets

Een PSET moet in iedere uitvoervorm dezelfde probleemstructuur behouden.

Typische onderdelen zijn:

- titel;
- badges;
- leerdoelen;
- probleem;
- demo;
- Understanding;
- opdracht;
- specificatie;
- hints;
- testen;
- inleveren.

Niet iedere PSET hoeft exact dezelfde tussenkoppen te hebben wanneer de
inhoud daar niet om vraagt.

De broninhoud blijft leidend; de renderer verandert presentatie, geen
didactische betekenis.


## 14. Weekpagina's

Weekpagina's hebben primair een organiserende functie.

Zij verbinden:

- de weekvraag;
- Thinking Set;
- klassikale activiteiten;
- Problem Set;
- Understanding;
- planning / deadlines.

Een weekpagina hoeft daarom niet automatisch dezelfde interne
architectuur te krijgen als Understanding, PSET of TSET.

In de complete Module-PDF vormt de weekopening samen met de bijbehorende
Thinking Set het begin van een week. Daarna volgen de PSET-index en de
bijbehorende Problem Sets.

De renderer bepaalt welke web-only presentatie uit de weekpagina wordt
weggelaten of vervangen.


## 15. Web-only presentatie

Onderstaande elementen zijn presentatie en worden niet letterlijk naar
PDF gekopieerd:

- webnavigatie;
- hover-effecten;
- open/dicht-status van details;
- embedded players;
- interactieve controls;
- localhost- of site-URL's als primaire navigatiemethode.

De onderliggende inhoud of functie blijft wel beschikbaar via een
PDF-passende vorm.


## 16. PDF-only presentatie

PDF mag specifieke presentatie-elementen toevoegen zonder een tweede
inhoudsbron te creëren.

Voorbeelden:

- dezelfde visuele badges als op de website, aangepast aan print/PDF;
- QR-codes;
- paginanummers;
- "Zie Understanding, p. …";
- printvriendelijke hintkaders;
- page breaks;
- kop- en voetteksten;
- inhoudsopgave;
- interne PDF-links.


## 17. Geen duplicatie van onderwijsinhoud

Maak geen bestanden zoals:

    jellybeans-web.md
    jellybeans-pdf.md

wanneer het inhoudelijke verschil alleen door het medium ontstaat.

Gebruik één bron en laat de renderer beslissen hoe onderdelen worden
weergegeven.


## 18. Data buiten de onderwijsinhoud

Veranderlijke of presentatie-afhankelijke gegevens worden waar mogelijk
centraal opgeslagen.

Voorbeelden:

- deadlines;
- Understanding-catalogus;
- gegenereerde Understanding-paginanummers;
- resourcecatalogus en resourcegroepen;
- multimedia-URL's;
- QR-doelen;
- eventueel documentmetadata.

Dit sluit aan op de bestaande werkwijze waarbij data zoals deadlines
via YAML in pagina's kan worden ingevoegd.


## 19. Gerealiseerde architectuur en vervolg

De oorspronkelijke referentie-implementatie is inmiddels doorontwikkeld
tot een werkende complete Module-PDF-pipeline.

Gerealiseerd:

1. Weekopeningen, Thinking Sets, PSET-indexen en Problem Sets worden uit
   dezelfde Markdown-bronnen samengesteld.
2. Understanding wordt centraal geregistreerd met stabiele IDs.
3. De Module-PDF gebruikt automatisch gegenereerde Understanding-
   paginaverwijzingen.
4. Mermaid-broncode wordt tijdens de build naar gedeelde PNG-assets
   gerenderd.
5. Video en andere geschikte resources kunnen via centrale IDs worden
   verwerkt en in PDF een passende QR-presentatie krijgen.
6. Hints blijven één inhoudsbron: uitklapbaar op web, volledig zichtbaar
   in PDF.
7. Badges blijven visueel herkenbaar in de PDF.
8. De complete Module-PDF wordt via een eigen renderpipeline samengesteld.
9. De website blijft vanuit dezelfde bronnen met MkDocs gebouwd.

Vervolgwerk wordt alleen aan dit contract toegevoegd wanneer een nieuwe
uitvoervorm of renderregel daadwerkelijk wordt ontworpen of gerealiseerd.

Losse PSET/TSET-PDF's en eventuele afzonderlijke Understanding-PDF's
blijven aparte uitvoervormen; hun precieze implementatie hoeft de
Module-PDF-architectuur niet te dupliceren.


## 20. Ontwerpcontrole

Controleer bij iedere wijziging:

- [ ] Is er nog steeds één inhoudsbron?
- [ ] Werkt de inhoud op de website?
- [ ] Kan dezelfde inhoud in een losse PDF worden gebruikt?
- [ ] Kan dezelfde inhoud zonder duplicatie in de Module-PDF worden gebruikt?
- [ ] Wordt Understanding in een losse PSET/TSET-PDF inline opgenomen?
- [ ] Wordt Understanding in de Module-PDF via een cross-reference weergegeven?
- [ ] Zijn paginanummers niet hardcoded in onderwijsinhoud?
- [ ] Worden resources via stabiele IDs en centrale data beheerd?
- [ ] Wordt multimedia op web embedded en in PDF passend via QR aangeboden?
- [ ] Gebruiken Mermaid-diagrammen één bron en gegenereerde gedeelde assets?
- [ ] Blijven badges herkenbaar in web én PDF?
- [ ] Blijven hints inhoudelijk identiek?
- [ ] Blijft een TSET productieve worsteling ondersteunen?
- [ ] Worden web-only presentatie-elementen niet als inhoud behandeld?
- [ ] Zijn toekomstige PDF-specifieke keuzes in renderer/data geplaatst in plaats van in dubbele onderwijsbestanden?
