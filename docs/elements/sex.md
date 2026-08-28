---
search:
  boost: 5.0
---



# Slot: Sex (sex) 


_Sex of Participant_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:sex](https://w3id.org/anvilproject/acr-harmonized-data-model/sex)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Demographics](Demographics.md) | Basic participant demographics summary |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EnumSex](EnumSex.md)&nbsp;or&nbsp;<br />[EnumUnknownOther](EnumUnknownOther.md) |
| Domain Of | [Demographics](Demographics.md) |

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
| self | acr_harmonized_data_model:sex |
| native | acr_harmonized_data_model:sex |




## LinkML Source

<details>
```yaml
name: sex
description: Sex of Participant
title: Sex
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Demographics
range: Concept
required: true
any_of:
- range: EnumSex
- range: EnumUnknownOther

```
</details></div>