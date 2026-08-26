---
search:
  boost: 5.0
---

# Slot: File ID (File_file_id) 


_Unique identifier for this File._



<div data-search-exclude markdown="1">



URI: [cam:file_id](https://includedcc.org/common-access-model/file_id)
Alias: file_id


## Inheritance

* [file_id](file_id.md)
    * **File_file_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | File |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [DrGlobalID](DrGlobalID.md) |
| Domain | [File](File.md) |
| Domain Of | [File](File.md) |
| Slot URI | [cam:file_id](https://includedcc.org/common-access-model/file_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [File](File.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | file_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:file_id |
| native | acr_harmonized_data_model:File_file_id |




## LinkML Source

<details>
```yaml
name: File_file_id
definition_uri: https://includedcc.org/common-access-model/file_id
description: Unique identifier for this File.
title: File ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: file_id
domain: File
slot_uri: cam:file_id
identifier: true
alias: file_id
owner: File
domain_of:
- File
is_usage_slot: true
usage_slot_name: file_id
range: drGlobalID
required: true

```
</details></div>