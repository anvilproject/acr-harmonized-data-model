
# Class: Procedure

Procedures

URI: [anvil:Procedure](https://anvilproject.org/acr-harmonized-data-model/Procedure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Procedure&#124;participant_id:string;procedure_code:string%20%2B;procedure_source_value:string;procedure_detail:EnumProcedureDetail%20%3F;age_at_observation:integer%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Procedure&#124;participant_id:string;procedure_code:string%20%2B;procedure_source_value:string;procedure_detail:EnumProcedureDetail%20%3F;age_at_observation:integer%20%3F])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [participant_id](participant_id.md)  <sub>1..1</sub>
     * Description: ID associated with the Participant
     * Range: [String](types/String.md)
 * [procedure_code](procedure_code.md)  <sub>1..\*</sub>
     * Description: Procedure code should be from a recognized ontology preceded by a recognized curie. Multiple entries should reflect alternate codes for the same procedure. 
* CPT : https://bioregistry.io/registry/cpt

     * Range: [String](types/String.md)
 * [procedure_source_value](procedure_source_value.md)  <sub>1..1</sub>
     * Description: Original procedure text
     * Range: [String](types/String.md)
 * [procedure_detail](procedure_detail.md)  <sub>0..1</sub>
     * Description: Non-procedure value indicating procedure status
     * Range: [EnumProcedureDetail](EnumProcedureDetail.md)
 * [age_at_observation](age_at_observation.md)  <sub>0..1</sub>
     * Description: Age of participant when measurement was taken/recorded
     * Range: [Integer](types/Integer.md)
