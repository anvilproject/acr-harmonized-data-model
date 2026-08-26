---
search:
  boost: 10.0
---

# Class: PersonCollection 


_A holder for Person objects_



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:PersonCollection](https://w3id.org/anvilproject/acr-harmonized-data-model/PersonCollection)





```mermaid
 classDiagram
    class PersonCollection
    click PersonCollection href "../PersonCollection/"
      PersonCollection : people
        
          
    
        
        
        PersonCollection --> "*" Person : people
        click Person href "../Person/"
    

        
      
```




<!-- no inheritance hierarchy -->

## Class Properties

| Property | Value |
| --- | --- |
| Tree Root | Yes |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [people](people.md) | * <br/> [Person](Person.md) |  | direct |















## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:PersonCollection |
| native | acr_harmonized_data_model:PersonCollection |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PersonCollection
description: A holder for Person objects
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
attributes:
  people:
    name: people
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    domain_of:
    - PersonCollection
    range: Person
    multivalued: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: PersonCollection
description: A holder for Person objects
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
attributes:
  people:
    name: people
    from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
    rank: 1000
    owner: PersonCollection
    domain_of:
    - PersonCollection
    range: Person
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details></div>