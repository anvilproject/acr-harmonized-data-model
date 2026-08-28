---
search:
  boost: 5.0
---



# Slot: File ID (file_id) 


_Unique identifier for this File._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:file_id](https://w3id.org/anvilproject/acr-harmonized-data-model/file_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [File](File.md) | File |  yes  |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  yes  |
| [Dataset](Dataset.md) | Set of files grouped together for release |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [File](File.md) |
| Domain Of | [File](File.md), [Assay](Assay.md), [Dataset](Dataset.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:file_id |
| native | acr_harmonized_data_model:file_id |




## LinkML Source

<details>
```yaml
name: file_id
description: Unique identifier for this File.
title: File ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- File
- Assay
- Dataset
range: File

```
</details></div>