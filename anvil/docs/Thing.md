
# Class: Thing

Highest Level Class

URI: [anvil:Thing](https://anvilproject.org/acr-harmonized-data-model/Thing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyParticipant],[Thing&#124;id:string]^-[StudyParticipant],[Thing]^-[Study],[Thing]^-[Sample],[Thing]^-[Procedure],[Thing]^-[Participant],[Thing]^-[Measurement],[Thing]^-[FamilyMember],[Thing]^-[Family],[Thing]^-[ConditionAssertion],[Thing]^-[BiospecimenCollection],[Thing]^-[Aliquot],[Thing]^-[AccessPolicy],[Thing]^-[AccessControlledRecord],[Study],[Sample],[Procedure],[Participant],[Measurement],[FamilyMember],[Family],[ConditionAssertion],[BiospecimenCollection],[Aliquot],[AccessPolicy],[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[StudyParticipant],[Thing&#124;id:string]^-[StudyParticipant],[Thing]^-[Study],[Thing]^-[Sample],[Thing]^-[Procedure],[Thing]^-[Participant],[Thing]^-[Measurement],[Thing]^-[FamilyMember],[Thing]^-[Family],[Thing]^-[ConditionAssertion],[Thing]^-[BiospecimenCollection],[Thing]^-[Aliquot],[Thing]^-[AccessPolicy],[Thing]^-[AccessControlledRecord],[Study],[Sample],[Procedure],[Participant],[Measurement],[FamilyMember],[Family],[ConditionAssertion],[BiospecimenCollection],[Aliquot],[AccessPolicy],[AccessControlledRecord])

## Children

 * [AccessControlledRecord](AccessControlledRecord.md) - Entity for which specific access control restrictions apply.
 * [AccessPolicy](AccessPolicy.md) - Describes the access required for a given element of data.
 * [Aliquot](Aliquot.md) - Represent exact tubes or total amounts available of a Sample.
 * [BiospecimenCollection](BiospecimenCollection.md) - Biospecimen Collection
 * [ConditionAssertion](ConditionAssertion.md) - Study Meta Data
 * [Family](Family.md) - Family
 * [FamilyMember](FamilyMember.md) - Family
 * [Measurement](Measurement.md) - Measurements
 * [Participant](Participant.md) - Basic participant demographics
 * [Procedure](Procedure.md) - Procedures
 * [Sample](Sample.md) - Biospecimen data
 * [Study](Study.md) - Study Meta Data
 * [StudyParticipant](StudyParticipant.md) - Research

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
