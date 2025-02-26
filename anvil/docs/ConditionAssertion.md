
# Class: ConditionAssertion

Study Meta Data

URI: [anvil:ConditionAssertion](https://anvilproject.org/acr-harmonized-data-model/ConditionAssertion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[ConditionAssertion&#124;condition_code:EnumConditionCode%20*;condition_source_value:string;condition_assertion:EnumConditionAssertion%20%3F;condition_type:EnumConditionType;age_at_assertion:integer%20%3F;age_at_onset:integer%20%3F;age_at_resolution:integer%20%3F;id(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[ConditionAssertion&#124;condition_code:EnumConditionCode%20*;condition_source_value:string;condition_assertion:EnumConditionAssertion%20%3F;condition_type:EnumConditionType;age_at_assertion:integer%20%3F;age_at_onset:integer%20%3F;age_at_resolution:integer%20%3F;id(i):string])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [condition_code](condition_code.md)  <sub>0..\*</sub>
     * Description: Condition Code should be from one of a recognized ontology. Multiple codes can be indicated, but should simply be alternative encodings for the same entity such as alternates encodings from other ontologies.       
Recommended ontologies include: SNOMED_CT, HP, OMIM and ORPHA and coded with the corresponding curies
* SNOMED : https://bioregistry.io/registry/snomedct
* HP : https://bioregistry.io/registry/hp
* OMIM : https://bioregistry.io/registry/omim
* ORPHA : https://bioregistry.io/registry/orphanet

     * Range: [EnumConditionCode](EnumConditionCode.md)
 * [condition_source_value](condition_source_value.md)  <sub>1..1</sub>
     * Description: Original Source Value for condition
     * Range: [String](types/String.md)
 * [condition_assertion](condition_assertion.md)  <sub>0..1</sub>
     * Description: Condition Assertion
     * Range: [EnumConditionAssertion](EnumConditionAssertion.md)
 * [condition_type](condition_type.md)  <sub>1..1</sub>
     * Description: Does this condition represent a specific "type" of condition, such as "Phenotypic Feature" vs "Disease" in a rare disease setting.
     * Range: [EnumConditionType](EnumConditionType.md)
 * [age_at_assertion](age_at_assertion.md)  <sub>0..1</sub>
     * Description: The age at which this condition is being asserted.
     * Range: [Integer](types/Integer.md)
 * [age_at_onset](age_at_onset.md)  <sub>0..1</sub>
     * Description: The age of onset for this condition.
     * Range: [Integer](types/Integer.md)
 * [age_at_resolution](age_at_resolution.md)  <sub>0..1</sub>
     * Description: The age at which this condition was resolved, abated or cured. Should be left empty in cases of current active status.
     * Range: [Integer](types/Integer.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
