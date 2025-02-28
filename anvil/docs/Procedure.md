
# Class: Procedure

Procedures

URI: [anvil:Procedure](https://anvilproject.org/acr-harmonized-data-model/Procedure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Procedure&#124;procedure_code:string%20%2B;procedure_source_value:string;age_at_event:float%20%3F;id(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Procedure&#124;procedure_code:string%20%2B;procedure_source_value:string;age_at_event:float%20%3F;id(i):string])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [procedure_code](procedure_code.md)  <sub>1..\*</sub>
     * Description: Procedure code should be from a recognized ontology preceded by a recognized curie. Multiple entries should reflect alternate codes for the same procedure. 
* CPT : https://bioregistry.io/registry/cpt

     * Range: [String](types/String.md)
 * [procedure_source_value](procedure_source_value.md)  <sub>1..1</sub>
     * Description: Original procedure text
     * Range: [String](types/String.md)
 * [age_at_event](age_at_event.md)  <sub>0..1</sub>
     * Description: The age in decimal years of the Subject at the time point which the assertion describes, | eg, age of onset or when a measurement was performed.
     * Range: [Float](types/Float.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
