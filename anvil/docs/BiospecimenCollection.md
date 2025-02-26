
# Class: BiospecimenCollection

Biospecimen Collection

URI: [anvil:BiospecimenCollection](https://anvilproject.org/acr-harmonized-data-model/BiospecimenCollection)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[BiospecimenCollection&#124;age_at_collection:integer%20%3F;method:EnumSampleCollectionMethod%20%3F;site:EnumSite%20%3F;spatial_qualifier:EnumSpatialQualifiers%20%3F;laterality:EnumLaterality%20%3F;id(i):string])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[BiospecimenCollection&#124;age_at_collection:integer%20%3F;method:EnumSampleCollectionMethod%20%3F;site:EnumSite%20%3F;spatial_qualifier:EnumSpatialQualifiers%20%3F;laterality:EnumLaterality%20%3F;id(i):string])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

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

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
