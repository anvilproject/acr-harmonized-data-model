---
search:
  boost: 5.0
---

# Slot: Sample ID (File_sample_id) 


_The unique identifier for this Sample._



<div data-search-exclude markdown="1">



URI: [cam:sample_id](https://includedcc.org/common-access-model/sample_id)
Alias: sample_id


## Inheritance

* [sample_id](sample_id.md)
    * **File_sample_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | File |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sample](Sample.md) |
| Domain | [File](File.md) |
| Domain Of | [File](File.md) |
| Slot URI | [cam:sample_id](https://includedcc.org/common-access-model/sample_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [File](File.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | sample_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:sample_id |
| native | acr_harmonized_data_model:File_sample_id |




## LinkML Source

<details>
```yaml
name: File_sample_id
definition_uri: https://includedcc.org/common-access-model/sample_id
description: The unique identifier for this Sample.
title: Sample ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: sample_id
domain: File
slot_uri: cam:sample_id
alias: sample_id
owner: File
domain_of:
- File
is_usage_slot: true
usage_slot_name: sample_id
range: Sample
multivalued: true

```
</details></div>