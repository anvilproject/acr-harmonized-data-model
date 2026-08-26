---
search:
  boost: 5.0
---

# Slot: Ethnicity (ethnicity) 


_Ethnicity of Participant_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:ethnicity](https://w3id.org/anvilproject/acr-harmonized-data-model/ethnicity)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Demographics](Demographics.md) | Basic participant demographics summary |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumEthnicity](EnumEthnicity.md)&nbsp;or&nbsp;<br />[EnumUnknownOther](EnumUnknownOther.md) |
| Domain Of | [Demographics](Demographics.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'EnumEthnicity'})
- AnonymousSlotExpression({'range': 'EnumUnknownOther'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:ethnicity |
| native | acr_harmonized_data_model:ethnicity |




## LinkML Source

<details>
```yaml
name: ethnicity
description: Ethnicity of Participant
title: Ethnicity
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Demographics
range: Concept
required: true
any_of:
- range: EnumEthnicity
- range: EnumUnknownOther

```
</details></div>