---
search:
  boost: 5.0
---



# Slot: Age at assertion (age_at_assertion) 


_The age in days of the Subject when the assertion was made._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:age_at_assertion](https://w3id.org/anvilproject/acr-harmonized-data-model/age_at_assertion)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [SubjectAssertion](SubjectAssertion.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Additional Constraints</summary>
**Unit:**

| Property | Value |
| --- | --- |
| ucum_code | d |

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:age_at_assertion |
| native | acr_harmonized_data_model:age_at_assertion |




## LinkML Source

<details>
```yaml
name: age_at_assertion
description: The age in days of the Subject when the assertion was made.
title: Age at assertion
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- SubjectAssertion
range: integer
unit:
  ucum_code: d

```
</details></div>