---
search:
  boost: 2.0
---


# Enum: Clinical Data Source Type (EnumClinicalDataSourceType) 




_Approaches to ascertain clinical information about a participant._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumClinicalDataSourceType](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumClinicalDataSourceType)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| medical_record | None | Data obtained directly from medical record | Title: Medical Record<br>|
| investigator_assessment | None | Data obtained by examination, interview, etc | Title: Investigator Assessment<br>|
| participant_or_caregiver_report | None | Data obtained from survey, questionnaire, etc | Title: Participant or Caregiver Report<br>|
| other | None | Data obtained from other source, such as tissue bank | Title: Other<br>|
| unknown | None |  | Title: Unknown<br>|




## Slots

| Name | Description |
| ---  | --- |
| [clinical_data_source_type](clinical_data_source_type.md) | Source(s) of data collected from study participants |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumClinicalDataSourceType
description: Approaches to ascertain clinical information about a participant.
title: Clinical Data Source Type
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  medical_record:
    text: medical_record
    description: Data obtained directly from medical record
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
  unknown:
    text: unknown
    title: Unknown

```
</details>

</div>