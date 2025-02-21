
# Class: DataAccessType

Research Access Policy

URI: [anvil:DataAccessType](https://anvilproject.org/acr-harmonized-data-model/DataAccessType)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[DataAccessType&#124;data_access_type_id:string;data_access_type:enum_access_type%20*;disease_use_limitation:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[DataAccessType&#124;data_access_type_id:string;data_access_type:enum_access_type%20*;disease_use_limitation:string%20%3F])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [data_access_type_id](data_access_type_id.md)  <sub>1..1</sub>
     * Description: Data Access Type ID
     * Range: [String](types/String.md)
 * [data_access_type](data_access_type.md)  <sub>0..\*</sub>
     * Description: Data Access Type
     * Range: [enum_access_type](enum_access_type.md)
 * [disease_use_limitation](disease_use_limitation.md)  <sub>0..1</sub>
     * Description: Disease Use Limitations
     * Range: [String](types/String.md)
