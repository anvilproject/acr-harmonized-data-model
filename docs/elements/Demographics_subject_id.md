---
search:
  boost: 5.0
---

# Slot: Study ID (Demographics_subject_id) 


_INCLUDE Global ID for the Subject_



<div data-search-exclude markdown="1">



URI: [cam:subject_id](https://includedcc.org/common-access-model/subject_id)
Alias: subject_id


## Inheritance

* [subject_id](subject_id.md)
    * **Demographics_subject_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Demographics](Demographics.md) | Basic participant demographics summary |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subject](Subject.md) |
| Domain | [Demographics](Demographics.md) |
| Domain Of | [Demographics](Demographics.md) |
| Slot URI | [cam:subject_id](https://includedcc.org/common-access-model/subject_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Demographics](Demographics.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | subject_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:subject_id |
| native | acr_harmonized_data_model:Demographics_subject_id |




## LinkML Source

<details>
```yaml
name: Demographics_subject_id
definition_uri: https://includedcc.org/common-access-model/subject_id
description: INCLUDE Global ID for the Subject
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: subject_id
domain: Demographics
slot_uri: cam:subject_id
identifier: true
alias: subject_id
owner: Demographics
domain_of:
- Demographics
is_usage_slot: true
usage_slot_name: subject_id
range: Subject
required: true
multivalued: false

```
</details></div>