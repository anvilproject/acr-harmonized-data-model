---
search:
  boost: 5.0
---

# Slot: primary_email 


_The main email address of a person_



<div data-search-exclude markdown="1">



URI: [schema:email](http://schema.org/email)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Person](Person.md) | Represents a Person |  yes  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [Person](Person.md) |
| Slot URI | [schema:email](http://schema.org/email) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | schema:email |
| native | acr_harmonized_data_model:primary_email |




## LinkML Source

<details>
```yaml
name: primary_email
description: The main email address of a person
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
slot_uri: schema:email
domain_of:
- Person
range: string

```
</details></div>