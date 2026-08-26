---
search:
  boost: 2.0
---


# Enum: EnumFileAvailability 




_Options describing file availability_



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumFileAvailability](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumFileAvailability)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| snomed_ct:103328004 | snomed_ct:103328004 | The file is available to users, authorization permitting | Title: Available<br>|
| snomed_ct:103329007 | snomed_ct:103329007 | The file is not available to users | Title: Unavailable<br>|




## Slots

| Name | Description |
| ---  | --- |
| [availability](availability.md) | Is or was this file available to users? |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumFileAvailability
description: Options describing file availability
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
is_a: EnumNull
permissible_values:
  snomed_ct:103328004:
    text: snomed_ct:103328004
    description: The file is available to users, authorization permitting.
    meaning: snomed_ct:103328004
    title: Available
  snomed_ct:103329007:
    text: snomed_ct:103329007
    description: The file is not available to users.
    meaning: snomed_ct:103329007
    title: Unavailable

```
</details>

</div>