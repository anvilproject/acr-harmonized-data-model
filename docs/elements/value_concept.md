---
search:
  boost: 5.0
---



# Slot: Value concept (value_concept) 


_The structured term defining the value of the assertion._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:value_concept](https://w3id.org/anvilproject/acr-harmonized-data-model/value_concept)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumPresentAbsent](EnumPresentAbsent.md) |
| Domain Of | [SubjectAssertion](SubjectAssertion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:value_concept |
| native | acr_harmonized_data_model:value_concept |




## LinkML Source

<details>
```yaml
name: value_concept
description: The structured term defining the value of the assertion.
title: Value concept
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- SubjectAssertion
range: Concept
multivalued: true
any_of:
- range: Concept
- range: EnumPresentAbsent

```
</details></div>