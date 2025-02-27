
# Class: Thing

Highest Level Class

URI: [anvil:Thing](https://anvilproject.org/acr-harmonized-data-model/Thing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing&#124;id:string]^-[Study],[Thing]^-[Sample],[Thing]^-[Procedure],[Thing]^-[Measurement],[Thing]^-[FamilyMember],[Thing]^-[Family],[Thing]^-[BiospecimenCollection],[Thing]^-[Aliquot],[Thing]^-[AccessPolicy],[Thing]^-[AccessControlledRecord],[Study],[Sample],[Procedure],[Measurement],[FamilyMember],[Family],[BiospecimenCollection],[Aliquot],[AccessPolicy],[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing&#124;id:string]^-[Study],[Thing]^-[Sample],[Thing]^-[Procedure],[Thing]^-[Measurement],[Thing]^-[FamilyMember],[Thing]^-[Family],[Thing]^-[BiospecimenCollection],[Thing]^-[Aliquot],[Thing]^-[AccessPolicy],[Thing]^-[AccessControlledRecord],[Study],[Sample],[Procedure],[Measurement],[FamilyMember],[Family],[BiospecimenCollection],[Aliquot],[AccessPolicy],[AccessControlledRecord])

## Children

 * [AccessControlledRecord](AccessControlledRecord.md) - Element for which specific access control restrictions apply.
 * [AccessPolicy](AccessPolicy.md) - Describes the access required for a given element of data.
 * [Aliquot](Aliquot.md) - Represent exact tubes or total amounts available of a Sample.
 * [BiospecimenCollection](BiospecimenCollection.md) - Biospecimen Collection
 * [Family](Family.md) - Family
 * [FamilyMember](FamilyMember.md) - Family
 * [Measurement](Measurement.md) - Measurements
 * [Procedure](Procedure.md) - Procedures
 * [Sample](Sample.md) - Biospecimen data
 * [Study](Study.md) - Study Meta Data

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
