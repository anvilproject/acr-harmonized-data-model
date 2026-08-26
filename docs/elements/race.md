---
search:
  boost: 5.0
---

# Slot: Race (race) 


_Race of Participant_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:race](https://w3id.org/anvilproject/acr-harmonized-data-model/race)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Demographics](Demographics.md) | Basic participant demographics summary |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumRace](EnumRace.md)&nbsp;or&nbsp;<br />[EnumUnknownOther](EnumUnknownOther.md) |
| Domain Of | [Demographics](Demographics.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'EnumRace'})
- AnonymousSlotExpression({'range': 'EnumUnknownOther'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:race |
| native | acr_harmonized_data_model:race |




## LinkML Source

<details>
```yaml
name: race
description: Race of Participant
title: Race
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Demographics
range: Concept
required: true
multivalued: true
any_of:
- range: EnumRace
- range: EnumUnknownOther

```
</details></div>