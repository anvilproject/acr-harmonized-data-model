---
search:
  boost: 5.0
---



# Slot: Subject Type (subject_type) 


_Type of entity this record represents_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:subject_type](https://w3id.org/anvilproject/acr-harmonized-data-model/subject_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | This entity is the subject about which data or references are recorded |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EnumSubjectType](EnumSubjectType.md)&nbsp;or&nbsp;<br />[EnumUnknownOther](EnumUnknownOther.md) |
| Domain Of | [Subject](Subject.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:subject_type |
| native | acr_harmonized_data_model:subject_type |




## LinkML Source

<details>
```yaml
name: subject_type
description: Type of entity this record represents
title: Subject Type
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Subject
range: Concept
required: true
any_of:
- range: EnumSubjectType
- range: EnumUnknownOther

```
</details></div>