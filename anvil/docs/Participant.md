
# Class: Participant

Basic participant demographics

URI: [anvil:Participant](https://anvilproject.org/acr-harmonized-data-model/Participant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Sample],[Sample]<has_sample%200..*-%20[Participant&#124;external_id:uriorcurie%20*;organism_type:string%20%3F;donor_type:enum_donor_type%20%3F;date_of_birth:integer%20%3F;date_of_birth_type:EnumDateOfBirthType%20%3F;phenotypic_sex:enum_sex;phenotypic_sex_source_value:string%20%3F;race:enum_race;race_source_value:string%20%3F;ethnicity:enum_ethnicity;ethnicity_source_value:string%20%3F;age_at_last_vital_status:integer%20%3F;vital_status:enum_vital_status%20%3F;id(i):string],[Thing]^-[Participant])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Sample],[Sample]<has_sample%200..*-%20[Participant&#124;external_id:uriorcurie%20*;organism_type:string%20%3F;donor_type:enum_donor_type%20%3F;date_of_birth:integer%20%3F;date_of_birth_type:EnumDateOfBirthType%20%3F;phenotypic_sex:enum_sex;phenotypic_sex_source_value:string%20%3F;race:enum_race;race_source_value:string%20%3F;ethnicity:enum_ethnicity;ethnicity_source_value:string%20%3F;age_at_last_vital_status:integer%20%3F;vital_status:enum_vital_status%20%3F;id(i):string],[Thing]^-[Participant])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
 * [external_id](external_id.md)  <sub>0..\*</sub>
     * Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [organism_type](organism_type.md)  <sub>0..1</sub>
     * Description: Organism Type Label
     * Range: [String](types/String.md)
 * [donor_type](donor_type.md)  <sub>0..1</sub>
     * Range: [enum_donor_type](enum_donor_type.md)
 * [date_of_birth](date_of_birth.md)  <sub>0..1</sub>
     * Range: [Integer](types/Integer.md)
 * [date_of_birth_type](date_of_birth_type.md)  <sub>0..1</sub>
     * Range: [EnumDateOfBirthType](EnumDateOfBirthType.md)
 * [phenotypic_sex](phenotypic_sex.md)  <sub>1..1</sub>
     * Description: Sex of the Participant
     * Range: [enum_sex](enum_sex.md)
 * [phenotypic_sex_source_value](phenotypic_sex_source_value.md)  <sub>0..1</sub>
     * Description: Original source value for phenotypic sex value
     * Range: [String](types/String.md)
 * [race](race.md)  <sub>1..1</sub>
     * Description: Reported race defined by NIH Racial and Ethnic Categories and Definitions (NOT-OD-15-089)
     * Range: [enum_race](enum_race.md)
 * [race_source_value](race_source_value.md)  <sub>0..1</sub>
     * Description: Race value as observed from the original source text
     * Range: [String](types/String.md)
 * [ethnicity](ethnicity.md)  <sub>1..1</sub>
     * Description: Classification categories of human, taken from NIH, based on the social group a person belongs to, and either identifies with or is identified with by others, as a result of a complex of cultural, biological, geographical and other factors such as linguistic, dietary and religion traditions; ancestry, background, allegiance, or association; and physical characteristics traditionally associated with race.
     * Range: [enum_ethnicity](enum_ethnicity.md)
 * [ethnicity_source_value](ethnicity_source_value.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [age_at_last_vital_status](age_at_last_vital_status.md)  <sub>0..1</sub>
     * Description: Age at Last Vital Status
     * Range: [Integer](types/Integer.md)
 * [vital_status](vital_status.md)  <sub>0..1</sub>
     * Description: Vital Status
     * Range: [enum_vital_status](enum_vital_status.md)
 * [has_sample](has_sample.md)  <sub>0..\*</sub>
     * Description: Which samples were collected or processed for this participant?
     * Range: [Sample](Sample.md)
