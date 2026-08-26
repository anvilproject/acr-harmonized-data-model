# acr-harmonized-data-model

LinkML Schema for ACR Harmonized Data. This model under development is intended to capture useful cross-study data in the AnVIL data repository.

URI: https://w3id.org/anvilproject/acr-harmonized-data-model

Name: acr-harmonized-data-model



## Classes

| Class | Description |
| --- | --- |
| [AccessPolicy](AccessPolicy.md) | The access policy that describes the controls around use of data |
| [ActivityDefinition](ActivityDefinition.md) | A definition of an activity in this study, eg, a biospecimen collection, assa... |
| [Aliquot](Aliquot.md) | A specific tube or amount of a biospecimen associated with a Sample |
| [Any](Any.md) |  |
| [Assay](Assay.md) | A specific assay that was performed on given subject(s) or sample(s) |
| [BiospecimenCollection](BiospecimenCollection.md) | A biospecimen collection event which yields one or more Samples |
| [Concept](Concept.md) | A standardized concept with display information |
| [Dataset](Dataset.md) | Set of files grouped together for release |
| [Demographics](Demographics.md) | Basic participant demographics summary |
| [DOI](DOI.md) | A DOI is a permanent reference with metadata about a digital object |
| [Encounter](Encounter.md) | An event at which data was collected about a participant, an intervention was... |
| [EncounterDefinition](EncounterDefinition.md) | A definition of an encounter type in this study, ie, an event at which data w... |
| [Family](Family.md) | A group of individuals of some relation who are grouped together in a study |
| [FamilyMembership](FamilyMembership.md) | Designates a Subject as a member of a family with a specified role |
| [FamilyRelationship](FamilyRelationship.md) | A relationship between two Subjects |
| [File](File.md) | File |
| [FileHash](FileHash.md) | Type and value of a file content hash |
| [Investigator](Investigator.md) | An individual who made contributions to the collection, analysis, or sharing ... |
| [Publication](Publication.md) | Information about a specific publication |
| [Record](Record.md) | One row / entity within the database |
| [Sample](Sample.md) | A functionally equivalent specimen taken from a participant or processed from... |
| [Study](Study.md) | Study Metadata |
| [StudyMetadata](StudyMetadata.md) | Additional features about studies that may not apply to all studies |
| [Subject](Subject.md) | This entity is the subject about which data or references are recorded |
| [SubjectAssertion](SubjectAssertion.md) | Assertion about a particular Subject |
| [VirtualBiorepository](VirtualBiorepository.md) | An organization that can provide access to specimen for further analysis |



## Slots

| Slot | Description |
| --- | --- |
| [access_description](access_description.md) | Any additional information to support access requests |
| [access_policy_id](access_policy_id.md) | Global identifier for the access policy that applies to this row of data |
| [acknowledgments](acknowledgments.md) | Funding statement and acknowledgments for this study |
| [activity_definition_id](activity_definition_id.md) | Unique identifier for this Activity Definition |
| [actual_number_of_participants](actual_number_of_participants.md) | Total participants included at this time |
| [age_at_assertion](age_at_assertion.md) | The age in days of the Subject when the assertion was made |
| [age_at_collection](age_at_collection.md) | The age at which this biospecimen was collected in decimal years |
| [age_at_event](age_at_event.md) | The age in days of the Subject at the time point which the assertion describe... |
| [age_at_first_engagement](age_at_first_engagement.md) | Age in days of Participant at first recorded study event (enrollment, visit, ... |
| [age_at_last_vital_status](age_at_last_vital_status.md) | Age in days when participant's vital status was last recorded |
| [age_at_resolution](age_at_resolution.md) | The age in days of the Subject when the asserted state was resolved |
| [aliquot_id](aliquot_id.md) | Unique identifier for an Aliquot |
| [assay_id](assay_id.md) | The unique identifier for the Assay |
| [assay_source](assay_source.md) | The original description of the Assay performed |
| [assay_type](assay_type.md) | The type of assay performed |
| [asserter_type](asserter_type.md) | The original asserter of this information |
| [assertion_id](assertion_id.md) | INCLUDE Global ID for the Assertion |
| [assertion_source_type](assertion_source_type.md) | The source of this assertion from the original data |
| [availability](availability.md) | Is or was this file available to users? |
| [availability_status](availability_status.md) | Can this Sample be requested for further analysis? |
| [bibliographic_reference](bibliographic_reference.md) | Text use to reference this Record |
| [biospecimen_collection_id](biospecimen_collection_id.md) | Unique identifier for this Biospecimen Collection |
| [citation_statement](citation_statement.md) | Statement that secondary data users should use to acknowledge use of this stu... |
| [clinical_data_source_type](clinical_data_source_type.md) | Source(s) of data collected from study participants |
| [concentration_number](concentration_number.md) | What is the concentration of the analyte in the Aliquot? |
| [concentration_unit](concentration_unit.md) | Units associated with the concentration of the analyte in the Aliquot |
| [concept](concept.md) | The structured term defining the meaning of the assertion |
| [concept_curie](concept_curie.md) | The standardized curie for the term |
| [concept_source](concept_source.md) | The source text yielding the standardized concept |
| [consanguinity](consanguinity.md) | Is there known or suspected consanguinity in this study family? |
| [contact](contact.md) | The individual to contact with questions about this record |
| [data_category](data_category.md) | General category of data in this Record (e |
| [data_collection_end](data_collection_end.md) | The date that data collection started |
| [data_collection_start](data_collection_start.md) | The date that data collection started |
| [data_type](data_type.md) | The type of data within this file |
| [data_use_accession](data_use_accession.md) | Accession used to provision access to the record, eg, a dbGaP phsID |
| [data_use_modifier](data_use_modifier.md) | Additional modifiers that limit data use |
| [data_use_permission](data_use_permission.md) | Broad category of restrictions on data use |
| [dataset_id](dataset_id.md) | Unique identifier for a Dataset |
| [description](description.md) | Description for this entity |
| [disease_limitation](disease_limitation.md) | If the access is limited to a specific disease purpose, it is specified here |
| [display](display.md) | The friendly display string of the coded term |
| [do_id](do_id.md) | Digital Object Identifier (DOI) for this Record |
| [drs_uri](drs_uri.md) | DRS location to access the data |
| [email](email.md) | An email address to reach the entity |
| [encounter_definition_id](encounter_definition_id.md) | Unique identifier for this Encounter Definition |
| [encounter_id](encounter_id.md) | Unique identifier for this Encounter |
| [ethnicity](ethnicity.md) | Ethnicity of Participant |
| [expected_number_of_participants](expected_number_of_participants.md) | Total expected number of participants to be recruited |
| [external_id](external_id.md) | Other identifiers for this entity, eg, from the submitting study or in system... |
| [family_description](family_description.md) | Free text describing the study family, such as potential inheritance or detai... |
| [family_id](family_id.md) | Global ID for the Family |
| [family_member_id](family_member_id.md) | The family member Subject who is the relationship "subject" |
| [family_membership_id](family_membership_id.md) | ID for the Family Relationship |
| [family_relationship_id](family_relationship_id.md) | Global ID for the Family Relationship |
| [family_role](family_role.md) | The "role" of this individual in this family |
| [family_study_focus](family_study_focus.md) | The specific focus of the investigation, eg, a condition |
| [family_type](family_type.md) | Describes the 'type' of study family, eg, trio |
| [file_extension](file_extension.md) | Typically a 3-4 letter code at the end of a filename that identifies the file... |
| [file_id](file_id.md) | Unique identifier for this File |
| [filename](filename.md) | The name of the file |
| [format](format.md) | The format of the file |
| [funding_source](funding_source.md) | The funding source(s) of the study |
| [hash](hash.md) | File hash information |
| [hash_type](hash_type.md) | The type of file hash, eg, md5 |
| [hash_value](hash_value.md) | The value of the file hash |
| [institution](institution.md) | Name of the institution this record is associated with |
| [internal_uri](internal_uri.md) | URI/URL for internal access to the data |
| [investigator_title](investigator_title.md) | The title of the Investigator, eg, "Assistant Professor" |
| [laterality](laterality.md) | Laterality that further refine the specific location of biospecimen collectio... |
| [method](method.md) | The approach used to collect the biospecimen |
| [name](name.md) | Name of the entity |
| [organism_type](organism_type.md) | Organism Type, typically from NCBITaxon |
| [parent_sample_id](parent_sample_id.md) | Sample from which this sample is derived |
| [parent_study](parent_study.md) | The parent study for this study, if it is a nested study |
| [participant_lifespan_stage](participant_lifespan_stage.md) | Focus age group(s) of the study population |
| [principal_investigator](principal_investigator.md) | The Principal Investigator(s) responsible for the study |
| [processing](processing.md) | Processing that was applied to the Parent Sample or from the Biospecimen Coll... |
| [program](program.md) | Funding source(s) for the study |
| [publication](publication.md) | Publications associated with this Record |
| [quantity_number](quantity_number.md) | The total quantity of the specimen |
| [quantity_unit](quantity_unit.md) | The structured term defining the units of the quantity |
| [race](race.md) | Race of Participant |
| [relation](relation.md) | Code definting the relationship predicate |
| [release_uri](release_uri.md) | URI/URL for controlled or open access to the data |
| [research_domain](research_domain.md) | Main research domain(s) of the study |
| [sample_id](sample_id.md) | The unique identifier for this Sample |
| [sample_type](sample_type.md) | Type of material of which this Sample is comprised |
| [selection_criteria](selection_criteria.md) | Brief description of inclusion and/or exclusion criteria for the study |
| [sex](sex.md) | Sex of Participant |
| [site](site.md) | The location of the specimen collection |
| [size](size.md) | Size of the file, in Bytes |
| [spatial_qualifier](spatial_qualifier.md) | Qualifier that further refine the specific location of biospecimen collection |
| [storage_class](storage_class.md) | Storage class of the object, reflecting cost and access characteristics |
| [storage_method](storage_method.md) | Sample storage method, eg, Frozen or with additives |
| [study_code](study_code.md) | Unique identifier for the study (generally a short acronym) |
| [study_description](study_description.md) | Brief description of the study (2-4 sentences) |
| [study_design](study_design.md) | Overall design of study, including whether it is longitudinal and whether fam... |
| [study_id](study_id.md) | INCLUDE Global ID for the study |
| [study_short_name](study_short_name.md) | Short name for the study |
| [study_title](study_title.md) | Full Study Title |
| [subject_id](subject_id.md) | INCLUDE Global ID for the Subject |
| [subject_type](subject_type.md) | Type of entity this record represents |
| [value_concept](value_concept.md) | The structured term defining the value of the assertion |
| [value_number](value_number.md) | The numeric value of the assertion |
| [value_source](value_source.md) | The source text yielding the value |
| [value_unit](value_unit.md) | The structured term defining the units of the value |
| [value_unit_source](value_unit_source.md) | The source text yielding the value's units |
| [vbr_id](vbr_id.md) | Information about the study's Virtual Biorepository, if participating |
| [vbr_readme](vbr_readme.md) | Instructions for contacting or requesting samples from Virtual Biorepository,... |
| [vital_status](vital_status.md) | Whether participant is alive or dead |
| [website](website.md) | Website with more information about this entity |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [EnumAssayType](EnumAssayType.md) | Type of assays performed |
| [EnumAsserterType](EnumAsserterType.md) | Individuals or organizations making assertions |
| [EnumAvailabilityStatus](EnumAvailabilityStatus.md) | Is this item available for use? |
| [EnumDataCategory](EnumDataCategory.md) | Categories of data which may be collected about participants |
| [EnumDataSourceType](EnumDataSourceType.md) | Approaches to ascertain information about a participant |
| [EnumDataUseModifier](EnumDataUseModifier.md) | Data Use Ontology (DUO) terms for data use modifiers |
| [EnumDataUsePermission](EnumDataUsePermission.md) | Data Use Ontology (DUO) terms for data use permissions |
| [EnumEDAMDataTypes](EnumEDAMDataTypes.md) | Data types from the EDAM ontology |
| [EnumEDAMFormats](EnumEDAMFormats.md) | Data formats from the EDAM ontology |
| [EnumEthnicity](EnumEthnicity.md) | Participant ethnicity, specific to Hispanic or Latino |
| [EnumFamilyRelation](EnumFamilyRelation.md) | Definitions of family relations as provided by KIN Ontology |
| [EnumFamilyRole](EnumFamilyRole.md) | Example terms related to an individual's role in a family study |
| [EnumFamilyType](EnumFamilyType.md) | Enumerations describing research family type |
| [EnumFileHashType](EnumFileHashType.md) | Types of file hashes supported |
| [EnumLaterality](EnumLaterality.md) | Laterality information for the site |
| [EnumOrganism](EnumOrganism.md) | Common Organism types |
| [EnumParticipantLifespanStage](EnumParticipantLifespanStage.md) | Stages of life during which participants may be recruited |
| [EnumPresentAbsent](EnumPresentAbsent.md) | Options for describing presence or absence |
| [EnumProgram](EnumProgram.md) | Specific funding program examples |
| [EnumRace](EnumRace.md) | Participant Race |
| [EnumResearchDomain](EnumResearchDomain.md) | Domains of research activities |
| [EnumSampleCollectionMethod](EnumSampleCollectionMethod.md) | The approach used to collect the biospecimen |
| [EnumSex](EnumSex.md) | Subject Sex |
| [EnumSite](EnumSite.md) | The location of the specimen collection |
| [EnumSpatialQualifiers](EnumSpatialQualifiers.md) | Any spatial/location qualifiers |
| [EnumStudyDesign](EnumStudyDesign.md) | Approaches for collecting data, investigating interventions, and/or analyzing... |
| [EnumSubjectType](EnumSubjectType.md) | Types of Subject entities |
| [EnumUnknown](EnumUnknown.md) | Base enumeration providing an Unknown option |
| [EnumUnknownOther](EnumUnknownOther.md) | Base enumeration providing Unknown and Other options |
| [EnumVitalStatus](EnumVitalStatus.md) | Descriptions of a Subject's vital status |


## Types

| Type | Description |
| --- | --- |
| [AdGlobalID](AdGlobalID.md) | Dewrangle ad global ID |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [BsGlobalID](BsGlobalID.md) | Dewrangle bs global ID |
| [CoGlobalID](CoGlobalID.md) | Dewrangle co global ID |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [DeGlobalID](DeGlobalID.md) | Dewrangle de global ID |
| [DiGlobalID](DiGlobalID.md) | Dewrangle di global ID |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [DrGlobalID](DrGlobalID.md) | Dewrangle dr global ID |
| [EnGlobalID](EnGlobalID.md) | Dewrangle en global ID |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [FmGlobalID](FmGlobalID.md) | Dewrangle __ global ID |
| [GrGlobalID](GrGlobalID.md) | Dewrangle gr global ID |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [LsGlobalID](LsGlobalID.md) | Dewrangle ls global ID |
| [MsGlobalID](MsGlobalID.md) | Dewrangle __ global ID |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [ObGlobalID](ObGlobalID.md) | Dewrangle ob global ID |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [OrGlobalID](OrGlobalID.md) | Dewrangle or global ID |
| [PdGlobalID](PdGlobalID.md) | Dewrangle __ global ID |
| [PtGlobalID](PtGlobalID.md) | Dewrangle pt global ID |
| [SdGlobalID](SdGlobalID.md) | Dewrangle sd global ID |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
