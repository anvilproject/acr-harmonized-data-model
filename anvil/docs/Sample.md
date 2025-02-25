
# Class: Sample

Biospecimen data

URI: [anvil:Sample](https://anvilproject.org/acr-harmonized-data-model/Sample)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Participant]-%20has_sample%200..*>[Sample&#124;parent_sample_id:string%20%3F;biospecimen_collection_id_fk:string;sample_type:string;processing:string%20*;availablity_status:EnumAvailabilityStatus%20%3F;storage_method:string%20%3F;quantity:string%20%3F;id(i):string],[Thing]^-[Sample],[Participant])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Participant]-%20has_sample%200..*>[Sample&#124;parent_sample_id:string%20%3F;biospecimen_collection_id_fk:string;sample_type:string;processing:string%20*;availablity_status:EnumAvailabilityStatus%20%3F;storage_method:string%20%3F;quantity:string%20%3F;id(i):string],[Thing]^-[Sample],[Participant])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Referenced by Class

 *  **None** *[has_sample](has_sample.md)*  <sub>0..\*</sub>  **[Sample](Sample.md)**

## Attributes


### Own

 * [parent_sample_id](parent_sample_id.md)  <sub>0..1</sub>
     * Description: Parent Sample ID
     * Range: [String](types/String.md)
 * [biospecimen_collection_id_fk](biospecimen_collection_id_fk.md)  <sub>1..1</sub>
     * Description: ID associated with the Biospecimen Collection event.
     * Range: [String](types/String.md)
 * [sample_type](sample_type.md)  <sub>1..1</sub>
     * Description: Curied code associated the type of material of which this Sample is comprised
     * Range: [String](types/String.md)
 * [processing](processing.md)  <sub>0..\*</sub>
     * Description: Curied code associated processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample
     * Range: [String](types/String.md)
 * [availablity_status](availablity_status.md)  <sub>0..1</sub>
     * Description: Can this Sample be requested for further analysis?
     * Range: [EnumAvailabilityStatus](EnumAvailabilityStatus.md)
 * [storage_method](storage_method.md)  <sub>0..1</sub>
     * Description: Curied code indicating how is the Sample stored, eg, Frozen or with additives
     * Range: [String](types/String.md)
 * [quantity](quantity.md)  <sub>0..1</sub>
     * Description: The total quantity of the specimen
     * Range: [String](types/String.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
