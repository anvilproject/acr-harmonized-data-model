---
search:
  boost: 2.0
---


# Enum: EnumAssertionProvenance 




_Possible data sources for assertions._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumAssertionProvenance](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumAssertionProvenance)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| medical_record | None | Data obtained from a medical record | Title: Medical Record<br>|
| investigator_assessment | None | Data obtained by examination, interview, etc | Title: Investigator Assessment<br>|
| participant_or_caregiver_report | None | Data obtained from survey, questionnaire, etc | Title: Participant or Caregiver Report<br>|
| other | None | Data obtained from other source, such as tissue bank | Title: Other<br>|




## Slots

| Name | Description |
| ---  | --- |
| [assertion_provenance](assertion_provenance.md) | The original source of this assertion |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumAssertionProvenance
description: Possible data sources for assertions.
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: EnumNull
permissible_values:
  medical_record:
    text: medical_record
    description: Data obtained from a medical record
    title: Medical Record
  investigator_assessment:
    text: investigator_assessment
    description: Data obtained by examination, interview, etc. with investigator
    title: Investigator Assessment
  participant_or_caregiver_report:
    text: participant_or_caregiver_report
    description: Data obtained from survey, questionnaire, etc. filled out by participant
      or caregiver
    title: Participant or Caregiver Report
  other:
    text: other
    description: Data obtained from other source, such as tissue bank
    title: Other

```
</details>

</div>