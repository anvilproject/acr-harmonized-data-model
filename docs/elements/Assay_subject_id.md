---
search:
  boost: 5.0
---

# Slot: Study ID (Assay_subject_id) 


_INCLUDE Global ID for the Subject_



<div data-search-exclude markdown="1">



URI: [cam:subject_id](https://includedcc.org/common-access-model/subject_id)
Alias: subject_id


## Inheritance

* [subject_id](subject_id.md)
    * **Assay_subject_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subject](Subject.md) |
| Domain | [Assay](Assay.md) |
| Domain Of | [Assay](Assay.md) |
| Slot URI | [cam:subject_id](https://includedcc.org/common-access-model/subject_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Assay](Assay.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | subject_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:subject_id |
| native | acr_harmonized_data_model:Assay_subject_id |




## LinkML Source

<details>
```yaml
name: Assay_subject_id
definition_uri: https://includedcc.org/common-access-model/subject_id
description: INCLUDE Global ID for the Subject
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: subject_id
domain: Assay
slot_uri: cam:subject_id
alias: subject_id
owner: Assay
domain_of:
- Assay
is_usage_slot: true
usage_slot_name: subject_id
range: Subject
multivalued: true

```
</details></div>