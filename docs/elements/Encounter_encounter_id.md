---
search:
  boost: 5.0
---

# Slot: Encounter ID (Encounter_encounter_id) 


_Unique identifier for this Encounter._



<div data-search-exclude markdown="1">



URI: [cam:encounter_id](https://includedcc.org/common-access-model/encounter_id)
Alias: encounter_id


## Inheritance

* [encounter_id](encounter_id.md)
    * **Encounter_encounter_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Encounter](Encounter.md) | An event at which data was collected about a participant, an intervention was... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EnGlobalID](EnGlobalID.md) |
| Domain | [Encounter](Encounter.md) |
| Domain Of | [Encounter](Encounter.md) |
| Slot URI | [cam:encounter_id](https://includedcc.org/common-access-model/encounter_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Encounter](Encounter.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | encounter_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:encounter_id |
| native | acr_harmonized_data_model:Encounter_encounter_id |




## LinkML Source

<details>
```yaml
name: Encounter_encounter_id
definition_uri: https://includedcc.org/common-access-model/encounter_id
description: Unique identifier for this Encounter.
title: Encounter ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: encounter_id
domain: Encounter
slot_uri: cam:encounter_id
identifier: true
alias: encounter_id
owner: Encounter
domain_of:
- Encounter
is_usage_slot: true
usage_slot_name: encounter_id
range: enGlobalID
required: true

```
</details></div>