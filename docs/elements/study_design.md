---
search:
  boost: 5.0
---



# Slot: Study Design (study_design) 


_Overall design of study, including whether it is longitudinal and whether family members/unrelated controls are also enrolled_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:study_design](https://w3id.org/anvilproject/acr-harmonized-data-model/study_design)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumStudyDesign](EnumStudyDesign.md) |
| Domain Of | [StudyMetadata](StudyMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:study_design |
| native | acr_harmonized_data_model:study_design |




## LinkML Source

<details>
```yaml
name: study_design
description: Overall design of study, including whether it is longitudinal and whether
  family members/unrelated controls are also enrolled
title: Study Design
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- StudyMetadata
range: Concept
required: true
multivalued: true
any_of:
- range: Concept
- range: EnumStudyDesign

```
</details></div>