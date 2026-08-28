---
search:
  boost: 5.0
---



# Slot: Quantity (quantity_number) 


_The total quantity of the specimen_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:quantity_number](https://w3id.org/anvilproject/acr-harmonized-data-model/quantity_number)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |  no  |
| [Aliquot](Aliquot.md) | A specific tube or amount of a biospecimen associated with a Sample |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Float](Float.md) |
| Domain Of | [Sample](Sample.md), [Aliquot](Aliquot.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:quantity_number |
| native | acr_harmonized_data_model:quantity_number |




## LinkML Source

<details>
```yaml
name: quantity_number
description: The total quantity of the specimen
title: Quantity
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Sample
- Aliquot
range: float

```
</details></div>