---
search:
  boost: 5.0
---

# Slot: Age at Biospecimen Collection (age_at_collection) 


_The age at which this biospecimen was collected in decimal years._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:age_at_collection](https://w3id.org/anvilproject/acr-harmonized-data-model/age_at_collection)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [BiospecimenCollection](BiospecimenCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | a |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:age_at_collection |
| native | acr_harmonized_data_model:age_at_collection |




## LinkML Source

<details>
```yaml
name: age_at_collection
description: The age at which this biospecimen was collected in decimal years.
title: Age at Biospecimen Collection
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- BiospecimenCollection
range: float
unit:
  ucum_code: a

```
</details></div>