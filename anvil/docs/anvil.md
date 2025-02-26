
# anvil-schema


**metamodel version:** 1.7.0

**version:** None





### Classes

 * [Any](Any.md)
 * [CodedTerm](CodedTerm.md) - A term that includes a string value as well as an associated uri or curie.
 * [Quantity](Quantity.md) - A numeric value and unit
 * [Thing](Thing.md) - Highest Level Class
     * [AccessControlledRecord](AccessControlledRecord.md) - Element for which specific access control restrictions apply.
         * [Subject](Subject.md) - This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity.
             * [Participant](Participant.md) - Basic participant demographics
     * [AccessPolicy](AccessPolicy.md) - Describes the access required for a given element of data.
     * [Aliquot](Aliquot.md) - Represent exact tubes or total amounts available of a Sample.
     * [BiospecimenCollection](BiospecimenCollection.md) - Biospecimen Collection
     * [Family](Family.md) - Family
     * [FamilyMember](FamilyMember.md) - Family
     * [Measurement](Measurement.md) - Measurements
     * [Procedure](Procedure.md) - Procedures
     * [Sample](Sample.md) - Biospecimen data
     * [Study](Study.md) - Study Meta Data
     * [SubjectAssertion](SubjectAssertion.md) - Generic template for linking information with a given Subject.
         * [ConditionAssertion](ConditionAssertion.md) - Study Meta Data

### Mixins


### Slots

 * [access_policy_code](access_policy_code.md) - Access Policy Code
 * [age_at_assertion](age_at_assertion.md) - The age at which this condition is being asserted.
 * [age_at_collection](age_at_collection.md) - The age at which this biospecimen was collected.
 * [age_at_event](age_at_event.md) - Age of participant when procedure was performed/recorded
 * [age_at_last_vital_status](age_at_last_vital_status.md) - Age at Last Vital Status
 * [age_at_observation](age_at_observation.md) - Age of participant when measurement was taken/recorded
 * [age_at_onset](age_at_onset.md) - The age of onset for this condition.
 * [age_at_resolution](age_at_resolution.md) - The age at which this condition was resolved, abated or cured. Should be left empty in cases of current active status.
 * [assertion](assertion.md) - The assertion that is being made.
 * [availablity_status](availablity_status.md) - Can this Sample be requested for further analysis?
 * [biospecimen_collection_id_fk](biospecimen_collection_id_fk.md) - ID associated with the Biospecimen Collection event.
 * [➞code](codedTerm__code.md)
 * [➞code_string](codedTerm__code_string.md)
 * [condition_assertion](condition_assertion.md) - Condition Assertion
 * [condition_code](condition_code.md) - Condition Code should be from one of a recognized ontology. Multiple codes can be indicated, but should simply be alternative encodings for the same entity such as alternates encodings from other ontologies.       
 * [condition_source_value](condition_source_value.md) - Original Source Value for condition
 * [condition_type](condition_type.md) - Does this condition represent a specific "type" of condition, such as "Phenotypic Feature" vs "Disease" in a rare disease setting.
 * [consanguinity](consanguinity.md) - Is there known or suspected consanguinity in this study family?
 * [data_access_type](data_access_type.md) - Data Access Type
 * [date_of_birth](date_of_birth.md) - Date at which the individual was born. May be impacted by privacy rules described in date_of_birth_type.
 * [date_of_birth_type](date_of_birth_type.md) - Privacy rule modification applied to date_of_birth.
 * [description](description.md) - Description
 * [disease_limitation](disease_limitation.md) - Disease Use Limitations
 * [ethnicity](ethnicity.md) - Classification categories of human, taken from NIH, based on the social group a person belongs to, and either identifies with or is identified with by others, as a result of a complex of cultural, biological, geographical and other factors such as linguistic, dietary and religion traditions; ancestry, background, allegiance, or association; and physical characteristics traditionally associated with race.
 * [ethnicity_source_value](ethnicity_source_value.md) - Ethnicity value as reported in the original source
 * [external_id](external_id.md) - Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
 * [external_study_id](external_study_id.md) - External Study ID
 * [family_description](family_description.md) - Free title describing the study family, such as potential inheritance or details about consanguinity
 * [family_external_id](family_external_id.md) - Other study specific study identifiers
 * [family_id_fk](family_id_fk.md) - Family Identifier
 * [family_member_id](family_member_id.md) - Family Member ID indicating presence in the family
 * [family_study_focus](family_study_focus.md) - What is this study family investigating? EG, a specific condition. The code should be prefixed with a recognizable curie. 
 * [family_type](family_type.md) - Describes the 'type' of study family, eg, trio.
 * [funding_source](funding_source.md) - Funding Source
 * [has_access_policy](has_access_policy.md) - Which access policy applies to this element?
 * [has_assertion](has_assertion.md) - Which samples were collected or processed for this participant?
 * [has_sample](has_sample.md) - Which samples were collected or processed for this participant?
 * [id](id.md) - ID associated with a class
 * [in_study](in_study.md) - With which study is this class associated?
 * [laterality](laterality.md) - Laterality information for the site
 * [measurement_code](measurement_code.md) - Measurement code should be from a recognized ontology preceded by a recognized curie. Multiple entries should reflect alternate codes for the same measurement. 
 * [measurement_source_value](measurement_source_value.md) - Original measurement text
 * [measurement_unit](measurement_unit.md) - UCUM Unit associated with the field
 * [measurement_value_code](measurement_value_code.md) - Code indicating measurement value such as positive, negative, etc.
 * [method](method.md) - The approach used to collect the biospecimen.
 * [organism_type](organism_type.md) - Organism Type Label
 * [other_family_member_id](other_family_member_id.md) - Other member of the same family to which there is a relationship being described
 * [parent_sample_id](parent_sample_id.md) - Parent Sample ID
 * [parent_study_id](parent_study_id.md) - Parent Study ID
 * [phenotypic_sex](phenotypic_sex.md) - Sex of the Participant
 * [phenotypic_sex_source_value](phenotypic_sex_source_value.md) - Original source value for phenotypic sex value
 * [principal_investigator](principal_investigator.md) - Principal Investigator
 * [procedure_code](procedure_code.md) - Procedure code should be from a recognized ontology preceded by a recognized curie. Multiple entries should reflect alternate codes for the same procedure. 
 * [procedure_source_value](procedure_source_value.md) - Original procedure text
 * [processing](processing.md) - Curied code associated processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample
 * [quantity](quantity.md) - The total quantity of the specimen
 * [➞unit](quantity__unit.md)
 * [➞value](quantity__value.md)
 * [race](race.md) - Reported race defined by NIH Racial and Ethnic Categories and Definitions (NOT-OD-15-089)
 * [race_source_value](race_source_value.md) - Race value as observed from the original source text
 * [relationship_code](relationship_code.md) - Relationship of the "Family Member" to the "Other Family Member" (i.e. mother, father, etc). This is required if other_family_member_id is present. Code must be from the HL7 [FamilyMember ValueSet](https://terminology.hl7.org/6.2.0/ValueSet-v3-FamilyMember.html)
 * [sample_availability_status](sample_availability_status.md) - Can this Sample be requested for further analysis
 * [sample_concentration](sample_concentration.md) - What is the concentration of the analyte in the Aliquot?
 * [sample_concentration_unit](sample_concentration_unit.md) - Units associated with the concentration of the analyte in the Aliquot? UCUM coding preferred (with curie, UCUM)
 * [sample_id_fk](sample_id_fk.md) - Sample ID the aliquot is associated with
 * [sample_type](sample_type.md) - Curied code associated the type of material of which this Sample is comprised
 * [sample_volume](sample_volume.md) - What is the volume of the Aliquot?
 * [sample_volume_unit](sample_volume_unit.md) - Units associated with the volume? UCUM coding preferred (with curie, UCUM)
 * [site](site.md) - The location of the specimen collection.
 * [source_assertion](source_assertion.md) - The assertion that is being made as originally recorded.
 * [source_value](source_value.md) - The value of the assertion that is being made as originally recoded.
 * [spatial_qualifier](spatial_qualifier.md) - Any spatial/location qualifiers
 * [storage_method](storage_method.md) - Curied code indicating how is the Sample stored, eg, Frozen or with additives
 * [study_title](study_title.md) - Study Title
 * [subject_assertion](subject_assertion.md) - Assertions made about this subject.
 * [subject_type](subject_type.md) - Type of entity this record represents
 * [value](value.md) - The value of the assertion that is being made.
 * [vital_status](vital_status.md) - Vital Status
 * [website](website.md) - Website

### Enums

 * [EnumAccessCode](EnumAccessCode.md) - Type of research use case allowed
 * [EnumAccessType](EnumAccessType.md) - Type of access controls applied
 * [EnumAvailabilityStatus](EnumAvailabilityStatus.md) - Is the Thing available for use?
 * [EnumConditionAssertion](EnumConditionAssertion.md) - Enumerations for Condition Assertion
 * [EnumConditionCode](EnumConditionCode.md) - Recommended ontologies include: SNOMED_CT, HP, OMIM and ORPHA, prefixed with those curies
 * [EnumConditionType](EnumConditionType.md) - Provides options to describe the expressed semantics of a condition.
 * [EnumConsanguinityAssertion](EnumConsanguinityAssertion.md) - Asserts known or suspected consanguinity in this study family
 * [EnumDateOfBirthType](EnumDateOfBirthType.md) - Privacy rules that may modify a date value.
 * [EnumEthnicity](EnumEthnicity.md) - OMB Codes describing Hispanic or Latino ethnicity.
 * [EnumFamilyType](EnumFamilyType.md) - Enumerations describing research family type
 * [EnumLaterality](EnumLaterality.md) - Laterality information for the site
 * [EnumMeasurementValueCode](EnumMeasurementValueCode.md) - Indicate measurement details such as positive/negative/indeterminate
 * [EnumRace](EnumRace.md) - OMB Codes describing race.
 * [EnumSampleCollectionMethod](EnumSampleCollectionMethod.md) - The approach used to collect the biospecimen. Recommend ontology: [LOINC](https://loinc.org).
 * [EnumSex](EnumSex.md) - Terms describing an individual's sex.
 * [EnumSite](EnumSite.md) - The location of the specimen collection. Recommended ontology: [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html)
 * [EnumSpatialQualifiers](EnumSpatialQualifiers.md) - Any spatial/location qualifiers.
 * [EnumSubjectType](EnumSubjectType.md) - Types of entities
 * [EnumVitalStatus](EnumVitalStatus.md) - Is the entity living?

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
