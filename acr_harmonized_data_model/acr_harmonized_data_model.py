
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Any(Base):
    """
    
    """
    __tablename__ = 'Any'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    

    def __repr__(self):
        return f"Any(id={self.id},)"



    


class Record(Base):
    """
    One row / entity within the database
    """
    __tablename__ = 'Record'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "RecordExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: RecordExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Record(id={self.id},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class AccessPolicy(Base):
    """
    The access policy that describes the controls around use of data
    """
    __tablename__ = 'AccessPolicy'

    access_policy_id = Column(Text(), primary_key=True, nullable=False )
    data_use_accession = Column(Text())
    data_use_permission = Column(Enum(name='EnumDataUsePermission'), nullable=False )
    data_use_modifier = Column(Enum(name='EnumDataUseModifier'))
    disease_limitation = Column(Text())
    access_description = Column(Text())
    website = Column(Text())
    

    def __repr__(self):
        return f"AccessPolicy(access_policy_id={self.access_policy_id},data_use_accession={self.data_use_accession},data_use_permission={self.data_use_permission},data_use_modifier={self.data_use_modifier},disease_limitation={self.disease_limitation},access_description={self.access_description},website={self.website},)"



    


class Study(Base):
    """
    Study Metadata
    """
    __tablename__ = 'Study'

    parent_study = Column(Text(), ForeignKey('Study.study_id'))
    study_title = Column(Text(), nullable=False )
    study_code = Column(Text(), nullable=False )
    study_short_name = Column(Text())
    study_description = Column(Text(), nullable=False )
    website = Column(Text())
    acknowledgments = Column(Text())
    citation_statement = Column(Text())
    do_id = Column(Text(), ForeignKey('DOI.do_id'))
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), primary_key=True, nullable=False )
    
    
    program_rel = relationship( "StudyProgram" )
    program = association_proxy("program_rel", "program",
                                  creator=lambda x_: StudyProgram(program=x_))
    
    
    funding_source_rel = relationship( "StudyFundingSource" )
    funding_source = association_proxy("funding_source_rel", "funding_source",
                                  creator=lambda x_: StudyFundingSource(funding_source=x_))
    
    
    # ManyToMany
    principal_investigator = relationship( "Investigator", secondary="Study_principal_investigator")
    
    
    # ManyToMany
    contact = relationship( "Investigator", secondary="Study_contact")
    
    
    # ManyToMany
    publication = relationship( "Publication", secondary="Study_publication")
    
    
    external_id_rel = relationship( "StudyExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: StudyExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Study(parent_study={self.parent_study},study_title={self.study_title},study_code={self.study_code},study_short_name={self.study_short_name},study_description={self.study_description},website={self.website},acknowledgments={self.acknowledgments},citation_statement={self.citation_statement},do_id={self.do_id},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class StudyMetadata(Base):
    """
    Additional features about studies that may not apply to all studies
    """
    __tablename__ = 'StudyMetadata'

    study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True, nullable=False )
    selection_criteria = Column(Text())
    vbr_id = Column(Text(), ForeignKey('VirtualBiorepository.vbr_id'))
    expected_number_of_participants = Column(Integer(), nullable=False )
    actual_number_of_participants = Column(Integer(), nullable=False )
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    
    
    participant_lifespan_stage_rel = relationship( "StudyMetadataParticipantLifespanStage" )
    participant_lifespan_stage = association_proxy("participant_lifespan_stage_rel", "participant_lifespan_stage",
                                  creator=lambda x_: StudyMetadataParticipantLifespanStage(participant_lifespan_stage=x_))
    
    
    study_design_rel = relationship( "StudyMetadataStudyDesign" )
    study_design = association_proxy("study_design_rel", "study_design",
                                  creator=lambda x_: StudyMetadataStudyDesign(study_design=x_))
    
    
    clinical_data_source_type_rel = relationship( "StudyMetadataClinicalDataSourceType" )
    clinical_data_source_type = association_proxy("clinical_data_source_type_rel", "clinical_data_source_type",
                                  creator=lambda x_: StudyMetadataClinicalDataSourceType(clinical_data_source_type=x_))
    
    
    data_category_rel = relationship( "StudyMetadataDataCategory" )
    data_category = association_proxy("data_category_rel", "data_category",
                                  creator=lambda x_: StudyMetadataDataCategory(data_category=x_))
    
    
    research_domain_rel = relationship( "StudyMetadataResearchDomain" )
    research_domain = association_proxy("research_domain_rel", "research_domain",
                                  creator=lambda x_: StudyMetadataResearchDomain(research_domain=x_))
    
    
    external_id_rel = relationship( "StudyMetadataExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: StudyMetadataExternalId(external_id=x_))
    

    def __repr__(self):
        return f"StudyMetadata(study_id={self.study_id},selection_criteria={self.selection_criteria},vbr_id={self.vbr_id},expected_number_of_participants={self.expected_number_of_participants},actual_number_of_participants={self.actual_number_of_participants},access_policy_id={self.access_policy_id},)"



    


class VirtualBiorepository(Base):
    """
    An organization that can provide access to specimen for further analysis.
    """
    __tablename__ = 'VirtualBiorepository'

    vbr_id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    institution = Column(Text())
    website = Column(Text())
    vbr_readme = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    # ManyToMany
    contact = relationship( "Investigator", secondary="VirtualBiorepository_contact")
    
    
    external_id_rel = relationship( "VirtualBiorepositoryExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: VirtualBiorepositoryExternalId(external_id=x_))
    

    def __repr__(self):
        return f"VirtualBiorepository(vbr_id={self.vbr_id},name={self.name},institution={self.institution},website={self.website},vbr_readme={self.vbr_readme},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class DOI(Base):
    """
    A DOI is a permanent reference with metadata about a digital object.
    """
    __tablename__ = 'DOI'

    do_id = Column(Text(), primary_key=True, nullable=False )
    bibliographic_reference = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "DOIExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: DOIExternalId(external_id=x_))
    

    def __repr__(self):
        return f"DOI(do_id={self.do_id},bibliographic_reference={self.bibliographic_reference},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Investigator(Base):
    """
    An individual who made contributions to the collection, analysis, or sharing of data.
    """
    __tablename__ = 'Investigator'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    name = Column(Text())
    institution = Column(Text())
    investigator_title = Column(Text())
    email = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "InvestigatorExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: InvestigatorExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Investigator(id={self.id},name={self.name},institution={self.institution},investigator_title={self.investigator_title},email={self.email},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Publication(Base):
    """
    Information about a specific publication.
    """
    __tablename__ = 'Publication'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    bibliographic_reference = Column(Text())
    website = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "PublicationExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: PublicationExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Publication(id={self.id},bibliographic_reference={self.bibliographic_reference},website={self.website},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Subject(Base):
    """
    This entity is the subject about which data or references are recorded. This includes the idea of a human participant in a study, a cell line, an animal model, or any other similar entity.
    """
    __tablename__ = 'Subject'

    subject_id = Column(Text(), primary_key=True, nullable=False )
    subject_type = Column(Enum('participant', 'non_participant', 'cell_line', 'animal_model', 'group', 'other', name='EnumSubjectType'), nullable=False )
    organism_type = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "SubjectExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: SubjectExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Subject(subject_id={self.subject_id},subject_type={self.subject_type},organism_type={self.organism_type},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Demographics(Base):
    """
    Basic participant demographics summary
    """
    __tablename__ = 'Demographics'

    subject_id = Column(Text(), ForeignKey('Subject.subject_id'), primary_key=True, nullable=False )
    sex = Column(Enum('female', 'male', 'other', 'unknown', name='EnumSex'), nullable=False )
    ethnicity = Column(Enum('hispanic_or_latino', 'not_hispanic_or_latino', 'prefer_not_to_answer', 'unknown', name='EnumEthnicity'), nullable=False )
    age_at_last_vital_status = Column(Integer())
    vital_status = Column(Enum('dead', 'alive', name='EnumVitalStatus'))
    age_at_first_engagement = Column(Integer())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    race_rel = relationship( "DemographicsRace" )
    race = association_proxy("race_rel", "race",
                                  creator=lambda x_: DemographicsRace(race=x_))
    
    
    external_id_rel = relationship( "DemographicsExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: DemographicsExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Demographics(subject_id={self.subject_id},sex={self.sex},ethnicity={self.ethnicity},age_at_last_vital_status={self.age_at_last_vital_status},vital_status={self.vital_status},age_at_first_engagement={self.age_at_first_engagement},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Family(Base):
    """
    A group of individuals of some relation who are grouped together in a study.
    """
    __tablename__ = 'Family'

    family_id = Column(Text(), primary_key=True, nullable=False )
    family_type = Column(Enum('control_only', 'duo', 'proband_only', 'trio', 'trio_plus', name='EnumFamilyType'))
    family_description = Column(Text())
    consanguinity = Column(Enum('not_suspected', 'suspected', 'known_present', 'unknown', name='EnumConsanguinityAssertion'))
    family_study_focus = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "FamilyExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FamilyExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Family(family_id={self.family_id},family_type={self.family_type},family_description={self.family_description},consanguinity={self.consanguinity},family_study_focus={self.family_study_focus},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class FamilyRelationship(Base):
    """
    A relationship between two Subjects. Directed as follows <family_member_id> <relationship> <subject_id> <Mother's id> <KIN:027 "isBiologicalMotherOf"> <subject_id>
    """
    __tablename__ = 'FamilyRelationship'

    family_relationship_id = Column(Text(), primary_key=True, nullable=False )
    family_member_id = Column(Text(), ForeignKey('Subject.subject_id'), nullable=False )
    relation = Column(Enum(name='EnumFamilyRelation'), nullable=False )
    subject_id = Column(Text(), ForeignKey('Subject.subject_id'), nullable=False )
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "FamilyRelationshipExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FamilyRelationshipExternalId(external_id=x_))
    

    def __repr__(self):
        return f"FamilyRelationship(family_relationship_id={self.family_relationship_id},family_member_id={self.family_member_id},relation={self.relation},subject_id={self.subject_id},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class FamilyMembership(Base):
    """
    Designates a Subject as a member of a family with a specified role.
    """
    __tablename__ = 'FamilyMembership'

    family_membership_id = Column(Text(), primary_key=True, nullable=False )
    family_id = Column(Text(), ForeignKey('Family.family_id'), nullable=False )
    subject_id = Column(Text(), ForeignKey('Subject.subject_id'), nullable=False )
    family_role = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "FamilyMembershipExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FamilyMembershipExternalId(external_id=x_))
    

    def __repr__(self):
        return f"FamilyMembership(family_membership_id={self.family_membership_id},family_id={self.family_id},subject_id={self.subject_id},family_role={self.family_role},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class SubjectAssertion(Base):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """
    __tablename__ = 'SubjectAssertion'

    assertion_id = Column(Text(), primary_key=True, nullable=False )
    subject_id = Column(Text(), ForeignKey('Subject.subject_id'))
    encounter_id = Column(Text(), ForeignKey('Encounter.encounter_id'))
    assertion_provenance = Column(Enum('medical_record', 'investigator_assessment', 'participant_or_caregiver_report', 'other', name='EnumAssertionProvenance'))
    age_at_assertion = Column(Integer())
    age_at_event = Column(Integer())
    age_at_resolution = Column(Integer())
    concept_source = Column(Text())
    value_number = Column(Float())
    value_source = Column(Text())
    value_unit = Column(Text(), ForeignKey('Concept.concept_curie'))
    value_unit_source = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    # ManyToMany
    concept = relationship( "Concept", secondary="SubjectAssertion_concept")
    
    
    # ManyToMany
    value_concept = relationship( "Concept", secondary="SubjectAssertion_value_concept")
    
    
    external_id_rel = relationship( "SubjectAssertionExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: SubjectAssertionExternalId(external_id=x_))
    

    def __repr__(self):
        return f"SubjectAssertion(assertion_id={self.assertion_id},subject_id={self.subject_id},encounter_id={self.encounter_id},assertion_provenance={self.assertion_provenance},age_at_assertion={self.age_at_assertion},age_at_event={self.age_at_event},age_at_resolution={self.age_at_resolution},concept_source={self.concept_source},value_number={self.value_number},value_source={self.value_source},value_unit={self.value_unit},value_unit_source={self.value_unit_source},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Concept(Base):
    """
    A standardized concept with display information.
    """
    __tablename__ = 'Concept'

    concept_curie = Column(Text(), primary_key=True, nullable=False )
    display = Column(Text())
    

    def __repr__(self):
        return f"Concept(concept_curie={self.concept_curie},display={self.display},)"



    


class Sample(Base):
    """
    A functionally equivalent specimen taken from a participant or processed from such a sample.
    """
    __tablename__ = 'Sample'

    sample_id = Column(Text(), primary_key=True, nullable=False )
    biospecimen_collection_id = Column(Text(), ForeignKey('BiospecimenCollection.biospecimen_collection_id'))
    parent_sample_id = Column(Text(), ForeignKey('Sample.sample_id'))
    sample_type = Column(Text(), nullable=False )
    availablity_status = Column(Enum('available', 'unavailable', name='EnumAvailabilityStatus'))
    quantity_number = Column(Float())
    quantity_unit = Column(Text(), ForeignKey('Concept.concept_curie'))
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    processing_rel = relationship( "SampleProcessing" )
    processing = association_proxy("processing_rel", "processing",
                                  creator=lambda x_: SampleProcessing(processing=x_))
    
    
    storage_method_rel = relationship( "SampleStorageMethod" )
    storage_method = association_proxy("storage_method_rel", "storage_method",
                                  creator=lambda x_: SampleStorageMethod(storage_method=x_))
    
    
    external_id_rel = relationship( "SampleExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: SampleExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Sample(sample_id={self.sample_id},biospecimen_collection_id={self.biospecimen_collection_id},parent_sample_id={self.parent_sample_id},sample_type={self.sample_type},availablity_status={self.availablity_status},quantity_number={self.quantity_number},quantity_unit={self.quantity_unit},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class BiospecimenCollection(Base):
    """
    A biospecimen collection event which yields one or more Samples.
    """
    __tablename__ = 'BiospecimenCollection'

    biospecimen_collection_id = Column(Text(), primary_key=True, nullable=False )
    age_at_collection = Column(Float())
    method = Column(Enum(name='EnumSampleCollectionMethod'))
    site = Column(Enum(name='EnumSite'))
    spatial_qualifier = Column(Enum(name='EnumSpatialQualifiers'))
    laterality = Column(Enum(name='EnumLaterality'))
    encounter_id = Column(Text(), ForeignKey('Encounter.encounter_id'))
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "BiospecimenCollectionExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: BiospecimenCollectionExternalId(external_id=x_))
    

    def __repr__(self):
        return f"BiospecimenCollection(biospecimen_collection_id={self.biospecimen_collection_id},age_at_collection={self.age_at_collection},method={self.method},site={self.site},spatial_qualifier={self.spatial_qualifier},laterality={self.laterality},encounter_id={self.encounter_id},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Aliquot(Base):
    """
    A specific tube or amount of a biospecimen associated with a Sample.
    """
    __tablename__ = 'Aliquot'

    aliquot_id = Column(Text(), primary_key=True, nullable=False )
    sample_id = Column(Text(), ForeignKey('Sample.sample_id'))
    availablity_status = Column(Enum('available', 'unavailable', name='EnumAvailabilityStatus'))
    quantity_number = Column(Float())
    quantity_unit = Column(Text(), ForeignKey('Concept.concept_curie'))
    concentration_number = Column(Float())
    concentration_unit = Column(Text(), ForeignKey('Concept.concept_curie'))
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "AliquotExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: AliquotExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Aliquot(aliquot_id={self.aliquot_id},sample_id={self.sample_id},availablity_status={self.availablity_status},quantity_number={self.quantity_number},quantity_unit={self.quantity_unit},concentration_number={self.concentration_number},concentration_unit={self.concentration_unit},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Encounter(Base):
    """
    An event at which data was collected about a participant, an intervention was made, or information about a participant was recorded.
    """
    __tablename__ = 'Encounter'

    encounter_id = Column(Text(), primary_key=True, nullable=False )
    subject_id = Column(Text(), ForeignKey('Subject.subject_id'))
    encounter_definition_id = Column(Text(), ForeignKey('EncounterDefinition.encounter_definition_id'))
    age_at_event = Column(Integer())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "EncounterExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: EncounterExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Encounter(encounter_id={self.encounter_id},subject_id={self.subject_id},encounter_definition_id={self.encounter_definition_id},age_at_event={self.age_at_event},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class EncounterDefinition(Base):
    """
    A definition of an encounter type in this study, ie, an event at which data was collected about a participant, an intervention was made, or information about a participant was recorded. This may be something planned by a study or a type of data collection.
    """
    __tablename__ = 'EncounterDefinition'

    encounter_definition_id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    # ManyToMany
    activity_definition_id = relationship( "ActivityDefinition", secondary="EncounterDefinition_activity_definition_id")
    
    
    external_id_rel = relationship( "EncounterDefinitionExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: EncounterDefinitionExternalId(external_id=x_))
    

    def __repr__(self):
        return f"EncounterDefinition(encounter_definition_id={self.encounter_definition_id},name={self.name},description={self.description},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class ActivityDefinition(Base):
    """
    A definition of an activity in this study, eg, a biospecimen collection, assay, intervention, survey, or assessment.
    """
    __tablename__ = 'ActivityDefinition'

    activity_definition_id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    external_id_rel = relationship( "ActivityDefinitionExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: ActivityDefinitionExternalId(external_id=x_))
    

    def __repr__(self):
        return f"ActivityDefinition(activity_definition_id={self.activity_definition_id},name={self.name},description={self.description},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class File(Base):
    """
    File
    """
    __tablename__ = 'File'

    file_id = Column(Text(), primary_key=True, nullable=False )
    filename = Column(Text())
    format = Column(Enum(name='EnumEDAMFormats'))
    file_extension = Column(Text(), nullable=False )
    data_category = Column(Enum('unharmonized_demographic_clinical_data', 'harmonized_demographic_clinical_data', 'genomics', 'transcriptomics', 'epigenomics', 'proteomics', 'metabolomics', 'cognitive_behavioral', 'immune_profiling', 'imaging', 'microbiome', 'fitness', 'physical_activity', 'other', 'sleep_study', name='EnumDataCategory'))
    data_type = Column(Enum(name='EnumEDAMDataTypes'))
    size = Column(Integer())
    internal_uri = Column(Text())
    release_uri = Column(Text())
    drs_uri = Column(Text())
    storage_class = Column(Text())
    availability = Column(Enum('snomed_ct:103328004', 'snomed_ct:103329007', name='EnumFileAvailability'))
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    # ManyToMany
    subject_id = relationship( "Subject", secondary="File_subject_id")
    
    
    # ManyToMany
    sample_id = relationship( "Sample", secondary="File_sample_id")
    
    
    # ManyToMany
    hash = relationship( "FileHash", secondary="File_hash")
    
    
    external_id_rel = relationship( "FileExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FileExternalId(external_id=x_))
    

    def __repr__(self):
        return f"File(file_id={self.file_id},filename={self.filename},format={self.format},file_extension={self.file_extension},data_category={self.data_category},data_type={self.data_type},size={self.size},internal_uri={self.internal_uri},release_uri={self.release_uri},drs_uri={self.drs_uri},storage_class={self.storage_class},availability={self.availability},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class FileHash(Base):
    """
    Type and value of a file content hash.
    """
    __tablename__ = 'FileHash'

    id = Column(Integer(), primary_key=True, autoincrement=True , nullable=False )
    hash_type = Column(Enum('md5', 'etag', 'sha1', name='EnumFileHashType'))
    hash_value = Column(Text())
    

    def __repr__(self):
        return f"FileHash(id={self.id},hash_type={self.hash_type},hash_value={self.hash_value},)"



    


class Assay(Base):
    """
    A specific assay that was performed on given subject(s) or sample(s).
    """
    __tablename__ = 'Assay'

    assay_id = Column(Text(), primary_key=True, nullable=False )
    assay_type = Column(Enum(name='EnumAssayType'), nullable=False )
    assay_source = Column(Text())
    activity_definition_id = Column(Text(), ForeignKey('ActivityDefinition.activity_definition_id'))
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    # ManyToMany
    subject_id = relationship( "Subject", secondary="Assay_subject_id")
    
    
    # ManyToMany
    sample_id = relationship( "Sample", secondary="Assay_sample_id")
    
    
    # ManyToMany
    file_id = relationship( "File", secondary="Assay_file_id")
    
    
    external_id_rel = relationship( "AssayExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: AssayExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Assay(assay_id={self.assay_id},assay_type={self.assay_type},assay_source={self.assay_source},activity_definition_id={self.activity_definition_id},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class Dataset(Base):
    """
    Set of files grouped together for release.
    """
    __tablename__ = 'Dataset'

    dataset_id = Column(Text(), primary_key=True, nullable=False )
    name = Column(Text())
    description = Column(Text())
    do_id = Column(Text(), ForeignKey('DOI.do_id'))
    data_collection_start = Column(Text())
    data_collection_end = Column(Text())
    
    
    # ManyToMany
    file_id = relationship( "File", secondary="Dataset_file_id")
    
    
    # ManyToMany
    publication = relationship( "Publication", secondary="Dataset_publication")
    

    def __repr__(self):
        return f"Dataset(dataset_id={self.dataset_id},name={self.name},description={self.description},do_id={self.do_id},data_collection_start={self.data_collection_start},data_collection_end={self.data_collection_end},)"



    


class RecordExternalId(Base):
    """
    
    """
    __tablename__ = 'Record_external_id'

    Record_id = Column(Integer(), ForeignKey('Record.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Record_external_id(Record_id={self.Record_id},external_id={self.external_id},)"



    


class StudyProgram(Base):
    """
    
    """
    __tablename__ = 'Study_program'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    program = Column(Enum('include', 'kf', 'other', name='EnumProgram'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Study_program(Study_study_id={self.Study_study_id},program={self.program},)"



    


class StudyFundingSource(Base):
    """
    
    """
    __tablename__ = 'Study_funding_source'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    funding_source = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_funding_source(Study_study_id={self.Study_study_id},funding_source={self.funding_source},)"



    


class StudyPrincipalInvestigator(Base):
    """
    
    """
    __tablename__ = 'Study_principal_investigator'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    principal_investigator_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Study_principal_investigator(Study_study_id={self.Study_study_id},principal_investigator_id={self.principal_investigator_id},)"



    


class StudyContact(Base):
    """
    
    """
    __tablename__ = 'Study_contact'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    contact_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Study_contact(Study_study_id={self.Study_study_id},contact_id={self.contact_id},)"



    


class StudyPublication(Base):
    """
    
    """
    __tablename__ = 'Study_publication'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    publication_id = Column(Integer(), ForeignKey('Publication.id'), primary_key=True)
    

    def __repr__(self):
        return f"Study_publication(Study_study_id={self.Study_study_id},publication_id={self.publication_id},)"



    


class StudyExternalId(Base):
    """
    
    """
    __tablename__ = 'Study_external_id'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_external_id(Study_study_id={self.Study_study_id},external_id={self.external_id},)"



    


class StudyMetadataParticipantLifespanStage(Base):
    """
    
    """
    __tablename__ = 'StudyMetadata_participant_lifespan_stage'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    participant_lifespan_stage = Column(Enum('fetal', 'neonatal', 'pediatric', 'adult', name='EnumParticipantLifespanStage'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_participant_lifespan_stage(StudyMetadata_study_id={self.StudyMetadata_study_id},participant_lifespan_stage={self.participant_lifespan_stage},)"



    


class StudyMetadataStudyDesign(Base):
    """
    
    """
    __tablename__ = 'StudyMetadata_study_design'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    study_design = Column(Enum('case_control', 'case_set', 'control_set', 'clinical_trial', 'cross_sectional', 'family_twins_trios', 'interventional', 'longitudinal', 'trial_readiness_study', 'tumor_vs_matched_normal', name='EnumStudyDesign'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_study_design(StudyMetadata_study_id={self.StudyMetadata_study_id},study_design={self.study_design},)"



    


class StudyMetadataClinicalDataSourceType(Base):
    """
    
    """
    __tablename__ = 'StudyMetadata_clinical_data_source_type'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    clinical_data_source_type = Column(Enum('medical_record', 'investigator_assessment', 'participant_or_caregiver_report', 'other', 'unknown', name='EnumClinicalDataSourceType'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_clinical_data_source_type(StudyMetadata_study_id={self.StudyMetadata_study_id},clinical_data_source_type={self.clinical_data_source_type},)"



    


class StudyMetadataDataCategory(Base):
    """
    
    """
    __tablename__ = 'StudyMetadata_data_category'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    data_category = Column(Enum('unharmonized_demographic_clinical_data', 'harmonized_demographic_clinical_data', 'genomics', 'transcriptomics', 'epigenomics', 'proteomics', 'metabolomics', 'cognitive_behavioral', 'immune_profiling', 'imaging', 'microbiome', 'fitness', 'physical_activity', 'other', 'sleep_study', name='EnumDataCategory'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_data_category(StudyMetadata_study_id={self.StudyMetadata_study_id},data_category={self.data_category},)"



    


class StudyMetadataResearchDomain(Base):
    """
    
    """
    __tablename__ = 'StudyMetadata_research_domain'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    research_domain = Column(Enum('behavior_and_behavior_mechanisms', 'congenital_heart_defects', 'immune_system_diseases', 'hematologic_diseases', 'neurodevelopment', 'sleep_wake_disorders', 'all_co_occurring_conditions', 'physical_fitness', 'other', name='EnumResearchDomain'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_research_domain(StudyMetadata_study_id={self.StudyMetadata_study_id},research_domain={self.research_domain},)"



    


class StudyMetadataExternalId(Base):
    """
    
    """
    __tablename__ = 'StudyMetadata_external_id'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"StudyMetadata_external_id(StudyMetadata_study_id={self.StudyMetadata_study_id},external_id={self.external_id},)"



    


class VirtualBiorepositoryContact(Base):
    """
    
    """
    __tablename__ = 'VirtualBiorepository_contact'

    VirtualBiorepository_vbr_id = Column(Text(), ForeignKey('VirtualBiorepository.vbr_id'), primary_key=True)
    contact_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"VirtualBiorepository_contact(VirtualBiorepository_vbr_id={self.VirtualBiorepository_vbr_id},contact_id={self.contact_id},)"



    


class VirtualBiorepositoryExternalId(Base):
    """
    
    """
    __tablename__ = 'VirtualBiorepository_external_id'

    VirtualBiorepository_vbr_id = Column(Text(), ForeignKey('VirtualBiorepository.vbr_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"VirtualBiorepository_external_id(VirtualBiorepository_vbr_id={self.VirtualBiorepository_vbr_id},external_id={self.external_id},)"



    


class DOIExternalId(Base):
    """
    
    """
    __tablename__ = 'DOI_external_id'

    DOI_do_id = Column(Text(), ForeignKey('DOI.do_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"DOI_external_id(DOI_do_id={self.DOI_do_id},external_id={self.external_id},)"



    


class InvestigatorExternalId(Base):
    """
    
    """
    __tablename__ = 'Investigator_external_id'

    Investigator_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Investigator_external_id(Investigator_id={self.Investigator_id},external_id={self.external_id},)"



    


class PublicationExternalId(Base):
    """
    
    """
    __tablename__ = 'Publication_external_id'

    Publication_id = Column(Integer(), ForeignKey('Publication.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Publication_external_id(Publication_id={self.Publication_id},external_id={self.external_id},)"



    


class SubjectExternalId(Base):
    """
    
    """
    __tablename__ = 'Subject_external_id'

    Subject_subject_id = Column(Text(), ForeignKey('Subject.subject_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Subject_external_id(Subject_subject_id={self.Subject_subject_id},external_id={self.external_id},)"



    


class DemographicsRace(Base):
    """
    
    """
    __tablename__ = 'Demographics_race'

    Demographics_subject_id = Column(Text(), ForeignKey('Demographics.subject_id'), primary_key=True)
    race = Column(Enum('american_indian_or_alaska_native', 'asian', 'black_or_african_american', 'more_than_one_race', 'native_hawaiian_or_other_pacific_islander', 'other', 'white', 'prefer_not_to_answer', 'unknown', 'east_asian', 'latin_american', 'middle_eastern_or_north_african', 'south_asian', name='EnumRace'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Demographics_race(Demographics_subject_id={self.Demographics_subject_id},race={self.race},)"



    


class DemographicsExternalId(Base):
    """
    
    """
    __tablename__ = 'Demographics_external_id'

    Demographics_subject_id = Column(Text(), ForeignKey('Demographics.subject_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Demographics_external_id(Demographics_subject_id={self.Demographics_subject_id},external_id={self.external_id},)"



    


class FamilyExternalId(Base):
    """
    
    """
    __tablename__ = 'Family_external_id'

    Family_family_id = Column(Text(), ForeignKey('Family.family_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Family_external_id(Family_family_id={self.Family_family_id},external_id={self.external_id},)"



    


class FamilyRelationshipExternalId(Base):
    """
    
    """
    __tablename__ = 'FamilyRelationship_external_id'

    FamilyRelationship_family_relationship_id = Column(Text(), ForeignKey('FamilyRelationship.family_relationship_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FamilyRelationship_external_id(FamilyRelationship_family_relationship_id={self.FamilyRelationship_family_relationship_id},external_id={self.external_id},)"



    


class FamilyMembershipExternalId(Base):
    """
    
    """
    __tablename__ = 'FamilyMembership_external_id'

    FamilyMembership_family_membership_id = Column(Text(), ForeignKey('FamilyMembership.family_membership_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FamilyMembership_external_id(FamilyMembership_family_membership_id={self.FamilyMembership_family_membership_id},external_id={self.external_id},)"



    


class SubjectAssertionConcept(Base):
    """
    
    """
    __tablename__ = 'SubjectAssertion_concept'

    SubjectAssertion_assertion_id = Column(Text(), ForeignKey('SubjectAssertion.assertion_id'), primary_key=True)
    concept_concept_curie = Column(Text(), ForeignKey('Concept.concept_curie'), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_concept(SubjectAssertion_assertion_id={self.SubjectAssertion_assertion_id},concept_concept_curie={self.concept_concept_curie},)"



    


class SubjectAssertionValueConcept(Base):
    """
    
    """
    __tablename__ = 'SubjectAssertion_value_concept'

    SubjectAssertion_assertion_id = Column(Text(), ForeignKey('SubjectAssertion.assertion_id'), primary_key=True)
    value_concept_concept_curie = Column(Text(), ForeignKey('Concept.concept_curie'), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_value_concept(SubjectAssertion_assertion_id={self.SubjectAssertion_assertion_id},value_concept_concept_curie={self.value_concept_concept_curie},)"



    


class SubjectAssertionExternalId(Base):
    """
    
    """
    __tablename__ = 'SubjectAssertion_external_id'

    SubjectAssertion_assertion_id = Column(Text(), ForeignKey('SubjectAssertion.assertion_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_external_id(SubjectAssertion_assertion_id={self.SubjectAssertion_assertion_id},external_id={self.external_id},)"



    


class SampleProcessing(Base):
    """
    
    """
    __tablename__ = 'Sample_processing'

    Sample_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    processing = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_processing(Sample_sample_id={self.Sample_sample_id},processing={self.processing},)"



    


class SampleStorageMethod(Base):
    """
    
    """
    __tablename__ = 'Sample_storage_method'

    Sample_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    storage_method = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_storage_method(Sample_sample_id={self.Sample_sample_id},storage_method={self.storage_method},)"



    


class SampleExternalId(Base):
    """
    
    """
    __tablename__ = 'Sample_external_id'

    Sample_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_external_id(Sample_sample_id={self.Sample_sample_id},external_id={self.external_id},)"



    


class BiospecimenCollectionExternalId(Base):
    """
    
    """
    __tablename__ = 'BiospecimenCollection_external_id'

    BiospecimenCollection_biospecimen_collection_id = Column(Text(), ForeignKey('BiospecimenCollection.biospecimen_collection_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"BiospecimenCollection_external_id(BiospecimenCollection_biospecimen_collection_id={self.BiospecimenCollection_biospecimen_collection_id},external_id={self.external_id},)"



    


class AliquotExternalId(Base):
    """
    
    """
    __tablename__ = 'Aliquot_external_id'

    Aliquot_aliquot_id = Column(Text(), ForeignKey('Aliquot.aliquot_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Aliquot_external_id(Aliquot_aliquot_id={self.Aliquot_aliquot_id},external_id={self.external_id},)"



    


class EncounterExternalId(Base):
    """
    
    """
    __tablename__ = 'Encounter_external_id'

    Encounter_encounter_id = Column(Text(), ForeignKey('Encounter.encounter_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Encounter_external_id(Encounter_encounter_id={self.Encounter_encounter_id},external_id={self.external_id},)"



    


class EncounterDefinitionActivityDefinitionId(Base):
    """
    
    """
    __tablename__ = 'EncounterDefinition_activity_definition_id'

    EncounterDefinition_encounter_definition_id = Column(Text(), ForeignKey('EncounterDefinition.encounter_definition_id'), primary_key=True)
    activity_definition_id_activity_definition_id = Column(Text(), ForeignKey('ActivityDefinition.activity_definition_id'), primary_key=True)
    

    def __repr__(self):
        return f"EncounterDefinition_activity_definition_id(EncounterDefinition_encounter_definition_id={self.EncounterDefinition_encounter_definition_id},activity_definition_id_activity_definition_id={self.activity_definition_id_activity_definition_id},)"



    


class EncounterDefinitionExternalId(Base):
    """
    
    """
    __tablename__ = 'EncounterDefinition_external_id'

    EncounterDefinition_encounter_definition_id = Column(Text(), ForeignKey('EncounterDefinition.encounter_definition_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"EncounterDefinition_external_id(EncounterDefinition_encounter_definition_id={self.EncounterDefinition_encounter_definition_id},external_id={self.external_id},)"



    


class ActivityDefinitionExternalId(Base):
    """
    
    """
    __tablename__ = 'ActivityDefinition_external_id'

    ActivityDefinition_activity_definition_id = Column(Text(), ForeignKey('ActivityDefinition.activity_definition_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ActivityDefinition_external_id(ActivityDefinition_activity_definition_id={self.ActivityDefinition_activity_definition_id},external_id={self.external_id},)"



    


class FileSubjectId(Base):
    """
    
    """
    __tablename__ = 'File_subject_id'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    subject_id_subject_id = Column(Text(), ForeignKey('Subject.subject_id'), primary_key=True)
    

    def __repr__(self):
        return f"File_subject_id(File_file_id={self.File_file_id},subject_id_subject_id={self.subject_id_subject_id},)"



    


class FileSampleId(Base):
    """
    
    """
    __tablename__ = 'File_sample_id'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    sample_id_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    

    def __repr__(self):
        return f"File_sample_id(File_file_id={self.File_file_id},sample_id_sample_id={self.sample_id_sample_id},)"



    


class FileHash(Base):
    """
    
    """
    __tablename__ = 'File_hash'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    hash_id = Column(Integer(), ForeignKey('FileHash.id'), primary_key=True)
    

    def __repr__(self):
        return f"File_hash(File_file_id={self.File_file_id},hash_id={self.hash_id},)"



    


class FileExternalId(Base):
    """
    
    """
    __tablename__ = 'File_external_id'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"File_external_id(File_file_id={self.File_file_id},external_id={self.external_id},)"



    


class AssaySubjectId(Base):
    """
    
    """
    __tablename__ = 'Assay_subject_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    subject_id_subject_id = Column(Text(), ForeignKey('Subject.subject_id'), primary_key=True)
    

    def __repr__(self):
        return f"Assay_subject_id(Assay_assay_id={self.Assay_assay_id},subject_id_subject_id={self.subject_id_subject_id},)"



    


class AssaySampleId(Base):
    """
    
    """
    __tablename__ = 'Assay_sample_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    sample_id_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    

    def __repr__(self):
        return f"Assay_sample_id(Assay_assay_id={self.Assay_assay_id},sample_id_sample_id={self.sample_id_sample_id},)"



    


class AssayFileId(Base):
    """
    
    """
    __tablename__ = 'Assay_file_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    file_id_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    

    def __repr__(self):
        return f"Assay_file_id(Assay_assay_id={self.Assay_assay_id},file_id_file_id={self.file_id_file_id},)"



    


class AssayExternalId(Base):
    """
    
    """
    __tablename__ = 'Assay_external_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Assay_external_id(Assay_assay_id={self.Assay_assay_id},external_id={self.external_id},)"



    


class DatasetFileId(Base):
    """
    
    """
    __tablename__ = 'Dataset_file_id'

    Dataset_dataset_id = Column(Text(), ForeignKey('Dataset.dataset_id'), primary_key=True)
    file_id_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    

    def __repr__(self):
        return f"Dataset_file_id(Dataset_dataset_id={self.Dataset_dataset_id},file_id_file_id={self.file_id_file_id},)"



    


class DatasetPublication(Base):
    """
    
    """
    __tablename__ = 'Dataset_publication'

    Dataset_dataset_id = Column(Text(), ForeignKey('Dataset.dataset_id'), primary_key=True)
    publication_id = Column(Integer(), ForeignKey('Publication.id'), primary_key=True)
    

    def __repr__(self):
        return f"Dataset_publication(Dataset_dataset_id={self.Dataset_dataset_id},publication_id={self.publication_id},)"



    


