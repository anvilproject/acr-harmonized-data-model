---
search:
  boost: 5.0
---

# Slot: DOI (DOI_do_id) 


_Digital Object Identifier (DOI) for this Record._



<div data-search-exclude markdown="1">



URI: [cam:do_id](https://includedcc.org/common-access-model/do_id)
Alias: do_id


## Inheritance

* [do_id](do_id.md)
    * **DOI_do_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DOI](DOI.md) | A DOI is a permanent reference with metadata about a digital object |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain | [DOI](DOI.md) |
| Domain Of | [DOI](DOI.md) |
| Slot URI | [cam:do_id](https://includedcc.org/common-access-model/do_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [DOI](DOI.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | do_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:do_id |
| native | acr_harmonized_data_model:DOI_do_id |




## LinkML Source

<details>
```yaml
name: DOI_do_id
definition_uri: https://includedcc.org/common-access-model/do_id
description: Digital Object Identifier (DOI) for this Record.
title: DOI
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: do_id
domain: DOI
slot_uri: cam:do_id
identifier: true
alias: do_id
owner: DOI
domain_of:
- DOI
is_usage_slot: true
usage_slot_name: do_id
range: string
required: true
multivalued: false

```
</details></div>