
# Class: StudyParticipant

Research

URI: [anvil:StudyParticipant](https://anvilproject.org/acr-harmonized-data-model/StudyParticipant)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study]<in_study%200..1-%20[StudyParticipant&#124;participant_id:string;id(i):string],[Thing]^-[StudyParticipant],[Study])](https://yuml.me/diagram/nofunky;dir:TB/class/[Thing],[Study]<in_study%200..1-%20[StudyParticipant&#124;participant_id:string;id(i):string],[Thing]^-[StudyParticipant],[Study])

## Parents

 *  is_a: [Thing](Thing.md) - Highest Level Class

## Attributes


### Own

 * [participant_id](participant_id.md)  <sub>1..1</sub>
     * Description: ID associated with the Participant
     * Range: [String](types/String.md)
 * [in_study](in_study.md)  <sub>0..1</sub>
     * Description: With which study is this class associated?
     * Range: [Study](Study.md)

### Inherited from Thing:

 * [id](id.md)  <sub>1..1</sub>
     * Description: ID associated with a class
     * Range: [String](types/String.md)
