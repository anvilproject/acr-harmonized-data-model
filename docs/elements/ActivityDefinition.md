---
search:
  boost: 10.0
---

# Class: Activity Definition (ActivityDefinition) 


_A definition of an activity in this study, eg, a biospecimen collection, assay, intervention, survey, or assessment._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:ActivityDefinition](https://w3id.org/anvilproject/acr-harmonized-data-model/ActivityDefinition)





```mermaid
 classDiagram
    class ActivityDefinition
    click ActivityDefinition href "../ActivityDefinition/"
      Record <|-- ActivityDefinition
        click Record href "../Record/"
      
      ActivityDefinition : access_policy_id
        
          
    
        
        
        ActivityDefinition --> "0..1" AccessPolicy : access_policy_id
        click AccessPolicy href "../AccessPolicy/"
    

        
      ActivityDefinition : activity_definition_id
        
      ActivityDefinition : description
        
      ActivityDefinition : external_id
        
      ActivityDefinition : name
        
      ActivityDefinition : study_id
        
          
    
        
        
        ActivityDefinition --> "0..1" Study : study_id
        click Study href "../Study/"
    

        
      
```





## Inheritance
* **ActivityDefinition** [ [Record](Record.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [activity_definition_id](activity_definition_id.md) | 1 <br/> [AdGlobalID](AdGlobalID.md) | Unique identifier for this Activity Definition | direct |
| [name](name.md) | 0..1 <br/> [String](String.md) | Name of the entity | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | Description for this entity | direct |
| [external_id](external_id.md) | * <br/> [Uriorcurie](Uriorcurie.md) | Other identifiers for this entity, eg, from the submitting study or in system... | [Record](Record.md) |
| [access_policy_id](access_policy_id.md) | 0..1 <br/> [AccessPolicy](AccessPolicy.md) | Global identifier for the access policy that applies to this row of data | [Record](Record.md) |
| [study_id](study_id.md) | 0..1 <br/> [Study](Study.md) | INCLUDE Global ID for the study | [Record](Record.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EncounterDefinition](EncounterDefinition.md) | [activity_definition_id](activity_definition_id.md) | range | [ActivityDefinition](ActivityDefinition.md) |
| [Assay](Assay.md) | [activity_definition_id](activity_definition_id.md) | range | [ActivityDefinition](ActivityDefinition.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:ActivityDefinition |
| native | acr_harmonized_data_model:ActivityDefinition |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ActivityDefinition
description: A definition of an activity in this study, eg, a biospecimen collection,
  assay, intervention, survey, or assessment.
title: Activity Definition
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
mixins:
- Record
slots:
- activity_definition_id
- name
- description
slot_usage:
  activity_definition_id:
    name: activity_definition_id
    identifier: true
    range: adGlobalID
    required: true

```
</details>

### Induced

<details>
```yaml
name: ActivityDefinition
description: A definition of an activity in this study, eg, a biospecimen collection,
  assay, intervention, survey, or assessment.
title: Activity Definition
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
mixins:
- Record
slot_usage:
  activity_definition_id:
    name: activity_definition_id
    identifier: true
    range: adGlobalID
    required: true
attributes:
  activity_definition_id:
    name: activity_definition_id
    description: Unique identifier for this Activity Definition.
    title: Activity Definition ID
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    identifier: true
    owner: ActivityDefinition
    domain_of:
    - EncounterDefinition
    - ActivityDefinition
    - Assay
    range: adGlobalID
    required: true
  name:
    name: name
    description: Name of the entity.
    title: Name
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: ActivityDefinition
    domain_of:
    - VirtualBiorepository
    - Investigator
    - EncounterDefinition
    - ActivityDefinition
    - Dataset
    range: string
    required: false
  description:
    name: description
    description: Description for this entity.
    title: Description
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: ActivityDefinition
    domain_of:
    - EncounterDefinition
    - ActivityDefinition
    - Dataset
    range: string
  external_id:
    name: external_id
    description: Other identifiers for this entity, eg, from the submitting study
      or in systems like dbGaP
    title: External Identifiers
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: ActivityDefinition
    domain_of:
    - Record
    range: uriorcurie
    required: false
    multivalued: true
  access_policy_id:
    name: access_policy_id
    description: Global identifier for the access policy that applies to this row
      of data.
    title: Access Policy ID
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: ActivityDefinition
    domain_of:
    - Record
    - AccessPolicy
    range: AccessPolicy
  study_id:
    name: study_id
    description: INCLUDE Global ID for the study
    title: Study ID
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: ActivityDefinition
    domain_of:
    - Record
    - StudyMetadata
    range: Study
    multivalued: false

```
</details></div>