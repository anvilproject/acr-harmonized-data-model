---
search:
  boost: 5.0
---

# Slot: Virtual Biorepository (VirtualBiorepository_vbr_id) 


_Information about the study's Virtual Biorepository, if participating_



<div data-search-exclude markdown="1">



URI: [cam:vbr_id](https://includedcc.org/common-access-model/vbr_id)
Alias: vbr_id


## Inheritance

* [vbr_id](vbr_id.md)
    * **VirtualBiorepository_vbr_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [VirtualBiorepository](VirtualBiorepository.md) | An organization that can provide access to specimen for further analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [OrGlobalID](OrGlobalID.md) |
| Domain | [VirtualBiorepository](VirtualBiorepository.md) |
| Domain Of | [VirtualBiorepository](VirtualBiorepository.md) |
| Slot URI | [cam:vbr_id](https://includedcc.org/common-access-model/vbr_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [VirtualBiorepository](VirtualBiorepository.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | vbr_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:vbr_id |
| native | acr_harmonized_data_model:VirtualBiorepository_vbr_id |




## LinkML Source

<details>
```yaml
name: VirtualBiorepository_vbr_id
definition_uri: https://includedcc.org/common-access-model/vbr_id
description: Information about the study's Virtual Biorepository, if participating
title: Virtual Biorepository
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: vbr_id
domain: VirtualBiorepository
slot_uri: cam:vbr_id
identifier: true
alias: vbr_id
owner: VirtualBiorepository
domain_of:
- VirtualBiorepository
is_usage_slot: true
usage_slot_name: vbr_id
range: orGlobalID
required: true

```
</details></div>