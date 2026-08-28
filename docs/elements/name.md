---
search:
  boost: 5.0
---



# Slot: Name (name) 


_Name of the entity._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:name](https://w3id.org/anvilproject/acr-harmonized-data-model/name)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirtualBiorepository](VirtualBiorepository.md) | An organization that can provide access to specimen for further analysis |  no  |
| [Investigator](Investigator.md) | An individual who made contributions to the collection, analysis, or sharing ... |  no  |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |  no  |
| [ActivityDefinition](ActivityDefinition.md) | A definition of an activity in this study, eg, a biospecimen collection, assa... |  no  |
| [Dataset](Dataset.md) | Set of files grouped together for release |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [VirtualBiorepository](VirtualBiorepository.md), [Investigator](Investigator.md), [EncounterDefinition](EncounterDefinition.md), [ActivityDefinition](ActivityDefinition.md), [Dataset](Dataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:name |
| native | acr_harmonized_data_model:name |




## LinkML Source

<details>
```yaml
name: name
description: Name of the entity.
title: Name
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- VirtualBiorepository
- Investigator
- EncounterDefinition
- ActivityDefinition
- Dataset
range: string
required: false

```
</details></div>