---
search:
  boost: 5.0
---

# Slot: Activity Definition ID (EncounterDefinition_activity_definition_id) 


_Unique identifier for this Activity Definition._



<div data-search-exclude markdown="1">



URI: [cam:activity_definition_id](https://includedcc.org/common-access-model/activity_definition_id)
Alias: activity_definition_id


## Inheritance

* [activity_definition_id](activity_definition_id.md)
    * **EncounterDefinition_activity_definition_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ActivityDefinition](ActivityDefinition.md) |
| Domain | [EncounterDefinition](EncounterDefinition.md) |
| Domain Of | [EncounterDefinition](EncounterDefinition.md) |
| Slot URI | [cam:activity_definition_id](https://includedcc.org/common-access-model/activity_definition_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [EncounterDefinition](EncounterDefinition.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | activity_definition_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:activity_definition_id |
| native | acr_harmonized_data_model:EncounterDefinition_activity_definition_id |




## LinkML Source

<details>
```yaml
name: EncounterDefinition_activity_definition_id
definition_uri: https://includedcc.org/common-access-model/activity_definition_id
description: Unique identifier for this Activity Definition.
title: Activity Definition ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: activity_definition_id
domain: EncounterDefinition
slot_uri: cam:activity_definition_id
alias: activity_definition_id
owner: EncounterDefinition
domain_of:
- EncounterDefinition
is_usage_slot: true
usage_slot_name: activity_definition_id
range: ActivityDefinition
multivalued: true

```
</details></div>