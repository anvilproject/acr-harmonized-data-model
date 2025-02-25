
# Class: AccessPolicy

Describes the access required for a given element of data.

URI: [anvil:AccessPolicy](https://anvilproject.org/acr-harmonized-data-model/AccessPolicy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[AccessControlledRecord]-%20has_access_policy%200..1>[AccessPolicy&#124;data_access_type:enum_access_type%20*;access_policy_code:enum_access_code%20%2B;disease_use_limitation:string%20%3F;description:string;website:string%20%3F;id(i):string],[Thing]^-[AccessPolicy],[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[AccessControlledRecord]-%20has_access_policy%200..1>[AccessPolicy&#124;data_access_type:enum_access_type%20*;access_policy_code:enum_access_code%20%2B;disease_use_limitation:string%20%3F;description:string;website:string%20%3F;id(i):string],[Thing]^-[AccessPolicy],[AccessControlledRecord])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Referenced by Class

 *  **None** *[has_access_policy](has_access_policy.md)*  <sub>0..1</sub>  **[AccessPolicy](AccessPolicy.md)**

## Attributes


### Own

 * [data_access_type](data_access_type.md)  <sub>0..\*</sub>
     * Description: Data Access Type
     * Range: [enum_access_type](enum_access_type.md)
 * [access_policy_code](access_policy_code.md)  <sub>1..\*</sub>
     * Description: Access Policy Code
     * Range: [enum_access_code](enum_access_code.md)
 * [disease_use_limitation](disease_use_limitation.md)  <sub>0..1</sub>
     * Description: Disease Use Limitations
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>1..1</sub>
     * Description: Description
     * Range: [String](types/String.md)
 * [website](website.md)  <sub>0..1</sub>
     * Description: Website
     * Range: [String](types/String.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
