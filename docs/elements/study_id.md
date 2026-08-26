---
search:
  boost: 5.0
---

# Slot: Study ID (study_id) 


_INCLUDE Global ID for the study_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:study_id](https://w3id.org/anvilproject/acr-harmonized-data-model/study_id)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Record](Record.md) | One row / entity within the database |  no  |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |  yes  |
| [Study](Study.md) | Study Metadata |  yes  |
| [VirtualBiorepository](VirtualBiorepository.md) | An organization that can provide access to specimen for further analysis |  no  |
| [DOI](DOI.md) | A DOI is a permanent reference with metadata about a digital object |  no  |
| [Investigator](Investigator.md) | An individual who made contributions to the collection, analysis, or sharing ... |  no  |
| [Publication](Publication.md) | Information about a specific publication |  no  |
| [Subject](Subject.md) | This entity is the subject about which data or references are recorded |  no  |
| [Demographics](Demographics.md) | Basic participant demographics summary |  no  |
| [Family](Family.md) | A group of individuals of some relation who are grouped together in a study |  no  |
| [FamilyRelationship](FamilyRelationship.md) | A relationship between two Subjects |  no  |
| [FamilyMembership](FamilyMembership.md) | Designates a Subject as a member of a family with a specified role |  no  |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |  no  |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |  no  |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  no  |
| [Aliquot](Aliquot.md) | A specific tube or amount of a biospecimen associated with a Sample |  no  |
| [Encounter](Encounter.md) | An event at which data was collected about a participant, an intervention was... |  no  |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |  no  |
| [ActivityDefinition](ActivityDefinition.md) | A definition of an activity in this study, eg, a biospecimen collection, assa... |  no  |
| [File](File.md) | File |  no  |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Study](Study.md) |
| Domain Of | [Record](Record.md), [StudyMetadata](StudyMetadata.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:study_id |
| native | acr_harmonized_data_model:study_id |




## LinkML Source

<details>
```yaml
name: study_id
description: INCLUDE Global ID for the study
title: Study ID
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Record
- StudyMetadata
range: Study
multivalued: false

```
</details></div>