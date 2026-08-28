---
search:
  boost: 5.0
---



# Slot: Program (program) 


_Funding source(s) for the study_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:program](https://w3id.org/anvilproject/acr-harmonized-data-model/program)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | Study Metadata |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md)&nbsp;or&nbsp;<br />[EnumProgram](EnumProgram.md) |
| Domain Of | [Study](Study.md) |

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
| self | acr_harmonized_data_model:program |
| native | acr_harmonized_data_model:program |




## LinkML Source

<details>
```yaml
name: program
description: Funding source(s) for the study
title: Program
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Study
range: uriorcurie
required: true
multivalued: true
any_of:
- range: uriorcurie
- range: EnumProgram

```
</details></div>