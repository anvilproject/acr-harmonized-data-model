---
search:
  boost: 2.0
---


# Enum: EnumFamilyType 




_Enumerations describing research family type_



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumFamilyType](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumFamilyType)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** CAMO:0000001
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| CAMO:0000002 | None | This family study includes at a minimum one parent and one child | Title: Parent(s) and Child(ren)<br>|
| CAMO:0000003 | None | This family study includes at a minimum one parent and one affected child | Title: Duo<br>|
| CAMO:0000004 | None | This family study includes at a minimum two parents of one affected child | Title: Trio<br>|
| CAMO:0000005 | None | This family study includes at a minimum two parents of one affected child and... | Title: Trio+<br>|
| CAMO:0000006 | None | This family study includes only one or more cases | Title: Case Only<br>|
| CAMO:0000007 | None | This family study includes only one or more probands | Title: Proband Only<br>|
| CAMO:0000008 | None | This family study includes only one or more controls | Title: Control Only<br>|




## Slots

| Name | Description |
| ---  | --- |
| [family_type](family_type.md) | Describes the 'type' of study family, eg, trio |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumFamilyType
description: Enumerations describing research family type
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  CAMO:0000002:
    text: CAMO:0000002
    description: This family study includes at a minimum one parent and one child.
    title: Parent(s) and Child(ren)
  CAMO:0000003:
    text: CAMO:0000003
    description: This family study includes at a minimum one parent and one affected
      child.
    title: Duo
    aliases:
    - duo
  CAMO:0000004:
    text: CAMO:0000004
    description: This family study includes at a minimum two parents of one affected
      child.
    title: Trio
    aliases:
    - trio
  CAMO:0000005:
    text: CAMO:0000005
    description: This family study includes at a minimum two parents of one affected
      child and at least one other child.
    title: Trio+
    aliases:
    - trio_plus
  CAMO:0000006:
    text: CAMO:0000006
    description: This family study includes only one or more cases.
    title: Case Only
  CAMO:0000007:
    text: CAMO:0000007
    description: This family study includes only one or more probands.
    title: Proband Only
    aliases:
    - proband_only
  CAMO:0000008:
    text: CAMO:0000008
    description: This family study includes only one or more controls.
    title: Control Only
    aliases:
    - control_only
reachable_from:
  source_ontology: camo
  source_nodes:
  - CAMO:0000001
  relationship_types:
  - rdfs:subClassOf
  is_direct: false
  include_self: true

```
</details>

</div>