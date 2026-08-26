---
search:
  boost: 5.0
---

# Slot: Biospecimen Collection Site (site) 


_The location of the specimen collection._



<div data-search-exclude markdown="1">



URI: [acr_harmonized_data_model:site](https://w3id.org/anvilproject/acr-harmonized-data-model/site)
<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [Concept](Concept.md)&nbsp;or&nbsp;<br />[EnumSite](EnumSite.md) |
| Domain Of | [BiospecimenCollection](BiospecimenCollection.md) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
<details>
<summary>Expressions & Logic</summary>
#### Any Of

Value must satisfy at least one of:
- AnonymousSlotExpression({'range': 'Concept'})
- AnonymousSlotExpression({'range': 'EnumSite'})

</details>











## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | acr_harmonized_data_model:site |
| native | acr_harmonized_data_model:site |




## LinkML Source

<details>
```yaml
name: site
description: The location of the specimen collection.
title: Biospecimen Collection Site
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
domain_of:
- BiospecimenCollection
range: Concept
any_of:
- range: Concept
- range: EnumSite

```
</details></div>