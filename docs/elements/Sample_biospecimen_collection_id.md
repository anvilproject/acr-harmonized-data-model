---
search:
  boost: 5.0
---

# Slot: Biospecimen Collection ID (Sample_biospecimen_collection_id) 


_Biospecimen Collection during which this sample was generated._



<div data-search-exclude markdown="1">



URI: [cam:biospecimen_collection_id](https://includedcc.org/common-access-model/biospecimen_collection_id)
Alias: biospecimen_collection_id


## Inheritance

* [biospecimen_collection_id](biospecimen_collection_id.md)
    * **Sample_biospecimen_collection_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiospecimenCollection](BiospecimenCollection.md) |
| Domain | [Sample](Sample.md) |
| Domain Of | [Sample](Sample.md) |
| Slot URI | [cam:biospecimen_collection_id](https://includedcc.org/common-access-model/biospecimen_collection_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [Sample](Sample.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | biospecimen_collection_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:biospecimen_collection_id |
| native | acr_harmonized_data_model:Sample_biospecimen_collection_id |




## LinkML Source

<details>
```yaml
name: Sample_biospecimen_collection_id
definition_uri: https://includedcc.org/common-access-model/biospecimen_collection_id
description: Biospecimen Collection during which this sample was generated.
title: Biospecimen Collection ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: biospecimen_collection_id
domain: Sample
slot_uri: cam:biospecimen_collection_id
alias: biospecimen_collection_id
owner: Sample
domain_of:
- Sample
is_usage_slot: true
usage_slot_name: biospecimen_collection_id
range: BiospecimenCollection

```
</details></div>