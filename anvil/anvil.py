# Auto generated from anvil.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-02-28T13:16:16
# Schema: anvil-schema
#
# id: https://anvilproject.org/acr-harmonized-data-model
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

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
ANVIL = CurieNamespace('anvil', 'https://anvilproject.org/acr-harmonized-data-model/')
CDC_RACE_ETH = CurieNamespace('cdc_race_eth', 'urn:oid:2.16.840.1.113883.6.238')
HL7_NULL = CurieNamespace('hl7_null', 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = ANVIL


# Types

# Class references
class ThingId(extended_str):
    pass


class AccessControlledRecordId(ThingId):
    pass


class SubjectId(AccessControlledRecordId):
    pass


class ParticipantId(SubjectId):
    pass


class StudyId(ThingId):
    pass


class SubjectAssertionId(AccessControlledRecordId):
    pass


class SourceDataId(AccessControlledRecordId):
    pass


class AccessPolicyId(ThingId):
    pass


class BiospecimenCollectionId(ThingId):
    pass


class AliquotId(ThingId):
    pass


class SampleId(ThingId):
    pass


class MeasurementId(ThingId):
    pass


class ProcedureId(ThingId):
    pass


class FamilyId(ThingId):
    pass


class FamilyMemberId(ThingId):
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

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

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

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Participant(Subject):
    """
    Basic participant demographics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["participant/Participant"]
    class_class_curie: ClassVar[str] = "anvil:participant/Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = ANVIL.Participant

    id: Union[str, ParticipantId] = None
    subject_type: Union[str, "EnumSubjectType"] = None
    phenotypic_sex: Union[str, "EnumSex"] = None
    race: Union[str, "EnumRace"] = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    date_of_birth: Optional[int] = None
    date_of_birth_type: Optional[Union[str, "EnumDateOfBirthType"]] = None
    phenotypic_sex_source_value: Optional[str] = None
    race_source_value: Optional[str] = None
    ethnicity_source_value: Optional[str] = None
    age_at_last_vital_status: Optional[int] = None
    vital_status: Optional[Union[str, "EnumVitalStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParticipantId):
            self.id = ParticipantId(self.id)

        if self._is_empty(self.phenotypic_sex):
            self.MissingRequiredField("phenotypic_sex")
        if not isinstance(self.phenotypic_sex, EnumSex):
            self.phenotypic_sex = EnumSex(self.phenotypic_sex)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, EnumRace):
            self.race = EnumRace(self.race)

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EnumEthnicity):
            self.ethnicity = EnumEthnicity(self.ethnicity)

        if self.date_of_birth is not None and not isinstance(self.date_of_birth, int):
            self.date_of_birth = int(self.date_of_birth)

        if self.date_of_birth_type is not None and not isinstance(self.date_of_birth_type, EnumDateOfBirthType):
            self.date_of_birth_type = EnumDateOfBirthType(self.date_of_birth_type)

        if self.phenotypic_sex_source_value is not None and not isinstance(self.phenotypic_sex_source_value, str):
            self.phenotypic_sex_source_value = str(self.phenotypic_sex_source_value)

        if self.race_source_value is not None and not isinstance(self.race_source_value, str):
            self.race_source_value = str(self.race_source_value)

        if self.ethnicity_source_value is not None and not isinstance(self.ethnicity_source_value, str):
            self.ethnicity_source_value = str(self.ethnicity_source_value)

        if self.age_at_last_vital_status is not None and not isinstance(self.age_at_last_vital_status, int):
            self.age_at_last_vital_status = int(self.age_at_last_vital_status)

        if self.vital_status is not None and not isinstance(self.vital_status, EnumVitalStatus):
            self.vital_status = EnumVitalStatus(self.vital_status)

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
class BiospecimenCollection(Thing):
    """
    Biospecimen Collection
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["biospecimen_collection/BiospecimenCollection"]
    class_class_curie: ClassVar[str] = "anvil:biospecimen_collection/BiospecimenCollection"
    class_name: ClassVar[str] = "BiospecimenCollection"
    class_model_uri: ClassVar[URIRef] = ANVIL.BiospecimenCollection

    id: Union[str, BiospecimenCollectionId] = None
    age_at_collection: Optional[int] = None
    method: Optional[Union[str, "EnumSampleCollectionMethod"]] = None
    site: Optional[Union[str, "EnumSite"]] = None
    spatial_qualifier: Optional[Union[str, "EnumSpatialQualifiers"]] = None
    laterality: Optional[Union[str, "EnumLaterality"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiospecimenCollectionId):
            self.id = BiospecimenCollectionId(self.id)

        if self.age_at_collection is not None and not isinstance(self.age_at_collection, int):
            self.age_at_collection = int(self.age_at_collection)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aliquot(Thing):
    """
    Represent exact tubes or total amounts available of a Sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["aliquot/Aliquot"]
    class_class_curie: ClassVar[str] = "anvil:aliquot/Aliquot"
    class_name: ClassVar[str] = "Aliquot"
    class_model_uri: ClassVar[URIRef] = ANVIL.Aliquot

    id: Union[str, AliquotId] = None
    sample_id_fk: str = None
    sample_availability_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    sample_volume: Optional[float] = None
    sample_volume_unit: Optional[str] = None
    sample_concentration: Optional[float] = None
    sample_concentration_unit: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AliquotId):
            self.id = AliquotId(self.id)

        if self._is_empty(self.sample_id_fk):
            self.MissingRequiredField("sample_id_fk")
        if not isinstance(self.sample_id_fk, str):
            self.sample_id_fk = str(self.sample_id_fk)

        if self.sample_availability_status is not None and not isinstance(self.sample_availability_status, EnumAvailabilityStatus):
            self.sample_availability_status = EnumAvailabilityStatus(self.sample_availability_status)

        if self.sample_volume is not None and not isinstance(self.sample_volume, float):
            self.sample_volume = float(self.sample_volume)

        if self.sample_volume_unit is not None and not isinstance(self.sample_volume_unit, str):
            self.sample_volume_unit = str(self.sample_volume_unit)

        if self.sample_concentration is not None and not isinstance(self.sample_concentration, float):
            self.sample_concentration = float(self.sample_concentration)

        if self.sample_concentration_unit is not None and not isinstance(self.sample_concentration_unit, str):
            self.sample_concentration_unit = str(self.sample_concentration_unit)

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


@dataclass(repr=False)
class Measurement(Thing):
    """
    Measurements
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["measurement/Measurement"]
    class_class_curie: ClassVar[str] = "anvil:measurement/Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = ANVIL.Measurement

    id: Union[str, MeasurementId] = None
    measurement_code: Union[str, List[str]] = None
    measurement_unit: str = None
    measurement_source_value: str = None
    measurement_value_code: Optional[Union[str, "EnumMeasurementValueCode"]] = None
    age_at_observation: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementId):
            self.id = MeasurementId(self.id)

        if self._is_empty(self.measurement_code):
            self.MissingRequiredField("measurement_code")
        if not isinstance(self.measurement_code, list):
            self.measurement_code = [self.measurement_code] if self.measurement_code is not None else []
        self.measurement_code = [v if isinstance(v, str) else str(v) for v in self.measurement_code]

        if self._is_empty(self.measurement_unit):
            self.MissingRequiredField("measurement_unit")
        if not isinstance(self.measurement_unit, str):
            self.measurement_unit = str(self.measurement_unit)

        if self._is_empty(self.measurement_source_value):
            self.MissingRequiredField("measurement_source_value")
        if not isinstance(self.measurement_source_value, str):
            self.measurement_source_value = str(self.measurement_source_value)

        if self.measurement_value_code is not None and not isinstance(self.measurement_value_code, EnumMeasurementValueCode):
            self.measurement_value_code = EnumMeasurementValueCode(self.measurement_value_code)

        if self.age_at_observation is not None and not isinstance(self.age_at_observation, int):
            self.age_at_observation = int(self.age_at_observation)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Procedure(Thing):
    """
    Procedures
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["procedure/Procedure"]
    class_class_curie: ClassVar[str] = "anvil:procedure/Procedure"
    class_name: ClassVar[str] = "Procedure"
    class_model_uri: ClassVar[URIRef] = ANVIL.Procedure

    id: Union[str, ProcedureId] = None
    procedure_code: Union[str, List[str]] = None
    procedure_source_value: str = None
    age_at_event: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureId):
            self.id = ProcedureId(self.id)

        if self._is_empty(self.procedure_code):
            self.MissingRequiredField("procedure_code")
        if not isinstance(self.procedure_code, list):
            self.procedure_code = [self.procedure_code] if self.procedure_code is not None else []
        self.procedure_code = [v if isinstance(v, str) else str(v) for v in self.procedure_code]

        if self._is_empty(self.procedure_source_value):
            self.MissingRequiredField("procedure_source_value")
        if not isinstance(self.procedure_source_value, str):
            self.procedure_source_value = str(self.procedure_source_value)

        if self.age_at_event is not None and not isinstance(self.age_at_event, float):
            self.age_at_event = float(self.age_at_event)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Family(Thing):
    """
    Family
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["family/Family"]
    class_class_curie: ClassVar[str] = "anvil:family/Family"
    class_name: ClassVar[str] = "Family"
    class_model_uri: ClassVar[URIRef] = ANVIL.Family

    id: Union[str, FamilyId] = None
    family_external_id: Optional[Union[str, List[str]]] = empty_list()
    family_type: Optional[Union[str, "EnumFamilyType"]] = None
    family_description: Optional[str] = None
    consanguinity: Optional[Union[str, "EnumConsanguinityAssertion"]] = None
    family_study_focus: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyId):
            self.id = FamilyId(self.id)

        if not isinstance(self.family_external_id, list):
            self.family_external_id = [self.family_external_id] if self.family_external_id is not None else []
        self.family_external_id = [v if isinstance(v, str) else str(v) for v in self.family_external_id]

        if self.family_type is not None and not isinstance(self.family_type, EnumFamilyType):
            self.family_type = EnumFamilyType(self.family_type)

        if self.family_description is not None and not isinstance(self.family_description, str):
            self.family_description = str(self.family_description)

        if self.consanguinity is not None and not isinstance(self.consanguinity, EnumConsanguinityAssertion):
            self.consanguinity = EnumConsanguinityAssertion(self.consanguinity)

        if self.family_study_focus is not None and not isinstance(self.family_study_focus, str):
            self.family_study_focus = str(self.family_study_focus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyMember(Thing):
    """
    Family
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ANVIL["family-member/FamilyMember"]
    class_class_curie: ClassVar[str] = "anvil:family-member/FamilyMember"
    class_name: ClassVar[str] = "FamilyMember"
    class_model_uri: ClassVar[URIRef] = ANVIL.FamilyMember

    id: Union[str, FamilyMemberId] = None
    family_member_id: str = None
    family_id_fk: Optional[str] = None
    other_family_member_id: Optional[str] = None
    relationship_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FamilyMemberId):
            self.id = FamilyMemberId(self.id)

        if self._is_empty(self.family_member_id):
            self.MissingRequiredField("family_member_id")
        if not isinstance(self.family_member_id, str):
            self.family_member_id = str(self.family_member_id)

        if self.family_id_fk is not None and not isinstance(self.family_id_fk, str):
            self.family_id_fk = str(self.family_id_fk)

        if self.other_family_member_id is not None and not isinstance(self.other_family_member_id, str):
            self.other_family_member_id = str(self.other_family_member_id)

        if self.relationship_code is not None and not isinstance(self.relationship_code, str):
            self.relationship_code = str(self.relationship_code)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDateOfBirthType(EnumDefinitionImpl):
    """
    Privacy rules that may modify a date value.
    """
    exact = PermissibleValue(
        text="exact",
        description="Exact",
        meaning=IG-DOB-METHOD["exact"])
    year_only = PermissibleValue(
        text="year_only",
        description="Year Only",
        meaning=IG-DOB-METHOD["year-only"])
    shifted = PermissibleValue(
        text="shifted",
        description="Shifted",
        meaning=IG-DOB-METHOD["shifted"])
    decade_only = PermissibleValue(
        text="decade_only",
        description="Decade Only",
        meaning=IG-DOB-METHOD["decade-only"])
    other = PermissibleValue(
        text="other",
        description="Other",
        meaning=IG-DOB-METHOD["other"])

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
        description="American Indian or Alaskan Native",
        meaning=CDC_RACE_ETH["1002-5"])
    asian = PermissibleValue(
        text="asian",
        description="Asian",
        meaning=CDC_RACE_ETH["2028-9"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        description="Black or African American",
        meaning=CDC_RACE_ETH["2054-5"])
    native_hawaiian_or_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_pacific_islander",
        description="Native Hawaiian or Other Pacific Islander",
        meaning=CDC_RACE_ETH["2076-8"])
    white = PermissibleValue(
        text="white",
        description="White",
        meaning=CDC_RACE_ETH["2106-3"])
    other_race = PermissibleValue(
        text="other_race",
        description="Other Race",
        meaning=CDC_RACE_ETH["2131-1"])
    unknown = PermissibleValue(
        text="unknown",
        description="unknown",
        meaning=HL7_NULL["UNK"])
    asked_but_unknown = PermissibleValue(
        text="asked_but_unknown",
        description="asked but unknown",
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

class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the Thing available for use?
    """
    available = PermissibleValue(
        text="available",
        description="Biospecimen is Available",
        meaning=IG2-BIOSPECIMEN-AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2-BIOSPECIMEN-AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the Thing available for use?",
    )

class EnumMeasurementValueCode(EnumDefinitionImpl):
    """
    Indicate measurement details such as positive/negative/indeterminate
    """
    negative = PermissibleValue(
        text="negative",
        description="Negative")
    positive = PermissibleValue(
        text="positive",
        description="Positive")
    not_performed = PermissibleValue(
        text="not_performed",
        description="Not Performed")
    indeterminate = PermissibleValue(
        text="indeterminate",
        description="Indeterminate")

    _defn = EnumDefinition(
        name="EnumMeasurementValueCode",
        description="Indicate measurement details such as positive/negative/indeterminate",
    )

class EnumFamilyType(EnumDefinitionImpl):
    """
    Enumerations describing research family type
    """
    control_only = PermissibleValue(
        text="control_only",
        description="Control Only")
    duo = PermissibleValue(
        text="duo",
        description="Duo")
    proband_only = PermissibleValue(
        text="proband_only",
        description="Proband Only")
    trio = PermissibleValue(
        text="trio",
        description="Trio (2 parents and affected child)")
    trio_plus = PermissibleValue(
        text="trio_plus",
        description="2 Parents and 2 or more children")
    other = PermissibleValue(
        text="other",
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
        description="Not suspected",
        meaning=SNOMED_CT["428263003"])
    suspected = PermissibleValue(
        text="suspected",
        description="Suspected",
        meaning=SNOMED_CT["415684004"])
    known_present = PermissibleValue(
        text="known_present",
        description="Known Present",
        meaning=SNOMED_CT["410515003"])
    unknown = PermissibleValue(
        text="unknown",
        description="Unknown",
        meaning=SNOMED_CT["261665006"])

    _defn = EnumDefinition(
        name="EnumConsanguinityAssertion",
        description="Asserts known or suspected consanguinity in this study family",
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

slots.phenotypic_sex = Slot(uri=ANVIL['participant/phenotypic_sex'], name="phenotypic_sex", curie=ANVIL.curie('participant/phenotypic_sex'),
                   model_uri=ANVIL.phenotypic_sex, domain=None, range=Union[str, "EnumSex"])

slots.phenotypic_sex_source_value = Slot(uri=ANVIL['participant/phenotypic_sex_source_value'], name="phenotypic_sex_source_value", curie=ANVIL.curie('participant/phenotypic_sex_source_value'),
                   model_uri=ANVIL.phenotypic_sex_source_value, domain=None, range=Optional[str])

slots.race = Slot(uri=ANVIL['participant/race'], name="race", curie=ANVIL.curie('participant/race'),
                   model_uri=ANVIL.race, domain=None, range=Union[str, "EnumRace"])

slots.race_source_value = Slot(uri=ANVIL['participant/race_source_value'], name="race_source_value", curie=ANVIL.curie('participant/race_source_value'),
                   model_uri=ANVIL.race_source_value, domain=None, range=Optional[str])

slots.ethnicity = Slot(uri=ANVIL['participant/ethnicity'], name="ethnicity", curie=ANVIL.curie('participant/ethnicity'),
                   model_uri=ANVIL.ethnicity, domain=None, range=Union[str, "EnumEthnicity"])

slots.ethnicity_source_value = Slot(uri=ANVIL['participant/ethnicity_source_value'], name="ethnicity_source_value", curie=ANVIL.curie('participant/ethnicity_source_value'),
                   model_uri=ANVIL.ethnicity_source_value, domain=None, range=Optional[str])

slots.age_at_last_vital_status = Slot(uri=ANVIL['participant/age_at_last_vital_status'], name="age_at_last_vital_status", curie=ANVIL.curie('participant/age_at_last_vital_status'),
                   model_uri=ANVIL.age_at_last_vital_status, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=ANVIL['participant/vital_status'], name="vital_status", curie=ANVIL.curie('participant/vital_status'),
                   model_uri=ANVIL.vital_status, domain=None, range=Optional[Union[str, "EnumVitalStatus"]])

slots.has_sample = Slot(uri=ANVIL['participant/has_sample'], name="has_sample", curie=ANVIL.curie('participant/has_sample'),
                   model_uri=ANVIL.has_sample, domain=None, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.has_assertion = Slot(uri=ANVIL['participant/has_assertion'], name="has_assertion", curie=ANVIL.curie('participant/has_assertion'),
                   model_uri=ANVIL.has_assertion, domain=None, range=Optional[Union[Dict[Union[str, SubjectAssertionId], Union[dict, SubjectAssertion]], List[Union[dict, SubjectAssertion]]]])

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

slots.age_at_collection = Slot(uri=ANVIL['biospecimen_collection/age_at_collection'], name="age_at_collection", curie=ANVIL.curie('biospecimen_collection/age_at_collection'),
                   model_uri=ANVIL.age_at_collection, domain=None, range=Optional[int])

slots.method = Slot(uri=ANVIL['biospecimen_collection/method'], name="method", curie=ANVIL.curie('biospecimen_collection/method'),
                   model_uri=ANVIL.method, domain=None, range=Optional[Union[str, "EnumSampleCollectionMethod"]])

slots.site = Slot(uri=ANVIL['biospecimen_collection/site'], name="site", curie=ANVIL.curie('biospecimen_collection/site'),
                   model_uri=ANVIL.site, domain=None, range=Optional[Union[str, "EnumSite"]])

slots.spatial_qualifier = Slot(uri=ANVIL['biospecimen_collection/spatial_qualifier'], name="spatial_qualifier", curie=ANVIL.curie('biospecimen_collection/spatial_qualifier'),
                   model_uri=ANVIL.spatial_qualifier, domain=None, range=Optional[Union[str, "EnumSpatialQualifiers"]])

slots.laterality = Slot(uri=ANVIL['biospecimen_collection/laterality'], name="laterality", curie=ANVIL.curie('biospecimen_collection/laterality'),
                   model_uri=ANVIL.laterality, domain=None, range=Optional[Union[str, "EnumLaterality"]])

slots.sample_id_fk = Slot(uri=ANVIL['aliquot/sample_id_fk'], name="sample_id_fk", curie=ANVIL.curie('aliquot/sample_id_fk'),
                   model_uri=ANVIL.sample_id_fk, domain=None, range=str)

slots.sample_volume = Slot(uri=ANVIL['aliquot/sample_volume'], name="sample_volume", curie=ANVIL.curie('aliquot/sample_volume'),
                   model_uri=ANVIL.sample_volume, domain=None, range=Optional[float])

slots.sample_volume_unit = Slot(uri=ANVIL['aliquot/sample_volume_unit'], name="sample_volume_unit", curie=ANVIL.curie('aliquot/sample_volume_unit'),
                   model_uri=ANVIL.sample_volume_unit, domain=None, range=Optional[str])

slots.sample_concentration = Slot(uri=ANVIL['aliquot/sample_concentration'], name="sample_concentration", curie=ANVIL.curie('aliquot/sample_concentration'),
                   model_uri=ANVIL.sample_concentration, domain=None, range=Optional[float])

slots.sample_concentration_unit = Slot(uri=ANVIL['aliquot/sample_concentration_unit'], name="sample_concentration_unit", curie=ANVIL.curie('aliquot/sample_concentration_unit'),
                   model_uri=ANVIL.sample_concentration_unit, domain=None, range=Optional[str])

slots.sample_availability_status = Slot(uri=ANVIL['aliquot/sample_availability_status'], name="sample_availability_status", curie=ANVIL.curie('aliquot/sample_availability_status'),
                   model_uri=ANVIL.sample_availability_status, domain=None, range=Optional[Union[str, "EnumAvailabilityStatus"]])

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

slots.measurement_code = Slot(uri=ANVIL['measurement/measurement_code'], name="measurement_code", curie=ANVIL.curie('measurement/measurement_code'),
                   model_uri=ANVIL.measurement_code, domain=None, range=Union[str, List[str]])

slots.measurement_unit = Slot(uri=ANVIL['measurement/measurement_unit'], name="measurement_unit", curie=ANVIL.curie('measurement/measurement_unit'),
                   model_uri=ANVIL.measurement_unit, domain=None, range=str)

slots.measurement_source_value = Slot(uri=ANVIL['measurement/measurement_source_value'], name="measurement_source_value", curie=ANVIL.curie('measurement/measurement_source_value'),
                   model_uri=ANVIL.measurement_source_value, domain=None, range=str)

slots.measurement_value_code = Slot(uri=ANVIL['measurement/measurement_value_code'], name="measurement_value_code", curie=ANVIL.curie('measurement/measurement_value_code'),
                   model_uri=ANVIL.measurement_value_code, domain=None, range=Optional[Union[str, "EnumMeasurementValueCode"]])

slots.age_at_observation = Slot(uri=ANVIL['measurement/age_at_observation'], name="age_at_observation", curie=ANVIL.curie('measurement/age_at_observation'),
                   model_uri=ANVIL.age_at_observation, domain=None, range=Optional[int])

slots.procedure_code = Slot(uri=ANVIL['procedure/procedure_code'], name="procedure_code", curie=ANVIL.curie('procedure/procedure_code'),
                   model_uri=ANVIL.procedure_code, domain=None, range=Union[str, List[str]])

slots.procedure_source_value = Slot(uri=ANVIL['procedure/procedure_source_value'], name="procedure_source_value", curie=ANVIL.curie('procedure/procedure_source_value'),
                   model_uri=ANVIL.procedure_source_value, domain=None, range=str)

slots.family_external_id = Slot(uri=ANVIL['family/family_external_id'], name="family_external_id", curie=ANVIL.curie('family/family_external_id'),
                   model_uri=ANVIL.family_external_id, domain=None, range=Optional[Union[str, List[str]]])

slots.family_type = Slot(uri=ANVIL['family/family_type'], name="family_type", curie=ANVIL.curie('family/family_type'),
                   model_uri=ANVIL.family_type, domain=None, range=Optional[Union[str, "EnumFamilyType"]])

slots.family_description = Slot(uri=ANVIL['family/family_description'], name="family_description", curie=ANVIL.curie('family/family_description'),
                   model_uri=ANVIL.family_description, domain=None, range=Optional[str])

slots.consanguinity = Slot(uri=ANVIL['family/consanguinity'], name="consanguinity", curie=ANVIL.curie('family/consanguinity'),
                   model_uri=ANVIL.consanguinity, domain=None, range=Optional[Union[str, "EnumConsanguinityAssertion"]])

slots.family_study_focus = Slot(uri=ANVIL['family/family_study_focus'], name="family_study_focus", curie=ANVIL.curie('family/family_study_focus'),
                   model_uri=ANVIL.family_study_focus, domain=None, range=Optional[str])

slots.family_id_fk = Slot(uri=ANVIL['family-member/family_id_fk'], name="family_id_fk", curie=ANVIL.curie('family-member/family_id_fk'),
                   model_uri=ANVIL.family_id_fk, domain=None, range=Optional[str])

slots.family_member_id = Slot(uri=ANVIL['family-member/family_member_id'], name="family_member_id", curie=ANVIL.curie('family-member/family_member_id'),
                   model_uri=ANVIL.family_member_id, domain=None, range=str)

slots.other_family_member_id = Slot(uri=ANVIL['family-member/other_family_member_id'], name="other_family_member_id", curie=ANVIL.curie('family-member/other_family_member_id'),
                   model_uri=ANVIL.other_family_member_id, domain=None, range=Optional[str])

slots.relationship_code = Slot(uri=ANVIL['family-member/relationship_code'], name="relationship_code", curie=ANVIL.curie('family-member/relationship_code'),
                   model_uri=ANVIL.relationship_code, domain=None, range=Optional[str])