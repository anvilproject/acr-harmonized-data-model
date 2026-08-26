---
search:
  boost: 2.0
---


# Enum: EnumConsanguinityAssertion 




_Asserts known or suspected consanguinity in this study family_



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumConsanguinityAssertion](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumConsanguinityAssertion)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| not_suspected | snomed_ct:428263003 | Not suspected | Title: not-suspected<br>|
| suspected | snomed_ct:415684004 | Suspected | Title: suspected<br>|
| known_present | snomed_ct:410515003 | Known Present | Title: known-present<br>|
| unknown | snomed_ct:261665006 | Unknown | Title: unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [consanguinity](consanguinity.md) | Is there known or suspected consanguinity in this study family? |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumConsanguinityAssertion
description: Asserts known or suspected consanguinity in this study family
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  not_suspected:
    text: not_suspected
    description: Not suspected
    meaning: snomed_ct:428263003
    title: not-suspected
  suspected:
    text: suspected
    description: Suspected
    meaning: snomed_ct:415684004
    title: suspected
  known_present:
    text: known_present
    description: Known Present
    meaning: snomed_ct:410515003
    title: known-present
  unknown:
    text: unknown
    description: Unknown
    meaning: snomed_ct:261665006
    title: unknown

```
</details>

</div>