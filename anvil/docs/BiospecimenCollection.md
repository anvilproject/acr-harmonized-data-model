
# Class: BiospecimenCollection

Biospecimen Collection

URI: [anvil:BiospecimenCollection](https://anvilproject.org/acr-harmonized-data-model/BiospecimenCollection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[BiospecimenCollection&#124;biospecimen_collection_id:string;participant_id:string;age_at_collection:integer%20%3F;method:EnumSampleCollectionMethod%20%3F;site:EnumSite%20%3F;spatial_qualifier:EnumSpatialQualifiers%20%3F;laterality:EnumLaterality%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[BiospecimenCollection&#124;biospecimen_collection_id:string;participant_id:string;age_at_collection:integer%20%3F;method:EnumSampleCollectionMethod%20%3F;site:EnumSite%20%3F;spatial_qualifier:EnumSpatialQualifiers%20%3F;laterality:EnumLaterality%20%3F])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [biospecimen_collection_id](biospecimen_collection_id.md)  <sub>1..1</sub>
     * Description: Biospecimen Collection ID
     * Range: [String](types/String.md)
 * [participant_id](participant_id.md)  <sub>1..1</sub>
     * Description: ID associated with the Participant
     * Range: [String](types/String.md)
 * [age_at_collection](age_at_collection.md)  <sub>0..1</sub>
     * Description: The age at which this biospecimen was collected.
     * Range: [Integer](types/Integer.md)
 * [method](method.md)  <sub>0..1</sub>
     * Description: The approach used to collect the biospecimen.
     * Range: [EnumSampleCollectionMethod](EnumSampleCollectionMethod.md)
 * [site](site.md)  <sub>0..1</sub>
     * Description: The location of the specimen collection.
     * Range: [EnumSite](EnumSite.md)
 * [spatial_qualifier](spatial_qualifier.md)  <sub>0..1</sub>
     * Description: Any spatial/location qualifiers
     * Range: [EnumSpatialQualifiers](EnumSpatialQualifiers.md)
 * [laterality](laterality.md)  <sub>0..1</sub>
     * Description: Laterality information for the site
     * Range: [EnumLaterality](EnumLaterality.md)
