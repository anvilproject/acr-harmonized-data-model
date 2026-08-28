---
search:
  boost: 5.0
---



# Slot: Age at First Participant Engagement (age_at_first_engagement) 


_Age in days of Participant at first recorded study event (enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:age_at_first_engagement](https://w3id.org/anvilproject/acr-harmonized-data-model/age_at_first_engagement)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Demographics](Demographics.md) | Basic participant demographics summary |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Integer](Integer.md) |
| Domain Of | [Demographics](Demographics.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Value Constraints

| Property | Value |
| --- | --- |
| Minimum Value | -365 |
| Maximum Value | 32507 |


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
| self | acr_harmonized_data_model:age_at_first_engagement |
| native | acr_harmonized_data_model:age_at_first_engagement |




## LinkML Source

<details>
```yaml
name: age_at_first_engagement
description: Age in days of Participant at first recorded study event (enrollment,
  visit, observation, sample collection, survey completion, etc.). Age at enrollment
  is preferred, if available.
title: Age at First Participant Engagement
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Demographics
range: integer
minimum_value: -365
maximum_value: 32507
unit:
  ucum_code: d

```
</details></div>