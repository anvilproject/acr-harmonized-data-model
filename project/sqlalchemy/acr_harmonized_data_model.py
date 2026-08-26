
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Any(Base):
    """
    None
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
    data_use_permission = Column(Enum('DUO:0000004', 'DUO:0000006', 'DUO:0000007', 'DUO:0000011', 'DUO:0000042', name='EnumDataUsePermission'), nullable=False )
    data_use_modifier = Column(Enum('DUO:00000044', 'DUO:0000012', 'DUO:0000015', 'DUO:0000016', 'DUO:0000018', 'DUO:0000019', 'DUO:0000020', 'DUO:0000021', 'DUO:0000022', 'DUO:0000024', 'DUO:0000025', 'DUO:0000026', 'DUO:0000027', 'DUO:0000028', 'DUO:0000029', 'DUO:0000043', 'DUO:0000045', 'DUO:0000046', name='EnumDataUseModifier'))
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
    
    
    # ManyToMany
    study_design = relationship( "Concept", secondary="StudyMetadata_study_design")
    
    
    clinical_data_source_type_rel = relationship( "StudyMetadataClinicalDataSourceType" )
    clinical_data_source_type = association_proxy("clinical_data_source_type_rel", "clinical_data_source_type",
                                  creator=lambda x_: StudyMetadataClinicalDataSourceType(clinical_data_source_type=x_))
    
    
    data_category_rel = relationship( "StudyMetadataDataCategory" )
    data_category = association_proxy("data_category_rel", "data_category",
                                  creator=lambda x_: StudyMetadataDataCategory(data_category=x_))
    
    
    # ManyToMany
    research_domain = relationship( "Concept", secondary="StudyMetadata_research_domain")
    
    
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
    subject_type = Column(Text(), ForeignKey('Concept.concept_curie'), nullable=False )
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
    sex = Column(Text(), ForeignKey('Concept.concept_curie'), nullable=False )
    ethnicity = Column(Text(), ForeignKey('Concept.concept_curie'), nullable=False )
    age_at_last_vital_status = Column(Integer())
    vital_status = Column(Text(), ForeignKey('Concept.concept_curie'))
    age_at_first_engagement = Column(Integer())
    access_policy_id = Column(Text(), ForeignKey('AccessPolicy.access_policy_id'))
    study_id = Column(Text(), ForeignKey('Study.study_id'))
    
    
    # ManyToMany
    race = relationship( "Concept", secondary="Demographics_race")
    
    
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
    family_type = Column(Enum('CAMO:0000002', 'CAMO:0000003', 'CAMO:0000004', 'CAMO:0000005', 'CAMO:0000006', 'CAMO:0000007', 'CAMO:0000008', name='EnumFamilyType'))
    family_description = Column(Text())
    consanguinity = Column(Enum('snomedct:410515003', 'snomedct:410516002', 'snomedct:410590009', 'snomedct:410591008', 'snomedct:410592001', 'snomedct:410593006', 'snomedct:410594000', 'snomedct:410605003', 'snomedct:415684004', 'snomedct:428263003', 'snomedct:723511001', name='EnumPresentAbsent'))
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
    relation = Column(Text(), ForeignKey('Concept.concept_curie'), nullable=False )
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
    asserter_type = Column(Enum('CAMO:0000016', 'CAMO:0000017', 'CAMO:0000018', 'CAMO:0000019', 'CAMO:0000020', 'CAMO:0000021', name='EnumAsserterType'))
    assertion_source_type = Column(Enum('CAMO:0000014', 'CAMO:0000010', 'CAMO:0000011', 'CAMO:0000012', 'CAMO:0000013', name='EnumDataSourceType'))
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
        return f"SubjectAssertion(assertion_id={self.assertion_id},subject_id={self.subject_id},encounter_id={self.encounter_id},asserter_type={self.asserter_type},assertion_source_type={self.assertion_source_type},age_at_assertion={self.age_at_assertion},age_at_event={self.age_at_event},age_at_resolution={self.age_at_resolution},concept_source={self.concept_source},value_number={self.value_number},value_source={self.value_source},value_unit={self.value_unit},value_unit_source={self.value_unit_source},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


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
    availability_status = Column(Enum('snomedct:103328004', 'snomedct:103329007', name='EnumAvailabilityStatus'))
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
        return f"Sample(sample_id={self.sample_id},biospecimen_collection_id={self.biospecimen_collection_id},parent_sample_id={self.parent_sample_id},sample_type={self.sample_type},availability_status={self.availability_status},quantity_number={self.quantity_number},quantity_unit={self.quantity_unit},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


class BiospecimenCollection(Base):
    """
    A biospecimen collection event which yields one or more Samples.
    """
    __tablename__ = 'BiospecimenCollection'

    biospecimen_collection_id = Column(Text(), primary_key=True, nullable=False )
    age_at_collection = Column(Float())
    method = Column(Enum(name='EnumSampleCollectionMethod'))
    site = Column(Text(), ForeignKey('Concept.concept_curie'))
    spatial_qualifier = Column(Text(), ForeignKey('Concept.concept_curie'))
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
    availability_status = Column(Enum('snomedct:103328004', 'snomedct:103329007', name='EnumAvailabilityStatus'))
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
        return f"Aliquot(aliquot_id={self.aliquot_id},sample_id={self.sample_id},availability_status={self.availability_status},quantity_number={self.quantity_number},quantity_unit={self.quantity_unit},concentration_number={self.concentration_number},concentration_unit={self.concentration_unit},access_policy_id={self.access_policy_id},study_id={self.study_id},)"



    


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
    format = Column(Enum('edam:format_1196', 'edam:format_1197', 'edam:format_1198', 'edam:format_1199', 'edam:format_1200', 'edam:format_1206', 'edam:format_1207', 'edam:format_1208', 'edam:format_1209', 'edam:format_1210', 'edam:format_1211', 'edam:format_1212', 'edam:format_1213', 'edam:format_1214', 'edam:format_1215', 'edam:format_1216', 'edam:format_1217', 'edam:format_1218', 'edam:format_1219', 'edam:format_1248', 'edam:format_1295', 'edam:format_1296', 'edam:format_1297', 'edam:format_1316', 'edam:format_1318', 'edam:format_1319', 'edam:format_1320', 'edam:format_1332', 'edam:format_1333', 'edam:format_1334', 'edam:format_1335', 'edam:format_1336', 'edam:format_1337', 'edam:format_1341', 'edam:format_1342', 'edam:format_1343', 'edam:format_1349', 'edam:format_1350', 'edam:format_1351', 'edam:format_1356', 'edam:format_1357', 'edam:format_1360', 'edam:format_1366', 'edam:format_1367', 'edam:format_1369', 'edam:format_1370', 'edam:format_1391', 'edam:format_1392', 'edam:format_1393', 'edam:format_1419', 'edam:format_1421', 'edam:format_1422', 'edam:format_1423', 'edam:format_1424', 'edam:format_1425', 'edam:format_1430', 'edam:format_1432', 'edam:format_1433', 'edam:format_1434', 'edam:format_1435', 'edam:format_1436', 'edam:format_1437', 'edam:format_1445', 'edam:format_1454', 'edam:format_1455', 'edam:format_1457', 'edam:format_1458', 'edam:format_1475', 'edam:format_1476', 'edam:format_1477', 'edam:format_1478', 'edam:format_1504', 'edam:format_1551', 'edam:format_1552', 'edam:format_1582', 'edam:format_1627', 'edam:format_1628', 'edam:format_1629', 'edam:format_1630', 'edam:format_1631', 'edam:format_1632', 'edam:format_1633', 'edam:format_1637', 'edam:format_1638', 'edam:format_1639', 'edam:format_1641', 'edam:format_1644', 'edam:format_1665', 'edam:format_1705', 'edam:format_1734', 'edam:format_1735', 'edam:format_1736', 'edam:format_1737', 'edam:format_1739', 'edam:format_1740', 'edam:format_1741', 'edam:format_1861', 'edam:format_1910', 'edam:format_1911', 'edam:format_1912', 'edam:format_1919', 'edam:format_1920', 'edam:format_1921', 'edam:format_1923', 'edam:format_1925', 'edam:format_1926', 'edam:format_1927', 'edam:format_1928', 'edam:format_1929', 'edam:format_1930', 'edam:format_1931', 'edam:format_1932', 'edam:format_1933', 'edam:format_1934', 'edam:format_1935', 'edam:format_1936', 'edam:format_1937', 'edam:format_1938', 'edam:format_1939', 'edam:format_1940', 'edam:format_1941', 'edam:format_1942', 'edam:format_1943', 'edam:format_1944', 'edam:format_1945', 'edam:format_1946', 'edam:format_1947', 'edam:format_1948', 'edam:format_1949', 'edam:format_1950', 'edam:format_1951', 'edam:format_1952', 'edam:format_1953', 'edam:format_1954', 'edam:format_1957', 'edam:format_1958', 'edam:format_1960', 'edam:format_1961', 'edam:format_1962', 'edam:format_1963', 'edam:format_1964', 'edam:format_1966', 'edam:format_1967', 'edam:format_1968', 'edam:format_1969', 'edam:format_1970', 'edam:format_1972', 'edam:format_1973', 'edam:format_1974', 'edam:format_1975', 'edam:format_1978', 'edam:format_1979', 'edam:format_1982', 'edam:format_1983', 'edam:format_1984', 'edam:format_1985', 'edam:format_1986', 'edam:format_1987', 'edam:format_1988', 'edam:format_1989', 'edam:format_1990', 'edam:format_1991', 'edam:format_1992', 'edam:format_1996', 'edam:format_1997', 'edam:format_1998', 'edam:format_1999', 'edam:format_2000', 'edam:format_2001', 'edam:format_2002', 'edam:format_2003', 'edam:format_2004', 'edam:format_2005', 'edam:format_2006', 'edam:format_2013', 'edam:format_2014', 'edam:format_2017', 'edam:format_2020', 'edam:format_2021', 'edam:format_2027', 'edam:format_2030', 'edam:format_2031', 'edam:format_2032', 'edam:format_2033', 'edam:format_2035', 'edam:format_2036', 'edam:format_2037', 'edam:format_2038', 'edam:format_2039', 'edam:format_2040', 'edam:format_2049', 'edam:format_2052', 'edam:format_2054', 'edam:format_2055', 'edam:format_2056', 'edam:format_2057', 'edam:format_2058', 'edam:format_2060', 'edam:format_2061', 'edam:format_2062', 'edam:format_2064', 'edam:format_2065', 'edam:format_2066', 'edam:format_2067', 'edam:format_2068', 'edam:format_2069', 'edam:format_2072', 'edam:format_2074', 'edam:format_2075', 'edam:format_2076', 'edam:format_2077', 'edam:format_2078', 'edam:format_2094', 'edam:format_2095', 'edam:format_2096', 'edam:format_2097', 'edam:format_2155', 'edam:format_2158', 'edam:format_2170', 'edam:format_2171', 'edam:format_2172', 'edam:format_2181', 'edam:format_2182', 'edam:format_2183', 'edam:format_2184', 'edam:format_2185', 'edam:format_2186', 'edam:format_2187', 'edam:format_2194', 'edam:format_2195', 'edam:format_2196', 'edam:format_2197', 'edam:format_2200', 'edam:format_2204', 'edam:format_2205', 'edam:format_2206', 'edam:format_2304', 'edam:format_2305', 'edam:format_2306', 'edam:format_2310', 'edam:format_2311', 'edam:format_2330', 'edam:format_2331', 'edam:format_2332', 'edam:format_2333', 'edam:format_2350', 'edam:format_2352', 'edam:format_2376', 'edam:format_2532', 'edam:format_2543', 'edam:format_2545', 'edam:format_2546', 'edam:format_2547', 'edam:format_2548', 'edam:format_2549', 'edam:format_2550', 'edam:format_2551', 'edam:format_2552', 'edam:format_2553', 'edam:format_2554', 'edam:format_2555', 'edam:format_2556', 'edam:format_2557', 'edam:format_2558', 'edam:format_2559', 'edam:format_2561', 'edam:format_2566', 'edam:format_2567', 'edam:format_2568', 'edam:format_2569', 'edam:format_2570', 'edam:format_2571', 'edam:format_2572', 'edam:format_2573', 'edam:format_2585', 'edam:format_2607', 'edam:format_2848', 'edam:format_2919', 'edam:format_2920', 'edam:format_2921', 'edam:format_2922', 'edam:format_2923', 'edam:format_2924', 'edam:format_3000', 'edam:format_3001', 'edam:format_3003', 'edam:format_3004', 'edam:format_3005', 'edam:format_3006', 'edam:format_3007', 'edam:format_3008', 'edam:format_3009', 'edam:format_3010', 'edam:format_3011', 'edam:format_3012', 'edam:format_3013', 'edam:format_3014', 'edam:format_3015', 'edam:format_3016', 'edam:format_3017', 'edam:format_3018', 'edam:format_3019', 'edam:format_3020', 'edam:format_3033', 'edam:format_3097', 'edam:format_3098', 'edam:format_3099', 'edam:format_3100', 'edam:format_3155', 'edam:format_3156', 'edam:format_3157', 'edam:format_3158', 'edam:format_3159', 'edam:format_3160', 'edam:format_3161', 'edam:format_3162', 'edam:format_3163', 'edam:format_3164', 'edam:format_3166', 'edam:format_3167', 'edam:format_3235', 'edam:format_3239', 'edam:format_3240', 'edam:format_3242', 'edam:format_3243', 'edam:format_3244', 'edam:format_3245', 'edam:format_3246', 'edam:format_3247', 'edam:format_3248', 'edam:format_3249', 'edam:format_3250', 'edam:format_3252', 'edam:format_3253', 'edam:format_3254', 'edam:format_3255', 'edam:format_3256', 'edam:format_3257', 'edam:format_3261', 'edam:format_3262', 'edam:format_3281', 'edam:format_3284', 'edam:format_3285', 'edam:format_3286', 'edam:format_3287', 'edam:format_3288', 'edam:format_3309', 'edam:format_3310', 'edam:format_3311', 'edam:format_3312', 'edam:format_3313', 'edam:format_3326', 'edam:format_3327', 'edam:format_3328', 'edam:format_3329', 'edam:format_3330', 'edam:format_3331', 'edam:format_3462', 'edam:format_3464', 'edam:format_3466', 'edam:format_3467', 'edam:format_3468', 'edam:format_3475', 'edam:format_3477', 'edam:format_3484', 'edam:format_3485', 'edam:format_3486', 'edam:format_3487', 'edam:format_3491', 'edam:format_3499', 'edam:format_3506', 'edam:format_3507', 'edam:format_3508', 'edam:format_3547', 'edam:format_3548', 'edam:format_3549', 'edam:format_3550', 'edam:format_3551', 'edam:format_3554', 'edam:format_3555', 'edam:format_3556', 'edam:format_3578', 'edam:format_3579', 'edam:format_3580', 'edam:format_3581', 'edam:format_3582', 'edam:format_3583', 'edam:format_3584', 'edam:format_3585', 'edam:format_3586', 'edam:format_3587', 'edam:format_3588', 'edam:format_3589', 'edam:format_3590', 'edam:format_3591', 'edam:format_3592', 'edam:format_3593', 'edam:format_3594', 'edam:format_3595', 'edam:format_3596', 'edam:format_3597', 'edam:format_3598', 'edam:format_3599', 'edam:format_3600', 'edam:format_3601', 'edam:format_3602', 'edam:format_3603', 'edam:format_3604', 'edam:format_3605', 'edam:format_3606', 'edam:format_3607', 'edam:format_3608', 'edam:format_3609', 'edam:format_3610', 'edam:format_3611', 'edam:format_3612', 'edam:format_3613', 'edam:format_3614', 'edam:format_3615', 'edam:format_3616', 'edam:format_3617', 'edam:format_3618', 'edam:format_3619', 'edam:format_3620', 'edam:format_3621', 'edam:format_3622', 'edam:format_3624', 'edam:format_3626', 'edam:format_3650', 'edam:format_3651', 'edam:format_3652', 'edam:format_3653', 'edam:format_3654', 'edam:format_3655', 'edam:format_3657', 'edam:format_3665', 'edam:format_3681', 'edam:format_3682', 'edam:format_3683', 'edam:format_3684', 'edam:format_3685', 'edam:format_3686', 'edam:format_3687', 'edam:format_3688', 'edam:format_3689', 'edam:format_3690', 'edam:format_3691', 'edam:format_3692', 'edam:format_3693', 'edam:format_3696', 'edam:format_3698', 'edam:format_3699', 'edam:format_3701', 'edam:format_3702', 'edam:format_3706', 'edam:format_3708', 'edam:format_3709', 'edam:format_3710', 'edam:format_3711', 'edam:format_3712', 'edam:format_3713', 'edam:format_3714', 'edam:format_3725', 'edam:format_3726', 'edam:format_3727', 'edam:format_3728', 'edam:format_3729', 'edam:format_3746', 'edam:format_3747', 'edam:format_3748', 'edam:format_3749', 'edam:format_3750', 'edam:format_3751', 'edam:format_3752', 'edam:format_3758', 'edam:format_3764', 'edam:format_3765', 'edam:format_3770', 'edam:format_3771', 'edam:format_3772', 'edam:format_3773', 'edam:format_3774', 'edam:format_3775', 'edam:format_3776', 'edam:format_3777', 'edam:format_3780', 'edam:format_3781', 'edam:format_3782', 'edam:format_3783', 'edam:format_3784', 'edam:format_3785', 'edam:format_3787', 'edam:format_3788', 'edam:format_3789', 'edam:format_3790', 'edam:format_3804', 'edam:format_3811', 'edam:format_3812', 'edam:format_3813', 'edam:format_3814', 'edam:format_3815', 'edam:format_3816', 'edam:format_3817', 'edam:format_3818', 'edam:format_3819', 'edam:format_3820', 'edam:format_3821', 'edam:format_3822', 'edam:format_3823', 'edam:format_3824', 'edam:format_3825', 'edam:format_3826', 'edam:format_3827', 'edam:format_3828', 'edam:format_3829', 'edam:format_3830', 'edam:format_3832', 'edam:format_3833', 'edam:format_3834', 'edam:format_3835', 'edam:format_3836', 'edam:format_3838', 'edam:format_3839', 'edam:format_3841', 'edam:format_3843', 'edam:format_3844', 'edam:format_3845', 'edam:format_3846', 'edam:format_3847', 'edam:format_3848', 'edam:format_3849', 'edam:format_3850', 'edam:format_3851', 'edam:format_3852', 'edam:format_3853', 'edam:format_3854', 'edam:format_3857', 'edam:format_3858', 'edam:format_3859', 'edam:format_3862', 'edam:format_3863', 'edam:format_3864', 'edam:format_3865', 'edam:format_3866', 'edam:format_3867', 'edam:format_3868', 'edam:format_3873', 'edam:format_3874', 'edam:format_3875', 'edam:format_3876', 'edam:format_3877', 'edam:format_3878', 'edam:format_3879', 'edam:format_3880', 'edam:format_3881', 'edam:format_3882', 'edam:format_3883', 'edam:format_3884', 'edam:format_3885', 'edam:format_3886', 'edam:format_3887', 'edam:format_3888', 'edam:format_3889', 'edam:format_3906', 'edam:format_3909', 'edam:format_3910', 'edam:format_3911', 'edam:format_3913', 'edam:format_3915', 'edam:format_3916', 'edam:format_3951', 'edam:format_3956', 'edam:format_3969', 'edam:format_3970', 'edam:format_3971', 'edam:format_3972', 'edam:format_3973', 'edam:format_3975', 'edam:format_3976', 'edam:format_3977', 'edam:format_3978', 'edam:format_3979', 'edam:format_3980', 'edam:format_3981', 'edam:format_3982', 'edam:format_3983', 'edam:format_3984', 'edam:format_3985', 'edam:format_3986', 'edam:format_3987', 'edam:format_3988', 'edam:format_3989', 'edam:format_3990', 'edam:format_3991', 'edam:format_3992', 'edam:format_3993', 'edam:format_3994', 'edam:format_3995', 'edam:format_3996', 'edam:format_3997', 'edam:format_3998', 'edam:format_3999', 'edam:format_4000', 'edam:format_4002', 'edam:format_4003', 'edam:format_4004', 'edam:format_4005', 'edam:format_4006', 'edam:format_4007', 'edam:format_4015', 'edam:format_4018', 'edam:format_4023', 'edam:format_4024', 'edam:format_4025', 'edam:format_4026', 'edam:format_4035', 'edam:format_4036', 'edam:format_4039', 'edam:format_4041', 'edam:format_4048', 'edam:format_4049', 'edam:format_4050', 'edam:format_4058', 'edam:format_4059', 'edam:format_4066', 'edam:format_4067', 'edam:format_4068', 'edam:format_4069', 'edam:format_4070', 'edam:format_4071', 'edam:format_4072', 'edam:format_4073', name='EnumEDAMFormats'))
    file_extension = Column(Text(), nullable=False )
    data_category = Column(Text())
    data_type = Column(Enum('edam:data_0582', 'edam:data_0842', 'edam:data_0844', 'edam:data_0845', 'edam:data_0846', 'edam:data_0847', 'edam:data_0849', 'edam:data_0850', 'edam:data_0856', 'edam:data_0857', 'edam:data_0858', 'edam:data_0860', 'edam:data_0862', 'edam:data_0863', 'edam:data_0865', 'edam:data_0867', 'edam:data_0870', 'edam:data_0871', 'edam:data_0872', 'edam:data_0874', 'edam:data_0878', 'edam:data_0880', 'edam:data_0881', 'edam:data_0883', 'edam:data_0886', 'edam:data_0887', 'edam:data_0888', 'edam:data_0889', 'edam:data_0890', 'edam:data_0892', 'edam:data_0893', 'edam:data_0896', 'edam:data_0897', 'edam:data_0905', 'edam:data_0906', 'edam:data_0907', 'edam:data_0909', 'edam:data_0910', 'edam:data_0912', 'edam:data_0914', 'edam:data_0916', 'edam:data_0919', 'edam:data_0920', 'edam:data_0924', 'edam:data_0925', 'edam:data_0926', 'edam:data_0927', 'edam:data_0928', 'edam:data_0937', 'edam:data_0938', 'edam:data_0939', 'edam:data_0940', 'edam:data_0942', 'edam:data_0943', 'edam:data_0944', 'edam:data_0945', 'edam:data_0949', 'edam:data_0950', 'edam:data_0951', 'edam:data_0954', 'edam:data_0955', 'edam:data_0956', 'edam:data_0957', 'edam:data_0958', 'edam:data_0960', 'edam:data_0962', 'edam:data_0963', 'edam:data_0966', 'edam:data_0967', 'edam:data_0968', 'edam:data_0970', 'edam:data_0971', 'edam:data_0972', 'edam:data_0976', 'edam:data_0977', 'edam:data_0982', 'edam:data_0983', 'edam:data_0984', 'edam:data_0987', 'edam:data_0988', 'edam:data_0989', 'edam:data_0990', 'edam:data_0991', 'edam:data_0993', 'edam:data_0994', 'edam:data_0995', 'edam:data_0996', 'edam:data_0997', 'edam:data_0998', 'edam:data_0999', 'edam:data_1000', 'edam:data_1001', 'edam:data_1002', 'edam:data_1003', 'edam:data_1004', 'edam:data_1005', 'edam:data_1006', 'edam:data_1007', 'edam:data_1008', 'edam:data_1009', 'edam:data_1010', 'edam:data_1011', 'edam:data_1012', 'edam:data_1013', 'edam:data_1015', 'edam:data_1016', 'edam:data_1017', 'edam:data_1020', 'edam:data_1021', 'edam:data_1022', 'edam:data_1023', 'edam:data_1025', 'edam:data_1026', 'edam:data_1027', 'edam:data_1031', 'edam:data_1032', 'edam:data_1033', 'edam:data_1034', 'edam:data_1035', 'edam:data_1036', 'edam:data_1037', 'edam:data_1038', 'edam:data_1039', 'edam:data_1040', 'edam:data_1041', 'edam:data_1042', 'edam:data_1043', 'edam:data_1044', 'edam:data_1045', 'edam:data_1046', 'edam:data_1047', 'edam:data_1048', 'edam:data_1049', 'edam:data_1050', 'edam:data_1051', 'edam:data_1052', 'edam:data_1053', 'edam:data_1055', 'edam:data_1056', 'edam:data_1058', 'edam:data_1059', 'edam:data_1060', 'edam:data_1061', 'edam:data_1063', 'edam:data_1064', 'edam:data_1066', 'edam:data_1068', 'edam:data_1069', 'edam:data_1070', 'edam:data_1071', 'edam:data_1072', 'edam:data_1073', 'edam:data_1074', 'edam:data_1075', 'edam:data_1076', 'edam:data_1077', 'edam:data_1078', 'edam:data_1079', 'edam:data_1080', 'edam:data_1081', 'edam:data_1082', 'edam:data_1083', 'edam:data_1084', 'edam:data_1085', 'edam:data_1086', 'edam:data_1087', 'edam:data_1088', 'edam:data_1089', 'edam:data_1091', 'edam:data_1092', 'edam:data_1093', 'edam:data_1095', 'edam:data_1096', 'edam:data_1097', 'edam:data_1098', 'edam:data_1100', 'edam:data_1102', 'edam:data_1103', 'edam:data_1104', 'edam:data_1105', 'edam:data_1106', 'edam:data_1112', 'edam:data_1113', 'edam:data_1114', 'edam:data_1115', 'edam:data_1116', 'edam:data_1117', 'edam:data_1118', 'edam:data_1119', 'edam:data_1123', 'edam:data_1124', 'edam:data_1126', 'edam:data_1127', 'edam:data_1128', 'edam:data_1129', 'edam:data_1130', 'edam:data_1131', 'edam:data_1132', 'edam:data_1133', 'edam:data_1134', 'edam:data_1135', 'edam:data_1136', 'edam:data_1137', 'edam:data_1138', 'edam:data_1139', 'edam:data_1140', 'edam:data_1141', 'edam:data_1142', 'edam:data_1143', 'edam:data_1144', 'edam:data_1145', 'edam:data_1146', 'edam:data_1147', 'edam:data_1148', 'edam:data_1149', 'edam:data_1150', 'edam:data_1151', 'edam:data_1153', 'edam:data_1154', 'edam:data_1155', 'edam:data_1157', 'edam:data_1158', 'edam:data_1159', 'edam:data_1160', 'edam:data_1161', 'edam:data_1162', 'edam:data_1163', 'edam:data_1164', 'edam:data_1165', 'edam:data_1166', 'edam:data_1167', 'edam:data_1170', 'edam:data_1171', 'edam:data_1172', 'edam:data_1173', 'edam:data_1174', 'edam:data_1175', 'edam:data_1176', 'edam:data_1177', 'edam:data_1178', 'edam:data_1179', 'edam:data_1180', 'edam:data_1181', 'edam:data_1182', 'edam:data_1183', 'edam:data_1184', 'edam:data_1185', 'edam:data_1186', 'edam:data_1187', 'edam:data_1188', 'edam:data_1189', 'edam:data_1190', 'edam:data_1191', 'edam:data_1192', 'edam:data_1193', 'edam:data_1194', 'edam:data_1195', 'edam:data_1201', 'edam:data_1202', 'edam:data_1203', 'edam:data_1204', 'edam:data_1205', 'edam:data_1233', 'edam:data_1234', 'edam:data_1235', 'edam:data_1238', 'edam:data_1239', 'edam:data_1240', 'edam:data_1245', 'edam:data_1246', 'edam:data_1249', 'edam:data_1254', 'edam:data_1255', 'edam:data_1259', 'edam:data_1260', 'edam:data_1261', 'edam:data_1262', 'edam:data_1263', 'edam:data_1265', 'edam:data_1266', 'edam:data_1267', 'edam:data_1268', 'edam:data_1270', 'edam:data_1274', 'edam:data_1276', 'edam:data_1277', 'edam:data_1278', 'edam:data_1279', 'edam:data_1280', 'edam:data_1283', 'edam:data_1284', 'edam:data_1285', 'edam:data_1286', 'edam:data_1288', 'edam:data_1289', 'edam:data_1347', 'edam:data_1352', 'edam:data_1353', 'edam:data_1354', 'edam:data_1355', 'edam:data_1361', 'edam:data_1362', 'edam:data_1363', 'edam:data_1364', 'edam:data_1365', 'edam:data_1381', 'edam:data_1383', 'edam:data_1384', 'edam:data_1385', 'edam:data_1394', 'edam:data_1397', 'edam:data_1398', 'edam:data_1399', 'edam:data_1401', 'edam:data_1402', 'edam:data_1403', 'edam:data_1410', 'edam:data_1411', 'edam:data_1412', 'edam:data_1413', 'edam:data_1426', 'edam:data_1427', 'edam:data_1428', 'edam:data_1429', 'edam:data_1439', 'edam:data_1442', 'edam:data_1444', 'edam:data_1448', 'edam:data_1449', 'edam:data_1459', 'edam:data_1460', 'edam:data_1461', 'edam:data_1462', 'edam:data_1463', 'edam:data_1464', 'edam:data_1465', 'edam:data_1466', 'edam:data_1467', 'edam:data_1468', 'edam:data_1470', 'edam:data_1479', 'edam:data_1481', 'edam:data_1482', 'edam:data_1493', 'edam:data_1494', 'edam:data_1497', 'edam:data_1498', 'edam:data_1499', 'edam:data_1501', 'edam:data_1502', 'edam:data_1503', 'edam:data_1505', 'edam:data_1506', 'edam:data_1507', 'edam:data_1508', 'edam:data_1519', 'edam:data_1520', 'edam:data_1521', 'edam:data_1522', 'edam:data_1523', 'edam:data_1524', 'edam:data_1525', 'edam:data_1526', 'edam:data_1527', 'edam:data_1528', 'edam:data_1529', 'edam:data_1530', 'edam:data_1531', 'edam:data_1532', 'edam:data_1534', 'edam:data_1537', 'edam:data_1539', 'edam:data_1542', 'edam:data_1544', 'edam:data_1545', 'edam:data_1546', 'edam:data_1547', 'edam:data_1548', 'edam:data_1549', 'edam:data_1566', 'edam:data_1583', 'edam:data_1584', 'edam:data_1585', 'edam:data_1588', 'edam:data_1589', 'edam:data_1590', 'edam:data_1595', 'edam:data_1596', 'edam:data_1597', 'edam:data_1598', 'edam:data_1600', 'edam:data_1602', 'edam:data_1621', 'edam:data_1622', 'edam:data_1636', 'edam:data_1667', 'edam:data_1668', 'edam:data_1669', 'edam:data_1689', 'edam:data_1690', 'edam:data_1691', 'edam:data_1692', 'edam:data_1696', 'edam:data_1707', 'edam:data_1708', 'edam:data_1709', 'edam:data_1710', 'edam:data_1711', 'edam:data_1712', 'edam:data_1713', 'edam:data_1714', 'edam:data_1731', 'edam:data_1742', 'edam:data_1743', 'edam:data_1748', 'edam:data_1755', 'edam:data_1756', 'edam:data_1757', 'edam:data_1758', 'edam:data_1759', 'edam:data_1771', 'edam:data_1772', 'edam:data_1794', 'edam:data_1795', 'edam:data_1796', 'edam:data_1802', 'edam:data_1803', 'edam:data_1804', 'edam:data_1805', 'edam:data_1807', 'edam:data_1855', 'edam:data_1856', 'edam:data_1857', 'edam:data_1858', 'edam:data_1859', 'edam:data_1860', 'edam:data_1863', 'edam:data_1867', 'edam:data_1868', 'edam:data_1869', 'edam:data_1870', 'edam:data_1872', 'edam:data_1873', 'edam:data_1874', 'edam:data_1875', 'edam:data_1881', 'edam:data_1882', 'edam:data_1883', 'edam:data_1885', 'edam:data_1886', 'edam:data_1891', 'edam:data_1893', 'edam:data_1895', 'edam:data_1896', 'edam:data_1897', 'edam:data_1898', 'edam:data_1899', 'edam:data_1900', 'edam:data_1901', 'edam:data_1902', 'edam:data_1903', 'edam:data_1904', 'edam:data_1905', 'edam:data_1907', 'edam:data_1908', 'edam:data_1916', 'edam:data_1917', 'edam:data_2007', 'edam:data_2012', 'edam:data_2016', 'edam:data_2019', 'edam:data_2024', 'edam:data_2025', 'edam:data_2026', 'edam:data_2042', 'edam:data_2044', 'edam:data_2048', 'edam:data_2050', 'edam:data_2070', 'edam:data_2071', 'edam:data_2080', 'edam:data_2082', 'edam:data_2084', 'edam:data_2085', 'edam:data_2087', 'edam:data_2088', 'edam:data_2091', 'edam:data_2093', 'edam:data_2098', 'edam:data_2099', 'edam:data_2101', 'edam:data_2102', 'edam:data_2104', 'edam:data_2105', 'edam:data_2106', 'edam:data_2107', 'edam:data_2108', 'edam:data_2109', 'edam:data_2110', 'edam:data_2111', 'edam:data_2112', 'edam:data_2113', 'edam:data_2114', 'edam:data_2117', 'edam:data_2118', 'edam:data_2119', 'edam:data_2127', 'edam:data_2128', 'edam:data_2129', 'edam:data_2131', 'edam:data_2133', 'edam:data_2137', 'edam:data_2139', 'edam:data_2140', 'edam:data_2154', 'edam:data_2160', 'edam:data_2161', 'edam:data_2162', 'edam:data_2163', 'edam:data_2165', 'edam:data_2166', 'edam:data_2167', 'edam:data_2168', 'edam:data_2174', 'edam:data_2190', 'edam:data_2193', 'edam:data_2208', 'edam:data_2209', 'edam:data_2216', 'edam:data_2219', 'edam:data_2220', 'edam:data_2223', 'edam:data_2253', 'edam:data_2254', 'edam:data_2285', 'edam:data_2290', 'edam:data_2291', 'edam:data_2292', 'edam:data_2293', 'edam:data_2294', 'edam:data_2295', 'edam:data_2297', 'edam:data_2298', 'edam:data_2299', 'edam:data_2301', 'edam:data_2302', 'edam:data_2309', 'edam:data_2313', 'edam:data_2314', 'edam:data_2315', 'edam:data_2316', 'edam:data_2317', 'edam:data_2318', 'edam:data_2319', 'edam:data_2320', 'edam:data_2321', 'edam:data_2325', 'edam:data_2326', 'edam:data_2327', 'edam:data_2335', 'edam:data_2337', 'edam:data_2338', 'edam:data_2339', 'edam:data_2340', 'edam:data_2342', 'edam:data_2343', 'edam:data_2344', 'edam:data_2345', 'edam:data_2346', 'edam:data_2347', 'edam:data_2348', 'edam:data_2349', 'edam:data_2353', 'edam:data_2354', 'edam:data_2355', 'edam:data_2356', 'edam:data_2362', 'edam:data_2365', 'edam:data_2366', 'edam:data_2367', 'edam:data_2368', 'edam:data_2369', 'edam:data_2370', 'edam:data_2371', 'edam:data_2373', 'edam:data_2374', 'edam:data_2375', 'edam:data_2379', 'edam:data_2380', 'edam:data_2382', 'edam:data_2383', 'edam:data_2384', 'edam:data_2385', 'edam:data_2386', 'edam:data_2387', 'edam:data_2388', 'edam:data_2389', 'edam:data_2390', 'edam:data_2391', 'edam:data_2392', 'edam:data_2393', 'edam:data_2398', 'edam:data_2523', 'edam:data_2526', 'edam:data_2530', 'edam:data_2531', 'edam:data_2534', 'edam:data_2535', 'edam:data_2536', 'edam:data_2537', 'edam:data_2538', 'edam:data_2563', 'edam:data_2564', 'edam:data_2565', 'edam:data_2576', 'edam:data_2578', 'edam:data_2580', 'edam:data_2582', 'edam:data_2583', 'edam:data_2586', 'edam:data_2587', 'edam:data_2588', 'edam:data_2589', 'edam:data_2591', 'edam:data_2593', 'edam:data_2594', 'edam:data_2595', 'edam:data_2596', 'edam:data_2597', 'edam:data_2600', 'edam:data_2603', 'edam:data_2605', 'edam:data_2606', 'edam:data_2608', 'edam:data_2609', 'edam:data_2610', 'edam:data_2611', 'edam:data_2612', 'edam:data_2613', 'edam:data_2614', 'edam:data_2615', 'edam:data_2616', 'edam:data_2617', 'edam:data_2618', 'edam:data_2619', 'edam:data_2620', 'edam:data_2621', 'edam:data_2622', 'edam:data_2625', 'edam:data_2626', 'edam:data_2628', 'edam:data_2629', 'edam:data_2630', 'edam:data_2631', 'edam:data_2632', 'edam:data_2633', 'edam:data_2634', 'edam:data_2635', 'edam:data_2636', 'edam:data_2637', 'edam:data_2638', 'edam:data_2639', 'edam:data_2641', 'edam:data_2642', 'edam:data_2643', 'edam:data_2644', 'edam:data_2645', 'edam:data_2646', 'edam:data_2647', 'edam:data_2648', 'edam:data_2649', 'edam:data_2650', 'edam:data_2651', 'edam:data_2652', 'edam:data_2653', 'edam:data_2654', 'edam:data_2655', 'edam:data_2656', 'edam:data_2657', 'edam:data_2658', 'edam:data_2659', 'edam:data_2660', 'edam:data_2662', 'edam:data_2663', 'edam:data_2664', 'edam:data_2665', 'edam:data_2666', 'edam:data_2667', 'edam:data_2668', 'edam:data_2669', 'edam:data_2670', 'edam:data_2700', 'edam:data_2701', 'edam:data_2702', 'edam:data_2704', 'edam:data_2705', 'edam:data_2706', 'edam:data_2709', 'edam:data_2710', 'edam:data_2711', 'edam:data_2713', 'edam:data_2714', 'edam:data_2715', 'edam:data_2716', 'edam:data_2717', 'edam:data_2718', 'edam:data_2719', 'edam:data_2720', 'edam:data_2721', 'edam:data_2723', 'edam:data_2725', 'edam:data_2727', 'edam:data_2728', 'edam:data_2729', 'edam:data_2730', 'edam:data_2731', 'edam:data_2732', 'edam:data_2736', 'edam:data_2737', 'edam:data_2738', 'edam:data_2739', 'edam:data_2741', 'edam:data_2742', 'edam:data_2744', 'edam:data_2745', 'edam:data_2746', 'edam:data_2749', 'edam:data_2752', 'edam:data_2753', 'edam:data_2755', 'edam:data_2756', 'edam:data_2757', 'edam:data_2758', 'edam:data_2759', 'edam:data_2761', 'edam:data_2762', 'edam:data_2764', 'edam:data_2766', 'edam:data_2769', 'edam:data_2770', 'edam:data_2771', 'edam:data_2772', 'edam:data_2773', 'edam:data_2774', 'edam:data_2775', 'edam:data_2776', 'edam:data_2777', 'edam:data_2778', 'edam:data_2779', 'edam:data_2780', 'edam:data_2781', 'edam:data_2782', 'edam:data_2783', 'edam:data_2784', 'edam:data_2785', 'edam:data_2786', 'edam:data_2787', 'edam:data_2789', 'edam:data_2790', 'edam:data_2791', 'edam:data_2792', 'edam:data_2793', 'edam:data_2794', 'edam:data_2795', 'edam:data_2796', 'edam:data_2797', 'edam:data_2798', 'edam:data_2799', 'edam:data_2800', 'edam:data_2802', 'edam:data_2803', 'edam:data_2804', 'edam:data_2805', 'edam:data_2812', 'edam:data_2835', 'edam:data_2836', 'edam:data_2837', 'edam:data_2849', 'edam:data_2850', 'edam:data_2851', 'edam:data_2852', 'edam:data_2854', 'edam:data_2855', 'edam:data_2856', 'edam:data_2858', 'edam:data_2865', 'edam:data_2870', 'edam:data_2872', 'edam:data_2873', 'edam:data_2877', 'edam:data_2878', 'edam:data_2879', 'edam:data_2884', 'edam:data_2886', 'edam:data_2887', 'edam:data_2891', 'edam:data_2892', 'edam:data_2893', 'edam:data_2894', 'edam:data_2895', 'edam:data_2896', 'edam:data_2897', 'edam:data_2898', 'edam:data_2899', 'edam:data_2900', 'edam:data_2901', 'edam:data_2902', 'edam:data_2903', 'edam:data_2904', 'edam:data_2905', 'edam:data_2906', 'edam:data_2907', 'edam:data_2908', 'edam:data_2909', 'edam:data_2910', 'edam:data_2911', 'edam:data_2912', 'edam:data_2914', 'edam:data_2915', 'edam:data_2916', 'edam:data_2917', 'edam:data_2955', 'edam:data_2956', 'edam:data_2957', 'edam:data_2968', 'edam:data_2969', 'edam:data_2970', 'edam:data_2976', 'edam:data_2977', 'edam:data_2978', 'edam:data_2979', 'edam:data_2984', 'edam:data_2985', 'edam:data_2991', 'edam:data_2992', 'edam:data_2994', 'edam:data_3002', 'edam:data_3021', 'edam:data_3022', 'edam:data_3025', 'edam:data_3028', 'edam:data_3029', 'edam:data_3034', 'edam:data_3035', 'edam:data_3036', 'edam:data_3103', 'edam:data_3104', 'edam:data_3106', 'edam:data_3108', 'edam:data_3110', 'edam:data_3111', 'edam:data_3112', 'edam:data_3113', 'edam:data_3115', 'edam:data_3117', 'edam:data_3128', 'edam:data_3134', 'edam:data_3148', 'edam:data_3153', 'edam:data_3181', 'edam:data_3210', 'edam:data_3236', 'edam:data_3238', 'edam:data_3241', 'edam:data_3264', 'edam:data_3265', 'edam:data_3266', 'edam:data_3270', 'edam:data_3271', 'edam:data_3272', 'edam:data_3273', 'edam:data_3274', 'edam:data_3275', 'edam:data_3354', 'edam:data_3355', 'edam:data_3358', 'edam:data_3424', 'edam:data_3425', 'edam:data_3442', 'edam:data_3449', 'edam:data_3451', 'edam:data_3479', 'edam:data_3483', 'edam:data_3488', 'edam:data_3492', 'edam:data_3494', 'edam:data_3495', 'edam:data_3498', 'edam:data_3505', 'edam:data_3509', 'edam:data_3546', 'edam:data_3558', 'edam:data_3567', 'edam:data_3568', 'edam:data_3667', 'edam:data_3668', 'edam:data_3669', 'edam:data_3670', 'edam:data_3671', 'edam:data_3707', 'edam:data_3716', 'edam:data_3717', 'edam:data_3718', 'edam:data_3719', 'edam:data_3720', 'edam:data_3721', 'edam:data_3722', 'edam:data_3723', 'edam:data_3724', 'edam:data_3732', 'edam:data_3733', 'edam:data_3734', 'edam:data_3735', 'edam:data_3736', 'edam:data_3737', 'edam:data_3738', 'edam:data_3739', 'edam:data_3743', 'edam:data_3753', 'edam:data_3754', 'edam:data_3756', 'edam:data_3757', 'edam:data_3759', 'edam:data_3768', 'edam:data_3769', 'edam:data_3779', 'edam:data_3786', 'edam:data_3805', 'edam:data_3806', 'edam:data_3807', 'edam:data_3808', 'edam:data_3842', 'edam:data_3856', 'edam:data_3861', 'edam:data_3869', 'edam:data_3870', 'edam:data_3871', 'edam:data_3872', 'edam:data_3905', 'edam:data_3914', 'edam:data_3917', 'edam:data_3924', 'edam:data_3932', 'edam:data_3949', 'edam:data_3952', 'edam:data_3953', 'edam:data_4022', 'edam:data_4040', 'edam:data_4075', name='EnumEDAMDataTypes'))
    size = Column(Integer())
    internal_uri = Column(Text())
    release_uri = Column(Text())
    drs_uri = Column(Text())
    storage_class = Column(Text())
    availability = Column(Enum('snomedct:103328004', 'snomedct:103329007', name='EnumAvailabilityStatus'))
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
    hash_type = Column(Enum('MS:1000568', 'CAMO:0000022', 'MS:1000569', 'MS:1003151', name='EnumFileHashType'))
    hash_value = Column(Text())
    

    def __repr__(self):
        return f"FileHash(id={self.id},hash_type={self.hash_type},hash_value={self.hash_value},)"



    


class Assay(Base):
    """
    A specific assay that was performed on given subject(s) or sample(s).
    """
    __tablename__ = 'Assay'

    assay_id = Column(Text(), primary_key=True, nullable=False )
    assay_type = Column(Enum('OBI:0000070', 'CHMO:0000087', 'CHMO:0000089', 'CHMO:0000102', 'CHMO:0000701', 'OBI:0000117', 'OBI:0000182', 'OBI:0000185', 'OBI:0000201', 'OBI:0000288', 'OBI:0000291', 'OBI:0000366', 'OBI:0000418', 'OBI:0000424', 'OBI:0000433', 'OBI:0000435', 'OBI:0000438', 'OBI:0000443', 'OBI:0000445', 'OBI:0000447', 'OBI:0000454', 'OBI:0000470', 'OBI:0000520', 'OBI:0000537', 'OBI:0000615', 'OBI:0000623', 'OBI:0000626', 'OBI:0000630', 'OBI:0000634', 'OBI:0000661', 'OBI:0000664', 'OBI:0000669', 'OBI:0000693', 'OBI:0000695', 'OBI:0000697', 'OBI:0000699', 'OBI:0000705', 'OBI:0000706', 'OBI:0000716', 'OBI:0000721', 'OBI:0000723', 'OBI:0000724', 'OBI:0000730', 'OBI:0000734', 'OBI:0000743', 'OBI:0000748', 'OBI:0000787', 'OBI:0000802', 'OBI:0000805', 'OBI:0000808', 'OBI:0000812', 'OBI:0000820', 'OBI:0000823', 'OBI:0000854', 'OBI:0000860', 'OBI:0000865', 'OBI:0000870', 'OBI:0000871', 'OBI:0000872', 'OBI:0000874', 'OBI:0000875', 'OBI:0000882', 'OBI:0000883', 'OBI:0000891', 'OBI:0000892', 'OBI:0000893', 'OBI:0000897', 'OBI:0000903', 'OBI:0000904', 'OBI:0000910', 'OBI:0000911', 'OBI:0000912', 'OBI:0000913', 'OBI:0000916', 'OBI:0000920', 'OBI:0000923', 'OBI:0000944', 'OBI:0000957', 'OBI:0000964', 'OBI:0000966', 'OBI:0000975', 'OBI:0000978', 'OBI:0001001', 'OBI:0001005', 'OBI:0001006', 'OBI:0001008', 'OBI:0001011', 'OBI:0001012', 'OBI:0001013', 'OBI:0001014', 'OBI:0001015', 'OBI:0001016', 'OBI:0001017', 'OBI:0001018', 'OBI:0001019', 'OBI:0001020', 'OBI:0001021', 'OBI:0001022', 'OBI:0001023', 'OBI:0001024', 'OBI:0001025', 'OBI:0001026', 'OBI:0001027', 'OBI:0001029', 'OBI:0001030', 'OBI:0001035', 'OBI:0001038', 'OBI:0001039', 'OBI:0001145', 'OBI:0001146', 'OBI:0001158', 'OBI:0001170', 'OBI:0001177', 'OBI:0001178', 'OBI:0001179', 'OBI:0001183', 'OBI:0001184', 'OBI:0001186', 'OBI:0001187', 'OBI:0001188', 'OBI:0001189', 'OBI:0001190', 'OBI:0001194', 'OBI:0001196', 'OBI:0001198', 'OBI:0001203', 'OBI:0001206', 'OBI:0001209', 'OBI:0001210', 'OBI:0001215', 'OBI:0001216', 'OBI:0001217', 'OBI:0001218', 'OBI:0001220', 'OBI:0001221', 'OBI:0001222', 'OBI:0001223', 'OBI:0001227', 'OBI:0001228', 'OBI:0001229', 'OBI:0001230', 'OBI:0001231', 'OBI:0001232', 'OBI:0001233', 'OBI:0001235', 'OBI:0001236', 'OBI:0001237', 'OBI:0001238', 'OBI:0001240', 'OBI:0001241', 'OBI:0001242', 'OBI:0001243', 'OBI:0001244', 'OBI:0001245', 'OBI:0001246', 'OBI:0001247', 'OBI:0001248', 'OBI:0001251', 'OBI:0001253', 'OBI:0001255', 'OBI:0001260', 'OBI:0001261', 'OBI:0001263', 'OBI:0001264', 'OBI:0001266', 'OBI:0001268', 'OBI:0001269', 'OBI:0001270', 'OBI:0001271', 'OBI:0001272', 'OBI:0001273', 'OBI:0001274', 'OBI:0001276', 'OBI:0001277', 'OBI:0001279', 'OBI:0001280', 'OBI:0001281', 'OBI:0001282', 'OBI:0001283', 'OBI:0001284', 'OBI:0001288', 'OBI:0001289', 'OBI:0001291', 'OBI:0001292', 'OBI:0001295', 'OBI:0001296', 'OBI:0001297', 'OBI:0001298', 'OBI:0001299', 'OBI:0001300', 'OBI:0001301', 'OBI:0001302', 'OBI:0001303', 'OBI:0001304', 'OBI:0001308', 'OBI:0001309', 'OBI:0001311', 'OBI:0001315', 'OBI:0001317', 'OBI:0001318', 'OBI:0001319', 'OBI:0001322', 'OBI:0001324', 'OBI:0001325', 'OBI:0001326', 'OBI:0001327', 'OBI:0001330', 'OBI:0001332', 'OBI:0001333', 'OBI:0001335', 'OBI:0001339', 'OBI:0001341', 'OBI:0001342', 'OBI:0001343', 'OBI:0001344', 'OBI:0001345', 'OBI:0001346', 'OBI:0001348', 'OBI:0001349', 'OBI:0001350', 'OBI:0001353', 'OBI:0001354', 'OBI:0001356', 'OBI:0001357', 'OBI:0001359', 'OBI:0001360', 'OBI:0001361', 'OBI:0001363', 'OBI:0001367', 'OBI:0001368', 'OBI:0001370', 'OBI:0001376', 'OBI:0001378', 'OBI:0001379', 'OBI:0001380', 'OBI:0001382', 'OBI:0001383', 'OBI:0001384', 'OBI:0001385', 'OBI:0001388', 'OBI:0001389', 'OBI:0001390', 'OBI:0001391', 'OBI:0001392', 'OBI:0001393', 'OBI:0001395', 'OBI:0001397', 'OBI:0001400', 'OBI:0001402', 'OBI:0001405', 'OBI:0001406', 'OBI:0001407', 'OBI:0001412', 'OBI:0001413', 'OBI:0001414', 'OBI:0001416', 'OBI:0001419', 'OBI:0001423', 'OBI:0001433', 'OBI:0001436', 'OBI:0001437', 'OBI:0001438', 'OBI:0001445', 'OBI:0001449', 'OBI:0001450', 'OBI:0001451', 'OBI:0001452', 'OBI:0001453', 'OBI:0001455', 'OBI:0001456', 'OBI:0001457', 'OBI:0001459', 'OBI:0001461', 'OBI:0001463', 'OBI:0001465', 'OBI:0001466', 'OBI:0001467', 'OBI:0001469', 'OBI:0001473', 'OBI:0001475', 'OBI:0001476', 'OBI:0001478', 'OBI:0001482', 'OBI:0001484', 'OBI:0001488', 'OBI:0001489', 'OBI:0001490', 'OBI:0001491', 'OBI:0001492', 'OBI:0001493', 'OBI:0001495', 'OBI:0001496', 'OBI:0001497', 'OBI:0001499', 'OBI:0001500', 'OBI:0001501', 'OBI:0001507', 'OBI:0001509', 'OBI:0001510', 'OBI:0001512', 'OBI:0001513', 'OBI:0001516', 'OBI:0001517', 'OBI:0001519', 'OBI:0001520', 'OBI:0001521', 'OBI:0001523', 'OBI:0001524', 'OBI:0001531', 'OBI:0001532', 'OBI:0001534', 'OBI:0001537', 'OBI:0001539', 'OBI:0001541', 'OBI:0001542', 'OBI:0001543', 'OBI:0001544', 'OBI:0001545', 'OBI:0001549', 'OBI:0001550', 'OBI:0001552', 'OBI:0001553', 'OBI:0001555', 'OBI:0001556', 'OBI:0001558', 'OBI:0001559', 'OBI:0001561', 'OBI:0001562', 'OBI:0001564', 'OBI:0001565', 'OBI:0001567', 'OBI:0001568', 'OBI:0001569', 'OBI:0001570', 'OBI:0001577', 'OBI:0001578', 'OBI:0001579', 'OBI:0001584', 'OBI:0001585', 'OBI:0001586', 'OBI:0001587', 'OBI:0001589', 'OBI:0001590', 'OBI:0001591', 'OBI:0001592', 'OBI:0001593', 'OBI:0001594', 'OBI:0001595', 'OBI:0001597', 'OBI:0001599', 'OBI:0001600', 'OBI:0001601', 'OBI:0001602', 'OBI:0001604', 'OBI:0001606', 'OBI:0001607', 'OBI:0001608', 'OBI:0001609', 'OBI:0001610', 'OBI:0001613', 'OBI:0001624', 'OBI:0001630', 'OBI:0001631', 'OBI:0001632', 'OBI:0001634', 'OBI:0001635', 'OBI:0001638', 'OBI:0001639', 'OBI:0001640', 'OBI:0001641', 'OBI:0001642', 'OBI:0001643', 'OBI:0001644', 'OBI:0001645', 'OBI:0001646', 'OBI:0001647', 'OBI:0001648', 'OBI:0001649', 'OBI:0001650', 'OBI:0001651', 'OBI:0001652', 'OBI:0001653', 'OBI:0001654', 'OBI:0001655', 'OBI:0001656', 'OBI:0001657', 'OBI:0001658', 'OBI:0001659', 'OBI:0001660', 'OBI:0001661', 'OBI:0001662', 'OBI:0001663', 'OBI:0001664', 'OBI:0001665', 'OBI:0001666', 'OBI:0001667', 'OBI:0001668', 'OBI:0001669', 'OBI:0001670', 'OBI:0001671', 'OBI:0001672', 'OBI:0001673', 'OBI:0001674', 'OBI:0001675', 'OBI:0001676', 'OBI:0001679', 'OBI:0001680', 'OBI:0001681', 'OBI:0001682', 'OBI:0001683', 'OBI:0001684', 'OBI:0001685', 'OBI:0001686', 'OBI:0001689', 'OBI:0001692', 'OBI:0001693', 'OBI:0001694', 'OBI:0001695', 'OBI:0001696', 'OBI:0001697', 'OBI:0001698', 'OBI:0001699', 'OBI:0001700', 'OBI:0001701', 'OBI:0001703', 'OBI:0001704', 'OBI:0001705', 'OBI:0001706', 'OBI:0001708', 'OBI:0001709', 'OBI:0001710', 'OBI:0001711', 'OBI:0001718', 'OBI:0001719', 'OBI:0001721', 'OBI:0001723', 'OBI:0001724', 'OBI:0001726', 'OBI:0001727', 'OBI:0001728', 'OBI:0001729', 'OBI:0001730', 'OBI:0001731', 'OBI:0001732', 'OBI:0001733', 'OBI:0001734', 'OBI:0001735', 'OBI:0001736', 'OBI:0001738', 'OBI:0001739', 'OBI:0001740', 'OBI:0001741', 'OBI:0001742', 'OBI:0001743', 'OBI:0001744', 'OBI:0001745', 'OBI:0001746', 'OBI:0001747', 'OBI:0001748', 'OBI:0001749', 'OBI:0001750', 'OBI:0001751', 'OBI:0001752', 'OBI:0001753', 'OBI:0001754', 'OBI:0001756', 'OBI:0001757', 'OBI:0001758', 'OBI:0001759', 'OBI:0001760', 'OBI:0001761', 'OBI:0001762', 'OBI:0001763', 'OBI:0001764', 'OBI:0001765', 'OBI:0001766', 'OBI:0001767', 'OBI:0001768', 'OBI:0001770', 'OBI:0001771', 'OBI:0001772', 'OBI:0001773', 'OBI:0001774', 'OBI:0001775', 'OBI:0001776', 'OBI:0001777', 'OBI:0001778', 'OBI:0001779', 'OBI:0001780', 'OBI:0001781', 'OBI:0001782', 'OBI:0001783', 'OBI:0001784', 'OBI:0001785', 'OBI:0001786', 'OBI:0001787', 'OBI:0001788', 'OBI:0001789', 'OBI:0001790', 'OBI:0001791', 'OBI:0001792', 'OBI:0001793', 'OBI:0001794', 'OBI:0001795', 'OBI:0001796', 'OBI:0001797', 'OBI:0001798', 'OBI:0001799', 'OBI:0001800', 'OBI:0001801', 'OBI:0001802', 'OBI:0001803', 'OBI:0001804', 'OBI:0001805', 'OBI:0001806', 'OBI:0001807', 'OBI:0001808', 'OBI:0001809', 'OBI:0001810', 'OBI:0001811', 'OBI:0001812', 'OBI:0001813', 'OBI:0001814', 'OBI:0001815', 'OBI:0001817', 'OBI:0001821', 'OBI:0001822', 'OBI:0001824', 'OBI:0001826', 'OBI:0001827', 'OBI:0001828', 'OBI:0001829', 'OBI:0001830', 'OBI:0001831', 'OBI:0001832', 'OBI:0001833', 'OBI:0001835', 'OBI:0001836', 'OBI:0001837', 'OBI:0001838', 'OBI:0001839', 'OBI:0001840', 'OBI:0001841', 'OBI:0001842', 'OBI:0001843', 'OBI:0001844', 'OBI:0001845', 'OBI:0001846', 'OBI:0001848', 'OBI:0001849', 'OBI:0001850', 'OBI:0001853', 'OBI:0001857', 'OBI:0001858', 'OBI:0001859', 'OBI:0001861', 'OBI:0001862', 'OBI:0001863', 'OBI:0001864', 'OBI:0001915', 'OBI:0001918', 'OBI:0001919', 'OBI:0001920', 'OBI:0001921', 'OBI:0001922', 'OBI:0001923', 'OBI:0001924', 'OBI:0001925', 'OBI:0001926', 'OBI:0001954', 'OBI:0001956', 'OBI:0001960', 'OBI:0001976', 'OBI:0001977', 'OBI:0001978', 'OBI:0001979', 'OBI:0001980', 'OBI:0001981', 'OBI:0001982', 'OBI:0001983', 'OBI:0001984', 'OBI:0001985', 'OBI:0001986', 'OBI:0001987', 'OBI:0001988', 'OBI:0001989', 'OBI:0001990', 'OBI:0001991', 'OBI:0001992', 'OBI:0001993', 'OBI:0001994', 'OBI:0001995', 'OBI:0001996', 'OBI:0001997', 'OBI:0001998', 'OBI:0001999', 'OBI:0002014', 'OBI:0002015', 'OBI:0002016', 'OBI:0002017', 'OBI:0002018', 'OBI:0002019', 'OBI:0002020', 'OBI:0002029', 'OBI:0002030', 'OBI:0002031', 'OBI:0002032', 'OBI:0002033', 'OBI:0002034', 'OBI:0002035', 'OBI:0002036', 'OBI:0002037', 'OBI:0002038', 'OBI:0002039', 'OBI:0002040', 'OBI:0002041', 'OBI:0002042', 'OBI:0002043', 'OBI:0002044', 'OBI:0002045', 'OBI:0002050', 'OBI:0002051', 'OBI:0002052', 'OBI:0002053', 'OBI:0002054', 'OBI:0002055', 'OBI:0002056', 'OBI:0002057', 'OBI:0002058', 'OBI:0002059', 'OBI:0002060', 'OBI:0002061', 'OBI:0002062', 'OBI:0002063', 'OBI:0002064', 'OBI:0002065', 'OBI:0002066', 'OBI:0002067', 'OBI:0002068', 'OBI:0002069', 'OBI:0002070', 'OBI:0002071', 'OBI:0002072', 'OBI:0002073', 'OBI:0002074', 'OBI:0002075', 'OBI:0002082', 'OBI:0002083', 'OBI:0002084', 'OBI:0002085', 'OBI:0002086', 'OBI:0002094', 'OBI:0002096', 'OBI:0002097', 'OBI:0002098', 'OBI:0002099', 'OBI:0002100', 'OBI:0002101', 'OBI:0002102', 'OBI:0002103', 'OBI:0002104', 'OBI:0002105', 'OBI:0002106', 'OBI:0002107', 'OBI:0002108', 'OBI:0002111', 'OBI:0002112', 'OBI:0002113', 'OBI:0002114', 'OBI:0002115', 'OBI:0002116', 'OBI:0002117', 'OBI:0002118', 'OBI:0002119', 'OBI:0002120', 'OBI:0002121', 'OBI:0002122', 'OBI:0002132', 'OBI:0002133', 'OBI:0002134', 'OBI:0002140', 'OBI:0002141', 'OBI:0002142', 'OBI:0002143', 'OBI:0002144', 'OBI:0002145', 'OBI:0002146', 'OBI:0002147', 'OBI:0002148', 'OBI:0002149', 'OBI:0002150', 'OBI:0002151', 'OBI:0002152', 'OBI:0002153', 'OBI:0002154', 'OBI:0002155', 'OBI:0002156', 'OBI:0002157', 'OBI:0002158', 'OBI:0002159', 'OBI:0002160', 'OBI:0002161', 'OBI:0002162', 'OBI:0002163', 'OBI:0002164', 'OBI:0002165', 'OBI:0002166', 'OBI:0002167', 'OBI:0002168', 'OBI:0002169', 'OBI:0002170', 'OBI:0002171', 'OBI:0002172', 'OBI:0002173', 'OBI:0002174', 'OBI:0002175', 'OBI:0002176', 'OBI:0002177', 'OBI:0002178', 'OBI:0002179', 'OBI:0002180', 'OBI:0002181', 'OBI:0002182', 'OBI:0002183', 'OBI:0002184', 'OBI:0002185', 'OBI:0002186', 'OBI:0002187', 'OBI:0002188', 'OBI:0002189', 'OBI:0002436', 'OBI:0002437', 'OBI:0002438', 'OBI:0002439', 'OBI:0002440', 'OBI:0002441', 'OBI:0002442', 'OBI:0002443', 'OBI:0002445', 'OBI:0002449', 'OBI:0002450', 'OBI:0002451', 'OBI:0002452', 'OBI:0002457', 'OBI:0002458', 'OBI:0002459', 'OBI:0002485', 'OBI:0002489', 'OBI:0002564', 'OBI:0002571', 'OBI:0002572', 'OBI:0002575', 'OBI:0002597', 'OBI:0002621', 'OBI:0002622', 'OBI:0002623', 'OBI:0002628', 'OBI:0002629', 'OBI:0002631', 'OBI:0002634', 'OBI:0002635', 'OBI:0002636', 'OBI:0002637', 'OBI:0002638', 'OBI:0002639', 'OBI:0002640', 'OBI:0002641', 'OBI:0002642', 'OBI:0002643', 'OBI:0002644', 'OBI:0002645', 'OBI:0002646', 'OBI:0002647', 'OBI:0002649', 'OBI:0002664', 'OBI:0002665', 'OBI:0002666', 'OBI:0002667', 'OBI:0002668', 'OBI:0002669', 'OBI:0002670', 'OBI:0002671', 'OBI:0002672', 'OBI:0002675', 'OBI:0002676', 'OBI:0002677', 'OBI:0002678', 'OBI:0002680', 'OBI:0002692', 'OBI:0002693', 'OBI:0002694', 'OBI:0002695', 'OBI:0002696', 'OBI:0002697', 'OBI:0002698', 'OBI:0002699', 'OBI:0002700', 'OBI:0002701', 'OBI:0002702', 'OBI:0002703', 'OBI:0002704', 'OBI:0002705', 'OBI:0002706', 'OBI:0002707', 'OBI:0002708', 'OBI:0002709', 'OBI:0002710', 'OBI:0002711', 'OBI:0002712', 'OBI:0002713', 'OBI:0002714', 'OBI:0002715', 'OBI:0002716', 'OBI:0002717', 'OBI:0002718', 'OBI:0002719', 'OBI:0002720', 'OBI:0002721', 'OBI:0002722', 'OBI:0002723', 'OBI:0002724', 'OBI:0002725', 'OBI:0002726', 'OBI:0002727', 'OBI:0002728', 'OBI:0002729', 'OBI:0002730', 'OBI:0002731', 'OBI:0002732', 'OBI:0002733', 'OBI:0002734', 'OBI:0002735', 'OBI:0002736', 'OBI:0002737', 'OBI:0002738', 'OBI:0002739', 'OBI:0002740', 'OBI:0002741', 'OBI:0002742', 'OBI:0002753', 'OBI:0002759', 'OBI:0002760', 'OBI:0002761', 'OBI:0002762', 'OBI:0002763', 'OBI:0002764', 'OBI:0002765', 'OBI:0002766', 'OBI:0002767', 'OBI:0002768', 'OBI:0002773', 'OBI:0002946', 'OBI:0002947', 'OBI:0002948', 'OBI:0002949', 'OBI:0002950', 'OBI:0002951', 'OBI:0002952', 'OBI:0002953', 'OBI:0002954', 'OBI:0002955', 'OBI:0002956', 'OBI:0002957', 'OBI:0002958', 'OBI:0002959', 'OBI:0002960', 'OBI:0002961', 'OBI:0002962', 'OBI:0002963', 'OBI:0002964', 'OBI:0002965', 'OBI:0002966', 'OBI:0002967', 'OBI:0002968', 'OBI:0002969', 'OBI:0002970', 'OBI:0002984', 'OBI:0002985', 'OBI:0002986', 'OBI:0002987', 'OBI:0002990', 'OBI:0002991', 'OBI:0003009', 'OBI:0003010', 'OBI:0003011', 'OBI:0003012', 'OBI:0003013', 'OBI:0003014', 'OBI:0003015', 'OBI:0003016', 'OBI:0003017', 'OBI:0003018', 'OBI:0003019', 'OBI:0003021', 'OBI:0003022', 'OBI:0003023', 'OBI:0003024', 'OBI:0003025', 'OBI:0003026', 'OBI:0003027', 'OBI:0003028', 'OBI:0003031', 'OBI:0003032', 'OBI:0003033', 'OBI:0003034', 'OBI:0003035', 'OBI:0003036', 'OBI:0003037', 'OBI:0003038', 'OBI:0003039', 'OBI:0003040', 'OBI:0003041', 'OBI:0003042', 'OBI:0003043', 'OBI:0003044', 'OBI:0003045', 'OBI:0003080', 'OBI:0003087', 'OBI:0003088', 'OBI:0003089', 'OBI:0003090', 'OBI:0003091', 'OBI:0003092', 'OBI:0003093', 'OBI:0003094', 'OBI:0003095', 'OBI:0003096', 'OBI:0003097', 'OBI:0003098', 'OBI:0003099', 'OBI:0003100', 'OBI:0003101', 'OBI:0003102', 'OBI:0003103', 'OBI:0003104', 'OBI:0003105', 'OBI:0003106', 'OBI:0003107', 'OBI:0003108', 'OBI:0003110', 'OBI:0003111', 'OBI:0003112', 'OBI:0003113', 'OBI:0003115', 'OBI:0003116', 'OBI:0003117', 'OBI:0003118', 'OBI:0003122', 'OBI:0003123', 'OBI:0003124', 'OBI:0003125', 'OBI:0003126', 'OBI:0003127', 'OBI:0003128', 'OBI:0003145', 'OBI:0003146', 'OBI:0003147', 'OBI:0003148', 'OBI:0003149', 'OBI:0003150', 'OBI:0003151', 'OBI:0003152', 'OBI:0003153', 'OBI:0003154', 'OBI:0003155', 'OBI:0003156', 'OBI:0003157', 'OBI:0003158', 'OBI:0003159', 'OBI:0003160', 'OBI:0003161', 'OBI:0003162', 'OBI:0003163', 'OBI:0003164', 'OBI:0003165', 'OBI:0003166', 'OBI:0003167', 'OBI:0003168', 'OBI:0003170', 'OBI:0003171', 'OBI:0003172', 'OBI:0003173', 'OBI:0003174', 'OBI:0003175', 'OBI:0003176', 'OBI:0003177', 'OBI:0003180', 'OBI:0003181', 'OBI:0003182', 'OBI:0003183', 'OBI:0003184', 'OBI:0003185', 'OBI:0003186', 'OBI:0003187', 'OBI:0003188', 'OBI:0003189', 'OBI:0003190', 'OBI:0003191', 'OBI:0003192', 'OBI:0003193', 'OBI:0003194', 'OBI:0003195', 'OBI:0003196', 'OBI:0003197', 'OBI:0003202', 'OBI:0003203', 'OBI:0003204', 'OBI:0003205', 'OBI:0003206', 'OBI:0003207', 'OBI:0003208', 'OBI:0003209', 'OBI:0003210', 'OBI:0003211', 'OBI:0003212', 'OBI:0003213', 'OBI:0003214', 'OBI:0003215', 'OBI:0003216', 'OBI:0003217', 'OBI:0003218', 'OBI:0003219', 'OBI:0003220', 'OBI:0003221', 'OBI:0003222', 'OBI:0003223', 'OBI:0003224', 'OBI:0003225', 'OBI:0003226', 'OBI:0003227', 'OBI:0003228', 'OBI:0003229', 'OBI:0003230', 'OBI:0003232', 'OBI:0003233', 'OBI:0003234', 'OBI:0003235', 'OBI:0003236', 'OBI:0003237', 'OBI:0003238', 'OBI:0003239', 'OBI:0003240', 'OBI:0003241', 'OBI:0003242', 'OBI:0003282', 'OBI:0003283', 'OBI:0003284', 'OBI:0003285', 'OBI:0003286', 'OBI:0003287', 'OBI:0003288', 'OBI:0003290', 'OBI:0003292', 'OBI:0003293', 'OBI:0003294', 'OBI:0003296', 'OBI:0003297', 'OBI:0003298', 'OBI:0003299', 'OBI:0003300', 'OBI:0003301', 'OBI:0003302', 'OBI:0003303', 'OBI:0003304', 'OBI:0003305', 'OBI:0003306', 'OBI:0003307', 'OBI:0003309', 'OBI:0003310', 'OBI:0003311', 'OBI:0003312', 'OBI:0003313', 'OBI:0003314', 'OBI:0003315', 'OBI:0003316', 'OBI:0003321', 'OBI:0003323', 'OBI:0003324', 'OBI:0003325', 'OBI:0003326', 'OBI:0003368', 'OBI:0003372', 'OBI:0003373', 'OBI:0003375', 'OBI:0003376', 'OBI:0003377', 'OBI:0003378', 'OBI:0003379', 'OBI:0003381', 'OBI:0003412', 'OBI:0003418', 'OBI:0003419', 'OBI:0003422', 'OBI:0003423', 'OBI:0003424', 'OBI:0003425', 'OBI:0003426', 'OBI:0003427', 'OBI:0003428', 'OBI:0003429', 'OBI:0003430', 'OBI:0003431', 'OBI:0003432', 'OBI:0003433', 'OBI:0003434', 'OBI:0003435', 'OBI:0003436', 'OBI:0003437', 'OBI:0003438', 'OBI:0003457', 'OBI:0003458', 'OBI:0003459', 'OBI:0003460', 'OBI:0003461', 'OBI:0003462', 'OBI:0003463', 'OBI:0003464', 'OBI:0003465', 'OBI:0003466', 'OBI:0003467', 'OBI:0003468', 'OBI:0003469', 'OBI:0003470', 'OBI:0003471', 'OBI:0003472', 'OBI:0003473', 'OBI:0003474', 'OBI:0003475', 'OBI:0003476', 'OBI:0003477', 'OBI:0003478', 'OBI:0003479', 'OBI:0003480', 'OBI:0003484', 'OBI:0003485', 'OBI:0003486', 'OBI:0003487', 'OBI:0003488', 'OBI:0003498', 'OBI:0003501', 'OBI:0003502', 'OBI:0003503', 'OBI:0003504', 'OBI:0003505', 'OBI:0003506', 'OBI:0003507', 'OBI:0003508', 'OBI:0003509', 'OBI:0003510', 'OBI:0003511', 'OBI:0003512', 'OBI:0003513', 'OBI:0003514', 'OBI:0003515', 'OBI:0003516', 'OBI:0003517', 'OBI:0003518', 'OBI:0003519', 'OBI:0003520', 'OBI:0003521', 'OBI:0003522', 'OBI:0003523', 'OBI:0003524', 'OBI:0003525', 'OBI:0003526', 'OBI:0003527', 'OBI:0003528', 'OBI:0003529', 'OBI:0003530', 'OBI:0003531', 'OBI:0003532', 'OBI:0003533', 'OBI:0003534', 'OBI:0003535', 'OBI:0003536', 'OBI:0003537', 'OBI:0003538', 'OBI:0003539', 'OBI:0003540', 'OBI:0003541', 'OBI:0003542', 'OBI:0003543', 'OBI:0003544', 'OBI:0003545', 'OBI:0003546', 'OBI:0003552', 'OBI:0003576', 'OBI:0003578', 'OBI:0003580', 'OBI:0003582', 'OBI:0003583', 'OBI:0003584', 'OBI:0003587', 'OBI:0003589', 'OBI:0003590', 'OBI:0003598', 'OBI:0003599', 'OBI:0003601', 'OBI:0003602', 'OBI:0003604', 'OBI:0003605', 'OBI:0003612', 'OBI:0003613', 'OBI:0003659', 'OBI:0003660', 'OBI:0003661', 'OBI:0003662', 'OBI:0003686', 'OBI:0003687', 'OBI:0003709', 'OBI:0003710', 'OBI:0003711', 'OBI:0003712', 'OBI:0003713', 'OBI:0003714', 'OBI:0003715', 'OBI:0003716', 'OBI:0003717', 'OBI:0003718', 'OBI:0003719', 'OBI:0003720', 'OBI:0003721', 'OBI:0003722', 'OBI:0003723', 'OBI:0003724', 'OBI:0003725', 'OBI:0003734', 'OBI:0003735', 'OBI:0003736', 'OBI:0003738', 'OBI:0003741', 'OBI:0003750', 'OBI:0003751', 'OBI:0003752', 'OBI:0003753', 'OBI:0003754', 'OBI:0003755', 'OBI:0003756', 'OBI:0003757', 'OBI:0003758', 'OBI:0003759', 'OBI:0003760', 'OBI:0003761', 'OBI:0003762', 'OBI:0003763', 'OBI:0003764', 'OBI:0003765', 'OBI:0003766', 'OBI:0003767', 'OBI:0003768', 'OBI:0003769', 'OBI:0003770', 'OBI:0003771', 'OBI:0003772', 'OBI:0003773', 'OBI:0003774', 'OBI:0003775', 'OBI:0003776', 'OBI:0003777', 'OBI:0003778', 'OBI:0003779', 'OBI:0003780', 'OBI:0003781', 'OBI:0003782', 'OBI:0003788', 'OBI:0003789', 'OBI:0003790', 'OBI:0003791', 'OBI:0003792', 'OBI:0003793', 'OBI:0003794', 'OBI:0003795', 'OBI:0003796', 'OBI:0003797', 'OBI:0003798', 'OBI:0003799', 'OBI:0003801', 'OBI:0003802', 'OBI:0003803', 'OBI:0003804', 'OBI:0003805', 'OBI:0003811', 'OBI:0003812', 'OBI:0003813', 'OBI:0003814', 'OBI:0003815', 'OBI:0003816', 'OBI:0003817', 'OBI:0003818', 'OBI:0003819', 'OBI:0003820', 'OBI:0003821', 'OBI:0003822', 'OBI:0003823', 'OBI:0003824', 'OBI:0003825', 'OBI:0003826', 'OBI:0003827', 'OBI:0003828', 'OBI:0003829', 'OBI:0003830', 'OBI:0003831', 'OBI:0003832', 'OBI:0003833', 'OBI:0003834', 'OBI:0003835', 'OBI:0003836', 'OBI:0003837', 'OBI:0003838', 'OBI:0003839', 'OBI:0003840', 'OBI:0003841', 'OBI:0003842', 'OBI:0003843', 'OBI:0003844', 'OBI:0003850', 'OBI:0003851', 'OBI:0003852', 'OBI:0003853', 'OBI:0003882', 'OBI:0003885', 'OBI:0003886', 'OBI:0003887', 'OBI:0003888', 'OBI:0003889', 'OBI:0003890', 'OBI:0003891', 'OBI:0003892', 'OBI:0003893', 'OBI:0003894', 'OBI:0003895', 'OBI:0003896', 'OBI:0003897', 'OBI:0003898', 'OBI:0003899', 'OBI:0003900', 'OBI:0003901', 'OBI:0003902', 'OBI:0003903', 'OBI:0003904', 'OBI:0003905', 'OBI:0003906', 'OBI:0003907', 'OBI:0003908', 'OBI:0003909', 'OBI:0003910', 'OBI:0003911', 'OBI:0003912', 'OBI:0003913', 'OBI:0003914', 'OBI:0003915', 'OBI:0302736', 'OBI:0302737', 'OBI:0600002', 'OBI:0600017', 'OBI:0600020', 'OBI:0600025', 'OBI:0600026', 'OBI:0600031', 'OBI:0600045', 'OBI:0600047', 'OBI:1110013', 'OBI:1110037', 'OBI:1110059', 'OBI:1110124', 'OBI:1110125', 'OBI:1110126', 'OBI:1110127', 'OBI:1110128', 'OBI:1110129', 'OBI:1110130', 'OBI:1110131', 'OBI:1110150', 'OBI:1110151', 'OBI:1110152', 'OBI:1110153', 'OBI:1110154', 'OBI:1110155', 'OBI:1110156', 'OBI:1110157', 'OBI:1110158', 'OBI:1110159', 'OBI:1110160', 'OBI:1110161', 'OBI:1110162', 'OBI:1110163', 'OBI:1110167', 'OBI:1110168', 'OBI:1110170', 'OBI:1110171', 'OBI:1110172', 'OBI:1110173', 'OBI:1110174', 'OBI:1110175', 'OBI:1110177', 'OBI:1110178', 'OBI:1110179', 'OBI:1110180', 'OBI:1110181', 'OBI:1110207', 'OBI:2100001', 'OBI:2100002', 'OBI:2100003', 'OBI:2100004', 'OBI:2100005', 'OBI:2100006', 'OBI:2100007', 'OBI:2100008', 'OBI:2100009', 'OBI:2100010', 'OBI:2100011', 'OBI:2100012', 'OBI:2100013', 'OBI:2100014', 'OBI:2100015', 'OBI:2100016', 'OBI:2100017', 'OBI:2100018', 'OBI:2100019', 'OBI:2100020', 'OBI:2100021', 'OBI:2100022', 'OBI:2100023', 'OBI:2100024', 'OBI:2100025', 'OBI:2100026', 'OBI:2100027', 'OBI:2100028', 'OBI:2100029', 'OBI:2100030', 'OBI:2100031', 'OBI:2100032', 'OBI:2100033', 'OBI:2100034', 'OBI:2100035', 'OBI:2100036', 'OBI:2100037', 'OBI:2100038', 'OBI:2100039', 'OBI:2100040', 'OBI:2100041', 'OBI:2100042', 'OBI:2100043', 'OBI:2100044', 'OBI:2100045', 'OBI:2100046', 'OBI:2100047', 'OBI:2100048', 'OBI:2100049', 'OBI:2100050', 'OBI:2100051', 'OBI:2100052', 'OBI:2100053', 'OBI:2100054', 'OBI:2100055', 'OBI:2100056', 'OBI:2100057', 'OBI:2100058', 'OBI:2100059', 'OBI:2100060', 'OBI:2100061', 'OBI:2100062', 'OBI:2100063', 'OBI:2100064', 'OBI:2100065', 'OBI:2100066', 'OBI:2100067', 'OBI:2100068', 'OBI:2100069', 'OBI:2100070', 'OBI:2100071', 'OBI:2100072', 'OBI:2100073', 'OBI:2100074', 'OBI:2100075', 'OBI:2100076', 'OBI:2100077', 'OBI:2100078', 'OBI:2100079', 'OBI:2100080', 'OBI:2100081', 'OBI:2100082', 'OBI:2100083', 'OBI:2100084', 'OBI:2100085', 'OBI:2100086', 'OBI:2100087', 'OBI:2100088', 'OBI:2100089', 'OBI:2100090', 'OBI:2100091', 'OBI:2100092', 'OBI:2100093', 'OBI:2100094', 'OBI:2100095', 'OBI:2100096', 'OBI:2100097', 'OBI:2100098', 'OBI:2100099', 'OBI:2100100', 'OBI:2100101', 'OBI:2100102', 'OBI:2100103', 'OBI:2100104', 'OBI:2100105', 'OBI:2100106', 'OBI:2100107', 'OBI:2100108', 'OBI:2100109', 'OBI:2100110', 'OBI:2100111', 'OBI:2100112', 'OBI:2100113', 'OBI:2100114', 'OBI:2100115', 'OBI:2100116', 'OBI:2100117', 'OBI:2100118', 'OBI:2100119', 'OBI:2100120', 'OBI:2100121', 'OBI:2100122', 'OBI:2100123', 'OBI:2100124', 'OBI:2100125', 'OBI:2100126', 'OBI:2100127', 'OBI:2100128', 'OBI:2100129', 'OBI:2100130', 'OBI:2100131', 'OBI:2100132', 'OBI:2100133', 'OBI:2100134', 'OBI:2100135', 'OBI:2100136', 'OBI:2100137', 'OBI:2100138', 'OBI:2100139', 'OBI:2100140', 'OBI:2100141', 'OBI:2100142', 'OBI:2100143', 'OBI:2100144', 'OBI:2100145', 'OBI:2100146', 'OBI:2100147', 'OBI:2100148', 'OBI:2100149', 'OBI:2100150', 'OBI:2100151', 'OBI:2100152', 'OBI:2100153', 'OBI:2100154', 'OBI:2100155', 'OBI:2100156', 'OBI:2100157', 'OBI:2100158', 'OBI:2100159', 'OBI:2100160', 'OBI:2100161', 'OBI:2100162', 'OBI:2100163', 'OBI:2100164', 'OBI:2100165', 'OBI:2100166', 'OBI:2100167', 'OBI:2100168', 'OBI:2100169', 'OBI:2100170', 'OBI:2100171', 'OBI:2100172', 'OBI:2100173', 'OBI:2100174', 'OBI:2100175', 'OBI:2100176', 'OBI:2100177', 'OBI:2100178', 'OBI:2100179', 'OBI:2100180', 'OBI:2100181', 'OBI:2100182', 'OBI:2100183', 'OBI:2100184', 'OBI:2100185', 'OBI:2100186', 'OBI:2100187', 'OBI:2100188', 'OBI:2100189', 'OBI:2100190', 'OBI:2100191', 'OBI:2100192', 'OBI:2100193', 'OBI:2100194', 'OBI:2100195', 'OBI:2100196', 'OBI:2100197', 'OBI:2100198', 'OBI:2100199', 'OBI:2100200', 'OBI:2100201', 'OBI:2100202', 'OBI:2100203', 'OBI:2100204', 'OBI:2100205', 'OBI:2100206', 'OBI:2100207', 'OBI:2100208', 'OBI:2100209', 'OBI:2100210', 'OBI:2100211', 'OBI:2100212', 'OBI:2100213', 'OBI:2100214', 'OBI:2100215', 'OBI:2100216', 'OBI:2100217', 'OBI:2100218', 'OBI:2100219', 'OBI:2100220', 'OBI:2100221', 'OBI:2100222', 'OBI:2100223', 'OBI:2100224', 'OBI:2100225', 'OBI:2100226', 'OBI:2100227', 'OBI:2100228', 'OBI:2100229', 'OBI:2100230', 'OBI:2100231', 'OBI:2100232', 'OBI:2100233', 'OBI:2100234', 'OBI:2100235', 'OBI:2100236', 'OBI:2100237', 'OBI:2100238', 'OBI:2100239', 'OBI:2100240', 'OBI:2100241', 'OBI:2100242', 'OBI:2100243', 'OBI:2100244', 'OBI:2100245', 'OBI:2100246', 'OBI:2100247', 'OBI:2100248', 'OBI:2100249', 'OBI:2100250', 'OBI:2100251', 'OBI:2100252', 'OBI:2100253', 'OBI:2100254', 'OBI:2100255', 'OBI:2100256', 'OBI:2100257', 'OBI:2100258', 'OBI:2100259', 'OBI:2100260', 'OBI:2100261', 'OBI:2100262', 'OBI:2100263', 'OBI:2100264', 'OBI:2100265', 'OBI:2100266', 'OBI:2100267', 'OBI:2100268', 'OBI:2100269', 'OBI:2100270', 'OBI:2100271', 'OBI:2100272', 'OBI:2100273', 'OBI:2100274', 'OBI:2100275', 'OBI:2100276', 'OBI:2100277', 'OBI:2100278', 'OBI:2100279', 'OBI:2100280', 'OBI:2100281', 'OBI:2100282', 'OBI:2100283', 'OBI:2100284', 'OBI:2100285', 'OBI:2100286', 'OBI:2100287', 'OBI:2100288', 'OBI:2100289', 'OBI:2100290', 'OBI:2100291', 'OBI:2100292', 'OBI:2100293', 'OBI:2100294', 'OBI:2100295', 'OBI:2100296', 'OBI:2100297', 'OBI:2100298', 'OBI:2100299', 'OBI:2100300', 'OBI:2100301', 'OBI:2100302', 'OBI:2100303', 'OBI:2100304', 'OBI:2100305', 'OBI:2100306', 'OBI:2100307', 'OBI:2100308', 'OBI:2100309', 'OBI:2100310', 'OBI:2100311', 'OBI:2100312', 'OBI:2100313', 'OBI:2100314', 'OBI:2100315', 'OBI:2100316', 'OBI:2100317', 'OBI:2100318', 'OBI:2100319', 'OBI:2100320', 'OBI:2100321', 'OBI:2100322', 'OBI:2100323', 'OBI:2100324', 'OBI:2100325', 'OBI:2100326', 'OBI:2100327', 'OBI:2100328', 'OBI:2100329', 'OBI:2100330', 'OBI:2100331', 'OBI:2100332', 'OBI:2100333', 'OBI:2100334', 'OBI:2100335', 'OBI:2100336', 'OBI:2100337', 'OBI:2100338', 'OBI:2100339', 'OBI:2100340', 'OBI:2100341', 'OBI:2100342', 'OBI:2100343', 'OBI:2100344', 'OBI:2100345', 'OBI:2100346', 'OBI:2100347', 'OBI:2100348', 'OBI:2100349', 'OBI:2100350', 'OBI:2100351', 'OBI:2100352', 'OBI:2100353', 'OBI:2100354', 'OBI:2100355', 'OBI:2100356', 'OBI:2100357', 'OBI:2100358', 'OBI:2100359', 'OBI:2100360', 'OBI:2100361', 'OBI:2100362', 'OBI:2100363', 'OBI:2100364', 'OBI:2100365', 'OBI:2100366', 'OBI:2100367', 'OBI:2100368', 'OBI:2100369', 'OBI:2100370', 'OBI:2100371', 'OBI:2100372', 'OBI:2100373', 'OBI:2100374', 'OBI:2100375', 'OBI:2100376', 'OBI:2100377', 'OBI:2100378', 'OBI:2100379', 'OBI:2100380', 'OBI:2100381', 'OBI:2100382', 'OBI:2100383', 'OBI:2100384', 'OBI:2100385', 'OBI:2100386', 'OBI:2100387', 'OBI:2100388', 'OBI:2100389', 'OBI:2100390', 'OBI:2100391', 'OBI:2100392', 'OBI:2100393', 'OBI:2100394', 'OBI:2100395', 'OBI:2100396', 'OBI:2100397', 'OBI:2100398', 'OBI:2100399', 'OBI:2100400', 'OBI:2100401', 'OBI:2100402', 'OBI:9999994', name='EnumAssayType'), nullable=False )
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
    None
    """
    __tablename__ = 'Record_external_id'

    Record_id = Column(Integer(), ForeignKey('Record.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Record_external_id(Record_id={self.Record_id},external_id={self.external_id},)"



    


class StudyProgram(Base):
    """
    None
    """
    __tablename__ = 'Study_program'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    program = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Study_program(Study_study_id={self.Study_study_id},program={self.program},)"



    


class StudyFundingSource(Base):
    """
    None
    """
    __tablename__ = 'Study_funding_source'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    funding_source = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_funding_source(Study_study_id={self.Study_study_id},funding_source={self.funding_source},)"



    


class StudyPrincipalInvestigator(Base):
    """
    None
    """
    __tablename__ = 'Study_principal_investigator'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    principal_investigator_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Study_principal_investigator(Study_study_id={self.Study_study_id},principal_investigator_id={self.principal_investigator_id},)"



    


class StudyContact(Base):
    """
    None
    """
    __tablename__ = 'Study_contact'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    contact_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Study_contact(Study_study_id={self.Study_study_id},contact_id={self.contact_id},)"



    


class StudyPublication(Base):
    """
    None
    """
    __tablename__ = 'Study_publication'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    publication_id = Column(Integer(), ForeignKey('Publication.id'), primary_key=True)
    

    def __repr__(self):
        return f"Study_publication(Study_study_id={self.Study_study_id},publication_id={self.publication_id},)"



    


class StudyExternalId(Base):
    """
    None
    """
    __tablename__ = 'Study_external_id'

    Study_study_id = Column(Text(), ForeignKey('Study.study_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_external_id(Study_study_id={self.Study_study_id},external_id={self.external_id},)"



    


class StudyMetadataParticipantLifespanStage(Base):
    """
    None
    """
    __tablename__ = 'StudyMetadata_participant_lifespan_stage'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    participant_lifespan_stage = Column(Enum(name='EnumParticipantLifespanStage'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_participant_lifespan_stage(StudyMetadata_study_id={self.StudyMetadata_study_id},participant_lifespan_stage={self.participant_lifespan_stage},)"



    


class StudyMetadataStudyDesign(Base):
    """
    None
    """
    __tablename__ = 'StudyMetadata_study_design'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    study_design_concept_curie = Column(Text(), ForeignKey('Concept.concept_curie'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_study_design(StudyMetadata_study_id={self.StudyMetadata_study_id},study_design_concept_curie={self.study_design_concept_curie},)"



    


class StudyMetadataClinicalDataSourceType(Base):
    """
    None
    """
    __tablename__ = 'StudyMetadata_clinical_data_source_type'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    clinical_data_source_type = Column(Enum('CAMO:0000014', 'CAMO:0000010', 'CAMO:0000011', 'CAMO:0000012', 'CAMO:0000013', name='EnumDataSourceType'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_clinical_data_source_type(StudyMetadata_study_id={self.StudyMetadata_study_id},clinical_data_source_type={self.clinical_data_source_type},)"



    


class StudyMetadataDataCategory(Base):
    """
    None
    """
    __tablename__ = 'StudyMetadata_data_category'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    data_category = Column(Text(), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_data_category(StudyMetadata_study_id={self.StudyMetadata_study_id},data_category={self.data_category},)"



    


class StudyMetadataResearchDomain(Base):
    """
    None
    """
    __tablename__ = 'StudyMetadata_research_domain'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    research_domain_concept_curie = Column(Text(), ForeignKey('Concept.concept_curie'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"StudyMetadata_research_domain(StudyMetadata_study_id={self.StudyMetadata_study_id},research_domain_concept_curie={self.research_domain_concept_curie},)"



    


class StudyMetadataExternalId(Base):
    """
    None
    """
    __tablename__ = 'StudyMetadata_external_id'

    StudyMetadata_study_id = Column(Text(), ForeignKey('StudyMetadata.study_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"StudyMetadata_external_id(StudyMetadata_study_id={self.StudyMetadata_study_id},external_id={self.external_id},)"



    


class VirtualBiorepositoryContact(Base):
    """
    None
    """
    __tablename__ = 'VirtualBiorepository_contact'

    VirtualBiorepository_vbr_id = Column(Text(), ForeignKey('VirtualBiorepository.vbr_id'), primary_key=True)
    contact_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"VirtualBiorepository_contact(VirtualBiorepository_vbr_id={self.VirtualBiorepository_vbr_id},contact_id={self.contact_id},)"



    


class VirtualBiorepositoryExternalId(Base):
    """
    None
    """
    __tablename__ = 'VirtualBiorepository_external_id'

    VirtualBiorepository_vbr_id = Column(Text(), ForeignKey('VirtualBiorepository.vbr_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"VirtualBiorepository_external_id(VirtualBiorepository_vbr_id={self.VirtualBiorepository_vbr_id},external_id={self.external_id},)"



    


class DOIExternalId(Base):
    """
    None
    """
    __tablename__ = 'DOI_external_id'

    DOI_do_id = Column(Text(), ForeignKey('DOI.do_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"DOI_external_id(DOI_do_id={self.DOI_do_id},external_id={self.external_id},)"



    


class InvestigatorExternalId(Base):
    """
    None
    """
    __tablename__ = 'Investigator_external_id'

    Investigator_id = Column(Integer(), ForeignKey('Investigator.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Investigator_external_id(Investigator_id={self.Investigator_id},external_id={self.external_id},)"



    


class PublicationExternalId(Base):
    """
    None
    """
    __tablename__ = 'Publication_external_id'

    Publication_id = Column(Integer(), ForeignKey('Publication.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Publication_external_id(Publication_id={self.Publication_id},external_id={self.external_id},)"



    


class SubjectExternalId(Base):
    """
    None
    """
    __tablename__ = 'Subject_external_id'

    Subject_subject_id = Column(Text(), ForeignKey('Subject.subject_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Subject_external_id(Subject_subject_id={self.Subject_subject_id},external_id={self.external_id},)"



    


class DemographicsRace(Base):
    """
    None
    """
    __tablename__ = 'Demographics_race'

    Demographics_subject_id = Column(Text(), ForeignKey('Demographics.subject_id'), primary_key=True)
    race_concept_curie = Column(Text(), ForeignKey('Concept.concept_curie'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Demographics_race(Demographics_subject_id={self.Demographics_subject_id},race_concept_curie={self.race_concept_curie},)"



    


class DemographicsExternalId(Base):
    """
    None
    """
    __tablename__ = 'Demographics_external_id'

    Demographics_subject_id = Column(Text(), ForeignKey('Demographics.subject_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Demographics_external_id(Demographics_subject_id={self.Demographics_subject_id},external_id={self.external_id},)"



    


class FamilyExternalId(Base):
    """
    None
    """
    __tablename__ = 'Family_external_id'

    Family_family_id = Column(Text(), ForeignKey('Family.family_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Family_external_id(Family_family_id={self.Family_family_id},external_id={self.external_id},)"



    


class FamilyRelationshipExternalId(Base):
    """
    None
    """
    __tablename__ = 'FamilyRelationship_external_id'

    FamilyRelationship_family_relationship_id = Column(Text(), ForeignKey('FamilyRelationship.family_relationship_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FamilyRelationship_external_id(FamilyRelationship_family_relationship_id={self.FamilyRelationship_family_relationship_id},external_id={self.external_id},)"



    


class FamilyMembershipExternalId(Base):
    """
    None
    """
    __tablename__ = 'FamilyMembership_external_id'

    FamilyMembership_family_membership_id = Column(Text(), ForeignKey('FamilyMembership.family_membership_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FamilyMembership_external_id(FamilyMembership_family_membership_id={self.FamilyMembership_family_membership_id},external_id={self.external_id},)"



    


class SubjectAssertionConcept(Base):
    """
    None
    """
    __tablename__ = 'SubjectAssertion_concept'

    SubjectAssertion_assertion_id = Column(Text(), ForeignKey('SubjectAssertion.assertion_id'), primary_key=True)
    concept_concept_curie = Column(Text(), ForeignKey('Concept.concept_curie'), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_concept(SubjectAssertion_assertion_id={self.SubjectAssertion_assertion_id},concept_concept_curie={self.concept_concept_curie},)"



    


class SubjectAssertionValueConcept(Base):
    """
    None
    """
    __tablename__ = 'SubjectAssertion_value_concept'

    SubjectAssertion_assertion_id = Column(Text(), ForeignKey('SubjectAssertion.assertion_id'), primary_key=True)
    value_concept_concept_curie = Column(Text(), ForeignKey('Concept.concept_curie'), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_value_concept(SubjectAssertion_assertion_id={self.SubjectAssertion_assertion_id},value_concept_concept_curie={self.value_concept_concept_curie},)"



    


class SubjectAssertionExternalId(Base):
    """
    None
    """
    __tablename__ = 'SubjectAssertion_external_id'

    SubjectAssertion_assertion_id = Column(Text(), ForeignKey('SubjectAssertion.assertion_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_external_id(SubjectAssertion_assertion_id={self.SubjectAssertion_assertion_id},external_id={self.external_id},)"



    


class SampleProcessing(Base):
    """
    None
    """
    __tablename__ = 'Sample_processing'

    Sample_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    processing = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_processing(Sample_sample_id={self.Sample_sample_id},processing={self.processing},)"



    


class SampleStorageMethod(Base):
    """
    None
    """
    __tablename__ = 'Sample_storage_method'

    Sample_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    storage_method = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_storage_method(Sample_sample_id={self.Sample_sample_id},storage_method={self.storage_method},)"



    


class SampleExternalId(Base):
    """
    None
    """
    __tablename__ = 'Sample_external_id'

    Sample_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_external_id(Sample_sample_id={self.Sample_sample_id},external_id={self.external_id},)"



    


class BiospecimenCollectionExternalId(Base):
    """
    None
    """
    __tablename__ = 'BiospecimenCollection_external_id'

    BiospecimenCollection_biospecimen_collection_id = Column(Text(), ForeignKey('BiospecimenCollection.biospecimen_collection_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"BiospecimenCollection_external_id(BiospecimenCollection_biospecimen_collection_id={self.BiospecimenCollection_biospecimen_collection_id},external_id={self.external_id},)"



    


class AliquotExternalId(Base):
    """
    None
    """
    __tablename__ = 'Aliquot_external_id'

    Aliquot_aliquot_id = Column(Text(), ForeignKey('Aliquot.aliquot_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Aliquot_external_id(Aliquot_aliquot_id={self.Aliquot_aliquot_id},external_id={self.external_id},)"



    


class EncounterExternalId(Base):
    """
    None
    """
    __tablename__ = 'Encounter_external_id'

    Encounter_encounter_id = Column(Text(), ForeignKey('Encounter.encounter_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Encounter_external_id(Encounter_encounter_id={self.Encounter_encounter_id},external_id={self.external_id},)"



    


class EncounterDefinitionActivityDefinitionId(Base):
    """
    None
    """
    __tablename__ = 'EncounterDefinition_activity_definition_id'

    EncounterDefinition_encounter_definition_id = Column(Text(), ForeignKey('EncounterDefinition.encounter_definition_id'), primary_key=True)
    activity_definition_id_activity_definition_id = Column(Text(), ForeignKey('ActivityDefinition.activity_definition_id'), primary_key=True)
    

    def __repr__(self):
        return f"EncounterDefinition_activity_definition_id(EncounterDefinition_encounter_definition_id={self.EncounterDefinition_encounter_definition_id},activity_definition_id_activity_definition_id={self.activity_definition_id_activity_definition_id},)"



    


class EncounterDefinitionExternalId(Base):
    """
    None
    """
    __tablename__ = 'EncounterDefinition_external_id'

    EncounterDefinition_encounter_definition_id = Column(Text(), ForeignKey('EncounterDefinition.encounter_definition_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"EncounterDefinition_external_id(EncounterDefinition_encounter_definition_id={self.EncounterDefinition_encounter_definition_id},external_id={self.external_id},)"



    


class ActivityDefinitionExternalId(Base):
    """
    None
    """
    __tablename__ = 'ActivityDefinition_external_id'

    ActivityDefinition_activity_definition_id = Column(Text(), ForeignKey('ActivityDefinition.activity_definition_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"ActivityDefinition_external_id(ActivityDefinition_activity_definition_id={self.ActivityDefinition_activity_definition_id},external_id={self.external_id},)"



    


class FileSubjectId(Base):
    """
    None
    """
    __tablename__ = 'File_subject_id'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    subject_id_subject_id = Column(Text(), ForeignKey('Subject.subject_id'), primary_key=True)
    

    def __repr__(self):
        return f"File_subject_id(File_file_id={self.File_file_id},subject_id_subject_id={self.subject_id_subject_id},)"



    


class FileSampleId(Base):
    """
    None
    """
    __tablename__ = 'File_sample_id'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    sample_id_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    

    def __repr__(self):
        return f"File_sample_id(File_file_id={self.File_file_id},sample_id_sample_id={self.sample_id_sample_id},)"



    


class FileHash(Base):
    """
    None
    """
    __tablename__ = 'File_hash'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    hash_id = Column(Integer(), ForeignKey('FileHash.id'), primary_key=True)
    

    def __repr__(self):
        return f"File_hash(File_file_id={self.File_file_id},hash_id={self.hash_id},)"



    


class FileExternalId(Base):
    """
    None
    """
    __tablename__ = 'File_external_id'

    File_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"File_external_id(File_file_id={self.File_file_id},external_id={self.external_id},)"



    


class AssaySubjectId(Base):
    """
    None
    """
    __tablename__ = 'Assay_subject_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    subject_id_subject_id = Column(Text(), ForeignKey('Subject.subject_id'), primary_key=True)
    

    def __repr__(self):
        return f"Assay_subject_id(Assay_assay_id={self.Assay_assay_id},subject_id_subject_id={self.subject_id_subject_id},)"



    


class AssaySampleId(Base):
    """
    None
    """
    __tablename__ = 'Assay_sample_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    sample_id_sample_id = Column(Text(), ForeignKey('Sample.sample_id'), primary_key=True)
    

    def __repr__(self):
        return f"Assay_sample_id(Assay_assay_id={self.Assay_assay_id},sample_id_sample_id={self.sample_id_sample_id},)"



    


class AssayFileId(Base):
    """
    None
    """
    __tablename__ = 'Assay_file_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    file_id_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    

    def __repr__(self):
        return f"Assay_file_id(Assay_assay_id={self.Assay_assay_id},file_id_file_id={self.file_id_file_id},)"



    


class AssayExternalId(Base):
    """
    None
    """
    __tablename__ = 'Assay_external_id'

    Assay_assay_id = Column(Text(), ForeignKey('Assay.assay_id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Assay_external_id(Assay_assay_id={self.Assay_assay_id},external_id={self.external_id},)"



    


class DatasetFileId(Base):
    """
    None
    """
    __tablename__ = 'Dataset_file_id'

    Dataset_dataset_id = Column(Text(), ForeignKey('Dataset.dataset_id'), primary_key=True)
    file_id_file_id = Column(Text(), ForeignKey('File.file_id'), primary_key=True)
    

    def __repr__(self):
        return f"Dataset_file_id(Dataset_dataset_id={self.Dataset_dataset_id},file_id_file_id={self.file_id_file_id},)"



    


class DatasetPublication(Base):
    """
    None
    """
    __tablename__ = 'Dataset_publication'

    Dataset_dataset_id = Column(Text(), ForeignKey('Dataset.dataset_id'), primary_key=True)
    publication_id = Column(Integer(), ForeignKey('Publication.id'), primary_key=True)
    

    def __repr__(self):
        return f"Dataset_publication(Dataset_dataset_id={self.Dataset_dataset_id},publication_id={self.publication_id},)"



    


