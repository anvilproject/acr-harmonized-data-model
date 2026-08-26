---
search:
  boost: 5.0
---

# Slot: Family ID (Family_family_id) 


_Global ID for the Family_



<div data-search-exclude markdown="1">



URI: [cam:family_id](https://includedcc.org/common-access-model/family_id)
Alias: family_id


## Inheritance

* [family_id](family_id.md)
    * **Family_family_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Family](Family.md) | A group of individuals of some relation who are grouped together in a study |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [GrGlobalID](GrGlobalID.md) |
| Domain | [Family](Family.md) |
| Domain Of | [Family](Family.md) |
| Slot URI | [cam:family_id](https://includedcc.org/common-access-model/family_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Family](Family.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | family_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:family_id |
| native | acr_harmonized_data_model:Family_family_id |




## LinkML Source

<details>
```yaml
name: Family_family_id
definition_uri: https://includedcc.org/common-access-model/family_id
description: Global ID for the Family
title: Family ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: family_id
domain: Family
slot_uri: cam:family_id
identifier: true
alias: family_id
owner: Family
domain_of:
- Family
is_usage_slot: true
usage_slot_name: family_id
range: grGlobalID
required: true

```
</details></div>