---
search:
  boost: 10.0
---

# Class: Family Membership (FamilyMembership) 


_Designates a Subject as a member of a family with a specified role._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:FamilyMembership](https://w3id.org/anvilproject/acr-harmonized-data-model/FamilyMembership)





```mermaid
 classDiagram
    class FamilyMembership
    click FamilyMembership href "../FamilyMembership/"
      Record <|-- FamilyMembership
        click Record href "../Record/"
      
      FamilyMembership : access_policy_id
        
          
    
        
        
        FamilyMembership --> "0..1" AccessPolicy : access_policy_id
        click AccessPolicy href "../AccessPolicy/"
    

        
      FamilyMembership : external_id
        
      FamilyMembership : family_id
        
          
    
        
        
        FamilyMembership --> "1" Family : family_id
        click Family href "../Family/"
    

        
      FamilyMembership : family_membership_id
        
      FamilyMembership : family_role
        
          
    
        
        
        FamilyMembership --> "0..1" Concept : family_role
        click Concept href "../Concept/"
    

        
      FamilyMembership : study_id
        
          
    
        
        
        FamilyMembership --> "0..1" Study : study_id
        click Study href "../Study/"
    

        
      FamilyMembership : subject_id
        
          
    
        
        
        FamilyMembership --> "1" Subject : subject_id
        click Subject href "../Subject/"
    

        
      
```





## Inheritance
* **FamilyMembership** [ [Record](Record.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [family_membership_id](family_membership_id.md) | 1 <br/> [String](String.md) | ID for the Family Relationship | direct |
| [family_id](family_id.md) | 1 <br/> [Family](Family.md) | Global ID for the Family | direct |
| [subject_id](subject_id.md) | 1 <br/> [Subject](Subject.md) | INCLUDE Global ID for the Subject | direct |
| [family_role](family_role.md) | 0..1 <br/> [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumFamilyRole](EnumFamilyRole.md) | The "role" of this individual in this family | direct |
| [external_id](external_id.md) | * <br/> [Uriorcurie](Uriorcurie.md) | Other identifiers for this entity, eg, from the submitting study or in system... | [Record](Record.md) |
| [access_policy_id](access_policy_id.md) | 0..1 <br/> [AccessPolicy](AccessPolicy.md) | Global identifier for the access policy that applies to this row of data | [Record](Record.md) |
| [study_id](study_id.md) | 0..1 <br/> [Study](Study.md) | INCLUDE Global ID for the study | [Record](Record.md) |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:FamilyMembership |
| native | acr_harmonized_data_model:FamilyMembership |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FamilyMembership
description: Designates a Subject as a member of a family with a specified role.
title: Family Membership
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
mixins:
- Record
slots:
- family_membership_id
- family_id
- subject_id
- family_role
slot_usage:
  family_membership_id:
    name: family_membership_id
    identifier: true
    range: string
    required: true
  family_id:
    name: family_id
    required: true
  subject_id:
    name: subject_id
    required: true

```
</details>

### Induced

<details>
```yaml
name: FamilyMembership
description: Designates a Subject as a member of a family with a specified role.
title: Family Membership
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
mixins:
- Record
slot_usage:
  family_membership_id:
    name: family_membership_id
    identifier: true
    range: string
    required: true
  family_id:
    name: family_id
    required: true
  subject_id:
    name: subject_id
    required: true
attributes:
  family_membership_id:
    name: family_membership_id
    description: ID for the Family Relationship
    title: Family Relationship ID
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    identifier: true
    owner: FamilyMembership
    domain_of:
    - FamilyMembership
    range: string
    required: true
  family_id:
    name: family_id
    description: Global ID for the Family
    title: Family ID
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: FamilyMembership
    domain_of:
    - Family
    - FamilyMembership
    range: Family
    required: true
  subject_id:
    name: subject_id
    description: INCLUDE Global ID for the Subject
    title: Study ID
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: FamilyMembership
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
    required: true
    multivalued: false
  family_role:
    name: family_role
    description: The "role" of this individual in this family. Could include terms
      like "proband", "mother", etc.
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: FamilyMembership
    domain_of:
    - FamilyMembership
    range: Concept
    any_of:
    - range: Concept
    - range: EnumFamilyRole
  external_id:
    name: external_id
    description: Other identifiers for this entity, eg, from the submitting study
      or in systems like dbGaP
    title: External Identifiers
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: FamilyMembership
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
    owner: FamilyMembership
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
    owner: FamilyMembership
    domain_of:
    - Record
    - StudyMetadata
    range: Study
    multivalued: false

```
</details></div>