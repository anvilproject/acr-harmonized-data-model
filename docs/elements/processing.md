---
search:
  boost: 5.0
---



# Slot: Sample Processing (processing) 


_Processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample. OBI is recommended._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:processing](https://w3id.org/anvilproject/acr-harmonized-data-model/processing)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [Sample](Sample.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:processing |
| native | acr_harmonized_data_model:processing |




## LinkML Source

<details>
```yaml
name: processing
description: Processing that was applied to the Parent Sample or from the Biospecimen
  Collection that yielded this distinct sample. OBI is recommended.
title: Sample Processing
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Sample
range: uriorcurie
multivalued: true

```
</details></div>