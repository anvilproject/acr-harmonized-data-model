
# Class: Family

Family

URI: [anvil:Family](https://anvilproject.org/acr-harmonized-data-model/Family)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Family&#124;family_external_id:string%20*;family_type:EnumFamilyType%20%3F;family_description:string%20%3F;consanguinity:EnumConsanguinityAssertion%20%3F;family_study_focus:string%20%3F;id(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Family&#124;family_external_id:string%20*;family_type:EnumFamilyType%20%3F;family_description:string%20%3F;consanguinity:EnumConsanguinityAssertion%20%3F;family_study_focus:string%20%3F;id(i):string])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [family_external_id](family_external_id.md)  <sub>0..\*</sub>
     * Description: Other study specific study identifiers
     * Range: [String](types/String.md)
 * [family_type](family_type.md)  <sub>0..1</sub>
     * Description: Describes the 'type' of study family, eg, trio.
     * Range: [EnumFamilyType](EnumFamilyType.md)
 * [family_description](family_description.md)  <sub>0..1</sub>
     * Description: Free title describing the study family, such as potential inheritance or details about consanguinity
     * Range: [String](types/String.md)
 * [consanguinity](consanguinity.md)  <sub>0..1</sub>
     * Description: Is there known or suspected consanguinity in this study family?
     * Range: [EnumConsanguinityAssertion](EnumConsanguinityAssertion.md)
 * [family_study_focus](family_study_focus.md)  <sub>0..1</sub>
     * Description: What is this study family investigating? EG, a specific condition. The code should be prefixed with a recognizable curie. 

     * Range: [String](types/String.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
