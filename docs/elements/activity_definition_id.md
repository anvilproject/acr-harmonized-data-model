---
search:
  boost: 5.0
---



# Slot: Activity Definition ID (activity_definition_id) 


_Unique identifier for this Activity Definition._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:activity_definition_id](https://w3id.org/anvilproject/acr-harmonized-data-model/activity_definition_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |  yes  |
| [ActivityDefinition](ActivityDefinition.md) | A definition of an activity in this study, eg, a biospecimen collection, assa... |  yes  |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [ActivityDefinition](ActivityDefinition.md) |
| Domain Of | [EncounterDefinition](EncounterDefinition.md), [ActivityDefinition](ActivityDefinition.md), [Assay](Assay.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:activity_definition_id |
| native | acr_harmonized_data_model:activity_definition_id |




## LinkML Source

<details>
```yaml
name: activity_definition_id
description: Unique identifier for this Activity Definition.
title: Activity Definition ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- EncounterDefinition
- ActivityDefinition
- Assay
range: ActivityDefinition

```
</details></div>