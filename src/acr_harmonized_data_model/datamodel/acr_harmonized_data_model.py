# Auto generated from acr_harmonized_data_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-03-18T08:51:28
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
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
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

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

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


class SourceDataId(AccessControlledRecordId):
    pass


class AccessPolicyId(ThingId):
    pass


class SampleId(ThingId):
    pass


@dataclass(repr=False)
class Thing(YAMLRoot):
    """
    Highest Level Class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["core/Thing"]
    class_class_curie: ClassVar[str] = "anvil:core/Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = ANVIL.Thing

    id: Union[str, ThingId] = None
    external_id: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["core/AccessControlledRecord"]
    class_class_curie: ClassVar[str] = "anvil:core/AccessControlledRecord"
    class_name: ClassVar[str] = "AccessControlledRecord"
    class_model_uri: ClassVar[URIRef] = ANVIL.AccessControlledRecord

    id: Union[str, AccessControlledRecordId] = None
    has_access_policy: Optional[Union[str, AccessPolicyId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["participant/Subject"]
    class_class_curie: ClassVar[str] = "anvil:participant/Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = ANVIL.Subject

    id: Union[str, SubjectId] = None
    subject_type: Union[str, "EnumSubjectType"] = None
    organism_type: Optional[str] = None
    has_sample: Optional[Union[Dict[Union[str, SampleId], Union[dict, "Sample"]], List[Union[dict, "Sample"]]]] = empty_dict()
    has_assertion: Optional[Union[Dict[Union[str, SubjectAssertionId], Union[dict, "SubjectAssertion"]], List[Union[dict, "SubjectAssertion"]]]] = empty_dict()
    has_demographics: Optional[Union[dict, "Demographics"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["participant/Demographics"]
    class_class_curie: ClassVar[str] = "anvil:participant/Demographics"
    class_name: ClassVar[str] = "Demographics"
    class_model_uri: ClassVar[URIRef] = ANVIL.Demographics

    id: Union[str, DemographicsId] = None
    sex: Union[str, "EnumSex"] = None
    sex_display: str = None
    race: Union[Union[str, "EnumRace"], List[Union[str, "EnumRace"]]] = None
    race_display: str = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    ethnicity_display: str = None
    date_of_birth: Optional[int] = None
    date_of_birth_type: Optional[Union[str, "EnumDateOfBirthType"]] = None
    age_at_last_vital_status: Optional[int] = None
    vital_status: Optional[Union[str, "EnumVitalStatus"]] = None
    source_data: Optional[Union[Union[str, SourceDataId], List[Union[str, SourceDataId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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

        if self.age_at_last_vital_status is not None and not isinstance(self.age_at_last_vital_status, int):
            self.age_at_last_vital_status = int(self.age_at_last_vital_status)

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
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["study/Study"]
    class_class_curie: ClassVar[str] = "anvil:study/Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = ANVIL.Study

    id: Union[str, StudyId] = None
    study_title: str = None
    external_study_id: Optional[Union[str, List[str]]] = empty_list()
    parent_study_id: Optional[Union[str, StudyId]] = None
    funding_source: Optional[Union[str, List[str]]] = empty_list()
    principal_investigator: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self._is_empty(self.study_title):
            self.MissingRequiredField("study_title")
        if not isinstance(self.study_title, str):
            self.study_title = str(self.study_title)

        if not isinstance(self.external_study_id, list):
            self.external_study_id = [self.external_study_id] if self.external_study_id is not None else []
        self.external_study_id = [v if isinstance(v, str) else str(v) for v in self.external_study_id]

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
    _inherited_slots: ClassVar[List[str]] = []

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
    source_data: Optional[Union[Union[str, SourceDataId], List[Union[str, SourceDataId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class SourceData(AccessControlledRecord):
    """
    Submitted data about a particular Subject.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["condition_assertion/SourceData"]
    class_class_curie: ClassVar[str] = "anvil:condition_assertion/SourceData"
    class_name: ClassVar[str] = "SourceData"
    class_model_uri: ClassVar[URIRef] = ANVIL.SourceData

    id: Union[str, SourceDataId] = None
    code: Optional[Union[str, URIorCURIE]] = None
    display: Optional[str] = None
    value_code: Optional[Union[str, URIorCURIE]] = None
    value_display: Optional[str] = None
    value_number: Optional[float] = None
    value_units: Optional[Union[str, URIorCURIE]] = None
    value_units_display: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SourceDataId):
            self.id = SourceDataId(self.id)

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AccessPolicy(Thing):
    """
    Describes the access required for a given element of data.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["data-access-policy/AccessPolicy"]
    class_class_curie: ClassVar[str] = "anvil:data-access-policy/AccessPolicy"
    class_name: ClassVar[str] = "AccessPolicy"
    class_model_uri: ClassVar[URIRef] = ANVIL.AccessPolicy

    id: Union[str, AccessPolicyId] = None
    access_policy_code: Union[Union[str, "EnumAccessCode"], List[Union[str, "EnumAccessCode"]]] = None
    description: str = None
    data_access_type: Optional[Union[Union[str, "EnumAccessType"], List[Union[str, "EnumAccessType"]]]] = empty_list()
    disease_limitation: Optional[str] = None
    website: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
class Sample(Thing):
    """
    Biospecimen data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["sample/Sample"]
    class_class_curie: ClassVar[str] = "anvil:sample/Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = ANVIL.Sample

    id: Union[str, SampleId] = None
    biospecimen_collection_id_fk: str = None
    sample_type: str = None
    parent_sample_id: Optional[str] = None
    processing: Optional[Union[str, List[str]]] = empty_list()
    availablity_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    storage_method: Optional[str] = None
    quantity: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self._is_empty(self.biospecimen_collection_id_fk):
            self.MissingRequiredField("biospecimen_collection_id_fk")
        if not isinstance(self.biospecimen_collection_id_fk, str):
            self.biospecimen_collection_id_fk = str(self.biospecimen_collection_id_fk)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, str):
            self.sample_type = str(self.sample_type)

        if self.parent_sample_id is not None and not isinstance(self.parent_sample_id, str):
            self.parent_sample_id = str(self.parent_sample_id)

        if not isinstance(self.processing, list):
            self.processing = [self.processing] if self.processing is not None else []
        self.processing = [v if isinstance(v, str) else str(v) for v in self.processing]

        if self.availablity_status is not None and not isinstance(self.availablity_status, EnumAvailabilityStatus):
            self.availablity_status = EnumAvailabilityStatus(self.availablity_status)

        if self.storage_method is not None and not isinstance(self.storage_method, str):
            self.storage_method = str(self.storage_method)

        if self.quantity is not None and not isinstance(self.quantity, str):
            self.quantity = str(self.quantity)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDateOfBirthType(EnumDefinitionImpl):
    """
    Privacy rules that may modify a date value.
    """
    exact = PermissibleValue(
        text="exact",
        description="Exact",
        meaning=IG_DOB_METHOD["exact"])
    year_only = PermissibleValue(
        text="year_only",
        description="Year Only",
        meaning=IG_DOB_METHOD["year-only"])
    shifted = PermissibleValue(
        text="shifted",
        description="Shifted",
        meaning=IG_DOB_METHOD["shifted"])
    decade_only = PermissibleValue(
        text="decade_only",
        description="Decade Only",
        meaning=IG_DOB_METHOD["decade-only"])
    other = PermissibleValue(
        text="other",
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
        description="Female",
        meaning=ADMIN_GENDER["female"])
    male = PermissibleValue(
        text="male",
        description="Male",
        meaning=ADMIN_GENDER["male"])
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown",
        meaning=ADMIN_GENDER["unknown"])
    intersex = PermissibleValue(
        text="intersex",
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
        meaning=CDC_RACE_ETH["1002-5"])
    asian = PermissibleValue(
        text="asian",
        meaning=CDC_RACE_ETH["2028-9"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        meaning=CDC_RACE_ETH["2054-5"])
    native_hawaiian_or_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_pacific_islander",
        meaning=CDC_RACE_ETH["2076-8"])
    white = PermissibleValue(
        text="white",
        meaning=CDC_RACE_ETH["2106-3"])
    other_race = PermissibleValue(
        text="other_race",
        meaning=CDC_RACE_ETH["2131-1"])
    unknown = PermissibleValue(
        text="unknown",
        meaning=HL7_NULL["UNK"])
    asked_but_unknown = PermissibleValue(
        text="asked_but_unknown",
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
        description="This is a phenotypic feature",
        meaning=IGCONDTYPE["Phenotypic-Feature"])
    disease = PermissibleValue(
        text="disease",
        description="Disease",
        meaning=IGCONDTYPE["Disease"])
    comorbidity = PermissibleValue(
        text="comorbidity",
        description="Comorbidity",
        meaning=IGCONDTYPE["Comorbidity"])
    histology = PermissibleValue(
        text="histology",
        description="Histology",
        meaning=IGCONDTYPE["Histology"])
    clinical_finding = PermissibleValue(
        text="clinical_finding",
        description="Clinical Finding",
        meaning=IGCONDTYPE["Clinical-Finding"])
    ehr_billing_code = PermissibleValue(
        text="ehr_billing_code",
        description="From an EHR billing record, which may indicate only investigation into a possible diagnosis.")

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
        description="Present")
    absent = PermissibleValue(
        text="absent",
        description="Absent")
    unsure = PermissibleValue(
        text="unsure",
        description="Unsure")
    unknown = PermissibleValue(
        text="unknown",
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
        description="Open Access",
        meaning=IG2DAT["open"])
    registered = PermissibleValue(
        text="registered",
        description="Registered Access",
        meaning=IG2DAT["registered"])
    controlled = PermissibleValue(
        text="controlled",
        description="Controlled",
        meaning=IG2DAT["controlled"])
    gsr_restricted = PermissibleValue(
        text="gsr_restricted",
        description="GSR Restricted",
        meaning=IG2DAT["gsr-restricted"])
    gsr_allowed = PermissibleValue(
        text="gsr_allowed",
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
        description="General Research Use",
        meaning=IG2DAC["GRU"])
    hmb = PermissibleValue(
        text="hmb",
        description="Health/Medical/Biomedical",
        meaning=IG2DAC["HMB"])
    ds = PermissibleValue(
        text="ds",
        description="Disease-Specific (Disease/Trait/Exposure)",
        meaning=IG2DAC["DS"])
    irb = PermissibleValue(
        text="irb",
        description="IRB Approval Required",
        meaning=IG2DAC["IRB"])
    pub = PermissibleValue(
        text="pub",
        description="Publication Required",
        meaning=IG2DAC["PUB"])
    col = PermissibleValue(
        text="col",
        description="Collaboration Required",
        meaning=IG2DAC["COL"])
    npu = PermissibleValue(
        text="npu",
        description="Not-for-profit use only",
        meaning=IG2DAC["NPU"])
    mds = PermissibleValue(
        text="mds",
        description="Methods",
        meaning=IG2DAC["MDS"])
    gso = PermissibleValue(
        text="gso",
        description="Genetic Studies only",
        meaning=IG2DAC["GSO"])
    gsr = PermissibleValue(
        text="gsr",
        description="Genomic Summary Results",
        meaning=IG2DAC["GSR"])

    _defn = EnumDefinition(
        name="EnumAccessCode",
        description="Type of research use case allowed",
    )

class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the Thing available for use?
    """
    available = PermissibleValue(
        text="available",
        description="Biospecimen is Available",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the Thing available for use?",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=ANVIL['core/id'], name="id", curie=ANVIL.curie('core/id'),
                   model_uri=ANVIL.id, domain=None, range=URIRef)

slots.external_id = Slot(uri=ANVIL['core/external_id'], name="external_id", curie=ANVIL.curie('core/external_id'),
                   model_uri=ANVIL.external_id, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

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
                   model_uri=ANVIL.race, domain=None, range=Union[Union[str, "EnumRace"], List[Union[str, "EnumRace"]]])

slots.race_display = Slot(uri=ANVIL['participant/race_display'], name="race_display", curie=ANVIL.curie('participant/race_display'),
                   model_uri=ANVIL.race_display, domain=None, range=str)

slots.ethnicity = Slot(uri=ANVIL['participant/ethnicity'], name="ethnicity", curie=ANVIL.curie('participant/ethnicity'),
                   model_uri=ANVIL.ethnicity, domain=None, range=Union[str, "EnumEthnicity"])

slots.ethnicity_display = Slot(uri=ANVIL['participant/ethnicity_display'], name="ethnicity_display", curie=ANVIL.curie('participant/ethnicity_display'),
                   model_uri=ANVIL.ethnicity_display, domain=None, range=str)

slots.age_at_last_vital_status = Slot(uri=ANVIL['participant/age_at_last_vital_status'], name="age_at_last_vital_status", curie=ANVIL.curie('participant/age_at_last_vital_status'),
                   model_uri=ANVIL.age_at_last_vital_status, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=ANVIL['participant/vital_status'], name="vital_status", curie=ANVIL.curie('participant/vital_status'),
                   model_uri=ANVIL.vital_status, domain=None, range=Optional[Union[str, "EnumVitalStatus"]])

slots.has_sample = Slot(uri=ANVIL['participant/has_sample'], name="has_sample", curie=ANVIL.curie('participant/has_sample'),
                   model_uri=ANVIL.has_sample, domain=None, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.has_assertion = Slot(uri=ANVIL['participant/has_assertion'], name="has_assertion", curie=ANVIL.curie('participant/has_assertion'),
                   model_uri=ANVIL.has_assertion, domain=None, range=Optional[Union[Dict[Union[str, SubjectAssertionId], Union[dict, SubjectAssertion]], List[Union[dict, SubjectAssertion]]]])

slots.has_demographics = Slot(uri=ANVIL['participant/has_demographics'], name="has_demographics", curie=ANVIL.curie('participant/has_demographics'),
                   model_uri=ANVIL.has_demographics, domain=None, range=Optional[Union[dict, Demographics]])

slots.external_study_id = Slot(uri=ANVIL['study/external_study_id'], name="external_study_id", curie=ANVIL.curie('study/external_study_id'),
                   model_uri=ANVIL.external_study_id, domain=None, range=Optional[Union[str, List[str]]])

slots.parent_study_id = Slot(uri=ANVIL['study/parent_study_id'], name="parent_study_id", curie=ANVIL.curie('study/parent_study_id'),
                   model_uri=ANVIL.parent_study_id, domain=None, range=Optional[Union[str, StudyId]])

slots.funding_source = Slot(uri=ANVIL['study/funding_source'], name="funding_source", curie=ANVIL.curie('study/funding_source'),
                   model_uri=ANVIL.funding_source, domain=None, range=Optional[Union[str, List[str]]])

slots.principal_investigator = Slot(uri=ANVIL['study/principal_investigator'], name="principal_investigator", curie=ANVIL.curie('study/principal_investigator'),
                   model_uri=ANVIL.principal_investigator, domain=None, range=Optional[Union[str, List[str]]])

slots.study_title = Slot(uri=ANVIL['study/study_title'], name="study_title", curie=ANVIL.curie('study/study_title'),
                   model_uri=ANVIL.study_title, domain=None, range=str)

slots.assertion_type = Slot(uri=ANVIL['condition_assertion/assertion_type'], name="assertion_type", curie=ANVIL.curie('condition_assertion/assertion_type'),
                   model_uri=ANVIL.assertion_type, domain=None, range=Optional[Union[str, "EnumAssertionType"]])

slots.age_at_assertion = Slot(uri=ANVIL['condition_assertion/age_at_assertion'], name="age_at_assertion", curie=ANVIL.curie('condition_assertion/age_at_assertion'),
                   model_uri=ANVIL.age_at_assertion, domain=None, range=Optional[float])

slots.age_at_event = Slot(uri=ANVIL['condition_assertion/age_at_event'], name="age_at_event", curie=ANVIL.curie('condition_assertion/age_at_event'),
                   model_uri=ANVIL.age_at_event, domain=None, range=Optional[float])

slots.age_at_resolution = Slot(uri=ANVIL['condition_assertion/age_at_resolution'], name="age_at_resolution", curie=ANVIL.curie('condition_assertion/age_at_resolution'),
                   model_uri=ANVIL.age_at_resolution, domain=None, range=Optional[float])

slots.source_data = Slot(uri=ANVIL['condition_assertion/source_data'], name="source_data", curie=ANVIL.curie('condition_assertion/source_data'),
                   model_uri=ANVIL.source_data, domain=None, range=Optional[Union[Union[str, SourceDataId], List[Union[str, SourceDataId]]]])

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
                   model_uri=ANVIL.data_access_type, domain=None, range=Optional[Union[Union[str, "EnumAccessType"], List[Union[str, "EnumAccessType"]]]])

slots.access_policy_code = Slot(uri=ANVIL['data-access-policy/access_policy_code'], name="access_policy_code", curie=ANVIL.curie('data-access-policy/access_policy_code'),
                   model_uri=ANVIL.access_policy_code, domain=None, range=Union[Union[str, "EnumAccessCode"], List[Union[str, "EnumAccessCode"]]])

slots.description = Slot(uri=ANVIL['data-access-policy/description'], name="description", curie=ANVIL.curie('data-access-policy/description'),
                   model_uri=ANVIL.description, domain=None, range=str)

slots.website = Slot(uri=ANVIL['data-access-policy/website'], name="website", curie=ANVIL.curie('data-access-policy/website'),
                   model_uri=ANVIL.website, domain=None, range=Optional[str])

slots.disease_limitation = Slot(uri=ANVIL['data-access-policy/disease_limitation'], name="disease_limitation", curie=ANVIL.curie('data-access-policy/disease_limitation'),
                   model_uri=ANVIL.disease_limitation, domain=None, range=Optional[str])

slots.has_access_policy = Slot(uri=ANVIL['data-access-policy/has_access_policy'], name="has_access_policy", curie=ANVIL.curie('data-access-policy/has_access_policy'),
                   model_uri=ANVIL.has_access_policy, domain=None, range=Optional[Union[str, AccessPolicyId]])

slots.parent_sample_id = Slot(uri=ANVIL['sample/parent_sample_id'], name="parent_sample_id", curie=ANVIL.curie('sample/parent_sample_id'),
                   model_uri=ANVIL.parent_sample_id, domain=None, range=Optional[str])

slots.biospecimen_collection_id_fk = Slot(uri=ANVIL['sample/biospecimen_collection_id_fk'], name="biospecimen_collection_id_fk", curie=ANVIL.curie('sample/biospecimen_collection_id_fk'),
                   model_uri=ANVIL.biospecimen_collection_id_fk, domain=None, range=str)

slots.sample_type = Slot(uri=ANVIL['sample/sample_type'], name="sample_type", curie=ANVIL.curie('sample/sample_type'),
                   model_uri=ANVIL.sample_type, domain=None, range=str)

slots.processing = Slot(uri=ANVIL['sample/processing'], name="processing", curie=ANVIL.curie('sample/processing'),
                   model_uri=ANVIL.processing, domain=None, range=Optional[Union[str, List[str]]])

slots.availablity_status = Slot(uri=ANVIL['sample/availablity_status'], name="availablity_status", curie=ANVIL.curie('sample/availablity_status'),
                   model_uri=ANVIL.availablity_status, domain=None, range=Optional[Union[str, "EnumAvailabilityStatus"]])

slots.storage_method = Slot(uri=ANVIL['sample/storage_method'], name="storage_method", curie=ANVIL.curie('sample/storage_method'),
                   model_uri=ANVIL.storage_method, domain=None, range=Optional[str])

slots.quantity = Slot(uri=ANVIL['sample/quantity'], name="quantity", curie=ANVIL.curie('sample/quantity'),
                   model_uri=ANVIL.quantity, domain=None, range=Optional[str])