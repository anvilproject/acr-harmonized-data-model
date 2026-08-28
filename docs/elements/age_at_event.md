---
search:
  boost: 5.0
---



# Slot: Age at event (age_at_event) 


_The age in days of the Subject at the time point which the assertion describes, eg, age of onset or when a measurement was performed._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:age_at_event](https://w3id.org/anvilproject/acr-harmonized-data-model/age_at_event)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |  no  |
| [Encounter](Encounter.md) | An event at which data was collected about a participant, an intervention was... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [SubjectAssertion](SubjectAssertion.md), [Encounter](Encounter.md) |

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
| self | acr_harmonized_data_model:age_at_event |
| native | acr_harmonized_data_model:age_at_event |




## LinkML Source

<details>
```yaml
name: age_at_event
description: The age in days of the Subject at the time point which the assertion
  describes, eg, age of onset or when a measurement was performed.
title: Age at event
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- SubjectAssertion
- Encounter
range: integer
unit:
  ucum_code: d

```
</details></div>