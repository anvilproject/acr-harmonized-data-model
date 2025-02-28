
# Class: SourceData

Submitted data about a particular Subject.

URI: [anvil:SourceData](https://anvilproject.org/acr-harmonized-data-model/SourceData)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Demographics]-%20source_data%200..*>[SourceData&#124;code:uriorcurie%20%3F;display:string%20%3F;value_code:uriorcurie%20%3F;value_display:string%20%3F;value_number:float%20%3F;value_units:uriorcurie%20%3F;value_units_display:string%20%3F;id(i):string],[SubjectAssertion]-%20source_data%200..*>[SourceData],[AccessControlledRecord]^-[SourceData],[SubjectAssertion],[Demographics],[AccessPolicy],[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[Demographics]-%20source_data%200..*>[SourceData&#124;code:uriorcurie%20%3F;display:string%20%3F;value_code:uriorcurie%20%3F;value_display:string%20%3F;value_number:float%20%3F;value_units:uriorcurie%20%3F;value_units_display:string%20%3F;id(i):string],[SubjectAssertion]-%20source_data%200..*>[SourceData],[AccessControlledRecord]^-[SourceData],[SubjectAssertion],[Demographics],[AccessPolicy],[AccessControlledRecord])

## Parents

 *  is_a: [AccessControlledRecord](AccessControlledRecord.md) - Element for which specific access control restrictions apply.

## Referenced by Class

 *  **None** *[source_data](source_data.md)*  <sub>0..\*</sub>  **[SourceData](SourceData.md)**

## Attributes


### Own

 * [code](code.md)  <sub>0..1</sub>
     * Description: The structured term defining the meaning of the assertion.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [display](display.md)  <sub>0..1</sub>
     * Description: The friendly display string of the coded term
     * Range: [String](types/String.md)
 * [value_code](value_code.md)  <sub>0..1</sub>
     * Description: The structured term defining the value of the assertion.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [value_display](value_display.md)  <sub>0..1</sub>
     * Description: The friendly display string of the coded term for the value of the assertion.
     * Range: [String](types/String.md)
 * [value_number](value_number.md)  <sub>0..1</sub>
     * Description: The numeric value of the assertion.
     * Range: [Float](types/Float.md)
 * [value_units](value_units.md)  <sub>0..1</sub>
     * Description: The structured term defining the units of the value.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [value_units_display](value_units_display.md)  <sub>0..1</sub>
     * Description: The friendly display string of units of the value.
     * Range: [String](types/String.md)

### Inherited from AccessControlledRecord:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
 * [has_access_policy](has_access_policy.md)  <sub>0..1</sub>
     * Description: Which access policy applies to this element?
     * Range: [AccessPolicy](AccessPolicy.md)
