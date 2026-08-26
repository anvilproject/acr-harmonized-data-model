---
search:
  boost: 10.0
---

# Class: Digital Object Identifier (DOI) (DOI) 


_A DOI is a permanent reference with metadata about a digital object._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:DOI](https://w3id.org/anvilproject/acr-harmonized-data-model/DOI)





```mermaid
 classDiagram
    class DOI
    click DOI href "../DOI/"
      Record <|-- DOI
        click Record href "../Record/"
      
      DOI : access_policy_id
        
          
    
        
        
        DOI --> "0..1" AccessPolicy : access_policy_id
        click AccessPolicy href "../AccessPolicy/"
    

        
      DOI : bibliographic_reference
        
      DOI : do_id
        
      DOI : external_id
        
      DOI : study_id
        
          
    
        
        
        DOI --> "0..1" Study : study_id
        click Study href "../Study/"
    

        
      
```





## Inheritance
* **DOI** [ [Record](Record.md)]


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [do_id](do_id.md) | 1 <br/> [String](String.md) | Digital Object Identifier (DOI) for this Record | direct |
| [bibliographic_reference](bibliographic_reference.md) | 0..1 <br/> [String](String.md) | Text use to reference this Record | direct |
| [external_id](external_id.md) | * <br/> [Uriorcurie](Uriorcurie.md) | Other identifiers for this entity, eg, from the submitting study or in system... | [Record](Record.md) |
| [access_policy_id](access_policy_id.md) | 0..1 <br/> [AccessPolicy](AccessPolicy.md) | Global identifier for the access policy that applies to this row of data | [Record](Record.md) |
| [study_id](study_id.md) | 0..1 <br/> [Study](Study.md) | INCLUDE Global ID for the study | [Record](Record.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [do_id](do_id.md) | range | [DOI](DOI.md) |
| [Dataset](Dataset.md) | [do_id](do_id.md) | range | [DOI](DOI.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:DOI |
| native | acr_harmonized_data_model:DOI |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DOI
description: A DOI is a permanent reference with metadata about a digital object.
title: Digital Object Identifier (DOI)
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
mixins:
- Record
slots:
- do_id
- bibliographic_reference
slot_usage:
  do_id:
    name: do_id
    identifier: true
    range: string
    required: true

```
</details>

### Induced

<details>
```yaml
name: DOI
description: A DOI is a permanent reference with metadata about a digital object.
title: Digital Object Identifier (DOI)
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
mixins:
- Record
slot_usage:
  do_id:
    name: do_id
    identifier: true
    range: string
    required: true
attributes:
  do_id:
    name: do_id
    description: Digital Object Identifier (DOI) for this Record.
    title: DOI
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    identifier: true
    owner: DOI
    domain_of:
    - Study
    - DOI
    - Dataset
    range: string
    required: true
    multivalued: false
  bibliographic_reference:
    name: bibliographic_reference
    description: Text use to reference this Record.
    title: Bibiliographic Reference
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: DOI
    domain_of:
    - DOI
    - Publication
    range: string
  external_id:
    name: external_id
    description: Other identifiers for this entity, eg, from the submitting study
      or in systems like dbGaP
    title: External Identifiers
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: DOI
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
    owner: DOI
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
    owner: DOI
    domain_of:
    - Record
    - StudyMetadata
    range: Study
    multivalued: false

```
</details></div>