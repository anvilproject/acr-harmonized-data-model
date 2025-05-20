-- # Abstract Class: "Thing" Description: "Highest Level Class"
--     * Slot: id Description: ID associated with a class
-- # Class: "AccessControlledRecord" Description: "Element for which specific access control restrictions apply."
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "Study" Description: "Study Meta Data"
--     * Slot: parent_study_id Description: Parent Study ID
--     * Slot: study_title Description: Study Title
--     * Slot: id Description: ID associated with a class
-- # Class: "Sample" Description: "Biospecimen data"
--     * Slot: parent_sample Description: Sample from which this sample is derived
--     * Slot: sample_type Description: Type of material of which this Sample is comprised
--     * Slot: availablity_status Description: Can this Sample be requested for further analysis?
--     * Slot: quantity_number Description: The total quantity of the specimen
--     * Slot: quantity_units Description: The structured term defining the units of the quantity.
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
--     * Slot: Subject_id Description: Autocreated FK slot
--     * Slot: biospecimen_collection_id Description: Biospecimen Collection that generated this sample.
-- # Class: "BiospecimenCollection" Description: "Biospecimen Collection"
--     * Slot: age_at_collection Description: The age at which this biospecimen was collected.
--     * Slot: method Description: The approach used to collect the biospecimen.
--     * Slot: site Description: The location of the specimen collection.
--     * Slot: spatial_qualifier Description: Any spatial/location qualifiers
--     * Slot: laterality Description: Laterality information for the site
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "Aliquot" Description: "Specific tubes or details of a Sample."
--     * Slot: availablity_status Description: Can this Sample be requested for further analysis?
--     * Slot: quantity_number Description: The total quantity of the specimen
--     * Slot: quantity_units Description: The structured term defining the units of the quantity.
--     * Slot: concentration_number Description: What is the concentration of the analyte in the Aliquot?
--     * Slot: concentration_unit Description: Units associated with the concentration of the analyte in the Aliquot? UCUM coding preferred (with curie, UCUM)
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
--     * Slot: Sample_id Description: Autocreated FK slot
-- # Class: "Subject" Description: "This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity."
--     * Slot: subject_type Description: Type of entity this record represents
--     * Slot: organism_type Description: Organism Type Label
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
--     * Slot: has_demographics_id Description: A demographic summary of the participant.
-- # Class: "Demographics" Description: "Basic participant demographics summary"
--     * Slot: date_of_birth Description: Date at which the individual was born. May be impacted by privacy rules described in date_of_birth_type.
--     * Slot: date_of_birth_type Description: Privacy rule modification applied to date_of_birth.
--     * Slot: sex Description: Sex of the individual
--     * Slot: sex_display Description: The friendly display string of the coded term for Sex
--     * Slot: race_display Description: The friendly display string of the coded term(s) for Race
--     * Slot: ethnicity Description: Reported ethnicity as defined by the 1997 OMB directives.
--     * Slot: ethnicity_display Description: The friendly display string of the coded term for Ethnicity
--     * Slot: age_at_last_vital_status Description: Age at last vital status in decimal years.
--     * Slot: vital_status Description: Vital Status
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "SubjectAssertion" Description: "Assertion about a particular Subject. May include Conditions, Measurements, etc."
--     * Slot: assertion_type Description: The semantic type of the resource, eg, Condition.
--     * Slot: age_at_assertion Description: The age in decimal years of the Subject when the assertion was made.
--     * Slot: age_at_event Description: The age in decimal years of the Subject at the time point which the assertion describes, | eg, age of onset or when a measurement was performed.
--     * Slot: age_at_resolution Description: The age in decimal years of the Subject when the asserted state was resolved.
--     * Slot: code Description: The structured term defining the meaning of the assertion.
--     * Slot: display Description: The friendly display string of the coded term
--     * Slot: value_code Description: The structured term defining the value of the assertion.
--     * Slot: value_display Description: The friendly display string of the coded term for the value of the assertion.
--     * Slot: value_number Description: The numeric value of the assertion.
--     * Slot: value_units Description: The structured term defining the units of the value.
--     * Slot: value_units_display Description: The friendly display string of units of the value.
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
--     * Slot: Subject_id Description: Autocreated FK slot
-- # Class: "SourceData" Description: "Submitted data about a particular Subject."
--     * Slot: code Description: The structured term defining the meaning of the assertion.
--     * Slot: display Description: The friendly display string of the coded term
--     * Slot: value_code Description: The structured term defining the value of the assertion.
--     * Slot: value_display Description: The friendly display string of the coded term for the value of the assertion.
--     * Slot: value_number Description: The numeric value of the assertion.
--     * Slot: value_units Description: The structured term defining the units of the value.
--     * Slot: value_units_display Description: The friendly display string of units of the value.
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "AccessPolicy" Description: "Describes the access required for a given element of data."
--     * Slot: disease_limitation Description: Disease Use Limitations
--     * Slot: description Description: Description
--     * Slot: website Description: Website
--     * Slot: id Description: ID associated with a class
-- # Class: "Family" Description: "A group of individuals of some relation who are grouped together in the study."
--     * Slot: family_type Description: Describes the 'type' of study family, eg, trio.
--     * Slot: family_description Description: Free title describing the study family, such as potential inheritance or details about consanguinity
--     * Slot: consanguinity Description: Is there known or suspected consanguinity in this study family?
--     * Slot: family_study_focus Description: What is this study family investigating? EG, a specific condition. The code should be prefixed with a recognizable curie. 
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "FamilyRelationship" Description: "A relationship between two Subjects."
--     * Slot: family_member Description: The family member Subject who is the relationship "subject".
--     * Slot: other_family_member Description: The family member Subject for the relationship "object".
--     * Slot: relationship_code Description: Code definting the relationship predicate. Relationship of the "Family Member" to the "Other Family Member" (i.e. mother, father, etc). Code must be from the HL7 [FamilyMember ValueSet](https://terminology.hl7.org/6.2.0/ValueSet-v3-FamilyMember.html)
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "FamilyMember" Description: "Designates a Subject as a member of a family with some specified role."
--     * Slot: family_member Description: The family member Subject who is the relationship "subject".
--     * Slot: family_role Description: The "role" of this indiviudal in this family.
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
--     * Slot: Family_id Description: Autocreated FK slot
-- # Class: "File" Description: "File"
--     * Slot: filename Description: The name of the file.
--     * Slot: format Description: The format of the file.
--     * Slot: data_type Description: The type of data within this file.
--     * Slot: size Description: Size of the file, in Bytes.
--     * Slot: drs_uri Description: DRS location to access the data.
--     * Slot: file_metadata Description: Additional metadata about the contents of the file, eg, genome reference build.
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
-- # Class: "FileMetadata" Description: "Metadata about the contents of the file."
--     * Slot: code Description: The structured term defining the meaning of the assertion.
--     * Slot: display Description: The friendly display string of the coded term
--     * Slot: value_code Description: The structured term defining the value of the assertion.
--     * Slot: value_display Description: The friendly display string of the coded term for the value of the assertion.
--     * Slot: id Description: ID associated with a class
-- # Class: "Thing_external_id" Description: ""
--     * Slot: Thing_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "AccessControlledRecord_external_id" Description: ""
--     * Slot: AccessControlledRecord_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "Study_external_study_id" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: external_study_id Description: External Study ID
-- # Class: "Study_funding_source" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: funding_source Description: Funding Source
-- # Class: "Study_principal_investigator" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: principal_investigator Description: Principal Investigator
-- # Class: "Study_external_id" Description: ""
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "Sample_processing" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: processing Description: Processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample
-- # Class: "Sample_storage_method" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: storage_method Description: Sample storage method, eg, Frozen or with additives
-- # Class: "Sample_external_id" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "BiospecimenCollection_external_id" Description: ""
--     * Slot: BiospecimenCollection_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "Aliquot_external_id" Description: ""
--     * Slot: Aliquot_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "Subject_external_id" Description: ""
--     * Slot: Subject_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "Demographics_race" Description: ""
--     * Slot: Demographics_id Description: Autocreated FK slot
--     * Slot: race Description: Reported race as defined by the 1997 OMB directives.
-- # Class: "Demographics_source_data" Description: ""
--     * Slot: Demographics_id Description: Autocreated FK slot
--     * Slot: source_data_id Description: The sources from which this assertion was derived
-- # Class: "Demographics_external_id" Description: ""
--     * Slot: Demographics_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "SubjectAssertion_source_data" Description: ""
--     * Slot: SubjectAssertion_id Description: Autocreated FK slot
--     * Slot: source_data_id Description: The sources from which this assertion was derived
-- # Class: "SubjectAssertion_external_id" Description: ""
--     * Slot: SubjectAssertion_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "SourceData_external_id" Description: ""
--     * Slot: SourceData_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "AccessPolicy_data_access_type" Description: ""
--     * Slot: AccessPolicy_id Description: Autocreated FK slot
--     * Slot: data_access_type Description: Data Access Type
-- # Class: "AccessPolicy_access_policy_code" Description: ""
--     * Slot: AccessPolicy_id Description: Autocreated FK slot
--     * Slot: access_policy_code Description: Access Policy Code
-- # Class: "AccessPolicy_external_id" Description: ""
--     * Slot: AccessPolicy_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "Family_family_relationships" Description: ""
--     * Slot: Family_id Description: Autocreated FK slot
--     * Slot: family_relationships_id Description: Family relationships associated with this family.
-- # Class: "Family_external_id" Description: ""
--     * Slot: Family_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "FamilyRelationship_external_id" Description: ""
--     * Slot: FamilyRelationship_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "FamilyMember_external_id" Description: ""
--     * Slot: FamilyMember_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "File_subject" Description: ""
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: subject_id Description: The Subject(s) which this file describes.
-- # Class: "File_sample" Description: ""
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: sample_id Description: The Samples(s) used to generate data in this file.
-- # Class: "File_external_id" Description: ""
--     * Slot: File_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP
-- # Class: "FileMetadata_external_id" Description: ""
--     * Slot: FileMetadata_id Description: Autocreated FK slot
--     * Slot: external_id Description: Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP

CREATE TABLE "Thing" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Study" (
	parent_study_id TEXT, 
	study_title TEXT NOT NULL, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_study_id) REFERENCES "Study" (id)
);
CREATE TABLE "AccessPolicy" (
	disease_limitation TEXT, 
	description TEXT NOT NULL, 
	website TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "FileMetadata" (
	code TEXT, 
	display TEXT, 
	value_code TEXT, 
	value_display TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AccessControlledRecord" (
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "BiospecimenCollection" (
	age_at_collection INTEGER, 
	method VARCHAR, 
	site VARCHAR, 
	spatial_qualifier VARCHAR, 
	laterality VARCHAR, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "Demographics" (
	date_of_birth INTEGER, 
	date_of_birth_type VARCHAR(11), 
	sex VARCHAR(8) NOT NULL, 
	sex_display TEXT NOT NULL, 
	race_display TEXT NOT NULL, 
	ethnicity VARCHAR(22) NOT NULL, 
	ethnicity_display TEXT NOT NULL, 
	age_at_last_vital_status INTEGER, 
	vital_status VARCHAR(12), 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "SourceData" (
	code TEXT, 
	display TEXT, 
	value_code TEXT, 
	value_display TEXT, 
	value_number FLOAT, 
	value_units TEXT, 
	value_units_display TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "Family" (
	family_type VARCHAR(12), 
	family_description TEXT, 
	consanguinity VARCHAR(13), 
	family_study_focus TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "File" (
	filename TEXT, 
	format VARCHAR, 
	data_type VARCHAR, 
	size INTEGER, 
	drs_uri TEXT, 
	file_metadata TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(file_metadata) REFERENCES "FileMetadata" (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "Thing_external_id" (
	"Thing_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Thing_id", external_id), 
	FOREIGN KEY("Thing_id") REFERENCES "Thing" (id)
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
CREATE TABLE "Study_external_id" (
	"Study_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Study_id", external_id), 
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
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
CREATE TABLE "AccessPolicy_external_id" (
	"AccessPolicy_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("AccessPolicy_id", external_id), 
	FOREIGN KEY("AccessPolicy_id") REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "FileMetadata_external_id" (
	"FileMetadata_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("FileMetadata_id", external_id), 
	FOREIGN KEY("FileMetadata_id") REFERENCES "FileMetadata" (id)
);
CREATE TABLE "Subject" (
	subject_type VARCHAR(15) NOT NULL, 
	organism_type TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	has_demographics_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id), 
	FOREIGN KEY(has_demographics_id) REFERENCES "Demographics" (id)
);
CREATE TABLE "AccessControlledRecord_external_id" (
	"AccessControlledRecord_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("AccessControlledRecord_id", external_id), 
	FOREIGN KEY("AccessControlledRecord_id") REFERENCES "AccessControlledRecord" (id)
);
CREATE TABLE "BiospecimenCollection_external_id" (
	"BiospecimenCollection_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("BiospecimenCollection_id", external_id), 
	FOREIGN KEY("BiospecimenCollection_id") REFERENCES "BiospecimenCollection" (id)
);
CREATE TABLE "Demographics_race" (
	"Demographics_id" TEXT, 
	race VARCHAR(35) NOT NULL, 
	PRIMARY KEY ("Demographics_id", race), 
	FOREIGN KEY("Demographics_id") REFERENCES "Demographics" (id)
);
CREATE TABLE "Demographics_source_data" (
	"Demographics_id" TEXT, 
	source_data_id TEXT, 
	PRIMARY KEY ("Demographics_id", source_data_id), 
	FOREIGN KEY("Demographics_id") REFERENCES "Demographics" (id), 
	FOREIGN KEY(source_data_id) REFERENCES "SourceData" (id)
);
CREATE TABLE "Demographics_external_id" (
	"Demographics_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Demographics_id", external_id), 
	FOREIGN KEY("Demographics_id") REFERENCES "Demographics" (id)
);
CREATE TABLE "SourceData_external_id" (
	"SourceData_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("SourceData_id", external_id), 
	FOREIGN KEY("SourceData_id") REFERENCES "SourceData" (id)
);
CREATE TABLE "Family_external_id" (
	"Family_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Family_id", external_id), 
	FOREIGN KEY("Family_id") REFERENCES "Family" (id)
);
CREATE TABLE "File_external_id" (
	"File_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("File_id", external_id), 
	FOREIGN KEY("File_id") REFERENCES "File" (id)
);
CREATE TABLE "Sample" (
	parent_sample TEXT, 
	sample_type TEXT NOT NULL, 
	availablity_status VARCHAR(11), 
	quantity_number FLOAT, 
	quantity_units TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	"Subject_id" TEXT, 
	biospecimen_collection_id TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent_sample) REFERENCES "Sample" (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id), 
	FOREIGN KEY(biospecimen_collection_id) REFERENCES "BiospecimenCollection" (id)
);
CREATE TABLE "SubjectAssertion" (
	assertion_type VARCHAR(18), 
	age_at_assertion FLOAT, 
	age_at_event FLOAT, 
	age_at_resolution FLOAT, 
	code TEXT, 
	display TEXT, 
	value_code TEXT, 
	value_display TEXT, 
	value_number FLOAT, 
	value_units TEXT, 
	value_units_display TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	"Subject_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id)
);
CREATE TABLE "FamilyRelationship" (
	family_member TEXT NOT NULL, 
	other_family_member TEXT NOT NULL, 
	relationship_code TEXT NOT NULL, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(family_member) REFERENCES "Subject" (id), 
	FOREIGN KEY(other_family_member) REFERENCES "Subject" (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id)
);
CREATE TABLE "FamilyMember" (
	family_member TEXT NOT NULL, 
	family_role TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	"Family_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(family_member) REFERENCES "Subject" (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id), 
	FOREIGN KEY("Family_id") REFERENCES "Family" (id)
);
CREATE TABLE "Subject_external_id" (
	"Subject_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Subject_id", external_id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id)
);
CREATE TABLE "File_subject" (
	"File_id" TEXT, 
	subject_id TEXT, 
	PRIMARY KEY ("File_id", subject_id), 
	FOREIGN KEY("File_id") REFERENCES "File" (id), 
	FOREIGN KEY(subject_id) REFERENCES "Subject" (id)
);
CREATE TABLE "Aliquot" (
	availablity_status VARCHAR(11), 
	quantity_number FLOAT, 
	quantity_units TEXT, 
	concentration_number FLOAT, 
	concentration_unit TEXT, 
	has_access_policy TEXT, 
	id TEXT NOT NULL, 
	"Sample_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_access_policy) REFERENCES "AccessPolicy" (id), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE TABLE "Sample_processing" (
	"Sample_id" TEXT, 
	processing TEXT, 
	PRIMARY KEY ("Sample_id", processing), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE TABLE "Sample_storage_method" (
	"Sample_id" TEXT, 
	storage_method TEXT, 
	PRIMARY KEY ("Sample_id", storage_method), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE TABLE "Sample_external_id" (
	"Sample_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Sample_id", external_id), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);
CREATE TABLE "SubjectAssertion_source_data" (
	"SubjectAssertion_id" TEXT, 
	source_data_id TEXT, 
	PRIMARY KEY ("SubjectAssertion_id", source_data_id), 
	FOREIGN KEY("SubjectAssertion_id") REFERENCES "SubjectAssertion" (id), 
	FOREIGN KEY(source_data_id) REFERENCES "SourceData" (id)
);
CREATE TABLE "SubjectAssertion_external_id" (
	"SubjectAssertion_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("SubjectAssertion_id", external_id), 
	FOREIGN KEY("SubjectAssertion_id") REFERENCES "SubjectAssertion" (id)
);
CREATE TABLE "Family_family_relationships" (
	"Family_id" TEXT, 
	family_relationships_id TEXT, 
	PRIMARY KEY ("Family_id", family_relationships_id), 
	FOREIGN KEY("Family_id") REFERENCES "Family" (id), 
	FOREIGN KEY(family_relationships_id) REFERENCES "FamilyRelationship" (id)
);
CREATE TABLE "FamilyRelationship_external_id" (
	"FamilyRelationship_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("FamilyRelationship_id", external_id), 
	FOREIGN KEY("FamilyRelationship_id") REFERENCES "FamilyRelationship" (id)
);
CREATE TABLE "FamilyMember_external_id" (
	"FamilyMember_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("FamilyMember_id", external_id), 
	FOREIGN KEY("FamilyMember_id") REFERENCES "FamilyMember" (id)
);
CREATE TABLE "File_sample" (
	"File_id" TEXT, 
	sample_id TEXT, 
	PRIMARY KEY ("File_id", sample_id), 
	FOREIGN KEY("File_id") REFERENCES "File" (id), 
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id)
);
CREATE TABLE "Aliquot_external_id" (
	"Aliquot_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Aliquot_id", external_id), 
	FOREIGN KEY("Aliquot_id") REFERENCES "Aliquot" (id)
);