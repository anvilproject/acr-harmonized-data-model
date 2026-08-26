---
search:
  boost: 5.0
---

# Slot: Assay ID (Assay_assay_id) 


_The unique identifier for the Assay._



<div data-search-exclude markdown="1">



URI: [cam:assay_id](https://includedcc.org/common-access-model/assay_id)
Alias: assay_id


## Inheritance

* [assay_id](assay_id.md)
    * **Assay_assay_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DiGlobalID](DiGlobalID.md) |
| Domain | [Assay](Assay.md) |
| Domain Of | [Assay](Assay.md) |
| Slot URI | [cam:assay_id](https://includedcc.org/common-access-model/assay_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Assay](Assay.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | assay_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:assay_id |
| native | acr_harmonized_data_model:Assay_assay_id |




## LinkML Source

<details>
```yaml
name: Assay_assay_id
definition_uri: https://includedcc.org/common-access-model/assay_id
description: The unique identifier for the Assay.
title: Assay ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: assay_id
domain: Assay
slot_uri: cam:assay_id
identifier: true
alias: assay_id
owner: Assay
domain_of:
- Assay
is_usage_slot: true
usage_slot_name: assay_id
range: diGlobalID
required: true

```
</details></div>