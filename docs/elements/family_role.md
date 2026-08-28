---
search:
  boost: 5.0
---



# Slot: family_role 


_The "role" of this individual in this family. Could include terms like "proband", "mother", etc._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:family_role](https://w3id.org/anvilproject/acr-harmonized-data-model/family_role)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FamilyMembership](FamilyMembership.md) | Designates a Subject as a member of a family with a specified role |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumFamilyRole](EnumFamilyRole.md) |
| Domain Of | [FamilyMembership](FamilyMembership.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:family_role |
| native | acr_harmonized_data_model:family_role |




## LinkML Source

<details>
```yaml
name: family_role
description: The "role" of this individual in this family. Could include terms like
  "proband", "mother", etc.
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- FamilyMembership
range: Concept
any_of:
- range: Concept
- range: EnumFamilyRole

```
</details></div>