---
search:
  boost: 5.0
---

# Slot: Sample ID (Sample_sample_id) 


_The unique identifier for this Sample._



<div data-search-exclude markdown="1">



URI: [cam:sample_id](https://includedcc.org/common-access-model/sample_id)
Alias: sample_id


## Inheritance

* [sample_id](sample_id.md)
    * **Sample_sample_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BsGlobalID](BsGlobalID.md) |
| Domain | [Sample](Sample.md) |
| Domain Of | [Sample](Sample.md) |
| Slot URI | [cam:sample_id](https://includedcc.org/common-access-model/sample_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Sample](Sample.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | sample_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:sample_id |
| native | acr_harmonized_data_model:Sample_sample_id |




## LinkML Source

<details>
```yaml
name: Sample_sample_id
definition_uri: https://includedcc.org/common-access-model/sample_id
description: The unique identifier for this Sample.
title: Sample ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: sample_id
domain: Sample
slot_uri: cam:sample_id
identifier: true
alias: sample_id
owner: Sample
domain_of:
- Sample
is_usage_slot: true
usage_slot_name: sample_id
range: bsGlobalID
required: true

```
</details></div>