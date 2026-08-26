---
search:
  boost: 5.0
---

# Slot: Encounter Definition ID (EncounterDefinition_encounter_definition_id) 


_Unique identifier for this Encounter Definition._



<div data-search-exclude markdown="1">



URI: [cam:encounter_definition_id](https://includedcc.org/common-access-model/encounter_definition_id)
Alias: encounter_definition_id


## Inheritance

* [encounter_definition_id](encounter_definition_id.md)
    * **EncounterDefinition_encounter_definition_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [PdGlobalID](PdGlobalID.md) |
| Domain | [EncounterDefinition](EncounterDefinition.md) |
| Domain Of | [EncounterDefinition](EncounterDefinition.md) |
| Slot URI | [cam:encounter_definition_id](https://includedcc.org/common-access-model/encounter_definition_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [EncounterDefinition](EncounterDefinition.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | encounter_definition_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:encounter_definition_id |
| native | acr_harmonized_data_model:EncounterDefinition_encounter_definition_id |




## LinkML Source

<details>
```yaml
name: EncounterDefinition_encounter_definition_id
definition_uri: https://includedcc.org/common-access-model/encounter_definition_id
description: Unique identifier for this Encounter Definition.
title: Encounter Definition ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: encounter_definition_id
domain: EncounterDefinition
slot_uri: cam:encounter_definition_id
identifier: true
alias: encounter_definition_id
owner: EncounterDefinition
domain_of:
- EncounterDefinition
is_usage_slot: true
usage_slot_name: encounter_definition_id
range: pdGlobalID
required: true

```
</details></div>