
# Class: Study

Study Meta Data

URI: [anvil:Study](https://anvilproject.org/acr-harmonized-data-model/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study]<parent_study_id%200..1-++[Study&#124;study_id:string;external_study_id:string%20*;funding_source:string%20*;principal_investigator:string%20*;study_title:string],[StudyParticipant]++-%20in_study%200..1>[Study],[Thing]^-[Study],[StudyParticipant])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study]<parent_study_id%200..1-++[Study&#124;study_id:string;external_study_id:string%20*;funding_source:string%20*;principal_investigator:string%20*;study_title:string],[StudyParticipant]++-%20in_study%200..1>[Study],[Thing]^-[Study],[StudyParticipant])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Referenced by Class

 *  **None** *[in_study](in_study.md)*  <sub>0..1</sub>  **[Study](Study.md)**
 *  **None** *[parent_study_id](parent_study_id.md)*  <sub>0..1</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [study_id](study_id.md)  <sub>1..1</sub>
     * Description: Study ID
     * Range: [String](types/String.md)
 * [external_study_id](external_study_id.md)  <sub>0..\*</sub>
     * Description: External Study ID
     * Range: [String](types/String.md)
 * [parent_study_id](parent_study_id.md)  <sub>0..1</sub>
     * Description: Parent Study ID
     * Range: [Study](Study.md)
 * [funding_source](funding_source.md)  <sub>0..\*</sub>
     * Description: Funding Source
     * Range: [String](types/String.md)
 * [principal_investigator](principal_investigator.md)  <sub>0..\*</sub>
     * Description: Principal Investigator
     * Range: [String](types/String.md)
 * [study_title](study_title.md)  <sub>1..1</sub>
     * Description: Study Title
     * Range: [String](types/String.md)
