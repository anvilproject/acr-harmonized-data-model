---
search:
  boost: 5.0
---

# Slot: Data Category (data_category) 


_General category of data in this Record (e.g. Clinical, Genomics, etc)_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:data_category](https://w3id.org/anvilproject/acr-harmonized-data-model/data_category)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  yes  |
| [File](File.md) | File |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumDataCategory](EnumDataCategory.md) |
| Domain Of | [StudyMetadata](StudyMetadata.md), [File](File.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'Concept'})
- AnonymousSlotExpression({'range': 'EnumDataCategory'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:data_category |
| native | acr_harmonized_data_model:data_category |




## LinkML Source

<details>
```yaml
name: data_category
description: General category of data in this Record (e.g. Clinical, Genomics, etc)
title: Data Category
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- StudyMetadata
- File
range: Concept
any_of:
- range: Concept
- range: EnumDataCategory

```
</details></div>