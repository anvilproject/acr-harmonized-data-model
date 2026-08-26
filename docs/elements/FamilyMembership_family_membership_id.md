---
search:
  boost: 5.0
---

# Slot: Family Relationship ID (FamilyMembership_family_membership_id) 


_ID for the Family Relationship_



<div data-search-exclude markdown="1">



URI: [cam:family_membership_id](https://includedcc.org/common-access-model/family_membership_id)
Alias: family_membership_id


## Inheritance

* [family_membership_id](family_membership_id.md)
    * **FamilyMembership_family_membership_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilyMembership](FamilyMembership.md) | Designates a Subject as a member of a family with a specified role |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [FamilyMembership](FamilyMembership.md) |
| Domain Of | [FamilyMembership](FamilyMembership.md) |
| Slot URI | [cam:family_membership_id](https://includedcc.org/common-access-model/family_membership_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [FamilyMembership](FamilyMembership.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | family_membership_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:family_membership_id |
| native | acr_harmonized_data_model:FamilyMembership_family_membership_id |




## LinkML Source

<details>
```yaml
name: FamilyMembership_family_membership_id
definition_uri: https://includedcc.org/common-access-model/family_membership_id
description: ID for the Family Relationship
title: Family Relationship ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: family_membership_id
domain: FamilyMembership
slot_uri: cam:family_membership_id
identifier: true
alias: family_membership_id
owner: FamilyMembership
domain_of:
- FamilyMembership
is_usage_slot: true
usage_slot_name: family_membership_id
range: string
required: true

```
</details></div>