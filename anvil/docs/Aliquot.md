
# Class: Aliquot

Represent exact tubes or total amounts available of a Sample.

URI: [anvil:Aliquot](https://anvilproject.org/acr-harmonized-data-model/Aliquot)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Aliquot&#124;aliquot_id:string;sample_id_fk:string;sample_availability_status:EnumAvailabilityStatus%20%3F;sample_volume:float%20%3F;sample_volume_unit:string%20%3F;sample_concentration:float%20%3F;sample_concentration_unit:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[Aliquot&#124;aliquot_id:string;sample_id_fk:string;sample_availability_status:EnumAvailabilityStatus%20%3F;sample_volume:float%20%3F;sample_volume_unit:string%20%3F;sample_concentration:float%20%3F;sample_concentration_unit:string%20%3F])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [aliquot_id](aliquot_id.md)  <sub>1..1</sub>
     * Description: Aliquot ID
     * Range: [String](types/String.md)
 * [sample_id_fk](sample_id_fk.md)  <sub>1..1</sub>
     * Description: Sample ID the aliquot is associated with
     * Range: [String](types/String.md)
 * [sample_availability_status](sample_availability_status.md)  <sub>0..1</sub>
     * Description: Can this Sample be requested for further analysis
     * Range: [EnumAvailabilityStatus](EnumAvailabilityStatus.md)
 * [sample_volume](sample_volume.md)  <sub>0..1</sub>
     * Description: What is the volume of the Aliquot?
     * Range: [Float](types/Float.md)
 * [sample_volume_unit](sample_volume_unit.md)  <sub>0..1</sub>
     * Description: Units associated with the volume? UCUM coding preferred (with curie, UCUM)
     * Range: [String](types/String.md)
 * [sample_concentration](sample_concentration.md)  <sub>0..1</sub>
     * Description: What is the concentration of the analyte in the Aliquot?
     * Range: [Float](types/Float.md)
 * [sample_concentration_unit](sample_concentration_unit.md)  <sub>0..1</sub>
     * Description: Units associated with the concentration of the analyte in the Aliquot? UCUM coding preferred (with curie, UCUM)
     * Range: [String](types/String.md)
