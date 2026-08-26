---
search:
  boost: 5.0
---

# Slot: File ID (Assay_file_id) 


_Unique identifier for this File._



<div data-search-exclude markdown="1">



URI: [cam:file_id](https://includedcc.org/common-access-model/file_id)
Alias: file_id


## Inheritance

* [file_id](file_id.md)
    * **Assay_file_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [File](File.md) |
| Domain | [Assay](Assay.md) |
| Domain Of | [Assay](Assay.md) |
| Slot URI | [cam:file_id](https://includedcc.org/common-access-model/file_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Assay](Assay.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | file_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:file_id |
| native | acr_harmonized_data_model:Assay_file_id |




## LinkML Source

<details>
```yaml
name: Assay_file_id
definition_uri: https://includedcc.org/common-access-model/file_id
description: Unique identifier for this File.
title: File ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: file_id
domain: Assay
slot_uri: cam:file_id
alias: file_id
owner: Assay
domain_of:
- Assay
is_usage_slot: true
usage_slot_name: file_id
range: File
multivalued: true

```
</details></div>