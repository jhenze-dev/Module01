---
title: Thinking Set 3 — Guess the Number
template: tset.html
---

# Thinking Set 3 *Guess the Number*

--8<-- "includes/badges.html:ct-algoritmen"
--8<-- "includes/badges.html:process-expressing"

## Waar werk je aan?

In deze Thinking Set werk je aan de volgende leerdoelen:

- Ik kan **beredeneren** hoe stappen en beslissingen logisch met elkaar samenhangen.
- Ik kan **een algoritmische oplossing ontwerpen** voor een probleem.
- Ik kan **een oplossing formuleren** als een geordende reeks stappen en beslissingen.

## De challenge

In de pot zit een onbekend aantal jellybeans.

Na iedere gok kan het antwoord **te hoog**, **te laag** of **precies goed** zijn.

Bij iedere gok is de situatie anders. Om steeds de juiste reactie te geven, moet duidelijk zijn **welke voorwaarden gelden en welke beslissing daarbij hoort**.

**Ontwerp een beslissysteem dat voor iedere mogelijke gok bepaalt welk antwoord gegeven moet worden.**

## Maak je denken zichtbaar

Werk jullie oplossing uit als een **flowchart**.

Een flowchart laat zien welke stappen worden uitgevoerd en waar beslissingen worden genomen.

```mermaid
flowchart TD
    A([Start]) --> B[Stap uitvoeren]
    B --> C{Beslissing}
    C -->|Ja| D[Actie A]
    C -->|Nee| E[Actie B]
    D --> F([Einde])
    E --> F
```

[Meer over flowcharts](../../understanding/visual-first/flowcharts-decisions.md)

## Test jullie oplossing

Geef jullie flowchart aan een andere groep.

Laat hen verschillende situaties door jullie beslissysteem doorlopen.

**Komt het systeem in iedere situatie tot de juiste beslissing?**
