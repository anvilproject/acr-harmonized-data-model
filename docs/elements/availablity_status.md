---
search:
  boost: 5.0
---

# Slot: Sample Availability (availablity_status) 


_Can this Sample be requested for further analysis?_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:availablity_status](https://w3id.org/anvilproject/acr-harmonized-data-model/availablity_status)
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
| Range | [EnumAvailabilityStatus](EnumAvailabilityStatus.md) |
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
| self | acr_harmonized_data_model:availablity_status |
| native | acr_harmonized_data_model:availablity_status |




## LinkML Source

<details>
```yaml
name: availablity_status
description: Can this Sample be requested for further analysis?
title: Sample Availability
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Sample
- Aliquot
range: EnumAvailabilityStatus

```
</details></div>