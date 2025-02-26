
# Class: AccessControlledRecord

Element for which specific access control restrictions apply.

URI: [anvil:AccessControlledRecord](https://anvilproject.org/acr-harmonized-data-model/AccessControlledRecord)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[AccessPolicy],[AccessPolicy]<has_access_policy%200..1-%20[AccessControlledRecord&#124;id(i):string],[AccessControlledRecord]^-[Subject],[Thing]^-[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Subject],[AccessPolicy],[AccessPolicy]<has_access_policy%200..1-%20[AccessControlledRecord&#124;id(i):string],[AccessControlledRecord]^-[Subject],[Thing]^-[AccessControlledRecord])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Children

 * [Subject](Subject.md) - This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity.

## Referenced by Class


## Attributes


### Own

 * [has_access_policy](has_access_policy.md)  <sub>0..1</sub>
     * Description: Which access policy applies to this element?
     * Range: [AccessPolicy](AccessPolicy.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
