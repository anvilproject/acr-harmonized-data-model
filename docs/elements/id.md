---
search:
  boost: 5.0
---

# Slot: id 


_A unique identifier for a thing_



<div data-search-exclude markdown="1">



URI: [schema:identifier](http://schema.org/identifier)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NamedThing](NamedThing.md) | A generic grouping for any identifiable entity |  no  |
| [Person](Person.md) | Represents a Person |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Uriorcurie](Uriorcurie.md) |
| Domain Of | [NamedThing](NamedThing.md) |
| Slot URI | [schema:identifier](http://schema.org/identifier) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Identifier | Yes |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:identifier |
| native | acr_harmonized_data_model:id |




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for a thing
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
slot_uri: schema:identifier
identifier: true
domain_of:
- NamedThing
range: uriorcurie
required: true

```
</details></div>