---
search:
  boost: 5.0
---



# Slot: Location Laterality (laterality) 


_Laterality that further refine the specific location of biospecimen collection_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:laterality](https://w3id.org/anvilproject/acr-harmonized-data-model/laterality)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumLaterality](EnumLaterality.md) |
| Domain Of | [BiospecimenCollection](BiospecimenCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:laterality |
| native | acr_harmonized_data_model:laterality |




## LinkML Source

<details>
```yaml
name: laterality
description: Laterality that further refine the specific location of biospecimen collection
title: Location Laterality
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- BiospecimenCollection
range: Concept
any_of:
- range: Concept
- range: EnumLaterality

```
</details></div>