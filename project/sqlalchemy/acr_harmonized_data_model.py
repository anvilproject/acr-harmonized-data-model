
from sqlalchemy import Column, Index, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import *
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

Base = declarative_base()
metadata = Base.metadata


class Thing(Base):
    """
    Highest Level Class
    """
    __tablename__ = 'Thing'

    id = Column(Text(), primary_key=True, nullable=False )
    
    
    external_id_rel = relationship( "ThingExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: ThingExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Thing(id={self.id},)"



    


class ThingExternalId(Base):
    """
    
    """
    __tablename__ = 'Thing_external_id'

    Thing_id = Column(Text(), ForeignKey('Thing.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Thing_external_id(Thing_id={self.Thing_id},external_id={self.external_id},)"



    


class AccessControlledRecordExternalId(Base):
    """
    
    """
    __tablename__ = 'AccessControlledRecord_external_id'

    AccessControlledRecord_id = Column(Text(), ForeignKey('AccessControlledRecord.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"AccessControlledRecord_external_id(AccessControlledRecord_id={self.AccessControlledRecord_id},external_id={self.external_id},)"



    


class SubjectExternalId(Base):
    """
    
    """
    __tablename__ = 'Subject_external_id'

    Subject_id = Column(Text(), ForeignKey('Subject.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Subject_external_id(Subject_id={self.Subject_id},external_id={self.external_id},)"



    


class DemographicsRace(Base):
    """
    
    """
    __tablename__ = 'Demographics_race'

    Demographics_id = Column(Text(), ForeignKey('Demographics.id'), primary_key=True)
    race = Column(Enum('american_indian_or_alaskan_native', 'asian', 'black_or_african_american', 'native_hawaiian_or_pacific_islander', 'white', 'other_race', 'unknown', 'asked_but_unknown', name='EnumRace'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"Demographics_race(Demographics_id={self.Demographics_id},race={self.race},)"



    


class DemographicsSourceData(Base):
    """
    
    """
    __tablename__ = 'Demographics_source_data'

    Demographics_id = Column(Text(), ForeignKey('Demographics.id'), primary_key=True)
    source_data_id = Column(Text(), ForeignKey('SourceData.id'), primary_key=True)
    

    def __repr__(self):
        return f"Demographics_source_data(Demographics_id={self.Demographics_id},source_data_id={self.source_data_id},)"



    


class DemographicsExternalId(Base):
    """
    
    """
    __tablename__ = 'Demographics_external_id'

    Demographics_id = Column(Text(), ForeignKey('Demographics.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Demographics_external_id(Demographics_id={self.Demographics_id},external_id={self.external_id},)"



    


class StudyFundingSource(Base):
    """
    
    """
    __tablename__ = 'Study_funding_source'

    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    funding_source = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_funding_source(Study_id={self.Study_id},funding_source={self.funding_source},)"



    


class StudyPrincipalInvestigator(Base):
    """
    
    """
    __tablename__ = 'Study_principal_investigator'

    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    principal_investigator = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_principal_investigator(Study_id={self.Study_id},principal_investigator={self.principal_investigator},)"



    


class StudyExternalId(Base):
    """
    
    """
    __tablename__ = 'Study_external_id'

    Study_id = Column(Text(), ForeignKey('Study.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Study_external_id(Study_id={self.Study_id},external_id={self.external_id},)"



    


class SubjectAssertionSourceData(Base):
    """
    
    """
    __tablename__ = 'SubjectAssertion_source_data'

    SubjectAssertion_id = Column(Text(), ForeignKey('SubjectAssertion.id'), primary_key=True)
    source_data_id = Column(Text(), ForeignKey('SourceData.id'), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_source_data(SubjectAssertion_id={self.SubjectAssertion_id},source_data_id={self.source_data_id},)"



    


class SubjectAssertionExternalId(Base):
    """
    
    """
    __tablename__ = 'SubjectAssertion_external_id'

    SubjectAssertion_id = Column(Text(), ForeignKey('SubjectAssertion.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SubjectAssertion_external_id(SubjectAssertion_id={self.SubjectAssertion_id},external_id={self.external_id},)"



    


class DataSourceExternalId(Base):
    """
    
    """
    __tablename__ = 'DataSource_external_id'

    DataSource_id = Column(Text(), ForeignKey('DataSource.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"DataSource_external_id(DataSource_id={self.DataSource_id},external_id={self.external_id},)"



    


class SourceDataQueryParameter(Base):
    """
    
    """
    __tablename__ = 'SourceData_query_parameter'

    SourceData_id = Column(Text(), ForeignKey('SourceData.id'), primary_key=True)
    query_parameter = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SourceData_query_parameter(SourceData_id={self.SourceData_id},query_parameter={self.query_parameter},)"



    


class SourceDataExternalId(Base):
    """
    
    """
    __tablename__ = 'SourceData_external_id'

    SourceData_id = Column(Text(), ForeignKey('SourceData.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"SourceData_external_id(SourceData_id={self.SourceData_id},external_id={self.external_id},)"



    


class AccessPolicyDataAccessType(Base):
    """
    
    """
    __tablename__ = 'AccessPolicy_data_access_type'

    AccessPolicy_id = Column(Text(), ForeignKey('AccessPolicy.id'), primary_key=True)
    data_access_type = Column(Enum('open', 'registered', 'controlled', 'gsr_restricted', 'gsr_allowed', name='EnumAccessType'), primary_key=True)
    

    def __repr__(self):
        return f"AccessPolicy_data_access_type(AccessPolicy_id={self.AccessPolicy_id},data_access_type={self.data_access_type},)"



    


class AccessPolicyAccessPolicyCode(Base):
    """
    
    """
    __tablename__ = 'AccessPolicy_access_policy_code'

    AccessPolicy_id = Column(Text(), ForeignKey('AccessPolicy.id'), primary_key=True)
    access_policy_code = Column(Enum('gru', 'hmb', 'ds', 'irb', 'pub', 'col', 'npu', 'mds', 'gso', 'gsr', 'rd', name='EnumAccessCode'), primary_key=True, nullable=False )
    

    def __repr__(self):
        return f"AccessPolicy_access_policy_code(AccessPolicy_id={self.AccessPolicy_id},access_policy_code={self.access_policy_code},)"



    


class AccessPolicyExternalId(Base):
    """
    
    """
    __tablename__ = 'AccessPolicy_external_id'

    AccessPolicy_id = Column(Text(), ForeignKey('AccessPolicy.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"AccessPolicy_external_id(AccessPolicy_id={self.AccessPolicy_id},external_id={self.external_id},)"



    


class FamilyFamilyRelationships(Base):
    """
    
    """
    __tablename__ = 'Family_family_relationships'

    Family_id = Column(Text(), ForeignKey('Family.id'), primary_key=True)
    family_relationships_id = Column(Text(), ForeignKey('FamilyRelationship.id'), primary_key=True)
    

    def __repr__(self):
        return f"Family_family_relationships(Family_id={self.Family_id},family_relationships_id={self.family_relationships_id},)"



    


class FamilyExternalId(Base):
    """
    
    """
    __tablename__ = 'Family_external_id'

    Family_id = Column(Text(), ForeignKey('Family.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Family_external_id(Family_id={self.Family_id},external_id={self.external_id},)"



    


class FamilyRelationshipExternalId(Base):
    """
    
    """
    __tablename__ = 'FamilyRelationship_external_id'

    FamilyRelationship_id = Column(Text(), ForeignKey('FamilyRelationship.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FamilyRelationship_external_id(FamilyRelationship_id={self.FamilyRelationship_id},external_id={self.external_id},)"



    


class FamilyMemberExternalId(Base):
    """
    
    """
    __tablename__ = 'FamilyMember_external_id'

    FamilyMember_id = Column(Text(), ForeignKey('FamilyMember.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FamilyMember_external_id(FamilyMember_id={self.FamilyMember_id},external_id={self.external_id},)"



    


class SampleProcessing(Base):
    """
    
    """
    __tablename__ = 'Sample_processing'

    Sample_id = Column(Text(), ForeignKey('Sample.id'), primary_key=True)
    processing = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_processing(Sample_id={self.Sample_id},processing={self.processing},)"



    


class SampleStorageMethod(Base):
    """
    
    """
    __tablename__ = 'Sample_storage_method'

    Sample_id = Column(Text(), ForeignKey('Sample.id'), primary_key=True)
    storage_method = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_storage_method(Sample_id={self.Sample_id},storage_method={self.storage_method},)"



    


class SampleExternalId(Base):
    """
    
    """
    __tablename__ = 'Sample_external_id'

    Sample_id = Column(Text(), ForeignKey('Sample.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Sample_external_id(Sample_id={self.Sample_id},external_id={self.external_id},)"



    


class BiospecimenCollectionExternalId(Base):
    """
    
    """
    __tablename__ = 'BiospecimenCollection_external_id'

    BiospecimenCollection_id = Column(Text(), ForeignKey('BiospecimenCollection.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"BiospecimenCollection_external_id(BiospecimenCollection_id={self.BiospecimenCollection_id},external_id={self.external_id},)"



    


class AliquotExternalId(Base):
    """
    
    """
    __tablename__ = 'Aliquot_external_id'

    Aliquot_id = Column(Text(), ForeignKey('Aliquot.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"Aliquot_external_id(Aliquot_id={self.Aliquot_id},external_id={self.external_id},)"



    


class FileSubject(Base):
    """
    
    """
    __tablename__ = 'File_subject'

    File_id = Column(Text(), ForeignKey('File.id'), primary_key=True)
    subject_id = Column(Text(), ForeignKey('Subject.id'), primary_key=True)
    

    def __repr__(self):
        return f"File_subject(File_id={self.File_id},subject_id={self.subject_id},)"



    


class FileSample(Base):
    """
    
    """
    __tablename__ = 'File_sample'

    File_id = Column(Text(), ForeignKey('File.id'), primary_key=True)
    sample_id = Column(Text(), ForeignKey('Sample.id'), primary_key=True)
    

    def __repr__(self):
        return f"File_sample(File_id={self.File_id},sample_id={self.sample_id},)"



    


class FileExternalId(Base):
    """
    
    """
    __tablename__ = 'File_external_id'

    File_id = Column(Text(), ForeignKey('File.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"File_external_id(File_id={self.File_id},external_id={self.external_id},)"



    


class FileMetadataExternalId(Base):
    """
    
    """
    __tablename__ = 'FileMetadata_external_id'

    FileMetadata_id = Column(Text(), ForeignKey('FileMetadata.id'), primary_key=True)
    external_id = Column(Text(), primary_key=True)
    

    def __repr__(self):
        return f"FileMetadata_external_id(FileMetadata_id={self.FileMetadata_id},external_id={self.external_id},)"



    


class AccessControlledRecord(Thing):
    """
    Element for which specific access control restrictions apply.
    """
    __tablename__ = 'AccessControlledRecord'

    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    external_id_rel = relationship( "AccessControlledRecordExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: AccessControlledRecordExternalId(external_id=x_))
    

    def __repr__(self):
        return f"AccessControlledRecord(has_access_policy={self.has_access_policy},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Study(Thing):
    """
    Study Meta Data
    """
    __tablename__ = 'Study'

    parent_study_id = Column(Text(), ForeignKey('Study.id'))
    study_title = Column(Text(), nullable=False )
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    funding_source_rel = relationship( "StudyFundingSource" )
    funding_source = association_proxy("funding_source_rel", "funding_source",
                                  creator=lambda x_: StudyFundingSource(funding_source=x_))
    
    
    principal_investigator_rel = relationship( "StudyPrincipalInvestigator" )
    principal_investigator = association_proxy("principal_investigator_rel", "principal_investigator",
                                  creator=lambda x_: StudyPrincipalInvestigator(principal_investigator=x_))
    
    
    external_id_rel = relationship( "StudyExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: StudyExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Study(parent_study_id={self.parent_study_id},study_title={self.study_title},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class DataSource(Thing):
    """
    Query configuration for specifying a source from which data are pulled.
    """
    __tablename__ = 'DataSource'

    snapshot_id = Column(Text())
    google_data_project = Column(Text())
    snapshot_dataset = Column(Text())
    table = Column(Text())
    parameterized_query = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    external_id_rel = relationship( "DataSourceExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: DataSourceExternalId(external_id=x_))
    

    def __repr__(self):
        return f"DataSource(snapshot_id={self.snapshot_id},google_data_project={self.google_data_project},snapshot_dataset={self.snapshot_dataset},table={self.table},parameterized_query={self.parameterized_query},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class AccessPolicy(Thing):
    """
    Describes the access required for a given element of data.
    """
    __tablename__ = 'AccessPolicy'

    disease_limitation = Column(Text())
    description = Column(Text(), nullable=False )
    website = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    data_access_type_rel = relationship( "AccessPolicyDataAccessType" )
    data_access_type = association_proxy("data_access_type_rel", "data_access_type",
                                  creator=lambda x_: AccessPolicyDataAccessType(data_access_type=x_))
    
    
    access_policy_code_rel = relationship( "AccessPolicyAccessPolicyCode" )
    access_policy_code = association_proxy("access_policy_code_rel", "access_policy_code",
                                  creator=lambda x_: AccessPolicyAccessPolicyCode(access_policy_code=x_))
    
    
    external_id_rel = relationship( "AccessPolicyExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: AccessPolicyExternalId(external_id=x_))
    

    def __repr__(self):
        return f"AccessPolicy(disease_limitation={self.disease_limitation},description={self.description},website={self.website},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class FileMetadata(Thing):
    """
    Metadata about the contents of the file.
    """
    __tablename__ = 'FileMetadata'

    code = Column(Text())
    display = Column(Text())
    value_code = Column(Text())
    value_display = Column(Text())
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    external_id_rel = relationship( "FileMetadataExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FileMetadataExternalId(external_id=x_))
    

    def __repr__(self):
        return f"FileMetadata(code={self.code},display={self.display},value_code={self.value_code},value_display={self.value_display},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Subject(AccessControlledRecord):
    """
    This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity.
    """
    __tablename__ = 'Subject'

    subject_type = Column(Enum('participant', 'non_participant', 'cell_line', 'animal_model', 'group', 'other', name='EnumSubjectType'), nullable=False )
    organism_type = Column(Text())
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    has_demographics_id = Column(Text(), ForeignKey('Demographics.id'))
    has_demographics = relationship("Demographics", uselist=False, foreign_keys=[has_demographics_id])
    
    
    # One-To-Many: OneToAnyMapping(source_class='Subject', source_slot='has_sample', mapping_type=None, target_class='Sample', target_slot='Subject_id', join_class=None, uses_join_table=None, multivalued=False)
    has_sample = relationship( "Sample", foreign_keys="[Sample.Subject_id]")
    
    
    # One-To-Many: OneToAnyMapping(source_class='Subject', source_slot='has_assertion', mapping_type=None, target_class='SubjectAssertion', target_slot='Subject_id', join_class=None, uses_join_table=None, multivalued=False)
    has_assertion = relationship( "SubjectAssertion", foreign_keys="[SubjectAssertion.Subject_id]")
    
    
    external_id_rel = relationship( "SubjectExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: SubjectExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Subject(subject_type={self.subject_type},organism_type={self.organism_type},has_access_policy={self.has_access_policy},id={self.id},has_demographics_id={self.has_demographics_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Demographics(AccessControlledRecord):
    """
    Basic participant demographics summary
    """
    __tablename__ = 'Demographics'

    date_of_birth = Column(Integer())
    date_of_birth_type = Column(Enum('exact', 'year_only', 'shifted', 'decade_only', 'other', name='EnumDateOfBirthType'))
    sex = Column(Enum('female', 'male', 'unknown', 'intersex', name='EnumSex'), nullable=False )
    sex_display = Column(Text(), nullable=False )
    race_display = Column(Text(), nullable=False )
    ethnicity = Column(Enum('hispanic_or_latino', 'not_hispanic_or_latino', 'unknown', 'asked_but_unknown', name='EnumEthnicity'), nullable=False )
    ethnicity_display = Column(Text(), nullable=False )
    age_at_last_vital_status = Column(Float())
    vital_status = Column(Enum('alive', 'dead', 'not_reported', 'unknown', 'unspecified', name='EnumVitalStatus'))
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    race_rel = relationship( "DemographicsRace" )
    race = association_proxy("race_rel", "race",
                                  creator=lambda x_: DemographicsRace(race=x_))
    
    
    # ManyToMany
    source_data = relationship( "SourceData", secondary="Demographics_source_data")
    
    
    external_id_rel = relationship( "DemographicsExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: DemographicsExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Demographics(date_of_birth={self.date_of_birth},date_of_birth_type={self.date_of_birth_type},sex={self.sex},sex_display={self.sex_display},race_display={self.race_display},ethnicity={self.ethnicity},ethnicity_display={self.ethnicity_display},age_at_last_vital_status={self.age_at_last_vital_status},vital_status={self.vital_status},has_access_policy={self.has_access_policy},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SubjectAssertion(AccessControlledRecord):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """
    __tablename__ = 'SubjectAssertion'

    assertion_type = Column(Enum('phenotypic_feature', 'disease', 'comorbidity', 'histology', 'clinical_finding', 'ehr_billing_code', 'measurement', name='EnumAssertionType'))
    age_at_assertion = Column(Float())
    age_at_event = Column(Float())
    age_at_resolution = Column(Float())
    code = Column(Text())
    display = Column(Text())
    value_code = Column(Text())
    value_display = Column(Text())
    value_number = Column(Float())
    value_units = Column(Text())
    value_units_display = Column(Text())
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    Subject_id = Column(Text(), ForeignKey('Subject.id'))
    
    
    # ManyToMany
    source_data = relationship( "SourceData", secondary="SubjectAssertion_source_data")
    
    
    external_id_rel = relationship( "SubjectAssertionExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: SubjectAssertionExternalId(external_id=x_))
    

    def __repr__(self):
        return f"SubjectAssertion(assertion_type={self.assertion_type},age_at_assertion={self.age_at_assertion},age_at_event={self.age_at_event},age_at_resolution={self.age_at_resolution},code={self.code},display={self.display},value_code={self.value_code},value_display={self.value_display},value_number={self.value_number},value_units={self.value_units},value_units_display={self.value_units_display},has_access_policy={self.has_access_policy},id={self.id},Subject_id={self.Subject_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class SourceData(AccessControlledRecord):
    """
    Reference to submitted data used to generate harmonized data. Applying the query_parameter(s) to the data_source.parameterized_query should return the specific data of interest.
    """
    __tablename__ = 'SourceData'

    data_source = Column(Text(), ForeignKey('DataSource.id'))
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    query_parameter_rel = relationship( "SourceDataQueryParameter" )
    query_parameter = association_proxy("query_parameter_rel", "query_parameter",
                                  creator=lambda x_: SourceDataQueryParameter(query_parameter=x_))
    
    
    external_id_rel = relationship( "SourceDataExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: SourceDataExternalId(external_id=x_))
    

    def __repr__(self):
        return f"SourceData(data_source={self.data_source},has_access_policy={self.has_access_policy},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Family(AccessControlledRecord):
    """
    A group of individuals of some relation who are grouped together in the study.
    """
    __tablename__ = 'Family'

    family_type = Column(Enum('control_only', 'duo', 'proband_only', 'trio', 'trio_plus', 'other', name='EnumFamilyType'))
    family_description = Column(Text())
    consanguinity = Column(Enum('not_suspected', 'suspected', 'known_present', 'unknown', name='EnumConsanguinityAssertion'))
    family_study_focus = Column(Text())
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    # One-To-Many: OneToAnyMapping(source_class='Family', source_slot='family_members', mapping_type=None, target_class='FamilyMember', target_slot='Family_id', join_class=None, uses_join_table=None, multivalued=False)
    family_members = relationship( "FamilyMember", foreign_keys="[FamilyMember.Family_id]")
    
    
    # ManyToMany
    family_relationships = relationship( "FamilyRelationship", secondary="Family_family_relationships")
    
    
    external_id_rel = relationship( "FamilyExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FamilyExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Family(family_type={self.family_type},family_description={self.family_description},consanguinity={self.consanguinity},family_study_focus={self.family_study_focus},has_access_policy={self.has_access_policy},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class FamilyRelationship(AccessControlledRecord):
    """
    A relationship between two Subjects.
    """
    __tablename__ = 'FamilyRelationship'

    family_member = Column(Text(), ForeignKey('Subject.id'), nullable=False )
    other_family_member = Column(Text(), ForeignKey('Subject.id'), nullable=False )
    relationship_code = Column(Text(), nullable=False )
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    external_id_rel = relationship( "FamilyRelationshipExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FamilyRelationshipExternalId(external_id=x_))
    

    def __repr__(self):
        return f"FamilyRelationship(family_member={self.family_member},other_family_member={self.other_family_member},relationship_code={self.relationship_code},has_access_policy={self.has_access_policy},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class FamilyMember(AccessControlledRecord):
    """
    Designates a Subject as a member of a family with some specified role.
    """
    __tablename__ = 'FamilyMember'

    family_member = Column(Text(), ForeignKey('Subject.id'), nullable=False )
    family_role = Column(Text())
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    Family_id = Column(Text(), ForeignKey('Family.id'))
    
    
    external_id_rel = relationship( "FamilyMemberExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FamilyMemberExternalId(external_id=x_))
    

    def __repr__(self):
        return f"FamilyMember(family_member={self.family_member},family_role={self.family_role},has_access_policy={self.has_access_policy},id={self.id},Family_id={self.Family_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Sample(AccessControlledRecord):
    """
    Biospecimen data
    """
    __tablename__ = 'Sample'

    parent_sample = Column(Text(), ForeignKey('Sample.id'))
    sample_type = Column(Text(), nullable=False )
    availablity_status = Column(Enum('available', 'unavailable', name='EnumAvailabilityStatus'))
    quantity_number = Column(Float())
    quantity_units = Column(Text())
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    Subject_id = Column(Text(), ForeignKey('Subject.id'))
    biospecimen_collection_id = Column(Text(), ForeignKey('BiospecimenCollection.id'))
    biospecimen_collection = relationship("BiospecimenCollection", uselist=False, foreign_keys=[biospecimen_collection_id])
    
    
    processing_rel = relationship( "SampleProcessing" )
    processing = association_proxy("processing_rel", "processing",
                                  creator=lambda x_: SampleProcessing(processing=x_))
    
    
    storage_method_rel = relationship( "SampleStorageMethod" )
    storage_method = association_proxy("storage_method_rel", "storage_method",
                                  creator=lambda x_: SampleStorageMethod(storage_method=x_))
    
    
    # One-To-Many: OneToAnyMapping(source_class='Sample', source_slot='aliquots', mapping_type=None, target_class='Aliquot', target_slot='Sample_id', join_class=None, uses_join_table=None, multivalued=False)
    aliquots = relationship( "Aliquot", foreign_keys="[Aliquot.Sample_id]")
    
    
    external_id_rel = relationship( "SampleExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: SampleExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Sample(parent_sample={self.parent_sample},sample_type={self.sample_type},availablity_status={self.availablity_status},quantity_number={self.quantity_number},quantity_units={self.quantity_units},has_access_policy={self.has_access_policy},id={self.id},Subject_id={self.Subject_id},biospecimen_collection_id={self.biospecimen_collection_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class BiospecimenCollection(AccessControlledRecord):
    """
    Biospecimen Collection
    """
    __tablename__ = 'BiospecimenCollection'

    age_at_collection = Column(Float())
    method = Column(Enum(name='EnumSampleCollectionMethod'))
    site = Column(Enum(name='EnumSite'))
    spatial_qualifier = Column(Enum(name='EnumSpatialQualifiers'))
    laterality = Column(Enum(name='EnumLaterality'))
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    external_id_rel = relationship( "BiospecimenCollectionExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: BiospecimenCollectionExternalId(external_id=x_))
    

    def __repr__(self):
        return f"BiospecimenCollection(age_at_collection={self.age_at_collection},method={self.method},site={self.site},spatial_qualifier={self.spatial_qualifier},laterality={self.laterality},has_access_policy={self.has_access_policy},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class Aliquot(AccessControlledRecord):
    """
    Specific tubes or details of a Sample.
    """
    __tablename__ = 'Aliquot'

    availablity_status = Column(Enum('available', 'unavailable', name='EnumAvailabilityStatus'))
    quantity_number = Column(Float())
    quantity_units = Column(Text())
    concentration_number = Column(Float())
    concentration_unit = Column(Text())
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    Sample_id = Column(Text(), ForeignKey('Sample.id'))
    
    
    external_id_rel = relationship( "AliquotExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: AliquotExternalId(external_id=x_))
    

    def __repr__(self):
        return f"Aliquot(availablity_status={self.availablity_status},quantity_number={self.quantity_number},quantity_units={self.quantity_units},concentration_number={self.concentration_number},concentration_unit={self.concentration_unit},has_access_policy={self.has_access_policy},id={self.id},Sample_id={self.Sample_id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


class File(AccessControlledRecord):
    """
    File
    """
    __tablename__ = 'File'

    filename = Column(Text())
    format = Column(Enum(name='EDAMFormats'))
    data_type = Column(Enum(name='EDAMDataTypes'))
    size = Column(Integer())
    drs_uri = Column(Text())
    file_metadata = Column(Text(), ForeignKey('FileMetadata.id'))
    has_access_policy = Column(Text(), ForeignKey('AccessPolicy.id'))
    id = Column(Text(), primary_key=True, nullable=False )
    
    
    # ManyToMany
    subject = relationship( "Subject", secondary="File_subject")
    
    
    # ManyToMany
    sample = relationship( "Sample", secondary="File_sample")
    
    
    external_id_rel = relationship( "FileExternalId" )
    external_id = association_proxy("external_id_rel", "external_id",
                                  creator=lambda x_: FileExternalId(external_id=x_))
    

    def __repr__(self):
        return f"File(filename={self.filename},format={self.format},data_type={self.data_type},size={self.size},drs_uri={self.drs_uri},file_metadata={self.file_metadata},has_access_policy={self.has_access_policy},id={self.id},)"



    
    # Using concrete inheritance: see https://docs.sqlalchemy.org/en/14/orm/inheritance.html
    __mapper_args__ = {
        'concrete': True
    }
    


