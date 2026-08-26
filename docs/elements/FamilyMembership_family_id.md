---
search:
  boost: 5.0
---

# Slot: Family ID (FamilyMembership_family_id) 


_Global ID for the Family_



<div data-search-exclude markdown="1">



URI: [cam:family_id](https://includedcc.org/common-access-model/family_id)
Alias: family_id


## Inheritance

* [family_id](family_id.md)
    * **FamilyMembership_family_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilyMembership](FamilyMembership.md) | Designates a Subject as a member of a family with a specified role |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Family](Family.md) |
| Domain | [FamilyMembership](FamilyMembership.md) |
| Domain Of | [FamilyMembership](FamilyMembership.md) |
| Slot URI | [cam:family_id](https://includedcc.org/common-access-model/family_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FamilyMembership](FamilyMembership.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | family_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:family_id |
| native | acr_harmonized_data_model:FamilyMembership_family_id |




## LinkML Source

<details>
```yaml
name: FamilyMembership_family_id
definition_uri: https://includedcc.org/common-access-model/family_id
description: Global ID for the Family
title: Family ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: family_id
domain: FamilyMembership
slot_uri: cam:family_id
alias: family_id
owner: FamilyMembership
domain_of:
- FamilyMembership
is_usage_slot: true
usage_slot_name: family_id
range: Family
required: true

```
</details></div>