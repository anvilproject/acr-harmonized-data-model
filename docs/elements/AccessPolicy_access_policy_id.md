---
search:
  boost: 5.0
---

# Slot: Access Policy ID (AccessPolicy_access_policy_id) 


_Global identifier for the access policy that applies to this row of data._



<div data-search-exclude markdown="1">



URI: [cam:access_policy_id](https://includedcc.org/common-access-model/access_policy_id)
Alias: access_policy_id


## Inheritance

* [access_policy_id](access_policy_id.md)
    * **AccessPolicy_access_policy_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AccessPolicy](AccessPolicy.md) | The access policy that describes the controls around use of data |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [CoGlobalID](CoGlobalID.md) |
| Domain | [AccessPolicy](AccessPolicy.md) |
| Domain Of | [AccessPolicy](AccessPolicy.md) |
| Slot URI | [cam:access_policy_id](https://includedcc.org/common-access-model/access_policy_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [AccessPolicy](AccessPolicy.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | access_policy_id |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:access_policy_id |
| native | acr_harmonized_data_model:AccessPolicy_access_policy_id |




## LinkML Source

<details>
```yaml
name: AccessPolicy_access_policy_id
definition_uri: https://includedcc.org/common-access-model/access_policy_id
description: Global identifier for the access policy that applies to this row of data.
title: Access Policy ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: access_policy_id
domain: AccessPolicy
slot_uri: cam:access_policy_id
identifier: true
alias: access_policy_id
owner: AccessPolicy
domain_of:
- AccessPolicy
is_usage_slot: true
usage_slot_name: access_policy_id
range: coGlobalID
required: true

```
</details></div>