---
search:
  boost: 5.0
---

# Slot: Study ID (subject_id) 


_INCLUDE Global ID for the Subject_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:subject_id](https://w3id.org/anvilproject/acr-harmonized-data-model/subject_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Subject](Subject.md) | This entity is the subject about which data or references are recorded |  yes  |
| [Demographics](Demographics.md) | Basic participant demographics summary |  yes  |
| [FamilyRelationship](FamilyRelationship.md) | A relationship between two Subjects |  yes  |
| [FamilyMembership](FamilyMembership.md) | Designates a Subject as a member of a family with a specified role |  yes  |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |  no  |
| [Encounter](Encounter.md) | An event at which data was collected about a participant, an intervention was... |  no  |
| [File](File.md) | File |  yes  |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Subject](Subject.md) |
| Domain Of | [Subject](Subject.md), [Demographics](Demographics.md), [FamilyRelationship](FamilyRelationship.md), [FamilyMembership](FamilyMembership.md), [SubjectAssertion](SubjectAssertion.md), [Encounter](Encounter.md), [File](File.md), [Assay](Assay.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:subject_id |
| native | acr_harmonized_data_model:subject_id |




## LinkML Source

<details>
```yaml
name: subject_id
description: INCLUDE Global ID for the Subject
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Subject
- Demographics
- FamilyRelationship
- FamilyMembership
- SubjectAssertion
- Encounter
- File
- Assay
range: Subject
multivalued: false

```
</details></div>