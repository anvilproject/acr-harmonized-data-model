---
search:
  boost: 5.0
---

# Slot: Study ID (Study_study_id) 


_INCLUDE Global ID for the study_



<div data-search-exclude markdown="1">



URI: [cam:study_id](https://includedcc.org/common-access-model/study_id)
Alias: study_id


## Inheritance

* [study_id](study_id.md)
    * **Study_study_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | Study Metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [SdGlobalID](SdGlobalID.md) |
| Domain | [Study](Study.md) |
| Domain Of | [Study](Study.md) |
| Slot URI | [cam:study_id](https://includedcc.org/common-access-model/study_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Study](Study.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | study_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:study_id |
| native | acr_harmonized_data_model:Study_study_id |




## LinkML Source

<details>
```yaml
name: Study_study_id
definition_uri: https://includedcc.org/common-access-model/study_id
description: INCLUDE Global ID for the study
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: study_id
domain: Study
slot_uri: cam:study_id
identifier: true
alias: study_id
owner: Study
domain_of:
- Study
is_usage_slot: true
usage_slot_name: study_id
range: sdGlobalID
required: true
multivalued: false

```
</details></div>