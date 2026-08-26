---
search:
  boost: 2.0
---


# Enum: EnumPresentAbsent 




_Options for describing presence or absence. Derived from SNOMED CT Known codes. The "Known" codes and "Not suspected" are the broadest terms and suitable for general use._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumPresentAbsent](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumPresentAbsent)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** snomedct:36692007
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| snomedct:410515003 | snomedct:410515003 |  | Title: Known present<br>|
| snomedct:410516002 | snomedct:410516002 |  | Title: Known absent<br>|
| snomedct:410590009 | snomedct:410590009 |  | Title: Known possible<br>|
| snomedct:410591008 | snomedct:410591008 |  | Title: Definitely present<br>|
| snomedct:410592001 | snomedct:410592001 |  | Title: Probably present<br>|
| snomedct:410593006 | snomedct:410593006 |  | Title: Probably not present<br>|
| snomedct:410594000 | snomedct:410594000 |  | Title: Definitely not present<br>|
| snomedct:410605003 | snomedct:410605003 |  | Title: Confirmed present<br>|
| snomedct:415684004 | snomedct:415684004 |  | Title: Suspected<br>|
| snomedct:428263003 | snomedct:428263003 |  | Title: Not suspected<br>|
| snomedct:723511001 | snomedct:723511001 |  | Title: Refuted<br>|




## Slots

| Name | Description |
| ---  | --- |
| [consanguinity](consanguinity.md) | Is there known or suspected consanguinity in this study family? |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumPresentAbsent
description: Options for describing presence or absence. Derived from SNOMED CT Known
  codes. The "Known" codes and "Not suspected" are the broadest terms and suitable
  for general use.
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  snomedct:410515003:
    text: snomedct:410515003
    meaning: snomedct:410515003
    title: Known present
  snomedct:410516002:
    text: snomedct:410516002
    meaning: snomedct:410516002
    title: Known absent
  snomedct:410590009:
    text: snomedct:410590009
    meaning: snomedct:410590009
    title: Known possible
  snomedct:410591008:
    text: snomedct:410591008
    meaning: snomedct:410591008
    title: Definitely present
  snomedct:410592001:
    text: snomedct:410592001
    meaning: snomedct:410592001
    title: Probably present
  snomedct:410593006:
    text: snomedct:410593006
    meaning: snomedct:410593006
    title: Probably not present
  snomedct:410594000:
    text: snomedct:410594000
    meaning: snomedct:410594000
    title: Definitely not present
  snomedct:410605003:
    text: snomedct:410605003
    meaning: snomedct:410605003
    title: Confirmed present
  snomedct:415684004:
    text: snomedct:415684004
    meaning: snomedct:415684004
    title: Suspected
  snomedct:428263003:
    text: snomedct:428263003
    meaning: snomedct:428263003
    title: Not suspected
  snomedct:723511001:
    text: snomedct:723511001
    meaning: snomedct:723511001
    title: Refuted
reachable_from:
  source_ontology: bioregistry:snomedct
  source_nodes:
  - snomedct:36692007
  relationship_types:
  - rdfs:subClassOf
  is_direct: false
  include_self: false

```
</details>

</div>