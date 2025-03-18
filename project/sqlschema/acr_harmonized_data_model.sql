-- # Class: "Thing" Description: "Highest Level Class"
--     * Slot: id Description: ID associated with a class
-- # Class: "AccessControlledRecord" Description: "Element for which specific access control restrictions apply."
--     * Slot: has_access_policy Description: Which access policy applies to this element?
--     * Slot: id Description: ID associated with a class
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
--     * Slot: Subject_id Description: Autocreated FK slot
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
--     * Slot: processing Description: Curied code associated processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample
-- # Class: "Sample_external_id" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
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
CREATE TABLE "AccessControlledRecord" (
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
CREATE TABLE "Sample" (
	parent_sample_id TEXT, 
	biospecimen_collection_id_fk TEXT NOT NULL, 
	sample_type TEXT NOT NULL, 
	availablity_status VARCHAR(11), 
	storage_method TEXT, 
	quantity TEXT, 
	id TEXT NOT NULL, 
	"Subject_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id)
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
CREATE TABLE "Subject_external_id" (
	"Subject_id" TEXT, 
	external_id TEXT, 
	PRIMARY KEY ("Subject_id", external_id), 
	FOREIGN KEY("Subject_id") REFERENCES "Subject" (id)
);
CREATE TABLE "Sample_processing" (
	"Sample_id" TEXT, 
	processing TEXT, 
	PRIMARY KEY ("Sample_id", processing), 
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