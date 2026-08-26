---
search:
  boost: 5.0
---

# Slot: Aliquot ID (Aliquot_aliquot_id) 


_Unique identifier for an Aliquot._



<div data-search-exclude markdown="1">



URI: [cam:aliquot_id](https://includedcc.org/common-access-model/aliquot_id)
Alias: aliquot_id


## Inheritance

* [aliquot_id](aliquot_id.md)
    * **Aliquot_aliquot_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Aliquot](Aliquot.md) | A specific tube or amount of a biospecimen associated with a Sample |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [Aliquot](Aliquot.md) |
| Domain Of | [Aliquot](Aliquot.md) |
| Slot URI | [cam:aliquot_id](https://includedcc.org/common-access-model/aliquot_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Aliquot](Aliquot.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | aliquot_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:aliquot_id |
| native | acr_harmonized_data_model:Aliquot_aliquot_id |




## LinkML Source

<details>
```yaml
name: Aliquot_aliquot_id
definition_uri: https://includedcc.org/common-access-model/aliquot_id
description: Unique identifier for an Aliquot.
title: Aliquot ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: aliquot_id
domain: Aliquot
slot_uri: cam:aliquot_id
identifier: true
alias: aliquot_id
owner: Aliquot
domain_of:
- Aliquot
is_usage_slot: true
usage_slot_name: aliquot_id
range: string
required: true

```
</details></div>