-- # Class: "Thing" Description: "Highest Level Class"
--     * Slot: id Description: ID associated with a class
-- # Class: "AccessControlledRecord" Description: "Element for which specific access control restrictions apply."
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "Any" Description: ""
--     * Slot: id Description: 
-- # Class: "Study" Description: "Study Meta Data"
--     * Slot: parent_study_id Description: Parent Study ID
--     * Slot: study_title Description: Study Title
--     * Slot: id Description: ID associated with a class
-- # Class: "Sample" Description: "Biospecimen data"
--     * Slot: parent_sample_id Description: Parent Sample ID
--     * Slot: biospecimen_collection_id_fk Description: ID associated with the Biospecimen Collection event.
--     * Slot: sample_type Description: Curied code associated the type of material of which this Sample is comprised
--     * Slot: availablity_status Description: Can this Sample be requested for further analysis?
--     * Slot: storage_method Description: Curied code indicating how is the Sample stored, eg, Frozen or with additives
--     * Slot: quantity Description: The total quantity of the specimen
--     * Slot: id Description: ID associated with a class
-- # Class: "SubjectAssertion" Description: "Generic template for linking information with a given Subject."
--     * Slot: age_at_assertion Description: The age at which this condition is being asserted.
--     * Slot: id Description: ID associated with a class
--     * Slot: assertion_id Description: The assertion that is being made.
--     * Slot: value_id Description: The value of the assertion that is being made.
--     * Slot: source_assertion_id Description: The assertion that is being made as originally recorded.
--     * Slot: source_value_id Description: The value of the assertion that is being made as originally recoded.
-- # Class: "ConditionAssertion" Description: "Study Meta Data"
--     * Slot: condition_type Description: Does this condition represent a specific "type" of condition, such as "Phenotypic Feature" vs "Disease" in a rare disease setting.
--     * Slot: age_at_onset Description: The age of onset for this condition.
--     * Slot: age_at_resolution Description: The age at which this condition was resolved, abated or cured. Should be left empty in cases of current active status.
--     * Slot: age_at_assertion Description: The age at which this condition is being asserted.
--     * Slot: id Description: ID associated with a class
--     * Slot: assertion_id Description: The assertion that is being made.
--     * Slot: value_id Description: The value of the assertion that is being made.
--     * Slot: source_assertion_id Description: The assertion that is being made as originally recorded.
--     * Slot: source_value_id Description: The value of the assertion that is being made as originally recoded.
-- # Class: "CodedTerm" Description: "A term that includes a string value as well as an associated uri or curie."
--     * Slot: id Description: 
--     * Slot: code Description: 
--     * Slot: code_string Description: 
-- # Class: "Quantity" Description: "A numeric value and unit"
--     * Slot: id Description: 
--     * Slot: value_id Description: 
--     * Slot: unit_id Description: 
-- # Class: "Subject" Description: "This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity."
--     * Slot: subject_type Description: Type of entity this record represents
--     * Slot: organism_type Description: Organism Type Label
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "Participant" Description: "Basic participant demographics"
--     * Slot: date_of_birth Description: Date at which the individual was born. May be impacted by privacy rules described in date_of_birth_type.
--     * Slot: date_of_birth_type Description: Privacy rule modification applied to date_of_birth.
--     * Slot: phenotypic_sex Description: Sex of the Participant
--     * Slot: phenotypic_sex_source_value Description: Original source value for phenotypic sex value
--     * Slot: race Description: Reported race defined by NIH Racial and Ethnic Categories and Definitions (NOT-OD-15-089)
--     * Slot: race_source_value Description: Race value as observed from the original source text
--     * Slot: ethnicity Description: Classification categories of human, taken from NIH, based on the social group a person belongs to, and either identifies with or is identified with by others, as a result of a complex of cultural, biological, geographical and other factors such as linguistic, dietary and religion traditions; ancestry, background, allegiance, or association; and physical characteristics traditionally associated with race.
--     * Slot: ethnicity_source_value Description: Ethnicity value as reported in the original source
--     * Slot: age_at_last_vital_status Description: Age at Last Vital Status
--     * Slot: vital_status Description: Vital Status
--     * Slot: subject_type Description: Type of entity this record represents
--     * Slot: organism_type Description: Organism Type Label
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "AccessPolicy" Description: "Describes the access required for a given element of data."
--     * Slot: disease_limitation Description: Disease Use Limitations
--     * Slot: description Description: Description
--     * Slot: website Description: Website
--     * Slot: id Description: ID associated with a class
-- # Class: "BiospecimenCollection" Description: "Biospecimen Collection"
--     * Slot: age_at_collection Description: The age at which this biospecimen was collected.
--     * Slot: method Description: The approach used to collect the biospecimen.
--     * Slot: site Description: The location of the specimen collection.
--     * Slot: spatial_qualifier Description: Any spatial/location qualifiers
--     * Slot: laterality Description: Laterality information for the site
--     * Slot: id Description: ID associated with a class
-- # Class: "Aliquot" Description: "Represent exact tubes or total amounts available of a Sample."
--     * Slot: sample_id_fk Description: Sample ID the aliquot is associated with
--     * Slot: sample_availability_status Description: Can this Sample be requested for further analysis
--     * Slot: sample_volume Description: What is the volume of the Aliquot?
--     * Slot: sample_volume_unit Description: Units associated with the volume? UCUM coding preferred (with curie, UCUM)
--     * Slot: sample_concentration Description: What is the concentration of the analyte in the Aliquot?
--     * Slot: sample_concentration_unit Description: Units associated with the concentration of the analyte in the Aliquot? UCUM coding preferred (with curie, UCUM)
--     * Slot: id Description: ID associated with a class
-- # Class: "Measurement" Description: "Measurements"
--     * Slot: measurement_unit Description: UCUM Unit associated with the field
--     * Slot: measurement_value_code Description: Code indicating measurement value such as positive, negative, etc.
--     * Slot: measurement_source_value Description: Original measurement text
--     * Slot: age_at_observation Description: Age of participant when measurement was taken/recorded
--     * Slot: id Description: ID associated with a class
-- # Class: "Procedure" Description: "Procedures"
--     * Slot: procedure_source_value Description: Original procedure text
--     * Slot: age_at_observation Description: Age of participant when measurement was taken/recorded
--     * Slot: id Description: ID associated with a class
-- # Class: "Family" Description: "Family"
--     * Slot: family_type Description: Describes the 'type' of study family, eg, trio.
--     * Slot: family_description Description: Free title describing the study family, such as potential inheritance or details about consanguinity
--     * Slot: consanguinity Description: Is there known or suspected consanguinity in this study family?
--     * Slot: family_study_focus Description: What is this study family investigating? EG, a specific condition. The code should be prefixed with a recognizable curie. 
--     * Slot: id Description: ID associated with a class
-- # Class: "FamilyMember" Description: "Family"
--     * Slot: family_id_fk Description: Family Identifier
--     * Slot: family_member_id Description: Family Member ID indicating presence in the family
--     * Slot: other_family_member_id Description: Other member of the same family to which there is a relationship being described
--     * Slot: relationship_code Description: Relationship of the "Family Member" to the "Other Family Member" (i.e. mother, father, etc). This is required if other_family_member_id is present. Code must be from the HL7 [FamilyMember ValueSet](https://terminology.hl7.org/6.2.0/ValueSet-v3-FamilyMember.html)
--     * Slot: id Description: ID associated with a class
-- # Class: "Study_external_study_id" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: external_study_id Description: External Study ID
-- # Class: "Study_funding_source" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: funding_source Description: Funding Source
-- # Class: "Study_principal_investigator" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: principal_investigator Description: Principal Investigator
-- # Class: "Sample_processing" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: processing Description: Curied code associated processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample
-- # Class: "Subject_subject_assertion" Description: ""
--     * Slot: Subject_id Description: Autocreated FK slot
--     * Slot: subject_assertion_id Description: Assertions made about this subject.
-- # Class: "Participant_has_sample" Description: ""
--     * Slot: Participant_id Description: Autocreated FK slot
--     * Slot: has_sample_id Description: Which samples were collected or processed for this participant?
-- # Class: "Participant_has_assertion" Description: ""
--     * Slot: Participant_id Description: Autocreated FK slot
--     * Slot: has_assertion_id Description: Which samples were collected or processed for this participant?
-- # Class: "Participant_subject_assertion" Description: ""
--     * Slot: Participant_id Description: Autocreated FK slot
--     * Slot: subject_assertion_id Description: Assertions made about this subject.
-- # Class: "AccessPolicy_data_access_type" Description: ""
--     * Slot: AccessPolicy_id Description: Autocreated FK slot
--     * Slot: data_access_type Description: Data Access Type
-- # Class: "AccessPolicy_access_policy_code" Description: ""
--     * Slot: AccessPolicy_id Description: Autocreated FK slot
--     * Slot: access_policy_code Description: Access Policy Code
-- # Class: "Measurement_measurement_code" Description: ""
--     * Slot: Measurement_id Description: Autocreated FK slot
--     * Slot: measurement_code Description: Measurement code should be from a recognized ontology preceded by a recognized curie. Multiple entries should reflect alternate codes for the same measurement. * LOINC : https://bioregistry.io/registry/loinc
-- # Class: "Procedure_procedure_code" Description: ""
--     * Slot: Procedure_id Description: Autocreated FK slot
--     * Slot: procedure_code Description: Procedure code should be from a recognized ontology preceded by a recognized curie. Multiple entries should reflect alternate codes for the same procedure. * CPT : https://bioregistry.io/registry/cpt
-- # Class: "Family_family_external_id" Description: ""
--     * Slot: Family_id Description: Autocreated FK slot
--     * Slot: family_external_id Description: Other study specific study identifiers

CREATE TABLE "Thing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Any" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Study" (
	parent_study_id TEXT, 
	study_title TEXT NOT NULL, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_study_id) REFERENCES "Study" (id)
);
CREATE TABLE "Sample" (
	parent_sample_id TEXT, 
	biospecimen_collection_id_fk TEXT NOT NULL, 
	sample_type TEXT NOT NULL, 
	availablity_status VARCHAR(11), 
	storage_method TEXT, 
	quantity TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CodedTerm" (
	id INTEGER NOT NULL, 
	code TEXT, 
	code_string TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "AccessPolicy" (
	disease_limitation TEXT, 
	description TEXT NOT NULL, 
	website TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "BiospecimenCollection" (
	age_at_collection INTEGER, 
	method VARCHAR, 
	site VARCHAR, 
	spatial_qualifier VARCHAR, 
	laterality VARCHAR, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Aliquot" (
	sample_id_fk TEXT NOT NULL, 
	sample_availability_status VARCHAR(11), 
	sample_volume FLOAT, 
	sample_volume_unit TEXT, 
	sample_concentration FLOAT, 
	sample_concentration_unit TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Measurement" (
	measurement_unit TEXT NOT NULL, 
	measurement_value_code VARCHAR(13), 
	measurement_source_value TEXT NOT NULL, 
	age_at_observation INTEGER, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Procedure" (
	procedure_source_value TEXT NOT NULL, 
	age_at_observation INTEGER, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Family" (
	family_type VARCHAR(12), 
	family_description TEXT, 
	consanguinity VARCHAR(13), 
	family_study_focus TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "FamilyMember" (
	family_id_fk TEXT, 
	family_member_id TEXT NOT NULL, 
	other_family_member_id TEXT, 
	relationship_code TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AccessControlledRecord" (
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "SubjectAssertion" (
	age_at_assertion INTEGER, 
	id TEXT NOT NULL, 
	assertion_id INTEGER, 
	value_id INTEGER, 
	source_assertion_id INTEGER, 
	source_value_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(assertion_id) REFERENCES "CodedTerm" (id), 
	FOREIGN KEY(value_id) REFERENCES "Any" (id), 
	FOREIGN KEY(source_assertion_id) REFERENCES "CodedTerm" (id), 
	FOREIGN KEY(source_value_id) REFERENCES "Any" (id)
);
CREATE TABLE "ConditionAssertion" (
	condition_type VARCHAR(18) NOT NULL, 
	age_at_onset INTEGER, 
	age_at_resolution INTEGER, 
	age_at_assertion INTEGER, 
	id TEXT NOT NULL, 
	assertion_id INTEGER, 
	value_id INTEGER, 
	source_assertion_id INTEGER, 
	source_value_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(assertion_id) REFERENCES "CodedTerm" (id), 
	FOREIGN KEY(value_id) REFERENCES "Any" (id), 
	FOREIGN KEY(source_assertion_id) REFERENCES "CodedTerm" (id), 
	FOREIGN KEY(source_value_id) REFERENCES "Any" (id)
);
CREATE TABLE "Quantity" (
	id INTEGER NOT NULL, 
	value_id INTEGER, 
	unit_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(value_id) REFERENCES "Any" (id), 
	FOREIGN KEY(unit_id) REFERENCES "CodedTerm" (id)
);
CREATE TABLE "Subject" (
	subject_type VARCHAR(15) NOT NULL, 
	organism_type TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "Participant" (
	date_of_birth INTEGER, 
	date_of_birth_type VARCHAR(11), 
	phenotypic_sex VARCHAR(8) NOT NULL, 
	phenotypic_sex_source_value TEXT, 
	race VARCHAR(35) NOT NULL, 
	race_source_value TEXT, 
	ethnicity VARCHAR(22) NOT NULL, 
	ethnicity_source_value TEXT, 
	age_at_last_vital_status INTEGER, 
	vital_status VARCHAR(12), 
	subject_type VARCHAR(15) NOT NULL, 
	organism_type TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "Study_external_study_id" (
	"Study_id" TEXT, 
	external_study_id TEXT, 
	PRIMARY KEY ("Study_id", external_study_id), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);
CREATE TABLE "Study_funding_source" (
	"Study_id" TEXT, 
	funding_source TEXT, 
	PRIMARY KEY ("Study_id", funding_source), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);
CREATE TABLE "Study_principal_investigator" (
	"Study_id" TEXT, 
	principal_investigator TEXT, 
	PRIMARY KEY ("Study_id", principal_investigator), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);
CREATE TABLE "Sample_processing" (
	"Sample_id" TEXT, 
	processing TEXT, 
	PRIMARY KEY ("Sample_id", processing), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE TABLE "AccessPolicy_data_access_type" (
	"AccessPolicy_id" TEXT, 
	data_access_type VARCHAR(14), 
	PRIMARY KEY ("AccessPolicy_id", data_access_type), 
	FOREIGN KEY("AccessPolicy_id") REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "AccessPolicy_access_policy_code" (
	"AccessPolicy_id" TEXT, 
	access_policy_code VARCHAR(3) NOT NULL, 
	PRIMARY KEY ("AccessPolicy_id", access_policy_code), 
	FOREIGN KEY("AccessPolicy_id") REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "Measurement_measurement_code" (
	"Measurement_id" TEXT, 
	measurement_code TEXT NOT NULL, 
	PRIMARY KEY ("Measurement_id", measurement_code), 
	FOREIGN KEY("Measurement_id") REFERENCES "Measurement" (id)
);
CREATE TABLE "Procedure_procedure_code" (
	"Procedure_id" TEXT, 
	procedure_code TEXT NOT NULL, 
	PRIMARY KEY ("Procedure_id", procedure_code), 
	FOREIGN KEY("Procedure_id") REFERENCES "Procedure" (id)
);
CREATE TABLE "Family_family_external_id" (
	"Family_id" TEXT, 
	family_external_id TEXT, 
	PRIMARY KEY ("Family_id", family_external_id), 
	FOREIGN KEY("Family_id") REFERENCES "Family" (id)
);
CREATE TABLE "Subject_subject_assertion" (
	"Subject_id" TEXT, 
	subject_assertion_id TEXT, 
	PRIMARY KEY ("Subject_id", subject_assertion_id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id), 
	FOREIGN KEY(subject_assertion_id) REFERENCES "SubjectAssertion" (id)
);
CREATE TABLE "Participant_has_sample" (
	"Participant_id" TEXT, 
	has_sample_id TEXT, 
	PRIMARY KEY ("Participant_id", has_sample_id), 
	FOREIGN KEY("Participant_id") REFERENCES "Participant" (id), 
	FOREIGN KEY(has_sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "Participant_has_assertion" (
	"Participant_id" TEXT, 
	has_assertion_id TEXT, 
	PRIMARY KEY ("Participant_id", has_assertion_id), 
	FOREIGN KEY("Participant_id") REFERENCES "Participant" (id), 
	FOREIGN KEY(has_assertion_id) REFERENCES "Sample" (id)
);
CREATE TABLE "Participant_subject_assertion" (
	"Participant_id" TEXT, 
	subject_assertion_id TEXT, 
	PRIMARY KEY ("Participant_id", subject_assertion_id), 
	FOREIGN KEY("Participant_id") REFERENCES "Participant" (id), 
	FOREIGN KEY(subject_assertion_id) REFERENCES "SubjectAssertion" (id)
);