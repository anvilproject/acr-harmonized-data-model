---
search:
  boost: 5.0
---



# Slot: Sample ID (sample_id) 


_The unique identifier for this Sample._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:sample_id](https://w3id.org/anvilproject/acr-harmonized-data-model/sample_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |  yes  |
| [Aliquot](Aliquot.md) | A specific tube or amount of a biospecimen associated with a Sample |  no  |
| [File](File.md) | File |  yes  |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Sample](Sample.md) |
| Domain Of | [Sample](Sample.md), [Aliquot](Aliquot.md), [File](File.md), [Assay](Assay.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:sample_id |
| native | acr_harmonized_data_model:sample_id |




## LinkML Source

<details>
```yaml
name: sample_id
description: The unique identifier for this Sample.
title: Sample ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Sample
- Aliquot
- File
- Assay
range: Sample

```
</details></div>