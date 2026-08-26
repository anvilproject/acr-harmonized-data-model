---
search:
  boost: 5.0
---

# Slot: Assay Type (Assay_assay_type) 


_The type of assay performed._



<div data-search-exclude markdown="1">



URI: [cam:assay_type](https://includedcc.org/common-access-model/assay_type)
Alias: assay_type


## Inheritance

* [assay_type](assay_type.md)
    * **Assay_assay_type**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EnumAssayType](EnumAssayType.md) |
| Domain | [Assay](Assay.md) |
| Domain Of | [Assay](Assay.md) |
| Slot URI | [cam:assay_type](https://includedcc.org/common-access-model/assay_type) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Assay](Assay.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | assay_type |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:assay_type |
| native | acr_harmonized_data_model:Assay_assay_type |




## LinkML Source

<details>
```yaml
name: Assay_assay_type
definition_uri: https://includedcc.org/common-access-model/assay_type
description: The type of assay performed.
title: Assay Type
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: assay_type
domain: Assay
slot_uri: cam:assay_type
alias: assay_type
owner: Assay
domain_of:
- Assay
is_usage_slot: true
usage_slot_name: assay_type
range: EnumAssayType
required: true

```
</details></div>