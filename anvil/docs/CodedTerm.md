
# Class: CodedTerm

A term that includes a string value as well as an associated uri or curie.

URI: [anvil:CodedTerm](https://anvilproject.org/acr-harmonized-data-model/CodedTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectAssertion]++-%20assertion%200..1>[CodedTerm&#124;code:uriorcurie%20%3F;code_string:string%20%3F],[Quantity]++-%20unit%200..1>[CodedTerm],[SubjectAssertion]++-%20source_assertion%200..1>[CodedTerm],[SubjectAssertion],[Quantity])](https://yuml.me/diagram/nofunky;dir:TB/class/[SubjectAssertion]++-%20assertion%200..1>[CodedTerm&#124;code:uriorcurie%20%3F;code_string:string%20%3F],[Quantity]++-%20unit%200..1>[CodedTerm],[SubjectAssertion]++-%20source_assertion%200..1>[CodedTerm],[SubjectAssertion],[Quantity])

## Referenced by Class

 *  **None** *[assertion](assertion.md)*  <sub>0..1</sub>  **[CodedTerm](CodedTerm.md)**
 *  **None** *[➞unit](quantity__unit.md)*  <sub>0..1</sub>  **[CodedTerm](CodedTerm.md)**
 *  **None** *[source_assertion](source_assertion.md)*  <sub>0..1</sub>  **[CodedTerm](CodedTerm.md)**

## Attributes


### Own

 * [➞code](codedTerm__code.md)  <sub>0..1</sub>
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞code_string](codedTerm__code_string.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
