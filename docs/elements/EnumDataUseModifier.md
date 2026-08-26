---
search:
  boost: 2.0
---


# Enum: Data Use Modifier (EnumDataUseModifier) 




_Data Use Ontology (DUO) terms for data use modifiers._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumDataUseModifier](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumDataUseModifier)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** DUO:0000017
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| DUO:00000044 | DUO:00000044 | This data use modifier indicates use for purposes of population, origin, or a... | Title: population origins or ancestry research prohibited<br>|
| DUO:0000012 | DUO:0000012 | This data use modifier indicates that use is limited to studies of a certain ... | Title: research specific restrictions<br>|
| DUO:0000015 | DUO:0000015 | This data use modifier indicates that use does not allow methods development ... | Title: no general methods research<br>|
| DUO:0000016 | DUO:0000016 | This data use modifier indicates that use is limited to genetic studies only ... | Title: genetic studies only<br>|
| DUO:0000018 | DUO:0000018 | This data use modifier indicates that use of the data is limited to not-for-p... | Title: not for profit, non commercial use only<br>|
| DUO:0000019 | DUO:0000019 | This data use modifier indicates that requestor agrees to make results of stu... | Title: publication required<br>|
| DUO:0000020 | DUO:0000020 | This could be coupled with a string describing the primary study investigator... | Title: collaboration required<br>|
| DUO:0000021 | DUO:0000021 | This data use modifier indicates that the requestor must provide documentatio... | Title: ethics approval required<br>|
| DUO:0000022 | DUO:0000022 | This data use modifier indicates that use is limited to within a specific geo... | Title: geographical restriction<br>|
| DUO:0000024 | DUO:0000024 | This data use modifier indicates that requestor agrees not to publish results... | Title: publication moratorium<br>|
| DUO:0000025 | DUO:0000025 | This data use modifier indicates that use is approved for a specific number o... | Title: time limit on use<br>|
| DUO:0000026 | DUO:0000026 | This data use modifier indicates that use is limited to use by approved users | Title: user specific restriction<br>|
| DUO:0000027 | DUO:0000027 | This data use modifier indicates that use is limited to use within an approve... | Title: project specific restriction<br>|
| DUO:0000028 | DUO:0000028 | This data use modifier indicates that use is limited to use within an approve... | Title: institution specific restriction<br>|
| DUO:0000029 | DUO:0000029 | This data use modifier indicates that the requestor must return derived/enric... | Title: return to database or resource<br>|
| DUO:0000043 | DUO:0000043 | Clinical Care is defined as Health care or services provided at home, in a he... | Title: clinical care use<br>|
| DUO:0000045 | DUO:0000045 | This data use modifier indicates that use of the data is limited to not-for-p... | Title: not for profit organisation use only<br>|
| DUO:0000046 | DUO:0000046 | This data use modifier indicates that use of the data is limited to not-for-p... | Title: non-commercial use only<br>|




## Slots

| Name | Description |
| ---  | --- |
| [data_use_modifier](data_use_modifier.md) | Additional modifiers that limit data use |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumDataUseModifier
description: Data Use Ontology (DUO) terms for data use modifiers.
title: Data Use Modifier
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  DUO:00000044:
    text: DUO:00000044
    description: This data use modifier indicates use for purposes of population,
      origin, or ancestry research is prohibited.
    meaning: DUO:00000044
    title: population origins or ancestry research prohibited
  DUO:0000012:
    text: DUO:0000012
    description: This data use modifier indicates that use is limited to studies of
      a certain research type.
    meaning: DUO:0000012
    title: research specific restrictions
  DUO:0000015:
    text: DUO:0000015
    description: This data use modifier indicates that use does not allow methods
      development research (e.g., development of software or algorithms).
    meaning: DUO:0000015
    title: no general methods research
  DUO:0000016:
    text: DUO:0000016
    description: This data use modifier indicates that use is limited to genetic studies
      only (i.e., studies that include genotype research alone or both genotype and
      phenotype research, but not phenotype research exclusively)
    meaning: DUO:0000016
    title: genetic studies only
  DUO:0000018:
    text: DUO:0000018
    description: This data use modifier indicates that use of the data is limited
      to not-for-profit organizations and not-for-profit use, non-commercial use.
    meaning: DUO:0000018
    title: not for profit, non commercial use only
  DUO:0000019:
    text: DUO:0000019
    description: This data use modifier indicates that requestor agrees to make results
      of studies using the data available to the larger scientific community.
    meaning: DUO:0000019
    title: publication required
  DUO:0000020:
    text: DUO:0000020
    description: 'This could be coupled with a string describing the primary study
      investigator(s).

      This data use modifier indicates that the requestor must agree to collaboration
      with the primary study investigator(s).'
    meaning: DUO:0000020
    title: collaboration required
  DUO:0000021:
    text: DUO:0000021
    description: This data use modifier indicates that the requestor must provide
      documentation of local IRB/ERB approval.
    meaning: DUO:0000021
    title: ethics approval required
  DUO:0000022:
    text: DUO:0000022
    description: 'This data use modifier indicates that use is limited to within a
      specific geographic region.

      This should be coupled with an ontology term describing the geographical location
      the restriction applies to.'
    meaning: DUO:0000022
    title: geographical restriction
  DUO:0000024:
    text: DUO:0000024
    description: 'This data use modifier indicates that requestor agrees not to publish
      results of studies until a specific date.

      This should be coupled with a date specified as ISO8601'
    meaning: DUO:0000024
    title: publication moratorium
  DUO:0000025:
    text: DUO:0000025
    description: 'This data use modifier indicates that use is approved for a specific
      number of months.

      This should be coupled with an integer value indicating the number of months.'
    meaning: DUO:0000025
    title: time limit on use
  DUO:0000026:
    text: DUO:0000026
    description: This data use modifier indicates that use is limited to use by approved
      users.
    meaning: DUO:0000026
    title: user specific restriction
  DUO:0000027:
    text: DUO:0000027
    description: This data use modifier indicates that use is limited to use within
      an approved project.
    meaning: DUO:0000027
    title: project specific restriction
  DUO:0000028:
    text: DUO:0000028
    description: This data use modifier indicates that use is limited to use within
      an approved institution.
    meaning: DUO:0000028
    title: institution specific restriction
  DUO:0000029:
    text: DUO:0000029
    description: This data use modifier indicates that the requestor must return derived/enriched
      data to the database/resource.
    meaning: DUO:0000029
    title: return to database or resource
  DUO:0000043:
    text: DUO:0000043
    description: 'Clinical Care is defined as Health care or services provided at
      home, in a healthcare facility or hospital. Data may be used for clinical decision
      making.

      This data use modifier indicates that use is allowed for clinical use and care.'
    meaning: DUO:0000043
    title: clinical care use
  DUO:0000045:
    text: DUO:0000045
    description: This data use modifier indicates that use of the data is limited
      to not-for-profit organizations.
    meaning: DUO:0000045
    title: not for profit organisation use only
  DUO:0000046:
    text: DUO:0000046
    description: 'This data use modifier indicates that use of the data is limited
      to not-for-profit use.

      This indicates that data can be used by commercial organisations for research
      purposes, but not commercial purposes.'
    meaning: DUO:0000046
    title: non-commercial use only
reachable_from:
  source_ontology: bioregistry:duo
  source_nodes:
  - DUO:0000017
  relationship_types:
  - rdfs:subClassOf
  is_direct: false

```
</details>

</div>