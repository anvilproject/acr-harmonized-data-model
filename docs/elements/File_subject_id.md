---
search:
  boost: 5.0
---

# Slot: Study ID (File_subject_id) 


_INCLUDE Global ID for the Subject_



<div data-search-exclude markdown="1">



URI: [cam:subject_id](https://includedcc.org/common-access-model/subject_id)
Alias: subject_id


## Inheritance

* [subject_id](subject_id.md)
    * **File_subject_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | File |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subject](Subject.md) |
| Domain | [File](File.md) |
| Domain Of | [File](File.md) |
| Slot URI | [cam:subject_id](https://includedcc.org/common-access-model/subject_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [File](File.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | subject_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:subject_id |
| native | acr_harmonized_data_model:File_subject_id |




## LinkML Source

<details>
```yaml
name: File_subject_id
definition_uri: https://includedcc.org/common-access-model/subject_id
description: INCLUDE Global ID for the Subject
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: subject_id
domain: File
slot_uri: cam:subject_id
alias: subject_id
owner: File
domain_of:
- File
is_usage_slot: true
usage_slot_name: subject_id
range: Subject
multivalued: true

```
</details></div>