---
search:
  boost: 2.0
---


# Enum: Data Source Type (EnumDataSourceType) 




_Approaches to ascertain information about a participant._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumDataSourceType](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumDataSourceType)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** CAMO:0000009
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| CAMO:0000014 | None | Data obtained directly from an Electronic Health Record | Title: Electronic Health Record<br>|
| CAMO:0000010 | None | Data obtained from a survey or questionnaire given to a participant or their ... | Title: Survey<br>|
| CAMO:0000011 | None | Data obtained by research staff for the study | Title: Research Assessment<br>|
| CAMO:0000012 | None | Data obtained by research staff interviewing participants, representatives, o... | Title: Interview<br>|
| CAMO:0000013 | None | Data obtained directly by research staff examining the participant | Title: Physical Examination<br>|




## Slots

| Name | Description |
| ---  | --- |
| [clinical_data_source_type](clinical_data_source_type.md) | Source(s) of data collected from study participants |
| [assertion_source_type](assertion_source_type.md) | The source of this assertion from the original data |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumDataSourceType
description: Approaches to ascertain information about a participant.
title: Data Source Type
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  CAMO:0000014:
    text: CAMO:0000014
    description: Data obtained directly from an Electronic Health Record.
    title: Electronic Health Record
    aliases:
    - medical_record
  CAMO:0000010:
    text: CAMO:0000010
    description: Data obtained from a survey or questionnaire given to a participant
      or their representative.
    title: Survey
    aliases:
    - participant_or_caregiver_report
  CAMO:0000011:
    text: CAMO:0000011
    description: Data obtained by research staff for the study.
    title: Research Assessment
    aliases:
    - investigator_assessment
  CAMO:0000012:
    text: CAMO:0000012
    description: Data obtained by research staff interviewing participants, representatives,
      or others.
    title: Interview
  CAMO:0000013:
    text: CAMO:0000013
    description: Data obtained directly by research staff examining the participant.
    title: Physical Examination
reachable_from:
  source_ontology: camo
  source_nodes:
  - CAMO:0000009
  relationship_types:
  - rdfs:subClassOf
  is_direct: false
  include_self: true

```
</details>

</div>