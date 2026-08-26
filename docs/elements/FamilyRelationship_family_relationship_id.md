---
search:
  boost: 5.0
---

# Slot: Family Relationship ID (FamilyRelationship_family_relationship_id) 


_Global ID for the Family Relationship_



<div data-search-exclude markdown="1">



URI: [cam:family_relationship_id](https://includedcc.org/common-access-model/family_relationship_id)
Alias: family_relationship_id


## Inheritance

* [family_relationship_id](family_relationship_id.md)
    * **FamilyRelationship_family_relationship_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilyRelationship](FamilyRelationship.md) | A relationship between two Subjects |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [FmGlobalID](FmGlobalID.md) |
| Domain | [FamilyRelationship](FamilyRelationship.md) |
| Domain Of | [FamilyRelationship](FamilyRelationship.md) |
| Slot URI | [cam:family_relationship_id](https://includedcc.org/common-access-model/family_relationship_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [FamilyRelationship](FamilyRelationship.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | family_relationship_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:family_relationship_id |
| native | acr_harmonized_data_model:FamilyRelationship_family_relationship_id |




## LinkML Source

<details>
```yaml
name: FamilyRelationship_family_relationship_id
definition_uri: https://includedcc.org/common-access-model/family_relationship_id
description: Global ID for the Family Relationship
title: Family Relationship ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: family_relationship_id
domain: FamilyRelationship
slot_uri: cam:family_relationship_id
identifier: true
alias: family_relationship_id
owner: FamilyRelationship
domain_of:
- FamilyRelationship
is_usage_slot: true
usage_slot_name: family_relationship_id
range: fmGlobalID
required: true

```
</details></div>