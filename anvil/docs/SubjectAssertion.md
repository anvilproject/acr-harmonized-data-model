
# Class: SubjectAssertion

Generic template for linking information with a given Subject.

URI: [anvil:SubjectAssertion](https://anvilproject.org/acr-harmonized-data-model/SubjectAssertion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Any]<source_value%200..1-++[SubjectAssertion&#124;age_at_assertion:integer%20%3F;id(i):string],[CodedTerm]<source_assertion%200..1-++[SubjectAssertion],[Any]<value%200..1-++[SubjectAssertion],[CodedTerm]<assertion%200..1-++[SubjectAssertion],[Subject]-%20subject_assertion%200..*>[SubjectAssertion],[SubjectAssertion]^-[ConditionAssertion],[Thing]^-[SubjectAssertion],[Subject],[ConditionAssertion],[CodedTerm],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Any]<source_value%200..1-++[SubjectAssertion&#124;age_at_assertion:integer%20%3F;id(i):string],[CodedTerm]<source_assertion%200..1-++[SubjectAssertion],[Any]<value%200..1-++[SubjectAssertion],[CodedTerm]<assertion%200..1-++[SubjectAssertion],[Subject]-%20subject_assertion%200..*>[SubjectAssertion],[SubjectAssertion]^-[ConditionAssertion],[Thing]^-[SubjectAssertion],[Subject],[ConditionAssertion],[CodedTerm],[Any])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Children

 * [ConditionAssertion](ConditionAssertion.md) - Study Meta Data

## Referenced by Class

 *  **None** *[subject_assertion](subject_assertion.md)*  <sub>0..\*</sub>  **[SubjectAssertion](SubjectAssertion.md)**

## Attributes


### Own

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

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
