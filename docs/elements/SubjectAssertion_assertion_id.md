---
search:
  boost: 5.0
---

# Slot: Assertion ID (SubjectAssertion_assertion_id) 


_INCLUDE Global ID for the Assertion_



<div data-search-exclude markdown="1">



URI: [cam:assertion_id](https://includedcc.org/common-access-model/assertion_id)
Alias: assertion_id


## Inheritance

* [assertion_id](assertion_id.md)
    * **SubjectAssertion_assertion_id**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md)&nbsp;or&nbsp;<br />[ObGlobalID](ObGlobalID.md)&nbsp;or&nbsp;<br />[DeGlobalID](DeGlobalID.md)&nbsp;or&nbsp;<br />[MsGlobalID](MsGlobalID.md) |
| Domain | [SubjectAssertion](SubjectAssertion.md) |
| Domain Of | [SubjectAssertion](SubjectAssertion.md) |
| Slot URI | [cam:assertion_id](https://includedcc.org/common-access-model/assertion_id) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |
| Owner | [SubjectAssertion](SubjectAssertion.md) |
| Is Usage Slot | Yes |
| Usage Slot Name | assertion_id |


<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'obGlobalID'})
- AnonymousSlotExpression({'range': 'deGlobalID'})
- AnonymousSlotExpression({'range': 'msGlobalID'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cam:assertion_id |
| native | acr_harmonized_data_model:SubjectAssertion_assertion_id |




## LinkML Source

<details>
```yaml
name: SubjectAssertion_assertion_id
definition_uri: https://includedcc.org/common-access-model/assertion_id
description: INCLUDE Global ID for the Assertion
title: Assertion ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: assertion_id
domain: SubjectAssertion
slot_uri: cam:assertion_id
identifier: true
alias: assertion_id
owner: SubjectAssertion
domain_of:
- SubjectAssertion
is_usage_slot: true
usage_slot_name: assertion_id
range: string
required: true
multivalued: false
any_of:
- range: obGlobalID
- range: deGlobalID
- range: msGlobalID

```
</details></div>