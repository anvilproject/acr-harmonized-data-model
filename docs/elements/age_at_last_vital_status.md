---
search:
  boost: 5.0
---

# Slot: Age at Last Vital Status (age_at_last_vital_status) 


_Age in days when participant's vital status was last recorded_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:age_at_last_vital_status](https://w3id.org/anvilproject/acr-harmonized-data-model/age_at_last_vital_status)
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
| self | acr_harmonized_data_model:age_at_last_vital_status |
| native | acr_harmonized_data_model:age_at_last_vital_status |




## LinkML Source

<details>
```yaml
name: age_at_last_vital_status
description: Age in days when participant's vital status was last recorded
title: Age at Last Vital Status
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