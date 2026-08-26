---
search:
  boost: 2.0
---


# Enum: EnumSubjectType 




_Types of Subject entities_



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumSubjectType](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumSubjectType)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** CAMO:0000023
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| CAMO:0000024 | None | Study participant with consent, assent, or waiver of consent | Title: Participant<br>|
| CAMO:0000025 | None | An individual not directly participating in a study, eg, the subject of a rep... | Title: Non-Participant<br>|
| CAMO:0000026 | None |  | Title: Cell Line<br>|
| CAMO:0000027 | None |  | Title: Animal Model<br>|
| CAMO:0000028 | None | A group of entities or things being assessed as a whole | Title: Group<br>|













## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumSubjectType
description: Types of Subject entities
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  CAMO:0000024:
    text: CAMO:0000024
    description: Study participant with consent, assent, or waiver of consent.
    title: Participant
    aliases:
    - participant
  CAMO:0000025:
    text: CAMO:0000025
    description: An individual not directly participating in a study, eg, the subject
      of a reported family history.
    title: Non-Participant
    aliases:
    - non_participant
  CAMO:0000026:
    text: CAMO:0000026
    title: Cell Line
    aliases:
    - cell_line
  CAMO:0000027:
    text: CAMO:0000027
    title: Animal Model
    aliases:
    - animal_model
  CAMO:0000028:
    text: CAMO:0000028
    description: A group of entities or things being assessed as a whole.
    title: Group
    aliases:
    - group
reachable_from:
  source_ontology: camo
  source_nodes:
  - CAMO:0000023
  relationship_types:
  - rdfs:subClassOf
  is_direct: false
  include_self: true

```
</details>

</div>