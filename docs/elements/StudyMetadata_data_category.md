---
search:
  boost: 5.0
---

# Slot: Data Category (StudyMetadata_data_category) 


_General category of data in this Record (e.g. Clinical, Genomics, etc)_



<div data-search-exclude markdown="1">



URI: [cam:data_category](https://includedcc.org/common-access-model/data_category)
Alias: data_category


## Inheritance

* [data_category](data_category.md)
    * **StudyMetadata_data_category**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumDataCategory](EnumDataCategory.md) |
| Domain | [StudyMetadata](StudyMetadata.md) |
| Domain Of | [StudyMetadata](StudyMetadata.md) |
| Slot URI | [cam:data_category](https://includedcc.org/common-access-model/data_category) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [StudyMetadata](StudyMetadata.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | data_category |


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
| self | cam:data_category |
| native | acr_harmonized_data_model:StudyMetadata_data_category |




## LinkML Source

<details>
```yaml
name: StudyMetadata_data_category
definition_uri: https://includedcc.org/common-access-model/data_category
description: General category of data in this Record (e.g. Clinical, Genomics, etc)
title: Data Category
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: data_category
domain: StudyMetadata
slot_uri: cam:data_category
alias: data_category
owner: StudyMetadata
domain_of:
- StudyMetadata
is_usage_slot: true
usage_slot_name: data_category
range: Concept
required: true
multivalued: true
any_of:
- range: Concept
- range: EnumDataCategory

```
</details></div>