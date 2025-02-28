
# Class: Demographics

Basic participant demographics summary

URI: [anvil:Demographics](https://anvilproject.org/acr-harmonized-data-model/Demographics)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SourceData],[SourceData]<source_data%200..*-%20[Demographics&#124;date_of_birth:integer%20%3F;date_of_birth_type:EnumDateOfBirthType%20%3F;sex:EnumSex;sex_display:string;race:EnumRace%20%2B;race_display:string;ethnicity:EnumEthnicity;ethnicity_display:string;age_at_last_vital_status:integer%20%3F;vital_status:EnumVitalStatus%20%3F;id(i):string],[Subject]++-%20has_demographics%200..1>[Demographics],[AccessControlledRecord]^-[Demographics],[Subject],[AccessPolicy],[AccessControlledRecord])](https://yuml.me/diagram/nofunky;dir:TB/class/[SourceData],[SourceData]<source_data%200..*-%20[Demographics&#124;date_of_birth:integer%20%3F;date_of_birth_type:EnumDateOfBirthType%20%3F;sex:EnumSex;sex_display:string;race:EnumRace%20%2B;race_display:string;ethnicity:EnumEthnicity;ethnicity_display:string;age_at_last_vital_status:integer%20%3F;vital_status:EnumVitalStatus%20%3F;id(i):string],[Subject]++-%20has_demographics%200..1>[Demographics],[AccessControlledRecord]^-[Demographics],[Subject],[AccessPolicy],[AccessControlledRecord])

## Parents

 *  is_a: [AccessControlledRecord](AccessControlledRecord.md) - Element for which specific access control restrictions apply.

## Referenced by Class

 *  **None** *[has_demographics](has_demographics.md)*  <sub>0..1</sub>  **[Demographics](Demographics.md)**

## Attributes


### Own

 * [date_of_birth](date_of_birth.md)  <sub>0..1</sub>
     * Description: Date at which the individual was born. May be impacted by privacy rules described in date_of_birth_type.
     * Range: [Integer](types/Integer.md)
 * [date_of_birth_type](date_of_birth_type.md)  <sub>0..1</sub>
     * Description: Privacy rule modification applied to date_of_birth.
     * Range: [EnumDateOfBirthType](EnumDateOfBirthType.md)
 * [sex](sex.md)  <sub>1..1</sub>
     * Description: Sex of the individual
     * Range: [EnumSex](EnumSex.md)
 * [sex_display](sex_display.md)  <sub>1..1</sub>
     * Description: The friendly display string of the coded term for Sex
     * Range: [String](types/String.md)
 * [race](race.md)  <sub>1..\*</sub>
     * Description: Reported race as defined by the 1997 OMB directives.
     * Range: [EnumRace](EnumRace.md)
 * [race_display](race_display.md)  <sub>1..1</sub>
     * Description: The friendly display string of the coded term(s) for Race
     * Range: [String](types/String.md)
 * [ethnicity](ethnicity.md)  <sub>1..1</sub>
     * Description: Reported ethnicity as defined by the 1997 OMB directives.
     * Range: [EnumEthnicity](EnumEthnicity.md)
 * [ethnicity_display](ethnicity_display.md)  <sub>1..1</sub>
     * Description: The friendly display string of the coded term for Ethnicity
     * Range: [String](types/String.md)
 * [age_at_last_vital_status](age_at_last_vital_status.md)  <sub>0..1</sub>
     * Description: Age at last vital status in decimal years.
     * Range: [Integer](types/Integer.md)
 * [vital_status](vital_status.md)  <sub>0..1</sub>
     * Description: Vital Status
     * Range: [EnumVitalStatus](EnumVitalStatus.md)
 * [source_data](source_data.md)  <sub>0..\*</sub>
     * Description: The sources from which this assertion was derived
     * Range: [SourceData](SourceData.md)

### Inherited from AccessControlledRecord:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
 * [has_access_policy](has_access_policy.md)  <sub>0..1</sub>
     * Description: Which access policy applies to this element?
     * Range: [AccessPolicy](AccessPolicy.md)
