---
search:
  boost: 5.0
---



# Slot: Encounter Definition ID (encounter_definition_id) 


_Unique identifier for this Encounter Definition._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:encounter_definition_id](https://w3id.org/anvilproject/acr-harmonized-data-model/encounter_definition_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](Encounter.md) | An event at which data was collected about a participant, an intervention was... |  no  |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EncounterDefinition](EncounterDefinition.md) |
| Domain Of | [Encounter](Encounter.md), [EncounterDefinition](EncounterDefinition.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:encounter_definition_id |
| native | acr_harmonized_data_model:encounter_definition_id |




## LinkML Source

<details>
```yaml
name: encounter_definition_id
description: Unique identifier for this Encounter Definition.
title: Encounter Definition ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Encounter
- EncounterDefinition
range: EncounterDefinition

```
</details></div>