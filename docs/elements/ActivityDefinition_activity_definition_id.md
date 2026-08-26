---
search:
  boost: 5.0
---

# Slot: Activity Definition ID (ActivityDefinition_activity_definition_id) 


_Unique identifier for this Activity Definition._



<div data-search-exclude markdown="1">



URI: [cam:activity_definition_id](https://includedcc.org/common-access-model/activity_definition_id)
Alias: activity_definition_id


## Inheritance

* [activity_definition_id](activity_definition_id.md)
    * **ActivityDefinition_activity_definition_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ActivityDefinition](ActivityDefinition.md) | A definition of an activity in this study, eg, a biospecimen collection, assa... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [AdGlobalID](AdGlobalID.md) |
| Domain | [ActivityDefinition](ActivityDefinition.md) |
| Domain Of | [ActivityDefinition](ActivityDefinition.md) |
| Slot URI | [cam:activity_definition_id](https://includedcc.org/common-access-model/activity_definition_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [ActivityDefinition](ActivityDefinition.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | activity_definition_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:activity_definition_id |
| native | acr_harmonized_data_model:ActivityDefinition_activity_definition_id |




## LinkML Source

<details>
```yaml
name: ActivityDefinition_activity_definition_id
definition_uri: https://includedcc.org/common-access-model/activity_definition_id
description: Unique identifier for this Activity Definition.
title: Activity Definition ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: activity_definition_id
domain: ActivityDefinition
slot_uri: cam:activity_definition_id
identifier: true
alias: activity_definition_id
owner: ActivityDefinition
domain_of:
- ActivityDefinition
is_usage_slot: true
usage_slot_name: activity_definition_id
range: adGlobalID
required: true

```
</details></div>