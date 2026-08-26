---
search:
  boost: 2.0
---


# Enum: Data Use Permission (EnumDataUsePermission) 




_Data Use Ontology (DUO) terms for data use permissions._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumDataUsePermission](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumDataUsePermission)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** DUO:0000001
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| DUO:0000004 | DUO:0000004 | This data use permission indicates there is no restriction on use | Title: no restriction<br>|
| DUO:0000006 | DUO:0000006 | This data use permission indicates that use is allowed for health/medical/bio... | Title: health or medical or biomedical research<br>|
| DUO:0000007 | DUO:0000007 | This data use permission indicates that use is allowed provided it is related... | Title: disease specific research<br>|
| DUO:0000011 | DUO:0000011 | This data use permission indicates that use of the data is limited to the stu... | Title: population origins or ancestry research only<br>|
| DUO:0000042 | DUO:0000042 | This data use permission indicates that use is allowed for general research u... | Title: general research use<br>|




## Slots

| Name | Description |
| ---  | --- |
| [data_use_permission](data_use_permission.md) | Broad category of restrictions on data use |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumDataUsePermission
description: Data Use Ontology (DUO) terms for data use permissions.
title: Data Use Permission
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  DUO:0000004:
    text: DUO:0000004
    description: This data use permission indicates there is no restriction on use.
    meaning: DUO:0000004
    title: no restriction
  DUO:0000006:
    text: DUO:0000006
    description: This data use permission indicates that use is allowed for health/medical/biomedical
      purposes; does not include the study of population origins or ancestry.
    meaning: DUO:0000006
    title: health or medical or biomedical research
  DUO:0000007:
    text: DUO:0000007
    description: "This data use permission indicates that use is allowed provided\
      \ it is related to the specified disease.\nThis term should be coupled with\
      \ a term describing a disease from an ontology to specify the disease the restriction\
      \ applies to. \n\nDUO recommends MONDO be used, to provide the basis for automated\
      \ evaluation. For more information see https://github.com/EBISPOT/DUO/blob/master/MONDO_Overview.md\n\
      \nOther resources, such as the Disease Ontology, HPO, SNOMED-CT or others, can\
      \ also be used. When those other resources are being used, this may require\
      \ an extra mapping step to leverage automated matching algorithms."
    meaning: DUO:0000007
    title: disease specific research
  DUO:0000011:
    text: DUO:0000011
    description: This data use permission indicates that use of the data is limited
      to the study of population origins or ancestry.
    meaning: DUO:0000011
    title: population origins or ancestry research only
  DUO:0000042:
    text: DUO:0000042
    description: 'This data use permission indicates that use is allowed for general
      research use for any research purpose.

      This includes but is not limited to: health/medical/biomedical purposes, fundamental
      biology research, the study of population origins or ancestry, statistical methods
      and algorithms development, and social-sciences research.'
    meaning: DUO:0000042
    title: general research use
reachable_from:
  source_ontology: bioregistry:duo
  source_nodes:
  - DUO:0000001
  relationship_types:
  - rdfs:subClassOf
  is_direct: false

```
</details>

</div>