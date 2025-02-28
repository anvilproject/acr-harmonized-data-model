
# Class: Subject

This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity.

URI: [anvil:Subject](https://anvilproject.org/acr-harmonized-data-model/Subject)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectAssertion],[SubjectAssertion]<has_assertion%200..*-++[Subject&#124;subject_type:EnumSubjectType;organism_type:string%20%3F;id(i):string],[Sample]<has_sample%200..*-++[Subject],[Subject]^-[Participant],[AccessControlledRecord]^-[Subject],[Sample],[Participant],[AccessPolicy],[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectAssertion],[SubjectAssertion]<has_assertion%200..*-++[Subject&#124;subject_type:EnumSubjectType;organism_type:string%20%3F;id(i):string],[Sample]<has_sample%200..*-++[Subject],[Subject]^-[Participant],[AccessControlledRecord]^-[Subject],[Sample],[Participant],[AccessPolicy],[AccessControlledRecord])

## Parents

 *  is_a: [AccessControlledRecord](AccessControlledRecord.md) - Element for which specific access control restrictions apply.

## Children

 * [Participant](Participant.md) - Basic participant demographics

## Referenced by Class


## Attributes


### Own

 * [subject_type](subject_type.md)  <sub>1..1</sub>
     * Description: Type of entity this record represents
     * Range: [EnumSubjectType](EnumSubjectType.md)
 * [organism_type](organism_type.md)  <sub>0..1</sub>
     * Description: Organism Type Label
     * Range: [String](types/String.md)
 * [has_sample](has_sample.md)  <sub>0..\*</sub>
     * Description: Which samples were collected or processed for this Subject?
     * Range: [Sample](Sample.md)
 * [has_assertion](has_assertion.md)  <sub>0..\*</sub>
     * Description: Which assertions are made about this Subject?
     * Range: [SubjectAssertion](SubjectAssertion.md)

### Inherited from AccessControlledRecord:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
 * [has_access_policy](has_access_policy.md)  <sub>0..1</sub>
     * Description: Which access policy applies to this element?
     * Range: [AccessPolicy](AccessPolicy.md)
