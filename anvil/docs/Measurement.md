
# Class: Measurement

Measurements

URI: [anvil:Measurement](https://anvilproject.org/acr-harmonized-data-model/Measurement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Measurement&#124;participant_id:string;measurement_code:string%20%2B;measurement_unit:string;measurement_value_code:EnumMeasurementValueCode%20%3F;measurement_source_value:string;age_at_observation:integer%20%3F;id(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Measurement&#124;participant_id:string;measurement_code:string%20%2B;measurement_unit:string;measurement_value_code:EnumMeasurementValueCode%20%3F;measurement_source_value:string;age_at_observation:integer%20%3F;id(i):string])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [participant_id](participant_id.md)  <sub>1..1</sub>
     * Description: ID associated with the Participant
     * Range: [String](types/String.md)
 * [measurement_code](measurement_code.md)  <sub>1..\*</sub>
     * Description: Measurement code should be from a recognized ontology preceded by a recognized curie. Multiple entries should reflect alternate codes for the same measurement. 
* LOINC : https://bioregistry.io/registry/loinc

     * Range: [String](types/String.md)
 * [measurement_unit](measurement_unit.md)  <sub>1..1</sub>
     * Description: UCUM Unit associated with the field
     * Range: [String](types/String.md)
 * [measurement_value_code](measurement_value_code.md)  <sub>0..1</sub>
     * Description: Code indicating measurement value such as positive, negative, etc.
     * Range: [EnumMeasurementValueCode](EnumMeasurementValueCode.md)
 * [measurement_source_value](measurement_source_value.md)  <sub>1..1</sub>
     * Description: Original measurement text
     * Range: [String](types/String.md)
 * [age_at_observation](age_at_observation.md)  <sub>0..1</sub>
     * Description: Age of participant when measurement was taken/recorded
     * Range: [Integer](types/Integer.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
