---
search:
  boost: 5.0
---

# Slot: Bibiliographic Reference (bibliographic_reference) 


_Text use to reference this Record._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:bibliographic_reference](https://w3id.org/anvilproject/acr-harmonized-data-model/bibliographic_reference)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DOI](DOI.md) | A DOI is a permanent reference with metadata about a digital object |  no  |
| [Publication](Publication.md) | Information about a specific publication |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [DOI](DOI.md), [Publication](Publication.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:bibliographic_reference |
| native | acr_harmonized_data_model:bibliographic_reference |




## LinkML Source

<details>
```yaml
name: bibliographic_reference
description: Text use to reference this Record.
title: Bibiliographic Reference
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- DOI
- Publication
range: string

```
</details></div>