---
search:
  boost: 5.0
---

# Slot: Clinical Data Source Type (clinical_data_source_type) 


_Source(s) of data collected from study participants_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:clinical_data_source_type](https://w3id.org/anvilproject/acr-harmonized-data-model/clinical_data_source_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EnumDataSourceType](EnumDataSourceType.md) |
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
| self | acr_harmonized_data_model:clinical_data_source_type |
| native | acr_harmonized_data_model:clinical_data_source_type |




## LinkML Source

<details>
```yaml
name: clinical_data_source_type
description: Source(s) of data collected from study participants
title: Clinical Data Source Type
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- StudyMetadata
range: EnumDataSourceType
required: true
multivalued: true

```
</details></div>