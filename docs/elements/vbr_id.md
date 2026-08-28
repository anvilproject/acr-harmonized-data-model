---
search:
  boost: 5.0
---



# Slot: Virtual Biorepository (vbr_id) 


_Information about the study's Virtual Biorepository, if participating_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:vbr_id](https://w3id.org/anvilproject/acr-harmonized-data-model/vbr_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  no  |
| [VirtualBiorepository](VirtualBiorepository.md) | An organization that can provide access to specimen for further analysis |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [VirtualBiorepository](VirtualBiorepository.md) |
| Domain Of | [StudyMetadata](StudyMetadata.md), [VirtualBiorepository](VirtualBiorepository.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:vbr_id |
| native | acr_harmonized_data_model:vbr_id |




## LinkML Source

<details>
```yaml
name: vbr_id
description: Information about the study's Virtual Biorepository, if participating
title: Virtual Biorepository
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- StudyMetadata
- VirtualBiorepository
range: VirtualBiorepository

```
</details></div>