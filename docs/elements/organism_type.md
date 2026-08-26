---
search:
  boost: 5.0
---

# Slot: Organism Type (organism_type) 


_Organism Type, typically from NCBITaxon._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:organism_type](https://w3id.org/anvilproject/acr-harmonized-data-model/organism_type)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | This entity is the subject about which data or references are recorded |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md)&nbsp;or&nbsp;<br />[EnumOrganism](EnumOrganism.md) |
| Domain Of | [Subject](Subject.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'uriorcurie'})
- AnonymousSlotExpression({'range': 'EnumOrganism'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:organism_type |
| native | acr_harmonized_data_model:organism_type |




## LinkML Source

<details>
```yaml
name: organism_type
description: Organism Type, typically from NCBITaxon.
title: Organism Type
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Subject
range: uriorcurie
any_of:
- range: uriorcurie
- range: EnumOrganism

```
</details></div>