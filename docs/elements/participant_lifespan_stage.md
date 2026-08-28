---
search:
  boost: 5.0
---



# Slot: Participant Lifespan Stage (participant_lifespan_stage) 


_Focus age group(s) of the study population_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:participant_lifespan_stage](https://w3id.org/anvilproject/acr-harmonized-data-model/participant_lifespan_stage)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [EnumParticipantLifespanStage](EnumParticipantLifespanStage.md) |
| Domain Of | [StudyMetadata](StudyMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:participant_lifespan_stage |
| native | acr_harmonized_data_model:participant_lifespan_stage |




## LinkML Source

<details>
```yaml
name: participant_lifespan_stage
description: Focus age group(s) of the study population
title: Participant Lifespan Stage
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- StudyMetadata
range: EnumParticipantLifespanStage
required: true
multivalued: true

```
</details></div>