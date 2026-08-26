---
search:
  boost: 5.0
---

# Slot: Dataset ID (Dataset_dataset_id) 


_Unique identifier for a Dataset._



<div data-search-exclude markdown="1">



URI: [cam:dataset_id](https://includedcc.org/common-access-model/dataset_id)
Alias: dataset_id


## Inheritance

* [dataset_id](dataset_id.md)
    * **Dataset_dataset_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Set of files grouped together for release |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [LsGlobalID](LsGlobalID.md) |
| Domain | [Dataset](Dataset.md) |
| Domain Of | [Dataset](Dataset.md) |
| Slot URI | [cam:dataset_id](https://includedcc.org/common-access-model/dataset_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [Dataset](Dataset.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | dataset_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:dataset_id |
| native | acr_harmonized_data_model:Dataset_dataset_id |




## LinkML Source

<details>
```yaml
name: Dataset_dataset_id
definition_uri: https://includedcc.org/common-access-model/dataset_id
description: Unique identifier for a Dataset.
title: Dataset ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: dataset_id
domain: Dataset
slot_uri: cam:dataset_id
identifier: true
alias: dataset_id
owner: Dataset
domain_of:
- Dataset
is_usage_slot: true
usage_slot_name: dataset_id
range: lsGlobalID
required: true

```
</details></div>