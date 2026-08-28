---
search:
  boost: 5.0
---



# Slot: Institution (institution) 


_Name of the institution this record is associated with._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:institution](https://w3id.org/anvilproject/acr-harmonized-data-model/institution)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirtualBiorepository](VirtualBiorepository.md) | An organization that can provide access to specimen for further analysis |  no  |
| [Investigator](Investigator.md) | An individual who made contributions to the collection, analysis, or sharing ... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [VirtualBiorepository](VirtualBiorepository.md), [Investigator](Investigator.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:institution |
| native | acr_harmonized_data_model:institution |




## LinkML Source

<details>
```yaml
name: institution
description: Name of the institution this record is associated with.
title: Institution
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- VirtualBiorepository
- Investigator
range: string
required: false

```
</details></div>