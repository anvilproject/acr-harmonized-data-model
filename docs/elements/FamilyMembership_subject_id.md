---
search:
  boost: 5.0
---

# Slot: Study ID (FamilyMembership_subject_id) 


_INCLUDE Global ID for the Subject_



<div data-search-exclude markdown="1">



URI: [cam:subject_id](https://includedcc.org/common-access-model/subject_id)
Alias: subject_id


## Inheritance

* [subject_id](subject_id.md)
    * **FamilyMembership_subject_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilyMembership](FamilyMembership.md) | Designates a Subject as a member of a family with a specified role |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subject](Subject.md) |
| Domain | [FamilyMembership](FamilyMembership.md) |
| Domain Of | [FamilyMembership](FamilyMembership.md) |
| Slot URI | [cam:subject_id](https://includedcc.org/common-access-model/subject_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FamilyMembership](FamilyMembership.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | subject_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:subject_id |
| native | acr_harmonized_data_model:FamilyMembership_subject_id |




## LinkML Source

<details>
```yaml
name: FamilyMembership_subject_id
definition_uri: https://includedcc.org/common-access-model/subject_id
description: INCLUDE Global ID for the Subject
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: subject_id
domain: FamilyMembership
slot_uri: cam:subject_id
alias: subject_id
owner: FamilyMembership
domain_of:
- FamilyMembership
is_usage_slot: true
usage_slot_name: subject_id
range: Subject
required: true
multivalued: false

```
</details></div>