
# Class: ConditionAssertion

Study Meta Data

URI: [anvil:ConditionAssertion](https://anvilproject.org/acr-harmonized-data-model/ConditionAssertion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectAssertion],[SubjectAssertion]^-[ConditionAssertion&#124;condition_type:EnumConditionType;age_at_onset:integer%20%3F;age_at_resolution:integer%20%3F;age_at_assertion(i):integer%20%3F;id(i):string],[CodedTerm],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectAssertion],[SubjectAssertion]^-[ConditionAssertion&#124;condition_type:EnumConditionType;age_at_onset:integer%20%3F;age_at_resolution:integer%20%3F;age_at_assertion(i):integer%20%3F;id(i):string],[CodedTerm],[Any])

## Parents

 *  is_a: [SubjectAssertion](SubjectAssertion.md) - Generic template for linking information with a given Subject.

## Attributes


### Own

 * [condition_type](condition_type.md)  <sub>1..1</sub>
     * Description: Does this condition represent a specific "type" of condition, such as "Phenotypic Feature" vs "Disease" in a rare disease setting.
     * Range: [EnumConditionType](EnumConditionType.md)
 * [age_at_onset](age_at_onset.md)  <sub>0..1</sub>
     * Description: The age of onset for this condition.
     * Range: [Integer](types/Integer.md)
 * [age_at_resolution](age_at_resolution.md)  <sub>0..1</sub>
     * Description: The age at which this condition was resolved, abated or cured. Should be left empty in cases of current active status.
     * Range: [Integer](types/Integer.md)

### Inherited from SubjectAssertion:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
 * [age_at_assertion](age_at_assertion.md)  <sub>0..1</sub>
     * Description: The age at which this condition is being asserted.
     * Range: [Integer](types/Integer.md)
 * [assertion](assertion.md)  <sub>0..1</sub>
     * Description: The assertion that is being made.
     * Range: [CodedTerm](CodedTerm.md)
 * [value](value.md)  <sub>0..1</sub>
     * Description: The value of the assertion that is being made.
     * Range: [Any](Any.md)
 * [source_assertion](source_assertion.md)  <sub>0..1</sub>
     * Description: The assertion that is being made as originally recorded.
     * Range: [CodedTerm](CodedTerm.md)
 * [source_value](source_value.md)  <sub>0..1</sub>
     * Description: The value of the assertion that is being made as originally recoded.
     * Range: [Any](Any.md)
