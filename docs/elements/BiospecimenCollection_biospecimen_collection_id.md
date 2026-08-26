---
search:
  boost: 5.0
---

# Slot: Biospecimen Collection ID (BiospecimenCollection_biospecimen_collection_id) 


_Unique identifier for this Biospecimen Collection._



<div data-search-exclude markdown="1">



URI: [cam:biospecimen_collection_id](https://includedcc.org/common-access-model/biospecimen_collection_id)
Alias: biospecimen_collection_id


## Inheritance

* [biospecimen_collection_id](biospecimen_collection_id.md)
    * **BiospecimenCollection_biospecimen_collection_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [BiospecimenCollection](BiospecimenCollection.md) |
| Domain Of | [BiospecimenCollection](BiospecimenCollection.md) |
| Slot URI | [cam:biospecimen_collection_id](https://includedcc.org/common-access-model/biospecimen_collection_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [BiospecimenCollection](BiospecimenCollection.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | biospecimen_collection_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:biospecimen_collection_id |
| native | acr_harmonized_data_model:BiospecimenCollection_biospecimen_collection_id |




## LinkML Source

<details>
```yaml
name: BiospecimenCollection_biospecimen_collection_id
definition_uri: https://includedcc.org/common-access-model/biospecimen_collection_id
description: Unique identifier for this Biospecimen Collection.
title: Biospecimen Collection ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: biospecimen_collection_id
domain: BiospecimenCollection
slot_uri: cam:biospecimen_collection_id
identifier: true
alias: biospecimen_collection_id
owner: BiospecimenCollection
domain_of:
- BiospecimenCollection
is_usage_slot: true
usage_slot_name: biospecimen_collection_id
range: string
required: true

```
</details></div>