---
search:
  boost: 2.0
---


# Enum: EnumAvailabilityStatus 




_Is this item available for use?_



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumAvailabilityStatus](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumAvailabilityStatus)

## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| snomedct:103328004 | snomedct:103328004 | The item is available to users, authorization/request permitting | Title: Available<br>|
| snomedct:103329007 | snomedct:103329007 | The item is not available to users | Title: Unavailable<br>|




## Slots

| Name | Description |
| ---  | --- |
| [availability_status](availability_status.md) | Can this Sample be requested for further analysis? |
| [availability](availability.md) | Is or was this file available to users? |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumAvailabilityStatus
description: Is this item available for use?
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  snomedct:103328004:
    text: snomedct:103328004
    description: The item is available to users, authorization/request permitting.
    meaning: snomedct:103328004
    title: Available
  snomedct:103329007:
    text: snomedct:103329007
    description: The item is not available to users.
    meaning: snomedct:103329007
    title: Unavailable

```
</details>

</div>