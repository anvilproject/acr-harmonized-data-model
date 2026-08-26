---
search:
  boost: 5.0
---

# Slot: relation 


_Code definting the relationship predicate. Relationship of the "Family Member" to the "Subject", eg, mother of. Ideally uses KIN ontology._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:relation](https://w3id.org/anvilproject/acr-harmonized-data-model/relation)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilyRelationship](FamilyRelationship.md) | A relationship between two Subjects |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumFamilyRelation](EnumFamilyRelation.md)&nbsp;or&nbsp;<br />[EnumUnknown](EnumUnknown.md) |
| Domain Of | [FamilyRelationship](FamilyRelationship.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'EnumFamilyRelation'})
- AnonymousSlotExpression({'range': 'EnumUnknown'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:relation |
| native | acr_harmonized_data_model:relation |




## LinkML Source

<details>
```yaml
name: relation
description: Code definting the relationship predicate. Relationship of the "Family
  Member" to the "Subject", eg, mother of. Ideally uses KIN ontology.
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- FamilyRelationship
range: Concept
required: true
any_of:
- range: EnumFamilyRelation
- range: EnumUnknown

```
</details></div>