---
search:
  boost: 2.0
---


# Enum: EnumAsserterType 




_Individuals or organizations making assertions._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumAsserterType](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumAsserterType)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** CAMO:0000015
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| CAMO:0000016 | None | Assertion made by research staff | Title: Research Staff Asserted<br>|
| CAMO:0000017 | None | Assertion documented by a healthcare system or provider | Title: Healthcare Asserted<br>|
| CAMO:0000018 | None | Assertion made by a study participant, their representative, or some combinat... | Title: Participant or Representative Asserted<br>|
| CAMO:0000019 | None | Assertion made by a study participant | Title: Participant Asserted<br>|
| CAMO:0000020 | None | Assertion made by a study participant's representative or representatives | Title: Representative Asserted<br>|
| CAMO:0000021 | None | Assertion made by a study participant's caregiver or caregivers | Title: Caregiver Asserted<br>|




## Slots

| Name | Description |
| ---  | --- |
| [asserter_type](asserter_type.md) | The original asserter of this information |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumAsserterType
description: Individuals or organizations making assertions.
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  CAMO:0000016:
    text: CAMO:0000016
    description: Assertion made by research staff.
    title: Research Staff Asserted
    aliases:
    - investigator_assessment
  CAMO:0000017:
    text: CAMO:0000017
    description: Assertion documented by a healthcare system or provider.
    title: Healthcare Asserted
    aliases:
    - medical_record
  CAMO:0000018:
    text: CAMO:0000018
    description: Assertion made by a study participant, their representative, or some
      combination.
    title: Participant or Representative Asserted
    aliases:
    - participant_or_caregiver_report
  CAMO:0000019:
    text: CAMO:0000019
    description: Assertion made by a study participant.
    title: Participant Asserted
  CAMO:0000020:
    text: CAMO:0000020
    description: Assertion made by a study participant's representative or representatives.
    title: Representative Asserted
  CAMO:0000021:
    text: CAMO:0000021
    description: Assertion made by a study participant's caregiver or caregivers.
    title: Caregiver Asserted
reachable_from:
  source_ontology: camo
  source_nodes:
  - CAMO:0000015
  relationship_types:
  - rdfs:subClassOf
  is_direct: false
  include_self: true

```
</details>

</div>