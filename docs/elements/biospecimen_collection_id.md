---
search:
  boost: 5.0
---

# Slot: Biospecimen Collection ID (biospecimen_collection_id) 


_Unique identifier for this Biospecimen Collection._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:biospecimen_collection_id](https://w3id.org/anvilproject/acr-harmonized-data-model/biospecimen_collection_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |  yes  |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [BiospecimenCollection](BiospecimenCollection.md) |
| Domain Of | [Sample](Sample.md), [BiospecimenCollection](BiospecimenCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:biospecimen_collection_id |
| native | acr_harmonized_data_model:biospecimen_collection_id |




## LinkML Source

<details>
```yaml
name: biospecimen_collection_id
description: Unique identifier for this Biospecimen Collection.
title: Biospecimen Collection ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Sample
- BiospecimenCollection
range: BiospecimenCollection

```
</details></div>