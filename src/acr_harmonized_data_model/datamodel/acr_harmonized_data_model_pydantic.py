from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'anvil',
     'default_range': 'string',
     'description': 'LinkML Schema for ACR Harmonized Data.',
     'id': 'https://anvilproject.org/acr-harmonized-data-model',
     'imports': ['linkml:types',
                 'participant',
                 'study',
                 'subject_assertion',
                 'data_access_policy',
                 'family',
                 'sample',
                 'file'],
     'license': 'MIT',
     'name': 'acr-harmonized-data-model',
     'prefixes': {'admin_gender': {'prefix_prefix': 'admin_gender',
                                   'prefix_reference': 'http://hl7.org/fhir/administrative-gender/'},
                  'anvil': {'prefix_prefix': 'anvil',
                            'prefix_reference': 'https://anvilproject.org/acr-harmonized-data-model/'},
                  'cdc_race_eth': {'prefix_prefix': 'cdc_race_eth',
                                   'prefix_reference': 'urn:oid:2.16.840.1.113883.6.238/'},
                  'hl7_null': {'prefix_prefix': 'hl7_null',
                               'prefix_reference': 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/'},
                  'ig2_biospecimen_availability': {'prefix_prefix': 'ig2_biospecimen_availability',
                                                   'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/'},
                  'ig2dac': {'prefix_prefix': 'ig2dac',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/'},
                  'ig2dat': {'prefix_prefix': 'ig2dat',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/'},
                  'ig_dob_method': {'prefix_prefix': 'ig_dob_method',
                                    'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/'},
                  'igcondtype': {'prefix_prefix': 'igcondtype',
                                 'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'snomed_ct': {'prefix_prefix': 'snomed_ct',
                                'prefix_reference': 'http://snomed.info/id/'}},
     'see_also': ['https://anvilproject.github.io/acr-harmonized-data-model'],
     'source_file': 'src/acr_harmonized_data_model/schema/acr_harmonized_data_model.yaml',
     'title': 'ACR Harmonized Data Model'} )

class EnumDateOfBirthType(str, Enum):
    """
    Privacy rules that may modify a date value.
    """
    Exact = "exact"
    """
    Exact
    """
    Year_Only = "year_only"
    """
    Year Only
    """
    Shifted = "shifted"
    """
    Shifted
    """
    Decade_Only = "decade_only"
    """
    Decade Only
    """
    Other = "other"
    """
    Other
    """


class EnumSex(str, Enum):
    """
    Terms describing an individual's sex.
    """
    Female = "female"
    """
    Female
    """
    Male = "male"
    """
    Male
    """
    Unknown = "unknown"
    """
    Unknown
    """
    Intersex = "intersex"
    """
    Intersex
    """


class EnumRace(str, Enum):
    """
    OMB Codes describing race.
    """
    American_Indian_or_Alaskan_Native = "american_indian_or_alaskan_native"
    Asian = "asian"
    Black_or_African_American = "black_or_african_american"
    Native_Hawaiian_or_Other_Pacific_Islander = "native_hawaiian_or_pacific_islander"
    White = "white"
    Other_Race = "other_race"
    unknown = "unknown"
    asked_but_unknown = "asked_but_unknown"


class EnumEthnicity(str, Enum):
    """
    OMB Codes describing Hispanic or Latino ethnicity.
    """
    hispanic_or_latino = "hispanic_or_latino"
    """
    Hispanic or Latino
    """
    not_hispanic_or_latino = "not_hispanic_or_latino"
    """
    Not Hispanic or Latino
    """
    unknown = "unknown"
    """
    unknown
    """
    asked_but_unknown = "asked_but_unknown"
    """
    asked but unknown
    """


class EnumSubjectType(str, Enum):
    """
    Types of entities
    """
    participant = "participant"
    """
    Study participant with consent, assent, or waiver of consent.
    """
    non_participant = "non_participant"
    """
    An individual associated with a study who was not explictly consented, eg, the subject | of a reported family history.
    """
    cell_line = "cell_line"
    """
    Cell Line
    """
    animal_model = "animal_model"
    """
    Animal model
    """
    group = "group"
    """
    A group of individuals or entities.
    """
    other = "other"
    """
    A different entity type- ideally this will be resolved!
    """


class EnumVitalStatus(str, Enum):
    """
    Is the entity living?
    """
    alive = "alive"
    """
    Alive
    """
    dead = "dead"
    """
    Dead
    """
    not_reported = "not_reported"
    """
    Not Reported
    """
    unknown = "unknown"
    """
    Unknown
    """
    unspecified = "unspecified"
    """
    Unspecified
    """


class EnumAssertionType(str, Enum):
    """
    Provides options to describe the expressed semantics of a condition.
    """
    Phenotypic_Feature = "phenotypic_feature"
    """
    This is a phenotypic feature
    """
    disease = "disease"
    """
    Disease
    """
    comorbidity = "comorbidity"
    """
    Comorbidity
    """
    histology = "histology"
    """
    Histology
    """
    clinical_finding = "clinical_finding"
    """
    Clinical Finding
    """
    EHR_Billing_Code = "ehr_billing_code"
    """
    From an EHR billing record, which may indicate only investigation into a possible diagnosis.
    """
    Measurement = "measurement"
    """
    A measurement of some feature, eg, height or glucose.
    """


class EnumConditionAssertion(str, Enum):
    """
    Enumerations for Condition Assertion
    """
    Present = "present"
    """
    Present
    """
    Absent = "absent"
    """
    Absent
    """
    Unsure = "unsure"
    """
    Unsure
    """
    Unknown = "unknown"
    """
    Unknown
    """


class EnumConditionCode(str):
    """
    Recommended ontologies include: SNOMED_CT, HP, OMIM and ORPHA, prefixed with those curies
* SNOMED : https://bioregistry.io/registry/snomedct
* HP : https://bioregistry.io/registry/hp
* OMIM : https://bioregistry.io/registry/omim
* ORPHA : https://bioregistry.io/registry/orphanet

    """
    pass


class EnumAccessType(str, Enum):
    """
    Type of access controls applied
    """
    open = "open"
    """
    Open Access
    """
    registered = "registered"
    """
    Registered Access
    """
    controlled = "controlled"
    """
    Controlled
    """
    gsr_restricted = "gsr_restricted"
    """
    GSR Restricted
    """
    gsr_allowed = "gsr_allowed"
    """
    GSR Allowed
    """


class EnumAccessCode(str, Enum):
    """
    Type of research use case allowed
    """
    GRU = "gru"
    """
    General Research Use
    """
    HMB = "hmb"
    """
    Health/Medical/Biomedical
    """
    DS = "ds"
    """
    Disease-Specific (Disease/Trait/Exposure)
    """
    IRB = "irb"
    """
    IRB Approval Required
    """
    PUB = "pub"
    """
    Publication Required
    """
    COL = "col"
    """
    Collaboration Required
    """
    NPU = "npu"
    """
    Not-for-profit use only
    """
    MDS = "mds"
    """
    Methods
    """
    GSO = "gso"
    """
    Genetic Studies only
    """
    GSR = "gsr"
    """
    Genomic Summary Results
    """
    RD = "rd"
    """
    Related Diseases
    """


class EnumFamilyType(str, Enum):
    """
    Enumerations describing research family type
    """
    Control_only = "control_only"
    """
    Control Only
    """
    Duo = "duo"
    """
    Duo
    """
    Proband_only = "proband_only"
    """
    Proband Only
    """
    Trio = "trio"
    """
    Trio (2 parents and affected child)
    """
    TrioPLUS_SIGN = "trio_plus"
    """
    2 Parents and 2 or more children
    """
    Other = "other"
    """
    Other
    """


class EnumConsanguinityAssertion(str, Enum):
    """
    Asserts known or suspected consanguinity in this study family
    """
    not_suspected = "not_suspected"
    """
    Not suspected
    """
    suspected = "suspected"
    """
    Suspected
    """
    known_present = "known_present"
    """
    Known Present
    """
    unknown = "unknown"
    """
    Unknown
    """


class EnumAvailabilityStatus(str, Enum):
    """
    Is the Thing available for use?
    """
    Available = "available"
    """
    Biospecimen is Available
    """
    Unavailable = "unavailable"
    """
    Biospecimen is Unavailable
    """


class EnumSampleCollectionMethod(str):
    """
    The approach used to collect the biospecimen. Recommend ontology: [LOINC](https://loinc.org).

    """
    pass


class EnumSite(str):
    """
    The location of the specimen collection. Recommended ontology: [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html)

    """
    pass


class EnumSpatialQualifiers(str):
    """
    Any spatial/location qualifiers.

    """
    pass


class EnumLaterality(str):
    """
    Laterality information for the site

    """
    pass


class EDAMFormats(str):
    """
    Data formats from the EDAM ontology.
    """
    pass


class EDAMDataTypes(str):
    """
    Data types from the EDAM ontology.
    """
    pass



class Thing(ConfiguredBaseModel):
    """
    Highest Level Class
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://anvilproject.org/acr-harmonized-data-model',
         'title': 'Thing'})

    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class Study(Thing):
    """
    Study Meta Data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/study',
         'title': 'Study'})

    parent_study_id: Optional[str] = Field(default=None, description="""Parent Study ID""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    funding_source: Optional[list[str]] = Field(default=[], description="""Funding Source""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    principal_investigator: Optional[list[str]] = Field(default=[], description="""Principal Investigator""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_title: str = Field(default=..., description="""Study Title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class DataSource(Thing):
    """
    Query configuration for specifying a source from which data are pulled.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/condition_assertion',
         'title': 'Data Source'})

    snapshot_id: Optional[str] = Field(default=None, title="Snapshot ID", description="""The Terra Data Repository Snapshot ID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource']} })
    google_data_project: Optional[str] = Field(default=None, title="Google Data Project", description="""The Google Data Project needed to query this snapshot in BigQuery.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource']} })
    snapshot_dataset: Optional[str] = Field(default=None, title="Snapshot Dataset", description="""The Dataset within BigQuery where the table can be queried.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource']} })
    table: Optional[str] = Field(default=None, title="Table", description="""The table in the dataset that contains the row of interest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource']} })
    parameterized_query: Optional[str] = Field(default=None, title="Parameterized Query", description="""A parameterized query that contains the primary key fields and can be used to select specific rows. This should be formatted according to (https://cloud.google.com/bigquery/docs/parameterized-queries)[BigQuery instructions], including using named parameters.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DataSource']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class AccessPolicy(Thing):
    """
    Describes the access required for a given element of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/data-access-policy'})

    data_access_type: Optional[list[EnumAccessType]] = Field(default=[], description="""Data Access Type""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    access_policy_code: list[EnumAccessCode] = Field(default=..., description="""Access Policy Code""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    disease_limitation: Optional[str] = Field(default=None, description="""Disease Use Limitations""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    description: str = Field(default=..., description="""Description""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    website: Optional[str] = Field(default=None, description="""Website""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class AccessControlledRecord(Thing):
    """
    Element for which specific access control restrictions apply.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model'})

    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class Subject(AccessControlledRecord):
    """
    This entity is the subject about which data or references are recorded. | This includes the idea of a human participant in a study, a cell line, an animal model, | or any other similar entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/participant',
         'title': 'Subject of data'})

    subject_type: EnumSubjectType = Field(default=..., title="Subject Type", description="""Type of entity this record represents""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject']} })
    organism_type: Optional[str] = Field(default=None, title="Organism Type", description="""Organism Type Label""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject']} })
    has_sample: Optional[dict[str, Sample]] = Field(default=None, title="Has sample", description="""Which samples were collected or processed for this Subject?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject']} })
    has_assertion: Optional[dict[str, SubjectAssertion]] = Field(default=None, title="Has assertion", description="""Which assertions are made about this Subject?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject']} })
    has_demographics: Optional[Demographics] = Field(default=None, title="Has demographics", description="""A demographic summary of the participant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class Demographics(AccessControlledRecord):
    """
    Basic participant demographics summary
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/participant',
         'title': 'Demographics'})

    date_of_birth: Optional[int] = Field(default=None, title="Date of Birth", description="""Date at which the individual was born. May be impacted by privacy rules described in date_of_birth_type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    date_of_birth_type: Optional[EnumDateOfBirthType] = Field(default=None, title="Date of Birth Type", description="""Privacy rule modification applied to date_of_birth.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    sex: EnumSex = Field(default=..., title="Sex", description="""Sex of the individual""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    sex_display: str = Field(default=..., title="Sex display string", description="""The friendly display string of the coded term for Sex""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    race: list[EnumRace] = Field(default=..., title="Race", description="""Reported race as defined by the 1997 OMB directives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    race_display: str = Field(default=..., title="Race display string", description="""The friendly display string of the coded term(s) for Race""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    ethnicity: EnumEthnicity = Field(default=..., title="Ethnicity", description="""Reported ethnicity as defined by the 1997 OMB directives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    ethnicity_display: str = Field(default=..., title="Ethnicity display string", description="""The friendly display string of the coded term for Ethnicity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    age_at_last_vital_status: Optional[float] = Field(default=None, title="Age at Last Vital Status", description="""Age at last vital status in decimal years.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics'], 'unit': {'ucum_code': 'a'}} })
    vital_status: Optional[EnumVitalStatus] = Field(default=None, title="VitalStatus", description="""Vital Status""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics']} })
    source_data: Optional[list[str]] = Field(default=[], title="Source Assertion", description="""The sources from which this assertion was derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics', 'SubjectAssertion']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class SubjectAssertion(AccessControlledRecord):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/condition_assertion',
         'title': 'Subject Assertion'})

    assertion_type: Optional[EnumAssertionType] = Field(default=None, title="Assertion Type", description="""The semantic type of the resource, eg, Condition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    age_at_assertion: Optional[float] = Field(default=None, title="Age at assertion", description="""The age in decimal years of the Subject when the assertion was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion'], 'unit': {'ucum_code': 'a'}} })
    age_at_event: Optional[float] = Field(default=None, title="Age at event", description="""The age in decimal years of the Subject at the time point which the assertion describes, | eg, age of onset or when a measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion'], 'unit': {'ucum_code': 'a'}} })
    age_at_resolution: Optional[float] = Field(default=None, title="Age at resolution", description="""The age in decimal years of the Subject when the asserted state was resolved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion'], 'unit': {'ucum_code': 'a'}} })
    code: Optional[str] = Field(default=None, title="Assertion Code", description="""The structured term defining the meaning of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    display: Optional[str] = Field(default=None, title="Display String", description="""The friendly display string of the coded term""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    value_code: Optional[str] = Field(default=None, title="Value Code", description="""The structured term defining the value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    value_display: Optional[str] = Field(default=None, title="Value Display String", description="""The friendly display string of the coded term for the value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    value_number: Optional[float] = Field(default=None, title="Value Number", description="""The numeric value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_units: Optional[str] = Field(default=None, title="Value Units", description="""The structured term defining the units of the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_units_display: Optional[str] = Field(default=None, title="Value Units", description="""The friendly display string of units of the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    source_data: Optional[list[str]] = Field(default=[], title="Source Assertion", description="""The sources from which this assertion was derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics', 'SubjectAssertion']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class SourceData(AccessControlledRecord):
    """
    Reference to submitted data used to generate harmonized data. Applying the query_parameter(s) to the data_source.parameterized_query should return the specific data of interest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/condition_assertion',
         'title': 'Source Data'})

    data_source: Optional[str] = Field(default=None, title="Data Source", description="""Defines the location of data and how to query it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceData']} })
    query_parameter: Optional[list[str]] = Field(default=[], title="Query Parameter", description="""One or more query parameters used to select the specific row. It will leverage the parameterized_query defined by a data_source. This should be formatted according to (https://cloud.google.com/bigquery/docs/parameterized-queries)[BigQuery instructions], specifically the bq CLI version with named parameters, ie, \"<parameter name>:<data type>:<value>\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['SourceData']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class Family(AccessControlledRecord):
    """
    A group of individuals of some relation who are grouped together in the study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/family',
         'title': 'Family'})

    family_type: Optional[EnumFamilyType] = Field(default=None, description="""Describes the 'type' of study family, eg, trio.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    family_description: Optional[str] = Field(default=None, description="""Free title describing the study family, such as potential inheritance or details about consanguinity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    consanguinity: Optional[EnumConsanguinityAssertion] = Field(default=None, description="""Is there known or suspected consanguinity in this study family?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    family_study_focus: Optional[str] = Field(default=None, description="""What is this study family investigating? EG, a specific condition. The code should be prefixed with a recognizable curie. 
""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    family_members: dict[str, FamilyMember] = Field(default=..., description="""The Subjects who are included in this family and their roles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    family_relationships: Optional[list[str]] = Field(default=[], description="""Family relationships associated with this family.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class FamilyRelationship(AccessControlledRecord):
    """
    A relationship between two Subjects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/family',
         'title': 'Family Member Relationship'})

    family_member: str = Field(default=..., description="""The family member Subject who is the relationship \"subject\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyRelationship', 'FamilyMember']} })
    other_family_member: str = Field(default=..., description="""The family member Subject for the relationship \"object\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyRelationship']} })
    relationship_code: str = Field(default=..., description="""Code definting the relationship predicate. Relationship of the \"Family Member\" to the \"Other Family Member\" (i.e. mother, father, etc). Code must be from the HL7 [FamilyMember ValueSet](https://terminology.hl7.org/6.2.0/ValueSet-v3-FamilyMember.html)
""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyRelationship']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class FamilyMember(AccessControlledRecord):
    """
    Designates a Subject as a member of a family with some specified role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/family',
         'title': 'Family Member'})

    family_member: str = Field(default=..., description="""The family member Subject who is the relationship \"subject\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyRelationship', 'FamilyMember']} })
    family_role: Optional[str] = Field(default=None, description="""The \"role\" of this individual in this family. Could include terms like \"proband\", \"mother\", etc.""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyMember']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class Sample(AccessControlledRecord):
    """
    Biospecimen data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/sample',
         'title': 'Sample'})

    biospecimen_collection: Optional[BiospecimenCollection] = Field(default=None, description="""Biospecimen Collection that generated this sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    parent_sample: Optional[str] = Field(default=None, description="""Sample from which this sample is derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    sample_type: str = Field(default=..., description="""Type of material of which this Sample is comprised""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    processing: Optional[list[str]] = Field(default=[], description="""Processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    availablity_status: Optional[EnumAvailabilityStatus] = Field(default=None, description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    storage_method: Optional[list[str]] = Field(default=[], description="""Sample storage method, eg, Frozen or with additives""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    quantity_number: Optional[float] = Field(default=None, title="Quantity", description="""The total quantity of the specimen""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_units: Optional[str] = Field(default=None, title="Quantity Units", description="""The structured term defining the units of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    aliquots: Optional[dict[str, Aliquot]] = Field(default=None, description="""Aliquot(s) from this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class BiospecimenCollection(AccessControlledRecord):
    """
    Biospecimen Collection
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/sample',
         'title': 'BiospecimenCollection'})

    age_at_collection: Optional[float] = Field(default=None, title="age_at_collection", description="""The age at which this biospecimen was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    method: Optional[EnumSampleCollectionMethod] = Field(default=None, title="method", description="""The approach used to collect the biospecimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    site: Optional[EnumSite] = Field(default=None, title="site", description="""The location of the specimen collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    spatial_qualifier: Optional[EnumSpatialQualifiers] = Field(default=None, title="spatial_qualifier", description="""Any spatial/location qualifiers""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    laterality: Optional[EnumLaterality] = Field(default=None, title="laterality", description="""Laterality information for the site""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class Aliquot(AccessControlledRecord):
    """
    Specific tubes or details of a Sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/sample',
         'title': 'Aliquot'})

    availablity_status: Optional[EnumAvailabilityStatus] = Field(default=None, description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_number: Optional[float] = Field(default=None, title="Quantity", description="""The total quantity of the specimen""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_units: Optional[str] = Field(default=None, title="Quantity Units", description="""The structured term defining the units of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    concentration_number: Optional[float] = Field(default=None, description="""What is the concentration of the analyte in the Aliquot?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    concentration_unit: Optional[str] = Field(default=None, description="""Units associated with the concentration of the analyte in the Aliquot? UCUM coding preferred (with curie, UCUM)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class File(AccessControlledRecord):
    """
    File
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/file',
         'title': 'File'})

    subject: Optional[list[str]] = Field(default=[], title="Subject(s) of file", description="""The Subject(s) which this file describes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    sample: Optional[list[str]] = Field(default=[], title="Sample(s) related to file", description="""The Samples(s) used to generate data in this file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    filename: Optional[str] = Field(default=None, title="Filename", description="""The name of the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    format: Optional[EDAMFormats] = Field(default=None, title="File Format", description="""The format of the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    data_type: Optional[EDAMDataTypes] = Field(default=None, title="Data Type", description="""The type of data within this file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    size: Optional[int] = Field(default=None, title="File Size", description="""Size of the file, in Bytes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    drs_uri: Optional[str] = Field(default=None, title="DRS URI", description="""DRS location to access the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    file_metadata: Optional[str] = Field(default=None, title="File Metadata", description="""Additional metadata about the contents of the file, eg, genome reference build.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    has_access_policy: Optional[str] = Field(default=None, description="""Which access policy applies to this element?""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessControlledRecord']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


class FileMetadata(Thing):
    """
    Metadata about the contents of the file.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://anvilproject.org/acr-harmonized-data-model/file',
         'title': 'File Metadata'})

    code: Optional[str] = Field(default=None, title="Assertion Code", description="""The structured term defining the meaning of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    display: Optional[str] = Field(default=None, title="Display String", description="""The friendly display string of the coded term""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    value_code: Optional[str] = Field(default=None, title="Value Code", description="""The structured term defining the value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    value_display: Optional[str] = Field(default=None, title="Value Display String", description="""The friendly display string of the coded term for the value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'FileMetadata']} })
    id: str = Field(default=..., title="ID", description="""ID associated with a class""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })
    external_id: Optional[list[str]] = Field(default=[], title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems link dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Thing']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Thing.model_rebuild()
Study.model_rebuild()
DataSource.model_rebuild()
AccessPolicy.model_rebuild()
AccessControlledRecord.model_rebuild()
Subject.model_rebuild()
Demographics.model_rebuild()
SubjectAssertion.model_rebuild()
SourceData.model_rebuild()
Family.model_rebuild()
FamilyRelationship.model_rebuild()
FamilyMember.model_rebuild()
Sample.model_rebuild()
BiospecimenCollection.model_rebuild()
Aliquot.model_rebuild()
File.model_rebuild()
FileMetadata.model_rebuild()
