---
search:
  boost: 5.0
---

# Slot: Encounter ID (encounter_id) 


_Unique identifier for this Encounter._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:encounter_id](https://w3id.org/anvilproject/acr-harmonized-data-model/encounter_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |  no  |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  no  |
| [Encounter](Encounter.md) | An event at which data was collected about a participant, an intervention was... |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Encounter](Encounter.md) |
| Domain Of | [SubjectAssertion](SubjectAssertion.md), [BiospecimenCollection](BiospecimenCollection.md), [Encounter](Encounter.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:encounter_id |
| native | acr_harmonized_data_model:encounter_id |




## LinkML Source

<details>
```yaml
name: encounter_id
description: Unique identifier for this Encounter.
title: Encounter ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- SubjectAssertion
- BiospecimenCollection
- Encounter
range: Encounter

```
</details></div>