# Auto generated from acr_harmonized_data_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-01-28T16:35:05
# Schema: acr-harmonized-data-model
#
# id: https://anvilproject.org/acr-harmonized-data-model
# description: LinkML Schema for ACR Harmonized Data.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
ADMIN_GENDER = CurieNamespace('admin_gender', 'http://hl7.org/fhir/administrative-gender/')
ANVIL = CurieNamespace('anvil', 'https://anvilproject.org/acr-harmonized-data-model/')
CDC_RACE_ETH = CurieNamespace('cdc_race_eth', 'urn:oid:2.16.840.1.113883.6.238/')
HL7_NULL = CurieNamespace('hl7_null', 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/')
IG2_BIOSPECIMEN_AVAILABILITY = CurieNamespace('ig2_biospecimen_availability', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/')
IG2DAC = CurieNamespace('ig2dac', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/')
IG2DAT = CurieNamespace('ig2dat', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/')
IG_DOB_METHOD = CurieNamespace('ig_dob_method', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/')
IGCONDTYPE = CurieNamespace('igcondtype', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SNOMED_CT = CurieNamespace('snomed_ct', 'http://snomed.info/id/')
DEFAULT_ = ANVIL


# Types

# Class references
class ThingId(extended_str):
    pass


class AccessControlledRecordId(ThingId):
    pass


class SubjectId(AccessControlledRecordId):
    pass


class DemographicsId(AccessControlledRecordId):
    pass


class StudyId(ThingId):
    pass


class SubjectAssertionId(AccessControlledRecordId):
    pass


class DataSourceId(ThingId):
    pass


class SourceDataId(AccessControlledRecordId):
    pass


class AccessPolicyId(ThingId):
    pass


class FamilyId(AccessControlledRecordId):
    pass


class FamilyRelationshipId(AccessControlledRecordId):
    pass


class FamilyMemberId(AccessControlledRecordId):
    pass


class SampleId(AccessControlledRecordId):
    pass


class BiospecimenCollectionId(AccessControlledRecordId):
    pass


class AliquotId(AccessControlledRecordId):
    pass


class FileId(AccessControlledRecordId):
    pass


class FileMetadataId(ThingId):
    pass


@dataclass(repr=False)
class Thing(YAMLRoot):
    """
    Highest Level Class
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["Thing"]
    class_class_curie: ClassVar[str] = "anvil:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = ANVIL.Thing

    id: Union[str, ThingId] = None
    external_id: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        if not isinstance(self.external_id, list):
            self.external_id = [self.external_id] if self.external_id is not None else []
        self.external_id = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_id]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AccessControlledRecord(Thing):
    """
    Element for which specific access control restrictions apply.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["AccessControlledRecord"]
    class_class_curie: ClassVar[str] = "anvil:AccessControlledRecord"
    class_name: ClassVar[str] = "AccessControlledRecord"
    class_model_uri: ClassVar[URIRef] = ANVIL.AccessControlledRecord

    id: Union[str, AccessControlledRecordId] = None
    has_access_policy: Optional[Union[str, AccessPolicyId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AccessControlledRecordId):
            self.id = AccessControlledRecordId(self.id)

        if self.has_access_policy is not None and not isinstance(self.has_access_policy, AccessPolicyId):
            self.has_access_policy = AccessPolicyId(self.has_access_policy)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subject(AccessControlledRecord):
    """
    This entity is the subject about which data or references are recorded. | This includes the idea of a human
    participant in a study, a cell line, an animal model, | or any other similar entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["participant/Subject"]
    class_class_curie: ClassVar[str] = "anvil:participant/Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = ANVIL.Subject

    id: Union[str, SubjectId] = None
    subject_type: Union[str, "EnumSubjectType"] = None
    organism_type: Optional[str] = None
    has_sample: Optional[Union[dict[Union[str, SampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()
    has_assertion: Optional[Union[dict[Union[str, SubjectAssertionId], Union[dict, "SubjectAssertion"]], list[Union[dict, "SubjectAssertion"]]]] = empty_dict()
    has_demographics: Optional[Union[dict, "Demographics"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubjectId):
            self.id = SubjectId(self.id)

        if self._is_empty(self.subject_type):
            self.MissingRequiredField("subject_type")
        if not isinstance(self.subject_type, EnumSubjectType):
            self.subject_type = EnumSubjectType(self.subject_type)

        if self.organism_type is not None and not isinstance(self.organism_type, str):
            self.organism_type = str(self.organism_type)

        self._normalize_inlined_as_dict(slot_name="has_sample", slot_type=Sample, key_name="id", keyed=True)

        self._normalize_inlined_as_dict(slot_name="has_assertion", slot_type=SubjectAssertion, key_name="id", keyed=True)

        if self.has_demographics is not None and not isinstance(self.has_demographics, Demographics):
            self.has_demographics = Demographics(**as_dict(self.has_demographics))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Demographics(AccessControlledRecord):
    """
    Basic participant demographics summary
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["participant/Demographics"]
    class_class_curie: ClassVar[str] = "anvil:participant/Demographics"
    class_name: ClassVar[str] = "Demographics"
    class_model_uri: ClassVar[URIRef] = ANVIL.Demographics

    id: Union[str, DemographicsId] = None
    sex: Union[str, "EnumSex"] = None
    sex_display: str = None
    race: Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]] = None
    race_display: str = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    ethnicity_display: str = None
    date_of_birth: Optional[int] = None
    date_of_birth_type: Optional[Union[str, "EnumDateOfBirthType"]] = None
    age_at_last_vital_status: Optional[float] = None
    vital_status: Optional[Union[str, "EnumVitalStatus"]] = None
    source_data: Optional[Union[Union[str, SourceDataId], list[Union[str, SourceDataId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DemographicsId):
            self.id = DemographicsId(self.id)

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, EnumSex):
            self.sex = EnumSex(self.sex)

        if self._is_empty(self.sex_display):
            self.MissingRequiredField("sex_display")
        if not isinstance(self.sex_display, str):
            self.sex_display = str(self.sex_display)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, list):
            self.race = [self.race] if self.race is not None else []
        self.race = [v if isinstance(v, EnumRace) else EnumRace(v) for v in self.race]

        if self._is_empty(self.race_display):
            self.MissingRequiredField("race_display")
        if not isinstance(self.race_display, str):
            self.race_display = str(self.race_display)

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EnumEthnicity):
            self.ethnicity = EnumEthnicity(self.ethnicity)

        if self._is_empty(self.ethnicity_display):
            self.MissingRequiredField("ethnicity_display")
        if not isinstance(self.ethnicity_display, str):
            self.ethnicity_display = str(self.ethnicity_display)

        if self.date_of_birth is not None and not isinstance(self.date_of_birth, int):
            self.date_of_birth = int(self.date_of_birth)

        if self.date_of_birth_type is not None and not isinstance(self.date_of_birth_type, EnumDateOfBirthType):
            self.date_of_birth_type = EnumDateOfBirthType(self.date_of_birth_type)

        if self.age_at_last_vital_status is not None and not isinstance(self.age_at_last_vital_status, float):
            self.age_at_last_vital_status = float(self.age_at_last_vital_status)

        if self.vital_status is not None and not isinstance(self.vital_status, EnumVitalStatus):
            self.vital_status = EnumVitalStatus(self.vital_status)

        if not isinstance(self.source_data, list):
            self.source_data = [self.source_data] if self.source_data is not None else []
        self.source_data = [v if isinstance(v, SourceDataId) else SourceDataId(v) for v in self.source_data]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(Thing):
    """
    Study Meta Data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["study/Study"]
    class_class_curie: ClassVar[str] = "anvil:study/Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = ANVIL.Study

    id: Union[str, StudyId] = None
    study_title: str = None
    parent_study_id: Optional[Union[str, StudyId]] = None
    funding_source: Optional[Union[str, list[str]]] = empty_list()
    principal_investigator: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.study_title):
            self.MissingRequiredField("study_title")
        if not isinstance(self.study_title, str):
            self.study_title = str(self.study_title)

        if self.parent_study_id is not None and not isinstance(self.parent_study_id, StudyId):
            self.parent_study_id = StudyId(self.parent_study_id)

        if not isinstance(self.funding_source, list):
            self.funding_source = [self.funding_source] if self.funding_source is not None else []
        self.funding_source = [v if isinstance(v, str) else str(v) for v in self.funding_source]

        if not isinstance(self.principal_investigator, list):
            self.principal_investigator = [self.principal_investigator] if self.principal_investigator is not None else []
        self.principal_investigator = [v if isinstance(v, str) else str(v) for v in self.principal_investigator]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectAssertion(AccessControlledRecord):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["condition_assertion/SubjectAssertion"]
    class_class_curie: ClassVar[str] = "anvil:condition_assertion/SubjectAssertion"
    class_name: ClassVar[str] = "SubjectAssertion"
    class_model_uri: ClassVar[URIRef] = ANVIL.SubjectAssertion

    id: Union[str, SubjectAssertionId] = None
    assertion_type: Optional[Union[str, "EnumAssertionType"]] = None
    age_at_assertion: Optional[float] = None
    age_at_event: Optional[float] = None
    age_at_resolution: Optional[float] = None
    code: Optional[Union[str, URIorCURIE]] = None
    display: Optional[str] = None
    value_code: Optional[Union[str, URIorCURIE]] = None
    value_display: Optional[str] = None
    value_number: Optional[float] = None
    value_units: Optional[Union[str, URIorCURIE]] = None
    value_units_display: Optional[str] = None
    source_data: Optional[Union[Union[str, SourceDataId], list[Union[str, SourceDataId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubjectAssertionId):
            self.id = SubjectAssertionId(self.id)

        if self.assertion_type is not None and not isinstance(self.assertion_type, EnumAssertionType):
            self.assertion_type = EnumAssertionType(self.assertion_type)

        if self.age_at_assertion is not None and not isinstance(self.age_at_assertion, float):
            self.age_at_assertion = float(self.age_at_assertion)

        if self.age_at_event is not None and not isinstance(self.age_at_event, float):
            self.age_at_event = float(self.age_at_event)

        if self.age_at_resolution is not None and not isinstance(self.age_at_resolution, float):
            self.age_at_resolution = float(self.age_at_resolution)

        if self.code is not None and not isinstance(self.code, URIorCURIE):
            self.code = URIorCURIE(self.code)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        if self.value_code is not None and not isinstance(self.value_code, URIorCURIE):
            self.value_code = URIorCURIE(self.value_code)

        if self.value_display is not None and not isinstance(self.value_display, str):
            self.value_display = str(self.value_display)

        if self.value_number is not None and not isinstance(self.value_number, float):
            self.value_number = float(self.value_number)

        if self.value_units is not None and not isinstance(self.value_units, URIorCURIE):
            self.value_units = URIorCURIE(self.value_units)

        if self.value_units_display is not None and not isinstance(self.value_units_display, str):
            self.value_units_display = str(self.value_units_display)

        if not isinstance(self.source_data, list):
            self.source_data = [self.source_data] if self.source_data is not None else []
        self.source_data = [v if isinstance(v, SourceDataId) else SourceDataId(v) for v in self.source_data]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataSource(Thing):
    """
    Query configuration for specifying a source from which data are pulled.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["condition_assertion/DataSource"]
    class_class_curie: ClassVar[str] = "anvil:condition_assertion/DataSource"
    class_name: ClassVar[str] = "DataSource"
    class_model_uri: ClassVar[URIRef] = ANVIL.DataSource

    id: Union[str, DataSourceId] = None
    snapshot_id: Optional[str] = None
    google_data_project: Optional[str] = None
    snapshot_dataset: Optional[str] = None
    table: Optional[str] = None
    parameterized_query: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataSourceId):
            self.id = DataSourceId(self.id)

        if self.snapshot_id is not None and not isinstance(self.snapshot_id, str):
            self.snapshot_id = str(self.snapshot_id)

        if self.google_data_project is not None and not isinstance(self.google_data_project, str):
            self.google_data_project = str(self.google_data_project)

        if self.snapshot_dataset is not None and not isinstance(self.snapshot_dataset, str):
            self.snapshot_dataset = str(self.snapshot_dataset)

        if self.table is not None and not isinstance(self.table, str):
            self.table = str(self.table)

        if self.parameterized_query is not None and not isinstance(self.parameterized_query, str):
            self.parameterized_query = str(self.parameterized_query)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SourceData(AccessControlledRecord):
    """
    Reference to submitted data used to generate harmonized data. Applying the query_parameter(s) to the
    data_source.parameterized_query should return the specific data of interest.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["condition_assertion/SourceData"]
    class_class_curie: ClassVar[str] = "anvil:condition_assertion/SourceData"
    class_name: ClassVar[str] = "SourceData"
    class_model_uri: ClassVar[URIRef] = ANVIL.SourceData

    id: Union[str, SourceDataId] = None
    data_source: Optional[Union[str, DataSourceId]] = None
    query_parameter: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SourceDataId):
            self.id = SourceDataId(self.id)

        if self.data_source is not None and not isinstance(self.data_source, DataSourceId):
            self.data_source = DataSourceId(self.data_source)

        if not isinstance(self.query_parameter, list):
            self.query_parameter = [self.query_parameter] if self.query_parameter is not None else []
        self.query_parameter = [v if isinstance(v, str) else str(v) for v in self.query_parameter]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AccessPolicy(Thing):
    """
    Describes the access required for a given element of data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["data-access-policy/AccessPolicy"]
    class_class_curie: ClassVar[str] = "anvil:data-access-policy/AccessPolicy"
    class_name: ClassVar[str] = "AccessPolicy"
    class_model_uri: ClassVar[URIRef] = ANVIL.AccessPolicy

    id: Union[str, AccessPolicyId] = None
    access_policy_code: Union[Union[str, "EnumAccessCode"], list[Union[str, "EnumAccessCode"]]] = None
    description: str = None
    data_access_type: Optional[Union[Union[str, "EnumAccessType"], list[Union[str, "EnumAccessType"]]]] = empty_list()
    disease_limitation: Optional[str] = None
    website: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AccessPolicyId):
            self.id = AccessPolicyId(self.id)

        if self._is_empty(self.access_policy_code):
            self.MissingRequiredField("access_policy_code")
        if not isinstance(self.access_policy_code, list):
            self.access_policy_code = [self.access_policy_code] if self.access_policy_code is not None else []
        self.access_policy_code = [v if isinstance(v, EnumAccessCode) else EnumAccessCode(v) for v in self.access_policy_code]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.data_access_type, list):
            self.data_access_type = [self.data_access_type] if self.data_access_type is not None else []
        self.data_access_type = [v if isinstance(v, EnumAccessType) else EnumAccessType(v) for v in self.data_access_type]

        if self.disease_limitation is not None and not isinstance(self.disease_limitation, str):
            self.disease_limitation = str(self.disease_limitation)

        if self.website is not None and not isinstance(self.website, str):
            self.website = str(self.website)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Family(AccessControlledRecord):
    """
    A group of individuals of some relation who are grouped together in the study.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["family/Family"]
    class_class_curie: ClassVar[str] = "anvil:family/Family"
    class_name: ClassVar[str] = "Family"
    class_model_uri: ClassVar[URIRef] = ANVIL.Family

    id: Union[str, FamilyId] = None
    family_members: Union[dict[Union[str, FamilyMemberId], Union[dict, "FamilyMember"]], list[Union[dict, "FamilyMember"]]] = empty_dict()
    family_type: Optional[Union[str, "EnumFamilyType"]] = None
    family_description: Optional[str] = None
    consanguinity: Optional[Union[str, "EnumConsanguinityAssertion"]] = None
    family_study_focus: Optional[str] = None
    family_relationships: Optional[Union[Union[str, FamilyRelationshipId], list[Union[str, FamilyRelationshipId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyId):
            self.id = FamilyId(self.id)

        if self._is_empty(self.family_members):
            self.MissingRequiredField("family_members")
        self._normalize_inlined_as_dict(slot_name="family_members", slot_type=FamilyMember, key_name="id", keyed=True)

        if self.family_type is not None and not isinstance(self.family_type, EnumFamilyType):
            self.family_type = EnumFamilyType(self.family_type)

        if self.family_description is not None and not isinstance(self.family_description, str):
            self.family_description = str(self.family_description)

        if self.consanguinity is not None and not isinstance(self.consanguinity, EnumConsanguinityAssertion):
            self.consanguinity = EnumConsanguinityAssertion(self.consanguinity)

        if self.family_study_focus is not None and not isinstance(self.family_study_focus, str):
            self.family_study_focus = str(self.family_study_focus)

        if not isinstance(self.family_relationships, list):
            self.family_relationships = [self.family_relationships] if self.family_relationships is not None else []
        self.family_relationships = [v if isinstance(v, FamilyRelationshipId) else FamilyRelationshipId(v) for v in self.family_relationships]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyRelationship(AccessControlledRecord):
    """
    A relationship between two Subjects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["family/FamilyRelationship"]
    class_class_curie: ClassVar[str] = "anvil:family/FamilyRelationship"
    class_name: ClassVar[str] = "FamilyRelationship"
    class_model_uri: ClassVar[URIRef] = ANVIL.FamilyRelationship

    id: Union[str, FamilyRelationshipId] = None
    family_member: Union[str, SubjectId] = None
    other_family_member: Union[str, SubjectId] = None
    relationship_code: Union[str, URIorCURIE] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyRelationshipId):
            self.id = FamilyRelationshipId(self.id)

        if self._is_empty(self.family_member):
            self.MissingRequiredField("family_member")
        if not isinstance(self.family_member, SubjectId):
            self.family_member = SubjectId(self.family_member)

        if self._is_empty(self.other_family_member):
            self.MissingRequiredField("other_family_member")
        if not isinstance(self.other_family_member, SubjectId):
            self.other_family_member = SubjectId(self.other_family_member)

        if self._is_empty(self.relationship_code):
            self.MissingRequiredField("relationship_code")
        if not isinstance(self.relationship_code, URIorCURIE):
            self.relationship_code = URIorCURIE(self.relationship_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyMember(AccessControlledRecord):
    """
    Designates a Subject as a member of a family with some specified role.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["family/FamilyMember"]
    class_class_curie: ClassVar[str] = "anvil:family/FamilyMember"
    class_name: ClassVar[str] = "FamilyMember"
    class_model_uri: ClassVar[URIRef] = ANVIL.FamilyMember

    id: Union[str, FamilyMemberId] = None
    family_member: Union[str, SubjectId] = None
    family_role: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyMemberId):
            self.id = FamilyMemberId(self.id)

        if self._is_empty(self.family_member):
            self.MissingRequiredField("family_member")
        if not isinstance(self.family_member, SubjectId):
            self.family_member = SubjectId(self.family_member)

        if self.family_role is not None and not isinstance(self.family_role, URIorCURIE):
            self.family_role = URIorCURIE(self.family_role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(AccessControlledRecord):
    """
    Biospecimen data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["sample/Sample"]
    class_class_curie: ClassVar[str] = "anvil:sample/Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = ANVIL.Sample

    id: Union[str, SampleId] = None
    sample_type: Union[str, URIorCURIE] = None
    biospecimen_collection: Optional[Union[dict, "BiospecimenCollection"]] = None
    parent_sample: Optional[Union[str, SampleId]] = None
    processing: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    availablity_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    storage_method: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    quantity_number: Optional[float] = None
    quantity_units: Optional[Union[str, URIorCURIE]] = None
    aliquots: Optional[Union[dict[Union[str, AliquotId], Union[dict, "Aliquot"]], list[Union[dict, "Aliquot"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, URIorCURIE):
            self.sample_type = URIorCURIE(self.sample_type)

        if self.biospecimen_collection is not None and not isinstance(self.biospecimen_collection, BiospecimenCollection):
            self.biospecimen_collection = BiospecimenCollection(**as_dict(self.biospecimen_collection))

        if self.parent_sample is not None and not isinstance(self.parent_sample, SampleId):
            self.parent_sample = SampleId(self.parent_sample)

        if not isinstance(self.processing, list):
            self.processing = [self.processing] if self.processing is not None else []
        self.processing = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.processing]

        if self.availablity_status is not None and not isinstance(self.availablity_status, EnumAvailabilityStatus):
            self.availablity_status = EnumAvailabilityStatus(self.availablity_status)

        if not isinstance(self.storage_method, list):
            self.storage_method = [self.storage_method] if self.storage_method is not None else []
        self.storage_method = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.storage_method]

        if self.quantity_number is not None and not isinstance(self.quantity_number, float):
            self.quantity_number = float(self.quantity_number)

        if self.quantity_units is not None and not isinstance(self.quantity_units, URIorCURIE):
            self.quantity_units = URIorCURIE(self.quantity_units)

        self._normalize_inlined_as_dict(slot_name="aliquots", slot_type=Aliquot, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiospecimenCollection(AccessControlledRecord):
    """
    Biospecimen Collection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["sample/BiospecimenCollection"]
    class_class_curie: ClassVar[str] = "anvil:sample/BiospecimenCollection"
    class_name: ClassVar[str] = "BiospecimenCollection"
    class_model_uri: ClassVar[URIRef] = ANVIL.BiospecimenCollection

    id: Union[str, BiospecimenCollectionId] = None
    age_at_collection: Optional[float] = None
    method: Optional[Union[str, "EnumSampleCollectionMethod"]] = None
    site: Optional[Union[str, "EnumSite"]] = None
    spatial_qualifier: Optional[Union[str, "EnumSpatialQualifiers"]] = None
    laterality: Optional[Union[str, "EnumLaterality"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiospecimenCollectionId):
            self.id = BiospecimenCollectionId(self.id)

        if self.age_at_collection is not None and not isinstance(self.age_at_collection, float):
            self.age_at_collection = float(self.age_at_collection)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aliquot(AccessControlledRecord):
    """
    Specific tubes or details of a Sample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["sample/Aliquot"]
    class_class_curie: ClassVar[str] = "anvil:sample/Aliquot"
    class_name: ClassVar[str] = "Aliquot"
    class_model_uri: ClassVar[URIRef] = ANVIL.Aliquot

    id: Union[str, AliquotId] = None
    availablity_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    quantity_number: Optional[float] = None
    quantity_units: Optional[Union[str, URIorCURIE]] = None
    concentration_number: Optional[float] = None
    concentration_unit: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AliquotId):
            self.id = AliquotId(self.id)

        if self.availablity_status is not None and not isinstance(self.availablity_status, EnumAvailabilityStatus):
            self.availablity_status = EnumAvailabilityStatus(self.availablity_status)

        if self.quantity_number is not None and not isinstance(self.quantity_number, float):
            self.quantity_number = float(self.quantity_number)

        if self.quantity_units is not None and not isinstance(self.quantity_units, URIorCURIE):
            self.quantity_units = URIorCURIE(self.quantity_units)

        if self.concentration_number is not None and not isinstance(self.concentration_number, float):
            self.concentration_number = float(self.concentration_number)

        if self.concentration_unit is not None and not isinstance(self.concentration_unit, URIorCURIE):
            self.concentration_unit = URIorCURIE(self.concentration_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class File(AccessControlledRecord):
    """
    File
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["file/File"]
    class_class_curie: ClassVar[str] = "anvil:file/File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = ANVIL.File

    id: Union[str, FileId] = None
    subject: Optional[Union[Union[str, SubjectId], list[Union[str, SubjectId]]]] = empty_list()
    sample: Optional[Union[Union[str, SampleId], list[Union[str, SampleId]]]] = empty_list()
    filename: Optional[str] = None
    format: Optional[Union[str, "EDAMFormats"]] = None
    data_type: Optional[Union[str, "EDAMDataTypes"]] = None
    size: Optional[int] = None
    drs_uri: Optional[Union[str, URIorCURIE]] = None
    file_metadata: Optional[Union[str, FileMetadataId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

        if not isinstance(self.subject, list):
            self.subject = [self.subject] if self.subject is not None else []
        self.subject = [v if isinstance(v, SubjectId) else SubjectId(v) for v in self.subject]

        if not isinstance(self.sample, list):
            self.sample = [self.sample] if self.sample is not None else []
        self.sample = [v if isinstance(v, SampleId) else SampleId(v) for v in self.sample]

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self.drs_uri is not None and not isinstance(self.drs_uri, URIorCURIE):
            self.drs_uri = URIorCURIE(self.drs_uri)

        if self.file_metadata is not None and not isinstance(self.file_metadata, FileMetadataId):
            self.file_metadata = FileMetadataId(self.file_metadata)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileMetadata(Thing):
    """
    Metadata about the contents of the file.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["file/FileMetadata"]
    class_class_curie: ClassVar[str] = "anvil:file/FileMetadata"
    class_name: ClassVar[str] = "FileMetadata"
    class_model_uri: ClassVar[URIRef] = ANVIL.FileMetadata

    id: Union[str, FileMetadataId] = None
    code: Optional[Union[str, URIorCURIE]] = None
    display: Optional[str] = None
    value_code: Optional[Union[str, URIorCURIE]] = None
    value_display: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileMetadataId):
            self.id = FileMetadataId(self.id)

        if self.code is not None and not isinstance(self.code, URIorCURIE):
            self.code = URIorCURIE(self.code)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        if self.value_code is not None and not isinstance(self.value_code, URIorCURIE):
            self.value_code = URIorCURIE(self.value_code)

        if self.value_display is not None and not isinstance(self.value_display, str):
            self.value_display = str(self.value_display)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDateOfBirthType(EnumDefinitionImpl):
    """
    Privacy rules that may modify a date value.
    """
    exact = PermissibleValue(
        text="exact",
        title="Exact",
        description="Exact",
        meaning=IG_DOB_METHOD["exact"])
    year_only = PermissibleValue(
        text="year_only",
        title="Year Only",
        description="Year Only",
        meaning=IG_DOB_METHOD["year-only"])
    shifted = PermissibleValue(
        text="shifted",
        title="Shifted",
        description="Shifted",
        meaning=IG_DOB_METHOD["shifted"])
    decade_only = PermissibleValue(
        text="decade_only",
        title="Decade Only",
        description="Decade Only",
        meaning=IG_DOB_METHOD["decade-only"])
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Other",
        meaning=IG_DOB_METHOD["other"])

    _defn = EnumDefinition(
        name="EnumDateOfBirthType",
        description="Privacy rules that may modify a date value.",
    )

class EnumSex(EnumDefinitionImpl):
    """
    Terms describing an individual's sex.
    """
    female = PermissibleValue(
        text="female",
        title="Female",
        description="Female",
        meaning=ADMIN_GENDER["female"])
    male = PermissibleValue(
        text="male",
        title="Male",
        description="Male",
        meaning=ADMIN_GENDER["male"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        description="Unknown",
        meaning=ADMIN_GENDER["unknown"])
    intersex = PermissibleValue(
        text="intersex",
        title="Intersex",
        description="Intersex")

    _defn = EnumDefinition(
        name="EnumSex",
        description="Terms describing an individual's sex.",
    )

class EnumRace(EnumDefinitionImpl):
    """
    OMB Codes describing race.
    """
    american_indian_or_alaskan_native = PermissibleValue(
        text="american_indian_or_alaskan_native",
        title="American Indian or Alaskan Native",
        meaning=CDC_RACE_ETH["1002-5"])
    asian = PermissibleValue(
        text="asian",
        title="Asian",
        meaning=CDC_RACE_ETH["2028-9"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        title="Black or African American",
        meaning=CDC_RACE_ETH["2054-5"])
    native_hawaiian_or_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_pacific_islander",
        title="Native Hawaiian or Other Pacific Islander",
        meaning=CDC_RACE_ETH["2076-8"])
    white = PermissibleValue(
        text="white",
        title="White",
        meaning=CDC_RACE_ETH["2106-3"])
    other_race = PermissibleValue(
        text="other_race",
        title="Other Race",
        meaning=CDC_RACE_ETH["2131-1"])
    unknown = PermissibleValue(
        text="unknown",
        title="unknown",
        meaning=HL7_NULL["UNK"])
    asked_but_unknown = PermissibleValue(
        text="asked_but_unknown",
        title="asked but unknown",
        meaning=HL7_NULL["ASKU"])

    _defn = EnumDefinition(
        name="EnumRace",
        description="OMB Codes describing race.",
    )

class EnumEthnicity(EnumDefinitionImpl):
    """
    OMB Codes describing Hispanic or Latino ethnicity.
    """
    hispanic_or_latino = PermissibleValue(
        text="hispanic_or_latino",
        description="Hispanic or Latino",
        meaning=CDC_RACE_ETH["2135-2"])
    not_hispanic_or_latino = PermissibleValue(
        text="not_hispanic_or_latino",
        description="Not Hispanic or Latino",
        meaning=CDC_RACE_ETH["2186-5"])
    unknown = PermissibleValue(
        text="unknown",
        description="unknown",
        meaning=HL7_NULL["UNK"])
    asked_but_unknown = PermissibleValue(
        text="asked_but_unknown",
        description="asked but unknown",
        meaning=HL7_NULL["ASKU"])

    _defn = EnumDefinition(
        name="EnumEthnicity",
        description="OMB Codes describing Hispanic or Latino ethnicity.",
    )

class EnumSubjectType(EnumDefinitionImpl):
    """
    Types of entities
    """
    participant = PermissibleValue(
        text="participant",
        description="Study participant with consent, assent, or waiver of consent.")
    non_participant = PermissibleValue(
        text="non_participant",
        description="""An individual associated with a study who was not explictly consented, eg, the subject | of a reported family history.""")
    cell_line = PermissibleValue(
        text="cell_line",
        description="Cell Line")
    animal_model = PermissibleValue(
        text="animal_model",
        description="Animal model")
    group = PermissibleValue(
        text="group",
        description="A group of individuals or entities.")
    other = PermissibleValue(
        text="other",
        description="A different entity type- ideally this will be resolved!")

    _defn = EnumDefinition(
        name="EnumSubjectType",
        description="Types of entities",
    )

class EnumVitalStatus(EnumDefinitionImpl):
    """
    Is the entity living?
    """
    alive = PermissibleValue(
        text="alive",
        description="Alive")
    dead = PermissibleValue(
        text="dead",
        description="Dead")
    not_reported = PermissibleValue(
        text="not_reported",
        description="Not Reported")
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown")
    unspecified = PermissibleValue(
        text="unspecified",
        description="Unspecified")

    _defn = EnumDefinition(
        name="EnumVitalStatus",
        description="Is the entity living?",
    )

class EnumAssertionType(EnumDefinitionImpl):
    """
    Provides options to describe the expressed semantics of a condition.
    """
    phenotypic_feature = PermissibleValue(
        text="phenotypic_feature",
        title="Phenotypic Feature",
        description="This is a phenotypic feature",
        meaning=IGCONDTYPE["Phenotypic-Feature"])
    disease = PermissibleValue(
        text="disease",
        title="disease",
        description="Disease",
        meaning=IGCONDTYPE["Disease"])
    comorbidity = PermissibleValue(
        text="comorbidity",
        title="comorbidity",
        description="Comorbidity",
        meaning=IGCONDTYPE["Comorbidity"])
    histology = PermissibleValue(
        text="histology",
        title="histology",
        description="Histology",
        meaning=IGCONDTYPE["Histology"])
    clinical_finding = PermissibleValue(
        text="clinical_finding",
        title="clinical-finding",
        description="Clinical Finding",
        meaning=IGCONDTYPE["Clinical-Finding"])
    ehr_billing_code = PermissibleValue(
        text="ehr_billing_code",
        title="EHR Billing Code",
        description="From an EHR billing record, which may indicate only investigation into a possible diagnosis.")
    measurement = PermissibleValue(
        text="measurement",
        title="Measurement",
        description="A measurement of some feature, eg, height or glucose.")

    _defn = EnumDefinition(
        name="EnumAssertionType",
        description="Provides options to describe the expressed semantics of a condition.",
    )

class EnumConditionAssertion(EnumDefinitionImpl):
    """
    Enumerations for Condition Assertion
    """
    present = PermissibleValue(
        text="present",
        title="Present",
        description="Present")
    absent = PermissibleValue(
        text="absent",
        title="Absent",
        description="Absent")
    unsure = PermissibleValue(
        text="unsure",
        title="Unsure",
        description="Unsure")
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        description="Unknown")

    _defn = EnumDefinition(
        name="EnumConditionAssertion",
        description="Enumerations for Condition Assertion",
    )

class EnumConditionCode(EnumDefinitionImpl):
    """
    Recommended ontologies include: SNOMED_CT, HP, OMIM and ORPHA, prefixed with those curies
    * SNOMED : https://bioregistry.io/registry/snomedct
    * HP : https://bioregistry.io/registry/hp
    * OMIM : https://bioregistry.io/registry/omim
    * ORPHA : https://bioregistry.io/registry/orphanet
    """
    _defn = EnumDefinition(
        name="EnumConditionCode",
        description="""Recommended ontologies include: SNOMED_CT, HP, OMIM and ORPHA, prefixed with those curies
* SNOMED : https://bioregistry.io/registry/snomedct
* HP : https://bioregistry.io/registry/hp
* OMIM : https://bioregistry.io/registry/omim
* ORPHA : https://bioregistry.io/registry/orphanet""",
    )

class EnumAccessType(EnumDefinitionImpl):
    """
    Type of access controls applied
    """
    open = PermissibleValue(
        text="open",
        title="open",
        description="Open Access",
        meaning=IG2DAT["open"])
    registered = PermissibleValue(
        text="registered",
        title="registered",
        description="Registered Access",
        meaning=IG2DAT["registered"])
    controlled = PermissibleValue(
        text="controlled",
        title="controlled",
        description="Controlled",
        meaning=IG2DAT["controlled"])
    gsr_restricted = PermissibleValue(
        text="gsr_restricted",
        title="gsr_restricted",
        description="GSR Restricted",
        meaning=IG2DAT["gsr-restricted"])
    gsr_allowed = PermissibleValue(
        text="gsr_allowed",
        title="gsr_allowed",
        description="GSR Allowed",
        meaning=IG2DAT["gsr-allowed"])

    _defn = EnumDefinition(
        name="EnumAccessType",
        description="Type of access controls applied",
    )

class EnumAccessCode(EnumDefinitionImpl):
    """
    Type of research use case allowed
    """
    gru = PermissibleValue(
        text="gru",
        title="GRU",
        description="General Research Use",
        meaning=IG2DAC["GRU"])
    hmb = PermissibleValue(
        text="hmb",
        title="HMB",
        description="Health/Medical/Biomedical",
        meaning=IG2DAC["HMB"])
    ds = PermissibleValue(
        text="ds",
        title="DS",
        description="Disease-Specific (Disease/Trait/Exposure)",
        meaning=IG2DAC["DS"])
    irb = PermissibleValue(
        text="irb",
        title="IRB",
        description="IRB Approval Required",
        meaning=IG2DAC["IRB"])
    pub = PermissibleValue(
        text="pub",
        title="PUB",
        description="Publication Required",
        meaning=IG2DAC["PUB"])
    col = PermissibleValue(
        text="col",
        title="COL",
        description="Collaboration Required",
        meaning=IG2DAC["COL"])
    npu = PermissibleValue(
        text="npu",
        title="NPU",
        description="Not-for-profit use only",
        meaning=IG2DAC["NPU"])
    mds = PermissibleValue(
        text="mds",
        title="MDS",
        description="Methods",
        meaning=IG2DAC["MDS"])
    gso = PermissibleValue(
        text="gso",
        title="GSO",
        description="Genetic Studies only",
        meaning=IG2DAC["GSO"])
    gsr = PermissibleValue(
        text="gsr",
        title="GSR",
        description="Genomic Summary Results",
        meaning=IG2DAC["GSR"])
    rd = PermissibleValue(
        text="rd",
        title="RD",
        description="Related Diseases")

    _defn = EnumDefinition(
        name="EnumAccessCode",
        description="Type of research use case allowed",
    )

class EnumFamilyType(EnumDefinitionImpl):
    """
    Enumerations describing research family type
    """
    control_only = PermissibleValue(
        text="control_only",
        title="Control-only",
        description="Control Only")
    duo = PermissibleValue(
        text="duo",
        title="Duo",
        description="Duo")
    proband_only = PermissibleValue(
        text="proband_only",
        title="Proband-only",
        description="Proband Only")
    trio = PermissibleValue(
        text="trio",
        title="Trio",
        description="Trio (2 parents and affected child)")
    trio_plus = PermissibleValue(
        text="trio_plus",
        title="Trio+",
        description="2 Parents and 2 or more children")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Other")

    _defn = EnumDefinition(
        name="EnumFamilyType",
        description="Enumerations describing research family type",
    )

class EnumConsanguinityAssertion(EnumDefinitionImpl):
    """
    Asserts known or suspected consanguinity in this study family
    """
    not_suspected = PermissibleValue(
        text="not_suspected",
        title="not-suspected",
        description="Not suspected",
        meaning=SNOMED_CT["428263003"])
    suspected = PermissibleValue(
        text="suspected",
        title="suspected",
        description="Suspected",
        meaning=SNOMED_CT["415684004"])
    known_present = PermissibleValue(
        text="known_present",
        title="known-present",
        description="Known Present",
        meaning=SNOMED_CT["410515003"])
    unknown = PermissibleValue(
        text="unknown",
        title="unknown",
        description="Unknown",
        meaning=SNOMED_CT["261665006"])

    _defn = EnumDefinition(
        name="EnumConsanguinityAssertion",
        description="Asserts known or suspected consanguinity in this study family",
    )

class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the Thing available for use?
    """
    available = PermissibleValue(
        text="available",
        title="Available",
        description="Biospecimen is Available",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        title="Unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the Thing available for use?",
    )

class EnumSampleCollectionMethod(EnumDefinitionImpl):
    """
    The approach used to collect the biospecimen. Recommend ontology: [LOINC](https://loinc.org).
    """
    _defn = EnumDefinition(
        name="EnumSampleCollectionMethod",
        description="""The approach used to collect the biospecimen. Recommend ontology: [LOINC](https://loinc.org).""",
    )

class EnumSite(EnumDefinitionImpl):
    """
    The location of the specimen collection. Recommended ontology: [SNOMED Body
    Site](https://hl7.org/fhir/R4B/valueset-body-site.html)
    """
    _defn = EnumDefinition(
        name="EnumSite",
        description="""The location of the specimen collection. Recommended ontology: [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html)""",
    )

class EnumSpatialQualifiers(EnumDefinitionImpl):
    """
    Any spatial/location qualifiers.
    """
    _defn = EnumDefinition(
        name="EnumSpatialQualifiers",
        description="""Any spatial/location qualifiers.""",
    )

class EnumLaterality(EnumDefinitionImpl):
    """
    Laterality information for the site
    """
    _defn = EnumDefinition(
        name="EnumLaterality",
        description="""Laterality information for the site""",
    )

class EDAMFormats(EnumDefinitionImpl):
    """
    Data formats from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EDAMFormats",
        description="Data formats from the EDAM ontology.",
    )

class EDAMDataTypes(EnumDefinitionImpl):
    """
    Data types from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EDAMDataTypes",
        description="Data types from the EDAM ontology.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=ANVIL.id, name="id", curie=ANVIL.curie('id'),
                   model_uri=ANVIL.id, domain=None, range=URIRef)

slots.external_id = Slot(uri=ANVIL.external_id, name="external_id", curie=ANVIL.curie('external_id'),
                   model_uri=ANVIL.external_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.in_study = Slot(uri=ANVIL['participant/in_study'], name="in_study", curie=ANVIL.curie('participant/in_study'),
                   model_uri=ANVIL.in_study, domain=None, range=Optional[Union[str, StudyId]])

slots.organism_type = Slot(uri=ANVIL['participant/organism_type'], name="organism_type", curie=ANVIL.curie('participant/organism_type'),
                   model_uri=ANVIL.organism_type, domain=None, range=Optional[str])

slots.subject_type = Slot(uri=ANVIL['participant/subject_type'], name="subject_type", curie=ANVIL.curie('participant/subject_type'),
                   model_uri=ANVIL.subject_type, domain=None, range=Union[str, "EnumSubjectType"])

slots.date_of_birth = Slot(uri=ANVIL['participant/date_of_birth'], name="date_of_birth", curie=ANVIL.curie('participant/date_of_birth'),
                   model_uri=ANVIL.date_of_birth, domain=None, range=Optional[int])

slots.date_of_birth_type = Slot(uri=ANVIL['participant/date_of_birth_type'], name="date_of_birth_type", curie=ANVIL.curie('participant/date_of_birth_type'),
                   model_uri=ANVIL.date_of_birth_type, domain=None, range=Optional[Union[str, "EnumDateOfBirthType"]])

slots.sex = Slot(uri=ANVIL['participant/sex'], name="sex", curie=ANVIL.curie('participant/sex'),
                   model_uri=ANVIL.sex, domain=None, range=Union[str, "EnumSex"])

slots.sex_display = Slot(uri=ANVIL['participant/sex_display'], name="sex_display", curie=ANVIL.curie('participant/sex_display'),
                   model_uri=ANVIL.sex_display, domain=None, range=str)

slots.race = Slot(uri=ANVIL['participant/race'], name="race", curie=ANVIL.curie('participant/race'),
                   model_uri=ANVIL.race, domain=None, range=Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]])

slots.race_display = Slot(uri=ANVIL['participant/race_display'], name="race_display", curie=ANVIL.curie('participant/race_display'),
                   model_uri=ANVIL.race_display, domain=None, range=str)

slots.ethnicity = Slot(uri=ANVIL['participant/ethnicity'], name="ethnicity", curie=ANVIL.curie('participant/ethnicity'),
                   model_uri=ANVIL.ethnicity, domain=None, range=Union[str, "EnumEthnicity"])

slots.ethnicity_display = Slot(uri=ANVIL['participant/ethnicity_display'], name="ethnicity_display", curie=ANVIL.curie('participant/ethnicity_display'),
                   model_uri=ANVIL.ethnicity_display, domain=None, range=str)

slots.age_at_last_vital_status = Slot(uri=ANVIL['participant/age_at_last_vital_status'], name="age_at_last_vital_status", curie=ANVIL.curie('participant/age_at_last_vital_status'),
                   model_uri=ANVIL.age_at_last_vital_status, domain=None, range=Optional[float])

slots.vital_status = Slot(uri=ANVIL['participant/vital_status'], name="vital_status", curie=ANVIL.curie('participant/vital_status'),
                   model_uri=ANVIL.vital_status, domain=None, range=Optional[Union[str, "EnumVitalStatus"]])

slots.has_sample = Slot(uri=ANVIL['participant/has_sample'], name="has_sample", curie=ANVIL.curie('participant/has_sample'),
                   model_uri=ANVIL.has_sample, domain=None, range=Optional[Union[dict[Union[str, SampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.has_assertion = Slot(uri=ANVIL['participant/has_assertion'], name="has_assertion", curie=ANVIL.curie('participant/has_assertion'),
                   model_uri=ANVIL.has_assertion, domain=None, range=Optional[Union[dict[Union[str, SubjectAssertionId], Union[dict, SubjectAssertion]], list[Union[dict, SubjectAssertion]]]])

slots.has_demographics = Slot(uri=ANVIL['participant/has_demographics'], name="has_demographics", curie=ANVIL.curie('participant/has_demographics'),
                   model_uri=ANVIL.has_demographics, domain=None, range=Optional[Union[dict, Demographics]])

slots.parent_study_id = Slot(uri=ANVIL['study/parent_study_id'], name="parent_study_id", curie=ANVIL.curie('study/parent_study_id'),
                   model_uri=ANVIL.parent_study_id, domain=None, range=Optional[Union[str, StudyId]])

slots.funding_source = Slot(uri=ANVIL['study/funding_source'], name="funding_source", curie=ANVIL.curie('study/funding_source'),
                   model_uri=ANVIL.funding_source, domain=None, range=Optional[Union[str, list[str]]])

slots.principal_investigator = Slot(uri=ANVIL['study/principal_investigator'], name="principal_investigator", curie=ANVIL.curie('study/principal_investigator'),
                   model_uri=ANVIL.principal_investigator, domain=None, range=Optional[Union[str, list[str]]])

slots.study_title = Slot(uri=ANVIL['study/study_title'], name="study_title", curie=ANVIL.curie('study/study_title'),
                   model_uri=ANVIL.study_title, domain=None, range=str)

slots.snapshot_id = Slot(uri=ANVIL['condition_assertion/snapshot_id'], name="snapshot_id", curie=ANVIL.curie('condition_assertion/snapshot_id'),
                   model_uri=ANVIL.snapshot_id, domain=None, range=Optional[str])

slots.google_data_project = Slot(uri=ANVIL['condition_assertion/google_data_project'], name="google_data_project", curie=ANVIL.curie('condition_assertion/google_data_project'),
                   model_uri=ANVIL.google_data_project, domain=None, range=Optional[str])

slots.snapshot_dataset = Slot(uri=ANVIL['condition_assertion/snapshot_dataset'], name="snapshot_dataset", curie=ANVIL.curie('condition_assertion/snapshot_dataset'),
                   model_uri=ANVIL.snapshot_dataset, domain=None, range=Optional[str])

slots.table = Slot(uri=ANVIL['condition_assertion/table'], name="table", curie=ANVIL.curie('condition_assertion/table'),
                   model_uri=ANVIL.table, domain=None, range=Optional[str])

slots.parameterized_query = Slot(uri=ANVIL['condition_assertion/parameterized_query'], name="parameterized_query", curie=ANVIL.curie('condition_assertion/parameterized_query'),
                   model_uri=ANVIL.parameterized_query, domain=None, range=Optional[str])

slots.data_source = Slot(uri=ANVIL['condition_assertion/data_source'], name="data_source", curie=ANVIL.curie('condition_assertion/data_source'),
                   model_uri=ANVIL.data_source, domain=None, range=Optional[Union[str, DataSourceId]])

slots.query_parameter = Slot(uri=ANVIL['condition_assertion/query_parameter'], name="query_parameter", curie=ANVIL.curie('condition_assertion/query_parameter'),
                   model_uri=ANVIL.query_parameter, domain=None, range=Optional[Union[str, list[str]]])

slots.assertion_type = Slot(uri=ANVIL['condition_assertion/assertion_type'], name="assertion_type", curie=ANVIL.curie('condition_assertion/assertion_type'),
                   model_uri=ANVIL.assertion_type, domain=None, range=Optional[Union[str, "EnumAssertionType"]])

slots.age_at_assertion = Slot(uri=ANVIL['condition_assertion/age_at_assertion'], name="age_at_assertion", curie=ANVIL.curie('condition_assertion/age_at_assertion'),
                   model_uri=ANVIL.age_at_assertion, domain=None, range=Optional[float])

slots.age_at_event = Slot(uri=ANVIL['condition_assertion/age_at_event'], name="age_at_event", curie=ANVIL.curie('condition_assertion/age_at_event'),
                   model_uri=ANVIL.age_at_event, domain=None, range=Optional[float])

slots.age_at_resolution = Slot(uri=ANVIL['condition_assertion/age_at_resolution'], name="age_at_resolution", curie=ANVIL.curie('condition_assertion/age_at_resolution'),
                   model_uri=ANVIL.age_at_resolution, domain=None, range=Optional[float])

slots.source_data = Slot(uri=ANVIL['condition_assertion/source_data'], name="source_data", curie=ANVIL.curie('condition_assertion/source_data'),
                   model_uri=ANVIL.source_data, domain=None, range=Optional[Union[Union[str, SourceDataId], list[Union[str, SourceDataId]]]])

slots.code = Slot(uri=ANVIL['condition_assertion/code'], name="code", curie=ANVIL.curie('condition_assertion/code'),
                   model_uri=ANVIL.code, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.display = Slot(uri=ANVIL['condition_assertion/display'], name="display", curie=ANVIL.curie('condition_assertion/display'),
                   model_uri=ANVIL.display, domain=None, range=Optional[str])

slots.value_code = Slot(uri=ANVIL['condition_assertion/value_code'], name="value_code", curie=ANVIL.curie('condition_assertion/value_code'),
                   model_uri=ANVIL.value_code, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.value_display = Slot(uri=ANVIL['condition_assertion/value_display'], name="value_display", curie=ANVIL.curie('condition_assertion/value_display'),
                   model_uri=ANVIL.value_display, domain=None, range=Optional[str])

slots.value_number = Slot(uri=ANVIL['condition_assertion/value_number'], name="value_number", curie=ANVIL.curie('condition_assertion/value_number'),
                   model_uri=ANVIL.value_number, domain=None, range=Optional[float])

slots.value_units = Slot(uri=ANVIL['condition_assertion/value_units'], name="value_units", curie=ANVIL.curie('condition_assertion/value_units'),
                   model_uri=ANVIL.value_units, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.value_units_display = Slot(uri=ANVIL['condition_assertion/value_units_display'], name="value_units_display", curie=ANVIL.curie('condition_assertion/value_units_display'),
                   model_uri=ANVIL.value_units_display, domain=None, range=Optional[str])

slots.data_access_type = Slot(uri=ANVIL['data-access-policy/data_access_type'], name="data_access_type", curie=ANVIL.curie('data-access-policy/data_access_type'),
                   model_uri=ANVIL.data_access_type, domain=None, range=Optional[Union[Union[str, "EnumAccessType"], list[Union[str, "EnumAccessType"]]]])

slots.access_policy_code = Slot(uri=ANVIL['data-access-policy/access_policy_code'], name="access_policy_code", curie=ANVIL.curie('data-access-policy/access_policy_code'),
                   model_uri=ANVIL.access_policy_code, domain=None, range=Union[Union[str, "EnumAccessCode"], list[Union[str, "EnumAccessCode"]]])

slots.description = Slot(uri=ANVIL['data-access-policy/description'], name="description", curie=ANVIL.curie('data-access-policy/description'),
                   model_uri=ANVIL.description, domain=None, range=str)

slots.website = Slot(uri=ANVIL['data-access-policy/website'], name="website", curie=ANVIL.curie('data-access-policy/website'),
                   model_uri=ANVIL.website, domain=None, range=Optional[str])

slots.disease_limitation = Slot(uri=ANVIL['data-access-policy/disease_limitation'], name="disease_limitation", curie=ANVIL.curie('data-access-policy/disease_limitation'),
                   model_uri=ANVIL.disease_limitation, domain=None, range=Optional[str])

slots.has_access_policy = Slot(uri=ANVIL['data-access-policy/has_access_policy'], name="has_access_policy", curie=ANVIL.curie('data-access-policy/has_access_policy'),
                   model_uri=ANVIL.has_access_policy, domain=None, range=Optional[Union[str, AccessPolicyId]])

slots.family_type = Slot(uri=ANVIL['family/family_type'], name="family_type", curie=ANVIL.curie('family/family_type'),
                   model_uri=ANVIL.family_type, domain=None, range=Optional[Union[str, "EnumFamilyType"]])

slots.family_description = Slot(uri=ANVIL['family/family_description'], name="family_description", curie=ANVIL.curie('family/family_description'),
                   model_uri=ANVIL.family_description, domain=None, range=Optional[str])

slots.consanguinity = Slot(uri=ANVIL['family/consanguinity'], name="consanguinity", curie=ANVIL.curie('family/consanguinity'),
                   model_uri=ANVIL.consanguinity, domain=None, range=Optional[Union[str, "EnumConsanguinityAssertion"]])

slots.family_study_focus = Slot(uri=ANVIL['family/family_study_focus'], name="family_study_focus", curie=ANVIL.curie('family/family_study_focus'),
                   model_uri=ANVIL.family_study_focus, domain=None, range=Optional[str])

slots.family_member = Slot(uri=ANVIL['family/family_member'], name="family_member", curie=ANVIL.curie('family/family_member'),
                   model_uri=ANVIL.family_member, domain=None, range=Union[str, SubjectId])

slots.other_family_member = Slot(uri=ANVIL['family/other_family_member'], name="other_family_member", curie=ANVIL.curie('family/other_family_member'),
                   model_uri=ANVIL.other_family_member, domain=None, range=Union[str, SubjectId])

slots.family_relationships = Slot(uri=ANVIL['family/family_relationships'], name="family_relationships", curie=ANVIL.curie('family/family_relationships'),
                   model_uri=ANVIL.family_relationships, domain=None, range=Optional[Union[Union[str, FamilyRelationshipId], list[Union[str, FamilyRelationshipId]]]])

slots.family_members = Slot(uri=ANVIL['family/family_members'], name="family_members", curie=ANVIL.curie('family/family_members'),
                   model_uri=ANVIL.family_members, domain=None, range=Union[dict[Union[str, FamilyMemberId], Union[dict, FamilyMember]], list[Union[dict, FamilyMember]]])

slots.relationship_code = Slot(uri=ANVIL['family/relationship_code'], name="relationship_code", curie=ANVIL.curie('family/relationship_code'),
                   model_uri=ANVIL.relationship_code, domain=None, range=Union[str, URIorCURIE])

slots.family_role = Slot(uri=ANVIL['family/family_role'], name="family_role", curie=ANVIL.curie('family/family_role'),
                   model_uri=ANVIL.family_role, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.parent_sample = Slot(uri=ANVIL['sample/parent_sample'], name="parent_sample", curie=ANVIL.curie('sample/parent_sample'),
                   model_uri=ANVIL.parent_sample, domain=None, range=Optional[Union[str, SampleId]])

slots.biospecimen_collection = Slot(uri=ANVIL['sample/biospecimen_collection'], name="biospecimen_collection", curie=ANVIL.curie('sample/biospecimen_collection'),
                   model_uri=ANVIL.biospecimen_collection, domain=None, range=Optional[Union[dict, BiospecimenCollection]])

slots.aliquots = Slot(uri=ANVIL['sample/aliquots'], name="aliquots", curie=ANVIL.curie('sample/aliquots'),
                   model_uri=ANVIL.aliquots, domain=None, range=Optional[Union[dict[Union[str, AliquotId], Union[dict, Aliquot]], list[Union[dict, Aliquot]]]])

slots.sample_type = Slot(uri=ANVIL['sample/sample_type'], name="sample_type", curie=ANVIL.curie('sample/sample_type'),
                   model_uri=ANVIL.sample_type, domain=None, range=Union[str, URIorCURIE])

slots.processing = Slot(uri=ANVIL['sample/processing'], name="processing", curie=ANVIL.curie('sample/processing'),
                   model_uri=ANVIL.processing, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.availablity_status = Slot(uri=ANVIL['sample/availablity_status'], name="availablity_status", curie=ANVIL.curie('sample/availablity_status'),
                   model_uri=ANVIL.availablity_status, domain=None, range=Optional[Union[str, "EnumAvailabilityStatus"]])

slots.storage_method = Slot(uri=ANVIL['sample/storage_method'], name="storage_method", curie=ANVIL.curie('sample/storage_method'),
                   model_uri=ANVIL.storage_method, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.quantity_number = Slot(uri=ANVIL['sample/quantity_number'], name="quantity_number", curie=ANVIL.curie('sample/quantity_number'),
                   model_uri=ANVIL.quantity_number, domain=None, range=Optional[float])

slots.quantity_units = Slot(uri=ANVIL['sample/quantity_units'], name="quantity_units", curie=ANVIL.curie('sample/quantity_units'),
                   model_uri=ANVIL.quantity_units, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.concentration_number = Slot(uri=ANVIL['sample/concentration_number'], name="concentration_number", curie=ANVIL.curie('sample/concentration_number'),
                   model_uri=ANVIL.concentration_number, domain=None, range=Optional[float])

slots.concentration_unit = Slot(uri=ANVIL['sample/concentration_unit'], name="concentration_unit", curie=ANVIL.curie('sample/concentration_unit'),
                   model_uri=ANVIL.concentration_unit, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.age_at_collection = Slot(uri=ANVIL['sample/age_at_collection'], name="age_at_collection", curie=ANVIL.curie('sample/age_at_collection'),
                   model_uri=ANVIL.age_at_collection, domain=None, range=Optional[float])

slots.method = Slot(uri=ANVIL['sample/method'], name="method", curie=ANVIL.curie('sample/method'),
                   model_uri=ANVIL.method, domain=None, range=Optional[Union[str, "EnumSampleCollectionMethod"]])

slots.site = Slot(uri=ANVIL['sample/site'], name="site", curie=ANVIL.curie('sample/site'),
                   model_uri=ANVIL.site, domain=None, range=Optional[Union[str, "EnumSite"]])

slots.spatial_qualifier = Slot(uri=ANVIL['sample/spatial_qualifier'], name="spatial_qualifier", curie=ANVIL.curie('sample/spatial_qualifier'),
                   model_uri=ANVIL.spatial_qualifier, domain=None, range=Optional[Union[str, "EnumSpatialQualifiers"]])

slots.laterality = Slot(uri=ANVIL['sample/laterality'], name="laterality", curie=ANVIL.curie('sample/laterality'),
                   model_uri=ANVIL.laterality, domain=None, range=Optional[Union[str, "EnumLaterality"]])

slots.subject = Slot(uri=ANVIL['file/subject'], name="subject", curie=ANVIL.curie('file/subject'),
                   model_uri=ANVIL.subject, domain=None, range=Optional[Union[Union[str, SubjectId], list[Union[str, SubjectId]]]])

slots.sample = Slot(uri=ANVIL['file/sample'], name="sample", curie=ANVIL.curie('file/sample'),
                   model_uri=ANVIL.sample, domain=None, range=Optional[Union[Union[str, SampleId], list[Union[str, SampleId]]]])

slots.filename = Slot(uri=ANVIL['file/filename'], name="filename", curie=ANVIL.curie('file/filename'),
                   model_uri=ANVIL.filename, domain=None, range=Optional[str])

slots.format = Slot(uri=ANVIL['file/format'], name="format", curie=ANVIL.curie('file/format'),
                   model_uri=ANVIL.format, domain=None, range=Optional[Union[str, "EDAMFormats"]])

slots.data_type = Slot(uri=ANVIL['file/data_type'], name="data_type", curie=ANVIL.curie('file/data_type'),
                   model_uri=ANVIL.data_type, domain=None, range=Optional[Union[str, "EDAMDataTypes"]])

slots.size = Slot(uri=ANVIL['file/size'], name="size", curie=ANVIL.curie('file/size'),
                   model_uri=ANVIL.size, domain=None, range=Optional[int])

slots.drs_uri = Slot(uri=ANVIL['file/drs_uri'], name="drs_uri", curie=ANVIL.curie('file/drs_uri'),
                   model_uri=ANVIL.drs_uri, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.file_metadata = Slot(uri=ANVIL['file/file_metadata'], name="file_metadata", curie=ANVIL.curie('file/file_metadata'),
                   model_uri=ANVIL.file_metadata, domain=None, range=Optional[Union[str, FileMetadataId]])
