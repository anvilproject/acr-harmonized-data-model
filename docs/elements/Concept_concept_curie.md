---
search:
  boost: 5.0
---

# Slot: Concept Curie (Concept_concept_curie) 


_The standardized curie for the term._



<div data-search-exclude markdown="1">



URI: [cam:concept_curie](https://includedcc.org/common-access-model/concept_curie)
Alias: concept_curie


## Inheritance

* [concept_curie](concept_curie.md)
    * **Concept_concept_curie**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Concept](Concept.md) | A standardized concept with display information |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain | [Concept](Concept.md) |
| Domain Of | [Concept](Concept.md) |
| Slot URI | [cam:concept_curie](https://includedcc.org/common-access-model/concept_curie) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Concept](Concept.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | concept_curie |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:concept_curie |
| native | acr_harmonized_data_model:Concept_concept_curie |




## LinkML Source

<details>
```yaml
name: Concept_concept_curie
definition_uri: https://includedcc.org/common-access-model/concept_curie
description: The standardized curie for the term.
title: Concept Curie
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: concept_curie
domain: Concept
slot_uri: cam:concept_curie
identifier: true
alias: concept_curie
owner: Concept
domain_of:
- Concept
is_usage_slot: true
usage_slot_name: concept_curie
range: uriorcurie
required: true

```
</details></div>