---
search:
  boost: 5.0
---

# Slot: Spatial Qualifier (spatial_qualifier) 


_Qualifier that further refine the specific location of biospecimen collection_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:spatial_qualifier](https://w3id.org/anvilproject/acr-harmonized-data-model/spatial_qualifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumSpatialQualifiers](EnumSpatialQualifiers.md) |
| Domain Of | [BiospecimenCollection](BiospecimenCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'Concept'})
- AnonymousSlotExpression({'range': 'EnumSpatialQualifiers'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:spatial_qualifier |
| native | acr_harmonized_data_model:spatial_qualifier |




## LinkML Source

<details>
```yaml
name: spatial_qualifier
description: Qualifier that further refine the specific location of biospecimen collection
title: Spatial Qualifier
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- BiospecimenCollection
range: Concept
any_of:
- range: Concept
- range: EnumSpatialQualifiers

```
</details></div>