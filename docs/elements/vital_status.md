---
search:
  boost: 5.0
---

# Slot: Vital Status (vital_status) 


_Whether participant is alive or dead_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:vital_status](https://w3id.org/anvilproject/acr-harmonized-data-model/vital_status)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Demographics](Demographics.md) | Basic participant demographics summary |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumVitalStatus](EnumVitalStatus.md)&nbsp;or&nbsp;<br />[EnumUnknown](EnumUnknown.md) |
| Domain Of | [Demographics](Demographics.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'EnumVitalStatus'})
- AnonymousSlotExpression({'range': 'EnumUnknown'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:vital_status |
| native | acr_harmonized_data_model:vital_status |




## LinkML Source

<details>
```yaml
name: vital_status
description: Whether participant is alive or dead
title: Vital Status
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Demographics
range: Concept
any_of:
- range: EnumVitalStatus
- range: EnumUnknown

```
</details></div>