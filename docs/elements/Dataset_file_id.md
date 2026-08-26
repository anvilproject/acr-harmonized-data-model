---
search:
  boost: 5.0
---

# Slot: File ID (Dataset_file_id) 


_The list of files comprising this dataset._



<div data-search-exclude markdown="1">



URI: [cam:file_id](https://includedcc.org/common-access-model/file_id)
Alias: file_id


## Inheritance

* [file_id](file_id.md)
    * **Dataset_file_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Set of files grouped together for release |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [File](File.md) |
| Domain | [Dataset](Dataset.md) |
| Domain Of | [Dataset](Dataset.md) |
| Slot URI | [cam:file_id](https://includedcc.org/common-access-model/file_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Dataset](Dataset.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | file_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:file_id |
| native | acr_harmonized_data_model:Dataset_file_id |




## LinkML Source

<details>
```yaml
name: Dataset_file_id
definition_uri: https://includedcc.org/common-access-model/file_id
description: The list of files comprising this dataset.
title: File ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: file_id
domain: Dataset
slot_uri: cam:file_id
alias: file_id
owner: Dataset
domain_of:
- Dataset
is_usage_slot: true
usage_slot_name: file_id
range: File
multivalued: true

```
</details></div>