
# Class: SubjectAssertion

Assertion about a particular Subject. May include Conditions, Measurements, etc.

URI: [anvil:SubjectAssertion](https://anvilproject.org/acr-harmonized-data-model/SubjectAssertion)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]++-%20has_assertion%200..*>[SubjectAssertion&#124;assertion_type:EnumAssertionType%20%3F;code:uriorcurie%20%3F;display:string%20%3F;source_code:uriorcurie%20%3F;source_display:string%20%3F;value_code:uriorcurie%20%3F;value_display:string%20%3F;value_number:float%20%3F;value_units:uriorcurie%20%3F;age_at_assertion:float%20%3F;age_at_event:float%20%3F;age_at_resolution:float%20%3F;id(i):string],[AccessControlledRecord]^-[SubjectAssertion],[Subject],[AccessPolicy],[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[Subject]++-%20has_assertion%200..*>[SubjectAssertion&#124;assertion_type:EnumAssertionType%20%3F;code:uriorcurie%20%3F;display:string%20%3F;source_code:uriorcurie%20%3F;source_display:string%20%3F;value_code:uriorcurie%20%3F;value_display:string%20%3F;value_number:float%20%3F;value_units:uriorcurie%20%3F;age_at_assertion:float%20%3F;age_at_event:float%20%3F;age_at_resolution:float%20%3F;id(i):string],[AccessControlledRecord]^-[SubjectAssertion],[Subject],[AccessPolicy],[AccessControlledRecord])

## Parents

 *  is_a: [AccessControlledRecord](AccessControlledRecord.md) - Element for which specific access control restrictions apply.

## Referenced by Class

 *  **None** *[has_assertion](has_assertion.md)*  <sub>0..\*</sub>  **[SubjectAssertion](SubjectAssertion.md)**

## Attributes


### Own

 * [➞assertion_type](subjectAssertion__assertion_type.md)  <sub>0..1</sub>
     * Description: The semantic type of the resource, eg, Condition.
     * Range: [EnumAssertionType](EnumAssertionType.md)
 * [➞code](subjectAssertion__code.md)  <sub>0..1</sub>
     * Description: The structured term defining the meaning of the assertion.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞display](subjectAssertion__display.md)  <sub>0..1</sub>
     * Description: The friendly display string of the coded term
     * Range: [String](types/String.md)
 * [➞source_code](subjectAssertion__source_code.md)  <sub>0..1</sub>
     * Description: The structured term defining the meaning of the assertion as provided by the source.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞source_display](subjectAssertion__source_display.md)  <sub>0..1</sub>
     * Description: The friendly display string of the coded term as provided by the source.
     * Range: [String](types/String.md)
 * [➞value_code](subjectAssertion__value_code.md)  <sub>0..1</sub>
     * Description: The structured term defining the value of the assertion.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞value_display](subjectAssertion__value_display.md)  <sub>0..1</sub>
     * Description: The friendly display string of the coded term for the value of the assertion.
     * Range: [String](types/String.md)
 * [➞value_number](subjectAssertion__value_number.md)  <sub>0..1</sub>
     * Description: The numeric value of the assertion.
     * Range: [Float](types/Float.md)
 * [➞value_units](subjectAssertion__value_units.md)  <sub>0..1</sub>
     * Description: The structured term defining the units of the value.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞age_at_assertion](subjectAssertion__age_at_assertion.md)  <sub>0..1</sub>
     * Description: The age in decimal years of the Subject when the assertion was made.
     * Range: [Float](types/Float.md)
 * [➞age_at_event](subjectAssertion__age_at_event.md)  <sub>0..1</sub>
     * Description: The age in decimal years of the Subject at the time point which the assertion describes, | eg, age of onset or when a measurement was performed.
     * Range: [Float](types/Float.md)
 * [➞age_at_resolution](subjectAssertion__age_at_resolution.md)  <sub>0..1</sub>
     * Description: The age in decimal years of the Subject when the asserted state was resolved.
     * Range: [Float](types/Float.md)

### Inherited from AccessControlledRecord:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
 * [has_access_policy](has_access_policy.md)  <sub>0..1</sub>
     * Description: Which access policy applies to this element?
     * Range: [AccessPolicy](AccessPolicy.md)
