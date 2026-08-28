---
search:
  boost: 5.0
---



# Slot: Contact Person (contact) 


_The individual to contact with questions about this record._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:contact](https://w3id.org/anvilproject/acr-harmonized-data-model/contact)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) | Study Metadata |  no  |
| [VirtualBiorepository](VirtualBiorepository.md) | An organization that can provide access to specimen for further analysis |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Investigator](Investigator.md) |
| Domain Of | [Study](Study.md), [VirtualBiorepository](VirtualBiorepository.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
| Multivalued | Yes |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:contact |
| native | acr_harmonized_data_model:contact |




## LinkML Source

<details>
```yaml
name: contact
description: The individual to contact with questions about this record.
title: Contact Person
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- Study
- VirtualBiorepository
range: Investigator
required: true
multivalued: true

```
</details></div>