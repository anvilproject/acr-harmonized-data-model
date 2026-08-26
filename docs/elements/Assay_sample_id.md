---
search:
  boost: 5.0
---

# Slot: Sample ID (Assay_sample_id) 


_The unique identifier for this Sample._



<div data-search-exclude markdown="1">



URI: [cam:sample_id](https://includedcc.org/common-access-model/sample_id)
Alias: sample_id


## Inheritance

* [sample_id](sample_id.md)
    * **Assay_sample_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sample](Sample.md) |
| Domain | [Assay](Assay.md) |
| Domain Of | [Assay](Assay.md) |
| Slot URI | [cam:sample_id](https://includedcc.org/common-access-model/sample_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Assay](Assay.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | sample_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:sample_id |
| native | acr_harmonized_data_model:Assay_sample_id |




## LinkML Source

<details>
```yaml
name: Assay_sample_id
definition_uri: https://includedcc.org/common-access-model/sample_id
description: The unique identifier for this Sample.
title: Sample ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: sample_id
domain: Assay
slot_uri: cam:sample_id
alias: sample_id
owner: Assay
domain_of:
- Assay
is_usage_slot: true
usage_slot_name: sample_id
range: Sample
multivalued: true

```
</details></div>