---
search:
  boost: 5.0
---

# Slot: Study ID (FamilyRelationship_subject_id) 


_The family member Subject who is the relationship "object"._



<div data-search-exclude markdown="1">



URI: [cam:subject_id](https://includedcc.org/common-access-model/subject_id)
Alias: subject_id


## Inheritance

* [subject_id](subject_id.md)
    * **FamilyRelationship_subject_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilyRelationship](FamilyRelationship.md) | A relationship between two Subjects |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subject](Subject.md) |
| Domain | [FamilyRelationship](FamilyRelationship.md) |
| Domain Of | [FamilyRelationship](FamilyRelationship.md) |
| Slot URI | [cam:subject_id](https://includedcc.org/common-access-model/subject_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [FamilyRelationship](FamilyRelationship.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | subject_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:subject_id |
| native | acr_harmonized_data_model:FamilyRelationship_subject_id |




## LinkML Source

<details>
```yaml
name: FamilyRelationship_subject_id
definition_uri: https://includedcc.org/common-access-model/subject_id
description: The family member Subject who is the relationship "object".
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: subject_id
domain: FamilyRelationship
slot_uri: cam:subject_id
alias: subject_id
owner: FamilyRelationship
domain_of:
- FamilyRelationship
is_usage_slot: true
usage_slot_name: subject_id
range: Subject
required: true
multivalued: false

```
</details></div>