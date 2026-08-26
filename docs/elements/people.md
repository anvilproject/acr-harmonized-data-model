---
search:
  boost: 5.0
---

# Slot: people 

<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:people](https://w3id.org/anvilproject/acr-harmonized-data-model/people)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PersonCollection](PersonCollection.md) | A holder for Person objects |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Person](Person.md) |
| Domain Of | [PersonCollection](PersonCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Multivalued | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [PersonCollection](PersonCollection.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:people |
| native | acr_harmonized_data_model:people |




## LinkML Source

<details>
```yaml
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

```
</details></div>