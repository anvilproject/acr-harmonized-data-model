---
search:
  boost: 5.0
---

# Slot: research_domain 


_Main research domain(s) of the study_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:research_domain](https://w3id.org/anvilproject/acr-harmonized-data-model/research_domain)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumResearchDomain](EnumResearchDomain.md) |
| Domain Of | [StudyMetadata](StudyMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'Concept'})
- AnonymousSlotExpression({'range': 'EnumResearchDomain'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:research_domain |
| native | acr_harmonized_data_model:research_domain |




## LinkML Source

<details>
```yaml
name: research_domain
description: Main research domain(s) of the study
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- StudyMetadata
range: Concept
required: true
multivalued: true
any_of:
- range: Concept
- range: EnumResearchDomain

```
</details></div>