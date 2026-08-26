---
search:
  boost: 2.0
---


# Enum: EnumFileHashType 




_Types of file hashes supported._



<div data-search-exclude markdown="1">

URI: [acr_harmonized_data_model:EnumFileHashType](https://w3id.org/anvilproject/acr-harmonized-data-model/EnumFileHashType)
## Enumeration Source
**Reachable From:**
- **Source:** NONE
- **Nodes:** MS:1000561
- **Via:** rdfs:subClassOf



## Permissible Values
| Value | Meaning | Description | Additional Info |
| --- | --- | --- | --- |
| MS:1000568 | None | MD5 (Message-Digest algorithm 5) is a (now deprecated) cryptographic hash fun... | Title: MD5<br>|
| CAMO:0000022 | None | The entity tag is a hash of the object | Title: ETag<br>|
| MS:1000569 | None | SHA-1 (Secure Hash Algorithm-1) is a cryptographic hash function designed by ... | Title: SHA-1<br>|
| MS:1003151 | None | SHA-256 (member of Secure Hash Algorithm-2 family) is a cryptographic hash fu... | Title: SHA-256<br>|




## Slots

| Name | Description |
| ---  | --- |
| [hash_type](hash_type.md) | The type of file hash, eg, md5 |










## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/anvilproject/acr-harmonized-data-model






## LinkML Source

<details>
```yaml
name: EnumFileHashType
description: Types of file hashes supported.
from_schema: https://w3id.org/anvilproject/acr-harmonized-data-model
rank: 1000
permissible_values:
  MS:1000568:
    text: MS:1000568
    description: MD5 (Message-Digest algorithm 5) is a (now deprecated) cryptographic
      hash function with a 128-bit hash value used to check the integrity of files.
    title: MD5
    aliases:
    - md5
  CAMO:0000022:
    text: CAMO:0000022
    description: The entity tag is a hash of the object. The ETag reflects changes
      only to the contents of an object, not its metadata. The ETag may or may not
      be an MD5 digest of the object data.
    title: ETag
    aliases:
    - etag
  MS:1000569:
    text: MS:1000569
    description: SHA-1 (Secure Hash Algorithm-1) is a cryptographic hash function
      designed by the National Security Agency (NSA). It is also used to verify file
      integrity. Since 2011 it has been deprecated by the NIST as a U. S. government
      standard.
    title: SHA-1
    aliases:
    - sha1
  MS:1003151:
    text: MS:1003151
    description: SHA-256 (member of Secure Hash Algorithm-2 family) is a cryptographic
      hash function designed by the National Security Agency (NSA) and published by
      the NIST as a U. S. government standard. It is also used to verify file integrity.
    title: SHA-256
reachable_from:
  source_ontology: camo
  source_nodes:
  - MS:1000561
  relationship_types:
  - rdfs:subClassOf
  is_direct: false
  include_self: true

```
</details>

</div>