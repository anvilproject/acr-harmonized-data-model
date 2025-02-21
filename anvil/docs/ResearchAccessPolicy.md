
# Class: ResearchAccessPolicy

Research Access Policy

URI: [anvil:ResearchAccessPolicy](https://anvilproject.org/acr-harmonized-data-model/ResearchAccessPolicy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[ResearchAccessPolicy&#124;access_policy_id:string;access_policy_code:enum_access_code%20%2B;description:string;website:string%20%3F])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Thing]^-[ResearchAccessPolicy&#124;access_policy_id:string;access_policy_code:enum_access_code%20%2B;description:string;website:string%20%3F])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [access_policy_id](access_policy_id.md)  <sub>1..1</sub>
     * Description: Access Policy ID
     * Range: [String](types/String.md)
 * [access_policy_code](access_policy_code.md)  <sub>1..\*</sub>
     * Description: Access Policy Code
     * Range: [enum_access_code](enum_access_code.md)
 * [description](description.md)  <sub>1..1</sub>
     * Description: Description
     * Range: [String](types/String.md)
 * [website](website.md)  <sub>0..1</sub>
     * Description: Website
     * Range: [String](types/String.md)
