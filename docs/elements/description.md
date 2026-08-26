---
search:
  boost: 5.0
---

# Slot: Description (description) 


_Description for this entity._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:description](https://w3id.org/anvilproject/acr-harmonized-data-model/description)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |  no  |
| [ActivityDefinition](ActivityDefinition.md) | A definition of an activity in this study, eg, a biospecimen collection, assa... |  no  |
| [Dataset](Dataset.md) | Set of files grouped together for release |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [EncounterDefinition](EncounterDefinition.md), [ActivityDefinition](ActivityDefinition.md), [Dataset](Dataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:description |
| native | acr_harmonized_data_model:description |




## LinkML Source

<details>
```yaml
name: description
description: Description for this entity.
title: Description
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- EncounterDefinition
- ActivityDefinition
- Dataset
range: string

```
</details></div>