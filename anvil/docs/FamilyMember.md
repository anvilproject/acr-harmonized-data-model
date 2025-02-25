
# Class: FamilyMember

Family

URI: [anvil:FamilyMember](https://anvilproject.org/acr-harmonized-data-model/FamilyMember)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[FamilyMember&#124;family_id_fk:string%20%3F;family_member_id:string;other_family_member_id:string%20%3F;relationship_code:string%20%3F;id(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[FamilyMember&#124;family_id_fk:string%20%3F;family_member_id:string;other_family_member_id:string%20%3F;relationship_code:string%20%3F;id(i):string])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [family_id_fk](family_id_fk.md)  <sub>0..1</sub>
     * Description: Family Identifier
     * Range: [String](types/String.md)
 * [family_member_id](family_member_id.md)  <sub>1..1</sub>
     * Description: Family Member ID indicating presence in the family
     * Range: [String](types/String.md)
 * [other_family_member_id](other_family_member_id.md)  <sub>0..1</sub>
     * Description: Other member of the same family to which there is a relationship being described
     * Range: [String](types/String.md)
 * [relationship_code](relationship_code.md)  <sub>0..1</sub>
     * Description: Relationship of the "Family Member" to the "Other Family Member" (i.e. mother, father, etc). This is required if other_family_member_id is present. Code must be from the HL7 [FamilyMember ValueSet](https://terminology.hl7.org/6.2.0/ValueSet-v3-FamilyMember.html)

     * Range: [String](types/String.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
