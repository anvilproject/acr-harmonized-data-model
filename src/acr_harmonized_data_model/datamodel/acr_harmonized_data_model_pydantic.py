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


metamodel_version = "1.11.0"
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


linkml_meta = LinkMLMeta({'default_prefix': 'acr_harmonized_data_model',
     'description': 'LinkML Schema for ACR Harmonized Data. This model under '
                    'development is intended to capture useful cross-study data in '
                    'the AnVIL data repository.',
     'id': 'https://w3id.org/anvilproject/acr-harmonized-data-model',
     'imports': ['upstream-models/common_access_model-0.0.7'],
     'license': 'MIT',
     'name': 'acr-harmonized-data-model',
     'prefixes': {'CDCREC': {'prefix_prefix': 'CDCREC',
                             'prefix_reference': 'urn:oid:2.16.840.1.113883.6.238/'},
                  'CHMO': {'prefix_prefix': 'CHMO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/CHMO_'},
                  'DUO': {'prefix_prefix': 'DUO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/DUO_'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'KIN': {'prefix_prefix': 'KIN',
                          'prefix_reference': 'http://purl.org/ga4gh/kin.owl#'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'MS': {'prefix_prefix': 'MS',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/MS_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'OBI': {'prefix_prefix': 'OBI',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/OBI_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'acr_harmonized_data_model': {'prefix_prefix': 'acr_harmonized_data_model',
                                                'prefix_reference': 'https://w3id.org/anvilproject/acr-harmonized-data-model/'},
                  'cam': {'prefix_prefix': 'cam',
                          'prefix_reference': 'https://includedcc.org/common-access-model/'},
                  'edam': {'prefix_prefix': 'edam',
                           'prefix_reference': 'http://edamontology.org'},
                  'hl7_null': {'prefix_prefix': 'hl7_null',
                               'prefix_reference': 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'loinc': {'prefix_prefix': 'loinc',
                            'prefix_reference': 'https://loinc.org/'},
                  'mesh': {'prefix_prefix': 'mesh',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'shex': {'prefix_prefix': 'shex',
                           'prefix_reference': 'http://www.w3.org/ns/shex#'},
                  'snomedct': {'prefix_prefix': 'snomedct',
                               'prefix_reference': 'http://snomed.info/id/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://anvilproject.github.io/acr-harmonized-data-model'],
     'source_file': 'src/acr_harmonized_data_model/schema/acr_harmonized_data_model.yaml',
     'title': 'acr-harmonized-data-model'} )

class EnumAssayType(str, Enum):
    """
    Type of assays performed
    """
    assay = "OBI:0000070"
    """
    assay
    """
    fluorescence_microscopy_assay = "CHMO:0000087"
    """
    Any type of light microscopy assay where the specimen can be made to fluoresce (emit energy as visible light) by illuminating it with light of specific wavelengths. These specimens are called fluorophores.
    """
    confocal_fluorescence_microscopy_assay = "CHMO:0000089"
    """
    Microscopy where the specimen can be made to fluoresce (emit energy as visible light) by scanning a gas (Ar or Kr) laser spot of specific wavelength over its surface and using a spatial pinhole to eliminate out-of-focus fluorescence.
    """
    light_microscopy_assay = "CHMO:0000102"
    """
    Microscopy where the specimen is illuminated with visible light and a system of lenses is used to produce an image.
    """
    liquid_chromatography_tandem_mass_spectrometry = "CHMO:0000701"
    """
    A method where a sample mixture is first separated by liquid chromatography before being ionised and characterised by mass-to-charge ratio and relative abundance using two mass spectrometers in series.
    """
    Bernoulli_trial = "OBI:0000117"
    """
    An assay where the output data is a datum with one of two values denoting success and failure.
    """
    NMR_3D_molecular_structure_determination_assay = "OBI:0000182"
    """
    A 3D molecular structure determination assay that uses magnetic properties of atomic nuclei to determine the 3D structure and dynamics of molecules in the input sample.
    """
    imaging_assay = "OBI:0000185"
    """
    An assay that produces a picture of an entity.
    """
    radioactivity_detection = "OBI:0000201"
    """
    An assay that measures the amount of radiation in the radioactive spectrum (alpha, beta or gamma rays) emitted from an input material.
    """
    protein_protein_interaction_detection_assay = "OBI:0000288"
    """
    An assay that determines interactions between proteins, such as protein-protein binding.
    """
    transcription_factor_binding_site_assay = "OBI:0000291"
    """
    An assay tthat determines DNA regions specifically recognized by proteins that function as transcription factors
    """
    metabolite_profiling_assay = "OBI:0000366"
    """
    An assay that detects and identifies chemical entities resulting from biochemical and cellular metabolism
    """
    measuring_glucose_concentration_in_blood_serum_assay = "OBI:0000418"
    """
    An assay that determines the concentration of glucose molecules in a blood serum sample
    """
    transcription_profiling_assay = "OBI:0000424"
    """
    An assay that determines gene expression and transcription activity using ribonucleic acids collected from a material entity.
    """
    DNA_sequence_feature_detection_assay = "OBI:0000433"
    """
    An assay with the objective to determine a sequence feature of DNA
    """
    genotyping_assay = "OBI:0000435"
    """
    An assay which generates data about a genotype from a specimen of genomic DNA. A variety of techniques and instruments can be used to produce information about sequence variation at particular genomic positions.
    """
    DNA_sequence_variation_detection_assay = "OBI:0000438"
    """
    An assay that measures changes (expansion, amplification, deletion, mutation) in the sequence of a DNA molecule.
    """
    analyte_assay = "OBI:0000443"
    """
    An assay with the objective to capture information about the presence, concentration, or amount of an analyte in an evaluant.
    """
    mass_measurement_assay = "OBI:0000445"
    """
    An assay that determines the mass of an evaluant
    """
    intracellular_electrophysiology_recording_assay = "OBI:0000447"
    """
    An electrophysiology assay where the recording location of the electrode is intracellular.
    """
    extracellular_electrophysiology_recording_assay = "OBI:0000454"
    """
    An electrophysiology assay where the recording location of the electrode is extracellular.
    """
    mass_spectrometry_assay = "OBI:0000470"
    """
    An assay that identifies the amount and type of material entities present in a sample by fragmenting the sample and measuring the mass-to-charge ratio of the resulting particles.
    """
    clinical_chemistry_assay = "OBI:0000520"
    """
    An analyte assay which uses analytical methods to produce measurements and data on the concentration of chemical parameters (analytes) present in a specimen collected from an organism in order to determine a phenotype of that organism.
    """
    copy_number_variation_profiling_assay = "OBI:0000537"
    """
    An assay that determines lost or amplified genomic regions of DNA by comparing genomic DNA originating from tissues from the same or different individuals using specific techniques such as CGH, array CGH, SNP genotyping
    """
    protein_expression_profiling_assay = "OBI:0000615"
    """
    An assay that determines protein expression and translation activity using protein extracts collected from a material entity.
    """
    NMR_spectroscopy_assay = "OBI:0000623"
    """
    An assay that exploits the magnetic properties of certain nuclei (those with a spin) to resonate when placed in particular magnetic field conditions. Instruments recording NMR spectrum and sets of analysis can be used to deduce identity of chemical as well as composition of complex chemical mixtures.
    """
    DNA_sequencing_assay = "OBI:0000626"
    """
    A sequencing assay which determines information on the sequence of a DNA molecule.
    """
    hematology_assay = "OBI:0000630"
    """
    An assay that studies phenotypes of an organism involving its blood and blood producing organs using a variety of techniques and instruments
    """
    DNA_methylation_profiling_assay = "OBI:0000634"
    """
    An assay that measures the state of methylation of DNA molecules using genomic DNA collected from a material entity using a range of techniques and instrument such as DNA sequencers and often relying on treatment with bisulfites to ensure cytosine conversion.
    """
    enzyme_linked_immunosorbent_assay = "OBI:0000661"
    """
    An analyte assay where binding of an enzyme linked antibody to a material entity that is immobilized on solid support is detected utilizing a chemiluminescent reaction. Depending on the setup, the enzyme-linked antibody could be binding directly to the analyte, or it serves as a secondary antibody detecting binding of the primary antibody to the analyte.
    """
    BrdU_incorporation_assay = "OBI:0000664"
    """
    A cell proliferation assay in which cells are cultured in the presence of BrdU which is incorporated into newly synthesized DNA of replicating cells (during the S phase of the cell cycle), substituting for thymidine during DNA replication, which can be quantified by BrdU specific antibodies.
    """
    tritiated_thymidine_incorporation_assay = "OBI:0000669"
    """
    A cell proliferation assay in which cells are cultured in the presence of tritiated thymidine which is incorporated into newly synthesized DNA of replicating cells (during the S phase of the cell cycle). The radioactivity of tritiated thymidine in a cell is a proxy for cells that were actively replicating.
    """
    MeDIP_seq_assay = "OBI:0000693"
    """
    A DNA methylation profiling assay that identifies methylated sites in genomic DNA and determines the methylation pattern that affect gene transcription using immunoprecipitation of methylated genomic DNA, creation of a library of corresponding DNA fragments (either single or paired-end fragments) and subsequent sequencing using parallelized sequencing methods.
    """
    chain_termination_sequencing_assay = "OBI:0000695"
    """
    A DNA sequencing assay which rely on the use of dideoxynucleotides used in 4 distinct sequencing reaction on the same DNA sample. The dideoxynucleotides, once incorporated in the complementary DNA strand being synthesized by the DNA polymerase prevent any further chain elongation. The newly generated sequences are resolved on a polyacrylamide gel using electrophoresis and labels (either fluorochrome or radioactivity) are used to determine the nucleotide present at a given position
    """
    Helicos_sequencing_assay = "OBI:0000697"
    """
    A DNA sequencing by synthesis assay that identifiies the sequnece of billions of DNA molecules immobilized to a surface using DNA polymerase and fluorescently labeled nucleotides added one at a time. The sequencing process does not require an amplification step and is typically able to produce reads of 25 base pair length.
    """
    survival_assessment_assay = "OBI:0000699"
    """
    An assay that measures the occurrence of death events in one or more organisms over time
    """
    Edman_degradation = "OBI:0000705"
    """
    A sequencing assay in which the amino acid sequence of input peptides or proteins is determined by iteratively cleaving of the amino-terminal (N-terminal) residue without disrupting the peptide bonds and identifying it by e.g. chromatography or electropheresis.
    """
    SOLiD_sequencing_assay = "OBI:0000706"
    """
    A DNA sequencing by ligation assay that identifies sequence information using primers to hybridize to the P1 adapter sequence within the library template, fluorescently labeled di-base probes to compete for ligation to the sequencing primer, multiple cycles of ligation, detection and cleavage to determine the eventual read length, following a series of ligation cycles, the extension product is removed and the template is reset with a primer complementary to the n-1 position for a second round of ligation cycles.
    """
    ChIP_seq_assay = "OBI:0000716"
    """
    An assay in which chromatin is immunoprecipitated and subsequently analyzed using a DNA sequencing step to identify which parts of DNA are part of the isolated chromatin
    """
    glucose_tolerance_test = "OBI:0000721"
    """
    An assay that measures glucose clearance from blood over time by repeated glucose measurement in blood serum or plasma after the administration of a glucose bolus in-vivo. This assay can be used to evaluate the severity of insulin resistance or the efficiency of glucose clearance.
    """
    DNA_sequencing_by_ligation_assay = "OBI:0000723"
    """
    A DNA sequencing assay that performs chain extension during the sequencing reaction step using DNA ligase
    """
    Solexa_sequencing_assay = "OBI:0000724"
    """
    A DNA sequencing by synthesis assay that identifies sequence information using DNA polymerase and reversible terminator, requiring immobilization of genomic DNA fragments onto a surface and a specific clonal amplification step known as bridge PCR. Reliance on a reversible terminator allows cycles of DNA chain extension by DNA polymerase and imaging without the need of electrophoretic separation of newly synthesized DNA fragment as with Sanger sequencing.
    """
    pyrosequencing_assay = "OBI:0000730"
    """
    A DNA sequencing by synthesis assay which sequences a single strand of DNA by synthesizing the complementary strand along it, one base pair at a time, and detecting which base was actually added at each step. The template DNA is immobilized, and solutions of A, C, G, and T nucleotides are added and removed after the reaction, sequentially. Light is produced only when the nucleotide solution complements the first unpaired base of the template. The sequence of solutions which produce chemiluminescent signals allows the determination of the sequence of the template. ssDNA template is hybridized to a sequencing primer and incubated with the enzymes DNA polymerase, ATP sulfurylase, luciferase and apyrase, and with the substrates adenosine 5-prime phosphosulfate (APS) and luciferin.
    """
    DNA_sequencing_by_synthesis_assay = "OBI:0000734"
    """
    A DNA sequencing assay that relies on DNA polymerase activity to perform chain extension during the sequencing reaction step.
    """
    immune_response_assay = "OBI:0000743"
    """
    An assay that determines information about an immune response
    """
    bisulfite_sequencing_assay = "OBI:0000748"
    """
    A DNA methylation profiling assay which determines the methylation status of genomic DNA using DNA sequencing techniques preceded by a bisulfite based chemical modification of genomic DNA at CpG island location.
    """
    human_antithrombin_III_in_blood_assay = "OBI:0000787"
    """
    An assay that measures the amount of antithrombin III in blood.
    """
    prothrombin_time_assay = "OBI:0000802"
    """
    An assay that measures the prothrombin ratio, which is the prothrombin time for a patient, divided by the result for control plasma. Most commonly the test is preformed using blood plasma. Blood is drawn into a test tube containing liquid citrate, which acts as an anticoagulant. An excess of calcium is added to enable the blood to clot again.Tissue factor (also known as factor III or thromboplastin) is added, and the time the sample takes to clot is measured optically as the prothrombin time, which is compared to a control sample.
    """
    antithrombin_III_berichrome_assay = "OBI:0000805"
    """
    An antithrombin-III (AT-III) assay in which exogenous bovine thrombin and heparin are added to test plasma to form a thrombin-heparin-AT complex. The residual thrombin not bound then hydrolyzes the p-nitroalanine substrate to produce a yellow color, which is read at 405 nm. The intensity of color produced is inversely proportional to the AT present. A calibration is done with standard human plasma reagent and results for a given specimen are reported as a percentage relative to the standard
    """
    spectrolyse_heparin_antifactor_Xa_assay = "OBI:0000808"
    """
    An assay that quantitatively measures heparin in human plasma using Factor Xa and Antithrombin III in excess, where the rate of Factor Xa inhibition is directly proportional to the heparin concentration. The residual Factor Xa activity, measured with a Factor Xa-specific chromogenic substrate, is inversely proportional to the heparin concentration.
    """
    measuring_neural_activity_in_the_caudate_nucleus_assay = "OBI:0000812"
    """
    An assay that measures neural activity in the caudate nucleus
    """
    activated_partial_thromboplastin_time_assay = "OBI:0000820"
    """
    An assay that evaluates blood coagulation by measuring the time required for the appearance of fibrin strands following the mixing blood or plasma with phospholipid platelet substitute (e.g., crude cephalins, soybean phosphatides). It is a test of the intrinsic pathway (factors VIII, IX, XI, and XII) and the common pathway (fibrinogen, prothrombin, factors V and X) of blood coaguation . It is used as a screening test and to monitor heparin therapy.
    """
    thrombin_time_assay = "OBI:0000823"
    """
    An assay that measures the time between the addition of the thrombin and the clot formation in plasma.
    """
    western_blot_assay = "OBI:0000854"
    """
    An analyte assay that detects specific peptides in an input material by separating it using gel electrophoresis, transfering the separated molecules to a membrane, and staining them with_ antibodies specific to the analyte molecules.
    """
    northern_blot_assay = "OBI:0000860"
    """
    An assay that determines the presence of gene transcripts by hybridizing labeled RNA or DNA probes against messenger RNAs isolated from tissue or cell cultures, resolved on denaturing gel, transfered by a blotting procedure to a solid support. Detection of hybridization signals is carried out by immunofluorescence or radioactivity measurements using photographic films or digital imaging devices such as Phosphor Imager.
    """
    number_96_well_neutralization_assay = "OBI:0000865"
    """
    A serum neutralization of viral infectivity assay which is performed in a 96-well plate.
    """
    single_nucleotide_resolution_nucleic_acid_structure_mapping_assay = "OBI:0000870"
    """
    An assay that provides information about the secondary structure of nucleic acids using chemical or enzymatic probing to establish the extent of base-pairing or solvent accessiblity.
    """
    viral_hemagglutination_assay = "OBI:0000871"
    """
    An assay that quantifies viruses by their hemagglutination activity.
    """
    serum_neutralization_of_viral_infectivity_assay = "OBI:0000872"
    """
    An analyte assay that measures virus-neutralizing abilities of different sera. Different dilutions of serum are mixed with virus and used to infect cells. At the lower dilutions, antibodies will block infection, but at higher dilutions, there will be too few antibodies to have an effect.The neutralization titer is expressed as the reciprocal of the highest dilution at which virus infection is blocked.
    """
    detection_of_specific_nucleic_acid_polymers_with_complementary_probes = "OBI:0000874"
    """
    An analyte assay in which a specified input material (the evaluant) is examined for the presence or quantity of specified nucleic acid polymers, which are identified based on the use of complementary nucleic acid probes.
    """
    viral_hemagglutination_inhibition_assay = "OBI:0000875"
    """
    An assay that measures the ability of an evaluant to inhibit hemagglutination by a virus. Hemagglutinin is a viral protein which binds to sialic acid receptors on cells or to erythrocytes, causing the cells to clump. Loss of clumping indicates that the evaluant blocks binding of hemagglutinin to sialic acid receptors.
    """
    cell_cell_killing_assay = "OBI:0000882"
    """
    A cytometry assay that monitors a cell population to track how many are killed by other cells.
    """
    in_vivo_cell_killing_assay = "OBI:0000883"
    """
    A cell killing assay that measures if and how many target cells are killed within an organism.
    """
    cell_proliferation_assay = "OBI:0000891"
    """
    A cytometry assay which measures the degreee to which input cells are replicating.
    """
    Southern_blot_assay = "OBI:0000892"
    """
    An analyte assay that detects the presence of a specific sequence in a DNA sample, which has been digested by restriction enzymes, resolved by gel electrophoresis, and blotted to a solid support, followed by hybridization of a probe raised against a specific sequence and detected with fluorescence or radioactivity.
    """
    real_time_polymerase_chain_reaction_assay = "OBI:0000893"
    """
    An assay, based on the PCR, that amplifies and simultaneously quantifies a specific DNA molecule based on the use of complementary probes/primers. It enables both detection and quantification (as absolute number of copies or relative amount when normalized to DNA input or additional normalizing genes) of one or more specific sequences in a DNA sample.
    """
    DEPC_structure_mapping_assay = "OBI:0000897"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay which determines nucleic acid secondary structure at a nucleotide resolution scale using DEPC as reagent and chemical probe
    """
    in_vitro_cell_killing_assay = "OBI:0000903"
    """
    A cell killing assay that measures if and how many target cells are actively killed by other cells in a cell culture.
    """
    reporter_cell_line_analyte_detection_bioassay = "OBI:0000904"
    """
    An analyte assay in which a cell line whose growth is known to be affected by the presence of a specific type of material (the anlyte) is cultured in the presence of an input material (the evaluant) in order to detect presence of the analyte in the evaluant.
    """
    radio_immuno_assay = "OBI:0000910"
    """
    An assay in which a radioactive labeled antigen or antibody is used to determine the interaction between an antigen and its receptor. This can be used to detect the presence of an antigen of interest in an input sample or determine the specificity of an input antibody.
    """
    real_time_reverse_transcription_polymerase_chain_reaction_assay = "OBI:0000911"
    """
    An assay that uses a reverse transcription step (an RNA strand is reverse transcribed into its DNA complement using the enzyme reverse transcriptase) before a PCR assay.
    """
    X_ray_crystallography_3D_molecular_structure_determination_assay = "OBI:0000912"
    """
    A 3D molecular structure determination assay in which the diffraction of pattern of X-ray beams in a crystal of purified material entities is used to resolve the 3-dimensional structure of the material entity of interest.
    """
    promoter_activity_detection_by_reporter_gene_assay = "OBI:0000913"
    """
    An assay in which the activity of a promoter in a cell is monitored by using a reporter gene that was inserted in a genomic location under control of the promoter and whose expression can be easily detected based on qualities or functions of the gene.
    """
    flow_cytometry_assay = "OBI:0000916"
    """
    A cytometry assay in which an input cell population is put in solution, is passed by a laser, and optical sensors are used to detect scattering of the laser light and/or fluorescence of specific markers to count and characterize the particles in solution.
    """
    cytometric_bead_array_assay = "OBI:0000920"
    """
    An analyte assay in which a series of beads coated with antibodies, antigens, or other small molecules are used to detect an analyte of interest.
    """
    surface_plasmon_resonance_binding_assay = "OBI:0000923"
    """
    A binding assay that uses the detection of electromagnetic waves in a surface to detect material entities adsorbed to the surface, which change the local optical index of refraction.
    """
    handedness_assay = "OBI:0000944"
    """
    An assay that measures the unequal distribution of fine motor skill between the left and right hands typically in human subjects by means of some questionnaire and scoring procedure.
    """
    self_reported_handedness_assessment = "OBI:0000957"
    """
    An assay where a person makes a statement that indicates what handedness he has from a choice of different categories.
    """
    in_live_cell_assay = "OBI:0000964"
    """
    An assay in which a measurement is made by observing entities located in a live cell.
    """
    in_live_organism_assay = "OBI:0000966"
    """
    An assay in which a measurement is made by observing entities located in an organism.
    """
    cell_cell_binding_detection_by_flow_cytometry_assay = "OBI:0000975"
    """
    A binding assay which uses a flow cytometer to detect pairs of cells that are bound to each other by staining them with different fluorescent labels.
    """
    in_container_assay = "OBI:0000978"
    """
    An assay in which a measurement is made by observing entities located in a container.
    """
    Edinburgh_handedness_assay = "OBI:0001001"
    """
    An assay that uses a set of questions (the Edinburgh Handedness inventory) to generate a score that can be used to assess the dominance of a person's right or left hand in everyday activities. The inventory can be used by an observer assessing the person, or by a person self-reporting hand use. The latter method tends to be less reliable due to a person over-attributing tasks to the dominant hand.
    """
    RNASE_CL3_structure_mapping_assay = "OBI:0001005"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using RNAse CL3 as reagent and enzymatic probe.
    """
    CMCT_structure_mapping_assay = "OBI:0001006"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay which uses CMCT as reagent and chemical probe to generate data and information at nucleotide resolution scale contributing to the determination of nucleic acid secondary structure
    """
    MPE_FeLEFT_PARENTHESISIIRIGHT_PARENTHESIS_structure_mapping_assay = "OBI:0001008"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using Fe-MP as reagent and chemical probe.
    """
    ENU_structure_mapping_assay = "OBI:0001011"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines the secondary structure of a nucleic acid at the nucleotide resolution scale which uses ENU as reagent and chemical probe
    """
    RNASE_V1_structure_mapping_assay = "OBI:0001012"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using RNAse V1 as reagent and enzymatic probe
    """
    kethoxal_structure_mapping_assay = "OBI:0001013"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines nucleic acid secondary structure at nucleotide resolution scale using kethoxal as reagent and chemical probe
    """
    single_nucleotide_resolution_nucleic_acid_structure_mapping_assay_using_enzymatic_probing = "OBI:0001014"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines structural information about the RNA species under study using proteins acting as enzymatic probes.
    """
    DMS_structure_mapping_assay = "OBI:0001015"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay which determins nucleic acid secondary structure at a nucleotide resolution scale using DMS as reagent and chemical probe
    """
    DNASE_1_structure_mapping_assay = "OBI:0001016"
    """
    A single-nucleotide-resolution deoxyribonucleic acid structure mapping assay which uses DNAse 1 as reagent and enzymatic probe to generate data and information at nucleotide resolution scale contributing to the determination of nucleic acid secondary structure
    """
    single_nucleotide_resolution_nucleic_acid_structure_mapping_assay_using_chemical_probing = "OBI:0001017"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines structural information about the RNA species under study using small chemical compounds acting as chemical probes.
    """
    Rhodium_DNA_structure_mapping_assay = "OBI:0001018"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using Rhodium as reagent and chemical probe.
    """
    RNA_ADA_I_RNA_structure_mapping_assay = "OBI:0001019"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using RNA adenosine deaminase I as reagent and enzymatic probe.
    """
    Lead_structure_mapping_assay = "OBI:0001020"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines nucleic acid secondary structure at nucleotide resolution scale using lead as reagent and chemical probe
    """
    RNASE_T2_structure_mapping_assay = "OBI:0001021"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using RNAse T2 as reagent and enzymatic probe
    """
    gene_dosage_assay = "OBI:0001022"
    """
    An assay that measures changes in phenotype due to increased or decreased dosage of a single allele of a gene.
    """
    Fe_BABE_RNA_structure_mapping_assay = "OBI:0001023"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic secondary structure at a nucleotide resolution scale using Fe-BABE as reagent and chemical probe.
    """
    RNASE_U2_structure_mapping_assay = "OBI:0001024"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using RNAase U2 as reagent and enzymatic probe
    """
    binding_constant_determination_assay = "OBI:0001025"
    """
    A binding assay where the specified output is a binding constant
    """
    NMIA_RNA_structure_mapping_assay = "OBI:0001026"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using NMIA as reagent and chemical probe
    """
    Terbium_RNA_structure_mapping_assay = "OBI:0001027"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using Terbium as reagent and chemical probe
    """
    OH_radical_structure_mapping_assay = "OBI:0001029"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay hat determines nucleic acid secondary structure at a nucleotide resolution scale using hydroxyl radical as reagent and chemical probe
    """
    RNASE_T1_structure_mapping_assay = "OBI:0001030"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale uses RNAse T1 as reagent and enzymatic probe.
    """
    Nuclease_S1_structure_mapping_assay = "OBI:0001035"
    """
    A single-nucleotide-resolution deoxyribonucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using DNAse 1 as reagent and enzymatic probe.
    """
    Ruthenium_structure_mapping_assay = "OBI:0001038"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that determines nucleic acid secondary structure at a nucleotide resolution scale using Rhutenium as reagent and chemical probe
    """
    inline_probing_RNA_structure_mapping_assay = "OBI:0001039"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at nucleotide resolution scale using intromolecular reactivity
    """
    number_3D_structure_determination_of_bound_molecular_complex_assay = "OBI:0001145"
    """
    A 3D molecular structure determination assay in which a complex of 2 or more molecular enties is characterized which provides information on their binding configuration.
    """
    binding_assay = "OBI:0001146"
    """
    An assay with the objective to characterize the disposition of two or more material entities to form a complex.
    """
    age_determination_assay = "OBI:0001158"
    """
    An assay that determines the duration of part of the life of an organism, where the initial time point is the beginning of some transitional state (such as birth or when planted).
    """
    reverse_transcription_polymerase_chain_reaction_assay = "OBI:0001170"
    """
    An assay that determines the concentration of RNA in a sample in which an RNA strand is first reverse transcribed into its DNA complement (complementary DNA, or cDNA) using the enzyme reverse transcriptase, and the resulting cDNA is amplified using traditional or real-time PCR.
    """
    RNA_sequencing_assay = "OBI:0001177"
    """
    An assay that determines the sequence of an RNA molecule.
    """
    efficacy_of_epitope_intervention_experiment = "OBI:0001178"
    """
    An assay that tests  if inducing an epitope specific immune response in an organism has an effect, such as the ability to prevent, treat or exacerbate diseases in the organism.
    """
    epitope_protection_from_infectious_challenge_experiment = "OBI:0001179"
    """
    An epitope protection experiment in which the ability of the epitope to protect the host from an infection is assessed.
    """
    epitope_protection_from_tumor_challenge_experiment = "OBI:0001183"
    """
    An epitope protection experiment in which the ability of the epitope to protect the host from developing tumors is assessed.
    """
    epitope_protection_experiment = "OBI:0001184"
    """
    An efficacy of epitope intervention experiment that tests the efficacy of inducing an immune epitope response to prevent disease in a host.
    """
    epitope_protection_from_infectious_challenge_experiment_based_on_pathogen_burden = "OBI:0001186"
    """
    An epitope protection from infectious challenge experiment in which the readout is a reduction in the presence of pathogens in the host compared to controls.
    """
    infectious_agent_detection_assay = "OBI:0001187"
    """
    An assay that measures the presence or amount of an infectious agent in an evaluant
    """
    epitope_disease_exacerbation_experiment = "OBI:0001188"
    """
    An efficacy of epitope intervention experiment that tests the ability of inducing an epitope immune response to increase the severity of an existing disease in the host.
    """
    epitope_protection_experiment_based_on_survival = "OBI:0001189"
    """
    An epitope protection experiment that determines the success of the epitope intervention based on increased survival of the host.
    """
    epitope_treatment_experiment = "OBI:0001190"
    """
    An epitope intervention experiment that tests the ability of inducing an epitope immune response to treat an existing disease  in the host.
    """
    ELISPOT_assay_measuring_epitope_specific_transforming_growth_factor_beta_production_by_T_cells = "OBI:0001194"
    """
    An enzyme-linked immunospot assay that detects transforming growth factor-beta production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_IP_10_production_by_T_cells = "OBI:0001196"
    """
    A cytometric bead array assay that detects IP-10 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_27_production_by_T_cells = "OBI:0001198"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-27 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_transforming_growth_factor_beta_production_by_T_cells = "OBI:0001203"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects transforming growth factor-beta production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_granulocyte_macrophage_colony_stimulating_factor_production_by_T_cells = "OBI:0001206"
    """
    An enzyme-linked immunospot assay that detects granulocyte macrophage colony stimulating factor production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_10_production_by_T_cells = "OBI:0001209"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-10 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_transforming_growth_factor_beta_production_by_T_cells = "OBI:0001210"
    """
    A cytometric bead array assay that detects transforming growth factor-beta production by T cells
    """
    intracellular_material_detection_assay_measuring_epitope_specific_perforin_release = "OBI:0001215"
    """
    A flow cytometry assay that detects epitope specific perforin release by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:0001216"
    """
    A reporter cell line analyte detection bioassay that detects interleukin-2 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_22_production_by_T_cells = "OBI:0001217"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-22 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_8_production_by_T_cells = "OBI:0001218"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-8 production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interleukin_10_production_by_T_cells = "OBI:0001220"
    """
    A reporter cell line analyte detection bioassay that detects interleukin-10 production by T cells.
    """
    ChIP_chip_by_SNP_array_assay = "OBI:0001221"
    """
    A ChIP-ChIP assay in which immunoprecipitated chromatin is run on a SNP array to detect polymorphism specific DNA elements in the isolated chromatin
    """
    ELISA_measuring_epitope_specific_RANTES_production_by_T_cells = "OBI:0001222"
    """
    An enzyme-linked immunosorbent assay that detects RANTES production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_1_beta_production_by_T_cells = "OBI:0001223"
    """
    A cytometric bead array assay that detects interleukin-1 beta production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_6_production_by_T_cells = "OBI:0001227"
    """
    An enzyme-linked immunospot assay that detects interleukin-6 production by T cells
    """
    in_vivo_assay_measuring_epitope_specific_helper_T_cell_enhancement_of_a_B_cell_mediated_immune_response = "OBI:0001228"
    """
    A T cell epitope specific helper activity assay that detects the ability of a T cell epitope to enhance an antibody response.
    """
    plasmon_resonance_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0001229"
    """
    A surface plasmon resonance binding assay that measures the dissociation constant [KD] of an epitope:MHC complex binding with a T cell receptor.
    """
    assay_measuring_epitope_specific_interleukin_5_production_by_T_cells = "OBI:0001230"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-5 production by T cells.
    """
    ELISA_measuring_epitope_specific_transforming_growth_factor_beta_production_by_T_cells = "OBI:0001231"
    """
    An enzyme-linked immunosorbent assay that detects transforming growth factor-beta production by T cells.
    """
    assay_measuring_epitope_specific_RANTES_production_by_T_cells = "OBI:0001232"
    """
    A T cell epitope specific cytokine production assay that detects RANTES production by T cells.
    """
    assay_measuring_epitope_specific_granulocyte_macrophage_colony_stimulating_factor_production_by_T_cells = "OBI:0001233"
    """
    A T cell epitope specific cytokine production assay that detects granulocyte macrophage colony stimulating factor production by T cells.
    """
    transcription_profiling_by_tiling_array_assay = "OBI:0001235"
    """
    A transcription profiling by array assay that uses a tiling path array.
    """
    ELISA_measuring_epitope_specific_interleukin_22_production_by_T_cells = "OBI:0001236"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-22 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_21_production_by_T_cells = "OBI:0001237"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-21 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_9_production_by_T_cells = "OBI:0001238"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-9 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_6_production_by_T_cells = "OBI:0001240"
    """
    A flow cytometry assay that detects interleukin-6 production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interleukin_4_production_by_T_cells = "OBI:0001241"
    """
    A reporter cell line analyte detection bioassay that detects interleukin-4 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_tumor_necrosis_factor_alpha_production_by_T_cells = "OBI:0001242"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects tumor necrosis factor alpha production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_monocyte_chemotactic_protein_1_production_by_T_cells = "OBI:0001243"
    """
    A cytometric bead array assay that detects monocyte chemotactic protein-1 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_23_production_by_T_cells = "OBI:0001244"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-23 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_perforin_release = "OBI:0001245"
    """
    A detection of specific nucleic acids with complementary probes assay that detects epitope specific perforin release by T cells.
    """
    ELISA_measuring_epitope_specific_tumor_necrosis_factor_superfamily_cytokine_production_by_T_cells = "OBI:0001246"
    """
    An enzyme-linked immunosorbent assay that detects tumor necrosis factor superfamily cytokine production by T cells.
    """
    genotyping_by_high_throughput_sequencing_assay = "OBI:0001247"
    """
    A genotyping assay that uses a high througput sequencer
    """
    ChIP_chip_assay = "OBI:0001248"
    """
    An assay in which chromatin is immunoprecipitated and subsequently analyzed using a DNA microarray to identify which parts of DNA are part of the isolated chromatin
    """
    assay_measuring_epitope_specific_interleukin_13_production_by_T_cells = "OBI:0001251"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-13 production by T cells.
    """
    assay_measuring_interleukin_9_production_by_T_cells = "OBI:0001253"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-9 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_5_production_by_T_cells = "OBI:0001255"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-5 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_3_production_by_T_cells = "OBI:0001260"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-3 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_1_alpha_production_by_T_cells = "OBI:0001261"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-1 alpha production by T cells.
    """
    in_vivo_assay_measuring_epitope_specific_helper_T_cell_enhancement_of_a_T_cell_mediated_immune_response = "OBI:0001263"
    """
    A T cell epitope specific helper activity assay that detects the ability of a T cell epitope to enhance a T cell response.
    """
    assay_measuring_epitope_specific_transforming_growth_factor_beta_production_by_T_cells = "OBI:0001264"
    """
    A T cell epitope specific cytokine production assay that detects transforming growth factor-beta production by T cells.
    """
    DNA_methylation_profiling_by_high_throughput_sequencing_assay = "OBI:0001266"
    """
    A DNA methylation profiling assay in which the methylation state of DNA is determined and can be compared between samples using sequencing based technology
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_12_production_by_T_cells = "OBI:0001268"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-12 production by T cells.
    """
    assay_measuring_epitope_specific_cytotoxic_T_cell_degranulation = "OBI:0001269"
    """
    A T cell epitope dependent biological activity assay that detects cytotoxic T cell degranulation.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_transforming_growth_factor_beta_production_by_T_cells = "OBI:0001270"
    """
    A reporter cell line analyte detection bioassay that detects transforming growth factor-beta production by T cells.
    """
    transcription_profiling_by_RNA_sequencing_assay = "OBI:0001271"
    """
    A type of transcription profiling assay where transcripts are extracted from a sample, usually (but not always) transformed into cDNA, and then sequenced. Sequence reads are generally mapped to a reference and quantified to establish levels of gene transcription.
    """
    ELISPOT_assay_measuring_epitope_specific_tumor_necrosis_factor_superfamily_cytokine_production_by_T_cells = "OBI:0001272"
    """
    An enzyme-linked immunospot assay that detects tumor necrosis factor superfamily cytokine production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interleukin_5_production_by_T_cells = "OBI:0001273"
    """
    A reporter cell line analyte detection bioassay that detects interleukin-5 production by T cells.
    """
    genotyping_by_array_assay = "OBI:0001274"
    """
    A genotyping assay that uses an array
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_1_production_by_T_cells = "OBI:0001276"
    """
    A T cell epitope specific cytokine production assay that detects production of chemokine (C-C motif) ligand 1 by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:0001277"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-2 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_22_production_by_T_cells = "OBI:0001279"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-22 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_16_production_by_T_cells = "OBI:0001280"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-16 production by T cells.
    """
    ELISA_measuring_epitope_specific_IP_10_production_by_T_cells = "OBI:0001281"
    """
    An enzyme-linked immunosorbent assay that detects IP-10 production by T cells.
    """
    translation_profiling_assay = "OBI:0001282"
    """
    An assay in which surface-bound, translationally competent ribosome complexes are used to generate a translation profile for mRNA, which mRNA may be a single molecular species, or a combination of species, including complex mixtures such as those found in the set of mRNAs isolated from a cell or tissue. One or more components of the surface-bound ribosome complex may be labeled at specific positions to permit analysis of multiple or single molecules for determination of ribosomal conformational changes and translation kinetics. Translation profiles are used as the basis for comparison of an mRNA or set of mRNA species. The translation profile can be used to determine such characteristics as kinetics of initiation, kinetic of elongation, identity of the polypeptide product, and the like. Analysis of translation profiles may be used to determine differential gene expression, optimization of mRNA sequences for expression, screening drug candidates for an effect on translation.
    """
    ELISA_measuring_epitope_specific_interleukin_15_production_by_T_cells = "OBI:0001283"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-15 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_12_production_by_T_cells = "OBI:0001284"
    """
    A cytometric bead array assay that detects interleukin-12 production by T cells.
    """
    ELISA_measuring_epitope_specific_lymphotoxin_A_production_by_T_cells = "OBI:0001288"
    """
    An enzyme-linked immunosorbent assay that detects lymphotoxin A production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_5_production_by_T_cells = "OBI:0001289"
    """
    A cytometric bead array assay that detects interleukin-5 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_17_production_by_T_cells = "OBI:0001291"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-17 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_15_production_by_T_cells = "OBI:0001292"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-15 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_17_production_by_T_cells = "OBI:0001295"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-17 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_17_production_by_T_cells = "OBI:0001296"
    """
    A cytometric bead array assay that detects interleukin-17 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_10_production_by_T_cells = "OBI:0001297"
    """
    A cytometric bead array assay that detects interleukin-10 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_21_production_by_T_cells = "OBI:0001298"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-21 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_5_production_by_T_cells = "OBI:0001299"
    """
    A flow cytometry assay that detects interleukin-5 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:0001300"
    """
    A cytometric bead array assay that detects interleukin-2 production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interleukin_16_production_by_T_cells = "OBI:0001301"
    """
    A reporter cell line analyte detection bioassay that detects interleukin-16 production by T cells.
    """
    ELISA_measuring_epitope_specific_macrophage_inflammatory_protein_1_alpha_production_by_T_cells = "OBI:0001302"
    """
    An enzyme-linked immunosorbent assay that detects macrophage inflammatory protein-1 alpha production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_granulocyte_macrophage_colony_stimulating_factor_production_by_T_cells = "OBI:0001303"
    """
    A flow cytometry assay that detects granulocyte macrophage colony stimulating factor production by T cells.
    """
    RNAi_profiling_by_array_assay = "OBI:0001304"
    """
    An assay in which double stranded RNA is synthesized with a sequence complementary to a gene(s) of interest and introduced into a cell or organism, where it is recognized as exogenous genetic material and activates the RNAi pathway resulting in knockdown of the transcripts and providing a means to study downstream changes in gene expression.
    """
    assay_measuring_epitope_specific_IP_10_production_by_T_cells = "OBI:0001308"
    """
    A T cell epitope specific cytokine production assay that detects IP-10 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_13_production_by_T_cells = "OBI:0001309"
    """
    A flow cytometry assay that detects interleukin-13 production by T cells.
    """
    X_ray_crystallography_assay_determining_the_3D_structure_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0001311"
    """
    A X-ray crystallography 3D molecular structure determination assay that characterizes the 3-dimensional molecular structure of a T cell epitope:MHC:TCR complex.
    """
    ELISA_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_1_production_by_T_cells = "OBI:0001315"
    """
    An enzyme-linked immunosorbent assay that detects chemokine (C-C motif) ligand 1 production by T cells.
    """
    flow_cytometry_assay_measuring_cell_cell_binding_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0001317"
    """
    A flow cytometry assay that measures the cell-cell binding of an epitope:MHC complex binding with a T cell receptor.
    """
    proteomic_profiling_by_array_assay = "OBI:0001318"
    """
    An assay that detects proteins in a sample (quantified or otherwise analyzed), e.g. antibody profiling using an array based technology.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:0001319"
    """
    A reporter cell line analyte detection bioassay that detects interferon-gamma production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_granzyme_B_release_by_T_cells = "OBI:0001322"
    """
    An enzyme-linked immunospot assay that detects  epitope specific granzyme B release by T cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_tolerance_induction = "OBI:0001324"
    """
    An efficacy of T cell epitope intervention experiment that uses a tolerance induction intervention experiment.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_RANTES_production_by_T_cells = "OBI:0001325"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects RANTES production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_4_production_by_T_cells = "OBI:0001326"
    """
    A cytometric bead array assay that detects interleukin-4 production by T cells
    """
    assay_measuring_epitope_specific_lymphotoxin_A_production_by_T_cells = "OBI:0001327"
    """
    A T cell epitope specific cytokine production assay that detects lymphotoxin A production by T cells.
    """
    ELISA_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_9_production_by_T_cells = "OBI:0001330"
    """
    An enzyme-linked immunosorbent assay that detects chemokine (C-X-C motif) ligand 9 production by T cells.
    """
    DNA_methylation_profiling_by_array_assay = "OBI:0001332"
    """
    A DNA methylation profiling assay in which the methylation state of DNA is determined and can be compared between samples using array technology
    """
    assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_alpha_production_by_T_cells = "OBI:0001333"
    """
    A T cell epitope specific cytokine production assay that detects macrophage inflammatory protein-1 alpha production by T cells.
    """
    microRNA_profiling_by_array_assay = "OBI:0001335"
    """
    An assay that analyses the microRNA component of the transcriptome using a microRNA array.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_4_production_by_T_cells = "OBI:0001339"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-4 production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_granulocyte_macrophage_colony_stimulating_factor_production_by_T_cells = "OBI:0001341"
    """
    A reporter cell line analyte detection bioassay that detects granulocyte macrophage colony stimulating factor production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_21_production_by_T_cells = "OBI:0001342"
    """
    A flow cytometry assay that detects interleukin-21 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_monocyte_chemotactic_protein_1_production_by_T_cells = "OBI:0001343"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects monocyte chemotactic protein-1 production by T cells.
    """
    ELISA_measuring_epitope_specific_monocyte_chemotactic_protein_1_production_by_T_cells = "OBI:0001344"
    """
    An enzyme-linked immunosorbent assay that detects monocyte chemotactic protein-1 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_4_production_by_T_cells = "OBI:0001345"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-C motif) ligand 4 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_21_production_by_T_cells = "OBI:0001346"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-21 production by T cells.
    """
    in_vivo_skin_test_assay_measuring_T_cell_epitope_specific_type_IV_hypersensitivity = "OBI:0001348"
    """
    An efficacy of T cell epitope intervention experiment that detects epitope specific type IV hypersensitivity.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_13_production_by_T_cells = "OBI:0001349"
    """
    A cytometric bead array assay that detects interleukin-13 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:0001350"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interferon-gamma production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_tumor_necrosis_factor_alpha_production_by_T_cells = "OBI:0001353"
    """
    A cytometric bead array assay that detects tumor necrosis factor alpha production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_17_production_by_T_cells = "OBI:0001354"
    """
    An enzyme-linked immunospot assay that detects interleukin-17 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interferon_beta_production_by_T_cells = "OBI:0001356"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interferon-beta production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_granulocyte_macrophage_colony_stimulating_factor_production_by_T_cells = "OBI:0001357"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects granulocyte macrophage colony stimulating factor production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_8_production_by_T_cells = "OBI:0001359"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-8 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_6_production_by_T_cells = "OBI:0001360"
    """
    A cytometric bead array assay that detects interleukin-6 production by T cells.
    """
    transcription_profiling_by_RT_PCR_assay = "OBI:0001361"
    """
    A transcription profiling assay that uses reverse transcription PCR (RT-PCR).
    """
    assay_measuring_epitope_specific_interleukin_23_production_by_T_cells = "OBI:0001363"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-23 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_10_production_by_T_cells = "OBI:0001367"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-10 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_tumor_necrosis_factor_superfamily_cytokine_production_by_T_cells = "OBI:0001368"
    """
    A cytometric bead array assay that detects tumor necrosis factor superfamily cytokine production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_4_production_by_T_cells = "OBI:0001370"
    """
    A flow cytometry assay that detects chemokine (C-C motif) ligand 4 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_3_production_by_T_cells = "OBI:0001376"
    """
    A flow cytometry assay that detects interleukin-3 production by T cells.
    """
    ELISA_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_4_production_by_T_cells = "OBI:0001378"
    """
    An enzyme-linked immunosorbent assay that detects chemokine (C-C motif) ligand 4 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:0001379"
    """
    A cytometric bead array assay that detects interferon-gamma production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_18_production_by_T_cells = "OBI:0001380"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-18 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_27_production_by_T_cells = "OBI:0001382"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-27 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_IP_10_production_by_T_cells = "OBI:0001383"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects IP-10 production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interleukin_3_production_by_T_cells = "OBI:0001384"
    """
    A reporter cell line analyte detection bioassay that detects interleukin-3 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_tumor_necrosis_factor_superfamily_cytokine_production_by_T_cells = "OBI:0001385"
    """
    A flow cytometry assay that detects tumor necrosis factor superfamily cytokine production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_1_alpha_production_by_T_cells = "OBI:0001388"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-1 alpha production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_6_production_by_T_cells = "OBI:0001389"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-6 production by T cells.
    """
    assay_measuring_epitope_specific_interferon_beta_production_by_T_cells = "OBI:0001390"
    """
    A T cell epitope specific cytokine production assay that detects interferon-beta production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_12_production_by_T_cells = "OBI:0001391"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-12 production by T cells.
    """
    in_vivo_assay_measuring_epitope_specific_T_cell_killing = "OBI:0001392"
    """
    An in vivo cell killing assay that measures the killing of antigen presenting cells (APC) by T cells whose TCR recognizes an epitope presented by the APC.
    """
    comparative_genomic_hybridization_by_array_assay = "OBI:0001393"
    """
    An assay that measures changes in DNA sequence copy number using a microarray. For example the analysis of LOH in tumor cells vs a non diseased sample or the comparison of clinical isolated of disease causing bacteria.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_23_production_by_T_cells = "OBI:0001395"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-23 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_granulocyte_colony_stimulating_factor_production_by_T_cells = "OBI:0001397"
    """
    A cytometric bead array assay that detects granulocyte colony stimulating factor production by T cells.
    """
    assay_measuring_epitope_specific_tumor_necrosis_factor_superfamily_cytokine_production_by_T_cells = "OBI:0001400"
    """
    A T cell epitope specific cytokine production assay that detects tumor necrosis factor superfamily cytokine production by T cells.
    """
    promoter_activity_detection_by_reporter_gene_assay_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:0001402"
    """
    A promoter activity detection by reporter gene assay that detects interleukin-2 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_alpha_production_by_T_cells = "OBI:0001405"
    """
    A cytometric bead array assay that detects macrophage inflammatory protein-1 alpha production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_3_production_by_T_cells = "OBI:0001406"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-3 production by T cells.
    """
    assay_measuring_epitope_specific_T_cell_activation = "OBI:0001407"
    """
    A T cell epitope dependent biological activity assay that detects T cell activation.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_RANTES_production_by_T_cells = "OBI:0001412"
    """
    A cytometric bead array assay that detects RANTES production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_interleukin_6_production_by_T_cells = "OBI:0001413"
    """
    A reporter cell line analyte detection bioassay that detects interleukin-6 production by T cells.
    """
    assay_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:0001414"
    """
    A T cell epitope specific cytokine production assay that detects interferon-gamma production by T cells.
    """
    assay_measuring_epitope_specific_tumor_necrosis_factor_alpha_production_by_T_cells = "OBI:0001416"
    """
    An assay of epitope specific tumor necrosis factor alpha production by T cells that detects tumor necrosis factor production.
    """
    ChIP_chip_by_tiling_array_assay = "OBI:0001419"
    """
    A ChIP-ChIP assay in which immunoprecipitated chromatin is run on a tiling array that covers stretches of DNA to to detect which elements in those stretches are present in the isolated chromatin
    """
    intracellular_material_detection_measuring_epitope_specific_granzyme_B_release_by_T_cells = "OBI:0001423"
    """
    A flow cytometry assay that detects epitope specific granzyme B release by T cells
    """
    radio_immuno_assay_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:0001433"
    """
    A radio immuno assay that detects interferon-gamma production by T cells.
    """
    assay_measuring_epitope_specific_granzyme_B_release_by_T_cells = "OBI:0001436"
    """
    A T cell epitope specific cytotoxic T cell degranulation assay that detects granzyme B release by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_9_production_by_T_cells = "OBI:0001437"
    """
    A flow cytometry assay that detects chemokine (C-X-C motif) ligand 9 production by T cells.
    """
    ELISA_measuring_epitope_specific_macrophage_inflammatory_protein_1_gamma_production_by_T_cells = "OBI:0001438"
    """
    An enzyme-linked immunosorbent assay that detects macrophage inflammatory protein-1 gamma production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:0001445"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-2 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_1_beta_production_by_T_cells = "OBI:0001449"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-1 beta production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_4_production_by_T_cells = "OBI:0001450"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-4 production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_6_production_by_T_cells = "OBI:0001451"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-6 production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_tumor_necrosis_factor_alpha_production_by_T_cells = "OBI:0001452"
    """
    A reporter cell line analyte detection bioassay that detects tumor necrosis factor alpha production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_lymphotoxin_A_production_by_T_cells = "OBI:0001453"
    """
    A flow cytometry assay that detects lymphotoxin A production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_5_production_by_T_cells = "OBI:0001455"
    """
    An enzyme-linked immunospot assay that detects interleukin-5 production by T cells.
    """
    assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_gamma_production_by_T_cells = "OBI:0001456"
    """
    A T cell epitope specific cytokine production assay that detects macrophage inflammatory protein-1 gamma production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_8_production_by_T_cells = "OBI:0001457"
    """
    A cytometric bead array assay that detects interleukin-8 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_9_production_by_T_cells = "OBI:0001459"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-X-C motif) ligand 9 production by T cells.
    """
    ELISA_measuring_epitope_specific_granzyme_B_release_by_T_cells = "OBI:0001461"
    """
    An enzyme-linked immunosorbent assay that detects epitope specific granzyme B release by T cells.
    """
    transcription_profiling_by_array_assay = "OBI:0001463"
    """
    A transcription profiling assay that uses array technology.
    """
    assay_measuring_epitope_specific_monocyte_chemotactic_protein_1_production_by_T_cells = "OBI:0001465"
    """
    A T cell epitope specific cytokine production assay that detects monocyte chemotactic protein-1 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_12_production_by_T_cells = "OBI:0001466"
    """
    A flow cytometry assay that detects interleukin-12 production by T cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_disease_exacerbation = "OBI:0001467"
    """
    An efficacy of T cell epitope intervention experiment that uses a disease exacerbation in vivo intervention experiment.
    """
    monospecific_T_cell_recognition_assay_measuring_MHC_ligand_processing_and_presentation = "OBI:0001469"
    """
    A MHC ligand processing and presentation assay in which the presence of a specific ligand in an eluate is detected using the response of T cells that are known to be monospecific for that ligand as a readout.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_after_tumor_burden_challenge = "OBI:0001473"
    """
    An in vivo assay measuring T cell epitope specific protection from tumor challenge using tumor burden.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_infectious_challenge_based_on_pathogen_burden = "OBI:0001475"
    """
    An in vivo assay measuring T cell epitope specific protection from pathogen challenge using pathogen burden.
    """
    phage_display_binding_assay = "OBI:0001476"
    """
    A binding assay in which a collection of phages expressing a library of different peptides or protein fragnments is used to infect cells, followed by screening for cells that bind a protein of interest, and identifiying the sequence of infecting phages to determine a suitable binding partner.
    """
    mass_spectrometry_assay_measuring_MHC_ligand_processing_and_presentation = "OBI:0001478"
    """
    A MHC ligand processing and presentation assay that uses a mass spectrometry assay to identify eluted ligands
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_transforming_growth_factor_beta_production_by_T_cells = "OBI:0001482"
    """
    A flow cytometry assay that detects transforming growth factor-beta production by T cells.
    """
    assay_measuring_T_cell_epitope_specific_in_vivo_activity = "OBI:0001484"
    """
    A T cell epitope dependent biological activity determination assay that uses an in vivo intervention experiment.
    """
    epitope_tolerance_induction_experiment = "OBI:0001488"
    """
    An efficacy of epitope intervention experiment that tests the ability of the intervention to decrease an existing immune response
    """
    mass_spectrometry_assay_measuring_MHC_ligand_processing_and_presentation_of_MHC_ligands_eluted_from_cellular_MHC = "OBI:0001489"
    """
    A mass spectrometry of MHC ligands assay that identifies eluted ligands from cell bound MHC.
    """
    cytometric_bead_array_measuring_epitope_specific_granulocyte_macrophage_colony_stimulating_factor_production_by_T_cells = "OBI:0001490"
    """
    A cytometric bead array assay that detects granulocyte macrophage colony stimulating factor production by T cells.
    """
    binding_assay_using_radioactivity_detection = "OBI:0001491"
    """
    A binding assay that uses radioactivity detection as an indicator of binding.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_based_on_survival = "OBI:0001492"
    """
    An in vivo assay measuring T cell epitope specific protection from other challenge using survival.
    """
    cell_bound_MHC_competitive_binding_assay_of_a_MHCCOLONligand_complex_using_T_cell_epitope_recognition = "OBI:0001493"
    """
    A cell bound MHC binding assay that uses a T cell epitope recognition assay.
    """
    in_vivo_assay_measuring_epitope_specific_T_cell_helper_activity = "OBI:0001495"
    """
    A T cell epitope dependent biological activity assay that detects the ability of epitope specific helper T cells to enhance either B cell or T cell adaptive immune response function.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_22_production_by_T_cells = "OBI:0001496"
    """
    A flow cytometry assay that detects interleukin-22 production by T cells.
    """
    assay_measuring_epitope_specific_perforin_release_by_T_cells = "OBI:0001497"
    """
    A T cell epitope specific cytotoxic T cell degranulation assay that detects perforin release by T cells.
    """
    binding_assay_using_fluorescence_detection = "OBI:0001499"
    """
    A binding assay that uses fluorescence detection as an indicator of binding.
    """
    coelution_assay_measuring_MHC_ligand_processing_and_presentation_using_T_cell_recognition_of_HPLC_fractionated_eluate_compared_to_synthetic_ligand = "OBI:0001500"
    """
    A MHC ligand processing and presentation assay in which an HPL chromatography is run to separate an input mixture of ligands eluted from MHC into fractions. These fractions are tested for recognition by T cells and compared to the recognition of a synthetic ligand that is presumed to be the recognized epitope. Identical HPLC fractionation and T cell recognition patterns confirm that the specific ligand was presented by MHC molecules.
    """
    fluorescence_detection_assay = "OBI:0001501"
    """
    An assay in which a material's fluorescence is determined.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_treatment_of_disease = "OBI:0001507"
    """
    An efficacy of T cell epitope intervention experiment that detects a decrease in disease.
    """
    Edman_degradation_assay_measuring_MHC_ligand_processing_and_presentation = "OBI:0001509"
    """
    A MHC ligand processing and presentation assay that uses Edman degradation to identify the eluted ligands
    """
    mass_spectrometry_assay_measuring_MHC_ligand_processing_and_presentation_of_MHC_ligands_eluted_from_secreted_MHC = "OBI:0001510"
    """
    A mass spectrometry of MHC ligands that identifies eluted ligands from secreted MHC.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_17A_production_by_T_cells = "OBI:0001512"
    """
    A cytometric bead array assay that detects interleukin-17A production by T cells.
    """
    radioactivity_detection_assay_measuring_competitive_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001513"
    """
    A radioactivity detection assay that detects loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation.
    """
    radioactivity_detection_assay_measuring_half_maximal_effective_concentration_LEFT_SQUARE_BRACKETEC50RIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_cell_lysate_MHCCOLONligand_complex = "OBI:0001516"
    """
    A radioactivity detection assay that measures half maximal effective concentration (EC50) to detect the direct binding of a cell-lysate-MHC molecule with a ligand.
    """
    radioactivity_detection_assay_measuring_half_maximal_inhibitory_concentration_LEFT_SQUARE_BRACKETIC50RIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001517"
    """
    A radioactivity detection assay that measures half maximal inhibitory concentration (IC50) to detect the loss of binding of a known reference ligand to cell-bound-MHC due to competition by the ligand under investigation.
    """
    fluorescence_detection_assay_measuring_direct_binding_of_a_cell_lysate_MHCCOLONligand_complex = "OBI:0001519"
    """
    A fluorescence detection assay that detects direct binding of a cell-lysate-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_half_maximal_inhibitory_concentration_LEFT_SQUARE_BRACKETIC50RIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001520"
    """
    A fluorescence detection assay that measures half maximal inhibitory concentration (IC50) to detect the loss of binding of a known reference ligand to cell-bound-MHC due to competition by the ligand under investigation.
    """
    ELISA_measuring_epitope_specific_granulocyte_colony_stimulating_factor_production_by_T_cells = "OBI:0001521"
    """
    An enzyme-linked immunosorbent assay that detects granulocyte colony stimulating factor production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_17F_production_by_T_cells = "OBI:0001523"
    """
    A cytometric bead array assay that detects interleukin-17F production by T cells.
    """
    fluorescence_detection_assay_measuring_equilibrium_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001524"
    """
    A fluorescence detection assay that measures equilibrium association constant (KA) to detect the direct binding of a cell-bound-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_half_life_to_determine_direct_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001531"
    """
    A fluorescence detection assay that measures half life to detect the direct binding of a purified-MHC molecule with a ligand.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_9_production_by_T_cells = "OBI:0001532"
    """
    A cytometric bead array assay that detects interleukin-9 production by T cells.
    """
    fluorescence_detection_assay_measuring_competitive_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001534"
    """
    A fluorescence detection assay that detects loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation.
    """
    fluorescence_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001537"
    """
    A fluorescence detection assay that measures equilibrium dissociation constant (KD) to detect the loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation.
    """
    fluorescence_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001539"
    """
    A fluorescence detection assay that measures equilibrium dissociation constant (KD) to detect the loss of binding of a known reference ligand to cell-bound-MHC due to competition by the ligand under investigation.
    """
    fluorescence_detection_assay_measuring_binding_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001541"
    """
    A fluorescence detection assay measuring binding on rate (kon) to detect direct binding of a purified-MHC:ligand complex.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_13_production_by_T_cells = "OBI:0001542"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-13 production by T cells.
    """
    fluorescence_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_purified_MHCCOLONligand_complex_approximated_by_EC50 = "OBI:0001543"
    """
    A fluorescence detection assay that measures equilibrium dissociation constant (KD) to detect direct binding of a purified-MHC molecule with a ligand and provides EC50 values determined under assay conditions where the EC50 approximates a KD value.
    """
    radioactivity_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_cell_lysate_MHCCOLONligand_complex = "OBI:0001544"
    """
    A radioactivity detection assay that measures equilibrium dissociation constant (KD) to detect the loss of binding of a known reference ligand to cell-lysate-MHC due to competition by the ligand under investigation.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_alpha_production_by_T_cells = "OBI:0001545"
    """
    A flow cytometry assay that detects macrophage inflammatory protein-1 alpha production by T cells.
    """
    radioactivity_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001549"
    """
    A radioactivity detection assay that measures equilibrium dissociation constant (KD) to detect the loss of binding of a known reference ligand to cell-bound-MHC due to competition by the ligand under investigation.
    """
    assay_measuring_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001550"
    """
    A qualitative binding assay that detects the binding of a cell-bound-MHC molecule with a ligand.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_tumor_necrosis_factor_LEFT_PARENTHESISligandRIGHT_PARENTHESIS_superfamily_member_11_production_by_T_cells = "OBI:0001552"
    """
    A flow cytometry assay that detects tumor necrosis factor (ligand) superfamily member 11 production by T cells.
    """
    assay_measuring_a_binding_constant_of_a_MHCCOLONligand_complex = "OBI:0001553"
    """
    A MHC:ligand binding assay that measures a binding constant.
    """
    assay_measuring_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001555"
    """
    A qualitative binding assay that detects the binding of a purified-MHC molecule with a ligand.
    """
    radioactivity_detection_assay_measuring_direct_binding_of_a_cell_lysate_MHCCOLONligand_complex = "OBI:0001556"
    """
    A radioactivity detection assay that detects direct binding of a cell-lysate-MHC molecule with a ligand.
    """
    radioactivity_detection_assay_measuring_half_life_to_determine_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001558"
    """
    A radioactivity detection assay that measures half life to detect the direct binding of a cell-bound-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_half_life_to_determine_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001559"
    """
    A fluorescence detection assay that measures half life to detect the direct binding of a cell-bound-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_half_maximal_effective_concentration_LEFT_SQUARE_BRACKETEC50RIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001561"
    """
    A fluorescence detection assay that measures half maximal effective concentration (EC50) to detect direct binding of a cell-bound-MHC molecule with a ligand.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_17F_production_by_T_cells = "OBI:0001562"
    """
    A flow cytometry assay that detects interleukin-17F production by T cells.
    """
    radioactivity_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_purified_MHCCOLONligand_complex_approximated_by_IC50 = "OBI:0001564"
    """
    A radioactivity detection assay that measures equilibrium dissociation constant (KD) to detect the loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation and provides IC50 values determined under assay conditions where the IC50 approximates a KD value.
    """
    radioactivity_detection_assay_measuring_half_life_to_determine_direct_binding_of_a_cell_lysate_MHCCOLONligand_complex = "OBI:0001565"
    """
    A radioactivity detection assay that measures half life to detect the direct binding of a cell-lysate-MHC molecule with a ligand.
    """
    radioactivity_detection_assay_measuring_binding_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_cell_lysate_MHCCOLONligand_complex = "OBI:0001567"
    """
    A radioactivity detection assay that measures binding off rate [koff] to detect direct binding of a cell-lysate-MHC molecule with a ligand.
    """
    radioactivity_detection_assay_measuring_half_maximal_inhibitory_concentration_LEFT_SQUARE_BRACKETIC50RIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001568"
    """
    A radioactivity detection assay that measures half maximal inhibitory concentration (IC50) to detect the loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation.
    """
    fluorescence_detection_assay_measuring_binding_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001569"
    """
    A fluorescence detection assay that measures binding off rate [koff] to detect direct binding of a purified-MHC molecule with a ligand.
    """
    assay_measuring_epitope_specific_vascular_endothelial_growth_factor_production_by_T_cells = "OBI:0001570"
    """
    A T cell epitope specific cytokine production assay that detects vascular endothelial growth factor production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_intracellular_cytokine_staining_LEFT_PARENTHESISICSRIGHT_PARENTHESIS_IL_22_production_by_T_cells = "OBI:0001577"
    """
    A cytometric bead array assay that detects interleukin-22 production by T cells.
    """
    ELISA_measuring_epitope_specific_vascular_endothelial_growth_factor_production_by_T_cells = "OBI:0001578"
    """
    An enzyme-linked immunosorbent assay that detects vascular endothelial growth factor production by T cells.
    """
    assay_measuring_binding_of_a_cell_lysate_MHCCOLONligand_complex = "OBI:0001579"
    """
    A qualitative binding assay that detects the binding of a cell-lysate-MHC molecule with a ligand.
    """
    phage_display_binding_assay_measuring_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001584"
    """
    A phage display binding assay that detects direct binding of a purified-MHC molecule with a ligand.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_7_production_by_T_cells = "OBI:0001585"
    """
    A cytometric bead array assay that detects interleukin-7 production by T cells.
    """
    radioactivity_detection_assay_measuring_half_life_to_determine_direct_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001586"
    """
    A radioactivity detection assay that measures half life to detect the direct binding of a purified-MHC molecule with a ligand.
    """
    assay_measuring_epitope_specific_interleukin_7_production_by_T_cells = "OBI:0001587"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-7 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_17A_production_by_T_cells = "OBI:0001589"
    """
    A flow cytometry assay that detects interleukin-17A production by T cells.
    """
    fluorescence_detection_assay_measuring_direct_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001590"
    """
    A fluorescence detection assay that detects direct binding of a purified-MHC molecule with a ligand.
    """
    direct_binding_assay = "OBI:0001591"
    """
    A binding assay that measures the formation or disassociation of a complex of 2 material entities directly without use of a competitve ligand.
    """
    fluorescence_detection_assay_measuring_half_maximal_effective_concentration_LEFT_SQUARE_BRACKETEC50RIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001592"
    """
    A fluorescence detection assay that measures half maximal effective concentration (EC50) to detect direct binding of a purified-MHC molecule with a ligand.
    """
    competitive_inhibition_of_binding_assay = "OBI:0001593"
    """
    A binding assay that detects the inhibition of binding between 2 material entities known to form a complex by the addition of a third material entity of interest. Inhibition of binding between the 2 materials reflects binding by the third material.
    """
    fluorescence_detection_assay_measuring_competitive_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001594"
    """
    A fluorescence detection assay that detects loss of binding of a known reference ligand to cell-bound-MHC due to competition by the ligand under investigation.
    """
    X_ray_crystallography_assay_determining_the_3D_structure_of_a_MHCCOLONligand_complex = "OBI:0001595"
    """
    A X-ray crystallography 3D molecular structure determination assay that characterizes the 3-dimensional molecular structure of a MHC:ligand complex.
    """
    cell_bound_MHC_competitive_binding_assay_measuring_half_maximal_inhibitory_concentration_LEFT_SQUARE_BRACKETIC50RIGHT_SQUARE_BRACKET_of_a_MHCCOLONligand_complex_using_T_cell_epitope_recognition = "OBI:0001597"
    """
    A cell bound MHC ligand binding half maximal inhibitory concentration (IC50) determination assay that uses a T cell epitope recognition assay to measure ligand binding.
    """
    radioactivity_detection_assay_measuring_competitive_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001599"
    """
    A radioactivity detection assay that detects loss of binding of a known reference ligand to cell-bound-MHC due to competition by the ligand under investigation.
    """
    assay_measuring_epitope_specific_granulocyte_colony_stimulating_factor_production_by_T_cells = "OBI:0001600"
    """
    A T cell epitope specific cytokine production assay that detects granulocyte colony stimulating factor production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_intracellular_cytokine_staining_LEFT_PARENTHESISICSRIGHT_PARENTHESIS_IL_21_production_by_T_cells = "OBI:0001601"
    """
    A cytometric bead array assay that detects interleukin-21 production by T cells.
    """
    radioactivity_detection_assay_measuring_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001602"
    """
    A radioactivity detection assay that detects direct binding of a cell-bound-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_50PERCENT_SIGN_dissociation_of_binding_temperature_LEFT_SQUARE_BRACKETTmRIGHT_SQUARE_BRACKET_of_a_purified_MHCCOLONligand_complex = "OBI:0001604"
    """
    A fluorescence detection assay that measures the 50% dissociation of binding temperature of a purified-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001606"
    """
    A fluorescence detection assay that detects direct binding of a cell-bound-MHC molecule with a ligand.
    """
    assay_measuring_epitope_specific_tumor_necrosis_factor_LEFT_PARENTHESISligandRIGHT_PARENTHESIS_superfamily_member_11_production_by_T_cells = "OBI:0001607"
    """
    An assay of epitope specific tumor necrosis factor (ligand) superfamily member 11 production by T cells that detects tumor necrosis factor production.
    """
    radioactivity_detection_assay_measuring_direct_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001608"
    """
    A radioactivity detection assay that detects direct binding of a purified-MHC molecule with a ligand.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_8_production_by_T_cells = "OBI:0001609"
    """
    A flow cytometry assay that detects interleukin-8 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_intracellular_cytokine_staining_LEFT_PARENTHESISICSRIGHT_PARENTHESIS_IL_23_production_by_T_cells = "OBI:0001610"
    """
    A cytometric bead array assay that detects interleukin-23 production by T cells.
    """
    fluorescence_detection_assay_measuring_half_maximal_inhibitory_concentration_LEFT_SQUARE_BRACKETIC50RIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001613"
    """
    A fluorescence detection assay that measures half maximal inhibitory concentration (IC50) to detect the loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation.
    """
    organism_species_detection_assay = "OBI:0001624"
    """
    An organism detection assay that identifies the organism species in a specimen.
    """
    analytical_chromatography = "OBI:0001630"
    """
    An analyte assay that uses a biomaterial's preferential affinity for either the mobile phase or the stationary phase to separate it from other materials and thereby detect its presence in an input material.
    """
    electron_microscopy_imaging_assay = "OBI:0001631"
    """
    An imaging assay in which an electrons are used to probe the density, shape and composition of an input material which are detected in an electron microscope and utilized to produce an image of the material.
    """
    immuno_staining_assay = "OBI:0001632"
    """
    A assay detecting a molecular label assay in which the label is attached to an antibody so that substances are marked based on the antibody's binding specificity.
    """
    calorimetric_binding_assay = "OBI:0001634"
    """
    A binding assay in which the heat generated or absorbed during a binding event is measured, which allows determination of binding constants, reaction stoichiometry, enthalpy and entropy.
    """
    antibody_binding_detection_by_fluorescence_quenching = "OBI:0001635"
    """
    A binding assay in which affinity is measured by detecting a change in fluorescence (usually quenching) that occurs upon binding of the antibody to the ligand. The fluorescent signal that is affected by binding is either from an exogenous fluorophore attached to the ligand, or is the intrisic fluorescence of aromatic (tryptophan) residues on the binding site of the antibody (no conjugated fluorophore necessary) or, less commonly, on the ligand binding region (epitope).
    """
    antigen_inhibition_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex_approximated_by_IC50 = "OBI:0001638"
    """
    A B cell epitope equilibrium dissociation constant (KD) assay that provides IC50 values determined under assay conditions where the IC50 approximates a KD value using a B cell epitope antigen inhibition of binding assay.
    """
    assay_measuring_epitope_specific_Ig_mediated_histamine_release = "OBI:0001639"
    """
    A B cell epitope specific activation of additional immune response assay that detects histamine release in vitro.
    """
    assay_measuring_epitope_specific_immunoglobulin_mediated_antigen_activation = "OBI:0001640"
    """
    A B cell epitope dependent biological activity determination assay that detects antigen activation.
    """
    assay_measuring_epitope_specific_complement_dependent_cytotoxicity = "OBI:0001641"
    """
    A B cell epitope specific activation of additional immune response assay that detects complement-dependent cytotoxicity in vitro .
    """
    assay_measuring_epitope_specific_antibody_dependent_cellular_cytotoxicity = "OBI:0001642"
    """
    A B cell epitope specific activation of additional immune response assay that detects antibody-dependent cellular cytotoxicity in vitro.
    """
    assay_measuring_epitope_specific_immunoglobulin_mediated_neutralization = "OBI:0001643"
    """
    A B cell epitope dependent biological activity determination assay that detects neutralization of the antigen.
    """
    assay_measuring_epitope_specific_opsonization = "OBI:0001644"
    """
    A B cell epitope specific activation of additional immune response assay that detects opsonization in vitro .
    """
    calorimetry_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001645"
    """
    A calorimetric binding assay that detects the binding of an antigen with an antibody.
    """
    electron_microscopy_assay_determining_the_3D_structure_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001646"
    """
    An electron-microscopy 3D molecular structure determination assay that characterizes the 3-dimensional molecular structrue of a B cell epitope:antibody complex
    """
    NMR_assay_determining_the_3D_structure_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001647"
    """
    A nuclear magnetic resonance 3D molecular structure determination assay that characterizes the 3-dimensional structure of a B cell epitope:antibody complex.
    """
    cross_blocking_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001648"
    """
    A cross-blocking assay that detects the binding of an antigen with an antibody.
    """
    RIA_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001649"
    """
    A radio immuno assay that detects the binding of an antigen with an antibody.
    """
    immunoblot_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001650"
    """
    An immunoblot assay that detects the binding of an antigen with an antibody.
    """
    plasmon_resonance_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001651"
    """
    A surface plasmon resonance binding assay that detects the binding of an antigen with an antibody.
    """
    immuno_staining_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001652"
    """
    An immuno staining assay that detects the binding of an antigen with an antibody.
    """
    immunoprecipitation_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001653"
    """
    An immunoprecipitation assay that detects the binding of an antigen with an antibody.
    """
    mass_spectrometry_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001654"
    """
    A mass spectrometry assay that detects the binding of an antigen with an antibody.
    """
    phage_display_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001655"
    """
    A phage display binding assay that detects the binding of an antigen with an antibody.
    """
    electron_microscopy_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001656"
    """
    An electron microscopy imaging assay that detects the binding of an antigen with an antibody.
    """
    ELISA_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001657"
    """
    An enzyme-linked immunosorbent assay that detects the binding of an antigen with an antibody.
    """
    ELISPOT_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001658"
    """
    An enzyme-linked immunospot assay that detects the binding of an antigen with an antibody.
    """
    flow_cytometry_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001659"
    """
    A flow cytometry assay that detects the binding of an antigen with an antibody.
    """
    intracellular_material_detection_assay_measuring_epitope_specific_granzyme_A_release_by_T_cells = "OBI:0001660"
    """
    A flow cytometry assay that detects epitope specific granzyme A release by T cells.
    """
    chromatography_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001661"
    """
    An analytical chromatography assay that detects the binding of an antigen with an antibody.
    """
    NMR_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001662"
    """
    A B cell epitope qualitative binding to antibody assay that uses a nuclear magnetic resonance assay.
    """
    ELISA_measuring_epitope_specific_granulysin_release_by_T_cells = "OBI:0001663"
    """
    An enzyme-linked immunosorbent assay that detects epitope specific granulysin release by T cells.
    """
    intracellular_material_detection_assay_measuring_epitope_specific_granulysin_release_by_T_cells = "OBI:0001664"
    """
    A flow cytometry assay that detects epitope specific granulysin release by T cells.
    """
    fluorescence_detection_assay_measuring_binding_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001665"
    """
    A fluorescence detection assay that measures binding off rate [koff] to detect direct binding of a cell-bound-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_binding_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_to_determine_direct_binding_of_a_cell_bound_MHCCOLONligand_complex = "OBI:0001666"
    """
    A fluorescence detection assay that measures binding on rate (kon) to detect direct binding of a cell-bound-MHC molecule with a ligand.
    """
    fluorescence_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_purified_MHCCOLONligand_complex_approximated_by_IC50 = "OBI:0001667"
    """
    A fluorescence detection assay that measures equilibrium dissociation constant (KD) to detect the loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation and provides IC50 values determined under assay conditions where the IC50 approximates a KD value.
    """
    split_ubiquitin_assay = "OBI:0001668"
    """
    A binding assay that screens membrane soluble proteins by fusion of two integral membrane proteins (bait and prey) to two different ubiquitin moieties. One moiety is also fused to a transcription factor (TF) that can be cleaved off by ubiquitin specific proteases. Upon bait and prey interaction, Nub and Cub-moieties assemble, reconstituting the split-ubiquitin. The reconstituted split-ubiquitin molecule is recognized by ubiquitin specific proteases, which cleave off the reporter protein, allowing it to induce the transcription of reporter genes.
    """
    far_western_blot_assay = "OBI:0001669"
    """
    An assay that measures protein-protein interactions by separating target proteins on an SDS-PAGE gel, transfering them to a solid substrate, hybridizing with a protein probe and visualizing bound proteins using a probe-directed antibody. This is a adaptation on the western blot assay.
    """
    RNA_protection_assay = "OBI:0001670"
    """
    An assay that determines the presence and estimates abundance of transcript species by first creating an homo or heteroduplex by adding a specific, complementary sequence to the sequence of interest and then exposing the mixture of ribonuclease, which will degrade only single stranded molecules. A detection step will reveal if the sample contained a sequence of interest.
    """
    electrophoretic_mobility_shift_assay = "OBI:0001671"
    """
    An assay that measures information about Protein-DNA or Protein-RNA interactions using gel electrophoresis and relying on the fact the molecular interactions will cause the heterodimer to be retarded on the gel when compared to controls corresponding to protein extract alone and protein extract + neutral nucleic acid.
    """
    gene_knock_down_assay = "OBI:0001672"
    """
    An assay which transiently disrupts gene transcripts by expressing antisense RNA constructs or delivering RNA interfering molecules in cells.
    """
    nano_cap_analysis_of_gene_expression_assay = "OBI:0001673"
    """
    A transcription profiling by RNA sequencing assay that is performed using a very low amount (nanogram scale) of mRNA samples using Cap analysis gene expression (CAGE).
    """
    cap_analysis_of_gene_expression_assay = "OBI:0001674"
    """
    A transcription profiling by RNA sequencing assay which measures RNA transcript abundances in biological samples by extracting 5' ends of capped transcripts, RTPCR and sequence those. Copy numbers of CAGE tags provide a way of quantification and provide a measure of expression of the transcriptome
    """
    ELISA_measuring_epitope_specific_interleukin_17A_production_by_T_cells = "OBI:0001675"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-17A production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_7_production_by_T_cells = "OBI:0001676"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-7 production by T cells.
    """
    yeast_2_hybrid_assay = "OBI:0001679"
    """
    An assay that detects protein protein interactions and protein DNA interactions by testing for physical interactions (such as binding) between two proteins or a single protein and a DNA molecule, respectively. The premise behind the test is the activation of downstream reporter gene(s) by the binding of a transcription factor onto an upstream activating sequence (UAS). For two-hybrid screening, the transcription factor is split into two separate fragments, called the binding domain (BD) and activating domain (AD). The BD is the domain responsible for binding to the UAS and the AD is the domain responsible for the activation of transcription. The Y2H is thus a protein-fragment complementation assay.
    """
    Sos_recruitment_assay = "OBI:0001680"
    """
    A binding assay that detects interacting proteins for a targeted domain where mammalian guanyl nucleotide exchange factor (GEF) Sos is recruited to the Saccharomyces cerevisiae plasma membrane harboring a temperature-sensitive Ras GEF, Cdc25-2, allowing growth at the nonpermissive temperature using the Sos recruitment system, a kind of yeast 2 hybrid system.
    """
    yeast_one_hybrid_assay = "OBI:0001681"
    """
    An assay that determines protein DNA interactions using a single fusion protein in which the activating domain is linked directly to the binding domain.
    """
    bacterial_one_hybrid_assay = "OBI:0001682"
    """
    An assay that identifies the sequence-specific target site of a DNA-binding domain. In this system, a given transcription factor (TF) is expressed as a fusion to a subunit of RNA polymerase. In parallel, a library of randomized oligonucleotides representing potential TF target sequences, is cloned into a separate vector containing the selectable genes HIS3 and URA3. If the DNA-binding domain (bait) binds a potential DNA target site (prey) in vivo, it will recruit RNA polymerase to the promoter and activate transcription of the reporter genes in that clone. The two reporter genes, HIS3 and URA3, allow for positive and negative selections, respectively. At the end of the process, positive clones are sequenced and examined with motif-finding tools in order to resolve the favoured DNA target sequence
    """
    chromosome_organization_assay_by_fluorescence_in_situ_hybridization = "OBI:0001683"
    """
    An in-situ hybridization assay that uses fluorescence to detect chromosomal integrity
    """
    methylation_specific_polymerase_chain_reaction_assay = "OBI:0001684"
    """
    An assay that uses initial modification of DNA by sodium bisulfite, converting all unmethylated, but not methylated, cytosines to uracil, and subsequent amplification with primers specific for methylated versus unmethylated DNA.
    """
    amplification_of_intermethylated_sites_assay = "OBI:0001685"
    """
    An assay that estimates genome-wide DNA methylation and measures methylation of DNA sequences. AIMS is based on the differential enzymatic digestion of genomic DNA with methylation-sensitive and methylation-insensitive isoschizomers followed by restrained PCR amplification of methylated sequences.
    """
    in_situ_hybridization_assay = "OBI:0001686"
    """
    An assay that localizes a specific DNA or RNA sequence within a portion or section of tissue using artificially induced nucleic hybridization.
    """
    cytochalasin_induced_inhibition_of_actin_polymerization_assay = "OBI:0001689"
    """
    An assay which uses compound cytochalasin (CHEBI: 23528) to block actin polymerization-dependent cell motility (GO:0070358) and actin filament polymerization (GO:0030041).
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_fertility = "OBI:0001692"
    """
    An efficacy of B cell epitope intervention experiment that uses a epitope protection experiment based on reduction of fertility.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_tolerance_induction = "OBI:0001693"
    """
    An efficacy of B cell epitope intervention experiment that uses a tolerance induction intervention experiment.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_induction_of_hypersensitivity = "OBI:0001694"
    """
    An efficacy of B cell epitope intervention experiment that detects a hypersensitivity response by monitoring skin reactions.
    """
    assay_measuring_epitope_specific_immune_complex_formation = "OBI:0001695"
    """
    A B cell epitope specific activation of additional immune response assay that detects agglutination in vitro.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_based_on_survival = "OBI:0001696"
    """
    An in vivo assay measuring B cell epitope specific protection from other challenge using survival.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_treatment_of_disease = "OBI:0001697"
    """
    An efficacy of B cell epitope intervention experiment that detects a decrease in disease.
    """
    assay_measuring_B_cell_epitope_specific_in_vivo_activity = "OBI:0001698"
    """
    A B cell epitope dependent biological activity determination assay that uses an in vivo intervention experiment.
    """
    antibody_cross_blocking_assay = "OBI:0001699"
    """
    A competitive inhibition of binding assay in which two antibodies that are known to bind the same antigen are tested for the ability of one antibody to inhibit binding of the other antibody to the antigen, thereby determining if they have overlapping binding sites.
    """
    immunoprecipitation_assay = "OBI:0001700"
    """
    An analyte assay in which an input material is mixed with antibodies and bound antigen:antibody complexes are separated out using immunoprecipitation. Either the antibody has known specificy, and the antigen mixture is tested for the presence of a specific antigen, or the antigen solution is well defined and the antibody solution is tested for the presence of antigen specific antibodies.
    """
    antigen_inhibition_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001701"
    """
    A B cell epitope qualitative binding to antibody assay that measures the ability of an antigen to inhibit antibody binding to a known ligand.
    """
    assay_measuring_qualitative_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001703"
    """
    An assay that detects the binding of an antigen with an antibody, and produces a qualitative measurement of the binding as an output.
    """
    assay_measuring_epitope_specific_activation_of_additional_immune_response_in_vitro = "OBI:0001704"
    """
    A B cell epitope dependent biological activity determination assay that detects secondary in vitro activity.
    """
    assay_measuring_epitope_specific_antigen_inhibition_of_antibody_activity = "OBI:0001705"
    """
    A B cell epitope dependent biological activity determination assay that detects inhibition of the antibody's activity by the antigen.
    """
    assay_measuring_biological_activity_resulting_from_B_cell_epitopeCOLONantibody_binding = "OBI:0001706"
    """
    A B cell epitope assay that measures the immune response process resulting from the binding of an antibody receptor to epitope or recognition of the epitope.
    """
    assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001708"
    """
    A B cell epitope binding constant determination assay that measures the dissociation constant KD.
    """
    assay_measuring_a_binding_constant_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001709"
    """
    A B cell epitope recognition assay that quantitavely characterizes the binding of an antibody / BCR with a ligand by determining a binding constant.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_challenge = "OBI:0001710"
    """
    An efficacy of B cell epitope intervention experiment that uses a epitope protection experiment.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_disease_exacerbation = "OBI:0001711"
    """
    An efficacy of B cell epitope intervention experiment that uses a disease exacerbation in vivo intervention experiment.
    """
    assay_measuring_the_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001718"
    """
    A B cell epitope binding constant determination assay that measures the on rate.
    """
    assay_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001719"
    """
    A B cell epitope binding constant determination assay that measures the association constant KA.
    """
    number_3D_molecular_structure_determination_assay_of_an_antigenCOLONantibody_complex = "OBI:0001721"
    """
    A 3D structure determination of bound molecular complex assay that characterizes the 3-dimensional structure of an antigen:antobody complex.
    """
    assay_measuring_the_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001723"
    """
    A B cell epitope binding constant determination assay that measures the off rate.
    """
    viral_hemagglutination_inhibition_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001724"
    """
    A viral hemagglutination inhibition assay that detects the binding of an antigen with an antibody.
    """
    quenching_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001726"
    """
    A fluorescence quenching assay that detects the binding of an antigen with an antibody.
    """
    RIA_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001727"
    """
    A radio immuno assay that measures the dissociation constant [KD] of an antigen binding with an antibody.
    """
    ELISA_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001728"
    """
    An enzyme-linked immunosorbent assay that measures the dissociation constant [KD] of an antigen binding with an antibody.
    """
    quenching_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001729"
    """
    A fluorescence quenching assay that measures the dissociation constant [KD] of an antigen binding with an antibody.
    """
    surface_plasmon_resonance_assay_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001730"
    """
    A surface plasmon resonance binding assay that measures the association constant [KA] of an antigen binding with an antibody.
    """
    surface_plasmon_resonance_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001731"
    """
    A surface plasmon resonance binding assay that measures the dissociation constant [KD] of an antigen binding with an antibody.
    """
    quenching_assay_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001732"
    """
    A fluorescence quenching assay that measures the association constant [KA] of an antigen binding with an antibody.
    """
    calorimetry_assay_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001733"
    """
    A calorimetric binding assay that measures the association constant [KA] of an antigen binding with an antibody.
    """
    calorimetry_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001734"
    """
    A calorimetric binding assay that measures the dissociation constant [KD] of an antigen binding with an antibody.
    """
    ELISA_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001735"
    """
    An enzyme-linked immunosorbent assay that measures the association constant [KA] of an antigen binding with an antibody.
    """
    RIA_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001736"
    """
    A radio immuno assay that measures the association constant [KA] of an antigen binding with an antibody.
    """
    X_ray_crystallography_assay_determining_the_3D_structure_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001738"
    """
    A X-ray crystallography 3D molecular structure determination assay that characterizes the 3-dimensional molecular structrue of a B cell epitope:antibody complex.
    """
    surface_plasmon_resonance_assay_measuring_the_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001739"
    """
    A surface plasmon resonance binding assay that measures the off rate [koff] of an antigen binding with an antibody.
    """
    quenching_assay_measuring_the_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001740"
    """
    A fluorescence quenching assay that measures the off rate [koff] of an antigen binding with an antibody.
    """
    surface_plasmon_resonance_assay_measuring_the_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001741"
    """
    A surface plasmon resonance binding assay that measures the on rate [kon] of an antigen binding with an antibody.
    """
    quenching_assay_measuring_the_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001742"
    """
    A fluorescence quenching assay that measures the on rate [kon] of an antigen binding with an antibody.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_1_beta_production_by_T_cells = "OBI:0001743"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-1 beta production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_1_alpha_production_by_T_cells = "OBI:0001744"
    """
    A flow cytometry assay that detects interleukin-1 alpha production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_1_alpha_production_by_T_cells = "OBI:0001745"
    """
    An enzyme-linked immunospot assay that detects interleukin-1 alpha production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_1_alpha_production_by_T_cells = "OBI:0001746"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-1 alpha production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_1_alpha_production_by_T_cells = "OBI:0001747"
    """
    A cytometric bead array assay that detects interleukin-1 alpha production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interferon_beta_production_by_T_cells = "OBI:0001748"
    """
    An enzyme-linked immunospot assay that detects interferon-beta production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interferon_beta_production_by_T_cells = "OBI:0001749"
    """
    A flow cytometry assay that detects interferon-beta production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_granulocyte_colony_stimulating_factor_production_by_T_cells = "OBI:0001750"
    """
    A flow cytometry assay that detects granulocyte colony stimulating factor production by T cells.
    """
    ELISA_measuring_epitope_specific_interferon_beta_production_by_T_cells = "OBI:0001751"
    """
    An enzyme-linked immunosorbent assay that detects interferon-beta production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_granulocyte_colony_stimulating_factor_production_by_T_cells = "OBI:0001752"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects granulocyte colony stimulating factor production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_granulocyte_colony_stimulating_factor_production_by_T_cells = "OBI:0001753"
    """
    An enzyme-linked immunospot assay that detects granulocyte colony stimulating factor production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_9_production_by_T_cells = "OBI:0001754"
    """
    A cytometric bead array assay that detects chemokine (C-X-C motif) ligand 9 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_9_production_by_T_cells = "OBI:0001756"
    """
    An enzyme-linked immunospot assay that detects chemokine (C-X-C motif) ligand 9 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_9_production_by_T_cells = "OBI:0001757"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-X-C motif) ligand 9 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_4_production_by_T_cells = "OBI:0001758"
    """
    An enzyme-linked immunospot assay that detects chemokine (C-C motif) ligand 4 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_12_production_by_T_cells = "OBI:0001759"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-X-C motif) ligand 12 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_13_production_by_T_cells = "OBI:0001760"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-X-C motif) ligand 13 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_16_production_by_T_cells = "OBI:0001761"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-X-C motif) ligand 16 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_21_production_by_T_cells = "OBI:0001762"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-C motif) ligand 21 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_22_production_by_T_cells = "OBI:0001763"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-C motif) ligand 22 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_4_production_by_T_cells = "OBI:0001764"
    """
    A cytometric bead array assay that detects chemokine (C-C motif) ligand 4 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_4_production_by_T_cells = "OBI:0001765"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-C motif) ligand 4 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_vascular_endothelial_growth_factor_production_by_T_cells = "OBI:0001766"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects vascular endothelial growth factor production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_19_production_by_T_cells = "OBI:0001767"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-C motif) ligand 19 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_1_production_by_T_cells = "OBI:0001768"
    """
    A flow cytometry assay that detects chemokine (C-C motif) ligand 1 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_vascular_endothelial_growth_factor_production_by_T_cells = "OBI:0001770"
    """
    A flow cytometry assay that detects vascular endothelial growth factor production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_vascular_endothelial_growth_factor_production_by_T_cells = "OBI:0001771"
    """
    An enzyme-linked immunospot assay that detects vascular endothelial growth factor production by T cells.
    """
    assay_measuring_epitope_specific_interleukin_17F_production_by_T_cells = "OBI:0001772"
    """
    An assay of epitope specific interleukin-17 production by T cells that detects interleukin-17F production.
    """
    assay_measuring_epitope_specific_interleukin_17A_production_by_T_cells = "OBI:0001773"
    """
    An assay of epitope specific interleukin-17 production by T cells that detects interleukin-17A production.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_21_production_by_T_cells = "OBI:0001774"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-C motif) ligand 21 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_19_production_by_T_cells = "OBI:0001775"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-C motif) ligand 19 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_12_production_by_T_cells = "OBI:0001776"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-X-C motif) ligand 12 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_22_production_by_T_cells = "OBI:0001777"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-C motif) ligand 22 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_16_production_by_T_cells = "OBI:0001778"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-X-C motif) ligand 16 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_X_C_motifRIGHT_PARENTHESIS_ligand_13_production_by_T_cells = "OBI:0001779"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-X-C motif) ligand 13 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_alpha_production_by_T_cells = "OBI:0001780"
    """
    An enzyme-linked immunospot assay that detects macrophage inflammatory protein-1 alpha production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_gamma_production_by_T_cells = "OBI:0001781"
    """
    A cytometric bead array assay that detects macrophage inflammatory protein-1 gamma production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_gamma_production_by_T_cells = "OBI:0001782"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects macrophage inflammatory protein-1 gamma production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_monocyte_chemotactic_protein_1_production_by_T_cells = "OBI:0001783"
    """
    A flow cytometry assay that detects monocyte chemotactic protein-1 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_monocyte_chemotactic_protein_1_production_by_T_cells = "OBI:0001784"
    """
    An enzyme-linked immunospot assay that detects monocyte chemotactic protein-1 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_gamma_production_by_T_cells = "OBI:0001785"
    """
    A flow cytometry assay that detects macrophage inflammatory protein-1 gamma production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_gamma_production_by_T_cells = "OBI:0001786"
    """
    An enzyme-linked immunospot assay that detects inflammatory protein-1 gamma production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_vascular_endothelial_growth_factor_production_by_T_cells = "OBI:0001787"
    """
    A cytometric bead array assay that detects vascular endothelial growth factor production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_tumor_necrosis_factor_superfamily_cytokine_production_by_T_cells = "OBI:0001788"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects tumor necrosis factor superfamily cytokine production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_RANTES_production_by_T_cells = "OBI:0001789"
    """
    A flow cytometry assay that detects RANTES production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_RANTES_production_by_T_cells = "OBI:0001790"
    """
    An enzyme-linked immunospot assay that detects RANTES production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_lymphotoxin_A_production_by_T_cells = "OBI:0001791"
    """
    An enzyme-linked immunospot assay that detects lymphotoxin A production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_macrophage_inflammatory_protein_1_alpha_production_by_T_cells = "OBI:0001792"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects macrophage inflammatory protein-1 alpha production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_lymphotoxin_A_production_by_T_cells = "OBI:0001793"
    """
    A cytometric bead array assay that detects lymphotoxin A production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_lymphotoxin_A_production_by_T_cells = "OBI:0001794"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects lymphotoxin A production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_IP_10_production_by_T_cells = "OBI:0001795"
    """
    An enzyme-linked immunospot assay that detects IP-10 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_IP_10_production_by_T_cells = "OBI:0001796"
    """
    A flow cytometry assay that detects IP-10 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_9_production_by_T_cells = "OBI:0001797"
    """
    An enzyme-linked immunospot assay that detects interleukin-9 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_9_production_by_T_cells = "OBI:0001798"
    """
    A flow cytometry assay that detects interleukin-9 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_9_production_by_T_cells = "OBI:0001799"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-9 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_8_production_by_T_cells = "OBI:0001800"
    """
    An enzyme-linked immunospot assay that detects interleukin-8 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_8_production_by_T_cells = "OBI:0001801"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-8 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_3_production_by_T_cells = "OBI:0001802"
    """
    An enzyme-linked immunospot assay that detects interleukin-3 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_7_production_by_T_cells = "OBI:0001803"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-7 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_7_production_by_T_cells = "OBI:0001804"
    """
    An enzyme-linked immunospot assay that detects interleukin-7 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_7_production_by_T_cells = "OBI:0001805"
    """
    A flow cytometry assay that detects interleukin-7 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_27_production_by_T_cells = "OBI:0001806"
    """
    A flow cytometry assay that detects interleukin-27 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_3_production_by_T_cells = "OBI:0001807"
    """
    A cytometric bead array assay that detects interleukin-3 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_3_production_by_T_cells = "OBI:0001808"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-3 production by T cells.
    """
    assay_measuring_epitope_specific_granzyme_A_release_by_T_cells = "OBI:0001809"
    """
    A T cell epitope specific cytotoxic T cell degranulation assay that detects granzyme A release by T cells.
    """
    assay_measuring_epitope_specific_granulysin_release_by_T_cells = "OBI:0001810"
    """
    A T cell epitope specific cytotoxic T cell degranulation assay that detects granulysin release by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_27_production_by_T_cells = "OBI:0001811"
    """
    A cytometric bead array assay that detects interleukin-27 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_23_production_by_T_cells = "OBI:0001812"
    """
    A flow cytometry assay that detects interleukin-23 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_27_production_by_T_cells = "OBI:0001813"
    """
    An enzyme-linked immunospot assay that detects interleukin-27 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_27_production_by_T_cells = "OBI:0001814"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-27 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_18_production_by_T_cells = "OBI:0001815"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-18 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_18_production_by_T_cells = "OBI:0001817"
    """
    An enzyme-linked immunospot assay that detects interleukin-18 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_22_production_by_T_cells = "OBI:0001821"
    """
    An enzyme-linked immunospot assay that detects interleukin-22 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_23_production_by_T_cells = "OBI:0001822"
    """
    An enzyme-linked immunospot assay that detects interleukin-23 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_18_production_by_T_cells = "OBI:0001824"
    """
    A flow cytometry assay that detects interleukin-18 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_21_production_by_T_cells = "OBI:0001826"
    """
    An enzyme-linked immunospot assay that detects interleukin-21 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_1_production_by_T_cells = "OBI:0001827"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-C motif) ligand 1 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_1_production_by_T_cells = "OBI:0001828"
    """
    A cytometric bead array assay that detects chemokine (C-C motif) ligand 1 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_1_production_by_T_cells = "OBI:0001829"
    """
    An enzyme-linked immunospot assay that detects chemokine (C-C motif) ligand 1 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_17F_production_by_T_cells = "OBI:0001830"
    """
    An enzyme-linked immunospot assay that detects interleukin-17F production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_17F_production_by_T_cells = "OBI:0001831"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-17F production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_17F_production_by_T_cells = "OBI:0001832"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-17F production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_17A_production_by_T_cells = "OBI:0001833"
    """
    An enzyme-linked immunospot assay that detects interleukin-17A production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_18_production_by_T_cells = "OBI:0001835"
    """
    A cytometric bead array assay that detects interleukin-18 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_16_production_by_T_cells = "OBI:0001836"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-16 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_16_production_by_T_cells = "OBI:0001837"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-16 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_16_production_by_T_cells = "OBI:0001838"
    """
    An enzyme-linked immunospot assay that detects interleukin-16 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_16_production_by_T_cells = "OBI:0001839"
    """
    A flow cytometry assay that detects interleukin-16 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_17A_production_by_T_cells = "OBI:0001840"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-17A production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_1_beta_production_by_T_cells = "OBI:0001841"
    """
    A flow cytometry assay that detects interleukin-1 beta production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_1_beta_production_by_T_cells = "OBI:0001842"
    """
    An enzyme-linked immunospot assay that detects interleukin-1 beta production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_measuring_epitope_specific_interleukin_15_production_by_T_cells = "OBI:0001843"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-15 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_12_production_by_T_cells = "OBI:0001844"
    """
    An enzyme-linked immunospot assay that detects interleukin-12 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_15_production_by_T_cells = "OBI:0001845"
    """
    A flow cytometry assay that detects interleukin-15 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_15_production_by_T_cells = "OBI:0001846"
    """
    An enzyme-linked immunospot assay that detects interleukin-15 production by T cells.
    """
    chromatin_interaction_analysis_by_paired_end_tag_sequencing_assay = "OBI:0001848"
    """
    An assay that incorporates chromatin immunoprecipitation (ChIP)-based enrichment, chromatin proximity ligation, Paired-End Tags, and high-throughput sequencing to determine de novo long-range chromatin interactions genome-wide.
    """
    structural_analysis_by_paired_end_tag_sequencing_assay = "OBI:0001849"
    """
    An assay that incorporates Paired-End Tags and sequencing technology to determine structural variants.
    """
    transcript_analysis_by_paired_end_tag_sequencing_assay = "OBI:0001850"
    """
    A transcription profiling by RNA sequencing assay that employs paired-end sequencing of RNA transcripts to determine things such as gene expression, gene structure, and alternative transcript structure.
    """
    DNase_I_hypersensitive_sites_sequencing_assay = "OBI:0001853"
    """
    An assay that identifies the location of regulatory regions, based on the genome-wide sequencing of regions super sensitive to cleavage by DNase I.
    """
    RNP_LEFT_PARENTHESISribonuclear_particleRIGHT_PARENTHESIS_immunoprecipitation_high__throughput_sequencing_assay = "OBI:0001857"
    """
    An analyte assay that combines immunoprecipitation of an RNA-binding protein and RNA-seq to identify mRNAs associated with selected RNA binding proteins (RBPs).
    """
    cross_linking_immunoprecipitation_high_throughput_sequencing_assay = "OBI:0001858"
    """
    An analyte assay that employs UV-crosslinking between RNA and a protein, followed by immunoprecipitation with antibodies for the protein, fragmentation, and high-throughput screening for RNA sequences that interact with a particular RNA-binding protein.
    """
    formaldehyde_assisted_isolation_of_regulatory_elements_assay = "OBI:0001859"
    """
    An assay to determine the sequences of those DNA regions in the genome associated with regulatory activity.
    """
    methylation_sensitive_restriction_enzyme_sequencing_assay = "OBI:0001861"
    """
    An assay that identifies unmethylated CpGs using methylation sensitive restriction enzymes to fragment DNA.
    """
    reduced_representation_bisulfite_sequencing_assay = "OBI:0001862"
    """
    A bisulfite sequencing assay that identifies genomic methylation patterns using a bisulfite based protocol that enriches CG-rich parts of the genome.
    """
    shotgun_bisulfite_seq_assay = "OBI:0001863"
    """
    A bisulfite sequencing assay that identifies methylated cytosines across the genome using high throughput sequencing.
    """
    RNA_Annotation_and_Mapping_of_Promoters_for_the_Analysis_of_Gene_Expression_assay = "OBI:0001864"
    """
    A transcription profiling by RNA sequencing assay that identifies transcription start sites (TSS), the quantification of their expression and the characterization of their transcripts using high throughput sequencing.
    """
    DNA_replication_timing_by_array_assay = "OBI:0001915"
    """
    An assay which quantifies the timing of DNA replication as a function of genome position using array technology.
    """
    RNA_binding_protein_immunoprecipitation_array_profiling_assay = "OBI:0001918"
    """
    An assay that combines immunoprecipitation of an RNA-binding protein and array technology to identify mRNAs associated with selected RNA binding proteins (RBPs).
    """
    Carbon_copy_chromosome_conformation_capture_assay = "OBI:0001919"
    """
    An assay that measures the organization of chromosomes at the genome-wide scale.
    """
    DNA_replication_timing_by_sequencing_assay = "OBI:0001920"
    """
    An assay in which timing of DNA replication is quantified as a function of genome position based on genome-wide sequencing.
    """
    RNA_binding_protein_immunoprecipitation_tiling_array_profiling_assay = "OBI:0001921"
    """
    An RNA-binding protein immunoprecipitation array profiling assay that combines immunoprecipitation of an RNA-binding protein and RNA tiling array to identify mRNAs associated with selected RNA binding proteins (RBPs).
    """
    microRNA_profiling_by_high_throughput_sequencing_assay = "OBI:0001922"
    """
    A microRNA profiling assay that analyzes the microRNA component of the transcriptome using high throughput sequencing technology.
    """
    protein_sequencing_by_tandem_mass_spectrometry_assay = "OBI:0001923"
    """
    A sequencing assay that detremines amino acid sequences of proteins using multiple rounds of mass spectrometry and molecule fragmentation.
    """
    micrococcal_nuclease_digestion_followed_by_high_throughput_sequencing_assay = "OBI:0001924"
    """
    An assay that identifies nucleosome positioning by genome wide sequencing of regions sensitive to digestion by micrococal nuclease
    """
    chromatin_immunoprecipitation_with_exonuclease_sequencing_assay = "OBI:0001925"
    """
    A ChIP-seq assay which uses immunoprecipitation to isolate protein bound DNA followed by an exonuclease step to degrade DNA that is not protein bound to provide greater resolution of the DNA binding site
    """
    microRNA_profiling_assay = "OBI:0001926"
    """
    A transcription profiling assay that quantifies the microRNA species within a biological sample.
    """
    ChIP_assay = "OBI:0001954"
    """
    An assay in which portions of chromatin, the ordered and organized complex of DNA and its interaction partners that make up a chormosome, is extracted and purified by immunoprecipitation with antibodies or tags, and subsequently analyzed
    """
    assay_using_chromatin_immunoprecipitation = "OBI:0001956"
    """
    An assay that produces data about protein-DNA interaction or DNA epigenetic modification using immunoprecipitation
    """
    taxonomic_diversity_assessment_by_targeted_gene_survey = "OBI:0001960"
    """
    An assay that dteremines taxonomic and community diversity information by sequencing specific genomic regions used as marker of identity or diversity.
    """
    hydrogenSOLIDUSdeuterium_exchange_footprinting_assay = "OBI:0001976"
    """
    A footprinting assay that uses a chemical reaction whereby a covalently bonded hydrogen atom is replaced by a deuterium atom, or vice versa in order to gather information about the solvent accessibility of parts of a molecule and thus its tertiary structure.
    """
    cytometry_assay = "OBI:0001977"
    """
    An assay that counts and/or measures characteristics of cells.
    """
    immunoblot_assay = "OBI:0001978"
    """
    An analyte assay that detects specific molecules in an input material by separating it using gel electrophoresis, transfering the separated molecules to a membrane, and staining them with_ antibodies specific to the analyte molecules.
    """
    fluorescence_quenching_binding_assay = "OBI:0001979"
    """
    A binding assay in which the proximity of two entities is monitored by measuring a fluorescent signal of one of the entities that gets reduced if the two entities are cliose to each other.
    """
    in_vivo_intervention_experiment = "OBI:0001980"
    """
    An assay in which the effect of a targeted process (the intervention) on an organism is tested.
    """
    disease_exacerbation_in_vivo_intervention_experiment = "OBI:0001981"
    """
    An in vivo intervention experiment that tests the ability of the intervention to increase the severity of a disease in the host.
    """
    protection_from_challenge_in_vivo_intervention_experiment = "OBI:0001982"
    """
    An in vivo intervention experiment that tests the ability of the intervention to prevent occurrence of a disease in a host.
    """
    tolerance_induction_intervention_experiment = "OBI:0001983"
    """
    An in vivo intervention experiment that tests the ability of the intervention to decrease an immune response.
    """
    treatment_intervention_experiment = "OBI:0001984"
    """
    An in vivo intervention experiment in which the ability of the intervention to reduce or cure the effects of a disease are tested.
    """
    microarray_assay = "OBI:0001985"
    """
    An analyte assay where binding of the analyte to immobilized matrix is measured.
    """
    immunohistochemistry = "OBI:0001986"
    """
    An immunostaining assay to detect and potentially localize antigens within the cells of a tissue section.
    """
    assay_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_MHCCOLONligand_complex = "OBI:0001987"
    """
    A MHC binding constant determination assay measuring equilibrium association constant (KA).
    """
    assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_MHCCOLONligand_complex = "OBI:0001988"
    """
    A MHC binding constant determination assay measuring equilibrium dissociation constant (KD).
    """
    radioactivity_detection_assay_measuring_equilibrium_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_to_determine_competitive_binding_of_a_purified_MHCCOLONligand_complex = "OBI:0001989"
    """
    A radioactivity detection assay that measures equilibrium dissociation constant (KD) to detect the loss of binding of a known reference ligand to purified-MHC due to competition by the ligand under investigation.
    """
    assay_measuring_the_half_life_of_a_MHCCOLONligand_complex = "OBI:0001990"
    """
    A MHC binding constant determination assay measuring half life of binding.
    """
    assay_measuring_the_half_maximal_effective_concentration_LEFT_SQUARE_BRACKETEC50RIGHT_SQUARE_BRACKET_of_a_MHCCOLONligand_complex = "OBI:0001991"
    """
    A MHC binding constant determination assay measuring half maximal effective concentration (EC50).
    """
    assay_measuring_the_half_maximal_inhibitory_concentration_LEFT_SQUARE_BRACKETIC50RIGHT_SQUARE_BRACKET_of_a_MHCCOLONligand_complex = "OBI:0001992"
    """
    A MHC binding constant determination assay measuring half maximal inhibitory concentration (IC50).
    """
    assay_measuring_the_off_rate_measurement_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_of_a_MHCCOLONligand_complex = "OBI:0001993"
    """
    A MHC binding constant determination assay measuring binding off rate measurement data item (koff).
    """
    assay_measuring_the_MHC_ligand_binding_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_of_a_MHCCOLONligand_complex = "OBI:0001994"
    """
    A MHC binding constant determination assay measuring binding on rate (kon).
    """
    chromatography_assay_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001995"
    """
    An analytical chromatography assay that measures the association constant [KA] of an antigen binding with an antibody.
    """
    chromatography_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001996"
    """
    An analytical chromatography assay that measures the dissociation constant [KD] of an antigen binding with an antibody.
    """
    hydrogenSOLIDUSdeuterium_exchange_footprinting_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001997"
    """
    A hydrogen/deuterium exchange footprinting assay that detects the binding of an antigen with an antibody.
    """
    immunohistochemistry_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0001998"
    """
    A immunohistochemistry assay that detects the binding of an antigen with an antibody.
    """
    number_3D_molecular_structure_determination_assay_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0001999"
    """
    A 3D structure determination of bound molecular complex assay that characterizes the 3-dimensional structure of a T cell epitope:MHC:TCR complex.
    """
    DNA_methylation_profiling_by_ChIP_chip_assay = "OBI:0002014"
    """
    An epigenetic modification assay that identifies sites of DNA methylation using ChIP-chip technologies.
    """
    transcription_profiling_by_MPSS_assay = "OBI:0002015"
    """
    A transcription profiling assay that uses Massive Parallel Signature Sequencing (MPSS).
    """
    histone_modification_identification_by_ChIP_chip_assay = "OBI:0002016"
    """
    An epigenetic modification assay that identifies regions containing specific histones and their modifications using ChIP-chip techniques.
    """
    histone_modification_identification_by_ChIP_Seq_assay = "OBI:0002017"
    """
    An epigenetic modification assay that identifies regions containing specific histones and their modifications using ChIP-Seq techniques.
    """
    transcription_factor_binding_site_identification_by_ChIP_chip_assay = "OBI:0002018"
    """
    A transcription factor binding site assay that utilizes ChIP-chip technology.
    """
    transcription_factor_binding_site_identification_by_ChIP_Seq_assay = "OBI:0002019"
    """
    A transcription factor binding site assay that utilizes ChIP-seq technology.
    """
    epigenetic_modification_assay = "OBI:0002020"
    """
    An assay that identifies epigenetic modifications including histone modifications, open chromatin, and DNA methylation.
    """
    serial_analysis_of_gene_expression_assay = "OBI:0002029"
    """
    A transcription profiling by RNA sequencing assay that quantifies RNA through creating short signature tags of the messages and ligating them into a larger molecule that is then sequenced.
    """
    genotyping_by_tiling_array_assay = "OBI:0002030"
    """
    A genotyping by array assay that uses tiling array technology.
    """
    genotyping_by_SNP_array_assay = "OBI:0002031"
    """
    A genotyping by array assay that uses SNP array technology.
    """
    parallel_analysis_of_RNA_structure_assay = "OBI:0002032"
    """
    A single-nucleotide-resolution nucleic acid structure mapping assay that performs simultaneous in vitro profiling of the secondary structure of thousands of RNA species at single nucleotide resolution using enzymatic probing based on deep sequencing fragments of RNAs that were treated with structure-specific enzymes
    """
    translation_associated_transcript_leader_sequencing_assay = "OBI:0002033"
    """
    A translation profiling assay that combines transcript leader sequencing with polysome fractionation. TATL-seq works by applying TL-seq across fractions of a polysome gradient, generating TL-specific translational measurements to identify how different transcript leader sequences effect translation.
    """
    transcript_leader_sequencing_assay = "OBI:0002034"
    """
    A transcription profiling by RNA sequencing assay that combines enzymatic capture of m(7)G-capped mRNA 5' ends with high-throughput sequencing.
    """
    peptide_mass_fingerprinting_assay = "OBI:0002035"
    """
    A mass spectrometry assay that measures the absolute mass of the cleaved peptides derived from an unknown protein of interest. These masses are then compared to values for known protein sequences to identify the unknown protein.
    """
    array_based_nucleic_acid_structure_mapping_assay = "OBI:0002036"
    """
    An assay which aims to provide information about the in vivo organization/structure of nucleic acids using chemical or enzymatic probes using a microarray.
    """
    micrococcal_nuclease_digestion_followed_by_tiling_array_assay = "OBI:0002037"
    """
    An array based nucleic acid structure mapping assay that identifies nucleosome positions genome wide, by detection of regions protected by nucleosomes from digestion by micrococal nuclease using tiling array assays
    """
    ribosomal_profiling_by_sequencing_assay = "OBI:0002038"
    """
    A translation profiling assay that sequences only mRNA protected by the ribosome during translation and thus provides information on which transcipts are undergoing active translation.
    """
    assay_for_transposase_accessible_chromatin_using_sequencing = "OBI:0002039"
    """
    An assay to capture the location of open chromatin, DNA-binding proteins, individual nucleosomes and chromatin compaction at nucleotide resolution by Tn5 transposase insertion.
    """
    chromatin_isolation_by_RNA_purification_sequencing_assay = "OBI:0002040"
    """
    A detection of specific nucleic acids with complementary probes assay that measures regions of the genome which are bound by a specific RNA (or a by a ribonucleoprotein containing the RNA of interest) using high-throughput sequencing.
    """
    self_transcribing_active_regulatory_region_sequencing_assay = "OBI:0002041"
    """
    An assay that identifies the sequences that act as transcriptional enhancers in a direct, quantitative, and genome-wide manner from sheared genomic DNA.
    """
    carbon_copy_chromosome_conformation_capture_assay_followed_by_sequencing_assay = "OBI:0002042"
    """
    A carbon-copy chromosome conformation capture assay to analyze the organization of chromosomes in an unbiased, genome-wide manner using high throughput sequening following carbon-copy chromosome conformation capture.
    """
    individual_nucleotide_resolution_cross_linking_and_immunoprecipitation_sequencing_assay = "OBI:0002043"
    """
    A cross-linking immunoprecipitation high-throughput sequencing assay that identifies protein-RNA interactions using UV light to covalently bind proteins and RNA molecules, allowing for a very stringent purification of the linked protein-RNA complexes.
    """
    RNA_Bind_n_Seq_assay = "OBI:0002044"
    """
    An assay that comprehensively characterizes sequence and structural specificity of RNA binding proteins (RBPs).
    """
    polyA_site_sequencing_assay = "OBI:0002045"
    """
    A transcription profiling by RNA sequencing assay that quantitatively profiles RNA polyadenylation at the transcriptome level.
    """
    number_3D_molecular_structure_determination_assay_of_a_MHCCOLONligand_complex = "OBI:0002050"
    """
    A 3D structure determination of bound molecular complex assay that characterizes the 3-dimensional structure of a MHC:ligand complex.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_infectious_challenge_based_on_pathogen_burden = "OBI:0002051"
    """
    An in vivo assay measuring B cell epitope specific protection from pathogen challenge using pathogen burden.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_after_tumor_burden_challenge = "OBI:0002052"
    """
    An in vivo assay measuring B cell epitope specific protection from tumor challenge using tumor burden.
    """
    microarray_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002053"
    """
    A microarray assay that detects the binding of an antigen with an antibody.
    """
    NMR_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002054"
    """
    A B cell epitope equilibrium dissociation constant (KD) determination assay that uses a nuclear magnetic resonance assay.
    """
    assay_measuring_biological_activity_resulting_from_T_cell_epitopeCOLONMHCCOLONTCR_binding = "OBI:0002055"
    """
    A T cell epitope recognition assay that measures the immune response process resulting from the binding of a T cell receptor to epitope or the recongition of the epitope.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_17_production_by_T_cells = "OBI:0002056"
    """
    A T cell epitope specific cytokine production assay that detects production of chemokine (C-C motif) ligand 17 production by T cells.
    """
    assay_measuring_epitope_specific_macrophage_migration_inhibitory_factor_LEFT_PARENTHESISMIFRIGHT_PARENTHESIS_production_by_T_cells = "OBI:0002057"
    """
    A T cell epitope specific cytokine production assay that detects macrophage migration inhibitory factor (MIF) production by T cells.
    """
    assay_measuring_epitope_specific_oncostatin_M_production_by_T_cells = "OBI:0002058"
    """
    A T cell epitope specific cytokine production assay that detects oncostatin M production by T cells.
    """
    assay_measuring_a_binding_constant_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0002059"
    """
    A T cell epitope recognition assay that quantitavely characterizes the binding of a TCR with a ligand by determining a binding constant.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_17_production_by_T_cells = "OBI:0002060"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects chemokine (C-C motif) ligand 17 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_22_production_by_T_cells = "OBI:0002061"
    """
    A cytometric bead array assay that detects chemokine (C-C motif) ligand 22 production by T cells.
    """
    in_vitro_assay_measuring_epitope_specific_T_cell_killing = "OBI:0002062"
    """
    An in vitro cell killing assay that measures the killing of antigen presenting cells (APC) by T cells whose TCR recognizes an epitope presented by the APC.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_granzyme_A_release_by_T_cells = "OBI:0002063"
    """
    A cytometric bead array assay that detects epitope specific granzyme A release by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_granzyme_A_release_by_T_cells = "OBI:0002064"
    """
    A detection of specific nucleic acids with complementary probes assay that detects epitope specific granzyme A release by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_granzyme_B_release_by_T_cells = "OBI:0002065"
    """
    A cytometric bead array assay that detects epitope specific granzyme B release by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_granzyme_B_release_by_T_cells = "OBI:0002066"
    """
    A detection of specific nucleic acids with complementary probes assay that detects epitope specific granzyme B release by T cells
    """
    cytometric_bead_array_assay_measuring_epitope_specific_macrophage_migration_inhibitory_factor_LEFT_PARENTHESISMIFRIGHT_PARENTHESIS_production_by_T_cells = "OBI:0002067"
    """
    A cytometric bead array assay that detects macrophage migration inhibitory factor (MIF) production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_oncostatin_M_production_by_T_cells = "OBI:0002068"
    """
    A cytometric bead array assay that detects oncostatin M production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_perforin_release_by_T_cells = "OBI:0002069"
    """
    An enzyme-linked immunospot assay that detects epitope specific perforin release by T cells.
    """
    in_vivo_assay_measuring_epitope_specific_proliferation_of_T_cells = "OBI:0002070"
    """
    A T cell epitope specific proliferation assay that is performed in vivo.
    """
    in_vitro_assay_measuring_epitope_specific_proliferation_of_T_cells = "OBI:0002071"
    """
    A T cell epitope specific proliferation assay that is performed on cells in vitro.
    """
    assay_measuring_qualitative_binding_of_a_MHCCOLONligand_complex = "OBI:0002072"
    """
    An assay that detects the binding of a MHC molecule with a ligand, and produces a qualitative measurement of the binding as an output.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_challenge = "OBI:0002073"
    """
    An efficacy of T cell epitope intervention experiment that uses a epitope protection experiment.
    """
    assay_measuring_T_cell_epitope_specific_suppression_in_vitro = "OBI:0002074"
    """
    T cell epitope dependent biological activity assay that detects suppression of an in vitro response.
    """
    MHC_ligand_assay = "OBI:0002075"
    """
    An immune epitope assay that characterizes the structrue of a MHC-ligand complex, or detects the processing and presentation of a ligand by an antigen presenting cell, or the binding of a ligand to an MHC molecule.
    """
    reporter_gene_assay = "OBI:0002082"
    """
    An assay that detects expression of a reporter gene that was inserted under the control of a regulatory sequence of interest.
    """
    enhancer_activity_detection_by_reporter_gene_assay = "OBI:0002083"
    """
    A reporter gene assay that detects expression of a reporter gene that was inserted under the control of an enhancer of interest.
    """
    transcription_cofactor_activity_region_identification_by_ChIP_Seq_assay = "OBI:0002084"
    """
    A ChIP-seq assay that identifies regions of chromatin bound to a chromatin modifying protein, e.g. a histone acetyltransferase.
    """
    transcript_expression_location_detection_by_hybridization_chain_reaction_assay = "OBI:0002085"
    """
    An in situ hybridization assay in which the location (e.g. anatomical/tissue) of a transcript is detected by a multiplexed fluorescent in situ hybridization, based on orthogonal amplification with hybridization chain reactions (HCR). RNA probes complementary to mRNA targets trigger chain reactions in which fluorophore-labeled RNA hairpins self-assemble into tethered fluorescent amplification polymers.
    """
    Tet_assisted_bisulfite_sequencing_assay = "OBI:0002086"
    """
    A bisulfite sequencing assay that identifies genomic methylation patterns by using a bisulfite based protocol with the Tet enzyme to differentiate 5-hydroxylmethylcytosine (5hmC) from 5-methylcytosine (5mC) through a step-wise oxidative demethylation of 5mC, converting it to 5-carboxylcytosine (5caC) while keeping 5hmC protected.
    """
    MethylC_Capture_sequencing_assay = "OBI:0002094"
    """
    A bisulfite sequencing assay in which a whole-genome sequencing library is prepared, bisulfite converted and amplified, followed by a capture enriching for targeted bisulfite-converted DNA fragments that are are subsequently identified by DNA sequencing.
    """
    carboxyfluorescein_succinimidyl_ester_staining_assay_measuring_epitope_specific_proliferation_of_T_cells = "OBI:0002096"
    """
    A CFSE assay that detects T cell epitope specific proliferation in vitro.
    """
    assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0002097"
    """
    A T cell epitope binding constant determination assay that measures the dissociation constant KD.
    """
    assay_measuring_the_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0002098"
    """
    A T cell epitope binding constant determination assay that measures the on rate.
    """
    assay_measuring_the_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0002099"
    """
    A T cell epitope binding constant determination assay that measures the off rate.
    """
    assay_measuring_the_association_constant_LEFT_SQUARE_BRACKETKARIGHT_SQUARE_BRACKET_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0002100"
    """
    A T cell epitope binding constant determination assay that measures the association constant KA.
    """
    small_angle_scattering_assay_determining_the_3D_structure_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002101"
    """
    A small-angle scattering 3D molecular structure determination assay that characterizes the 3-dimensional molecular structure of a B cell epitope:antibody complex
    """
    bio_layer_interferometry_assay_measuring_the_on_rate_LEFT_SQUARE_BRACKETkonRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002102"
    """
    A bio-layer interferometry assay that measures the on rate of an antigen with an antibody.
    """
    bio_layer_interferometry_assay_measuring_the_off_rate_LEFT_SQUARE_BRACKETkoffRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002103"
    """
    A bio-layer interferometry assay that measures the off rate of an antigen with an antibody.
    """
    bio_layer_interferometry_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002104"
    """
    A bio-layer interferometry assay that detects the binding of an antigen with an antibody.
    """
    bio_layer_interferometry_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002105"
    """
    A bio-layer interferometry assay that measures the dissociation constant [KD] of an antigen with an antibody.
    """
    carboxyfluorescein_succinimidyl_ester_staining_assay = "OBI:0002106"
    """
    An assay using carboxyfluorescein succinimidyl ester staining.
    """
    bio_layer_interferometry_assay = "OBI:0002107"
    """
    A binding assay that detects a shift in the interference pattern reflected from a layer of immobilized material on the biosensor tip to measure binding to- or dissociating from the material on the biosensor.
    """
    small_angle_scattering_3D_molecular_structure_determination_assay = "OBI:0002108"
    """
    A 3D molecular structure determination assay in which the scattering pattern of a neutron or x-ray beam targeted at a material entity is recorded at small angles relative to the incident beam to determine the size, shape and structure of the material entity examined.
    """
    enhanced_cross_linking_immunoprecipitation_high_throughput_sequencing_assay = "OBI:0002111"
    """
    An iCLIP assay that is enhanced to robustly identify protein-RNA interactions with high efficiency through improvements in library preparation of RNA fragments.
    """
    small_RNA_sequencing_assay = "OBI:0002112"
    """
    A transcription profiling by RNA sequencing assay which is targeting small RNA (< 200 bp) sequences such as, but not exclusive to, miRNAs using, for example, small RNA library preparation kits.
    """
    bromouridine_labeling_and_sequencing_assay = "OBI:0002113"
    """
    A transcription profiling by RNA sequencing assay used to identify spans of nascent transcription in the genome through isolation of recent bromouridine (Bru) labelled RNAs.
    """
    bromouridine_pulse_chase_and_sequencing_assay = "OBI:0002114"
    """
    A transcription profiling by RNA sequencing assay used to identify RNA populations of specific ages through isolation of RNAs first labelled with bromouridine (Bru) followed by chasing in uridine for different periods of time.
    """
    cytometry_time_of_flight_assay = "OBI:0002115"
    """
    A cytometry assay in which the presence of molecules of interest on or in cells is indicated by binding of antibodies labeled with rare earth element tags which are detected by time-of-flight mass spectrometry.
    """
    high_performance_liquid_chromatography_assay = "OBI:0002116"
    """
    An analytical chromatography assay that utilizes a high performance liquid chromatography instrument for separation of compounts in a solution.
    """
    whole_genome_sequencing_assay = "OBI:0002117"
    """
    A DNA sequencing assay that intends to provide information about the sequence of an entire genome of an organism.
    """
    exome_sequencing_assay = "OBI:0002118"
    """
    A DNA sequencing assay that intends to provide information about the sequence of the protein coding components of a genome (exons).
    """
    microscopy_assay = "OBI:0002119"
    """
    An imaging assay that utilizes a microscope to magnify features of the visualized material of interest that are not visible to naked eye.
    """
    mixed_lymphocyte_reaction_assay = "OBI:0002120"
    """
    A cytometry assay where lymphocytes from two individuals are co-cultured with the lymphocytes from one of the allogeneic individuals (Responders) being labeled (with 3H Thymidine or BrdU) and the proliferation of the labeled cells is measured, which is thought to reflect recognition of histocompatibility antigens on the unlabeled cells (stimulators).
    """
    killer_cell_immunoglobulin_like_receptor_typing_assay = "OBI:0002121"
    """
    A genotyping assay in which the alleles of genes encoding for killer cell immunoglobulin-like receptors are determined.
    """
    major_histocompatibility_typing_assay = "OBI:0002122"
    """
    A genotyping assay in which the alleles of genes encoding for major histocompatibility complex molecules are determined.
    """
    pulse_stable_isotope_labeling_by_amino_acids_in_cell_culture = "OBI:0002132"
    """
    An assay that detects differences in protein abundance using samples that have been metabolically labeled in vivo with a stable non-radioactive heavy isotope containing amino acid for a short period of time. After diluting the pulsed cells into growth media without label, high resolution mass spectrometry-based proteomics is used to analyze the time-dependent decay and determine protein stability.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_20_production_by_T_cells = "OBI:0002133"
    """
    A cytometric bead array assay that detects chemokine (C-C motif) ligand 20 production by T cells.
    """
    assay_measuring_epitope_specific_chemokine_LEFT_PARENTHESISC_C_motifRIGHT_PARENTHESIS_ligand_20_production_by_T_cells = "OBI:0002134"
    """
    A T cell epitope specific cytokine production assay that detects chemokine (C-C motif) ligand 20 production by T cells.
    """
    temperature_measurement_assay = "OBI:0002140"
    """
    An assay to determine the temperature of an evaluant.
    """
    volume_measurement_assay = "OBI:0002141"
    """
    An assay to determine the volume of an evaluant.
    """
    Nanostring_nCounter_miRNA_expression_assay = "OBI:0002142"
    """
    A microRNA profiling assay using digital molecular barcoding technology to quantify target microRNA molecules without the need for amplification.
    """
    bromouride_labeling_and_sequencing_after_UV_exposure = "OBI:0002143"
    """
    A transcription profiling by RNA sequencing assay used to identify transcription start sites and active enhancer elements through isolation of bromouridine (Bru) labelled RNAs after UV light exposure introduces transcription-blocking lesions.
    """
    extrachromosomal_circular_DNA_sequencing_assay = "OBI:0002144"
    """
    An assay which aims at identifying the endogenous population of extrachromosomal circular DNA originating from a subset of genomic loci and potentially having profound consequences on the regulatory and coding capabilities of these regions. The assay includes creation of a library out of the circular DNA molecules and subsequent sequencing using parallelized sequencing methods.
    """
    antigen_specific_antibodies_assay = "OBI:0002145"
    """
    An analyte assay that measures the presence or amount of antibodies to a specified antigen.
    """
    HIV_antibody_assay = "OBI:0002146"
    """
    An antigen specific antibodies assay that is meant to detect antibodies that bind to human immunodeficiency virus (HIV) antigens.
    """
    HIV_group_O_antibody_assay = "OBI:0002147"
    """
    An antigen specific antibodies assay that is meant to detect antibodies that bind to human immunodeficiency virus (HIV) group O antigens.
    """
    surface_HBV_antibody_assay = "OBI:0002148"
    """
    An antigen specific antibodies assay that is meant to detect antibodies that bind to hepatitis B virus (HBV) surface antigens.
    """
    core_HBV_antibody_assay = "OBI:0002149"
    """
    An antigen specific antibodies assay that is meant to detect antibodies that bind to hepatitis B virus (HBV) core antigens.
    """
    core_HBV_IgM_antibody_assay = "OBI:0002150"
    """
    An antigen specific antibodies assay that is meant to detectimmunoglobulin M (IgM) antibodies that bind to hepatitis B virus (HBV) core antigens.
    """
    HCV_antibody_assay = "OBI:0002151"
    """
    An antigen specific antibodies assay that is meant to detect antibodies that bind to Hepacivirus C (HCV) antigens.
    """
    EBV_IgG_antibody_assay = "OBI:0002152"
    """
    An antigen specific antibodies assay that is meant to detect immunoglobulin G (IgG) antibodies that bind to Epstein-Barr virus (EBV) antigens.
    """
    EBV_IgM_antibody_assay = "OBI:0002153"
    """
    An antigen specific antibodies assay that is meant to detect immunoglobulin M (IgM) antibodies that bind to Epstein-Barr virus (EBV) antigens.
    """
    CMV_antibody_assay = "OBI:0002154"
    """
    An antigen specific antibodies assay that is meant to detect antibodies that bind to cytomegalovirus (CMV) antigens.
    """
    venereal_disease_research_laboratory_test = "OBI:0002155"
    """
    An analyte assay that is meant to detect general antibodies that react with substances that are produced by cellular damage caused by Treponema pallidum indicating a syphilis infection. VDRL tests require a microscope and can be done on cerebrospinal fluid as well as blood.
    """
    rapid_plasma_reagin_test = "OBI:0002156"
    """
    An analyte assay that is meant to detect with the aid of carbon or charcoal particles general antibodies that react with substances that are produced by cellular damage caused by Treponema pallidum indicating a syphilis infection. RPR tests can be done without a microscope.
    """
    HBV_surface_antigen_assay = "OBI:0002157"
    """
    An analyte assay that is meant to detect hepatitis B virus (HBV) surface antigens.
    """
    HIV_1_nucleic_acid_testing = "OBI:0002158"
    """
    An analyte assay that is meant to detect human immunodeficiency virus (HIV-1) nucleic acids.
    """
    HCV_nucleic_acid_testing = "OBI:0002159"
    """
    An analyte assay that is meant to detect hepatitis C virus (HCV) nucleic acids.
    """
    multiplexed_indexed_T7_ChIP_seq_assay = "OBI:0002160"
    """
    A ChIP-seq assay which leverages T7 promoter amplification to allow low sample input and chromatin barcoding and pool-and-split multiplexing for high-throughput, quantitative profiling of chromatin states.
    """
    systematic_evolution_of_ligands_by_exponential_enrichment_assay = "OBI:0002161"
    """
    A binding assay that identifies protein-binding sites on nucleic acids by selecting high-affinity target ligands from a randomized pool. The process is repeated in rounds, then the bound nucleic acids are separated from the unbound nucleic acids and amplified by PCR._
    """
    footprinting_assay = "OBI:0002162"
    """
    An assay that measures ligand binding and conformational changes by the solvent accessibility of the backbone, bases, or side-chain structures of macromolecules through their sensitivity to chemical or enzymatic cleavage or modification reactions.
    """
    DNAse_footprinting_assay = "OBI:0002163"
    """
    An enzymatic footprinting assay that determines protein-binding sites on DNA by identifying bound fragments that are protected from DNAse I-catalyzed hydrolysis
    """
    mammalian_2_hybrid_assay = "OBI:0002164"
    """
    A binding assay that increases the expression of a reporter gene in mammalian cells by proteins of interest attached to two portions of the transcriptional activator, bringing those portions closer together.
    """
    protein_localization_assay = "OBI:0002165"
    """
    An assay that determines the specific location of a protein. Subcellular localization is distinguished from tissue-based localization based on the type of microscopy applied.
    """
    tissue_based_protein_localization_assay = "OBI:0002166"
    """
    A protein localization assay that determines the specific location of a protein in a living tissue sample.
    """
    subcellular_protein_localization_assay = "OBI:0002167"
    """
    A protein localization assay that determines the specific subcellular location of a protein. The location is visualized through electron microscopy.
    """
    subcellular_protein_immunohistochemistry_assay = "OBI:0002168"
    """
    An immunohistochemistry assay that uses antibodies to display the specific subcellular location of proteins.
    """
    ChIP_qPCR_assay = "OBI:0002169"
    """
    A ChIP assay that uses quantitative PCR to determine levels of specific DNA in immunoprecipitated samples.
    """
    genomic_SELEX = "OBI:0002170"
    """
    A systematic evolution of ligands by exponential enrichment assay that starts with a library derived from genomic DNA instead of synthetically derived random DNA molecules.
    """
    dot_blot_assay = "OBI:0002171"
    """
    An analyte assay that detects molecules in a mixture dotted on a membrane using DNA probes or antibodies.
    """
    Northwestern_blot_assay = "OBI:0002172"
    """
    A direct binding assay that detects interactions of labeled RNA with immobilized protein on a membrane.
    """
    Southwestern_blot_assay = "OBI:0002173"
    """
    A direct binding assay that detects interactions of labeled DNA with immobilized protein on a membrane.
    """
    immunocytochemistry = "OBI:0002174"
    """
    An immuno staining assay in which samples of intact cells are examined that have had most, if not all, of their surrounding extracellular matrix removed
    """
    ATP_bioluminescence_assay = "OBI:0002175"
    """
    An analyte assay that detects ATP concentration through light intensity when luciferase catalyzes the oxidation of luciferin in the presence of ATP, magnesium ions, and molecular oxygen.
    """
    electrophysiology_assay = "OBI:0002176"
    """
    An assay that measures the electrical properties of biological cells or tissues. Typically, this assay will generate measurements of voltage changes or electric current (or other associated variables such as impedence or capacitance).
    """
    patch_clamp_assay = "OBI:0002177"
    """
    An intracellular electrophysiology assay where a glass micropipette is sealed to the surface of the cell membrane as a recording electrode to study ion channel activity. The key distinction of this technique is the electrical resistance of the seal between the cell membrane and the pipette is of the order 10-100 gigaohms, permitting high-resolution current measurements over the cell membrane in several different standard configurations.
    """
    whole_cell_patch_clamp_assay = "OBI:0002178"
    """
    A patch-clamp assay where the electrode is left in place on the cell, as in cell-attached recordings, but the membrane patch has been perforated, providing access from the interior of the pipette to the intracellular space of the cell. Measurements made with this technique involve recording currents through multiple channels simultaneously, over the membrane of the entire cell.
    """
    cell_attached_patch_clamp_assay = "OBI:0002179"
    """
    A patch-clamp assay where the electrode is left in place on the cell, and the membrane patch has been left intact been perforated. This maintains the separation of the interior of the pipette to the intracellular space of the cell. Measurements made with this technique involve recording currents through multiple channels simultaneously, over the membrane of the entire cell.
    """
    inside_out_patch_clamp_assay = "OBI:0002180"
    """
    A patch-clamp assay where a patch of the membrane is attached to the patch pipette, detached from the rest of the cell, and the cytosolic surface of the membrane is exposed to the external media, or bath. This provides the experimenter has access to the intracellular surface of the membrane via the bath and can manipulate the environment at the intracellular surface of single ion channels. For example, channels that are activated by intracellular ligands can then be studied through a range of ligand concentrations.
    """
    outside_out_patch_clamp_assay = "OBI:0002181"
    """
    A patch-clamp assay where a patch of the membrane is attached to the patch pipette. In this configuration, the external surface of the cell membrane is exposed as the outside of the membrane patch relative to the patch electrode. An outside-out patch starts with a gigaohm seal in a whole-cell recording configuration. The electrode is slowly withdrawn from the cell, until a fragment of membrane bulges away from the cell, which detaches and reforms as a convex membrane on the end of the electrode, with the original external surface of the membrane facing outward from the electrode. This provides the experimenter with access to the extracellular surface of the membrane via the bath and can manipulate the environment at the extracellular surface of single ion channels.
    """
    voltage_clamp_assay = "OBI:0002182"
    """
    An cellular electrophysiology assay where the membrane potential of a cell is controlled by the experimentalist. This is accomplished through a feedback mechanism where any change in membrane potential is countered by permitting electrical current to flow into or out of the cell.
    """
    two_electrode_voltage_clamp_assay = "OBI:0002183"
    """
    The two electrode voltage clamp (TEVC) method utilizes two low-resistance pipettes, one sensing voltage and the other injecting current. The microelectrodes are filled with conductive solution and inserted into the cell to artificially control membrane potential. The membrane acts as a dielectric as well as a resistor, while the fluids on either side of the membrane function as capacitors.[9] The microelectrodes compare the membrane potential against a command voltage, giving an accurate reproduction of the currents flowing across the membrane. Current readings can be used to analyze the electrical response of the cell to different applications. This technique is mainly used in the Oocyte preparation.
    """
    cut_open_oocyte_voltage_clamp_assay = "OBI:0002184"
    """
    The cut-open oocyte Vaseline gap (COVG) voltage-clamp technique is designed to solve weaknesses in the two elextrode voltage clamp by maximizing the benefits of the Xenopus oocyte expression system by improving on clamp speed, signal-to-noise ratio, and ability to effectively perfuse the oocyte. In this way, it was possible to combine the most popular transient expression system, and the associated benefits of molecular cloning and site-directed mutagenesis, with the superior voltage-clamp properties of cut-open cell techniques.
    """
    current_clamp_assay = "OBI:0002185"
    """
    The current clamp technique records the membrane potential by injecting current into a cell through the recording electrode. Unlike in the voltage clamp mode, where the membrane potential is held at a level determined by the experimenter, in "current clamp" mode the membrane potential is free to vary, and the amplifier records whatever voltage the cell generates on its own or as a result of stimulation. This technique is used to study how a cell responds when electric current enters a cell; this is important for instance for understanding how neurons respond to neurotransmitters that act by opening membrane ion channels.
    """
    electroencephalography = "OBI:0002186"
    """
    An extracellular electrophysiology assay where electrodes are mounted outside the brain (either on the surface of the scalp on onto the brain surface itself during surgery) to measure the electrical field over the external surface.
    """
    single_unit_recording = "OBI:0002187"
    """
    An extracellular electrophysiology assay where a single microelectrode is placed in close proximity to a single neuron to measure voltage and current changes over time. This is the technicque used by Hubel and Wiesel to measure firing properties of primary visual cortex neurons in the 1950s in their original Nobel-prize winning study. A classic, old technique.
    """
    multi_unit_recording = "OBI:0002188"
    """
    An extracellular electrophysiology assay where a collection of microelectrodes (often in an 'array' configuration) is placed into neural tissue to measure the distribution of voltage and current changes for a population of cells over time.
    """
    local_field_potential_recording = "OBI:0002189"
    """
    An extracellular electrophysiology assay where a microelectrode is placed in the extracellular space of brain tissue to measure action potential and compared to an electrode either outside or inside that tissue.
    """
    RNA_interactome_capture = "OBI:0002436"
    """
    An assay that identifies RNA binding proteins by cross-linking RNA and proteins with UV light, then purifying the bound complexes by oligo(dT) capture. Finally, the complexes are analyzed by mass spectrometry.
    """
    widefield_microscopy_assay = "OBI:0002437"
    """
    A fluorescence microscopy technique where the specimen under investigation is fully bathed in light, as opposed to confocal microscopy in which only a small portion of the specimen is illuminated.
    """
    nuclear_ligation_assay = "OBI:0002438"
    """
    An assay that detects the proximity of chromosomal DNA through the use of a ligation reaction in isolated nuclei.
    """
    chromosome_conformation_capture_assay = "OBI:0002439"
    """
    A nuclear ligation assay that detects chromosomal interactions between any two genomic loci. Chromatin segments are cross-linked, cut by restriction enzymes, ligated, and finally analyzed by PCR.
    """
    Hi_C_assay = "OBI:0002440"
    """
    A chromosome conformation capture assay that detects genome-wide chromosomal interactions. High-throughput techniques are used to sequence the ligated fragments after cross-linking and cutting with restriction enzymes.
    """
    physical_examination_of_an_organism = "OBI:0002441"
    """
    An assay that produces a description of the qualities of an organism that has not been transformed, through observation and physical, non-invasive techniques.
    """
    hydroxyl_radical_footprinting_assay = "OBI:0002442"
    """
    A footprinting assay that uses the reaction of hydroxyl radicals with side-chain sites in molecules (proteins, DNA, etc)_ with the resultant mass shift demonstrating the site of modification, used to_ to asses the accessibility of that site.
    """
    methidiumpropyl_EDTA_ironLEFT_PARENTHESISIIRIGHT_PARENTHESIS_footprinting_assay = "OBI:0002443"
    """
    A footprinting assay that determines protein-binding sites on DNA by partial cleavage of ligand-protected DNA restriction fragments with methidium-propyl-EDTA (MPE). MPE-Fe(II) in the presence of oxygen efficiently catalyzes the non-specific clevage of DNA.
    """
    transcription_start_site_mapping_by_primer_extension_assay = "OBI:0002445"
    """
    A transcription profiling assay in which the transcription start site for a gene is determined by identifying the 5' end of mRNA. A radio-labeled primer is annealed to a complementary mRNA sequence near the 3' end, then cDNA is synthesized until the 5' end is reached.
    """
    footprinting_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002449"
    """
    A footprinting assay that detects the binding of an antigen with an antibody.
    """
    hydroxyl_radical_footprinting_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0002450"
    """
    A hydroxyl-radical footprinting assay that detects the binding of an antigen with an antibody.
    """
    ELISA_measuring_epitope_specific_interferon_alpha_production_by_T_cells = "OBI:0002451"
    """
    An enzyme-linked immunosorbent assay that detects interferon-alpha production by T cells.
    """
    assay_measuring_epitope_specific_interferon_alpha_production_by_T_cells = "OBI:0002452"
    """
    A T cell epitope specific cytokine production assay that detects interferon-alpha production by T cells.
    """
    precision_nuclear_run_on_sequencing_assay = "OBI:0002457"
    """
    A transcription profiling by RNA sequencing assay that maps the genome-wide distribution of transcriptionally-engaged Pol II at base-pair resolution by using biotin-labeled ribonucleotide triphosphate analogs (biotin-NTP) for nuclear run-on reactions, allowing the efficient affinity purification of nascent RNAs for high throughput sequencing from their 3' ends.
    """
    chromosome_conformation_capture_on_chip_assay = "OBI:0002458"
    """
    A nuclear ligation assay which uses cross-linking of proteins to proteins and DNA, followed by two rounds of digestion and ligation, inverse PCR, and characterization by microarray or DNA sequencing. This enables unbiased genome-wide screens for DNA contacts made by single genomic sites of interest.
    """
    genotype_phasing_by_Hi_C_assay = "OBI:0002459"
    """
    A genotyping assay in which carbon-copy chromosome conformation is used to detect polymorphism in DNA samples.
    """
    transcript_analysis_by_single_end_sequencing_assay = "OBI:0002485"
    """
    A sequencing assay that incorporates single-end reads and sequencing technology to determine transcripts, gene structures, and gene expressions.
    """
    differential_medium_assay = "OBI:0002489"
    """
    An organism detection assay that uses a differential medium to achieve its objective.
    """
    histopathology_assay = "OBI:0002564"
    """
    A histological assay that is intended to check for the presence or level of a specific disease.
    """
    polyA_selected_RNA_sequencing_assay = "OBI:0002571"
    """
    A transcription profiling by RNA sequencing assay to study transcriptomes through the enrichment of polyadenylated transcripts or removal of ribosomal RNA prior to high-throughput sequencing.
    """
    polyA_depleted_RNA_sequencing_assay = "OBI:0002572"
    """
    A transcription profiling by RNA sequencing assay to study non-polyadenylated transcripts, such as, but not exclusive to unspliced and circular isoforms, through the depletion of polyadenylated transcripts prior to high-throughput sequencing.
    """
    isoform_sequencing = "OBI:0002575"
    """
    A transcription profiling by RNA sequencing assay for sequencing isoforms by enriching a cDNA library for full-length reads spanning entire transcript isoforms.
    """
    chromosome_conformation_capture_sequencing_assay = "OBI:0002597"
    """
    A chromosome conformation capture-on-chip assay quantitates the products with multiplexed high-throughput sequencing.
    """
    reconstitution_assay = "OBI:0002621"
    """
    An assay in which a cellular process is replicated from the bottom-up using isolated components in order to observe how the components work together.
    """
    in_vitro_transcription_reconstitution_assay = "OBI:0002622"
    """
    A reconstitution assay in which RNA synthesis is investigated using RNA polymerase II transcription systems replicated in vitro from their base components.
    """
    whole_metagenome_sequencing_assay = "OBI:0002623"
    """
    A DNA sequencing assay that intends to provide information on the DNA sequences of multiple genomes (a metagenome) from different organisms present in the same input sample.
    """
    RNAi_knockdown_assay = "OBI:0002628"
    """
    A gene knockdown assay in which RNAi gene knockdown is used to disrupt gene transcripts.
    """
    direct_RNA_sequencing_assay = "OBI:0002629"
    """
    An assay to study transcription through direct RNA sequence determination, without prior conversion of RNA molecules to cDNA.
    """
    single_cell_transcription_profiling_by_RNA_sequencing_assay = "OBI:0002631"
    """
    A transcription profiling by RNA sequencing assay that uses as input RNA extracts that can be traced to a single cell of origin. These extracts may come from the entire cell or only a part of the cell such as the nucleus or the cytoplasm.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_disease_exacerbation_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0002634"
    """
    An efficacy of B cell epitope intervention experiment that uses a disease exacerbation in vivo intervention experiment after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_disease_reduction_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002635"
    """
    An efficacy of T cell epitope intervention experiment that detects a decrease in disease after adoptive transfer of epitope specfic T cells.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_disease_reduction_resulting_from_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0002636"
    """
    An efficacy of B cell epitope intervention experiment that detects a decrease in disease after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002637"
    """
    An efficacy of T cell epitope intervention experiment that uses a epitope protection experiment after adoptive transfer of epitope specfic T cells.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_challenge_resulting_from_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0002638"
    """
    An efficacy of B cell epitope intervention experiment that uses a epitope protection experiment after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells_based_on_pathogen_burden = "OBI:0002639"
    """
    An in vivo assay measuring T cell epitope specific protection from pathogen challenge resulting from the adoptive transfer of epitope specific antibodies or B cells using pathogen burden.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells_based_on_pathogen_burden = "OBI:0002640"
    """
    An in vivo assay measuring B cell epitope specific protection from pathogen challenge resulting from the adoptive transfer of epitope specific antibodies or B cells using pathogen burden.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_other_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells_based_on_survival = "OBI:0002641"
    """
    An in vivo assay measuring T cell epitope specific protection from other challenge resulting from the adoptive transfer of epitope specific T cells using survival.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_other_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells_based_on_survival = "OBI:0002642"
    """
    An in vivo assay measuring B cell epitope specific protection from other challenge resulting from the adoptive transfer of epitope specific antibodies or B cells using survival.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells_based_on_tumor_burden = "OBI:0002643"
    """
    An in vivo assay measuring T cell epitope specific protection from tumor challenge resulting from the adoptive transfer of epitope specific T cells using tumor burden.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells_based_on_tumor_burden = "OBI:0002644"
    """
    An in vivo assay measuring B cell epitope specific protection from tumor challenge resulting from the adoptive transfer of epitope specific antibodies or B cells using tumor burden.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_tolerance_induction_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002645"
    """
    An efficacy of T cell epitope intervention experiment that uses a tolerance induction intervention experiment after adoptive transfer of epitope specfic T cells.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_tolerance_induction_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0002646"
    """
    An efficacy of B cell epitope intervention experiment that uses a tolerance induction intervention experiment after adoptive transfer of epitope specific antibodies or B cells.
    """
    Giemsa_stain_assay = "OBI:0002647"
    """
    An assay that uses a Giemsa stain to characterize cells.
    """
    blood_microbiology_assay = "OBI:0002649"
    """
    An organism detection assay that detects microorganisms in a blood specimen.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_15_production_by_T_cells = "OBI:0002664"
    """
    A cytometric bead array assay that detects interleukin-15 production by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_interleukin_16_production_by_T_cells = "OBI:0002665"
    """
    A cytometric bead array assay that detects interleukin-16 production by T cells.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_induction_of_hypersensitivity_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0002666"
    """
    An efficacy of B cell epitope intervention experiment that detects a hypersensitivity response by monitoring skin reactions after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_skin_test_assay_measuring_T_cell_epitope_specific_type_IV_hypersensitivity_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002667"
    """
    An efficacy of T cell epitope intervention experiment that detects epitope specific type IV hypersensitivity after adoptive transfer of epitope specfic T cells.
    """
    in_vivo_assay_measuring_epitope_specific_proliferation_of_T_cells_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002668"
    """
    A T cell epitope specific proliferation assay that is performed in vivo after adoptive transfer of epitope specfic T cells.
    """
    assay_measuring_epitope_specific_helper_T_cell_enhancement_of_a_B_cell_mediated_immune_response_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002669"
    """
    A T cell epitope specific helper activity assay that detects the ability of a T cell epitope to enhance an antibody response after adoptive transfer of epitope specfic T cells.
    """
    assay_measuring_epitope_specific_helper_T_cell_enhancement_of_a_T_cell_mediated_immune_response_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002670"
    """
    A T cell epitope specific helper activity assay that detects the ability of a T cell epitope to enhance a T cell response after adoptive transfer of epitope specfic T cells.
    """
    in_vivo_assay_measuring_epitope_specific_T_cell_killing_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002671"
    """
    An in vivo cell killing assay that detects the killing of an antigen presenting cell (APC) by a T cell whose TCR recognizes an epitope presented by the APC after adoptive transfer of epitope specific T cells.
    """
    ELISA_measuring_epitope_specific_perforin_release_by_T_cells = "OBI:0002672"
    """
    An enzyme-linked immunosorbent assay that detects epitope specific perforin release by T cells.
    """
    massively_parallel_reporter_assay = "OBI:0002675"
    """
    An assay in which multiplexing the construction and interrogation of larger libraries of reporter constructs allows measurement of the transcriptional regulatory activities of thousands to hundreds of thousands of DNA sequences.
    """
    in_vivo_assay_measuring_a_T_cell_epitope_specific_response_after_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002676"
    """
    An efficacy of T cell epitope intervention experiment that is performed after adoptive transfer of epitope specfic T cells.
    """
    in_vivo_assay_measuring_a_B_cell_epitope_specific_response_after_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0002677"
    """
    An efficacy of B cell epitope intervention experiment that is performed after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_disease_exacerbation_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0002678"
    """
    An efficacy of T cell epitope intervention experiment that uses a disease exacerbation in vivo intervention experiment after adoptive transfer of epitope specfic T cells.
    """
    pseudovirus_entry_assay = "OBI:0002680"
    """
    An assay that measures the entry in target cells of reporter viral particles that express an envelope protein of a different virus of interest.
    """
    polymerase_chain_reaction_assay = "OBI:0002692"
    """
    An assay that uses polymerase chain reaction technique to amplify DNA.
    """
    restriction_fragment_length_polymorphism_assay = "OBI:0002693"
    """
    An assay that uses digestion of DNA with specific restriction enzymes followed by gel electropheresis to detect differences in the sizes of the generated fragments that are due to genetic differences (polymorphisms) in homologous sequences.
    """
    DNA_fingerprinting_assay = "OBI:0002694"
    """
    An assay to identify a specific individual organism from a DNA specimen by looking at unique patterns in their DNA.
    """
    insecticide_resistance_assay = "OBI:0002695"
    """
    An assay that aims to detect the presence and/or frequency of resistance to insecticides in an organism or organism population.
    """
    insecticide_resistance_by_monitoring_known_mutations_assay = "OBI:0002696"
    """
    An insecticide resistance assay that detects, in a population, presence and frequency of mutant alleles for previously characterized mutations with insecticide resistance phenotypes.
    """
    insecticide_resistance_by_detecting_enzyme_activity_assay = "OBI:0002697"
    """
    An insecticide resistance assay that is based on determination the catalytic activity of an enzyme associated with insecticide resistance phenotypes.
    """
    insecticide_resistance_bioassay = "OBI:0002698"
    """
    An insecticide resistance assay that is typically conducted to measure the effects of a substance on a living organism.
    """
    insecticide_resistance_by_detecting_alpha_esterase_activity_assay = "OBI:0002699"
    """
    An insecticide resistance by detecting enzyme activity assay that measures activity of alpha esterase.
    """
    insecticide_resistance_by_detecting_beta_esterase_activity_assay = "OBI:0002700"
    """
    An insecticide resistance by detecting enzyme activity assay that measures activity of beta esterase.
    """
    insecticide_resistance_by_detecting_acetylcholinesterase_activity_assay = "OBI:0002701"
    """
    An insecticide resistance by detecting enzyme activity assay that measures activity of acetylcholinesterase.
    """
    insecticide_resistance_by_detecting_glutathione_S_transferase_activity_assay = "OBI:0002702"
    """
    An insecticide resistance by detecting enzyme activity assay that measures activity of glutathione S-transferase (GST).
    """
    insecticide_resistance_by_detecting_carboxylic_ester_hydrolase_activity_assay = "OBI:0002703"
    """
    An insecticide resistance by detecting enzyme activity assay that measures activity of carboxylic ester hydrolase using p-nitrophenyl acetate as a substrate.
    """
    insecticide_resistance_by_detecting_mixed_function_oxidase_assay = "OBI:0002704"
    """
    An insecticide resistance by detecting enzyme activity assay that measures whether mixed-function oxidase activity present.
    """
    direct_insecticide_resistance_bioassay = "OBI:0002705"
    """
    An insecticide resistance bioassay without the use of any synergist.
    """
    topical_application_insecticide_resistance_bioassay = "OBI:0002706"
    """
    An insecticide resistance bioassay by adding insecticide directly to the thorax of the insect.
    """
    direct_insecticide_resistance_diagnostic_assay = "OBI:0002707"
    """
    A direct insecticide resistance assay that at preset insecticide dosage scoring mortality to determine resistance of a population.
    """
    insecticide_resistance_dose_response_assay = "OBI:0002708"
    """
    A direct insecticide resistance assay in which an insect population is exposed to a range of insecticide dosage scoring mortality to determine resistance.
    """
    insecticide_resistance_time_response_assay = "OBI:0002709"
    """
    A direct insecticide resistance assay to determine resistance as a consequence of the time of exposure to insecticide.
    """
    Centre_for_Disease_Control_and_Prevention_bottle_bioassay = "OBI:0002710"
    """
    A direct insecticide resistance diagnostic assay performs in a glass bottle coated with insecticides for detecting resistance to insecticides in vector populations.
    """
    WHO_cone_kit_diagnostic_assay = "OBI:0002711"
    """
    A direct insecticide resistance diagnostic assay uses WHO cone kit.
    """
    WHO_paper_kit_diagnostic_assay = "OBI:0002712"
    """
    A direct insecticide resistance diagnostic assay uses WHO paper kit.
    """
    WHO_larvicide_diagnostic_assay = "OBI:0002713"
    """
    A direct insecticide resistance diagnostic assay tests survival of larvae in a medium supplemented with insecticide.
    """
    insecticide_resistance_dose_response_by_bottle_assay = "OBI:0002714"
    """
    An insecticide resistance dose response assay that performs in a glass bottle coated with insecticides.
    """
    insecticide_resistance_dose_response_by_survival_of_larvae_assay = "OBI:0002715"
    """
    An insecticide resistance dose response assay that tests survival of larvae in a medium supplemented with insecticide.
    """
    insecticide_resistance_dose_response_by_WHO_paper_kit_assay = "OBI:0002716"
    """
    An insecticide resistance dose response assay using WHO paper kit.
    """
    insecticide_resistance_time_response_by_bottle_assay = "OBI:0002717"
    """
    An insecticide resistance time response assay that is performed in a glass bottle coated with insecticides, with the presence of a synergist.
    """
    insecticide_resistance_time_response_by_WHO_paper_kit_assay = "OBI:0002718"
    """
    An insecticide resistance time response assay using WHO paper kit, with the presence of a synergist.
    """
    insecticide_resistance_by_amplification_refractory_mutation_system_assay = "OBI:0002719"
    """
    An insecticide resistance by monitoring known mutations assay that detects any mutation involving single base changes or small deletions using amplification refractory mutation system (ARMS). The ARMS is based on the use of sequence-specific PCR primers that allow amplification of test DNA only when the target allele is contained within the sample. Following an ARMS reaction the presence or absence of a PCR product is diagnostic for the presence or absence of the target allele. It can be used to analyze human genomic DNA for one or more mutations.
    """
    insecticide_resistance_by_primer_introduced_restriction_analysis_PCR_assay = "OBI:0002720"
    """
    An insecticide resistance by monitoring known mutations assay that detects Single Nucleotide Polymorphisms (SNPs) using PCR technique and mismatched primers that is close to the mutation of interest and digested the PCR productions using restriction enzymes.
    """
    insecticide_resistance_by_nested_polymerase_chain_reaction_assay = "OBI:0002721"
    """
    An insecticide resistance by monitoring known mutations assay that detects gene mutation based on nested polymerase chain reaction technique.
    """
    insecticide_resistance_by_ligase_detection_reaction_assay = "OBI:0002722"
    """
    An insecticide resistance assay that is based on monitoring known mutations using ligase detection reaction exquisitely discriminate between a mismatched and complementary DNA helix.
    """
    insecticide_resistance_by_ligase_detection_reaction_fluorescent_microsphere_assay = "OBI:0002723"
    """
    An insecticide resistance by ligase detection reaction assay that uses fluorescently labeled conserved probes in ligase detection reaction.
    """
    insecticide_resistance_by_PCR_amplification_of_specific_alleles_assay = "OBI:0002724"
    """
    An insecticide resistance assay that is based on monitoring known mutations by PCR amplification of specific alleles to detect polymorphic or mutant alleles.
    """
    insecticide_resistance_by_fluorogenic_PCR_assay = "OBI:0002725"
    """
    An insecticide resistance assay that is based on monitoring known mutations by PCR technique that uses target specific probes labeled with fluorogenic chromophores to detect gene mutation.
    """
    insecticide_resistance_by_PCR_RFLP_assay = "OBI:0002726"
    """
    An insecticide resistance by monitoring known mutations assay based on restriction fragment length polymorphism assay.
    """
    insecticide_resistance_by_short_interspersed_elements_PCR_assay = "OBI:0002727"
    """
    An insecticide resistance assay that is based on monitoring known mutations by PCR amplification of short interspersed elements (SINEs).
    """
    pathogen_detection_assay = "OBI:0002728"
    """
    An organism detection assay that detects pathogens.
    """
    VectorTest_assay = "OBI:0002729"
    """
    A pathogen detection assay that identifies the presence or absence of specific peptide epitopes of circumsporozoite (CS) protein of the most important Plasmodium falciparum and two strains (variants 210 and 247) of the more widespread Plasmodium vivax using a dipstick wicking test strip.
    """
    pathogen_detection_by_Rapid_Analyte_Measurement_Platform_assay = "OBI:0002730"
    """
    A pathogen detection assay that is based on Rapid Analyte Measurement Platform (RAMP) technology to quantify immunologically active substances.
    """
    pathogen_detection_by_loop_mediated_isothermal_amplification_assay = "OBI:0002731"
    """
    A pathogen detection assay that is based on loop-mediated isothermal amplification.
    """
    blood_meal_assay = "OBI:0002732"
    """
    An assay that analyzes the specimen taken from blood meal fed organism, such as insect.
    """
    blood_meal_by_counter_current_immunoelectrophoresis_assay = "OBI:0002733"
    """
    A blood meal assay that uses a counter current immunoelectrophoresis technique.
    """
    DNA_based_blood_meal_finger_printing_assay = "OBI:0002734"
    """
    A DNA fingerprinting assay that uses DNA extracted from blood meal fed organism, such as insect.
    """
    organism_detection_by_size_assay = "OBI:0002735"
    """
    An organism detection assay that is based on the size of organism.
    """
    organism_detection_by_cross_mating_assay = "OBI:0002736"
    """
    An organism detection assay that is based on genetic crossings between specimens collected in the field to determine whether fertile progeny is produced.
    """
    organism_detection_by_cytological_chromosome_examination_assay = "OBI:0002737"
    """
    An organism detection assay that is based on analysis of polytene chromosomes through cytological examination of the banding pattern of the species.
    """
    organism_detection_by_isoenzyme_electrophoresis_assay = "OBI:0002738"
    """
    An organism detection assay that is based on electrophoresis to determine the isozymes that are present in a specific population to determine the species.
    """
    organism_detection_by_morphological_examination_assay = "OBI:0002739"
    """
    An organism detection assay that is based on examination of morphology and the use of specific taxonomic keys to determine the species of the specimen.
    """
    organism_detection_by_PCR_assay = "OBI:0002740"
    """
    An organism detection assay that is based on PCR.
    """
    organism_detection_by_specific_DNA_hybridization_assay = "OBI:0002741"
    """
    An organism detection assay that is based on DNA hybrdization.
    """
    organism_detection_by_salinity_tolerance_assay = "OBI:0002742"
    """
    An organism detection assay of mosquito species that is on the basis of mosquito survival depending on the salt concentration in the water used to lay their eggs to differentiate between morphologically very similar species.
    """
    PRO_cap = "OBI:0002753"
    """
    Precision nuclear run-on and sequencing to detect Pol II initiation sites
    """
    ribosomal_RNA_depleted_RNA_sequencing_assay = "OBI:0002759"
    """
    A transcription profiling by RNA sequencing assay in which highly abundant ribosomal RNAs are removed from total RNA before sequencing, resulting in more efficient transcript/gene detection.
    """
    metatranscriptome_profiling_assay = "OBI:0002760"
    """
    A transcription profiling by RNA sequencing assay that determines the RNA sequence of microbial transcripts from a microbioal community of mixed species from a given microbiome.
    """
    lipid_profiling_assay = "OBI:0002761"
    """
    An analyte assay assay that detects and identifies lipids resulting from biochemical and cellular metabolism.
    """
    single_nucleus_ATAC_seq = "OBI:0002762"
    """
    An ATAC-seq assay in which single nuclei are isolated from frozen tissue samples, through a protocol designed to maximally preserve nucleus integrity during sample processing and optimize transposase-mediated fragmentation of chromatin in individual nuclei.
    """
    number_16s_ribosomal_gene_sequencing_assay = "OBI:0002763"
    """
    An amplicon sequencing assay in which the amplicon is derived from universal primers used to amplify the 16S ribosomal RNA gene from isolate bacterial genomic DNA or metagenomic DNA from a microbioal community. Resulting sequences are compared to reference 16S sequence databases to identify or classify bacteria present within a given sample.
    """
    single_cell_ATAC_seq = "OBI:0002764"
    """
    An ATAC assay designed to robustly map the accessible genome of individual cells, using sequencing integrated into a programmable microfluidics platform, in order to provide insights into cell-to-cell variation in accessibility profiles.
    """
    microbiome_protein_expression_profiling_assay = "OBI:0002765"
    """
    A protein expression profiling assay of microbial proteins extracted from a microbioal community of mixed species from a given microbiome.
    """
    cytokine_assay = "OBI:0002766"
    """
    An analyte assay to study presence, concentration, or amount of cytokines.
    """
    amplicon_sequencing_assay = "OBI:0002767"
    """
    A sequencing assay in which a DNA or RNA input molecule is amplified by PCR and the product sequenced.
    """
    whole_virome_sequencing_assay = "OBI:0002768"
    """
    A whole metagenome sequencing assay that intends to provide information on multiple genome sequences from different viruses present in the same input sample.
    """
    single_value_binding_of_antibody_with_reporter_to_antigen_assay = "OBI:0002773"
    """
    An assay that detects the linking of antigens and antibodies via special signaling mechanisms, such as EIA, ELISA, chemiluminescence, etc. that produces one measure (quantitative or qualitative) of the analyte of interest
    """
    fluorescence_imaging_based_apoptosis_assay = "OBI:0002946"
    """
    A type of cytometry assay in which fluorescent dyes are used to label and detect proteins or structures associated with molecular processes of apoptosis.
    """
    fluorescence_imaging_based_cell_proliferation_assay = "OBI:0002947"
    """
    A type of cell proliferation assay in which fluorescent dyes are ued to label and detect proteins or structures that can be used to count cells.
    """
    fluorescence_imaging_based_cell_cycle_state_assay = "OBI:0002948"
    """
    A type of cytometry assay in which fluorescent dyes are used to label and detect proteins or structures associated with particular cell cycle states.
    """
    fluorescence_imaging_based_cell_viability_assay = "OBI:0002949"
    """
    A type of cytometry assay in which fluorescent dyes are used to label and detect proteins or structures associated with cell viability.
    """
    fluorescence_imaging_based_drug_synergy_assay = "OBI:0002950"
    """
    A type of cytometry assay in which fluorescent dyes are used to label and detect proteins or structures to determine if drugs applied to cells in combination have a greater effect together than the sum of their separate effects.
    """
    fluorescence_imaging_based_cell_morphology_assay = "OBI:0002951"
    """
    A type of cytometry assay in which fluorescent dyes are used to label and detect proteins or structures in order to determine cell morphology.
    """
    fluorescence_imaging_multiplex_cytological_profiling = "OBI:0002952"
    """
    A type of cytometry assay in which fluorescent dyes are used to stain seven major cellular components followed by automatic image capture and analysis which extracts shape, texture, and intensity parameters.
    """
    protein_state_assay = "OBI:0002953"
    """
    A type of assay that measures the quantity and/or identity of proteins in their modficied and unmodified states where modifications include phosphorylation, methylation, acetylation, etc.
    """
    fluorescence_imaging_based_protein_phosphorylation_state_assay = "OBI:0002954"
    """
    A type of protein state assay that employs high-throughput microscopy to measure levels of proteins in different phosphorylation states.
    """
    mass_spectrometry_based_protein_state_assay = "OBI:0002955"
    """
    A type of protein state assay that employs mass spectrometry to measure levels of proteins in different phosphorylation states.
    """
    targeted_drug_modulated_mass_spectrometry_based_protein_phoshporylation_state_assay = "OBI:0002956"
    """
    A type of mass spectrometry protein state assay that measures levels of a targeted set of proteins in different phosphorylation states in response to drug perturbations.
    """
    reverse_phase_protein_array_profiling_assay = "OBI:0002957"
    """
    A type of protein state assay where tissue or cell samples are lysed and then spotted onto a slide which is probed with antibodies specific to proteins with and without post-translational modifications.
    """
    SWATH_MS_protein_profiling_assay = "OBI:0002958"
    """
    A type of mass spectrometry assay using a data-independent acquisition method to identify target peptides.
    """
    tandem_mass_tag_mass_spectrometry_assay = "OBI:0002959"
    """
    A type of tandem mass spectrometry where isotopomer labels are employed for accurate quantification and identification of specific proteins.
    """
    fluorescence_imaging_based_reporter_gene_assay = "OBI:0002960"
    """
    A type of reporter gene assay that employs fluorescence imaging to detect a reporter gene's expression.
    """
    global_chromatin_profiling_by_mass_spectrometry_assay = "OBI:0002961"
    """
    A type of epigenetic modification assay that employs targeted quantitative mass spectrometry to profile modifications of the core histones of chromatin.
    """
    kinase_inhibitor_assay = "OBI:0002962"
    """
    A type of assay that identifies compounds that inhibit the activity of kinases.
    """
    KINOMEscan_assay = "OBI:0002963"
    """
    A type of proprietary kinase inhibitor assay that and employs a panel of kinases against which one can test compounds for their selectivity and potency in interactions with kinases, without the need to add ATP to the reactions.
    """
    KiNativ_assay = "OBI:0002964"
    """
    A type of proprietary in situ kinase inhibitor assay that employs biotinylated acyl phosphates of ATP and ADP.
    """
    landmark_transcript_profiling_assay = "OBI:0002965"
    """
    A type of transcription profiling assay in which a set of landmark transcripts that have been determined to provide a comprehensive profile of cell activity, plus numerous steady-state controls, are assayed via ligation-mediated amplification followed by capture on fluorescently labeled microspheres followed by detection of fluorescence.
    """
    microenvironment_microarray_assay = "OBI:0002966"
    """
    A type of cytometry assay where cells are incubated for three days with a standardized set of extracellular matrix proteins in combination with various ligands creating varying microenvironment perterbations for the cells. Immunofluorescent imaging of cells is used to measure features such as morphology, metabolism, cell cycle, and nuclear activity.
    """
    microwestern_meso_scale_quantitative_western_blot_assay = "OBI:0002967"
    """
    A western blot assay that provides a high-throughput, sensitive, and quantitative measurement of proteins from numerous samples via an array of small western blots on a single sheet of nitrocellulose.
    """
    positiveSOLIDUSnegative_ion_switching_metabolite_profiling_assay = "OBI:0002968"
    """
    A type of metabolic profiling assay which employs a hybrid dual quadrupole linear ion trap mass spectrometer for steady-state profiling of endogenous polar metabolites from organic extractions from biological samples.
    """
    cyclic_immunofluoroescence_assay = "OBI:0002969"
    """
    A type of microscopy assay resulting in highly multiplexed immunofluorescence imaging through sequential rounds of imaging followed by fluorophore inactivation.
    """
    multiplex_bead_based_protein_state_immunoassay = "OBI:0002970"
    """
    A type of protein state assay in which antibodies attached to different colored beads and fluorescent reporter dye labels are used in a multiplexed mixture to assay for proteins in specific states.
    """
    capture_Hi_C_assay = "OBI:0002984"
    """
    A Hi-C assay in which a selection step is performed on ligated fragments in order to enrich for ligation products containing specific regions of interest.
    """
    magnetic_resonance_imaging_assay = "OBI:0002985"
    """
    An imaging assay in which nuclear magnetic resonance is used to produce information about the interior structure and composition of an input material entity.
    """
    computed_tomography_imaging_assay = "OBI:0002986"
    """
    An imaging assay that uses a series of X-ray images to produce information about the interior structure and composition of an input material entity.
    """
    positron_emission_tomography_imaging_assay = "OBI:0002987"
    """
    An imaging assay in which positron-emitting radionuclides are used to visualize functional processes of an input material entity.
    """
    T_cell_receptor_repertoire_sequencing_assay = "OBI:0002990"
    """
    A sequencing assay that determines the sequences of DNA or RNA molecules that encode the repertoire of T cell receptors within an input sample.
    """
    B_cell_receptor_repertoire_sequencing_assay = "OBI:0002991"
    """
    A sequencing assay that determines the sequence of a DNA or RNA molecules that encode the repertoire of B cell receptors within an input sample.
    """
    ferritin_assay = "OBI:0003009"
    """
    An assay that measures ferritin
    """
    fibrinogen_assay = "OBI:0003010"
    """
    An assay that measures fibrinogen
    """
    iron_assay = "OBI:0003011"
    """
    An analyte assay that measures the abundance of iron
    """
    ionized_calcium_assay = "OBI:0003012"
    """
    An analyte assay that measures the abundance of ionized calcium
    """
    transferrin_assay = "OBI:0003013"
    """
    An analyte assay that measures the abundance of transferrin
    """
    uric_acid_assay = "OBI:0003014"
    """
    An analyte assay that measures the abundance of uric acid
    """
    globulin_assay = "OBI:0003015"
    """
    An analyte assay that measures the abundance of globulin
    """
    myelocyte_assay = "OBI:0003016"
    """
    A cytometry assay that measures the abundance and/or characteristics of myelocytes
    """
    metamyelocyte_assay = "OBI:0003017"
    """
    A cytometry assay that measures the abundance and/or characteristics of metamyelocytes
    """
    hematocrit_assay = "OBI:0003018"
    """
    A cytometry assay that measures the proportion of red blood cells
    """
    promyelocyte_assay = "OBI:0003019"
    """
    A cytometry assay that measures the abundance and/or characteristics of promyelocytes
    """
    basophil_assay = "OBI:0003021"
    """
    A cytometry assay that measures the abundance and/or characteristics of basophils
    """
    neutrophil_assay = "OBI:0003022"
    """
    A cytometry assay that measures the abundance and/or characteristics of neutrophils
    """
    eosinophil_assay = "OBI:0003023"
    """
    A cytometry assay that measures the abundance and/or characteristics of eosinophils
    """
    lymphocyte_assay = "OBI:0003024"
    """
    A cytometry assay that measures the abundance and/or characteristics of lymphocytes
    """
    monocyte_assay = "OBI:0003025"
    """
    A cytometry assay that measures the abundance and/or characteristics of monocytes
    """
    reticulocyte_assay = "OBI:0003026"
    """
    A cytometry assay that measures the abundance and/or characteristics of reticulocytes
    """
    macrophage_assay = "OBI:0003027"
    """
    A cytometry assay that measures the abundance and/or characteristics of macrophages
    """
    platelet_assay = "OBI:0003028"
    """
    A cytometry assay that measures the abundance and/or characteristics of platelets
    """
    fluorogenic_PCR_assay = "OBI:0003031"
    """
    A polymerase chain reaction assay that uses target specific probes labeled with fluorogenic chromophores.
    """
    genotyping_by_PCR_assay = "OBI:0003032"
    """
    A genotyping assay that uses polymerase chain reaction.
    """
    cleavage_under_targets_and_release_using_nuclease_assay = "OBI:0003033"
    """
    A type of DNA sequencing assay employing in situ chromatin profiling in which antibody-targeted controlled cleavage by micrococcal nuclease releases specific protein-DNA complexes into the the supernatant for sequencing.
    """
    cleavage_under_targets_and_tagmentation = "OBI:0003034"
    """
    A type of DNA sequencing assay employing in situ chromatin profiling in which a chromatin protein is bound in situ by a specific antibody, which then tethers to a protein A-Tn5 hyperactive transposase fusion protein (pA-Tn5) loaded with sequence adapters. Activation of pA-Tn5 results in factor-targeted tagmentation, generating fragments ready for PCR enrichment and DNA sequencing.
    """
    coma_severity_assay = "OBI:0003035"
    """
    A physical examination of an organism that has the objective to determine the severity of coma in a patient.
    """
    Plasmodium_gametocyte_detection_assay = "OBI:0003036"
    """
    An assay that detects Plasmodium gametocytes in a specimen.
    """
    malaria_rapid_diagnosis_assay = "OBI:0003037"
    """
    An assay that is quick and easy in the diagnosis of malaria by detecting evidence of malaria parasites (antigens) in human blood.
    """
    parasite_detection_assay = "OBI:0003038"
    """
    An assay that detects parasite in a specimen.
    """
    feces_microbiology_assay = "OBI:0003039"
    """
    An organism detection assay that detects microorganisms in a feces specimen.
    """
    blood_assay = "OBI:0003040"
    """
    An assay that has a blood specimen as evaulant.
    """
    falcivax_rapid_diagnostic_test = "OBI:0003041"
    """
    A parasite detection assay that can quickly establish the diagnosis of P. falciparum or P. vivax malaria infection by detecting the antigens in a person's blood.
    """
    optimal_IT_rapid_diagnostic_test = "OBI:0003042"
    """
    A parasite detection assay that is rapid, sensitive, and able to differentiate between P. falciparum and other malaria parasites.
    """
    urine_assay = "OBI:0003043"
    """
    An assay that has a urine specimen as evaluant.
    """
    parasite_species_identification_by_PCR_assay = "OBI:0003044"
    """
    A parasite detection by PCR assay that identifies the species of parasite.
    """
    parasite_detection_by_PCR_assay = "OBI:0003045"
    """
    A parasite detection assay that uses PCR.
    """
    organismal_body_temperature_measurement_assay = "OBI:0003080"
    """
    An assay that detects body temperature of an organism.
    """
    autofluorescence_assay = "OBI:0003087"
    """
    A fluorescence detection assay in which the light that is naturally emitted by a sample is visualized after excitation of the sample with light at a suitable wavelength.
    """
    autofluorescence_microscopy_assay = "OBI:0003088"
    """
    An autofluorescence assay in which the light that is naturally emitted by a sample is visualized via microscopy after excitation of the sample with light at a suitable wavelength.
    """
    bulk_assay_for_transposase_accessible_chromatin_using_sequencing = "OBI:0003089"
    """
    An assay for transposase-accessible chromatin using sequencing in which the sample that is sequenced is derived from a collection of cells, such as a tissue sample or entire cell culture, and therefore provides results representative of the aggregate of sample cells.
    """
    bulk_RNA_seq_assay = "OBI:0003090"
    """
    A transcription profiling by RNA sequencing assay in which the sample that is sequenced is derived from a collection of cells, such as a tissue sample or entire cell culture, and therefore provides results representative of the aggregate of sample cells.
    """
    multiplexed_fluorescent_antibody_imaging_assay = "OBI:0003091"
    """
    An imaging assay in which multiple cycles consisting of fluorescent labeling, imaging, and fluorophor deactivation are used to detect multiple proteins and their locations in a given sample of tissues or cells.
    """
    Cell_DIVE_multiplexed_imaging_assay = "OBI:0003092"
    """
    A multiplexed fluorescent antibody imaging assay that involves an iterative staining, imaging and dye inactivation workflow for over 60 biomarkers on a single fixed tissue section.
    """
    co_detection_by_indexing_assay = "OBI:0003093"
    """
    A multiplexed fluorescent antibody imaging assay that involves a highly multiplexed analysis of up to 40 proteins in a tissue using cyclic detection of DNA-indexed antibody panels.
    """
    fluorescence_in_situ_hybridization_assay = "OBI:0003094"
    """
    An in-situ hybridization assay in which fluorescently labeled molecules are used to localize specific DNA or RNA sequences.
    """
    decoding_amplified_targeted_transcripts_with_fluorescence_in_situ_hybridization_assay = "OBI:0003095"
    """
    A fluorescence in-situ hybridization assay which involves multiplex in situ digital quantification of targeted RNA transcripts in fresh or frozen tissue providing an understanding of the spatial organization of different cell types.
    """
    imaging_mass_cytometry_assay = "OBI:0003096"
    """
    A cytometry time of flight assay in which molecules of interest on or in cells are imaged through a system in which samples are labeled with multiple different rare-earth tagged antibodies. The sample is then ablated with a laser and the labeled material is detected by cytometry time of flight mass spectrometry.
    """
    liquid_chromatography_mass_spectrometry_assay = "OBI:0003097"
    """
    A mass spectrometry assay where a sample mixture is first separated by liquid chromatography before being converted into ions which are characterized by using mass spectrometry based on their mass-to-charge ratio and relative abundance.
    """
    lightsheet_fluorescence_microscopy_assay = "OBI:0003098"
    """
    A fluorescence microscopy that involves capturing of photons emitted by fluorophores excited with a thin sheet of laser light in a sample only in a relatively narrow plane by a detection objective oriented perpendicularly to the light sheet and imaged onto a detection device such as a CCD camera.
    """
    matrix_assisted_laser_desorption_ionization_imaging_mass_spectrometry_assay = "OBI:0003099"
    """
    A mass spectrometry assay that involves collection of spatially resolved mass spectra of a sample during microscopy where a pulse laser is used to produce both ionisation and vaporization. The sample is held in a matrix (such as dihydrobenzoic acid) to protect it from direct laser illumination and to separate the sample molecules. The spectra are used to visualise the spatial distribution of biomolecules by their molecular masses.
    """
    multiplexed_ion_beam_imaging_assay = "OBI:0003100"
    """
    A cytometry time of flight assay in which molecules of interest on or in cells are imaged through a system in which samples are labeled with multiple different rare-earth tagged antibodies. A primary ion beam is ued to rasterize sections under vacuum, releasing showers of secondary ions detected by cytometry time of flight mass spectrometry.
    """
    nanospray_desorption_electrospray_ionization_assay = "OBI:0003101"
    """
    A mass spectrometry assay that analyzes organic and biological molecules on a substrate by desorption of an analyte into a solvent bridge formed between two capillaries and the analysis surface. One capillary supplies solvent to create and maintain the bridge, while the second capillary transports the dissolved analyte from the bridge to the mass spectrometer. A high voltage applied between the inlet of mass spectrometer and the primary capillary creates a self-aspirating nanospray.
    """
    nanodroplet_processing_in_one_pot_for_trace_samples_assay = "OBI:0003102"
    """
    A protein expression profiling assay in which proteomics sample processing is performed in nanoliter volumes. Flow cytometry or laser microdissection is employed to isolate a small population or single cells into a nanoPOTS chip. Then, liquid chromatography mass spectrometry is used to measure the global protein expression.
    """
    periodic_acid_Schiff_staining_assay = "OBI:0003103"
    """
    A histological assay which is used on tissue samples to demonstrate the presence of carbohydrates and carbohydrate compounds such as polysaccharides, mucin, glycogen, or fungal cell wall components.
    """
    single_cell_combinatorial_indexing_assay_for_transposase_accessessable_chromatin_using_sequencing = "OBI:0003104"
    """
    An assay for transposase-accessible chromatin that uses sequencing which involves single cell combinatorial indexing ('sci-') strategy where nucleic acids from each of many cells are uniquely tagged through several rounds of split-pool barcoding which enables identification of single cells without single cell isolation.
    """
    single_cell_combinatorial_indexing_RNA_sequencing_assay = "OBI:0003105"
    """
    A single-cell transcription profiling by RNA sequencing assay that involves single cell combinatorial indexing ('sci-') strategy to profile the transcriptomes of single cells or nuclei without single cell isolation.
    """
    sequential_fluorescence_in_situ_hybridization_assay = "OBI:0003106"
    """
    A fluorescence in-situ hybridization assay that involves ultra-resolution imaging of cell activity by targetting thousands of single molecules with fluorescent probes which find and hybridize with complementary DNA or RNA sequences in the tissue sample, thus enabling identification of those molecules directly in single cells with their spatial context preserved.
    """
    slide_seq_assay = "OBI:0003107"
    """
    A transcription profiling by RNA sequencing assay that involves transfer of RNA from tissue sections onto a surface covered in DNA-barcoded beads with known positions, allowing the locations of the RNA to be inferred by sequencing.
    """
    single_nucleus_chromatin_accessibility_and_mRNA_expression_sequencing_assay = "OBI:0003108"
    """
    An assay that involves joint profiling of accessible chromatin and RNA within the same cells which enables direct matching of transcriptional regulation to its outputs.
    """
    gas_chromatography_mass_spectrometry_assay = "OBI:0003110"
    """
    A mass spectrometry assay combining mass spectrometry and gas chromatography for the qualitative as well as quantitative determination of compounds.
    """
    SOMAscan_assay = "OBI:0003111"
    """
    An analyte assay that uses aptamers to detect protein analytes in serum.
    """
    Olink_assay = "OBI:0003112"
    """
    A proximity extension assay that uses quantitative polymerase chain reaction (qPCR) technology to determine the concentration/presence of proteins using a high-multiplex, high-throughput protein biomarker platform. The assay utilizes two distinct oligonucleotide-labeled antibodies (‘probes’) that bind at different sites for each detected protein. When the two probes are in close proximity, a new PCR target sequence is formed by a proximity-dependent DNA polymerization event. The resulting sequence is subsequently detected and quantified using standard real-time PCR.
    """
    proximity_extension_assay = "OBI:0003113"
    """
    An analyte assay that uses quantitative polymerase chain reaction (qPCR) technology to determine the concentration/presence of an analyte or analyte complex.
    """
    antigen_detection_by_cytometric_bead_array_assay = "OBI:0003115"
    """
    A cytometric bead array assay in which a series of beads are coated with antibodies specific to antigens of interest. Antigens of interest attach to antibodies on the beads. Fluorescent labeled secondary antibodies are used to detect the antigens of interest.
    """
    antibody_detection_by_cytometric_bead_array_assay = "OBI:0003116"
    """
    A cytometric bead array assay that detects antigen-specific antibodies. In the assay a series of beads are coated with antigens which capture antibodies specific to the antigens. Fluorescent labeled secondary antibodies are used to detect the antibodies of interest.
    """
    number_3D_molecular_structure_determination_assay = "OBI:0003117"
    """
    An assay that determines the 3-dimensional configuration of a molecular entity or molecular complex.
    """
    electron_microscopy_3D_molecular_structure_determination_assay = "OBI:0003118"
    """
    A 3D molecular structure determination assay that uses electron microscopy imaging.
    """
    number_3D_cell_structure_determination_assay = "OBI:0003122"
    """
    A 3D structure determination assay that determines the 3-dimensional configuration of a cell.
    """
    number_3D_neural_cell_structure_determination_assay = "OBI:0003123"
    """
    A 3D cell structure determination assay that determines the 3-dimensional configuration of a neural cell.
    """
    neuron_morphology_assay = "OBI:0003124"
    """
    A 3D neural cell structure determination assay that determines the 3-dimensional configuration of a neuron.
    """
    mosaicism_with_repeat_frameshift_genetic_sparse_labeling = "OBI:0003125"
    """
    A 3D neural cell structure determination assay where sparse and stochastic methods are used to label genetically-defined neurons.
    """
    neuron_morphology_reconstruction_assay = "OBI:0003126"
    """
    A neuron morphology assay where the morphology or structure of a neuron is represented. Often, this assay is a combination of different assays (sparse labelling, fluorescent labeling, fMOST).
    """
    B_cell_epitope_assay = "OBI:0003127"
    """
    An immune epitope assay that characterizes the structrue of an antibody-epitope complex, or measures the binding of an antibody receptor to epitope, or the immune response process resulting from such a binding event or the recognition of the epitope.
    """
    T_cell_epitope_assay = "OBI:0003128"
    """
    An immune epitope assay that characterizes the structrue of an epitope-T cell receptor complex, or measures the binding of a T cell receptor to epitope, or the immune response process resulting from such a binding event or the recognition of the epitope.
    """
    assay_measuring_quantitative_binding_of_a_MHCCOLONligand_complex = "OBI:0003145"
    """
    An assay that detects the binding of a MHC molecule with a ligand, and produces a quantitative measurement of the binding as an output.
    """
    assay_measuring_quantitative_binding_of_an_antigenCOLONantibody_complex = "OBI:0003146"
    """
    An assay that detects the binding of an antigen with an antibody, and produces a quantitative measurement of the binding as an output.
    """
    assay_measuring_quantitative_binding_of_an_epitopeCOLONMHCCOLONTCR_complex = "OBI:0003147"
    """
    An assay that detects the binding of a MHC:epitope complex with a T cell receptor, and produces a quantitative measurement of the binding as an output.
    """
    albumin_concentration_assay = "OBI:0003148"
    """
    An albumin assay that measures the concentration of albumin in a specimen.
    """
    basophil_percentage_assay = "OBI:0003149"
    """
    A basophil assay that measures the percentage of basophils in a specimen.
    """
    calcium_cation_concentration_assay = "OBI:0003150"
    """
    A calcium cation assay that measures the concentration of calcium cations in a specimen.
    """
    chloride_concentration_assay = "OBI:0003151"
    """
    A chloride assay that measures the concentration of chloride in a specimen.
    """
    cholesterol_concentration_assay = "OBI:0003152"
    """
    A cholesterol assay that measures the concentration of cholesterol in a specimen.
    """
    creatinine_concentration_assay = "OBI:0003153"
    """
    A creatinine assay that measures the concentration of creatinine in a specimen.
    """
    eosinophil_percentage_assay = "OBI:0003154"
    """
    An eosinophil assay that measures the percentage of eosinophils in a specimen.
    """
    globulin_concentration_assay = "OBI:0003155"
    """
    A globulin assay that measures the concentration of globulin in a specimen.
    """
    hemoglobin_concentration_assay = "OBI:0003156"
    """
    A hemoglobin assay that measures the amount of hemoglobin in a specimen.
    """
    high_density_lipoprotein_cholesterol_concentration_assay = "OBI:0003157"
    """
    A high-density lipoprotein cholesterol assay that measures the concentration of high-density lipoprotein cholesterol in a specimen.
    """
    iron_concentration_assay = "OBI:0003158"
    """
    An iron assay that measures the concentration of iron cation in a specimen.
    """
    low_density_lipoprotein_cholesterol_concentration_assay = "OBI:0003159"
    """
    A low-density lipoprotein cholesterol assay that measures the concentration of low-density lipoprotein cholesterol in a specimen.
    """
    lymphocyte_percentage_assay = "OBI:0003160"
    """
    A lymphocyte assay that measures the percentage of lymphocytes in a specimen.
    """
    metamyelocyte_count_assay = "OBI:0003161"
    """
    A metamyelocyte assay that measures the number of metamyelocytes in a specimen.
    """
    metamyelocyte_percentage_assay = "OBI:0003162"
    """
    A metamyelocyte assay that measures the percentage of metamyelocytes in a specimen.
    """
    methemoglobin_percentage_assay = "OBI:0003163"
    """
    A methemoglobin assay that measures the percentage of methemoglobin in a specimen.
    """
    monocyte_percentage_assay = "OBI:0003164"
    """
    A monocyte assay that measures the percentage of monocytes in a specimen.
    """
    myelocyte_count_assay = "OBI:0003165"
    """
    A myelocyte assay that measures the number of myelocytes in a specimen.
    """
    neutrophil_percentage_assay = "OBI:0003166"
    """
    A neutrophil assay that measures the percentage of neutrophils in a specimen.
    """
    phosphate_ion_concentration_assay = "OBI:0003167"
    """
    A phosphate ion assay that measures the concentration of phosphate ions in a specimen.
    """
    potassiumLEFT_PARENTHESIS1PLUS_SIGNRIGHT_PARENTHESIS_concentration_assay = "OBI:0003168"
    """
    A potassium(1+) assay that measures the concentration of potassium(1+) in a specimen.
    """
    reticulocyte_percentage_assay = "OBI:0003170"
    """
    A reticulocyte assay that measures the percentage of reticulocytes in a specimen.
    """
    sodiumLEFT_PARENTHESIS1PLUS_SIGNRIGHT_PARENTHESIS_concentration_assay = "OBI:0003171"
    """
    A sodium(1+) assay that measures the concentration of sodium(1+) in a specimen.
    """
    thyroid_stimulating_hormone_concentration_assay = "OBI:0003172"
    """
    A thyroid stimulating hormone assay that measures the concentration of thyroid stimulating hormone in a specimen.
    """
    triglyceride_concentration_assay = "OBI:0003173"
    """
    A triglyceride assay that measures the concentration of triglycerides in a specimen.
    """
    number_33APOSTROPHE5APOSTROPHE_triiodothyronine_concentration_assay = "OBI:0003174"
    """
    A 3,3',5'-triiodothyronine assay that measures the concentration of 3,3',5'-triiodothyronine in a specimen.
    """
    fibrinogen_concentration_assay = "OBI:0003175"
    """
    A fibrinogen assay that measures the concentration of fibrinogen in a specimen.
    """
    free_thyroxine_concentration_assay = "OBI:0003176"
    """
    A thyroxine assay that measures the concentration of free thyroxine in a specimen.
    """
    total_thyroxine_concentration_assay = "OBI:0003177"
    """
    A thyroxine assay that measures the concentration of total thyroxine in a specimen.
    """
    direct_bilirubin_concentration_assay = "OBI:0003180"
    """
    A bilirubin IXalpha assay that measures the concentration of direct bilirubin in a specimen.
    """
    indirect_bilirubin_concentration_assay = "OBI:0003181"
    """
    A bilirubin IXalpha assay that measures the concentration of indirect bilirubin in a specimen.
    """
    total_bilirubin_concentration_assay = "OBI:0003182"
    """
    A bilirubin IXalpha assay that measures the concentration of total bilirubin in a specimen.
    """
    mean_cell_hemoglobin_assay = "OBI:0003183"
    """
    A hemoglobin assay that measures the average concentration of hemoglobin in a population of erythrocytes.
    """
    mean_cell_hemoglobin_concentration_assay = "OBI:0003184"
    """
    A hemoglobin assay that measures the concentration of hemoglobin in a specimen.
    """
    mean_platelet_volume_assay = "OBI:0003185"
    """
    A platelet assay that measures the average volume of platelets in a specimen.
    """
    immature_neutrophil_count_assay = "OBI:0003186"
    """
    A neutrophil assay that measures the number of immature neutrophils in a specimen.
    """
    immature_neutrophil_percentage_assay = "OBI:0003187"
    """
    An neutrophil assay that measures the percentage of immature neutrophils in a specimen.
    """
    nucleated_erythrocyte_percentage_assay = "OBI:0003188"
    """
    An erythrocyte assay that measures the percentage of nucleated erythrocytes in a specimen.
    """
    mean_cell_volume_assay = "OBI:0003189"
    """
    An erythrocyte assay that measures the average volume of erythrocytes in a specimen.
    """
    erythrocyte_assay = "OBI:0003190"
    """
    A cytometry assay that measures the abundance and/or characteristics of erythrocytes.
    """
    manual_hematocrit_assay = "OBI:0003191"
    """
    A hematocrit assay that measures the percentage of erythrocytes in a specimen by manual processes.
    """
    adiponectin_assay = "OBI:0003192"
    """
    An analyte assay that measures the abundance of adiponectin
    """
    adiponectin_concentration_assay = "OBI:0003193"
    """
    An adiponectin assay that measures the concentration of adiponectin in a specimen.
    """
    creatine_assay = "OBI:0003194"
    """
    An analyte assay that measures the abundance of creatine
    """
    creatine_concentration_assay = "OBI:0003195"
    """
    A creatine assay that measures the concentration of creatine in a specimen.
    """
    estradiol_assay = "OBI:0003196"
    """
    An analyte assay that measures the abundance of estradiol
    """
    estradiol_concentration_assay = "OBI:0003197"
    """
    An estradiol assay that measures the concentration of estradiol in a specimen.
    """
    leptin_assay = "OBI:0003202"
    """
    An analyte assay that measures the abundance of leptin
    """
    leptin_concentration_assay = "OBI:0003203"
    """
    An leptin assay that measures the concentration of leptin in a specimen.
    """
    lipoprotein_concentration_assay = "OBI:0003204"
    """
    An analyte assay that measures the abundance of lipoprotein
    """
    high_density_lipoprotein_concentration_assay = "OBI:0003205"
    """
    A lipoprotein concentration assay that measures the concentration of high-density lipoprotein in a specimen.
    """
    low_density_lipoprotein_concentration_assay = "OBI:0003206"
    """
    A lipoprotein concentration assay that measures the concentration of low-density lipoprotein in a specimen.
    """
    very_low_density_lipoprotein_concentration_assay = "OBI:0003207"
    """
    A lipoprotein concentration assay that measures the concentration of very-low-density lipoprotein in a specimen.
    """
    luteinizing_hormone_assay = "OBI:0003208"
    """
    An analyte assay that measures the abundance of luteinizing hormone
    """
    luteinizing_hormone_concentration_assay = "OBI:0003209"
    """
    A luteinizing hormone assay that measures the concentration of luteinizing hormone in a specimen.
    """
    nitrite_assay = "OBI:0003210"
    """
    An analyte assay that measures the abundance of nitrite
    """
    nitrite_concentration_assay = "OBI:0003211"
    """
    A nitrite assay that measures the concentration of nitrite in a specimen.
    """
    phospholipid_assay = "OBI:0003212"
    """
    An analyte assay that measures the abundance of phospholipid
    """
    phospholipid_concentration_assay = "OBI:0003213"
    """
    A phospholipid assay that measures the concentration of phospholipids in a specimen.
    """
    progesterone_assay = "OBI:0003214"
    """
    An analyte assay that measures the abundance of progesterone
    """
    progesterone_concentration_assay = "OBI:0003215"
    """
    A progesterone assay that measures the concentration of progesterone in a specimen.
    """
    testosterone_assay = "OBI:0003216"
    """
    An analyte assay that measures the abundance of testosterone
    """
    testosterone_concentration_assay = "OBI:0003217"
    """
    A testosterone assay that measures the concentration of testosterone in a specimen.
    """
    bile_salt_assay = "OBI:0003218"
    """
    An analyte assay that measures the abundance of bile salt
    """
    bile_salt_concentration_assay = "OBI:0003219"
    """
    A bile salt assay that measures the concentration of bile salt in a specimen.
    """
    fatty_acid_assay = "OBI:0003220"
    """
    An analyte assay that measures the abundance of fatty acid
    """
    free_fatty_acid_concentration_assay = "OBI:0003221"
    """
    A fatty acid assay that measures the concentration of free fatty acids in a specimen.
    """
    insulin_assay = "OBI:0003222"
    """
    An analyte assay that measures the abundance of insulin
    """
    insulin_concentration_assay = "OBI:0003223"
    """
    A insulin assay that measures the concentration of insulin in a specimen.
    """
    follicle_stimulating_hormone_assay = "OBI:0003224"
    """
    An analyte assay that measures the abundance of follicle stimulating hormone
    """
    follicle_stimulating_hormone_concentration_assay = "OBI:0003225"
    """
    A follicle stimulating hormone assay that measures the concentration of follicle stimulating hormone in a specimen.
    """
    total_lymphocyte_count_assay = "OBI:0003226"
    """
    A lymphocyte assay that measures the number of lymphocytes and large unstained cells in a specimen.
    """
    total_lymphocyte_percentage_assay = "OBI:0003227"
    """
    A lymphocyte assay that measures the percentage of lymphocytes and large unstained cells in a specimen.
    """
    fluorescent_immunospot_assay = "OBI:0003228"
    """
    A cytometry assay that detects the presence of cells that secrete a material of interest (analyte). In the assay, a plate is coated with an antibody specific to the analyte of interest. These antibodies capture the analytes secreted by the cells. The analytes are then detected using fluorescent labeled secondary antibodies.
    """
    plasma_proteomics_assay = "OBI:0003229"
    """
    A proteomics profiling assay that detects proteins in a blood plasma specimen.
    """
    T_cell_activation_induced_marker_assay = "OBI:0003230"
    """
    A flow cytometry assay that detects the presence/amount of antigen-specific T cells without the need to identify their cytokine production. Instead, antigen-specific T cells are detected on the basis of upregulation of TCR stimulation-induced surface markers.
    """
    cerebrospinal_fluid_assay = "OBI:0003232"
    """
    An assay that has a cerebrospinal fluid specimen as evaluant.
    """
    endotracheal_aspirate_assay = "OBI:0003233"
    """
    An assay that has an endotracheal aspirate specimen as evaluant.
    """
    induced_sputum_assay = "OBI:0003234"
    """
    An assay that has an induced sputum specimen as evaluant.
    """
    lung_assay = "OBI:0003235"
    """
    An assay that has a lung specimen as evaluant.
    """
    milk_assay = "OBI:0003236"
    """
    An assay that has a milk specimen as evaluant.
    """
    feces_assay = "OBI:0003237"
    """
    An assay that has a feces specimen as evaluant.
    """
    umbilical_cord_blood_assay = "OBI:0003238"
    """
    An assay that has an umbilical cord blood specimen as evaluant.
    """
    saliva_assay = "OBI:0003239"
    """
    An assay that has a saliva specimen as evaluant.
    """
    cerebrospinal_fluid_microbiology_assay = "OBI:0003240"
    """
    An organism detection assay that detects microorganisms in a cerebrospinal fluid specimen.
    """
    endotracheal_tube_aspirate_microbiology_assay = "OBI:0003241"
    """
    An organism detection assay that detects microorganisms in an endotracheal aspirate specimen.
    """
    induced_sputum_microbiology_assay = "OBI:0003242"
    """
    An organism detection assay that detects microorganisms in an induced sputum specimen.
    """
    lung_microbiology_assay = "OBI:0003282"
    """
    An organism detection assay that detects microorganisms in a lung specimen.
    """
    pleural_fluid_microbiology_assay = "OBI:0003283"
    """
    An organism detection assay that detects microorganisms in a pleural fluid specimen.
    """
    umbilical_cord_blood_microbiology_assay = "OBI:0003284"
    """
    An organism detection assay that detects microorganisms in an umbilical cord blood specimen.
    """
    nasopharyngeal_or_oropharyngeal_swab_microbiology_assay = "OBI:0003285"
    """
    An organism detection assay that detects microorganisms in a nasopharyngeal or oropharyngeal swab specimen.
    """
    urine_microbiology_assay = "OBI:0003286"
    """
    An organism detection assay that detects microorganisms in a urine specimen.
    """
    multiplex_real_time_polymerase_chain_reaction_assay = "OBI:0003287"
    """
    A real time polymerase chain reaction assay in which multiple DNA sequences are amplified in a single cycle.
    """
    multiplex_real_time_reverse_transcription_polymerase_chain_reaction_assay = "OBI:0003288"
    """
    A real time reverse-transcription polymerase chain reaction assay in which multiple DNA sequences are amplified in a single cycle.
    """
    mosquito_membrane_feeding_assay = "OBI:0003290"
    """
    An assay that evaluates host-to-mosquito transmission of a parasite organism by feeding a specimen of host blood infected with the parasite organism to a collection of mosquitoes through a mosquito membrane feeding device and, after a given time, dissecting the mosquitoes and counting the number of parasite organisms within them.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_granulysin_release_by_T_cells = "OBI:0003292"
    """
    A cytometric bead array assay that detects epitope specific granulysin release by T cells.
    """
    cytometric_bead_array_assay_measuring_epitope_specific_perforin_release_by_T_cells = "OBI:0003293"
    """
    A cytometric bead array assay that detects epitope specific perforin release by T cells.
    """
    modified_acid_fast_stain_microscopy_assay = "OBI:0003294"
    """
    A microscopy assay that uses staining to identify acid-fast organisms in a specimen and does not require heating.
    """
    antibodies_from_lymphocyte_secretions_assay = "OBI:0003296"
    """
    An assay that evaluates a blood specimen for antibodies currently being produced by lymphocytes in the specimen, by separating peripheral blood mononuclear cells, culturing them, and then collecting the supernatant containing the antibodies secreted from those cells.
    """
    tyramide_signal_amplification_sequencing_assay = "OBI:0003297"
    """
    A DNA sequencing assay that uses tyramide signal amplification (TSA) to assess distance of DNA regions to a targeted nuclear compartment or protein, typically on a scale of 100-1000 nm.
    """
    DNA_adenine_methyltransferase_identification_assay = "OBI:0003298"
    """
    An assay for identifying DNA binding sites for a protein by fusing it to Dam methylase, and expressing it so that bound DNA gets methylated. The methylated DNA can then be isolated and analyzed.
    """
    DamID_seq = "OBI:0003299"
    """
    A DNA adenine methyltransferase identification (DamID) assay in which DamID-generated DNA fragments undergo high-throughput sequencing to determine a protein's DNA-binding site.
    """
    nucleolus_associated_domain_sequencing_assay = "OBI:0003300"
    """
    A DNA sequencing assay in which nucleoli are isolated and the DNA associated with them is sequenced to identify nucleoli-associating domains.
    """
    DNase_Hi_C_assay = "OBI:0003301"
    """
    A Hi-C assay in which DNase I is used for digesting DNA fragments rather than a restriction enzyme, which can result in a higher resolution of mapped chromosome contacts.
    """
    micro_C_assay = "OBI:0003302"
    """
    A Hi-C assay which uses micrococcal nuclease digestion in place of the restriction enzyme digestion step.
    """
    single_cell_combinatorial_indexing_Hi_C_assay = "OBI:0003303"
    """
    A Hi-C assay performed on massively multiplexed single-cell samples.
    """
    single_nucleus_Hi_C_assay = "OBI:0003304"
    """
    A Hi-C assay performed on isolated nuclei.
    """
    single_cell_Hi_C_assay = "OBI:0003305"
    """
    A Hi-C assay performed on a single cell.
    """
    bulk_Hi_C_assay = "OBI:0003306"
    """
    A Hi-C assay in which the sample that is sequenced is derived from a collection of cells, such as a tissue sample or entire cell culture, and therefore provides results representative of the aggregate of sample cells.
    """
    multi_contact_Hi_C_assay = "OBI:0003307"
    """
    A Hi-C assay that assesses interactions between multiple DNA fragments rather than only pairwise interactions as in traditional Hi-C. The experimental procedure of cross-linking, digestion, and ligation is performed similarly to traditional Hi-C, but after DNA is purified a long-read library is produced in which many ligated fragments may be contained in a single molecule. The library is then sequenced on a long read sequencer.
    """
    transposase_mediated_analysis_of_chromatin_looping_assay = "OBI:0003309"
    """
    A DNA sequencing assay designed to detect interacting genomic regions. Rather than the traditional Hi-C approach of digestion and proximity ligation, the procedure involves transposase-mediated insertion of an oligonucleotide linker between the pair of interacting regions.
    """
    split_pool_recognition_of_interactions_and_tag_extension_assay = "OBI:0003310"
    """
    A sequencing assay designed to detect multi-way interactions between nucleic acids. The procedure involves crosslinking nuclei, and then splitting the lysate among wells in a 96-well or other multi-well plate. A different barcode is ligated to the fragments in each well, and the lysates are pooled together again. This sequence of splitting, tagging, and re-combining is repeated several times so that fragments with the same sequences of barcodes represent fragments that have co-associated throughout the experiment. Finally, a sequencing library is constructed and high-throughput sequencing is performed.
    """
    DNA_split_pool_recognition_of_interactions_and_tag_extension_assay = "OBI:0003311"
    """
    A split-pool recognition of interactions and tag extension (SPRITE) assay that only assays interactions between regions of genomic DNA.
    """
    RNA_DNA_split_pool_recognition_of_interactions_and_tag_extension_assay = "OBI:0003312"
    """
    A split-pool recognition of interactions and tag extension (SPRITE) assay in which RNA in the cross-linked complexes is converted to cDNA before the initial splitting step, allowing analysis of RNA-DNA interactions.
    """
    genome_architecture_mapping_assay = "OBI:0003313"
    """
    A DNA sequencing assay designed to analyze 3D chromatin structure without relying on digestion and ligation. The procedure involves cryosectioning samples in random orientation, and then single nuclear profiles are isolated by laser microdissection. Each nuclear profile then undergoes high-throughput sequencing, and subsequent analysis can generate a matrix of inferred proximity between genomic regions.
    """
    mapping_RNA_genome_interactions_assay = "OBI:0003314"
    """
    A nuclear ligation assay for probing RNA-DNA interactions in the nucleus. Nuclei are crosslinked, and RNA fragments are ligated to proximal DNA fragments via a special linker molecule. After reverse transcription, high-throughput sequencing is performed.
    """
    assay_measuring_epitope_specific_amphiregulin_production_by_T_cells = "OBI:0003315"
    """
    A T cell epitope specific cytokine production assay that detects amphiregulin production by T cells.
    """
    ELISA_measuring_epitope_specific_amphiregulin_production_by_T_cells = "OBI:0003316"
    """
    An enzyme-linked immunosorbent assay that detects amphiregulin production by T cells.
    """
    venous_blood_microbiology_assay = "OBI:0003321"
    """
    A blood microbiology assay that detects a microorganism in a venous blood specimen.
    """
    high_throughput_multiplexed_assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0003323"
    """
    A B cell epitope assay that measures the binding of an antibody receptor to an epitope using a high throughput multiplexed assay.
    """
    high_throughput_multiplexed_assay_measuring_binding_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0003324"
    """
    A T cell epitope assay that measures the binding of T cell receptor to an epitope using a high throughput multiplexed assay.
    """
    high_throughput_multiplexed_assay_measuring_binding_of_a_MHCCOLONligand_complex = "OBI:0003325"
    """
    A MHC ligand assay that detects the binding of a ligand to an MHC molecule using a high throughput multiplexed assay.
    """
    high_throughput_multiplexed_assay_measuring_MHC_ligand_processing_and_presentation = "OBI:0003326"
    """
    A MHC ligand assay that determines what ligands are processed and loaded onto MHC molecules by eluting ligands and identifying them using a high throughput multiplexed assay.
    """
    detection_technique = "OBI:0003368"
    """
    An assay (A) that is part of another assay (B), where the target entities of A and B are disjoint, and the target entity of A is a proxy for the target of assay B.
    """
    assay_measuring_epitope_specific_lymphotactin_production_by_T_cells = "OBI:0003372"
    """
    A T cell epitope specific cytokine production assay that detects lymphotactin production by T cells.
    """
    ELISA_measuring_epitope_specific_lymphotactin_production_by_T_cells = "OBI:0003373"
    """
    An enzyme-linked immunosorbent assay that detects lymphotactin production by T cells.
    """
    patch_seq_assay = "OBI:0003375"
    """
    An assay that combines electrophysiological, transcriptomic, and morphological characterization of individual neurons. In this approach, patch-clamp is used to generate an electrophysiological recording of the neuron, then the neuron's cytoplasm and/or nucleus is collected and processed for RNAseq, and finally the cell is simultaneously filled with a dye that allows for subsequent morphological reconstruction.
    """
    droplet_based_single_cell_RNA_sequencing_assay = "OBI:0003376"
    """
    A single-cell transcription profiling by RNA sequencing assay that analyzes mRNA transcripts from droplets of individual cells. The process involves the following steps: (1) prepare a single-cell suspension from a tissue; (2) co-encapsulate each cell with a distinctly barcoded microparticle (bead) in a nanoliter-scale droplet; (3) lyse cells after they have been isolated in droplets; (4) capture a cell’s mRNAs on its companion microparticle, forming STAMPs (single-cell transcriptomes attached to microparticles); (5) reverse-transcribe, amplify, and sequence.
    """
    single_nucleus_chromatin_accessibility_and_mRNA_expression_sequencing_2_assay = "OBI:0003377"
    """
    An assay that uses combinatorial indexing to generate a library of cDNA and open chromatin gDNA fragments by tagmenting a single nuclei and open chromatin, and encapsulating those in a droplet including both an oligo-dT-containing barcoded bead and a splint oligonucleotide, which links the tagmented gDNA fragments to the bead which capture both mRNAs and open chromatin fragments.
    """
    switching_mechanism_at_the_5APOSTROPHE_end_of_RNA_template_sequencing_assay = "OBI:0003378"
    """
    A single cell transcription profiling by RNA sequencing assay wherein cells are lysed and their recovered RNA is hybridized to an oligo(dT) that primes a reverse transcription reaction, the outcome of which are cDNA’s that have PCR handles on both ends. The cDNA's are then amplified using PCR, and the products are sequenced.
    """
    switching_mechanism_at_the_5APOSTROPHE_end_of_RNA_template_sequencing_2_assay = "OBI:0003379"
    """
    A single cell transcription profiling by RNA sequencing assay that is a variation on the switching mechanism at the 5' end of RNA template sequencing assay (SMARTseq) that allows the generation of full-length cDNA and sequencing libraries by using standard reagents.
    """
    placental_blood_microbiology_assay = "OBI:0003381"
    """
    A blood microbiology assay that detects microorganisms in a placental blood specimen.
    """
    linked_read_sequencing_assay = "OBI:0003412"
    """
    A DNA sequencing assay that uses microfluidics to partition and barcode high molecular weight DNA such that short reads derived from fragments of the large piece of DNA can be assembled within the context of the high molecular weight piece of DNA they are derived from, facilitating the use of short read data to sequence and assemble large genomes.
    """
    antigen_specific_antibodies_in_blood_assay = "OBI:0003418"
    """
    An antigen specific antibodies assay that has a blood specimen as evaluant.
    """
    antigen_specific_antibodies_in_milk_assay = "OBI:0003419"
    """
    An antigen specific antibodies assay that has a milk specimen as evaluant.
    """
    enzymatic_activity_level_assay = "OBI:0003422"
    """
    An assay in which the level of catalytic activity of an enzyme is determined.
    """
    number_5APOSTROPHE_nucleotidase_activity_level_assay = "OBI:0003423"
    """
    An enzymatic activity level assay that measures the activity of 5'-nucleotidase in a sample.
    """
    alanine_aminotransferase_activity_level_assay = "OBI:0003424"
    """
    An enzymatic activity level assay that measures the activity of alanine aminotransferase in a sample.
    """
    alkaline_phosphatase_activity_level_assay = "OBI:0003425"
    """
    An enzymatic activity level assay that measures the activity of alkaline phosphatase in a sample.
    """
    amylase_activity_level_assay = "OBI:0003426"
    """
    An enzymatic activity level assay that measures the activity of amylase in a sample.
    """
    aspartate_aminotransferase_activity_level_assay = "OBI:0003427"
    """
    An enzymatic activity level assay that measures the activity of aspartate aminotransferase in a sample.
    """
    cholinesterase_activity_level_assay = "OBI:0003428"
    """
    An enzymatic activity level assay that measures the activity of cholinesterase in a sample.
    """
    creatine_kinase_activity_level_assay = "OBI:0003429"
    """
    An enzymatic activity level assay that measures the activity of creatine kinase in a sample.
    """
    gamma_glutamyltransferase_activity_level_assay = "OBI:0003430"
    """
    An enzymatic activity level assay that measures the activity of gamma-glutamyltransferase in a sample.
    """
    glutamate_dehydrogenase_activity_level_assay = "OBI:0003431"
    """
    An enzymatic activity level assay that measures the activity of glutamate dehydrogenase in a sample.
    """
    isocitrate_dehydrogenase_activity_level_assay = "OBI:0003432"
    """
    An enzymatic activity level assay that measures the activity of isocitrate dehydrogenase in a sample.
    """
    lactate_dehydrogenase_activity_level_assay = "OBI:0003433"
    """
    An enzymatic activity level assay that measures the activity of lactate dehydrogenase in a sample.
    """
    sorbitol_dehydrogenase_activity_level_assay = "OBI:0003434"
    """
    An enzymatic activity level assay that measures the activity of sorbitol dehydrogenase in a sample.
    """
    acyl_CoA_oxidase_activity_level_assay = "OBI:0003435"
    """
    An enzymatic activity level assay that measures the activity of Acyl-CoA oxidase in a sample.
    """
    N_acetyl_beta_glucosaminidase_activity_level_assay = "OBI:0003436"
    """
    An enzymatic activity level assay that measures the activity of N-acetyl-beta-glucosaminidase in a sample.
    """
    ribonuclease_activity_level_assay = "OBI:0003437"
    """
    An enzymatic activity level assay that measures the activity of ribonuclease in a sample.
    """
    galactosidase_activity_level_assay = "OBI:0003438"
    """
    An enzymatic activity level assay that measures the activity of galactosidase in a sample.
    """
    epitope_protection_from_infectious_challenge_experiment_based_on_survival = "OBI:0003457"
    """
    An epitope protection from infectious challenge experiment that determines the success of the epitope intervention based on increased survival of the host compared to controls.
    """
    epitope_protection_from_tumor_challenge_experiment_based_on_burden = "OBI:0003458"
    """
    An epitope protection from tumor challenge experiment in which the readout is a reduction in the presence of malignant cells in the host compared to controls.
    """
    epitope_protection_from_tumor_challenge_experiment_based_on_survival = "OBI:0003459"
    """
    An epitope protection from tumor challenge experiment that determines the success of the epitope intervention based on increased survival of the host compared to controls.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_pathogen_challenge = "OBI:0003460"
    """
    An in vivo assay measuring T cell epitope specific protection from pathogen challenge.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_tumor_challenge = "OBI:0003461"
    """
    An in vivo assay measuring T cell epitope specific protection from tumor challenge.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_other_challenge = "OBI:0003462"
    """
    An in vivo assay measuring T cell epitope specific protection from a challenge other than pathogen, infection, or tumor.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_survival_after_tumor_challenge = "OBI:0003463"
    """
    An in vivo assay measuring T cell epitope specific protection from tumor challenge using survival.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_survival_after_pathogen_challenge = "OBI:0003464"
    """
    An in vivo assay measuring T cell epitope specific protection from pathogen challenge using survival.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_pathogen_challenge = "OBI:0003465"
    """
    An in vivo assay measuring B cell epitope specific protection from pathogen challenge.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_tumor_challenge = "OBI:0003466"
    """
    An in vivo assay measuring B cell epitope specific protection from tumor challenge.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_other_challenge = "OBI:0003467"
    """
    An in vivo assay measuring B cell epitope specific protection from a challenge other than pathogen, infection, or tumor.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_survival_after_pathogen_challenge = "OBI:0003468"
    """
    An in vivo assay measuring B cell epitope specific protection from pathogen challenge using survival.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_survival_after_tumor_challenge = "OBI:0003469"
    """
    An in vivo assay measuring B cell epitope specific protection from tumor challenge using survival.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_pathogen_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0003470"
    """
    An in vivo assay measuring a T cell epitope specific protection from a pathogen challenge after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_pathogen_protection_from_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells_based_on_survival = "OBI:0003471"
    """
    An in vivo assay measuring T cell epitope specific protection from pathogen challenge resulting from the adoptive transfer of epitope specific T cells using survival.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_tumor_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0003472"
    """
    An in vivo assay measuring a T cell epitope specific protection from a tumor challenge after adoptive transfer of epitope specific T cells.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_tumor_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells_based_on_survival = "OBI:0003473"
    """
    An in vivo assay measuring T cell epitope specific protection from tumor challenge resulting from the adoptive transfer of epitope specific T cells using survival.
    """
    in_vivo_assay_measuring_T_cell_epitope_specific_protection_from_other_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_T_cells = "OBI:0003474"
    """
    An in vivo assay measuring a T cell epitope specific protection from other challenge after adoptive transfer of epitope specific T cells.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_pathogen_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0003475"
    """
    An in vivo assay measuring a B cell epitope specific protection from a pathogen challenge after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_pathogen_protection_from_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells_based_on_survival = "OBI:0003476"
    """
    An in vivo assay measuring B cell epitope specific protection from pathogen challenge resulting from the adoptive transfer of epitope specific antibodies or B cells using survival.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_tumor_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0003477"
    """
    An in vivo assay measuring a B cell epitope specific protection from a tumor challenge after adoptive transfer of epitope specific antibodies or B cells.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_tumor_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells_based_on_survival = "OBI:0003478"
    """
    An in vivo assay measuring B cell epitope specific protection from tumor challenge resulting from the adoptive transfer of epitope specific antibodies or B cells using survival.
    """
    in_vivo_assay_measuring_B_cell_epitope_specific_protection_from_other_challenge_resulting_from_the_adoptive_transfer_of_epitope_specific_antibodies_or_B_cells = "OBI:0003479"
    """
    An in vivo assay measuring a B cell epitope specific protection from other challenge after adoptive transfer of epitope specific antibodies or B cells.
    """
    Gram_stain_assay = "OBI:0003480"
    """
    An organism detection assay that identifies bacteria based on the differential retention of a crystal violet-iodine complex within the cell wall.
    """
    assay_measuring_epitope_specific_interleukin_25_production_by_T_cells = "OBI:0003484"
    """
    A T cell epitope specific cytokine production assay that detects interleukin-25 production by T cells.
    """
    detection_of_specific_nucleic_acids_with_complementary_probes_assay_measuring_epitope_specific_interleukin_25_production_by_T_cells = "OBI:0003485"
    """
    A detection of specific nucleic acid polymers with complementary probes that detects interleukin-25 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_25_production_by_T_cells = "OBI:0003486"
    """
    A flow cytometry assay that detects interleukin-25 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_25_production_by_T_cells = "OBI:0003487"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-25 production by T cells.
    """
    cell_culture_analyte_detection_bioassay_measuring_epitope_specific_tumor_necrosis_factor_superfamily_cytokine_production_by_T_cells = "OBI:0003488"
    """
    A reporter cell line analyte detection bioassay that detects tumor necrosis factor superfamily cytokine production by T cells.
    """
    organism_detection_assay = "OBI:0003498"
    """
    An assay that detects a type of organism and/or the quantity of individuals of a type of organism.
    """
    functional_assessment_of_individual = "OBI:0003501"
    """
    A physical examination of an organism's ability to perform functional activities.
    """
    facial_atrophy_assessment = "OBI:0003502"
    """
    An observational assessment of the loss of facial muscle tissue due to inactivity or disease.
    """
    tongue_atrophy_assessment = "OBI:0003503"
    """
    An observational assessment of the loss of muscle tissue related to tongue movement due to inactivity or disease.
    """
    forced_cough_assessment = "OBI:0003504"
    """
    A functional assessment of an individual's ability to cough forcefully.
    """
    speech_test_assessment = "OBI:0003505"
    """
    A functional assessment of an individual's ability to understandably repeat spoken sentences.
    """
    finger_to_finger_assessment = "OBI:0003506"
    """
    A functional assessment of an individual's ability to touch index fingers together in front of the sternum without oscillation for a specified duration of time
    """
    nose_to_finger_assessment = "OBI:0003507"
    """
    A functional assessment of an individual's ability to touch their own nose and then touch an examiners finger in front of them and then touch their own nose once more.
    """
    dysmetria_assessment = "OBI:0003508"
    """
    A functional assessment of an individual's ability to accurately touch a moving target with their finger and then touch their own chin a number of times in a row.
    """
    rapid_alternating_hands_assessment = "OBI:0003509"
    """
    A functional assessment of an individual's ability to alternate the forearm between pronation and suppination as quickly as possible during a specified duration of time
    """
    finger_taps_assessment = "OBI:0003510"
    """
    A functional assessment of an individual's ability to touch their finger-tip to thumb as many times as possible during a specified duration of time.
    """
    heel_along_shin_assessment = "OBI:0003511"
    """
    A functional assessment of an individual's ability to slide their heel back and forth along their contralateral tibia from the patella to the ankle with the contralateral leg extended.
    """
    heel_to_shin_assessment = "OBI:0003512"
    """
    A functional assessment of an individual's ability to tap their heel to the midpoint of the contralateral shin a number of times.
    """
    muscle_atrophy_assessment = "OBI:0003513"
    """
    An observational assesment of an individual's muscle tissue loss due to inactivity or disease.
    """
    muscle_weakness_assessment = "OBI:0003514"
    """
    A functional assessment of an individual's ability to perform muscle movement to overcome gravity or physical resistence.
    """
    vibratory_sense_assessment = "OBI:0003515"
    """
    A functional assessment of an individual's ability to sense vibration.
    """
    position_sense_assessment = "OBI:0003516"
    """
    A functional assessment of an individual's ability to sense the position of a finger or toe that has been manipulated by minimal random movements.
    """
    deep_tendon_reflex_assessment = "OBI:0003517"
    """
    A functional assessment of an individual's muscle contraction when a muscle is triggered by a signal from a muscle spindle in response to a stimulus applied to a specific trigger point on the body.
    """
    limits_of_stability_assessment = "OBI:0003518"
    """
    The functional assessment of an individual's ability to maintain balance, posture or upright stability.
    """
    sitting_posture_assessment = "OBI:0003519"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain unsupported posture while sitting over a given time period.
    """
    stance_feet_apart_assessment = "OBI:0003520"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain a stable stance with feet 20 cm apart.
    """
    stance_feet_apart_assessment_with_eyes_closed = "OBI:0003521"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain a stable stance with their eyes closed.
    """
    stance_feet_together_assessment = "OBI:0003522"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain a stable stance with feet together.
    """
    stance_feet_together_assessment_with_eyes_closed = "OBI:0003523"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain a stable stance with feet together and eyes closed.
    """
    tandem_stance_assessment = "OBI:0003524"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain a stable stance with feet in tandem placement.
    """
    stance_on_one_foot_assessment = "OBI:0003525"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain a stable stance on one foot.
    """
    tandem_walk_assessment = "OBI:0003526"
    """
    A limits of stability assessment designed to assess an individual's ability to maintain balance while walking in a straight line placing steps in tandem.
    """
    gait_assessment = "OBI:0003527"
    """
    A limits of stability assessment designed to assess an individual's manner or pattern of walking.
    """
    bulbar_assessment = "OBI:0003528"
    """
    A functional assessment of an individual's lower cranial nerve function via proxy of facial muscle performance.
    """
    spontaneous_speech_assessment = "OBI:0003529"
    """
    A functional assessment of an individual's ability to articulate spoken words.
    """
    limb_coordination_assessment = "OBI:0003530"
    """
    A functional assessment of an individual's ability to coordinate limb movement.
    """
    upper_limb_coordination_assessment = "OBI:0003531"
    """
    A limb coordination assessment designed to assess an individual's ability to coordinate upper limb movement.
    """
    lower_limb_coordination_assessment = "OBI:0003532"
    """
    A limb coordination assessment designed to assess an individual's ability to coordinate lower limb movement.
    """
    nervous_system_functionality_assessment = "OBI:0003533"
    """
    A functional assesment of an individual's nerve performance. Specifically the nerves connecting the sensory and motor structures with the central nervous system.
    """
    upright_stability_assessment = "OBI:0003534"
    """
    A functional assessment of an individual's ability to maintain upright body posture.
    """
    deep_tendon_reflex_assessment_of_the_knee_joint = "OBI:0003535"
    """
    A deep tendon reflex assessment of an individual's reaction to stimulus applied to a knee joint.
    """
    observational_assessment_of_individual = "OBI:0003536"
    """
    A physical examination of an organism through visual assesment.
    """
    deep_tendon_reflex_assessment_of_the_ankle_joint = "OBI:0003537"
    """
    A deep tendon reflex assessment of an individual's reaction to stimulus applied to an ankle joint.
    """
    deep_tendon_reflex_assessment_of_the_tendon_of_biceps_brachii = "OBI:0003538"
    """
    A deep tendon reflex assessment of an individual's reaction to stimulus applied to a tendon of biceps brachii.
    """
    deep_tendon_reflex_assessment_of_the_brachioradialis = "OBI:0003539"
    """
    A deep tendon reflex assessment of an individual's reaction to stimulus applied to a brachioradialis.
    """
    tandem_mass_spectrometry_assay = "OBI:0003540"
    """
    A mass spectrometry assay that uses two or more analyzers separated by a region in which ions can be induced to fragment by transfer of energy (frequently by collision with other molecules).
    """
    ELISA_measuring_Orientia_tsutsugamushi_IgM_antibody = "OBI:0003541"
    """
    An enzyme-linked immunosorbent assay that detects the IgM antibody that binds Orientia tsutsugamushi.
    """
    microarray_assay_measuring_Dengue_IgM_antibody = "OBI:0003542"
    """
    A microarray assay that detects the IgM antibody that binds Dengue.
    """
    microarray_assay_measuring_NS1 = "OBI:0003543"
    """
    A microarray assay that detects NS1.
    """
    analytical_chromatography_measuring_Chikungunya_IgM_antibody = "OBI:0003544"
    """
    Analytical chromatography that detects the IgM antibody that binds Chikungunya.
    """
    ELISA_measuring_Chikungunya_IgM_antibody = "OBI:0003545"
    """
    An enzyme-linked immunosorbent assay that detects the IgM antibody that binds Chikungunya.
    """
    microarray_ELISA_measuring_Chikungunya_IgM_antibody = "OBI:0003546"
    """
    An enzyme-linked immunosorbent assay that uses a microarray as the solid support and detects the IgM antibody that binds Chikungunya.
    """
    proximity_ligation_assisted_ChIP_seq = "OBI:0003552"
    """
    A chromosome conformation capture assay in which proximity ligation is conducted in nuclei prior to chromatin shearing and immunoprecipitation. Immunopreciptation with an antibody that targets a transcription factor or histone modification allows for selection and enrichment of specific genomic regions for investigation of long-range chromosomal interactions.
    """
    skin_of_body_microbiology_assay = "OBI:0003576"
    """
    An organism detection assay that detects microorganisms in a skin of body specimen.
    """
    bone_marrow_microbiology_assay = "OBI:0003578"
    """
    An organism detection assay that detects microorganisms in a bone marrow specimen.
    """
    nasal_aspirate_microbiology_assay = "OBI:0003580"
    """
    An organism detection assay that detects microorganisms in a nasal aspirate specimen.
    """
    cell_proliferation_assay_using_carboxyfluorescein_succinimidyl_ester_staining = "OBI:0003582"
    """
    A cell proliferation assay that uses carboxyfluorescein succinimidyl ester staining to detect cell division.
    """
    cell_viability_assay = "OBI:0003583"
    """
    A cytometry assay which measures the number of living cells in a population.
    """
    cell_viability_assay_using_Annexin_V_staining = "OBI:0003584"
    """
    A cell viability assay that uses Annexin V staining to detect apoptotic cells.
    """
    cell_culture_assay = "OBI:0003587"
    """
    An assay that has cell culture as an input.
    """
    serum_anti_Epstein_Barr_virus_antibody_level_assay = "OBI:0003589"
    """
    An antigen specific antibodies assay that is meant to detect antibodies that bind to Epstein-Barr virus (EBV) antigens in a serum sample.
    """
    serum_anti_cytomegalovirus_antibody_level_assay = "OBI:0003590"
    """
    A CMV antibody assay that has serum as an input.
    """
    single_cell_B_cell_receptor_repertoire_sequencing_assay = "OBI:0003598"
    """
    A B cell receptor repertoire sequencing assay that determines the sequence of DNA or RNA molecules that encode the repertoire of B cell receptors that can be traced to a single cell of origin.
    """
    single_cell_T_cell_receptor_repertoire_sequencing_assay = "OBI:0003599"
    """
    A T cell receptor repertoire sequencing assay that determines the sequence of DNA or RNA molecules that encode the repertoire of T cell receptors that can be traced to a single cell of origin.
    """
    quartz_crystal_microbalance_assay = "OBI:0003601"
    """
    An assay that measures the change in frequency of a quartz crystal resonator resulting from the addition or removal of a small mass of a ligand specifically binding at the surface of the resonator.
    """
    quartz_crystal_microbalance_assay_measuring_the_dissociation_constant_LEFT_SQUARE_BRACKETKDRIGHT_SQUARE_BRACKET_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:0003602"
    """
    A quartz crystal microbalance assay that measures the dissociation constant [KD] of an antigen binding with an antibody.
    """
    multiplexed_error_robust_fluorescence_in_situ_hybridization_assay = "OBI:0003604"
    """
    A fluorescence in-situ hybridization assay that uses combinatorial FISH labeling with error resistant encoding schemes for highly multiplexed single-molecule imaging.
    """
    single_molecule_fluorescence_in_situ_hybridization = "OBI:0003605"
    """
    A fluorescence in-situ hybridization assay that detects single RNA molecules in fixed cells, allowing for both the quantification and localization at the single-cell level and single-molecule resolution.
    """
    electron_microscopy_assay_determining_the_3D_structure_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:0003612"
    """
    An electron-microscopy 3D molecular structure determination assay that characterizes the 3-dimensional molecular structrue of a T cell epitope:MHC:TCR complex.
    """
    electron_microscopy_assay_determining_the_3D_structure_of_a_MHCCOLONligand_complex = "OBI:0003613"
    """
    An electron-microscopy 3D molecular structure determination assay that characterizes the 3-dimensional molecular structrue of a MHC:ligand complex.
    """
    in_vitro_CRISPR_screen_assay = "OBI:0003659"
    """
    An assay in which cells expressing a Cas system are infected with a library of guide RNAs with the intent of causing a perturbation at the target of the guide RNAs.
    """
    in_vitro_CRISPR_screen_using_single_cell_RNA_seq = "OBI:0003660"
    """
    An in vitro CRISPR screen assay that uses single-cell RNA-Seq to detect induced changes in gene expression.
    """
    in_vitro_CRISPR_screen_using_flow_cytometry = "OBI:0003661"
    """
    An in vitro CRISPR screen assay that uses flow cytometry to detect induced changes in gene expression of the targeted genes.
    """
    single_nucleus_methylcytosine_and_transcriptome_sequencing_assay = "OBI:0003662"
    """
    A DNA methylation profiling by high throughput sequencing assay that measures the cytosine DNA methylation and gene expression signature of single nuclei.
    """
    chromatin_accessibility_assay = "OBI:0003686"
    """
    An assay that determines which regions of a DNA molecule are in the form of euchromatin and thus able to make direct physical contact with (i.e. are accessible to) other molecules such as RNA polymerase, transcription factors, etc.
    """
    m6A_MTase_sequencing_assay = "OBI:0003687"
    """
    A DNA methylation profiling assay in which chromatin stencils are created by treating nuclei with m6A methyltransferase (MTase) and then sequenced using single-molecule circular consensus sequencing to identify regions of accessible DNA at nucleotide resolution.
    """
    assessment_of_learning_andSOLIDUSor_memory_response_in_an_organism = "OBI:0003709"
    """
    A nervous system functionality assessment of learning or memory in an organism
    """
    assessment_of_startle_response_in_an_organism = "OBI:0003710"
    """
    A nervous system functionality assessment of auditory startle response in an organism in an anechoic chamber by exposing to sound.
    """
    grip_strength_assay = "OBI:0003711"
    """
    A nervous system functionality assessment that uses the grip strength of a lab animal to measure neuromuscular function.
    """
    assay_of_organismal_behavior = "OBI:0003712"
    """
    A physical examination to assess behavior quality in a live organism.
    """
    organism_development_assay = "OBI:0003713"
    """
    A physical examination of an organism that provides information about some developmental process in that organism.
    """
    reproductive_assay = "OBI:0003714"
    """
    A physical examination of an organism that provides information about some reproductive process in that organism.
    """
    vital_sign_assay = "OBI:0003715"
    """
    An assay of a organism to measure basic physiological functions such as breathing, pulse, etc. (phylum bilateral).
    """
    blood_pressure_assay = "OBI:0003716"
    """
    A vital sign assay that determines the blood pressure (force of blood against the artery walls) of an organism.
    """
    heart_rate_variability_assay = "OBI:0003717"
    """
    A pulse rate assay that measures beat to beat variability in heart beats.
    """
    pulse_rate_assay = "OBI:0003718"
    """
    A vital sign assay that measures the heart beat rate of an organism.
    """
    respiratory_assay = "OBI:0003719"
    """
    A vital sign assay that measures the quality of respiration / respiratory system of an organism
    """
    cell_differentiation_assay = "OBI:0003720"
    """
    A cytometry assay that monitors the differentiation stage of cells in culture.
    """
    cell_based_DNA_damage_assay = "OBI:0003721"
    """
    A cytometry assay that measures DNA damage in cells.
    """
    natural_killer_cell_count_assay = "OBI:0003722"
    """
    A cytometry assay to determine the number of natural killer cells in a specimen
    """
    natural_killer_cell_percentage_assay = "OBI:0003723"
    """
    A cytometry assay that measures the percentage of natural killer cells in a specimen.
    """
    sperm_count_assay = "OBI:0003724"
    """
    A cytometry assay to count the number of mature sperm in a specimen.
    """
    survey_administration_assay = "OBI:0003725"
    """
    An assay that obtains data from one or more participants by using a survey or questionnaire
    """
    clinical_history_collection_assay = "OBI:0003734"
    """
    A clinical assay that produces a data item indicating whether an organism has ever had a particular disease, lifestyle factor, immune exposure, or medical procedure.
    """
    disease_severity_assay = "OBI:0003735"
    """
    An assay that measures the severity of a disease in an organism.
    """
    genetic_characteristic_assay = "OBI:0003736"
    """
    An assay that produces information about a genetic characteristic of an organism.
    """
    blood_type_assay = "OBI:0003738"
    """
    An assay that classifies an organism's blood within one or more blood group classification systems by identifying antigens present in the blood.
    """
    capillary_electrophoresis_mass_spectrometry_assay = "OBI:0003741"
    """
    A mass spectrometry assay where a sample mixture is first separated by capillary electrophoresis before being analysed by mass spectrometry.
    """
    neurite_outgrowth_assay = "OBI:0003750"
    """
    A cell differentiation assay that detects neurite outgrowth and/or branching
    """
    neuronal_differentiation_assay = "OBI:0003751"
    """
    A cell differentiation assay that measures differentiation of neurons.
    """
    oligodendrocyte_differentiation_assay = "OBI:0003752"
    """
    A cell differentiation assay that measures differentiation of oligodendrocytes.
    """
    regulation_of_synapse_maturation_assay = "OBI:0003753"
    """
    A cell differentiation assay that measures synapse formation and maturation using antibodies to protein found in synaptic puncta.
    """
    Ames_assay = "OBI:0003754"
    """
    A cell based DNA damage assay that uses several constructed bacterial strains to detect mutations.
    """
    micronucleus_assay = "OBI:0003755"
    """
    A cell based DNA damage assay in eukaryotic cells that detects cytoplasmic micronuclei.
    """
    PIG_a_assay = "OBI:0003756"
    """
    A cell based DNA damage assay in eukaryotic cells that detects loss of function through mutation of the X-linked (single-copy) Pig-a gene.
    """
    cell_viability_assay_based_on_detection_of_resorufin = "OBI:0003757"
    """
    A cell viability assay using the NAD(P)H-aided conversion of resazurin to resorufin by metabolically active cells.
    """
    cell_death_assay_using_caspase_abundance_to_detect_apoptosis = "OBI:0003758"
    """
    A cell death assay that uses fluorescence imaging-based detection of caspases involved in apoptosis
    """
    cell_death_assay = "OBI:0003759"
    """
    A cell viability assay which measures the number or proportion of dead cells in a population.
    """
    cell_viability_assay_based_on_detection_of_resorufin_using_fluorescence_to_qualtify_the_presence_of_resorufinFULL_STOP = "OBI:0003760"
    """
    A cell viability assay based on detection of resorufin that uses fluorescence to quantify resorufin
    """
    cell_death_assay_detecting_lactate_dehydrogenase_LEFT_PARENTHESISLDHRIGHT_PARENTHESIS_release = "OBI:0003761"
    """
    A cell death assay that measures the release of intracellular LDH.
    """
    cell_death_assay_detecting_lactate_dehydrogenase_LEFT_PARENTHESISLDHRIGHT_PARENTHESIS_release_using_absorbance_detectionFULL_STOP = "OBI:0003762"
    """
    A cell death assay detecting lactate dehydrogenase (LDH) release by absorbance of substrate
    """
    ovulation_assessment_in_rodent_assay = "OBI:0003763"
    """
    A histological assay that measures the number of corpora lutea (UBERON:0002512) in the ovary of an organism; corpora lutea develop from the postovulatory follicle.
    """
    macroscopic_examination_of_material_anatomical_entity_assay = "OBI:0003764"
    """
    An assay that performs a macroscopic assessment of a material anatomical entity using the sense of sight.
    """
    pathological_macroscopic_examination_of_specimen_assay = "OBI:0003765"
    """
    A macroscopic examination of material anatomical entity assay performed on a post-mortem anatomical specimen.
    """
    estrous_cycle_assay_based_on_tissue_morphology = "OBI:0003766"
    """
    A histological assay that evaluates cells in the vaginal endometrium to assess the estrous cycle phase the subject was in at the time of specimen collection.
    """
    organism_development_assay_in_late_embryo = "OBI:0003767"
    """
    An organism development assay performed with a late embryo stage subject.
    """
    pregnancy_assessment_based_on_tissue_morphology_assay = "OBI:0003768"
    """
    A histological assay that measures the number of implantation sites in an organism.
    """
    cell_death_assay_using_vital_dye = "OBI:0003769"
    """
    A cell death assay that uses the Trypan blue vital dye to stain cells which have lost membrane integrity.
    """
    neurite_length_assay = "OBI:0003770"
    """
    A cytometry assay that uses a distance measurement assay to determine the length of a neurite.
    """
    neurite_degree_of_arborization_assay = "OBI:0003771"
    """
    A cytometry assay that measures the degree of arborization, or branching, in neuronal processes
    """
    neurite_count_assay = "OBI:0003772"
    """
    A cytometry assay that measures the number of neurites in a cultured specimen.
    """
    neuron_count_assay = "OBI:0003773"
    """
    A cytometry assay that measures the number of neurons in a sample
    """
    cell_body_associated_presynaptic_puncta_count_assay = "OBI:0003774"
    """
    A regulation of synapse maturation assay that determines the number of  synaptic puncta in the cell body compartment of a neuron.
    """
    dendrite_associated_presynaptic_puncta_count_assay = "OBI:0003775"
    """
    A regulation of synapse maturation assay that determines the number of synaptic puncta in the dendritic compartment of a neuron.
    """
    synapse_per_neuron_assay = "OBI:0003776"
    """
    A regulation of synapse maturation assay that determines the number of synaptic puncta in a culture and normalizes it by the number of neurons in the culture.
    """
    absorbance_quality_detection_assay = "OBI:0003777"
    """
    An assay that measures the absorbance quality of the evaluant
    """
    hormone_assay = "OBI:0003778"
    """
    The analyte assay that measures the abundance of a hormone in a specimen.
    """
    chemiluminescent_assay = "OBI:0003779"
    """
    An analyte assay that detects a substance by measuring the release of light triggered by a chemical reaction.
    """
    electrochemiluminescence_assay = "OBI:0003780"
    """
    A chemiluminescent assay that detects a substance by measuring the release of light triggered by an electrochemical reaction.
    """
    proteomics_by_mass_spectrometry_assay = "OBI:0003781"
    """
    A mass spectrometry assay that identifies and measures proteins.
    """
    metabolomics_by_mass_spectrometry_assay = "OBI:0003782"
    """
    A mass spectrometry assay that identifies and measures metabolites.
    """
    cellular_indexing_of_transcriptomes_and_epitopes_by_sequencing = "OBI:0003788"
    """
    An assay performed on single cells that simultaneously measures transcript expression via single-cell RNA sequencing and profiles surface proteins via sequencing of DNA-barcodes attached to antibodies recognizing particular surface proteins from individual cells.
    """
    immune_receptor_repertoire_profiling_assay = "OBI:0003789"
    """
    An assay that determines the sequence of a DNA or RNA molecules that encode the repertoire of B cell receptors or T cell receptors within an input sample.
    """
    antibody_dependent_complement_deposition_assay = "OBI:0003790"
    """
    An assay measuring antibody-dependent complement-dependent cytotoxicity.
    """
    bacterial_flagellin_detection_in_plasma_assay = "OBI:0003791"
    """
    An analyte assay measuring bacterial flagellin in a plasma sample.
    """
    bacterial_flagellin_detection_in_feces_assay = "OBI:0003792"
    """
    An analyte assay measuring bacterial flagellin in a feces sample.
    """
    bacterial_lipopolysaccharide_detection_in_plasma_assay = "OBI:0003793"
    """
    An analyte assay measuring bacterial lipopolysaccharide in a plasma sample.
    """
    bacterial_lipopolysaccharide_detection_in_feces_assay = "OBI:0003794"
    """
    An analyte assay measuring bacterial lipopolysaccharide in a feces sample.
    """
    adenosine_deaminase_activity_assay = "OBI:0003795"
    """
    An analyte assay measuring adenosine deaminase activity in a sample.
    """
    pathogen_neutralization_assay = "OBI:0003796"
    """
    An assay that measures neutralization of a pathogen.
    """
    bacterial_neutralization_assay = "OBI:0003797"
    """
    A pathogen neutralization assay measuring neutralization of bacteria.
    """
    viral_plaque_assay = "OBI:0003798"
    """
    An analyte assay measuring the number of discrete viral plaques.
    """
    analyte_detection_by_flow_based_bead_assay = "OBI:0003799"
    """
    An analyte assay that uses beads to measure the concentration of an analyte with a flow cytometer.
    """
    urine_opacity_assay = "OBI:0003801"
    """
    A histological assay with urine evaluant that measures opacity of the urine
    """
    urine_color_assay = "OBI:0003802"
    """
    A histological assay with urine evaluant that measures color.
    """
    urine_histological_assay = "OBI:0003803"
    """
    A histological assay with urine sediment as evaluant.
    """
    color_detection_assay = "OBI:0003804"
    """
    An assay that measures the color of the evaluant
    """
    opacity_determination_assay = "OBI:0003805"
    """
    An assay that measures the opacity of the evaluant
    """
    estrous_cycle_count_assay = "OBI:0003811"
    """
    An estrous cycle assay based on tissue morphology that determines the number of estrous cycles observed in a defined time.
    """
    estrous_cycle_duration_assay = "OBI:0003812"
    """
    An estrous cycle assay based on tissue morphology that determines the average length of a full estrous cycle observed in a defined time.
    """
    organism_development_assay_in_late_embryo_based_on_examination_of_surface_structure = "OBI:0003813"
    """
    An organism development assay in late embryo that evaluates only the external surface structure of the organism
    """
    organism_development_assay_in_late_embryo_based_on_examination_of_skeletal_system = "OBI:0003814"
    """
    An organism development assay in late embryo that evaluates the skeletal system of the organism
    """
    organism_development_assay_in_late_embryo_based_on_examination_of_anatomical_system = "OBI:0003815"
    """
    An organism development assay in late embryo that evaluates the anatomical system of the organism
    """
    distance_measurement_assay = "OBI:0003816"
    """
    An assay that measures the space between two entities.
    """
    length_measurement_assay = "OBI:0003817"
    """
    An assay that measures the distance between two points.
    """
    crown_rump_length = "OBI:0003818"
    """
    A length measurement assay that measures the length of a neonate or fetus from crown of head to base of torso (rump)
    """
    path_length_assay = "OBI:0003819"
    """
    An assay that measures the distance traveled in a defined period of time.
    """
    cell_migration_assay = "OBI:0003820"
    """
    A distance measurement assay in which the migration of cells in culture is monitored by measuring the distance between the start position and the cell's location when observed.
    """
    oligodendrocyte_migration_assay = "OBI:0003821"
    """
    A cell migration assay that measures migration of an oligodendrocyte
    """
    radial_glial_migration_assay = "OBI:0003822"
    """
    A cell migration assay that measures migration of a radial glia cell
    """
    neuron_migration_assay = "OBI:0003823"
    """
    A cell migration assay that measures migration of a neuron
    """
    neural_crest_cell_migration_assay = "OBI:0003824"
    """
    A cell migration assay that measures migration of a neural crest cell
    """
    acidity_quality_assay = "OBI:0003825"
    """
    An assay that measures the acidity of a specimen on the pH scale.
    """
    specific_gravity_assay = "OBI:0003826"
    """
    An assay that measures the specific gravity of a sample.
    """
    speed_measurement_assay = "OBI:0003827"
    """
    An assay to determine the speed of an evaluant.
    """
    velocity_measurement_assay = "OBI:0003828"
    """
    An assay to measure the velocity of an evaluant
    """
    luminescence_detection_assay = "OBI:0003829"
    """
    An assay that measures the luminescence of the evaluant
    """
    cell_viability_assay_using_luciferase_to_detect_ATP_in_the_cell = "OBI:0003830"
    """
    A cell viability assay that uses an ATP bioluminescence assay to detect ATP in the living cell
    """
    population_count_assay = "OBI:0003831"
    """
    An assay that measures the number of elements in a portion of a population
    """
    hemolysis_assay = "OBI:0003832"
    """
    A hematology assay that measures the fragility of red blood cells by observing spillage of hemoglobin from burst cells.
    """
    neuron_action_potential_rate_assay = "OBI:0003833"
    """
    An electrophysiology assay that measures action potential events in neurons during a time period.
    """
    neuron_burst_rate_assay = "OBI:0003834"
    """
    An electrophysiology assay that measures the number of action potential bursts in neurons during a time period.
    """
    neuron_interburst_interval_assay = "OBI:0003835"
    """
    An electrophysiology assay that measures the elapsed time between consecutive action potential bursts in neurons.
    """
    neuron_burst_duration_assay = "OBI:0003836"
    """
    An electrophysiology assay that measures the time elapsed between the first action potential in a neuron burst and the last in that burst.
    """
    action_potential_interval_assay = "OBI:0003837"
    """
    An electrophysiology assay that measures the time elapsed between the peaks of consecutive action potential spikes in a neuron burst.
    """
    rate_of_action_potentials_in_neuron_burst_assay = "OBI:0003838"
    """
    An electrophysiology assay that measures the number of action potential spikes occurring within a neuron burst
    """
    body_mass_assay = "OBI:0003839"
    """
    A mass measurement assay with evaluant an individual organism.
    """
    body_mass_change_assay = "OBI:0003840"
    """
    A body mass assay that measures the change in body mass for a subject over a period of time.
    """
    body_weight_assay_at_death = "OBI:0003841"
    """
    A body weight assay with evaluant individual organism specimen with quality dead.
    """
    tissue_mass_assay = "OBI:0003842"
    """
    A mass measurement assay with evaluant tissue or bodily fluid specimen.
    """
    tissue_mass_percent_of_body_mass_assay = "OBI:0003843"
    """
    A mass measurement assay with evaluant tissue expressed as a percentage of the body weight of the organism from which the specimen was derived.
    """
    developmental_marker_age_of_attainment_assessment = "OBI:0003844"
    """
    An age determination assay which determines the age of the subject at the time of the change from a state where it did not have a developmental stage marker to one in which it does.
    """
    cytochrome_P450_assay = "OBI:0003850"
    """
    A protein assay that measures the abundance of cytochrome P450 in a specimen.
    """
    growth_factor_assay = "OBI:0003851"
    """
    An analyte assay to measure the abundance of one or more growth factors in a volume of sample.
    """
    Hoechst_dye_assay = "OBI:0003852"
    """
    A fluorescence imaging-based cell morphology assay that uses Hoechst dye 33342
    """
    hypersensitivity_assay = "OBI:0003853"
    """
    An immune response assay to assess the hypersensitivity response in an organism or cell culture.
    """
    super_resolution_microscopy_assay = "OBI:0003882"
    """
    A type of light microscopy assay where the images are taken with a resolution higher than the diffraction limit.
    """
    number_1M7_RNA_structure_mapping_assay = "OBI:0003885"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 1-methyl-7-nitroisatoic anhydride as reagent and chemical probe
    """
    NAI_RNA_structure_mapping_assay = "OBI:0003886"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 2-methylnicotinic acid imidazolide as reagent and chemical probe
    """
    NAI_N3_RNA_structure_mapping_assay = "OBI:0003887"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 2-(azidomethyl)nicotinic acid imidazolide as reagent and chemical probe
    """
    number_2A3_RNA_structure_mapping_assay = "OBI:0003888"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 2-aminopyridine-3-carboxylic acid imidazolide as reagent and chemical probe
    """
    I5_RNA_structure_mapping_assay = "OBI:0003889"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using indoline-5-carboxylic acid imidazolide as reagent and chemical probe
    """
    number_1M4_RNA_structure_mapping_assay = "OBI:0003890"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 1-methylimidazole-4-carboxylic acid imidazolide as reagent and chemical probe
    """
    number_6A3_RNA_structure_mapping_assay = "OBI:0003891"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 6-aminopyridine-3-carboxylic acid imidazolide as reagent and chemical probe
    """
    B5_RNA_structure_mapping_assay = "OBI:0003892"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using benzotriazole-5-carboxylic acid imidazolide as reagent and chemical probe
    """
    NIC_RNA_structure_mapping_assay = "OBI:0003893"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using nicotinic acid imidazolide as reagent and chemical probe
    """
    BzCN_RNA_structure_mapping_assay = "OBI:0003894"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using benzoyl cyanide as reagent and chemical probe
    """
    number_1M6_RNA_structure_mapping_assay = "OBI:0003895"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 1-methyl-6-nitroisatoic anhydride as reagent and chemical probe
    """
    number_5NIA_RNA_structure_mapping_assay = "OBI:0003896"
    """
    A single-nucleotide-resolution ribonucleic acid structure mapping assay that determines nucleic acid secondary structure at the nucleotide resolution scale using 5-nitroisatoic anhydride as reagent and chemical probe
    """
    cell_count_assay = "OBI:0003897"
    """
    An assay that measures the number of cells in a portion of a cell culture or tissue or bodily fluid
    """
    differential_leukocyte_count_assay = "OBI:0003898"
    """
    A hematology assay that measures the percentage of classes of leukocytes in a sample.
    """
    electrocardiogram_assay = "OBI:0003899"
    """
    An electrophysiology assay that measures heart activity using electrodes placed to detect electrical signals from the heart.
    """
    telemeter_sensor_detection_assay = "OBI:0003900"
    """
    An assay which uses an implanted telemeter to measure physiological data in a living organism and transmit the measures via radio waves to a recording device.
    """
    multi_electrode_array_assay = "OBI:0003901"
    """
    A multi-unit recording assay using a multi-electrode array (MEA) on the surface of a well on a cell culture plate.
    """
    transepithelial_SOLIDUS_transendothelial_electrical_resistance_LEFT_PARENTHESISTEERRIGHT_PARENTHESIS_assay = "OBI:0003902"
    """
    An extracellular electrophysiology recording assay to measure the integrity of a cell monolayer
    """
    count_of_multi_electrode_plate_electrodes_detecting_action_potential_assay = "OBI:0003903"
    """
    A multi-electrode array assay that measures the number of electrodes in a well where the mean rate of action potentials is at least 5 spikes per minute.
    """
    count_of_multi_electrode_plate_electrodes_detecting_neuron_burst_assay = "OBI:0003904"
    """
    A multi-electrode array assay that measures the number of electrodes in a well where the burst rate is at least 0.5 bursts per minute.
    """
    neural_network_spike_rate_assay = "OBI:0003905"
    """
    An multi-electrode assay that measures the number of events when multiple electrodes simultaneously detect an action potential during a time period.
    """
    neural_network_spike_duration_assay = "OBI:0003906"
    """
    A multi-electrode assay that measures the mean duration of events when multiple electrodes detect an action potential
    """
    count_of_multi_electrode_plate_electrodes_detecting_spike_peak_assay = "OBI:0003907"
    """
    A multi-electrode array assay that measures the average number of electrodes detecting a network spike, measured at the peak of a network spike.
    """
    mean_interspike_interval_in_network_spike = "OBI:0003908"
    """
    A multi-electrode assay that measures the average interval between network spikes, events where multiple electrodes simultaneously detect an action potential.
    """
    bile_acid_concentration_assay = "OBI:0003909"
    """
    An analyte assay that measures the abundance of bile acid in a volume of sample.
    """
    urea_nitrogen_assay = "OBI:0003910"
    """
    An analyte assay that measures the abundance of urea nitrogen.
    """
    urea_nitrogen_concentration_assay = "OBI:0003911"
    """
    A urea nitrogen assay that measures the abundance of urea nitrogen in a specimen
    """
    in_vitro_CRISPR_screen_using_single_cell_ATAC_seq = "OBI:0003912"
    """
    An in vitro CRISPR screen assay that uses single-cell ATAC-Seq to detect induced changes in chromatin accessibility
    """
    single_cell_metabolically_labeled_new_RNA_tagging_sequencing = "OBI:0003913"
    """
    A single-cell transcription profiling by RNA sequencing assay in which mRNA transcripts are metabolically labeled with 4-thiouridine to investigate temporal RNA dynamics.
    """
    single_cell_massively_parallel_reporter_assay = "OBI:0003914"
    """
    A massively parallel reporter assay in which libraries of reporter constructs are transfected into samples and then measured via single cell transcriptomic methods to enable discovery of cell-specific transcriptional regulatory activity
    """
    ultra_high_throughput_single_cell_combinatorial_indexing_RNA_sequencing_3_assay = "OBI:0003915"
    """
    A single-cell transcription profiling by RNA sequencing assay that involves single cell combinatorial indexing ('sci-') to profile the transcriptomes of single cells or nuclei in an ultra high-throughput manor via changes to the method, as compared to sci-RNA-seq, that include extraction of nuclei directly from fresh tissue, use of hairpin ligation for the third level of indexing, optimization of enxymatic reactions, and use of dilution instead of FACS sorting.
    """
    DNA_damage_comet_assay = "OBI:0302736"
    """
    A cell based DNA damage assay that measures DNA damage (DNA breakage) in eucaryotic cells exposed to a challenge by determining the size and shape of DNA migration by detecting fluorescently labeled DNA from a cell placed in an electric field using gel electrophoresis
    """
    PCR_SSCP_assay = "OBI:0302737"
    """
    An assay that identifies DNA sequence variation (mutation, deletion, insertions) in target DNA sequences amplified using polymerase chain reaction using gel electrophoresis and denaturating conditions
    """
    tumor_grading = "OBI:0600002"
    """
    An assay that determines the grade (severity/stage) of a tumor sample, used in cancer biology to describe abnormalities/qualities of tumor cells or tissues. Values can be described by terms from NCI Thesaurus.
    """
    assay_detecting_a_molecular_label = "OBI:0600017"
    """
    An assay that detects the presence or a quality of a molecular label which is a proxy for the detection of the molecular target to which the label is attached
    """
    histological_assay = "OBI:0600020"
    """
    An assay that uses visual examination of cells or tissue (or images of them) to make an assessment regarding a quality of the cells or tissue. This assay can include steps of staining, imaging, and judgement.
    """
    substance_detection_assay = "OBI:0600025"
    """
    An assay that detects a specified substance
    """
    longitudinal_mass_measurement_assay = "OBI:0600026"
    """
    An assay that measures the mass of a material at two or more time points
    """
    enzyme_linked_immunospot_assay = "OBI:0600031"
    """
    A cytometry assay in which cells are cultured on a surface coated with a capture antibody binding a secretory material of interest which subsequently gets stained resulting in a spot for each cell producing the secretory material of interest.
    """
    number_3D_structure_determination_assay = "OBI:0600045"
    """
    An assay that determines the 3-dimensional configuration of an input material.
    """
    sequencing_assay = "OBI:0600047"
    """
    An assay the uses chemical or biochemical means to infer the sequence of a biomaterial
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:1110013"
    """
    An enzyme-linked immunospot assay that detects interleukin-2 production by T cells.
    """
    assay_measuring_binding_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:1110037"
    """
    A T cell epitope assay that measures the binding of T cell receptor to an epitope.
    """
    ELISPOT_assay_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:1110059"
    """
    An enzyme-linked immunospot assay that detects interferon-gamma production by T cells.
    """
    assay_measuring_qualitative_binding_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:1110124"
    """
    An assay that detects the binding of a MHC:epitope complex with a T cell receptor, and produces a qualitative measurement of the binding as an output.
    """
    assay_measuring_MHC_ligand_processing_and_presentation = "OBI:1110125"
    """
    A MHC ligand assay that determines what ligands are processed and loaded onto MHC molecules by eluting ligands and identifying them.
    """
    assay_measuring_binding_of_a_MHCCOLONligand_complex = "OBI:1110126"
    """
    A MHC ligand assay that detects the binding of a ligand to an MHC molecule.
    """
    assay_measuring_binding_of_a_B_cell_epitopeCOLONantibody_complex = "OBI:1110127"
    """
    A B cell epitope assay that measures the binding of an antibody receptor to an epitope.
    """
    immune_epitope_assay = "OBI:1110128"
    """
    An assay that detects the binding of an epitope to an adaptive immune receptor, or an immune process resulting from such a binding event, or characterizes the structrue of the complex resulting from such a binding event.
    """
    assay_measuring_epitope_specific_cytokine_production_by_T_cells = "OBI:1110129"
    """
    A T cell epitope assay that detects cytokine production by T cells.
    """
    assay_measuring_epitope_specific_T_cell_killing = "OBI:1110130"
    """
    A T cell epitope dependent biological activity assay that detects the killing of an antigen presenting cell (APC) by a T cell whose TCR recognizes an epitope presented by the APC.
    """
    assay_measuring_epitope_specific_proliferation_of_T_cells = "OBI:1110131"
    """
    A T cell epitope dependent biological activity assay that detects T cell proliferation.
    """
    number_51_chromium_assay_measuring_epitope_specific_T_cell_killing = "OBI:1110150"
    """
    A chromium release assay that detects the killing of an antigen presenting cell (APC) by a T cell whose TCR recognizes an epitope presented by the APC.
    """
    ELISA_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:1110151"
    """
    An enzyme-linked immunosorbent assay that detects interferon-gamma production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:1110152"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-2 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_4_production_by_T_cells = "OBI:1110153"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-4 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_5_production_by_T_cells = "OBI:1110154"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-5 production by T cells.
    """
    ELISA_measuring_epitope_specific_tumor_necrosis_factor_alpha_production_by_T_cells = "OBI:1110155"
    """
    An enzyme-linked immunosorbent assay that detects tumor necrosis factor alpha production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_10_production_by_T_cells = "OBI:1110156"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-10 production by T cells.
    """
    ELISA_measuring_epitope_specific_granulocyte_macrophage_colony_stimulating_factor_production_by_T_cells = "OBI:1110157"
    """
    An enzyme-linked immunosorbent assay that detects granulocyte macrophage colony stimulating factor production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_6_production_by_T_cells = "OBI:1110158"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-6 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_13_production_by_T_cells = "OBI:1110159"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-13 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_12_production_by_T_cells = "OBI:1110160"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-12 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_1_beta_production_by_T_cells = "OBI:1110161"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-1 beta production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_17_production_by_T_cells = "OBI:1110162"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-17 production by T cells.
    """
    ELISA_measuring_epitope_specific_interleukin_18_production_by_T_cells = "OBI:1110163"
    """
    An enzyme-linked immunosorbent assay that detects interleukin-18 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_4_production_by_T_cells = "OBI:1110167"
    """
    An enzyme-linked immunospot assay that detects interleukin-4 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_tumor_necrosis_factor_alpha_production_by_T_cells = "OBI:1110168"
    """
    An enzyme-linked immunospot assay that detects tumor necrosis factor alpha production by T cells
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_10_production_by_T_cells = "OBI:1110170"
    """
    An enzyme-linked immunospot assay that detects interleukin-10 production by T cells.
    """
    ELISPOT_assay_measuring_epitope_specific_interleukin_13_production_by_T_cells = "OBI:1110171"
    """
    An enzyme-linked immunospot assay that detects interleukin-13 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interferon_gamma_production_by_T_cells = "OBI:1110172"
    """
    A flow cytometry assay that detects interferon-gamma production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_2_production_by_T_cells = "OBI:1110173"
    """
    A flow cytometry assay that detects interleukin-2 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_tumor_necrosis_factor_alpha_production_by_T_cells = "OBI:1110174"
    """
    A flow cytometry assay that detects tumor necrosis factor alpha production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_4_production_by_T_cells = "OBI:1110175"
    """
    A flow cytometry assay that detects interleukin-4 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_10_production_by_T_cells = "OBI:1110177"
    """
    A flow cytometry assay that detects interleukin-10 production by T cells.
    """
    intracellular_cytokine_staining_assay_measuring_epitope_specific_interleukin_17_production_by_T_cells = "OBI:1110178"
    """
    A flow cytometry assay that detects interleukin-17 production by T cells.
    """
    MHC_tetramerSOLIDUSmultimer_assay_measuring_binding_of_a_T_cell_epitopeCOLONMHCCOLONTCR_complex = "OBI:1110179"
    """
    A MHC tetramer/multimer assay that measures the binding of an epitope:MHC complex binding with a T cell receptor.
    """
    number_3H_thymidine_assay_measuring_epitope_specific_proliferation_of_T_cells = "OBI:1110180"
    """
    A tritiated thymidine incorporation assay that detects T cell epitope specific proliferation in vitro.
    """
    BrdU_assay_measuring_epitope_specific_proliferation_of_T_cells = "OBI:1110181"
    """
    A BrdU incorporation assay that detects T cell epitope specific proliferation in vitro.
    """
    assay_detecting_IFN_gamma_production = "OBI:1110207"
    """
    An assay that determines information about the production of the cytokine interferon gamma
    """
    carbon_dioxide_assay = "OBI:2100001"
    """
    An analyte assay that measures the abundance of carbon dioxide
    """
    sodiumLEFT_PARENTHESIS1PLUS_SIGNRIGHT_PARENTHESIS_assay = "OBI:2100002"
    """
    An analyte assay that measures the abundance of sodium(1+)
    """
    creatinine_assay = "OBI:2100003"
    """
    An analyte assay that measures the abundance of creatinine
    """
    potassiumLEFT_PARENTHESIS1PLUS_SIGNRIGHT_PARENTHESIS_assay = "OBI:2100004"
    """
    An analyte assay that measures the abundance of potassium(1+)
    """
    basophil_count_assay = "OBI:2100005"
    """
    A cytometry assay that measures the count of basophils
    """
    neutrophil_count_assay = "OBI:2100006"
    """
    A cytometry assay that measures the count of neutrophils
    """
    eosinophil_count_assay = "OBI:2100007"
    """
    A cytometry assay that measures the count of eosinophils
    """
    lymphocyte_count_assay = "OBI:2100008"
    """
    A cytometry assay that measures the count of lymphocytes
    """
    monocyte_count_assay = "OBI:2100009"
    """
    A cytometry assay that measures the count of monocytes
    """
    chloride_assay = "OBI:2100010"
    """
    An analyte assay that measures the abundance of chloride
    """
    erythrocyte_count_assay = "OBI:2100011"
    """
    A cytometry assay that measures the count of erythrocytes
    """
    platelet_count_assay = "OBI:2100012"
    """
    A cytometry assay that measures the count of platelets
    """
    leukocyte_count_assay = "OBI:2100013"
    """
    A cytometry assay that measures the count of leukocytes
    """
    hemoglobin_assay = "OBI:2100014"
    """
    An analyte assay that measures the abundance of hemoglobin
    """
    phosphate_ion_assay = "OBI:2100015"
    """
    An analyte assay that measures the abundance of phosphate ion
    """
    alanine_aminotransferase_assay = "OBI:2100016"
    """
    An analyte assay that measures the abundance of alanine aminotransferase
    """
    alkaline_phosphatase_LEFT_PARENTHESIShumanRIGHT_PARENTHESIS_assay = "OBI:2100017"
    """
    An analyte assay that measures the abundance of alkaline phosphatase (human)
    """
    bilirubin_IXalpha_assay = "OBI:2100018"
    """
    An analyte assay that measures the abundance of bilirubin IXalpha
    """
    aspartate_aminotransferase_LEFT_PARENTHESIShumanRIGHT_PARENTHESIS_assay = "OBI:2100019"
    """
    An analyte assay that measures the abundance of aspartate aminotransferase (human)
    """
    glucose_assay = "OBI:2100020"
    """
    An analyte assay that measures the abundance of glucose
    """
    magnesium_cation_assay = "OBI:2100021"
    """
    An analyte assay that measures the abundance of magnesium cation
    """
    albumin_assay = "OBI:2100022"
    """
    An analyte assay that measures the abundance of albumin
    """
    protein_assay = "OBI:2100023"
    """
    An analyte assay that measures the abundance of protein
    """
    calcium_cation_assay = "OBI:2100024"
    """
    An analyte assay that measures the abundance of calcium cation
    """
    creatine_kinase_assay = "OBI:2100025"
    """
    An analyte assay that measures the abundance of creatine kinase
    """
    nucleate_erythrocyte_count_assay = "OBI:2100026"
    """
    A cytometry assay that measures the count of nucleate erythrocytes
    """
    segmented_neutrophil_of_bone_marrow_count_assay = "OBI:2100027"
    """
    A cytometry assay that measures the count of segmented neutrophil of bone marrows
    """
    lactate_dehydrogenase_complex_assay = "OBI:2100028"
    """
    An assay that measures lactate dehydrogenase complex
    """
    triglyceride_assay = "OBI:2100029"
    """
    An analyte assay that measures the abundance of triglyceride
    """
    high_density_lipoprotein_cholesterol_assay = "OBI:2100030"
    """
    An analyte assay that measures the abundance of high-density lipoprotein cholesterol
    """
    cholesterol_assay = "OBI:2100031"
    """
    An analyte assay that measures the abundance of cholesterol
    """
    low_density_lipoprotein_cholesterol_assay = "OBI:2100032"
    """
    An analyte assay that measures the abundance of low-density lipoprotein cholesterol
    """
    thyroid_stimulating_hormone_assay = "OBI:2100033"
    """
    An analyte assay that measures the abundance of thyroid stimulating hormone
    """
    prostate_specific_antigen_assay = "OBI:2100034"
    """
    An analyte assay that measures the abundance of prostate-specific antigen
    """
    thyroxine_assay = "OBI:2100035"
    """
    An analyte assay that measures the abundance of thyroxine
    """
    elemental_oxygen_assay = "OBI:2100036"
    """
    An analyte assay that measures the abundance of elemental oxygen
    """
    folic_acids_assay = "OBI:2100037"
    """
    An analyte assay that measures the abundance of folic acids
    """
    reticulocyte_count_assay = "OBI:2100038"
    """
    A cytometry assay that measures the count of reticulocytes
    """
    osmolality_assay = "OBI:2100039"
    """
    An assay that measures osmolality
    """
    methemoglobin_assay = "OBI:2100040"
    """
    An analyte assay that measures the abundance of methemoglobin
    """
    cytosolic_creatine_kinase_complex_MB_type_assay = "OBI:2100041"
    """
    An assay that measures cytosolic creatine kinase complex, MB-type
    """
    rac_lactic_acid_assay = "OBI:2100042"
    """
    An assay that measures rac-lactic acid
    """
    hydrogencarbonate_assay = "OBI:2100043"
    """
    An analyte assay that measures the abundance of hydrogencarbonate
    """
    vancomycin_assay = "OBI:2100044"
    """
    An analyte assay that measures the abundance of vancomycin
    """
    tobramycin_assay = "OBI:2100045"
    """
    An analyte assay that measures the abundance of tobramycin
    """
    number_33APOSTROPHE5APOSTROPHE_triiodothyronine_assay = "OBI:2100046"
    """
    An analyte assay that measures the abundance of 3,3',5'-triiodothyronine
    """
    C_reactive_protein_assay = "OBI:2100047"
    """
    An analyte assay that measures the abundance of C-reactive protein
    """
    megakaryocyte_count_assay = "OBI:2100048"
    """
    A cytometry assay that measures the count of megakaryocytes
    """
    mesothelial_cell_count_assay = "OBI:2100049"
    """
    A cytometry assay that measures the count of mesothelial cells
    """
    macrophage_count_assay = "OBI:2100050"
    """
    A cytometry assay that measures the count of macrophages
    """
    number_3_hydroxybutyric_acid_assay = "OBI:2100051"
    """
    An analyte assay that measures the abundance of 3-hydroxybutyric acid
    """
    panel5_venous_blood_carbon_dioxide_assay = "OBI:2100052"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a panel5 order
    """
    panel5_venous_blood_sodium_assay = "OBI:2100053"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a panel5 order
    """
    panel5_venous_blood_creatinine_assay = "OBI:2100054"
    """
    An analyte assay that measures the abundance of creatinine in venous blood as part of a panel5 order
    """
    panel5_venous_blood_potassium_assay = "OBI:2100055"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a panel5 order
    """
    automated_differential_venous_blood_basophil_count_assay = "OBI:2100056"
    """
    A cytometry assay that measures the count of basophils in venous blood as part of a automated differential order
    """
    automated_differential_venous_blood_neutrophil_count_assay = "OBI:2100057"
    """
    A cytometry assay that measures the count of neutrophils in venous blood as part of a automated differential order
    """
    automated_differential_venous_blood_eosinophil_count_assay = "OBI:2100058"
    """
    A cytometry assay that measures the count of eosinophils in venous blood as part of a automated differential order
    """
    automated_differential_venous_blood_lymphocyte_count_assay = "OBI:2100059"
    """
    A cytometry assay that measures the count of lymphocytes in venous blood as part of a automated differential order
    """
    automated_differential_venous_blood_monocyte_count_assay = "OBI:2100060"
    """
    A cytometry assay that measures the count of monocytes in venous blood as part of a automated differential order
    """
    venous_blood_chloride_assay = "OBI:2100061"
    """
    An analyte assay that measures the abundance of chloride in venous blood
    """
    CBC_with_automated_differential_venous_blood_RBC_count_assay = "OBI:2100062"
    """
    A cytometry assay that measures the count of RBCs in venous blood as part of a CBC with automated differential order
    """
    CBC_with_automated_differential_venous_blood_platelet_count_assay = "OBI:2100063"
    """
    A cytometry assay that measures the count of platelets in venous blood as part of a CBC with automated differential order
    """
    CBC_with_automated_differential_venous_blood_WBC_count_assay = "OBI:2100064"
    """
    A cytometry assay that measures the count of WBCs in venous blood as part of a CBC with automated differential order
    """
    CBC_with_automated_differential_venous_blood_hematocrit_assay = "OBI:2100065"
    """
    A cytometry assay that measures the proportion of red blood cells in venous blood as part of a CBC with automated differential order
    """
    CBC_with_automated_differential_venous_blood_hemoglobin_assay = "OBI:2100066"
    """
    An analyte assay that measures the abundance of hemoglobin in venous blood as part of a CBC with automated differential order
    """
    venous_blood_phosphate_assay = "OBI:2100067"
    """
    An analyte assay that measures the abundance of phosphate in venous blood
    """
    liver_injury_venous_blood_alanine_aminotransferase_assay = "OBI:2100068"
    """
    An analyte assay that measures the abundance of alanine aminotransferase in venous blood as part of a liver injury order
    """
    liver_injury_venous_blood_human_alkaline_phosphatase_assay = "OBI:2100069"
    """
    An analyte assay that measures the abundance of human alkaline phosphatase in venous blood as part of a liver injury order
    """
    liver_injury_venous_blood_bilirubin_assay = "OBI:2100070"
    """
    An analyte assay that measures the abundance of bilirubin in venous blood as part of a liver injury order
    """
    liver_injury_venous_blood_human_aspartate_aminotransferase_assay = "OBI:2100071"
    """
    An analyte assay that measures the abundance of human aspartate aminotransferase in venous blood as part of a liver injury order
    """
    venous_blood_glucose_assay = "OBI:2100072"
    """
    An analyte assay that measures the abundance of glucose in venous blood
    """
    venous_blood_magnesium_assay = "OBI:2100073"
    """
    An analyte assay that measures the abundance of magnesium in venous blood
    """
    CBC_venous_blood_RBC_count_assay = "OBI:2100074"
    """
    A cytometry assay that measures the count of RBCs in venous blood as part of a CBC order
    """
    CBC_venous_blood_WBC_count_assay = "OBI:2100075"
    """
    A cytometry assay that measures the count of WBCs in venous blood as part of a CBC order
    """
    CBC_venous_blood_hematocrit_assay = "OBI:2100076"
    """
    A cytometry assay that measures the proportion of red blood cells in venous blood as part of a CBC order
    """
    CBC_venous_blood_platelet_count_assay = "OBI:2100077"
    """
    A cytometry assay that measures the count of platelets in venous blood as part of a CBC order
    """
    CBC_venous_blood_hemoglobin_assay = "OBI:2100078"
    """
    An analyte assay that measures the abundance of hemoglobin in venous blood as part of a CBC order
    """
    corrected_venous_blood_leukocyte_count_assay = "OBI:2100079"
    """
    A cytometry assay that measures the count of leukocytes in venous blood as part of a corrected order
    """
    liver_evaluation_venous_blood_bilirubin_assay = "OBI:2100080"
    """
    An analyte assay that measures the abundance of bilirubin in venous blood as part of a liver evaluation order
    """
    liver_evaluation_venous_blood_globulin_assay = "OBI:2100081"
    """
    An analyte assay that measures the abundance of globulin in venous blood as part of a liver evaluation order
    """
    liver_evaluation_venous_blood_albumin_assay = "OBI:2100082"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a liver evaluation order
    """
    liver_evaluation_venous_blood_human_aspartate_aminotransferase_assay = "OBI:2100083"
    """
    An analyte assay that measures the abundance of human aspartate aminotransferase in venous blood as part of a liver evaluation order
    """
    liver_evaluation_venous_blood_alanine_aminotransferase_assay = "OBI:2100084"
    """
    An analyte assay that measures the abundance of alanine aminotransferase in venous blood as part of a liver evaluation order
    """
    liver_evaluation_venous_blood_human_alkaline_phosphatase_assay = "OBI:2100085"
    """
    An analyte assay that measures the abundance of human alkaline phosphatase in venous blood as part of a liver evaluation order
    """
    liver_evaluation_venous_blood_protein_assay = "OBI:2100086"
    """
    An analyte assay that measures the abundance of protein in venous blood as part of a liver evaluation order
    """
    basic_metabolic_panel_venous_blood_chloride_assay = "OBI:2100087"
    """
    An analyte assay that measures the abundance of chloride in venous blood as part of a basic metabolic panel order
    """
    basic_metabolic_panel_venous_blood_potassium_assay = "OBI:2100088"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a basic metabolic panel order
    """
    basic_metabolic_panel_venous_blood_sodium_assay = "OBI:2100089"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a basic metabolic panel order
    """
    basic_metabolic_panel_venous_blood_creatinine_assay = "OBI:2100090"
    """
    An analyte assay that measures the abundance of creatinine in venous blood as part of a basic metabolic panel order
    """
    basic_metabolic_panel_venous_blood_glucose_assay = "OBI:2100091"
    """
    An analyte assay that measures the abundance of glucose in venous blood as part of a basic metabolic panel order
    """
    basic_metabolic_panel_venous_blood_calcium_assay = "OBI:2100092"
    """
    An analyte assay that measures the abundance of calcium in venous blood as part of a basic metabolic panel order
    """
    basic_metabolic_panel_venous_blood_carbon_dioxide_assay = "OBI:2100093"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a basic metabolic panel order
    """
    venous_blood_creatine_kinase_assay = "OBI:2100094"
    """
    An analyte assay that measures the abundance of creatine kinase in venous blood
    """
    venous_blood_calcium_assay = "OBI:2100095"
    """
    An analyte assay that measures the abundance of calcium in venous blood
    """
    venous_blood_ferritin_assay = "OBI:2100096"
    """
    An assay that measures ferritin in venous blood
    """
    total_venous_blood_calcium_assay = "OBI:2100097"
    """
    An analyte assay that measures the abundance of calcium in venous blood as part of a total order
    """
    venous_blood_iron_assay = "OBI:2100098"
    """
    An analyte assay that measures the abundance of iron in venous blood
    """
    CBC_with_manual_differential_venous_blood_band_neutrophil_count_assay = "OBI:2100099"
    """
    A cytometry assay that measures the count of band neutrophils in venous blood as part of a CBC with manual differential order
    """
    CBC_with_manual_differential_venous_blood_WBC_count_assay = "OBI:2100100"
    """
    A cytometry assay that measures the count of WBCs in venous blood as part of a CBC with manual differential order
    """
    CBC_with_manual_differential_venous_blood_eosinophil_count_assay = "OBI:2100101"
    """
    A cytometry assay that measures the count of eosinophils in venous blood as part of a CBC with manual differential order
    """
    CBC_with_manual_differential_venous_blood_lymphocyte_count_assay = "OBI:2100102"
    """
    A cytometry assay that measures the count of lymphocytes in venous blood as part of a CBC with manual differential order
    """
    CBC_with_manual_differential_venous_blood_nucleated_RBC_count_assay = "OBI:2100103"
    """
    A cytometry assay that measures the count of nucleated RBCs in venous blood as part of a CBC with manual differential order
    """
    CBC_with_manual_differential_venous_blood_monocyte_count_assay = "OBI:2100104"
    """
    A cytometry assay that measures the count of monocytes in venous blood as part of a CBC with manual differential order
    """
    CBC_with_manual_differential_venous_blood_segmented_neutrophil_count_assay = "OBI:2100105"
    """
    A cytometry assay that measures the count of segmented neutrophils in venous blood as part of a CBC with manual differential order
    """
    CBC_with_manual_differential_venous_blood_basophil_count_assay = "OBI:2100106"
    """
    A cytometry assay that measures the count of basophils in venous blood as part of a CBC with manual differential order
    """
    venous_blood_albumin_assay = "OBI:2100107"
    """
    An analyte assay that measures the abundance of albumin in venous blood
    """
    cardiac_enzymes_venous_blood_creatine_kinase_assay = "OBI:2100108"
    """
    An analyte assay that measures the abundance of creatine kinase in venous blood as part of a cardiac enzymes order
    """
    venous_blood_haptoglobin_assay = "OBI:2100109"
    """
    An analyte assay that measures the abundance of haptoglobin in venous blood
    """
    venous_blood_lactate_dehydrogenase_assay = "OBI:2100110"
    """
    An assay that measures lactate dehydrogenase in venous blood
    """
    venous_blood_prealbunin_assay = "OBI:2100111"
    """
    An analyte assay that measures the abundance of prealbunin in venous blood
    """
    lipid_panel_venous_blood_triglyceride_assay = "OBI:2100112"
    """
    An analyte assay that measures the abundance of triglyceride in venous blood as part of a lipid panel order
    """
    lipid_panel_venous_blood_high_density_lipoprotein_assay = "OBI:2100113"
    """
    An analyte assay that measures the abundance of high density lipoprotein in venous blood as part of a lipid panel order
    """
    lipid_panel_venous_blood_cholesterol_assay = "OBI:2100114"
    """
    An analyte assay that measures the abundance of cholesterol in venous blood as part of a lipid panel order
    """
    lipid_panel_venous_blood_low_density_lipoprotein_assay = "OBI:2100115"
    """
    An analyte assay that measures the abundance of low density lipoprotein in venous blood as part of a lipid panel order
    """
    venous_blood_hemoglobin_A1c_assay = "OBI:2100116"
    """
    An assay that measures hemoglobin A1c in venous blood
    """
    venous_blood_uric_acid_assay = "OBI:2100117"
    """
    An analyte assay that measures the abundance of uric acid in venous blood
    """
    total_venous_blood_protein_assay = "OBI:2100118"
    """
    An analyte assay that measures the abundance of protein in venous blood as part of a total order
    """
    venous_blood_thyroid_stimulating_hormone_assay = "OBI:2100119"
    """
    An analyte assay that measures the abundance of thyroid stimulating hormone in venous blood
    """
    venous_blood_prostate_specific_antigen_assay = "OBI:2100120"
    """
    An analyte assay that measures the abundance of prostate specific antigen in venous blood
    """
    number_24_hour_total_urine_volume_assay = "OBI:2100121"
    """
    An assay that measures volume in urine as part of a 24 hour total order
    """
    T4_uptake_venous_blood_T4_assay = "OBI:2100122"
    """
    An analyte assay that measures the abundance of T4 in venous blood as part of a T4 uptake order
    """
    arterial_blood_glucose_assay = "OBI:2100123"
    """
    An analyte assay that measures the abundance of glucose in arterial blood
    """
    CBC_with_manual_differential_venous_blood_cell_count_assay = "OBI:2100124"
    """
    A cytometry assay that measures the count of cells in venous blood as part of a CBC with manual differential order
    """
    hemoglobin_oxygen_saturation_arterial_blood_oxygen_assay = "OBI:2100125"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a hemoglobin oxygen saturation order
    """
    hemoglobin_oxygen_saturation_arterial_blood_hemoglobin_assay = "OBI:2100126"
    """
    An analyte assay that measures the abundance of hemoglobin in arterial blood as part of a hemoglobin oxygen saturation order
    """
    inpatient_profile_venous_blood_sodium_assay = "OBI:2100127"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a inpatient profile order
    """
    inpatient_profile_venous_blood_creatinine_assay = "OBI:2100128"
    """
    An analyte assay that measures the abundance of creatinine in venous blood as part of a inpatient profile order
    """
    inpatient_profile_venous_blood_potassium_assay = "OBI:2100129"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a inpatient profile order
    """
    inpatient_profile_venous_blood_carbon_dioxide_assay = "OBI:2100130"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a inpatient profile order
    """
    venous_blood_folic_acid_assay = "OBI:2100131"
    """
    An analyte assay that measures the abundance of folic acid in venous blood
    """
    count_venous_blood_reticulocyte_count_assay = "OBI:2100132"
    """
    A cytometry assay that measures the count of reticulocytes in venous blood as part of a count order
    """
    venous_blood_potassium_assay = "OBI:2100133"
    """
    An analyte assay that measures the abundance of potassium in venous blood
    """
    venous_blood_carbon_dioxide_assay = "OBI:2100134"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood
    """
    venous_blood_transferrin_assay = "OBI:2100135"
    """
    An analyte assay that measures the abundance of transferrin in venous blood
    """
    venous_blood_sodium_assay = "OBI:2100136"
    """
    An analyte assay that measures the abundance of sodium in venous blood
    """
    random_electrolytes_urine_sodium_assay = "OBI:2100137"
    """
    An analyte assay that measures the abundance of sodium in urine as part of a random electrolytes order
    """
    random_electrolytes_urine_potassium_assay = "OBI:2100138"
    """
    An analyte assay that measures the abundance of potassium in urine as part of a random electrolytes order
    """
    urine_creatinine_assay = "OBI:2100139"
    """
    An analyte assay that measures the abundance of creatinine in urine
    """
    urine_osmolality_assay = "OBI:2100140"
    """
    An assay that measures osmolality in urine
    """
    cooximitery_arterial_blood_oxygen_assay = "OBI:2100141"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a cooximitery order
    """
    cooximitery_arterial_blood_hemoglobin_assay = "OBI:2100142"
    """
    An analyte assay that measures the abundance of hemoglobin in arterial blood as part of a cooximitery order
    """
    cooximitery_arterial_blood_methemoglobin_assay = "OBI:2100143"
    """
    An analyte assay that measures the abundance of methemoglobin in arterial blood as part of a cooximitery order
    """
    electrolytes_urine_sodium_assay = "OBI:2100144"
    """
    An analyte assay that measures the abundance of sodium in urine as part of a electrolytes order
    """
    electrolytes_urine_potassium_assay = "OBI:2100145"
    """
    An analyte assay that measures the abundance of potassium in urine as part of a electrolytes order
    """
    Biosite_cardiac_panel_arterial_blood_creatine_kinase_MB_assay = "OBI:2100146"
    """
    An assay that measures creatine kinase MB in arterial blood as part of a Biosite cardiac panel order
    """
    venous_blood_fibrinogen_assay = "OBI:2100147"
    """
    An assay that measures fibrinogen in venous blood
    """
    comprehensive_metabolic_panel_venous_blood_carbon_dioxide_assay = "OBI:2100148"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_calcium_assay = "OBI:2100149"
    """
    An analyte assay that measures the abundance of calcium in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_potassium_assay = "OBI:2100150"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_sodium_assay = "OBI:2100151"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_glucose_assay = "OBI:2100152"
    """
    An analyte assay that measures the abundance of glucose in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_albumin_assay = "OBI:2100153"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_human_alkaline_phosphatase_assay = "OBI:2100154"
    """
    An analyte assay that measures the abundance of human alkaline phosphatase in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_bilirubin_assay = "OBI:2100155"
    """
    An analyte assay that measures the abundance of bilirubin in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_chloride_assay = "OBI:2100156"
    """
    An analyte assay that measures the abundance of chloride in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_human_aspartate_aminotransferase_assay = "OBI:2100157"
    """
    An analyte assay that measures the abundance of human aspartate aminotransferase in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_protein_assay = "OBI:2100158"
    """
    An analyte assay that measures the abundance of protein in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_creatinine_assay = "OBI:2100159"
    """
    An analyte assay that measures the abundance of creatinine in venous blood as part of a comprehensive metabolic panel order
    """
    comprehensive_metabolic_panel_venous_blood_alanine_aminotransferase_assay = "OBI:2100160"
    """
    An analyte assay that measures the abundance of alanine aminotransferase in venous blood as part of a comprehensive metabolic panel order
    """
    venous_blood_LDH_assay = "OBI:2100161"
    """
    An assay that measures LDH in venous blood
    """
    venous_blood_creatine_kinase_MB_assay = "OBI:2100162"
    """
    An assay that measures creatine kinase MB in venous blood
    """
    venous_blood_lactic_acid_assay = "OBI:2100163"
    """
    An assay that measures lactic acid in venous blood
    """
    venous_blood_hematocrit_assay = "OBI:2100164"
    """
    A cytometry assay that measures the proportion of red blood cells in venous blood
    """
    venous_blood_creatinine_assay = "OBI:2100165"
    """
    An analyte assay that measures the abundance of creatinine in venous blood
    """
    blood_gas_venous_blood_oxygen_assay = "OBI:2100166"
    """
    An analyte assay that measures the abundance of oxygen in venous blood as part of a blood gas order
    """
    ionized_venous_blood_ionized_calcium_assay = "OBI:2100167"
    """
    An analyte assay that measures the abundance of ionized calcium in venous blood as part of a ionized order
    """
    blood_gas_venous_blood_carbon_dioxide_assay = "OBI:2100168"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a blood gas order
    """
    blood_gas_venous_blood_bicarbonate_assay = "OBI:2100169"
    """
    An analyte assay that measures the abundance of bicarbonate in venous blood as part of a blood gas order
    """
    arterial_blood_creatinine_assay = "OBI:2100170"
    """
    An analyte assay that measures the abundance of creatinine in arterial blood
    """
    venous_blood_tacrolimus_assay = "OBI:2100171"
    """
    An analyte assay that measures the abundance of tacrolimus in venous blood
    """
    random_venous_blood_vancomycin_assay = "OBI:2100172"
    """
    An analyte assay that measures the abundance of vancomycin in venous blood as part of a random order
    """
    venous_blood_mycophenolic_acid_assay = "OBI:2100173"
    """
    An analyte assay that measures the abundance of mycophenolic acid in venous blood
    """
    non_vented_blood_gas_arterial_blood_carbon_dioxide_assay = "OBI:2100174"
    """
    An analyte assay that measures the abundance of carbon dioxide in arterial blood as part of a non-vented blood gas order
    """
    non_vented_blood_gas_arterial_blood_oxygen_assay = "OBI:2100175"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a non-vented blood gas order
    """
    non_vented_blood_gas_arterial_blood_bicarbonate_assay = "OBI:2100176"
    """
    An analyte assay that measures the abundance of bicarbonate in arterial blood as part of a non-vented blood gas order
    """
    quantitative_venous_blood_IgG_assay = "OBI:2100177"
    """
    An assay that measures IgG in venous blood as part of a quantitative order
    """
    quantitative_venous_blood_IgM_assay = "OBI:2100178"
    """
    An assay that measures IgM in venous blood as part of a quantitative order
    """
    quantitative_venous_blood_IgA_assay = "OBI:2100179"
    """
    An assay that measures IgA in venous blood as part of a quantitative order
    """
    arterial_blood_sodium_assay = "OBI:2100180"
    """
    An analyte assay that measures the abundance of sodium in arterial blood
    """
    arterial_blood_potassium_assay = "OBI:2100181"
    """
    An analyte assay that measures the abundance of potassium in arterial blood
    """
    ionized_arterial_blood_calcium_assay = "OBI:2100182"
    """
    An analyte assay that measures the abundance of calcium in arterial blood as part of a ionized order
    """
    vented_blood_gas_arterial_blood_bicarbonate_assay = "OBI:2100183"
    """
    An analyte assay that measures the abundance of bicarbonate in arterial blood as part of a vented blood gas order
    """
    vented_blood_gas_arterial_blood_oxygen_assay = "OBI:2100184"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a vented blood gas order
    """
    vented_blood_gas_arterial_blood_carbon_dioxide_assay = "OBI:2100185"
    """
    An analyte assay that measures the abundance of carbon dioxide in arterial blood as part of a vented blood gas order
    """
    arterial_blood_hematocrit_assay = "OBI:2100186"
    """
    A cytometry assay that measures the proportion of red blood cells in arterial blood
    """
    arterial_blood_chloride_assay = "OBI:2100187"
    """
    An analyte assay that measures the abundance of chloride in arterial blood
    """
    arterial_blood_hemoglobin_assay = "OBI:2100188"
    """
    An analyte assay that measures the abundance of hemoglobin in arterial blood
    """
    GEM_premier_blood_gas_venous_blood_hematocrit_assay = "OBI:2100189"
    """
    A cytometry assay that measures the proportion of red blood cells in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_ionized_calcium_assay = "OBI:2100190"
    """
    An analyte assay that measures the abundance of ionized calcium in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_potassium_assay = "OBI:2100191"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_oxygen_assay = "OBI:2100192"
    """
    An analyte assay that measures the abundance of oxygen in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_hemoglobin_assay = "OBI:2100193"
    """
    An analyte assay that measures the abundance of hemoglobin in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_bicarbonate_assay = "OBI:2100194"
    """
    An analyte assay that measures the abundance of bicarbonate in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_glucose_assay = "OBI:2100195"
    """
    An analyte assay that measures the abundance of glucose in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_sodium_assay = "OBI:2100196"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_lactic_acid_assay = "OBI:2100197"
    """
    An assay that measures lactic acid in venous blood as part of a GEM premier blood gas order
    """
    GEM_premier_blood_gas_venous_blood_carbon_dioxide_assay = "OBI:2100198"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a GEM premier blood gas order
    """
    trough_venous_blood_tobramycin_assay = "OBI:2100199"
    """
    An analyte assay that measures the abundance of tobramycin in venous blood as part of a trough order
    """
    random_venous_blood_tobramycin_assay = "OBI:2100200"
    """
    An analyte assay that measures the abundance of tobramycin in venous blood as part of a random order
    """
    CBC_with_manual_differential_venous_blood_metamyelocyte_count_assay = "OBI:2100201"
    """
    A cytometry assay that measures the count of metamyelocytes in venous blood as part of a CBC with manual differential order
    """
    arterial_blood_lactic_acid_assay = "OBI:2100202"
    """
    An assay that measures lactic acid in arterial blood
    """
    venous_blood_25_hydroxyvitamin_D2_assay = "OBI:2100203"
    """
    An analyte assay that measures the abundance of 25-hydroxyvitamin D2 in venous blood
    """
    venous_blood_digoxin_assay = "OBI:2100204"
    """
    An analyte assay that measures the abundance of digoxin in venous blood
    """
    urine_protein_assay = "OBI:2100205"
    """
    An analyte assay that measures the abundance of protein in urine
    """
    venous_blood_tobramycin_assay = "OBI:2100206"
    """
    An analyte assay that measures the abundance of tobramycin in venous blood
    """
    CBC_with_manual_differential_venous_blood_myelocyte_count_assay = "OBI:2100207"
    """
    A cytometry assay that measures the count of myelocytes in venous blood as part of a CBC with manual differential order
    """
    SPEP_protein_electrophoresis_venous_blood_beta_globin_assay = "OBI:2100208"
    """
    An analyte assay that measures the abundance of beta-globin in venous blood as part of a SPEP protein electrophoresis order
    """
    SPEP_protein_electrophoresis_venous_blood_albumin_assay = "OBI:2100209"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a SPEP protein electrophoresis order
    """
    SPEP_protein_electrophoresis_venous_blood_protein_assay = "OBI:2100210"
    """
    An analyte assay that measures the abundance of protein in venous blood as part of a SPEP protein electrophoresis order
    """
    trough_venous_blood_vancomycin_assay = "OBI:2100211"
    """
    An analyte assay that measures the abundance of vancomycin in venous blood as part of a trough order
    """
    hepatic_panel_venous_blood_protein_assay = "OBI:2100212"
    """
    An analyte assay that measures the abundance of protein in venous blood as part of a hepatic panel order
    """
    hepatic_panel_venous_blood_bilirubin_assay = "OBI:2100213"
    """
    An analyte assay that measures the abundance of bilirubin in venous blood as part of a hepatic panel order
    """
    hepatic_panel_venous_blood_alanine_aminotransferase_assay = "OBI:2100214"
    """
    An analyte assay that measures the abundance of alanine aminotransferase in venous blood as part of a hepatic panel order
    """
    hepatic_panel_venous_blood_human_aspartate_aminotransferase_assay = "OBI:2100215"
    """
    An analyte assay that measures the abundance of human aspartate aminotransferase in venous blood as part of a hepatic panel order
    """
    hepatic_panel_venous_blood_albumin_assay = "OBI:2100216"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a hepatic panel order
    """
    hepatic_panel_venous_blood_human_alkaline_phosphatase_assay = "OBI:2100217"
    """
    An analyte assay that measures the abundance of human alkaline phosphatase in venous blood as part of a hepatic panel order
    """
    estimated_venous_blood_glomerular_filtration_assay = "OBI:2100218"
    """
    An assay that measures glomerular filtration in venous blood as part of a estimated order
    """
    DT60_venous_blood_creatinine_assay = "OBI:2100219"
    """
    An analyte assay that measures the abundance of creatinine in venous blood as part of a DT60 order
    """
    fasting_venous_blood_glucose_assay = "OBI:2100220"
    """
    An analyte assay that measures the abundance of glucose in venous blood as part of a fasting order
    """
    random_venous_blood_amikacin_assay = "OBI:2100221"
    """
    An analyte assay that measures the abundance of amikacin in venous blood as part of a random order
    """
    venous_blood_ammonia_assay = "OBI:2100222"
    """
    An analyte assay that measures the abundance of ammonia in venous blood
    """
    venous_blood_GGT_assay = "OBI:2100223"
    """
    An analyte assay that measures the abundance of GGT in venous blood
    """
    chem11_venous_blood_phosphate_assay = "OBI:2100224"
    """
    An analyte assay that measures the abundance of phosphate in venous blood as part of a chem11 order
    """
    chem11_venous_blood_potassium_assay = "OBI:2100225"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a chem11 order
    """
    chem11_venous_blood_calcium_assay = "OBI:2100226"
    """
    An analyte assay that measures the abundance of calcium in venous blood as part of a chem11 order
    """
    chem11_venous_blood_glucose_assay = "OBI:2100227"
    """
    An analyte assay that measures the abundance of glucose in venous blood as part of a chem11 order
    """
    chem11_venous_blood_carbon_dioxide_assay = "OBI:2100228"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a chem11 order
    """
    chem11_venous_blood_albumin_assay = "OBI:2100229"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a chem11 order
    """
    chem11_venous_blood_sodium_assay = "OBI:2100230"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a chem11 order
    """
    chem11_venous_blood_magnesium_assay = "OBI:2100231"
    """
    An analyte assay that measures the abundance of magnesium in venous blood as part of a chem11 order
    """
    chem11_venous_blood_creatinine_assay = "OBI:2100232"
    """
    An analyte assay that measures the abundance of creatinine in venous blood as part of a chem11 order
    """
    chem11_venous_blood_chloride_assay = "OBI:2100233"
    """
    An analyte assay that measures the abundance of chloride in venous blood as part of a chem11 order
    """
    total_venous_blood_IgE_assay = "OBI:2100234"
    """
    An assay that measures IgE in venous blood as part of a total order
    """
    chem16_venous_blood_human_aspartate_aminotransferase_assay = "OBI:2100235"
    """
    An analyte assay that measures the abundance of human aspartate aminotransferase in venous blood as part of a chem16 order
    """
    chem16_venous_blood_creatinine_assay = "OBI:2100236"
    """
    An analyte assay that measures the abundance of creatinine in venous blood as part of a chem16 order
    """
    chem16_venous_blood_magnesium_assay = "OBI:2100237"
    """
    An analyte assay that measures the abundance of magnesium in venous blood as part of a chem16 order
    """
    chem16_venous_blood_carbon_dioxide_assay = "OBI:2100238"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a chem16 order
    """
    chem16_venous_blood_glucose_assay = "OBI:2100239"
    """
    An analyte assay that measures the abundance of glucose in venous blood as part of a chem16 order
    """
    chem16_venous_blood_calcium_assay = "OBI:2100240"
    """
    An analyte assay that measures the abundance of calcium in venous blood as part of a chem16 order
    """
    chem16_venous_blood_triglyceride_assay = "OBI:2100241"
    """
    An analyte assay that measures the abundance of triglyceride in venous blood as part of a chem16 order
    """
    chem16_venous_blood_sodium_assay = "OBI:2100242"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a chem16 order
    """
    chem16_venous_blood_phosphate_assay = "OBI:2100243"
    """
    An analyte assay that measures the abundance of phosphate in venous blood as part of a chem16 order
    """
    chem16_venous_blood_human_alkaline_phosphatase_assay = "OBI:2100244"
    """
    An analyte assay that measures the abundance of human alkaline phosphatase in venous blood as part of a chem16 order
    """
    chem16_venous_blood_albumin_assay = "OBI:2100245"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a chem16 order
    """
    chem16_venous_blood_bilirubin_assay = "OBI:2100246"
    """
    An analyte assay that measures the abundance of bilirubin in venous blood as part of a chem16 order
    """
    chem16_venous_blood_chloride_assay = "OBI:2100247"
    """
    An analyte assay that measures the abundance of chloride in venous blood as part of a chem16 order
    """
    chem16_venous_blood_alanine_aminotransferase_assay = "OBI:2100248"
    """
    An analyte assay that measures the abundance of alanine aminotransferase in venous blood as part of a chem16 order
    """
    chem16_venous_blood_potassium_assay = "OBI:2100249"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a chem16 order
    """
    POC_chem8_arterial_blood_glucose_assay = "OBI:2100250"
    """
    An analyte assay that measures the abundance of glucose in arterial blood as part of a POC chem8 order
    """
    POC_chem8_arterial_blood_ionized_calcium_assay = "OBI:2100251"
    """
    An analyte assay that measures the abundance of ionized calcium in arterial blood as part of a POC chem8 order
    """
    POC_chem8_arterial_blood_potassium_assay = "OBI:2100252"
    """
    An analyte assay that measures the abundance of potassium in arterial blood as part of a POC chem8 order
    """
    POC_chem8_arterial_blood_sodium_assay = "OBI:2100253"
    """
    An analyte assay that measures the abundance of sodium in arterial blood as part of a POC chem8 order
    """
    POC_chem8_arterial_blood_creatinine_assay = "OBI:2100254"
    """
    An analyte assay that measures the abundance of creatinine in arterial blood as part of a POC chem8 order
    """
    POC_chem8_arterial_blood_hematocrit_assay = "OBI:2100255"
    """
    A cytometry assay that measures the proportion of red blood cells in arterial blood as part of a POC chem8 order
    """
    POC_chem8_arterial_blood_chloride_assay = "OBI:2100256"
    """
    An analyte assay that measures the abundance of chloride in arterial blood as part of a POC chem8 order
    """
    peak_venous_blood_tobramycin_assay = "OBI:2100257"
    """
    An analyte assay that measures the abundance of tobramycin in venous blood as part of a peak order
    """
    number_24_hour_urine_creatinine_assay = "OBI:2100258"
    """
    An analyte assay that measures the abundance of creatinine in urine as part of a 24 hour order
    """
    intact_venous_blood_PTH_assay = "OBI:2100259"
    """
    An analyte assay that measures the abundance of PTH in venous blood as part of a intact order
    """
    total_venous_blood_PSA_assay = "OBI:2100260"
    """
    An analyte assay that measures the abundance of PSA in venous blood as part of a total order
    """
    total_venous_blood_T3_assay = "OBI:2100261"
    """
    An analyte assay that measures the abundance of T3 in venous blood as part of a total order
    """
    number_24_hour_urine_protein_assay = "OBI:2100262"
    """
    An analyte assay that measures the abundance of protein in urine as part of a 24 hour order
    """
    total_venous_blood_cholesterol_assay = "OBI:2100263"
    """
    An analyte assay that measures the abundance of cholesterol in venous blood as part of a total order
    """
    venous_blood_triglyceride_assay = "OBI:2100264"
    """
    An analyte assay that measures the abundance of triglyceride in venous blood
    """
    tube_4_count_cerebrospinal_fluid_cell_count_assay = "OBI:2100265"
    """
    A cytometry assay that measures the count of cells in cerebrospinal fluid as part of a tube 4 count order
    """
    cerebrospinal_fluid_protein_assay = "OBI:2100266"
    """
    An analyte assay that measures the abundance of protein in cerebrospinal fluid
    """
    cerebrospinal_fluid_glucose_assay = "OBI:2100267"
    """
    An analyte assay that measures the abundance of glucose in cerebrospinal fluid
    """
    tube_1_count_cerebrospinal_fluid_cell_count_assay = "OBI:2100268"
    """
    A cytometry assay that measures the count of cells in cerebrospinal fluid as part of a tube 1 count order
    """
    venous_blood_dehydroepiandrosterone_assay = "OBI:2100269"
    """
    An analyte assay that measures the abundance of dehydroepiandrosterone in venous blood
    """
    venous_blood_cortisol_assay = "OBI:2100270"
    """
    An analyte assay that measures the abundance of cortisol in venous blood
    """
    ABL90_panel_arterial_blood_sodium_assay = "OBI:2100271"
    """
    An analyte assay that measures the abundance of sodium in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_oxygen_assay = "OBI:2100272"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_glucose_assay = "OBI:2100273"
    """
    An analyte assay that measures the abundance of glucose in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_lactic_acid_assay = "OBI:2100274"
    """
    An assay that measures lactic acid in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_hemoglobin_assay = "OBI:2100275"
    """
    An analyte assay that measures the abundance of hemoglobin in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_chloride_assay = "OBI:2100276"
    """
    An analyte assay that measures the abundance of chloride in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_carbon_dioxide_assay = "OBI:2100277"
    """
    An analyte assay that measures the abundance of carbon dioxide in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_hematocrit_assay = "OBI:2100278"
    """
    A cytometry assay that measures the proportion of red blood cells in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_calcium_assay = "OBI:2100279"
    """
    An analyte assay that measures the abundance of calcium in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_temperature_assay = "OBI:2100280"
    """
    An assay that measures temperature in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_bicarbonate_assay = "OBI:2100281"
    """
    An analyte assay that measures the abundance of bicarbonate in arterial blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_potassium_assay = "OBI:2100282"
    """
    An analyte assay that measures the abundance of potassium in arterial blood as part of a ABL90 panel order
    """
    CBC_with_manual_differential_venous_blood_promyelocyte_count_assay = "OBI:2100283"
    """
    A cytometry assay that measures the count of promyelocytes in venous blood as part of a CBC with manual differential order
    """
    ABL90_panel_venous_blood_glucose_assay = "OBI:2100284"
    """
    An analyte assay that measures the abundance of glucose in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_hemoglobin_assay = "OBI:2100285"
    """
    An analyte assay that measures the abundance of hemoglobin in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_ionized_calcium_assay = "OBI:2100286"
    """
    An analyte assay that measures the abundance of ionized calcium in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_carbon_dioxide_assay = "OBI:2100287"
    """
    An analyte assay that measures the abundance of carbon dioxide in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_hematocrit_assay = "OBI:2100288"
    """
    A cytometry assay that measures the proportion of red blood cells in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_sodium_assay = "OBI:2100289"
    """
    An analyte assay that measures the abundance of sodium in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_oxygen_assay = "OBI:2100290"
    """
    An analyte assay that measures the abundance of oxygen in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_bicarbonate_assay = "OBI:2100291"
    """
    An analyte assay that measures the abundance of bicarbonate in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_lactic_acid_assay = "OBI:2100292"
    """
    An assay that measures lactic acid in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_venous_blood_chloride_assay = "OBI:2100293"
    """
    An analyte assay that measures the abundance of chloride in venous blood as part of a ABL90 panel order
    """
    venous_blood_T4_assay = "OBI:2100294"
    """
    An analyte assay that measures the abundance of T4 in venous blood
    """
    free_venous_blood_T4_assay = "OBI:2100295"
    """
    An analyte assay that measures the abundance of T4 in venous blood as part of a free order
    """
    ABL90_panel_venous_blood_potassium_assay = "OBI:2100296"
    """
    An analyte assay that measures the abundance of potassium in venous blood as part of a ABL90 panel order
    """
    urine_sodium_assay = "OBI:2100297"
    """
    An analyte assay that measures the abundance of sodium in urine
    """
    bone_profile_venous_blood_albumin_assay = "OBI:2100298"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a bone profile order
    """
    bone_profile_venous_blood_calcium_assay = "OBI:2100299"
    """
    An analyte assay that measures the abundance of calcium in venous blood as part of a bone profile order
    """
    bone_profile_venous_blood_human_alkaline_phosphatase_assay = "OBI:2100300"
    """
    An analyte assay that measures the abundance of human alkaline phosphatase in venous blood as part of a bone profile order
    """
    bone_profile_venous_blood_protein_assay = "OBI:2100301"
    """
    An analyte assay that measures the abundance of protein in venous blood as part of a bone profile order
    """
    bone_profile_venous_blood_phosphate_assay = "OBI:2100302"
    """
    An analyte assay that measures the abundance of phosphate in venous blood as part of a bone profile order
    """
    ABGSOLIDUSelectrolytes_arterial_blood_carbon_dioxide_assay = "OBI:2100303"
    """
    An analyte assay that measures the abundance of carbon dioxide in arterial blood as part of a ABG/electrolytes order
    """
    ABGSOLIDUSelectrolytes_arterial_blood_oxygen_assay = "OBI:2100304"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a ABG/electrolytes order
    """
    ABGSOLIDUSelectrolytes_arterial_blood_ionized_calcium_assay = "OBI:2100305"
    """
    An analyte assay that measures the abundance of ionized calcium in arterial blood as part of a ABG/electrolytes order
    """
    CBC_with_automated_differential_venous_blood_nucleated_RBC_count_assay = "OBI:2100306"
    """
    A cytometry assay that measures the count of nucleated RBCs in venous blood as part of a CBC with automated differential order
    """
    ABL90_panel_venous_blood_methemoglobin_assay = "OBI:2100307"
    """
    An analyte assay that measures the abundance of methemoglobin in venous blood as part of a ABL90 panel order
    """
    ABL90_panel_arterial_blood_methemoglobin_assay = "OBI:2100308"
    """
    An analyte assay that measures the abundance of methemoglobin in arterial blood as part of a ABL90 panel order
    """
    venous_blood_valproic_acid_assay = "OBI:2100309"
    """
    An analyte assay that measures the abundance of valproic acid in venous blood
    """
    high_sensitivity_cardiacSOLIDUSneonatal_venous_blood_c_reactive_protein_assay = "OBI:2100310"
    """
    An analyte assay that measures the abundance of c-reactive protein in venous blood as part of a high sensitivity cardiac/neonatal order
    """
    POC_arterial_blood_creatinine_assay = "OBI:2100311"
    """
    An analyte assay that measures the abundance of creatinine in arterial blood as part of a POC order
    """
    GEM4000_ANLCOOX_arterial_blood_bicarbonate_assay = "OBI:2100312"
    """
    An analyte assay that measures the abundance of bicarbonate in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_oxygen_assay = "OBI:2100313"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_hematocrit_assay = "OBI:2100314"
    """
    A cytometry assay that measures the proportion of red blood cells in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_temperature_assay = "OBI:2100315"
    """
    An assay that measures temperature in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_hemoglobin_assay = "OBI:2100316"
    """
    An analyte assay that measures the abundance of hemoglobin in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_potassium_assay = "OBI:2100317"
    """
    An analyte assay that measures the abundance of potassium in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_glucose_assay = "OBI:2100318"
    """
    An analyte assay that measures the abundance of glucose in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_ionized_calcium_assay = "OBI:2100319"
    """
    An analyte assay that measures the abundance of ionized calcium in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_carbon_dioxide_assay = "OBI:2100320"
    """
    An analyte assay that measures the abundance of carbon dioxide in arterial blood as part of a GEM4000 ANLCOOX order
    """
    GEM4000_ANLCOOX_arterial_blood_sodium_assay = "OBI:2100321"
    """
    An analyte assay that measures the abundance of sodium in arterial blood as part of a GEM4000 ANLCOOX order
    """
    ionized_venous_blood_calcium_assay = "OBI:2100322"
    """
    An analyte assay that measures the abundance of calcium in venous blood as part of a ionized order
    """
    venous_blood_hemoglobin_assay = "OBI:2100323"
    """
    An analyte assay that measures the abundance of hemoglobin in venous blood
    """
    CBC_with_manual_differential_venous_blood_megakaryocyte_count_assay = "OBI:2100324"
    """
    A cytometry assay that measures the count of megakaryocytes in venous blood as part of a CBC with manual differential order
    """
    non_cardiac_venous_blood_c_reactive_protein_assay = "OBI:2100325"
    """
    An analyte assay that measures the abundance of c-reactive protein in venous blood as part of a non-cardiac order
    """
    intraoperative_venous_blood_PTH_assay = "OBI:2100326"
    """
    An analyte assay that measures the abundance of PTH in venous blood as part of a intraoperative order
    """
    venous_blood_parathyroid_hormone_assay = "OBI:2100327"
    """
    An analyte assay that measures the abundance of parathyroid hormone in venous blood
    """
    total_bodily_fluid_protein_assay = "OBI:2100328"
    """
    An analyte assay that measures the abundance of protein in bodily fluid as part of a total order
    """
    bodily_fluid_glucose_assay = "OBI:2100329"
    """
    An analyte assay that measures the abundance of glucose in bodily fluid
    """
    count_bodily_fluid_cell_count_assay = "OBI:2100330"
    """
    A cytometry assay that measures the count of cells in bodily fluid as part of a count order
    """
    manual_differential_bodily_fluid_segmented_neutrophil_count_assay = "OBI:2100331"
    """
    A cytometry assay that measures the count of segmented neutrophils in bodily fluid as part of a manual differential order
    """
    manual_differential_bodily_fluid_mesothelial_cell_count_assay = "OBI:2100332"
    """
    A cytometry assay that measures the count of mesothelial cells in bodily fluid as part of a manual differential order
    """
    manual_differential_bodily_fluid_monocyte_count_assay = "OBI:2100333"
    """
    A cytometry assay that measures the count of monocytes in bodily fluid as part of a manual differential order
    """
    manual_differential_bodily_fluid_lymphocyte_count_assay = "OBI:2100334"
    """
    A cytometry assay that measures the count of lymphocytes in bodily fluid as part of a manual differential order
    """
    manual_differential_bodily_fluid_macrophage_count_assay = "OBI:2100335"
    """
    A cytometry assay that measures the count of macrophages in bodily fluid as part of a manual differential order
    """
    manual_differential_bodily_fluid_basophil_count_assay = "OBI:2100336"
    """
    A cytometry assay that measures the count of basophils in bodily fluid as part of a manual differential order
    """
    manual_differential_bodily_fluid_eosinophil_count_assay = "OBI:2100337"
    """
    A cytometry assay that measures the count of eosinophils in bodily fluid as part of a manual differential order
    """
    liver_function_venous_blood_bilirubin_assay = "OBI:2100338"
    """
    An analyte assay that measures the abundance of bilirubin in venous blood as part of a liver function order
    """
    liver_function_venous_blood_alanine_aminotransferase_assay = "OBI:2100339"
    """
    An analyte assay that measures the abundance of alanine aminotransferase in venous blood as part of a liver function order
    """
    liver_function_venous_blood_human_aspartate_aminotransferase_assay = "OBI:2100340"
    """
    An analyte assay that measures the abundance of human aspartate aminotransferase in venous blood as part of a liver function order
    """
    liver_function_venous_blood_albumin_assay = "OBI:2100341"
    """
    An analyte assay that measures the abundance of albumin in venous blood as part of a liver function order
    """
    liver_function_venous_blood_protein_assay = "OBI:2100342"
    """
    An analyte assay that measures the abundance of protein in venous blood as part of a liver function order
    """
    liver_function_venous_blood_human_alkaline_phosphatase_assay = "OBI:2100343"
    """
    An analyte assay that measures the abundance of human alkaline phosphatase in venous blood as part of a liver function order
    """
    vitamin_B12_and_Folate_venous_blood_folic_acid_assay = "OBI:2100344"
    """
    An analyte assay that measures the abundance of folic acid in venous blood as part of a vitamin B12 and Folate order
    """
    bodily_fluid_cell_count_assay = "OBI:2100345"
    """
    A cytometry assay that measures the count of cells in bodily fluid
    """
    venous_blood_reticulocyte_count_assay = "OBI:2100346"
    """
    A cytometry assay that measures the count of reticulocytes in venous blood
    """
    bodily_fluid_cholesterol_assay = "OBI:2100347"
    """
    An analyte assay that measures the abundance of cholesterol in bodily fluid
    """
    TSH_reflex_Free_T4_venous_blood_thyroid_stimulating_hormone_assay = "OBI:2100348"
    """
    An analyte assay that measures the abundance of thyroid stimulating hormone in venous blood as part of a TSH reflex Free T4 order
    """
    direct_venous_blood_bilirubin_assay = "OBI:2100349"
    """
    An analyte assay that measures the abundance of bilirubin in venous blood as part of a direct order
    """
    free_venous_blood_T3_assay = "OBI:2100350"
    """
    An analyte assay that measures the abundance of T3 in venous blood as part of a free order
    """
    bodily_fluid_albumin_assay = "OBI:2100351"
    """
    An analyte assay that measures the abundance of albumin in bodily fluid
    """
    bodily_fluid_triglyceride_assay = "OBI:2100352"
    """
    An analyte assay that measures the abundance of triglyceride in bodily fluid
    """
    hemoglobin_and_hematocrit_venous_blood_hematocrit_assay = "OBI:2100353"
    """
    A cytometry assay that measures the proportion of red blood cells in venous blood as part of a hemoglobin and hematocrit order
    """
    hemoglobin_and_hematocrit_venous_blood_hemoglobin_assay = "OBI:2100354"
    """
    An analyte assay that measures the abundance of hemoglobin in venous blood as part of a hemoglobin and hematocrit order
    """
    venous_blood_ionized_calcium_assay = "OBI:2100355"
    """
    An analyte assay that measures the abundance of ionized calcium in venous blood
    """
    venous_blood_temperature_assay = "OBI:2100356"
    """
    An assay that measures temperature in venous blood
    """
    venous_blood_bicarbonate_assay = "OBI:2100357"
    """
    An analyte assay that measures the abundance of bicarbonate in venous blood
    """
    venous_blood_oxygen_assay = "OBI:2100358"
    """
    An analyte assay that measures the abundance of oxygen in venous blood
    """
    venous_blood_osmolality_assay = "OBI:2100359"
    """
    An assay that measures osmolality in venous blood
    """
    liver_fibrosis_LEFT_PARENTHESISchronic_viral_hepatitisRIGHT_PARENTHESIS_venous_blood_platelet_count_assay = "OBI:2100360"
    """
    A cytometry assay that measures the count of platelets in venous blood as part of a liver fibrosis (chronic viral hepatitis) order
    """
    venous_blood_T3_assay = "OBI:2100361"
    """
    An analyte assay that measures the abundance of T3 in venous blood
    """
    CBC_with_manual_differential_venous_blood_neutrophil_count_assay = "OBI:2100362"
    """
    A cytometry assay that measures the count of neutrophils in venous blood as part of a CBC with manual differential order
    """
    creatinine_clearance_urine_creatinine_assay = "OBI:2100363"
    """
    An analyte assay that measures the abundance of creatinine in urine as part of a creatinine clearance order
    """
    venous_blood_beta_hydroxybutryic_acid_assay = "OBI:2100364"
    """
    An analyte assay that measures the abundance of beta hydroxybutryic acid in venous blood
    """
    venous_blood_megakaryocyte_count_assay = "OBI:2100365"
    """
    A cytometry assay that measures the count of megakaryocytes in venous blood
    """
    venous_blood_nucleated_RBC_count_assay = "OBI:2100366"
    """
    A cytometry assay that measures the count of nucleated RBCs in venous blood
    """
    venous_blood_WBC_count_assay = "OBI:2100367"
    """
    A cytometry assay that measures the count of WBCs in venous blood
    """
    automated_count_venous_blood_reticulocyte_count_assay = "OBI:2100368"
    """
    A cytometry assay that measures the count of reticulocytes in venous blood as part of a automated count order
    """
    total_venous_blood_homocysteine_assay = "OBI:2100369"
    """
    An analyte assay that measures the abundance of homocysteine in venous blood as part of a total order
    """
    venous_blood_Ceruloplasmin_assay = "OBI:2100370"
    """
    An analyte assay that measures the abundance of Ceruloplasmin in venous blood
    """
    GEM4_arterial_blood_bicarbonate_assay = "OBI:2100371"
    """
    An analyte assay that measures the abundance of bicarbonate in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_lactic_acid_assay = "OBI:2100372"
    """
    An assay that measures lactic acid in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_hemoglobin_assay = "OBI:2100373"
    """
    An analyte assay that measures the abundance of hemoglobin in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_sodium_assay = "OBI:2100374"
    """
    An analyte assay that measures the abundance of sodium in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_potassium_assay = "OBI:2100375"
    """
    An analyte assay that measures the abundance of potassium in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_temperature_assay = "OBI:2100376"
    """
    An assay that measures temperature in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_glucose_assay = "OBI:2100377"
    """
    An analyte assay that measures the abundance of glucose in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_oxygen_assay = "OBI:2100378"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_hematocrit_assay = "OBI:2100379"
    """
    A cytometry assay that measures the proportion of red blood cells in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_ionized_calcium_assay = "OBI:2100380"
    """
    An analyte assay that measures the abundance of ionized calcium in arterial blood as part of a GEM4 order
    """
    GEM4_arterial_blood_carbon_dioxide_assay = "OBI:2100381"
    """
    An analyte assay that measures the abundance of carbon dioxide in arterial blood as part of a GEM4 order
    """
    liver_fibrosis_LEFT_PARENTHESISNAFLDRIGHT_PARENTHESIS_venous_blood_platelet_count_assay = "OBI:2100382"
    """
    A cytometry assay that measures the count of platelets in venous blood as part of a liver fibrosis (NAFLD) order
    """
    venous_blood_beta_hydroxybutric_acid_assay = "OBI:2100383"
    """
    An analyte assay that measures the abundance of beta hydroxybutric acid in venous blood
    """
    CBC_with_manual_differential_venous_blood_plasma_cell_count_assay = "OBI:2100384"
    """
    A cytometry assay that measures the count of plasma cells in venous blood as part of a CBC with manual differential order
    """
    venous_blood_erythropoietin_assay = "OBI:2100385"
    """
    An analyte assay that measures the abundance of erythropoietin in venous blood
    """
    blood_gas_arterial_blood_oxygen_assay = "OBI:2100386"
    """
    An analyte assay that measures the abundance of oxygen in arterial blood as part of a blood gas order
    """
    blood_gas_arterial_blood_bicarbonate_assay = "OBI:2100387"
    """
    An analyte assay that measures the abundance of bicarbonate in arterial blood as part of a blood gas order
    """
    blood_gas_arterial_blood_carbon_dioxide_assay = "OBI:2100388"
    """
    An analyte assay that measures the abundance of carbon dioxide in arterial blood as part of a blood gas order
    """
    freeSOLIDUStotal_venous_blood_PSA_assay = "OBI:2100389"
    """
    An analyte assay that measures the abundance of PSA in venous blood as part of a free/total order
    """
    cerebrospinal_fluid_lymphocyte_count_assay = "OBI:2100390"
    """
    A cytometry assay that measures the count of lymphocytes in cerebrospinal fluid
    """
    cerebrospinal_fluid_segmented_neutrophil_count_assay = "OBI:2100391"
    """
    A cytometry assay that measures the count of segmented neutrophils in cerebrospinal fluid
    """
    cerebrospinal_fluid_mesothelial_cell_count_assay = "OBI:2100392"
    """
    A cytometry assay that measures the count of mesothelial cells in cerebrospinal fluid
    """
    cerebrospinal_fluid_macrophage_count_assay = "OBI:2100393"
    """
    A cytometry assay that measures the count of macrophages in cerebrospinal fluid
    """
    cerebrospinal_fluid_basophil_count_assay = "OBI:2100394"
    """
    A cytometry assay that measures the count of basophils in cerebrospinal fluid
    """
    cerebrospinal_fluid_monocyte_count_assay = "OBI:2100395"
    """
    A cytometry assay that measures the count of monocytes in cerebrospinal fluid
    """
    cerebrospinal_fluid_eosinophil_count_assay = "OBI:2100396"
    """
    A cytometry assay that measures the count of eosinophils in cerebrospinal fluid
    """
    venous_blood_beta_2_microglobulin_assay = "OBI:2100397"
    """
    An analyte assay that measures the abundance of beta-2-microglobulin in venous blood
    """
    lipid_panel_reflex_direct_venous_blood_low_density_lipoprotein_assay = "OBI:2100398"
    """
    An analyte assay that measures the abundance of low density lipoprotein in venous blood as part of a Lipid panel reflex direct order
    """
    lipid_panel_reflex_direct_venous_blood_triglyceride_assay = "OBI:2100399"
    """
    An analyte assay that measures the abundance of triglyceride in venous blood as part of a Lipid panel reflex direct order
    """
    lipid_panel_reflex_direct_venous_blood_cholesterol_assay = "OBI:2100400"
    """
    An analyte assay that measures the abundance of cholesterol in venous blood as part of a Lipid panel reflex direct order
    """
    lipid_panel_reflex_direct_venous_blood_high_density_lipoprotein_assay = "OBI:2100401"
    """
    An analyte assay that measures the abundance of high density lipoprotein in venous blood as part of a Lipid panel reflex direct order
    """
    pooled_clone_sequencing_assay = "OBI:2100402"
    """
    A DNA sequencing assay in which the DNA input is derived from pooled clones (for example BACs and Fosmids) is sequenced.
    """
    chromium_release_assay = "OBI:9999994"
    """
    An in vitro cell killing assay in which radioactive chromium is absorbed by cells and released into supernatant when the cells die. The amount of radioactivity measured in the supernatant is a proxy for the number of cells that have died.
    """


class EnumAsserterType(str, Enum):
    """
    Individuals or organizations making assertions.
    """
    Research_Staff_Asserted = "CAMO:0000016"
    """
    Assertion made by research staff.
    """
    Healthcare_Asserted = "CAMO:0000017"
    """
    Assertion documented by a healthcare system or provider.
    """
    Participant_or_Representative_Asserted = "CAMO:0000018"
    """
    Assertion made by a study participant, their representative, or some combination.
    """
    Participant_Asserted = "CAMO:0000019"
    """
    Assertion made by a study participant.
    """
    Representative_Asserted = "CAMO:0000020"
    """
    Assertion made by a study participant's representative or representatives.
    """
    Caregiver_Asserted = "CAMO:0000021"
    """
    Assertion made by a study participant's caregiver or caregivers.
    """


class EnumAvailabilityStatus(str, Enum):
    """
    Is this item available for use?
    """
    Available = "snomedct:103328004"
    """
    The item is available to users, authorization/request permitting.
    """
    Unavailable = "snomedct:103329007"
    """
    The item is not available to users.
    """


class EnumDataCategory(str, Enum):
    """
    Categories of data which may be collected about participants.
    """
    Nucleic_acids = "edam:topic_0077"
    """
    The processing and analysis of nucleic acid sequence, structural and other data.
    """
    Proteins = "edam:topic_0078"
    """
    Archival, processing and analysis of protein data, typically molecular sequence and structural data.
    """
    Sequence_analysis = "edam:topic_0080"
    """
    The archival, processing and analysis of molecular sequences (monomer composition of polymers) including molecular sequence data resources, sequence sites, alignments, motifs and profiles.
    """
    Structure_analysis = "edam:topic_0081"
    """
    The curation, processing, analysis and prediction of data about the structure of biological molecules, typically proteins and nucleic acids and other macromolecules.
    """
    Structure_prediction = "edam:topic_0082"
    """
    The prediction of molecular structure, including the prediction, modelling, recognition or design of protein secondary or tertiary structure or other structural features, and the folding of nucleic acid molecules and the prediction or design of nucleic acid (typically RNA) sequences with specific conformations.
    """
    Phylogeny = "edam:topic_0084"
    """
    The study of evolutionary relationships amongst organisms.
    """
    Functional_genomics = "edam:topic_0085"
    """
    The study of gene or protein functions and their interactions in totality in a given organism, tissue, cell etc.
    """
    Ontology_and_terminology = "edam:topic_0089"
    """
    The conceptualisation, categorisation and nomenclature (naming) of entities or phenomena within biology or bioinformatics. This includes formal ontologies, controlled vocabularies, structured glossary, symbols and terminology or other related resource.
    """
    Bioinformatics = "edam:topic_0091"
    """
    The archival, curation, processing and analysis of complex biological data.
    """
    Data_visualisation = "edam:topic_0092"
    """
    Rendering (drawing on a computer screen) or visualisation of molecular sequences, structures or other biomolecular data.
    """
    Nucleic_acid_structure_analysis = "edam:topic_0097"
    """
    The archival, curation, processing and analysis of nucleic acid structural information, such as whole structures, structural features and alignments, and associated annotation.
    """
    RNA = "edam:topic_0099"
    """
    RNA sequences and structures.
    """
    Mapping = "edam:topic_0102"
    """
    The mapping of complete (typically nucleotide) sequences. Mapping (in the sense of short read alignment, or more generally, just alignment) has application in RNA-Seq analysis (mapping of transcriptomics reads), variant discovery (e.g. mapping of exome capture), and re-sequencing (mapping of WGS reads).
    """
    Protein_expression = "edam:topic_0108"
    """
    The translation of mRNA into protein and subsequent protein processing in the cell.
    """
    Gene_structure = "edam:topic_0114"
    """
    Gene structure, regions which make an RNA product and features such as promoters, coding regions, gene fusion, splice sites etc.
    """
    Proteomics = "edam:topic_0121"
    """
    Proteomics is in the narrow sense (sensu stricto) the application of methods to separate, characterise, identify, and quantify all proteins (the proteome) - or a substantial set of proteins - that are present in a sample. Proteomics in the broad sense is the science of proteins and peptides on the large scale.
    """
    Structural_genomics = "edam:topic_0122"
    """
    The elucidation of the three dimensional structure for all (available) proteins in a given organism.
    """
    Protein_properties = "edam:topic_0123"
    """
    The study of the physical and biochemical properties of peptides and proteins, for example the hydrophobic, hydrophilic and charge properties of a protein.
    """
    Protein_interactions = "edam:topic_0128"
    """
    Protein-protein, protein-DNA/RNA and protein-ligand interactions, including analysis of known interactions and prediction of putative interactions.
    """
    Protein_folding_stability_and_design = "edam:topic_0130"
    """
    Protein stability, folding (in 3D space) and protein sequence-structure-function relationships. This includes for example study of inter-atomic or inter-residue interactions in protein (3D) structures, the effect of mutation, and the design of proteins with specific properties, typically by designing changes (via site-directed mutagenesis) to an existing protein.
    """
    Protein_targeting_and_localisation = "edam:topic_0140"
    """
    The study of how proteins are transported within and without the cell, including signal peptides, protein subcellular localisation and export.
    """
    Carbohydrates = "edam:topic_0152"
    """
    Carbohydrates, typically including structural information.
    """
    Lipidomics = "edam:topic_0153"
    """
    Lipids and their structures.
    """
    Small_molecules = "edam:topic_0154"
    """
    Small molecules of biological significance, typically archival, curation, processing and analysis of structural information.
    """
    Sequence_composition_complexity_and_repeats = "edam:topic_0157"
    """
    The archival, processing and analysis of the basic character composition of molecular sequences, for example character or word frequency, ambiguity, complexity, particularly regions of low complexity, and repeats or the repetitive nature of molecular sequences.
    """
    Sequence_sites_features_and_motifs = "edam:topic_0160"
    """
    The archival, detection, prediction and analysis of positional features such as functional and other key sites, in molecular sequences and the conserved patterns (motifs, profiles etc.) that may be used to describe them.
    """
    Protein_structural_motifs_and_surfaces = "edam:topic_0166"
    """
    Structural features or common 3D motifs within protein structures, including the surface of a protein structure, such as biological interfaces with other molecules.
    """
    Molecular_dynamics = "edam:topic_0176"
    """
    The study and simulation of molecular (typically protein) conformation using a computational model of physical forces and computer simulation.
    """
    Phylogenomics = "edam:topic_0194"
    """
    The integrated study of evolutionary relationships and whole genome data, for example, in the analysis of species trees, horizontal gene transfer and evolutionary reconstruction.
    """
    Sequence_assembly = "edam:topic_0196"
    """
    The assembly of fragments of a DNA sequence to reconstruct the original sequence.
    """
    Genetic_variation = "edam:topic_0199"
    """
    Stable, naturally occurring mutations in a nucleotide sequence including alleles, naturally occurring mutations such as single base nucleotide substitutions, deletions and insertions, RFLPs and other polymorphisms.
    """
    Pharmacology = "edam:topic_0202"
    """
    The study of drugs and their effects or responses in living systems.
    """
    Gene_expression = "edam:topic_0203"
    """
    The analysis of levels and patterns of synthesis of gene products (proteins and functional RNA) including interpretation in functional terms of gene expression data.
    """
    Gene_regulation = "edam:topic_0204"
    """
    The regulation of gene expression.
    """
    Pharmacogenomics = "edam:topic_0208"
    """
    The influence of genotype on drug response, for example by correlating gene expression or single-nucleotide polymorphisms with drug efficacy or toxicity.
    """
    Medicinal_chemistry = "edam:topic_0209"
    """
    The design and chemical synthesis of bioactive molecules, for example drugs or potential drug compounds, for medicinal purposes.
    """
    Natural_language_processing = "edam:topic_0218"
    """
    The processing and analysis of natural language, such as scientific literature in English, in order to extract data and information, or to enable human-computer interaction.
    """
    Data_curation_and_archival = "edam:topic_0219"
    """
    Data curation and archival includes the preservation of data in a repository, archive, or a deposition database; and curation of data and metadata, database accessions, annotation, and data provenance.
    """
    NMR = "edam:topic_0593"
    """
    An analytical technique that exploits the magenetic properties of certain atomic nuclei to provide information on the structure, dynamics, reaction state and chemical environment of molecules.
    """
    Protein_modifications = "edam:topic_0601"
    """
    Protein chemical modifications, e.g. post-translational modifications.
    """
    Molecular_interactions_pathways_and_networks = "edam:topic_0602"
    """
    Molecular interactions, biological pathways, networks and other models.
    """
    Informatics = "edam:topic_0605"
    """
    The study and practice of information processing and use of computer information systems.
    """
    Laboratory_information_management = "edam:topic_0607"
    """
    Laboratory management and resources, for example, catalogues of biological resources for use in the lab including cell lines, viruses, plasmids, phages, DNA probes and primers and so on.
    """
    Ecology = "edam:topic_0610"
    """
    The ecological and environmental sciences and especially the application of information technology (ecoinformatics).
    """
    Electron_microscopy = "edam:topic_0611"
    """
    The study of matter by studying the interference pattern from firing electrons at a sample, to analyse structures at resolutions higher than can be achieved using light.
    """
    Model_organisms = "edam:topic_0621"
    """
    A specific organism, or group of organisms, used to study a particular aspect of biology.
    """
    Genomics = "edam:topic_0622"
    """
    Whole genomes of one or more organisms, or genomes in general, such as meta-information on genomes, genome projects, gene names etc.
    """
    Gene_and_protein_families = "edam:topic_0623"
    """
    Particular gene(s), gene family or other gene group or system and their encoded proteins.Primarily the classification of proteins (from sequence or structural data) into clusters, groups, families etc., curation of a particular protein or protein family, or any other proteins that have been classified as members of a common group.
    """
    Genotype_and_phenotype = "edam:topic_0625"
    """
    The study of genetic constitution of a living entity, such as an individual, and organism, a cell and so on, typically with respect to a particular observable phenotypic traits, or resources concerning such traits, which might be an aspect of biochemistry, physiology, morphology, anatomy, development and so on.
    """
    Probes_and_primers = "edam:topic_0632"
    """
    Molecular probes (e.g. a peptide probe or DNA microarray probe) or PCR primers and hybridisation oligos in a nucleic acid sequence.
    """
    Pathology = "edam:topic_0634"
    """
    Diseases, including diseases in general and the genes, gene variations and proteins involved in one or more specific diseases.
    """
    Taxonomy = "edam:topic_0637"
    """
    Organism classification, identification and naming.
    """
    DNA = "edam:topic_0654"
    """
    DNA sequences and structure, including processes such as methylation and replication.
    """
    Functional_regulatory_and_non_coding_RNA = "edam:topic_0659"
    """
    Non-coding or functional RNA sequences, including regulatory RNA sequences, ribosomal RNA (rRNA) and transfer RNA (tRNA).
    """
    Protein_folds_and_structural_domains = "edam:topic_0736"
    """
    Protein tertiary structural domains and folds in a protein or polypeptide chain.
    """
    Transcription_factors_and_regulatory_sites = "edam:topic_0749"
    """
    Proteins that bind to DNA and control transcription of DNA to mRNA (transcription factors) and also transcriptional regulatory sites, elements and regions (such as promoters, enhancers, silencers and boundary elements / insulators) in nucleotide sequences.
    """
    Workflows = "edam:topic_0769"
    """
    Biological or biomedical analytical workflows or pipelines.
    """
    Plant_biology = "edam:topic_0780"
    """
    Plants, e.g. information on a specific plant genome including molecular sequences, genes and annotation.
    """
    Virology = "edam:topic_0781"
    """
    Study of viruses, e.g. sequence and structural data, interactions of viral proteins, or a viral genome including molecular sequences, genes and annotation.
    """
    Comparative_genomics = "edam:topic_0797"
    """
    The study (typically comparison) of the sequence, structure or function of multiple genomes.
    """
    Mobile_genetic_elements = "edam:topic_0798"
    """
    Mobile genetic elements, such as transposons, Plasmids, Bacteriophage elements and Group II introns.
    """
    Immunology = "edam:topic_0804"
    """
    The application of information technology to immunology such as immunological processes, immunological genes, proteins and peptide ligands, antigens and so on.
    """
    Membrane_and_lipoproteins = "edam:topic_0820"
    """
    Lipoproteins (protein-lipid assemblies), and proteins or region of a protein that spans or are associated with a membrane.
    """
    Enzymes = "edam:topic_0821"
    """
    Proteins that catalyze chemical reaction, the kinetics of enzyme-catalysed reactions, enzyme nomenclature etc.
    """
    Structural_biology = "edam:topic_1317"
    """
    The molecular structure of biological molecules, particularly macromolecules such as proteins and nucleic acids.
    """
    Function_analysis = "edam:topic_1775"
    """
    The study of gene and protein function including the prediction of functional properties of a protein.
    """
    Cell_biology = "edam:topic_2229"
    """
    Cells, such as key genes and proteins involved in the cell cycle.
    """
    Cheminformatics = "edam:topic_2258"
    """
    The application of information technology to chemistry in biological research environment.
    """
    Systems_biology = "edam:topic_2259"
    """
    The holistic modelling and analysis of complex biological systems and the interactions therein.
    """
    Statistics_and_probability = "edam:topic_2269"
    """
    The application of statistical methods to biological problems.
    """
    Molecular_modelling = "edam:topic_2275"
    """
    The construction, analysis, evaluation, refinement etc. of models of a molecules properties or behaviour, including the modelling the structure of proteins in complex with small molecules or other macromolecules (docking).
    """
    DNA_mutation = "edam:topic_2533"
    """
    DNA mutation.
    """
    Oncology = "edam:topic_2640"
    """
    The study of cancer, for example, genes and proteins implicated in cancer.
    """
    Protein_structure_analysis = "edam:topic_2814"
    """
    Protein secondary or tertiary structural data and/or associated annotation.
    """
    Human_biology = "edam:topic_2815"
    """
    The study of human beings in general, including the human genome and proteome.
    """
    X_ray_diffraction = "edam:topic_2828"
    """
    The study of matter and their structure by means of the diffraction of X-rays, typically the diffraction pattern caused by the regularly spaced atoms of a crystalline sample.
    """
    Immunoproteins_and_antigens = "edam:topic_2830"
    """
    Immunity-related proteins and their ligands.
    """
    Toxicology = "edam:topic_2840"
    """
    Toxins and the adverse effects of these chemical substances on living organisms.
    """
    DNA_polymorphism = "edam:topic_2885"
    """
    DNA polymorphism.
    """
    Molecular_biology = "edam:topic_3047"
    """
    The molecular basis of biological activity, particularly the macromolecules (e.g. proteins and nucleic acids) that are essential to life.
    """
    Biodiversity = "edam:topic_3050"
    """
    The degree of variation of life forms within a given ecosystem, biome or an entire planet.
    """
    Genetics = "edam:topic_3053"
    """
    The study of genes, genetic variation and heredity in living organisms.
    """
    Quantitative_genetics = "edam:topic_3055"
    """
    The genes and genetic mechanisms such as Mendelian inheritance that underly continuous phenotypic traits (such as height or weight).
    """
    Population_genetics = "edam:topic_3056"
    """
    The distribution of allele frequencies in a population of organisms and its change subject to evolutionary processes including natural selection, genetic drift, mutation and gene flow.
    """
    Medical_informatics = "edam:topic_3063"
    """
    The application of information technology to health, disease and biomedicine.
    """
    Developmental_biology = "edam:topic_3064"
    """
    How organisms grow and develop.
    """
    Embryology = "edam:topic_3065"
    """
    The development of organisms between the one-cell stage (typically the zygote) and the end of the embryonic stage.
    """
    Anatomy = "edam:topic_3067"
    """
    The form and function of the structures of living organisms.
    """
    Literature_and_language = "edam:topic_3068"
    """
    The scientific literature, language processing, reference information, and documentation.
    """
    Biology = "edam:topic_3070"
    """
    The study of life and living organisms, including their morphology, biochemistry, physiology, development, evolution, and so on.
    """
    Data_management = "edam:topic_3071"
    """
    Data management comprises the practices and principles of taking care of data, other than analysing them. This includes for example taking care of the associated metadata, data formats, storage, preservation/archiving, access, and legal aspects related to using and sharing data.
    """
    Data_acquisition = "edam:topic_3077"
    """
    The acquisition of data, typically measurements of physical systems using any type of sampling system, or by another other means.
    """
    Protein_variants = "edam:topic_3120"
    """
    Protein sequence variants produced e.g. from alternative splicing, alternative promoter usage, alternative initiation and ribosomal frameshifting.
    """
    DNA_binding_sites = "edam:topic_3125"
    """
    Nucleic acids binding to some other molecule.
    """
    DNA_replication_and_recombination = "edam:topic_3127"
    """
    DNA replication or recombination.
    """
    Sequencing = "edam:topic_3168"
    """
    The determination of complete (typically nucleotide) sequences, including those of genomes (full genome sequencing, de novo sequencing and resequencing), amplicons and transcriptomes.
    """
    ChIP_seq = "edam:topic_3169"
    """
    The analysis of protein-DNA interactions where chromatin immunoprecipitation (ChIP) is used in combination with massively parallel DNA sequencing to identify the binding sites of DNA-associated proteins.
    """
    RNA_Seq = "edam:topic_3170"
    """
    A topic concerning high-throughput sequencing of cDNA to measure the RNA content (transcriptome) of a sample, for example, to investigate how different alleles of a gene are expressed, detect post-transcriptional mutations or identify gene fusions.
    """
    Metabolomics = "edam:topic_3172"
    """
    The systematic study of metabolites, the chemical processes they are involved, and the chemical fingerprints of specific cellular processes in a whole cell, tissue, organ or organism.
    """
    Epigenomics = "edam:topic_3173"
    """
    The study of the epigenetic modifications of a whole cell, tissue, organism etc.
    """
    Metagenomics = "edam:topic_3174"
    """
    The study of genetic material recovered from environmental samples, and associated environmental data.
    """
    Structural_variation = "edam:topic_3175"
    """
    Variation in chromosome structure including microscopic and submicroscopic types of variation such as deletions, duplications, copy-number variants, insertions, inversions and translocations.
    """
    DNA_packaging = "edam:topic_3176"
    """
    DNA-histone complexes (chromatin), organisation of chromatin into nucleosomes and packaging into higher-order structures.
    """
    ChIP_on_chip = "edam:topic_3179"
    """
    Experimental techniques that combine chromatin immunoprecipitation ('ChIP') with microarray ('chip'). ChIP-on-chip is used for high-throughput study protein-DNA interactions.
    """
    Sample_collections = "edam:topic_3277"
    """
    Biological samples and specimens.
    """
    Biochemistry = "edam:topic_3292"
    """
    Chemical substances and physico-chemical processes and that occur within living organisms.
    """
    Phylogenetics = "edam:topic_3293"
    """
    The study of evolutionary relationships amongst organisms from analysis of genetic information (typically gene or protein sequences).
    """
    Epigenetics = "edam:topic_3295"
    """
    Topic concerning the study of heritable changes, for example in gene expression or phenotype, caused by mechanisms other than changes in the DNA sequence.
    """
    Biotechnology = "edam:topic_3297"
    """
    The exploitation of biological process, structure and function for industrial purposes, for example the genetic manipulation of microorganisms for the antibody production.
    """
    Phenomics = "edam:topic_3298"
    """
    Phenomes, or the study of the change in phenotype (the physical and biochemical traits of organisms) in response to genetic and environmental factors.
    """
    Evolutionary_biology = "edam:topic_3299"
    """
    The evolutionary processes, from the genetic to environmental scale, that produced life in all its diversity.
    """
    Physiology = "edam:topic_3300"
    """
    The functions of living organisms and their constituent parts.
    """
    Microbiology = "edam:topic_3301"
    """
    The biology of microorganisms.
    """
    Parasitology = "edam:topic_3302"
    """
    The biology of parasites.
    """
    Medicine = "edam:topic_3303"
    """
    Research in support of healing by diagnosis, treatment, and prevention of disease.
    """
    Neurobiology = "edam:topic_3304"
    """
    The study of the nervous system and brain; its anatomy, physiology and function.
    """
    Public_health_and_epidemiology = "edam:topic_3305"
    """
    Topic concerning the the patterns, cause, and effect of disease within populations.
    """
    Biophysics = "edam:topic_3306"
    """
    The use of physics to study biological system.
    """
    Computational_biology = "edam:topic_3307"
    """
    The development and application of theory, analytical methods, mathematical models and computational simulation of biological systems.
    """
    Transcriptomics = "edam:topic_3308"
    """
    The analysis of transcriptomes, or a set of all the RNA molecules in a specific cell, tissue etc.
    """
    Chemistry = "edam:topic_3314"
    """
    The composition and properties of matter, reactions, and the use of reactions to create new substances.
    """
    Mathematics = "edam:topic_3315"
    """
    The study of numbers (quantity) and other topics including structure, space, and change.
    """
    Computer_science = "edam:topic_3316"
    """
    The theory and practical use of computer systems.
    """
    Physics = "edam:topic_3318"
    """
    The study of matter, space and time, and related concepts such as energy and force.
    """
    RNA_splicing = "edam:topic_3320"
    """
    RNA splicing; post-transcription RNA modification involving the removal of introns and joining of exons.
    """
    Molecular_genetics = "edam:topic_3321"
    """
    The structure and function of genes at a molecular level.
    """
    Respiratory_medicine = "edam:topic_3322"
    """
    The study of respiratory system.
    """
    Infectious_disease = "edam:topic_3324"
    """
    The branch of medicine that deals with the prevention, diagnosis and management of transmissible disease with clinically evident illness resulting from infection with pathogenic biological agents (viruses, bacteria, fungi, protozoa, parasites and prions).
    """
    Rare_diseases = "edam:topic_3325"
    """
    The study of rare diseases.
    """
    Computational_chemistry = "edam:topic_3332"
    """
    Topic concerning the development and application of theory, analytical methods, mathematical models and computational simulation of chemical systems.
    """
    Neurology = "edam:topic_3334"
    """
    The branch of medicine that deals with the anatomy, functions and disorders of the nervous system.
    """
    Cardiology = "edam:topic_3335"
    """
    The diseases and abnormalities of the heart and circulatory system.
    """
    Drug_discovery = "edam:topic_3336"
    """
    The discovery and design of drugs or potential drug compounds.
    """
    Biobank = "edam:topic_3337"
    """
    Repositories of biological samples, typically human, for basic biological and clinical research.
    """
    Mouse_clinic = "edam:topic_3338"
    """
    Laboratory study of mice, for example, phenotyping, and mutagenesis of mouse cell lines.
    """
    Microbial_collection = "edam:topic_3339"
    """
    Collections of microbial cells including bacteria, yeasts and moulds.
    """
    Cell_culture_collection = "edam:topic_3340"
    """
    Collections of cells grown under laboratory conditions, specifically, cells from multi-cellular eukaryotes and especially animal cells.
    """
    Clone_library = "edam:topic_3341"
    """
    Collections of DNA, including both collections of cloned molecules, and populations of micro-organisms that store and propagate cloned DNA.
    """
    Translational_medicine = "edam:topic_3342"
    """
    'translating' the output of basic and biomedical research into better diagnostic tools, medicines, medical procedures, policies and advice.
    """
    Compound_libraries_and_screening = "edam:topic_3343"
    """
    Collections of chemicals, typically for use in high-throughput screening experiments.
    """
    Biomedical_science = "edam:topic_3344"
    """
    Topic concerning biological science that is (typically) performed in the context of medicine.
    """
    Data_identity_and_mapping = "edam:topic_3345"
    """
    Topic concerning the identity of biological entities, or reports on such entities, and the mapping of entities and records in different databases.
    """
    Biomarkers = "edam:topic_3360"
    """
    Objective indicators of biological state often used to assess health, and determinate treatment.
    """
    Data_architecture_analysis_and_design = "edam:topic_3365"
    """
    The development of policies, models and standards that cover data acquisition, storage and integration, such that it can be put to use, typically through a process of systematically applying statistical and / or logical techniques to describe, illustrate, summarise or evaluate data.
    """
    Data_integration_and_warehousing = "edam:topic_3366"
    """
    The combination and integration of data from different sources, for example into a central repository or warehouse, to provide users with a unified view of these data.
    """
    Biomaterials = "edam:topic_3368"
    """
    Any matter, surface or construct that interacts with a biological system.
    """
    Chemical_biology = "edam:topic_3369"
    """
    The use of synthetic chemistry to study and manipulate biological systems.
    """
    Analytical_chemistry = "edam:topic_3370"
    """
    The study of the separation, identification, and quantification of the chemical components of natural and artificial materials.
    """
    Synthetic_chemistry = "edam:topic_3371"
    """
    The use of chemistry to create new compounds.
    """
    Software_engineering = "edam:topic_3372"
    """
    The process that leads from an original formulation of a computing problem to executable programs.
    """
    Drug_development = "edam:topic_3373"
    """
    The process of bringing a new drug to market once a lead compounds has been identified through drug discovery.
    """
    Biotherapeutics = "edam:topic_3374"
    """
    The process of formulating and administering a pharmaceutical compound to achieve a therapeutic effect.
    """
    Drug_metabolism = "edam:topic_3375"
    """
    The study of how a drug interacts with the body.
    """
    Medicines_research_and_development = "edam:topic_3376"
    """
    The discovery, development and approval of medicines.
    """
    Safety_sciences = "edam:topic_3377"
    """
    The safety (or lack) of drugs and other medical interventions.
    """
    Pharmacovigilance = "edam:topic_3378"
    """
    The detection, assessment, understanding and prevention of adverse effects of medicines.
    """
    Preclinical_and_clinical_studies = "edam:topic_3379"
    """
    The testing of new medicines, vaccines or procedures on animals (preclinical) and humans (clinical) prior to their approval by regulatory authorities.
    """
    Imaging = "edam:topic_3382"
    """
    The visual representation of an object.
    """
    Bioimaging = "edam:topic_3383"
    """
    The use of imaging techniques to understand biology.
    """
    Medical_imaging = "edam:topic_3384"
    """
    The use of imaging techniques for clinical purposes for medical research.
    """
    Light_microscopy = "edam:topic_3385"
    """
    The use of optical instruments to magnify the image of an object.
    """
    Laboratory_animal_science = "edam:topic_3386"
    """
    The use of animals and alternatives in experimental research.
    """
    Marine_biology = "edam:topic_3387"
    """
    The study of organisms in the ocean or brackish waters.
    """
    Molecular_medicine = "edam:topic_3388"
    """
    The identification of molecular and genetic causes of disease and the development of interventions to correct them.
    """
    Nutritional_science = "edam:topic_3390"
    """
    The study of the effects of food components on the metabolism, health, performance and disease resistance of humans and animals. It also includes the study of human behaviours related to food choices.
    """
    Omics = "edam:topic_3391"
    """
    The collective characterisation and quantification of pools of biological molecules that translate into the structure, function, and dynamics of an organism or organisms.
    """
    Quality_affairs = "edam:topic_3393"
    """
    The processes that need to be in place to ensure the quality of products for human or animal use.
    """
    Regulatory_affairs = "edam:topic_3394"
    """
    The protection of public health by controlling the safety and efficacy of products in areas including pharmaceuticals, veterinary medicine, medical devices, pesticides, agrochemicals, cosmetics, and complementary medicines.
    """
    Regenerative_medicine = "edam:topic_3395"
    """
    Biomedical approaches to clinical interventions that involve the use of stem cells.
    """
    Systems_medicine = "edam:topic_3396"
    """
    An interdisciplinary field of study that looks at the dynamic systems of the human body as part of an integrted whole, incorporating biochemical, physiological, and environmental interactions that sustain life.
    """
    Veterinary_medicine = "edam:topic_3397"
    """
    Topic concerning the branch of medicine that deals with the prevention, diagnosis, and treatment of disease, disorder and injury in animals.
    """
    Bioengineering = "edam:topic_3398"
    """
    The application of biological concepts and methods to the analytical and synthetic methodologies of engineering.
    """
    Geriatric_medicine = "edam:topic_3399"
    """
    The branch of medicine dealing with the diagnosis, treatment and prevention of disease in older people, and the problems specific to aging.
    """
    Allergy_clinical_immunology_and_immunotherapeutics = "edam:topic_3400"
    """
    Health issues related to the immune system and their prevention, diagnosis and management.
    """
    Pain_medicine = "edam:topic_3401"
    """
    The prevention of pain and the evaluation, treatment and rehabilitation of persons in pain.
    """
    Anaesthesiology = "edam:topic_3402"
    """
    Anaesthesia and anaesthetics.
    """
    Critical_care_medicine = "edam:topic_3403"
    """
    The multidisciplinary that cares for patients with acute, life-threatening illness or injury.
    """
    Dermatology = "edam:topic_3404"
    """
    The branch of medicine that deals with prevention, diagnosis and treatment of disorders of the skin, scalp, hair and nails.
    """
    Dentistry = "edam:topic_3405"
    """
    The study, diagnosis, prevention and treatments of disorders of the oral cavity, maxillofacial area and adjacent structures.
    """
    Ear_nose_and_throat_medicine = "edam:topic_3406"
    """
    The branch of medicine that deals with the prevention, diagnosis, and treatment of disorders of the ear, nose and throat.
    """
    Endocrinology_and_metabolism = "edam:topic_3407"
    """
    The branch of medicine dealing with diseases of endocrine organs, hormone systems, their target organs, and disorders of the pathways of glucose and lipid metabolism.
    """
    Haematology = "edam:topic_3408"
    """
    The branch of medicine that deals with the blood, blood-forming organs and blood diseases.
    """
    Gastroenterology = "edam:topic_3409"
    """
    The branch of medicine that deals with disorders of the oesophagus, stomach, duodenum, jejenum, ileum, large intestine, sigmoid colon and rectum.
    """
    Gender_medicine = "edam:topic_3410"
    """
    The study of the biological and physiological differences between males and females and how they effect differences in disease presentation and management.
    """
    Gynaecology_and_obstetrics = "edam:topic_3411"
    """
    The branch of medicine that deals with the health of the female reproductive system, pregnancy and birth.
    """
    Hepatic_and_biliary_medicine = "edam:topic_3412"
    """
    The branch of medicine that deals with the liver, gallbladder, bile ducts and bile.
    """
    Trauma_medicine = "edam:topic_3414"
    """
    The branch of medicine that treats body wounds or shock produced by sudden physical injury, as from violence or accident.
    """
    Medical_toxicology = "edam:topic_3415"
    """
    The branch of medicine that deals with the diagnosis, management and prevention of poisoning and other adverse health effects caused by medications, occupational and environmental toxins, and biological agents.
    """
    Musculoskeletal_medicine = "edam:topic_3416"
    """
    The branch of medicine that deals with the prevention, diagnosis, and treatment of disorders of the muscle, bone and connective tissue. It incorporates aspects of orthopaedics, rheumatology, rehabilitation medicine and pain medicine.
    """
    Ophthalmology = "edam:topic_3417"
    """
    The branch of medicine that deals with disorders of the eye, including eyelid, optic nerve/visual pathways and occular muscles.
    """
    Paediatrics = "edam:topic_3418"
    """
    The branch of medicine that deals with the medical care of infants, children and adolescents.
    """
    Psychiatry = "edam:topic_3419"
    """
    The branch of medicine that deals with the management of mental illness, emotional disturbance and abnormal behaviour.
    """
    Reproductive_health = "edam:topic_3420"
    """
    The health of the reproductive processes, functions and systems at all stages of life.
    """
    Surgery = "edam:topic_3421"
    """
    The use of operative, manual and instrumental techniques on a patient to investigate and/or treat a pathological condition or help improve bodily function or appearance.
    """
    Urology_and_nephrology = "edam:topic_3422"
    """
    The branches of medicine and physiology focussing on the function and disorders of the urinary system in males and females, the reproductive system in males, and the kidney.
    """
    Complementary_medicine = "edam:topic_3423"
    """
    Medical therapies that fall beyond the scope of conventional medicine but may be used alongside it in the treatment of disease and ill health.
    """
    MRI = "edam:topic_3444"
    """
    Techniques that uses magnetic fields and radiowaves to form images, typically to investigate the anatomy and physiology of the human body.
    """
    Neutron_diffraction = "edam:topic_3448"
    """
    The study of matter by studying the diffraction pattern from firing neutrons at a sample, typically to determine atomic and/or magnetic structure.
    """
    Tomography = "edam:topic_3452"
    """
    Imaging in sections (sectioning), through the use of a wave-generating device (tomograph) that generates an image (a tomogram).
    """
    Data_mining = "edam:topic_3473"
    """
    The discovery of patterns in large data sets and the extraction and trasnsformation of those patterns into a useful format.
    """
    Machine_learning = "edam:topic_3474"
    """
    A topic concerning the application of artificial intelligence methods to algorithms, in order to create methods that can learn from data in order to generate an output, rather than relying on explicitly encoded information only.
    """
    Database_management = "edam:topic_3489"
    """
    The general handling of data stored in digital archives such as databases, databanks, web portals, and other data resources.
    """
    Zoology = "edam:topic_3500"
    """
    Animals, e.g. information on a specific animal genome including molecular sequences, genes and annotation.
    """
    Protein_sites_features_and_motifs = "edam:topic_3510"
    """
    The biology, archival, detection, prediction and analysis of positional features such as functional and other key sites, in protein sequences and the conserved patterns (motifs, profiles etc.) that may be used to describe them.
    """
    Nucleic_acid_sites_features_and_motifs = "edam:topic_3511"
    """
    The biology, archival, detection, prediction and analysis of positional features such as functional and other key sites, in nucleic acid sequences and the conserved patterns (motifs, profiles etc.) that may be used to describe them.
    """
    Gene_transcripts = "edam:topic_3512"
    """
    Transcription of DNA into RNA and features of a messenger RNA (mRNA) molecules including precursor RNA, primary (unprocessed) transcript and fully processed molecules.
    """
    Genotyping_experiment = "edam:topic_3516"
    """
    Genotype experiment including case control, population, and family studies. These might use array based methods and re-sequencing methods.
    """
    GWAS_study = "edam:topic_3517"
    """
    Genome-wide association study experiments.
    """
    Microarray_experiment = "edam:topic_3518"
    """
    Microarray experiments including conditions, protocol, sample:data relationships etc.
    """
    PCR_experiment = "edam:topic_3519"
    """
    PCR experiments, e.g. quantitative real-time PCR.
    """
    Proteomics_experiment = "edam:topic_3520"
    """
    Proteomics experiments.
    """
    RNAi_experiment = "edam:topic_3523"
    """
    Experiment in which the expression of a specific gene is post-transcriptionally knocked down or silenced by means of a small RNA (sRNA) causing the degradation of the gene transcript (mRNA), and thus preventing the production of the corresponding protein.
    """
    Simulation_experiment = "edam:topic_3524"
    """
    Biological computational model experiments (simulation), for example the minimum information required in order to permit its correct interpretation and reproduction.
    """
    Protein_binding_sites = "edam:topic_3534"
    """
    Binding sites in proteins, including cleavage sites (for a proteolytic enzyme or agent), key residues involved in protein folding, catalytic residues (active site) of an enzyme, ligand-binding (non-catalytic) residues of a protein, such as sites that bind metal, prosthetic groups or lipids, RNA and DNA-binding proteins and binding sites etc.
    """
    Protein_disordered_structure = "edam:topic_3538"
    """
    Disordered structure in a protein.
    """
    Protein_secondary_structure = "edam:topic_3542"
    """
    Secondary structure (predicted or real) of a protein, including super-secondary structure.
    """
    Applied_mathematics = "edam:topic_3569"
    """
    The application of mathematics to specific problems in science, typically by the formulation and analysis of mathematical models.
    """
    Pure_mathematics = "edam:topic_3570"
    """
    The study of abstract mathematical concepts.
    """
    Data_governance = "edam:topic_3571"
    """
    Data governance is the control of data entry and maintenance to ensure the data meets defined standards, qualities, or constraints.
    """
    Data_quality_management = "edam:topic_3572"
    """
    The quality, integrity, and cleaning up of data.
    """
    Freshwater_biology = "edam:topic_3573"
    """
    The study of organisms in freshwater ecosystems.
    """
    Human_genetics = "edam:topic_3574"
    """
    The study of inheritance in human beings.
    """
    Tropical_medicine = "edam:topic_3575"
    """
    Health problems that are prevalent in tropical and subtropical regions.
    """
    Medical_biotechnology = "edam:topic_3576"
    """
    Biotechnology applied to the medical sciences and the development of medicines.
    """
    Personalised_medicine = "edam:topic_3577"
    """
    An approach to medicine whereby decisions, practices and are tailored to the individual patient based on their predicted response or risk of disease.
    """
    Immunoprecipitation_experiment = "edam:topic_3656"
    """
    Experimental techniques to purify a protein-DNA crosslinked complex. Usually sequencing follows e.g. in the techniques ChIP-chip, ChIP-seq and MeDIP-seq.
    """
    Whole_genome_sequencing = "edam:topic_3673"
    """
    Laboratory technique to sequence the complete DNA sequence of an organism's genome at a single time.
    """
    Methylated_DNA_immunoprecipitation = "edam:topic_3674"
    """
    Laboratory technique to sequence the methylated regions in DNA.
    """
    Exome_sequencing = "edam:topic_3676"
    """
    Laboratory technique to sequence all the protein-coding regions in a genome, i.e., the exome.
    """
    Experimental_design_and_studies = "edam:topic_3678"
    """
    The design of an experiment intended to test a hypothesis, and describe or explain empirical data obtained under various experimental conditions.
    """
    Animal_study = "edam:topic_3679"
    """
    The design of an experiment involving non-human animals.
    """
    Microbial_ecology = "edam:topic_3697"
    """
    The ecology of microorganisms including their relationship with one another and their environment.
    """
    RNA_immunoprecipitation = "edam:topic_3794"
    """
    An antibody-based technique used to map in vivo RNA-protein interactions.
    """
    Population_genomics = "edam:topic_3796"
    """
    Large-scale study (typically comparison) of DNA sequences of populations.
    """
    Agricultural_science = "edam:topic_3810"
    """
    Multidisciplinary study, research and development within the field of agriculture.
    """
    Metagenomic_sequencing = "edam:topic_3837"
    """
    Approach which samples, in parallel, all genes in all organisms present in a given sample, e.g. to provide insight into biodiversity and function.
    """
    Environmental_sciences = "edam:topic_3855"
    """
    Study of the environment, the interactions between its physical, chemical, and biological components and it's effect on life. Also how humans impact upon the environment, and how we can manage and utilise natural resources.
    """
    Biomolecular_simulation = "edam:topic_3892"
    """
    The study and simulation of molecular conformations using a computational model and computer simulations.
    """
    Synthetic_biology = "edam:topic_3895"
    """
    The application of multi-disciplinary science and technology for the construction of artificial biological systems for diverse applications.
    """
    Genetic_engineering = "edam:topic_3912"
    """
    The application of biotechnology to directly manipulate an organism's genes.
    """
    Proteogenomics = "edam:topic_3922"
    """
    A field of biological research focused on the discovery and identification of peptides, typically by comparing mass spectra against a protein database.
    """
    Genome_resequencing = "edam:topic_3923"
    """
    Laboratory experiment to identify the differences between a specific genome (of an individual) and a reference genome (developed typically from many thousands of individuals). WGS re-sequencing is used as golden standard to detect variations compared to a given reference genome, including small variants (SNP and InDels) as well as larger genome re-organisations (CNVs, translocations, etc.).
    """
    Immunogenetics = "edam:topic_3930"
    """
    A biomedical field that bridges immunology and genetics, to study the genetic basis of the immune system.
    """
    Chemometrics = "edam:topic_3931"
    """
    Interdisciplinary science focused on extracting information from chemical systems by data analytical approaches, for example multivariate statistics, applied mathematics, and computer science.
    """
    Cytometry = "edam:topic_3934"
    """
    Cytometry is the measurement of the characteristics of cells.
    """
    Metabolic_engineering = "edam:topic_3939"
    """
    Biotechnology approach that seeks to optimize cellular genetic and regulatory processes in order to increase the cells' production of a certain substance.
    """
    Chromosome_conformation_capture = "edam:topic_3940"
    """
    Molecular biology methods used to analyze the spatial organization of chromatin in a cell.
    """
    Metatranscriptomics = "edam:topic_3941"
    """
    The study of microbe gene expression within natural environments (i.e. the metatranscriptome).
    """
    Paleogenomics = "edam:topic_3943"
    """
    The reconstruction and analysis of genomic information in extinct species.
    """
    Cladistics = "edam:topic_3944"
    """
    The biological classification of organisms by categorizing them in groups ("clades") based on their most recent common ancestor.
    """
    Molecular_evolution = "edam:topic_3945"
    """
    The study of the process and mechanism of change of biomolecules such as DNA, RNA, and proteins across generations.
    """
    Immunoinformatics = "edam:topic_3948"
    """
    Immunoinformatics is the field of computational biology that deals with the study of immunoloogical questions. Immunoinformatics is at the interface between immunology and computer science. It takes advantage of computational, statistical, mathematical approaches and enhances the understanding of immunological knowledge.
    """
    Echography = "edam:topic_3954"
    """
    A diagnostic imaging technique based on the application of ultrasound.
    """
    Fluxomics = "edam:topic_3955"
    """
    Experimental approaches to determine the rates of metabolic reactions - the metabolic fluxes - within a biological entity.
    """
    Protein_interaction_experiment = "edam:topic_3957"
    """
    An experiment for studying protein-protein interactions.
    """
    Copy_number_variation = "edam:topic_3958"
    """
    A DNA structural variation, specifically a duplication or deletion event, resulting in sections of the genome to be repeated, or the number of repeats in the genome to vary between individuals.
    """
    Cytogenetics = "edam:topic_3959"
    """
    The branch of genetics concerned with the relationships between chromosomes and cellular behaviour, especially during mitosis and meiosis.
    """
    Vaccinology = "edam:topic_3966"
    """
    The design of vaccines to protect against a particular pathogen, including antigens, delivery systems, and adjuvants to elicit a predictable immune response against specific epitopes.
    """
    Immunomics = "edam:topic_3967"
    """
    The study of immune system as a whole, its regulation and response to pathogens using genome-wide approaches.
    """
    Epistasis = "edam:topic_3974"
    """
    Epistasis can be defined as the ability of the genotype at one locus to supersede the phenotypic effect of a mutation at another locus. This interaction between genes can occur at different level: gene expression, protein levels, etc...
    """
    Open_science = "edam:topic_4010"
    """
    Open science encompasses the practices of making scientific research transparent and participatory, and its outputs publicly accessible.
    """
    Data_rescue = "edam:topic_4011"
    """
    Data rescue denotes digitalisation, formatting, archival, and publication of data that were not available in accessible or usable form. Examples are data from private archives, data inside publications, or in paper records stored privately or publicly.
    """
    FAIR_data = "edam:topic_4012"
    """
    FAIR data is scientific data that meets the principles of being findable, accessible, interoperable, and reusable.
    """
    Antimicrobial_resistance = "edam:topic_4013"
    """
    Microbial mechanisms for protecting microorganisms against antimicrobial agents.
    """
    Electroencephalography = "edam:topic_4014"
    """
    The monitoring method for measuring electrical activity in the brain.
    """
    Electrocardiography = "edam:topic_4016"
    """
    The monitoring method for measuring electrical activity in the heart.
    """
    Cryogenic_electron_microscopy = "edam:topic_4017"
    """
    A method for studying biomolecules and other structures at very low (cryogenic) temperature using electron microscopy.
    """
    Biosciences = "edam:topic_4019"
    """
    Biosciences, or life sciences, include fields of study related to life, living beings, and biomolecules.
    """
    Carbon_cycle = "edam:topic_4020"
    """
    The carbon cycle is the biogeochemical pathway of carbon moving through the different parts of the Earth (such as ocean, atmosphere, soil), or eventually another planet.
    """
    Multiomics = "edam:topic_4021"
    """
    Multiomics concerns integration of data from multiple omics (e.g. transcriptomics, proteomics, epigenomics).
    """
    Ribosome_Profiling = "edam:topic_4027"
    """
    With ribosome profiling, ribosome-protected mRNA fragments are analyzed with RNA-seq techniques leading to a genome-wide measurement of the translation landscape.
    """
    Single_cell_sequencing = "edam:topic_4028"
    """
    Combined with NGS (Next Generation Sequencing) technologies, single-cell sequencing allows the study of genetic information (DNA, RNA, epigenome...) at a single cell level. It is often used for differential analysis and gene expression profiling.
    """
    Acoustics = "edam:topic_4029"
    """
    The study of mechanical waves in liquids, solids, and gases.
    """
    Microfluidics = "edam:topic_4030"
    """
    Interdisplinary study of behavior, precise control, and manipulation of low (microlitre) volume fluids in constrained space.
    """
    Genomic_imprinting = "edam:topic_4037"
    """
    Genomic imprinting is a gene regulation mechanism by which a subset of genes are expressed from one of the two parental chromosomes only. Imprinted genes are organized in clusters, their silencing/activation of the imprinted loci involves epigenetic marks (DNA methylation, etc) and so-called imprinting control regions (ICR). It has been described in mammals, but also plants and insects.
    """
    Metabarcoding = "edam:topic_4038"
    """
    Metabarcoding is the barcoding of (environmental) DNA or RNA to identify multiple taxa from the same sample.
    """
    Data_protection = "edam:topic_4044"
    """
    Data protection is a topic concerning data that should be protected from disclosure, damage, or unauthorised access, due to its sensitive nature.
    """
    Cybersecurity = "edam:topic_4045"
    """
    Cybersecurity is a topic comprising the approaches and technologies that enable the protection of computer systems, networks and programs from digital attacks. It ensures the availability, integrity, and confidentiality of processed and stored information.
    """
    Version_control = "edam:topic_4046"
    """
    Version control is a technology for consistent management, storing, and sharing of evolving versions of digital artefacts, such as computer programs, scripts, documents, data, or media files.
    """
    Software_management = "edam:topic_4047"
    """
    Software management comprises the practices and principles of taking care of software and software-based or software-like services, other than programming and maintenance. This includes for example taking care of the associated information and documentation, and the processes of contribution, validation, release/publication, or deployment.
    """
    ChIP_exo = "edam:topic_4051"
    """
    Chromatin immunoprecipitation-based exeperiment similar to ChIP-seq, with an additional experimental step using an exonuclease to increase the resolution of protein binding site identification.
    """
    Hi_C = "edam:topic_4052"
    """
    High-throughput genomic and epigenomic technique that capture chromatin conformation, allowing a genome-wide identification of chromatin interactions and structure.
    """
    ATAC_seq = "edam:topic_4053"
    """
    Assay for Transposase-Accessible Chromatin with high throughput sequencing. This technique is designed for the genome-wide detection of open chromatin regions.
    """
    miRNA_silencing = "edam:topic_4054"
    """
    Experiment in which the expression of a given gene is knocked down by means of a micro RNA (miRNA) causing the degradation of the gene transcript (mRNA).
    """
    siRNA_experiment = "edam:topic_4055"
    """
    Experiment in which the expression of a given gene is knocked down by means of a small interfering RNA (siRNA) causing the degradation of the gene transcript (mRNA).
    """
    Long_read_sequencing = "edam:topic_4056"
    """
    Long-read sequencing is a sequencing method that produces reads thousands to millions of base pairs long, allowing for better resolution of complex regions, structural variants, and full-length transcripts.
    """
    Short_read_sequencing = "edam:topic_4057"
    """
    Short-read sequencing is a high-throughput sequencing method that generates millions of short nucleotide fragments, typically 50–300 base pairs in length.
    """
    Metaproteomics = "edam:topic_4060"
    """
    Metaproteomics is the profiling of proteins in a sample that contains material from multiple species or strains of organisms.
    """
    Bisulfite_sequencing = "edam:topic_4061"
    """
    Bisulfite sequencing is a sequencing technique used to determine DNA methylation patterns by treating DNA with bisulfite, which converts unmethylated cytosines to uracils while leaving methylated cytosines unchanged.
    """
    Bulk_RNA_barcoding_and_sequencing = "edam:topic_4062"
    """
    Bulk RNA barcoding and sequencing (BRB-seq) is a highly mutliplexed bulk RNA-Seq technique where each RNA sample gets a barcode, and many samples are sequenced together.
    """
    DNase_sequencing = "edam:topic_4063"
    """
    DNase sequencing is a technique used to identify regions of open chromatin by sequencing DNA fragments generated after treatment with DNase I, which preferentially cuts accessible DNA.
    """
    MicroRNA_sequencing = "edam:topic_4064"
    """
    Specific sequencing of small RNAs using a variant of RNA-seq, with an additional fragment size selection step.
    """
    Exposomics = "edam:topic_4065"
    """
    Exposomics is the systematic and comprehensive study of the exposome and the associated biological responses (exposure-phenotype interaction). Exposome is the totality of environmental exposures, that is, the cumulative (e.g. life-long) totality of contacts between external factors (e.g. chemical agents) and a living organism, a population, or a biological taxon.
    """


class EnumDataSourceType(str, Enum):
    """
    Approaches to ascertain information about a participant.
    """
    Electronic_Health_Record = "CAMO:0000014"
    """
    Data obtained directly from an Electronic Health Record.
    """
    Survey = "CAMO:0000010"
    """
    Data obtained from a survey or questionnaire given to a participant or their representative.
    """
    Research_Assessment = "CAMO:0000011"
    """
    Data obtained by research staff for the study.
    """
    Interview = "CAMO:0000012"
    """
    Data obtained by research staff interviewing participants, representatives, or others.
    """
    Physical_Examination = "CAMO:0000013"
    """
    Data obtained directly by research staff examining the participant.
    """


class EnumDataUseModifier(str, Enum):
    """
    Data Use Ontology (DUO) terms for data use modifiers.
    """
    population_origins_or_ancestry_research_prohibited = "DUO:00000044"
    """
    This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited.
    """
    research_specific_restrictions = "DUO:0000012"
    """
    This data use modifier indicates that use is limited to studies of a certain research type.
    """
    no_general_methods_research = "DUO:0000015"
    """
    This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms).
    """
    genetic_studies_only = "DUO:0000016"
    """
    This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively)
    """
    not_for_profit_non_commercial_use_only = "DUO:0000018"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.
    """
    publication_required = "DUO:0000019"
    """
    This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community.
    """
    collaboration_required = "DUO:0000020"
    """
    This could be coupled with a string describing the primary study investigator(s).
    This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s).
    """
    ethics_approval_required = "DUO:0000021"
    """
    This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.
    """
    geographical_restriction = "DUO:0000022"
    """
    This data use modifier indicates that use is limited to within a specific geographic region.
    This should be coupled with an ontology term describing the geographical location the restriction applies to.
    """
    publication_moratorium = "DUO:0000024"
    """
    This data use modifier indicates that requestor agrees not to publish results of studies until a specific date.
    This should be coupled with a date specified as ISO8601
    """
    time_limit_on_use = "DUO:0000025"
    """
    This data use modifier indicates that use is approved for a specific number of months.
    This should be coupled with an integer value indicating the number of months.
    """
    user_specific_restriction = "DUO:0000026"
    """
    This data use modifier indicates that use is limited to use by approved users.
    """
    project_specific_restriction = "DUO:0000027"
    """
    This data use modifier indicates that use is limited to use within an approved project.
    """
    institution_specific_restriction = "DUO:0000028"
    """
    This data use modifier indicates that use is limited to use within an approved institution.
    """
    return_to_database_or_resource = "DUO:0000029"
    """
    This data use modifier indicates that the requestor must return derived/enriched data to the database/resource.
    """
    clinical_care_use = "DUO:0000043"
    """
    Clinical Care is defined as Health care or services provided at home, in a healthcare facility or hospital. Data may be used for clinical decision making.
    This data use modifier indicates that use is allowed for clinical use and care.
    """
    not_for_profit_organisation_use_only = "DUO:0000045"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit organizations.
    """
    non_commercial_use_only = "DUO:0000046"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit use.
    This indicates that data can be used by commercial organisations for research purposes, but not commercial purposes.
    """


class EnumDataUsePermission(str, Enum):
    """
    Data Use Ontology (DUO) terms for data use permissions.
    """
    no_restriction = "DUO:0000004"
    """
    This data use permission indicates there is no restriction on use.
    """
    health_or_medical_or_biomedical_research = "DUO:0000006"
    """
    This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry.
    """
    disease_specific_research = "DUO:0000007"
    """
    This data use permission indicates that use is allowed provided it is related to the specified disease.
    This term should be coupled with a term describing a disease from an ontology to specify the disease the restriction applies to. 

    DUO recommends MONDO be used, to provide the basis for automated evaluation. For more information see https://github.com/EBISPOT/DUO/blob/master/MONDO_Overview.md

    Other resources, such as the Disease Ontology, HPO, SNOMED-CT or others, can also be used. When those other resources are being used, this may require an extra mapping step to leverage automated matching algorithms.
    """
    population_origins_or_ancestry_research_only = "DUO:0000011"
    """
    This data use permission indicates that use of the data is limited to the study of population origins or ancestry.
    """
    general_research_use = "DUO:0000042"
    """
    This data use permission indicates that use is allowed for general research use for any research purpose.
    This includes but is not limited to: health/medical/biomedical purposes, fundamental biology research, the study of population origins or ancestry, statistical methods and algorithms development, and social-sciences research.
    """


class EnumEDAMDataTypes(str, Enum):
    """
    Data types from the EDAM ontology.
    """
    Ontology = "edam:data_0582"
    """
    An ontology of biological or bioinformatics concepts and relations, a controlled vocabulary, structured glossary etc.
    """
    Identifier = "edam:data_0842"
    """
    A text token, number or something else which identifies an entity, but which may not be persistent (stable) or unique (the same identifier may identify multiple things).
    """
    Molecular_mass = "edam:data_0844"
    """
    Mass of a molecule.
    """
    Molecular_charge = "edam:data_0845"
    """
    Net charge of a molecule.
    """
    Chemical_formula = "edam:data_0846"
    """
    A specification of a chemical structure.
    """
    QSAR_descriptor = "edam:data_0847"
    """
    A QSAR quantitative descriptor (name-value pair) of chemical structure.
    """
    Sequence_record = "edam:data_0849"
    """
    A molecular sequence and associated metadata.
    """
    Sequence_set = "edam:data_0850"
    """
    A collection of one or typically multiple molecular sequences (which can include derived data or metadata) that do not (typically) correspond to molecular sequence database records or entries and which (typically) are derived from some analytical method.
    """
    Sequence_feature_source = "edam:data_0856"
    """
    How the annotation of a sequence feature (for example in EMBL or Swiss-Prot) was derived.
    """
    Sequence_search_results = "edam:data_0857"
    """
    A report of sequence hits and associated data from searching a database of sequences (for example a BLAST search). This will typically include a list of scores (often with statistical evaluation) and a set of alignments for the hits.
    """
    Sequence_signature_matches = "edam:data_0858"
    """
    Report on the location of matches ("hits") between sequences, sequence profiles, motifs (conserved or functional patterns) and other types of sequence signatures.
    """
    Sequence_signature_data = "edam:data_0860"
    """
    Sequence signature data concerns specific or conserved pattern in molecular sequences and the classifiers used for their identification, including sequence motifs, profiles or other diagnostic element.
    """
    Dotplot = "edam:data_0862"
    """
    A dotplot of sequence similarities identified from word-matching or character comparison.
    """
    Sequence_alignment = "edam:data_0863"
    """
    Alignment of multiple molecular sequences.
    """
    Sequence_similarity_score = "edam:data_0865"
    """
    A value representing molecular sequence similarity.
    """
    Sequence_alignment_report = "edam:data_0867"
    """
    An informative report of molecular sequence alignment-derived data or metadata.
    """
    Sequence_distance_matrix = "edam:data_0870"
    """
    A matrix of estimated evolutionary distance between molecular sequences, such as is suitable for phylogenetic tree calculation.
    """
    Phylogenetic_character_data = "edam:data_0871"
    """
    Basic character data from which a phylogenetic tree may be generated.
    """
    Phylogenetic_tree = "edam:data_0872"
    """
    The raw data (not just an image) from which a phylogenetic tree is directly generated or plotted, such as topology, lengths (in time or in expected amounts of variance) and a confidence interval for each length.
    """
    Comparison_matrix = "edam:data_0874"
    """
    Matrix of integer or floating point numbers for amino acid or nucleotide sequence comparison.
    """
    Protein_secondary_structure_alignment = "edam:data_0878"
    """
    Alignment of the (1D representations of) secondary structure of two or more proteins.
    """
    RNA_secondary_structure = "edam:data_0880"
    """
    An informative report of secondary structure (predicted or real) of an RNA molecule.
    """
    RNA_secondary_structure_alignment = "edam:data_0881"
    """
    Alignment of the (1D representations of) secondary structure of two or more RNA molecules.
    """
    Structure = "edam:data_0883"
    """
    3D coordinate and associated data for a macromolecular tertiary (3D) structure or part of a structure.
    """
    Structure_alignment = "edam:data_0886"
    """
    Alignment (superimposition) of molecular tertiary (3D) structures.
    """
    Structure_alignment_report = "edam:data_0887"
    """
    An informative report of molecular tertiary structure alignment-derived data.
    """
    Structure_similarity_score = "edam:data_0888"
    """
    A value representing molecular structure similarity, measured from structure alignment or some other type of structure comparison.
    """
    Structural_profile = "edam:data_0889"
    """
    Some type of structural (3D) profile or template (representing a structure or structure alignment).
    """
    Structural_LEFT_PARENTHESIS3DRIGHT_PARENTHESIS_profile_alignment = "edam:data_0890"
    """
    A 3D profile-3D profile alignment (each profile representing structures or a structure alignment).
    """
    Protein_sequence_structure_scoring_matrix = "edam:data_0892"
    """
    Matrix of values used for scoring sequence-structure compatibility.
    """
    Sequence_structure_alignment = "edam:data_0893"
    """
    An alignment of molecular sequence to structure (from threading sequence(s) through 3D structure or representation of structure(s)).
    """
    Protein_report = "edam:data_0896"
    """
    An informative human-readable report about one or more specific protein molecules or protein structural domains, derived from analysis of primary (sequence or structural) data.
    """
    Protein_property = "edam:data_0897"
    """
    A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a protein molecule or model.
    """
    Protein_interaction_raw_data = "edam:data_0905"
    """
    Protein-protein interaction data from for example yeast two-hybrid analysis, protein microarrays, immunoaffinity chromatography followed by mass spectrometry, phage display etc.
    """
    Protein_interaction_data = "edam:data_0906"
    """
    Data concerning the interactions (predicted or known) within or between a protein, structural domain or part of a protein. This includes intra- and inter-residue contacts and distances, as well as interactions with other proteins and non-protein entities such as nucleic acid, metal atoms, water, ions etc.
    """
    Protein_family_report = "edam:data_0907"
    """
    An informative report on a specific protein family or other classification or group of protein sequences or structures.
    """
    Vmax = "edam:data_0909"
    """
    The maximum initial velocity or rate of a reaction. It is the limiting velocity as substrate concentrations get very large.
    """
    Km = "edam:data_0910"
    """
    Km is the concentration (usually in Molar units) of substrate that leads to half-maximal velocity of an enzyme-catalysed reaction.
    """
    Nucleic_acid_property = "edam:data_0912"
    """
    A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a nucleic acid molecule.
    """
    Codon_usage_data = "edam:data_0914"
    """
    Data derived from analysis of codon usage (typically a codon usage table) of DNA sequences.
    """
    Gene_report = "edam:data_0916"
    """
    A report on predicted or actual gene structure, regions which make an RNA product and features such as promoters, coding regions, splice sites etc.
    """
    Chromosome_report = "edam:data_0919"
    """
    A human-readable collection of information about a specific chromosome.
    """
    GenotypeSOLIDUSphenotype_report = "edam:data_0920"
    """
    A human-readable collection of information about the set of genes (or allelic forms) present in an individual, organism or cell and associated with a specific physical characteristic, or a report concerning an organisms traits and phenotypes.
    """
    Sequence_trace = "edam:data_0924"
    """
    Fluorescence trace data generated by an automated DNA sequencer, which can be interpreted as a molecular sequence (reads), given associated sequencing metadata such as base-call quality scores.
    """
    Sequence_assembly = "edam:data_0925"
    """
    An assembly of fragments of a (typically genomic) DNA sequence.
    """
    RH_scores = "edam:data_0926"
    """
    Radiation hybrid scores (RH) scores for one or more markers.
    """
    Genetic_linkage_report = "edam:data_0927"
    """
    A human-readable collection of information about the linkage of alleles.
    """
    Gene_expression_profile = "edam:data_0928"
    """
    Data quantifying the level of expression of (typically) multiple genes, derived for example from microarray experiments.
    """
    Electron_density_map = "edam:data_0937"
    """
    X-ray crystallography data.
    """
    Raw_NMR_data = "edam:data_0938"
    """
    Nuclear magnetic resonance (NMR) raw data, typically for a protein.
    """
    CD_spectra = "edam:data_0939"
    """
    Protein secondary structure from protein coordinate or circular dichroism (CD) spectroscopic data.
    """
    Volume_map = "edam:data_0940"
    """
    Volume map data from electron microscopy.
    """
    number_2D_PAGE_image = "edam:data_0942"
    """
    Two-dimensional gel electrophoresis image.
    """
    Mass_spectrum = "edam:data_0943"
    """
    Spectra from mass spectrometry.
    """
    Peptide_mass_fingerprint = "edam:data_0944"
    """
    A set of peptide masses (peptide mass fingerprint) from mass spectrometry.
    """
    Peptide_identification = "edam:data_0945"
    """
    Protein or peptide identifications with evidence supporting the identifications, for example from comparing a peptide mass fingerprint (from mass spectrometry) to a sequence database, or the set of typical spectra one obtains when running a protein through a mass spectrometer.
    """
    Workflow_metadata = "edam:data_0949"
    """
    Basic information, annotation or documentation concerning a workflow (but not the workflow itself).
    """
    Mathematical_model = "edam:data_0950"
    """
    A biological model represented in mathematical terms.
    """
    Statistical_estimate_score = "edam:data_0951"
    """
    A value representing estimated statistical significance of some observed data; typically sequence database hits.
    """
    Database_cross_mapping = "edam:data_0954"
    """
    A mapping of the accession numbers (or other database identifier) of entries between (typically) two biological or biomedical databases.
    """
    Data_index = "edam:data_0955"
    """
    An index of data of biological relevance.
    """
    Data_index_report = "edam:data_0956"
    """
    A human-readable collection of information concerning an analysis of an index of biological data.
    """
    Database_metadata = "edam:data_0957"
    """
    Basic information on bioinformatics database(s) or other data sources such as name, type, description, URL etc.
    """
    Tool_metadata = "edam:data_0958"
    """
    Basic information about one or more bioinformatics applications or packages, such as name, type, description, or other documentation.
    """
    User_metadata = "edam:data_0960"
    """
    Textual metadata on a software author or end-user, for example a person or other software.
    """
    Small_molecule_report = "edam:data_0962"
    """
    A human-readable collection of information about a specific chemical compound.
    """
    Cell_line_report = "edam:data_0963"
    """
    A human-readable collection of information about a particular strain of organism cell line including plants, virus, fungi and bacteria. The data typically includes strain number, organism type, growth conditions, source and so on.
    """
    Ontology_term = "edam:data_0966"
    """
    A term (name) from an ontology.
    """
    Ontology_concept_data = "edam:data_0967"
    """
    Data concerning or derived from a concept from a biological ontology.
    """
    Keyword = "edam:data_0968"
    """
    Keyword(s) or phrase(s) used (typically) for text-searching purposes.
    """
    Citation = "edam:data_0970"
    """
    Bibliographic data that uniquely identifies a scientific article, book or other published material.
    """
    Article = "edam:data_0971"
    """
    A scientific text, typically a full text article from a scientific journal.
    """
    Text_mining_report = "edam:data_0972"
    """
    A human-readable collection of information resulting from text mining.
    """
    Identifier_LEFT_PARENTHESISby_type_of_entityRIGHT_PARENTHESIS = "edam:data_0976"
    """
    An identifier that identifies a particular type of data.
    """
    Tool_identifier = "edam:data_0977"
    """
    An identifier of a bioinformatics tool, e.g. an application or web service.
    """
    Molecule_identifier = "edam:data_0982"
    """
    Name or other identifier of a molecule.
    """
    Atom_ID = "edam:data_0983"
    """
    Identifier (e.g. character symbol) of a specific atom.
    """
    Molecule_name = "edam:data_0984"
    """
    Name of a specific molecule.
    """
    Chromosome_name = "edam:data_0987"
    """
    Name of a chromosome.
    """
    Peptide_identifier = "edam:data_0988"
    """
    Identifier of a peptide chain.
    """
    Protein_identifier = "edam:data_0989"
    """
    Identifier of a protein.
    """
    Compound_name = "edam:data_0990"
    """
    Unique name of a chemical compound.
    """
    Chemical_registry_number = "edam:data_0991"
    """
    Unique registry number of a chemical compound.
    """
    Drug_identifier = "edam:data_0993"
    """
    Identifier of a drug.
    """
    Amino_acid_identifier = "edam:data_0994"
    """
    Identifier of an amino acid.
    """
    Nucleotide_identifier = "edam:data_0995"
    """
    Name or other identifier of a nucleotide.
    """
    Monosaccharide_identifier = "edam:data_0996"
    """
    Identifier of a monosaccharide.
    """
    Chemical_name_LEFT_PARENTHESISChEBIRIGHT_PARENTHESIS = "edam:data_0997"
    """
    Unique name from Chemical Entities of Biological Interest (ChEBI) of a chemical compound.
    """
    Chemical_name_LEFT_PARENTHESISIUPACRIGHT_PARENTHESIS = "edam:data_0998"
    """
    IUPAC recommended name of a chemical compound.
    """
    Chemical_name_LEFT_PARENTHESISINNRIGHT_PARENTHESIS = "edam:data_0999"
    """
    International Non-proprietary Name (INN or 'generic name') of a chemical compound, assigned by the World Health Organisation (WHO).
    """
    Chemical_name_LEFT_PARENTHESISbrandRIGHT_PARENTHESIS = "edam:data_1000"
    """
    Brand name of a chemical compound.
    """
    Chemical_name_LEFT_PARENTHESISsynonymousRIGHT_PARENTHESIS = "edam:data_1001"
    """
    Synonymous name of a chemical compound.
    """
    CAS_number = "edam:data_1002"
    """
    CAS registry number of a chemical compound; a unique numerical identifier of chemicals in the scientific literature, as assigned by the Chemical Abstracts Service.
    """
    Chemical_registry_number_LEFT_PARENTHESISBeilsteinRIGHT_PARENTHESIS = "edam:data_1003"
    """
    Beilstein registry number of a chemical compound.
    """
    Chemical_registry_number_LEFT_PARENTHESISGmelinRIGHT_PARENTHESIS = "edam:data_1004"
    """
    Gmelin registry number of a chemical compound.
    """
    HET_group_name = "edam:data_1005"
    """
    3-letter code word for a ligand (HET group) from a PDB file, for example ATP.
    """
    Amino_acid_name = "edam:data_1006"
    """
    String of one or more ASCII characters representing an amino acid.
    """
    Nucleotide_code = "edam:data_1007"
    """
    String of one or more ASCII characters representing a nucleotide.
    """
    Polypeptide_chain_ID = "edam:data_1008"
    """
    Identifier of a polypeptide chain from a protein.
    """
    Protein_name = "edam:data_1009"
    """
    Name of a protein.
    """
    Enzyme_identifier = "edam:data_1010"
    """
    Name or other identifier of an enzyme or record from a database of enzymes.
    """
    EC_number = "edam:data_1011"
    """
    An Enzyme Commission (EC) number of an enzyme.
    """
    Enzyme_name = "edam:data_1012"
    """
    Name of an enzyme.
    """
    Restriction_enzyme_name = "edam:data_1013"
    """
    Name of a restriction enzyme.
    """
    Sequence_feature_ID = "edam:data_1015"
    """
    A unique identifier of molecular sequence feature, for example an ID of a feature that is unique within the scope of the GFF file.
    """
    Sequence_position = "edam:data_1016"
    """
    A position of one or more points (base or residue) in a sequence, or part of such a specification.
    """
    Sequence_range = "edam:data_1017"
    """
    Specification of range(s) of sequence positions.
    """
    Sequence_feature_key = "edam:data_1020"
    """
    The type of a sequence feature, typically a term or accession from the Sequence Ontology, for example an EMBL or Swiss-Prot sequence feature key.
    """
    Sequence_feature_qualifier = "edam:data_1021"
    """
    Typically one of the EMBL or Swiss-Prot feature qualifiers.
    """
    Sequence_feature_label = "edam:data_1022"
    """
    A name of a sequence feature, e.g. the name of a feature to be displayed to an end-user. Typically an EMBL or Swiss-Prot feature label.
    """
    EMBOSS_Uniform_Feature_Object = "edam:data_1023"
    """
    The name of a sequence feature-containing entity adhering to the standard feature naming scheme used by all EMBOSS applications.
    """
    Gene_identifier = "edam:data_1025"
    """
    An identifier of a gene, such as a name/symbol or a unique identifier of a gene in a database.
    """
    Gene_symbol = "edam:data_1026"
    """
    The short name of a gene; a single word that does not contain white space characters. It is typically derived from the gene name.
    """
    Gene_ID_LEFT_PARENTHESISNCBIRIGHT_PARENTHESIS = "edam:data_1027"
    """
    An NCBI unique identifier of a gene.
    """
    Gene_ID_LEFT_PARENTHESISCGDRIGHT_PARENTHESIS = "edam:data_1031"
    """
    Identifier of a gene or feature from the CGD database.
    """
    Gene_ID_LEFT_PARENTHESISDictyBaseRIGHT_PARENTHESIS = "edam:data_1032"
    """
    Identifier of a gene from DictyBase.
    """
    Ensembl_gene_ID = "edam:data_1033"
    """
    Unique identifier for a gene (or other feature) from the Ensembl database.
    """
    Gene_ID_LEFT_PARENTHESISSGDRIGHT_PARENTHESIS = "edam:data_1034"
    """
    Identifier of an entry from the SGD database.
    """
    Gene_ID_LEFT_PARENTHESISGeneDBRIGHT_PARENTHESIS = "edam:data_1035"
    """
    Identifier of a gene from the GeneDB database.
    """
    TIGR_identifier = "edam:data_1036"
    """
    Identifier of an entry from the TIGR database.
    """
    TAIR_accession_LEFT_PARENTHESISgeneRIGHT_PARENTHESIS = "edam:data_1037"
    """
    Identifier of an gene from the TAIR database.
    """
    Protein_domain_ID = "edam:data_1038"
    """
    Identifier of a protein structural domain.
    """
    SCOP_domain_identifier = "edam:data_1039"
    """
    Identifier of a protein domain (or other node) from the SCOP database.
    """
    CATH_domain_ID = "edam:data_1040"
    """
    Identifier of a protein domain from CATH.
    """
    SCOP_concise_classification_string_LEFT_PARENTHESISsccsRIGHT_PARENTHESIS = "edam:data_1041"
    """
    A SCOP concise classification string (sccs) is a compact representation of a SCOP domain classification.
    """
    SCOP_sunid = "edam:data_1042"
    """
    Unique identifier (number) of an entry in the SCOP hierarchy, for example 33229.
    """
    CATH_node_ID = "edam:data_1043"
    """
    A code number identifying a node from the CATH database.
    """
    Kingdom_name = "edam:data_1044"
    """
    The name of a biological kingdom (Bacteria, Archaea, or Eukaryotes).
    """
    Species_name = "edam:data_1045"
    """
    The name of a species (typically a taxonomic group) of organism.
    """
    Strain_name = "edam:data_1046"
    """
    The name of a strain of an organism variant, typically a plant, virus or bacterium.
    """
    URI = "edam:data_1047"
    """
    A string of characters that name or otherwise identify a resource on the Internet.
    """
    Database_ID = "edam:data_1048"
    """
    An identifier of a biological or bioinformatics database.
    """
    Directory_name = "edam:data_1049"
    """
    The name of a directory.
    """
    File_name = "edam:data_1050"
    """
    The name (or part of a name) of a file (of any type).
    """
    Ontology_name = "edam:data_1051"
    """
    Name of an ontology of biological or bioinformatics concepts and relations.
    """
    URL = "edam:data_1052"
    """
    A Uniform Resource Locator (URL).
    """
    URN = "edam:data_1053"
    """
    A Uniform Resource Name (URN).
    """
    LSID = "edam:data_1055"
    """
    A Life Science Identifier (LSID) - a unique identifier of some data.
    """
    Database_name = "edam:data_1056"
    """
    The name of a biological or bioinformatics database.
    """
    Enumerated_file_name = "edam:data_1058"
    """
    The name of a file (of any type) with restricted possible values.
    """
    File_name_extension = "edam:data_1059"
    """
    The extension of a file name.
    """
    File_base_name = "edam:data_1060"
    """
    The base name of a file.
    """
    QSAR_descriptor_name = "edam:data_1061"
    """
    Name of a QSAR descriptor.
    """
    Sequence_identifier = "edam:data_1063"
    """
    An identifier of molecular sequence(s) or entries from a molecular sequence database.
    """
    Sequence_set_ID = "edam:data_1064"
    """
    An identifier of a set of molecular sequence(s).
    """
    Sequence_alignment_ID = "edam:data_1066"
    """
    Identifier of a molecular sequence alignment, for example a record from an alignment database.
    """
    Phylogenetic_tree_ID = "edam:data_1068"
    """
    Identifier of a phylogenetic tree for example from a phylogenetic tree database.
    """
    Comparison_matrix_identifier = "edam:data_1069"
    """
    An identifier of a comparison matrix.
    """
    Structure_ID = "edam:data_1070"
    """
    A unique and persistent identifier of a molecular tertiary structure, typically an entry from a structure database.
    """
    Structural_LEFT_PARENTHESIS3DRIGHT_PARENTHESIS_profile_ID = "edam:data_1071"
    """
    Identifier or name of a structural (3D) profile or template (representing a structure or structure alignment).
    """
    Structure_alignment_ID = "edam:data_1072"
    """
    Identifier of an entry from a database of tertiary structure alignments.
    """
    Amino_acid_index_ID = "edam:data_1073"
    """
    Identifier of an index of amino acid physicochemical and biochemical property data.
    """
    Protein_interaction_ID = "edam:data_1074"
    """
    Identifier of a report of protein interactions from a protein interaction database (typically).
    """
    Protein_family_identifier = "edam:data_1075"
    """
    Identifier of a protein family.
    """
    Codon_usage_table_name = "edam:data_1076"
    """
    Unique name of a codon usage table.
    """
    Transcription_factor_identifier = "edam:data_1077"
    """
    Identifier of a transcription factor (or a TF binding site).
    """
    Experiment_annotation_ID = "edam:data_1078"
    """
    Identifier of an entry from a database of microarray data.
    """
    Electron_microscopy_model_ID = "edam:data_1079"
    """
    Identifier of an entry from a database of electron microscopy data.
    """
    Gene_expression_report_ID = "edam:data_1080"
    """
    Accession of a report of gene expression (e.g. a gene expression profile) from a database.
    """
    Genotype_and_phenotype_annotation_ID = "edam:data_1081"
    """
    Identifier of an entry from a database of genotypes and phenotypes.
    """
    Pathway_or_network_identifier = "edam:data_1082"
    """
    Identifier of an entry from a database of biological pathways or networks.
    """
    Workflow_ID = "edam:data_1083"
    """
    Identifier of a biological or biomedical workflow, typically from a database of workflows.
    """
    Data_resource_definition_ID = "edam:data_1084"
    """
    Identifier of a data type definition from some provider.
    """
    Biological_model_ID = "edam:data_1085"
    """
    Identifier of a mathematical model, typically an entry from a database.
    """
    Compound_identifier = "edam:data_1086"
    """
    Identifier of an entry from a database of chemicals.
    """
    Ontology_concept_ID = "edam:data_1087"
    """
    A unique (typically numerical) identifier of a concept in an ontology of biological or bioinformatics concepts and relations.
    """
    Article_ID = "edam:data_1088"
    """
    Unique identifier of a scientific article.
    """
    FlyBase_ID = "edam:data_1089"
    """
    Identifier of an object from the FlyBase database.
    """
    WormBase_name = "edam:data_1091"
    """
    Name of an object from the WormBase database, usually a human-readable name.
    """
    WormBase_class = "edam:data_1092"
    """
    Class of an object from the WormBase database.
    """
    Sequence_accession = "edam:data_1093"
    """
    A persistent, unique identifier of a molecular sequence database entry.
    """
    EMBOSS_Uniform_Sequence_Address = "edam:data_1095"
    """
    The name of a sequence-based entity adhering to the standard sequence naming scheme used by all EMBOSS applications.
    """
    Sequence_accession_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:data_1096"
    """
    Accession number of a protein sequence database entry.
    """
    Sequence_accession_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "edam:data_1097"
    """
    Accession number of a nucleotide sequence database entry.
    """
    RefSeq_accession = "edam:data_1098"
    """
    Accession number of a RefSeq database entry.
    """
    PIR_identifier = "edam:data_1100"
    """
    An identifier of PIR sequence database entry.
    """
    Gramene_primary_identifier = "edam:data_1102"
    """
    Primary identifier of a Gramene database entry.
    """
    EMBLSOLIDUSGenBankSOLIDUSDDBJ_ID = "edam:data_1103"
    """
    Identifier of a (nucleic acid) entry from the EMBL/GenBank/DDBJ databases.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniGeneRIGHT_PARENTHESIS = "edam:data_1104"
    """
    A unique identifier of an entry (gene cluster) from the NCBI UniGene database.
    """
    dbEST_accession = "edam:data_1105"
    """
    Identifier of a dbEST database entry.
    """
    dbSNP_ID = "edam:data_1106"
    """
    Identifier of a dbSNP database entry.
    """
    Sequence_cluster_ID = "edam:data_1112"
    """
    An identifier of a cluster of molecular sequence(s).
    """
    Sequence_cluster_ID_LEFT_PARENTHESISCOGRIGHT_PARENTHESIS = "edam:data_1113"
    """
    Unique identifier of an entry from the COG database.
    """
    Sequence_motif_identifier = "edam:data_1114"
    """
    Identifier of a sequence motif, for example an entry from a motif database.
    """
    Sequence_profile_ID = "edam:data_1115"
    """
    Identifier of a sequence profile.
    """
    ELM_ID = "edam:data_1116"
    """
    Identifier of an entry from the ELMdb database of protein functional sites.
    """
    Prosite_accession_number = "edam:data_1117"
    """
    Accession number of an entry from the Prosite database.
    """
    HMMER_hidden_Markov_model_ID = "edam:data_1118"
    """
    Unique identifier or name of a HMMER hidden Markov model.
    """
    JASPAR_profile_ID = "edam:data_1119"
    """
    Unique identifier or name of a profile from the JASPAR database.
    """
    TreeBASE_study_accession_number = "edam:data_1123"
    """
    Accession number of an entry from the TreeBASE database.
    """
    TreeFam_accession_number = "edam:data_1124"
    """
    Accession number of an entry from the TreeFam database.
    """
    Comparison_matrix_name = "edam:data_1126"
    """
    Unique name or identifier of a comparison matrix.
    """
    PDB_ID = "edam:data_1127"
    """
    An identifier of an entry from the PDB database.
    """
    AAindex_ID = "edam:data_1128"
    """
    Identifier of an entry from the AAindex database.
    """
    BIND_accession_number = "edam:data_1129"
    """
    Accession number of an entry from the BIND database.
    """
    IntAct_accession_number = "edam:data_1130"
    """
    Accession number of an entry from the IntAct database.
    """
    Protein_family_name = "edam:data_1131"
    """
    Name of a protein family.
    """
    InterPro_entry_name = "edam:data_1132"
    """
    Name of an InterPro entry, usually indicating the type of protein matches for that entry.
    """
    InterPro_accession = "edam:data_1133"
    """
    Primary accession number of an InterPro entry.
    """
    InterPro_secondary_accession = "edam:data_1134"
    """
    Secondary accession number of an InterPro entry.
    """
    Gene3D_ID = "edam:data_1135"
    """
    Unique identifier of an entry from the Gene3D database.
    """
    PIRSF_ID = "edam:data_1136"
    """
    Unique identifier of an entry from the PIRSF database.
    """
    PRINTS_code = "edam:data_1137"
    """
    The unique identifier of an entry in the PRINTS database.
    """
    Pfam_accession_number = "edam:data_1138"
    """
    Accession number of a Pfam entry.
    """
    SMART_accession_number = "edam:data_1139"
    """
    Accession number of an entry from the SMART database.
    """
    Superfamily_hidden_Markov_model_number = "edam:data_1140"
    """
    Unique identifier (number) of a hidden Markov model from the Superfamily database.
    """
    TIGRFam_ID = "edam:data_1141"
    """
    Accession number of an entry (family) from the TIGRFam database.
    """
    ProDom_accession_number = "edam:data_1142"
    """
    A ProDom domain family accession number.
    """
    TRANSFAC_accession_number = "edam:data_1143"
    """
    Identifier of an entry from the TRANSFAC database.
    """
    ArrayExpress_accession_number = "edam:data_1144"
    """
    Accession number of an entry from the ArrayExpress database.
    """
    PRIDE_experiment_accession_number = "edam:data_1145"
    """
    PRIDE experiment accession number.
    """
    EMDB_ID = "edam:data_1146"
    """
    Identifier of an entry from the EMDB electron microscopy database.
    """
    GEO_accession_number = "edam:data_1147"
    """
    Accession number of an entry from the GEO database.
    """
    GermOnline_ID = "edam:data_1148"
    """
    Identifier of an entry from the GermOnline database.
    """
    EMAGE_ID = "edam:data_1149"
    """
    Identifier of an entry from the EMAGE database.
    """
    Disease_ID = "edam:data_1150"
    """
    Accession number of an entry from a database of disease.
    """
    HGVbase_ID = "edam:data_1151"
    """
    Identifier of an entry from the HGVbase database.
    """
    OMIM_ID = "edam:data_1153"
    """
    Identifier of an entry from the OMIM database.
    """
    KEGG_object_identifier = "edam:data_1154"
    """
    Unique identifier of an object from one of the KEGG databases (excluding the GENES division).
    """
    Pathway_ID_LEFT_PARENTHESISreactomeRIGHT_PARENTHESIS = "edam:data_1155"
    """
    Identifier of an entry from the Reactome database.
    """
    Pathway_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "edam:data_1157"
    """
    Identifier of an pathway from the BioCyc biological pathways database.
    """
    Pathway_ID_LEFT_PARENTHESISINOHRIGHT_PARENTHESIS = "edam:data_1158"
    """
    Identifier of an entry from the INOH database.
    """
    Pathway_ID_LEFT_PARENTHESISPATIKARIGHT_PARENTHESIS = "edam:data_1159"
    """
    Identifier of an entry from the PATIKA database.
    """
    Pathway_ID_LEFT_PARENTHESISCPDBRIGHT_PARENTHESIS = "edam:data_1160"
    """
    Identifier of an entry from the CPDB (ConsensusPathDB) biological pathways database, which is an identifier from an external database integrated into CPDB.
    """
    Pathway_ID_LEFT_PARENTHESISPantherRIGHT_PARENTHESIS = "edam:data_1161"
    """
    Identifier of a biological pathway from the Panther Pathways database.
    """
    MIRIAM_identifier = "edam:data_1162"
    """
    Unique identifier of a MIRIAM data resource.
    """
    MIRIAM_data_type_name = "edam:data_1163"
    """
    The name of a data type from the MIRIAM database.
    """
    MIRIAM_URI = "edam:data_1164"
    """
    The URI (URL or URN) of a data entity from the MIRIAM database.
    """
    MIRIAM_data_type_primary_name = "edam:data_1165"
    """
    The primary name of a data type from the MIRIAM database.
    """
    MIRIAM_data_type_synonymous_name = "edam:data_1166"
    """
    A synonymous name of a data type from the MIRIAM database.
    """
    Taverna_workflow_ID = "edam:data_1167"
    """
    Unique identifier of a Taverna workflow.
    """
    Biological_model_name = "edam:data_1170"
    """
    Name of a biological (mathematical) model.
    """
    BioModel_ID = "edam:data_1171"
    """
    Unique identifier of an entry from the BioModel database.
    """
    PubChem_CID = "edam:data_1172"
    """
    Chemical structure specified in PubChem Compound Identification (CID), a non-zero integer identifier for a unique chemical structure.
    """
    ChemSpider_ID = "edam:data_1173"
    """
    Identifier of an entry from the ChemSpider database.
    """
    ChEBI_ID = "edam:data_1174"
    """
    Identifier of an entry from the ChEBI database.
    """
    BioPax_concept_ID = "edam:data_1175"
    """
    An identifier of a concept from the BioPax ontology.
    """
    GO_concept_ID = "edam:data_1176"
    """
    An identifier of a concept from The Gene Ontology.
    """
    MeSH_concept_ID = "edam:data_1177"
    """
    An identifier of a concept from the MeSH vocabulary.
    """
    HGNC_concept_ID = "edam:data_1178"
    """
    An identifier of a concept from the HGNC controlled vocabulary.
    """
    NCBI_taxonomy_ID = "edam:data_1179"
    """
    A stable unique identifier for each taxon (for a species, a family, an order, or any other group in the NCBI taxonomy database.
    """
    Plant_Ontology_concept_ID = "edam:data_1180"
    """
    An identifier of a concept from the Plant Ontology (PO).
    """
    UMLS_concept_ID = "edam:data_1181"
    """
    An identifier of a concept from the UMLS vocabulary.
    """
    FMA_concept_ID = "edam:data_1182"
    """
    An identifier of a concept from Foundational Model of Anatomy.
    """
    EMAP_concept_ID = "edam:data_1183"
    """
    An identifier of a concept from the EMAP mouse ontology.
    """
    ChEBI_concept_ID = "edam:data_1184"
    """
    An identifier of a concept from the ChEBI ontology.
    """
    MGED_concept_ID = "edam:data_1185"
    """
    An identifier of a concept from the MGED ontology.
    """
    myGrid_concept_ID = "edam:data_1186"
    """
    An identifier of a concept from the myGrid ontology.
    """
    PubMed_ID = "edam:data_1187"
    """
    PubMed unique identifier of an article.
    """
    DOI = "edam:data_1188"
    """
    Digital Object Identifier (DOI) of a published article.
    """
    Medline_UI = "edam:data_1189"
    """
    Medline UI (unique identifier) of an article.
    """
    Tool_name = "edam:data_1190"
    """
    The name of a computer package, application, method or function.
    """
    Tool_name_LEFT_PARENTHESISsignatureRIGHT_PARENTHESIS = "edam:data_1191"
    """
    The unique name of a signature (sequence classifier) method.
    """
    Tool_name_LEFT_PARENTHESISBLASTRIGHT_PARENTHESIS = "edam:data_1192"
    """
    The name of a BLAST tool.
    """
    Tool_name_LEFT_PARENTHESISFASTARIGHT_PARENTHESIS = "edam:data_1193"
    """
    The name of a FASTA tool.
    """
    Tool_name_LEFT_PARENTHESISEMBOSSRIGHT_PARENTHESIS = "edam:data_1194"
    """
    The name of an EMBOSS application.
    """
    Tool_name_LEFT_PARENTHESISEMBASSY_packageRIGHT_PARENTHESIS = "edam:data_1195"
    """
    The name of an EMBASSY package.
    """
    QSAR_descriptor_LEFT_PARENTHESISconstitutionalRIGHT_PARENTHESIS = "edam:data_1201"
    """
    A QSAR constitutional descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESISelectronicRIGHT_PARENTHESIS = "edam:data_1202"
    """
    A QSAR electronic descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESISgeometricalRIGHT_PARENTHESIS = "edam:data_1203"
    """
    A QSAR geometrical descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESIStopologicalRIGHT_PARENTHESIS = "edam:data_1204"
    """
    A QSAR topological descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESISmolecularRIGHT_PARENTHESIS = "edam:data_1205"
    """
    A QSAR molecular descriptor.
    """
    Sequence_set_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:data_1233"
    """
    Any collection of multiple protein sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries.
    """
    Sequence_set_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "edam:data_1234"
    """
    Any collection of multiple nucleotide sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries.
    """
    Sequence_cluster = "edam:data_1235"
    """
    A set of sequences that have been clustered or otherwise classified as belonging to a group including (typically) sequence cluster information.
    """
    Proteolytic_digest = "edam:data_1238"
    """
    A protein sequence cleaved into peptide fragments (by enzymatic or chemical cleavage) with fragment masses.
    """
    Restriction_digest = "edam:data_1239"
    """
    Restriction digest fragments from digesting a nucleotide sequence with restriction sites using a restriction endonuclease.
    """
    PCR_primers = "edam:data_1240"
    """
    Oligonucleotide primer(s) for PCR and DNA amplification, for example a minimal primer set.
    """
    Sequence_cluster_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:data_1245"
    """
    A cluster of protein sequences.
    """
    Sequence_cluster_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "edam:data_1246"
    """
    A cluster of nucleotide sequences.
    """
    Sequence_length = "edam:data_1249"
    """
    The size (length) of a sequence, subsequence or region in a sequence, or range(s) of lengths.
    """
    Sequence_property = "edam:data_1254"
    """
    An informative report about non-positional sequence features, typically a report on general molecular sequence properties derived from sequence analysis.
    """
    Sequence_features = "edam:data_1255"
    """
    Annotation of positional features of molecular sequence(s), i.e. that can be mapped to position(s) in the sequence.
    """
    Sequence_complexity_report = "edam:data_1259"
    """
    A report on sequence complexity, for example low-complexity or repeat regions in sequences.
    """
    Sequence_ambiguity_report = "edam:data_1260"
    """
    A report on ambiguity in molecular sequence(s).
    """
    Sequence_composition_report = "edam:data_1261"
    """
    A report (typically a table) on character or word composition / frequency of a molecular sequence(s).
    """
    Peptide_molecular_weight_hits = "edam:data_1262"
    """
    A report on peptide fragments of certain molecular weight(s) in one or more protein sequences.
    """
    Base_position_variability_plot = "edam:data_1263"
    """
    A plot of third base position variability in a nucleotide sequence.
    """
    Base_frequencies_table = "edam:data_1265"
    """
    A table of base frequencies of a nucleotide sequence.
    """
    Base_word_frequencies_table = "edam:data_1266"
    """
    A table of word composition of a nucleotide sequence.
    """
    Amino_acid_frequencies_table = "edam:data_1267"
    """
    A table of amino acid frequencies of a protein sequence.
    """
    Amino_acid_word_frequencies_table = "edam:data_1268"
    """
    A table of amino acid word composition of a protein sequence.
    """
    Feature_table = "edam:data_1270"
    """
    Annotation of positional sequence features, organised into a standard feature table.
    """
    Map = "edam:data_1274"
    """
    A map of (typically one) DNA sequence annotated with positional or non-positional features.
    """
    Nucleic_acid_features = "edam:data_1276"
    """
    An informative report on intrinsic positional features of a nucleotide sequence, formatted to be machine-readable.
    """
    Protein_features = "edam:data_1277"
    """
    An informative report on intrinsic positional features of a protein sequence.
    """
    Genetic_map = "edam:data_1278"
    """
    A map showing the relative positions of genetic markers in a nucleic acid sequence, based on estimation of non-physical distance such as recombination frequencies.
    """
    Sequence_map = "edam:data_1279"
    """
    A map of genetic markers in a contiguous, assembled genomic sequence, with the sizes and separation of markers measured in base pairs.
    """
    Physical_map = "edam:data_1280"
    """
    A map of DNA (linear or circular) annotated with physical features or landmarks such as restriction sites, cloned DNA fragments, genes or genetic markers, along with the physical distances between them.
    """
    Cytogenetic_map = "edam:data_1283"
    """
    A map showing banding patterns derived from direct observation of a stained chromosome.
    """
    DNA_transduction_map = "edam:data_1284"
    """
    A gene map showing distances between loci based on relative cotransduction frequencies.
    """
    Gene_map = "edam:data_1285"
    """
    Sequence map of a single gene annotated with genetic features such as introns, exons, untranslated regions, polyA signals, promoters, enhancers and (possibly) mutations defining alleles of a gene.
    """
    Plasmid_map = "edam:data_1286"
    """
    Sequence map of a plasmid (circular DNA).
    """
    Genome_map = "edam:data_1288"
    """
    Sequence map of a whole genome.
    """
    Restriction_map = "edam:data_1289"
    """
    Image of the restriction enzyme cleavage sites (restriction sites) in a nucleic acid sequence.
    """
    Dirichlet_distribution = "edam:data_1347"
    """
    Dirichlet distribution used by hidden Markov model analysis programs.
    """
    Regular_expression = "edam:data_1352"
    """
    Regular expression pattern.
    """
    Sequence_motif = "edam:data_1353"
    """
    Any specific or conserved pattern (typically expressed as a regular expression) in a molecular sequence.
    """
    Sequence_profile = "edam:data_1354"
    """
    Some type of statistical model representing a (typically multiple) sequence alignment.
    """
    Protein_signature = "edam:data_1355"
    """
    An informative report about a specific or conserved protein sequence pattern.
    """
    Position_frequency_matrix = "edam:data_1361"
    """
    A profile (typically representing a sequence alignment) that is a simple matrix of nucleotide (or amino acid) counts per position.
    """
    Position_weight_matrix = "edam:data_1362"
    """
    A profile (typically representing a sequence alignment) that is weighted matrix of nucleotide (or amino acid) counts per position.
    """
    Information_content_matrix = "edam:data_1363"
    """
    A profile (typically representing a sequence alignment) derived from a matrix of nucleotide (or amino acid) counts per position that reflects information content at each position.
    """
    Hidden_Markov_model = "edam:data_1364"
    """
    A statistical Markov model of a system which is assumed to be a Markov process with unobserved (hidden) states. For example, a hidden Markov model representation of a set or alignment of sequences.
    """
    Fingerprint = "edam:data_1365"
    """
    One or more fingerprints (sequence classifiers) as used in the PRINTS database.
    """
    Pair_sequence_alignment = "edam:data_1381"
    """
    Alignment of exactly two molecular sequences.
    """
    Nucleic_acid_sequence_alignment = "edam:data_1383"
    """
    Alignment of multiple nucleotide sequences.
    """
    Protein_sequence_alignment = "edam:data_1384"
    """
    Alignment of multiple protein sequences.
    """
    Hybrid_sequence_alignment = "edam:data_1385"
    """
    Alignment of multiple molecular sequences of different types.
    """
    Alignment_score_or_penalty = "edam:data_1394"
    """
    A simple floating point number defining the penalty for opening or extending a gap in an alignment.
    """
    Gap_opening_penalty = "edam:data_1397"
    """
    A penalty for opening a gap in an alignment.
    """
    Gap_extension_penalty = "edam:data_1398"
    """
    A penalty for extending a gap in an alignment.
    """
    Gap_separation_penalty = "edam:data_1399"
    """
    A penalty for gaps that are close together in an alignment.
    """
    Match_reward_score = "edam:data_1401"
    """
    The score for a 'match' used in various sequence database search applications with simple scoring schemes.
    """
    Mismatch_penalty_score = "edam:data_1402"
    """
    The score (penalty) for a 'mismatch' used in various alignment and sequence database search applications with simple scoring schemes.
    """
    Drop_off_score = "edam:data_1403"
    """
    This is the threshold drop in score at which extension of word alignment is halted.
    """
    Terminal_gap_opening_penalty = "edam:data_1410"
    """
    A number defining the penalty for opening gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences.
    """
    Terminal_gap_extension_penalty = "edam:data_1411"
    """
    A number defining the penalty for extending gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences.
    """
    Sequence_identity = "edam:data_1412"
    """
    Sequence identity is the number (%) of matches (identical characters) in positions from an alignment of two molecular sequences.
    """
    Sequence_similarity = "edam:data_1413"
    """
    Sequence similarity is the similarity (expressed as a percentage) of two molecular sequences calculated from their alignment, a scoring matrix for scoring characters substitutions and penalties for gap insertion and extension.
    """
    Phylogenetic_continuous_quantitative_data = "edam:data_1426"
    """
    Continuous quantitative data that may be read during phylogenetic tree calculation.
    """
    Phylogenetic_discrete_data = "edam:data_1427"
    """
    Character data with discrete states that may be read during phylogenetic tree calculation.
    """
    Phylogenetic_character_cliques = "edam:data_1428"
    """
    One or more cliques of mutually compatible characters that are generated, for example from analysis of discrete character data, and are used to generate a phylogeny.
    """
    Phylogenetic_invariants = "edam:data_1429"
    """
    Phylogenetic invariants data for testing alternative tree topologies.
    """
    DNA_substitution_model = "edam:data_1439"
    """
    A model of DNA substitution that explains a DNA sequence alignment, derived from phylogenetic tree analysis.
    """
    Phylogenetic_tree_distances = "edam:data_1442"
    """
    Distances, such as Branch Score distance, between two or more phylogenetic trees.
    """
    Phylogenetic_character_contrasts = "edam:data_1444"
    """
    Independent contrasts for characters used in a phylogenetic tree, or covariances, regressions and correlations between characters for those contrasts.
    """
    Comparison_matrix_LEFT_PARENTHESISnucleotideRIGHT_PARENTHESIS = "edam:data_1448"
    """
    Matrix of integer or floating point numbers for nucleotide comparison.
    """
    Comparison_matrix_LEFT_PARENTHESISamino_acidRIGHT_PARENTHESIS = "edam:data_1449"
    """
    Matrix of integer or floating point numbers for amino acid comparison.
    """
    Nucleic_acid_structure = "edam:data_1459"
    """
    3D coordinate and associated data for a nucleic acid tertiary (3D) structure.
    """
    Protein_structure = "edam:data_1460"
    """
    3D coordinate and associated data for a protein tertiary (3D) structure, or part of a structure, possibly in complex with other molecules.
    """
    Protein_ligand_complex = "edam:data_1461"
    """
    The structure of a protein in complex with a ligand, typically a small molecule such as an enzyme substrate or cofactor, but possibly another macromolecule.
    """
    Carbohydrate_structure = "edam:data_1462"
    """
    3D coordinate and associated data for a carbohydrate (3D) structure.
    """
    Small_molecule_structure = "edam:data_1463"
    """
    3D coordinate and associated data for the (3D) structure of a small molecule, such as any common chemical compound.
    """
    DNA_structure = "edam:data_1464"
    """
    3D coordinate and associated data for a DNA tertiary (3D) structure.
    """
    RNA_structure = "edam:data_1465"
    """
    3D coordinate and associated data for an RNA tertiary (3D) structure.
    """
    tRNA_structure = "edam:data_1466"
    """
    3D coordinate and associated data for a tRNA tertiary (3D) structure, including tmRNA, snoRNAs etc.
    """
    Protein_chain = "edam:data_1467"
    """
    3D coordinate and associated data for the tertiary (3D) structure of a polypeptide chain.
    """
    Protein_domain = "edam:data_1468"
    """
    3D coordinate and associated data for the tertiary (3D) structure of a protein domain.
    """
    C_alpha_trace = "edam:data_1470"
    """
    3D coordinate and associated data for a protein tertiary (3D) structure (typically C-alpha atoms only).
    """
    Structure_alignment_LEFT_PARENTHESISpairRIGHT_PARENTHESIS = "edam:data_1479"
    """
    Alignment (superimposition) of exactly two molecular tertiary (3D) structures.
    """
    Protein_structure_alignment = "edam:data_1481"
    """
    Alignment (superimposition) of protein tertiary (3D) structures.
    """
    Nucleic_acid_structure_alignment = "edam:data_1482"
    """
    Alignment (superimposition) of nucleic acid tertiary (3D) structures.
    """
    RNA_structure_alignment = "edam:data_1493"
    """
    Alignment (superimposition) of RNA tertiary (3D) structures.
    """
    Structural_transformation_matrix = "edam:data_1494"
    """
    Matrix to transform (rotate/translate) 3D coordinates, typically the transformation necessary to superimpose two molecular structures.
    """
    Root_mean_square_deviation = "edam:data_1497"
    """
    Root-mean-square deviation (RMSD) is calculated to measure the average distance between superimposed macromolecular coordinates.
    """
    Tanimoto_similarity_score = "edam:data_1498"
    """
    A measure of the similarity between two ligand fingerprints.
    """
    number_3D_1D_scoring_matrix = "edam:data_1499"
    """
    A matrix of 3D-1D scores reflecting the probability of amino acids to occur in different tertiary structural environments.
    """
    Amino_acid_index = "edam:data_1501"
    """
    A table of 20 numerical values which quantify a property (e.g. physicochemical or biochemical) of the common amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESISchemical_classesRIGHT_PARENTHESIS = "edam:data_1502"
    """
    Chemical classification (small, aliphatic, aromatic, polar, charged etc) of amino acids.
    """
    Amino_acid_pair_wise_contact_potentials = "edam:data_1503"
    """
    Statistical protein contact potentials.
    """
    Amino_acid_index_LEFT_PARENTHESISmolecular_weightRIGHT_PARENTHESIS = "edam:data_1505"
    """
    Molecular weights of amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESIShydropathyRIGHT_PARENTHESIS = "edam:data_1506"
    """
    Hydrophobic, hydrophilic or charge properties of amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESISWhite_Wimley_dataRIGHT_PARENTHESIS = "edam:data_1507"
    """
    Experimental free energy values for the water-interface and water-octanol transitions for the amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESISvan_der_Waals_radiiRIGHT_PARENTHESIS = "edam:data_1508"
    """
    Van der Waals radii of atoms for different amino acid residues.
    """
    Peptide_molecular_weights = "edam:data_1519"
    """
    List of molecular weight(s) of one or more proteins or peptides, for example cut by proteolytic enzymes or reagents.
    """
    Peptide_hydrophobic_moment = "edam:data_1520"
    """
    Report on the hydrophobic moment of a polypeptide sequence.
    """
    Protein_aliphatic_index = "edam:data_1521"
    """
    The aliphatic index of a protein.
    """
    Protein_sequence_hydropathy_plot = "edam:data_1522"
    """
    A protein sequence with annotation on hydrophobic or hydrophilic / charged regions, hydrophobicity plot etc.
    """
    Protein_charge_plot = "edam:data_1523"
    """
    A plot of the mean charge of the amino acids within a window of specified length as the window is moved along a protein sequence.
    """
    Protein_solubility = "edam:data_1524"
    """
    The solubility or atomic solvation energy of a protein sequence or structure.
    """
    Protein_crystallizability = "edam:data_1525"
    """
    Data on the crystallizability of a protein sequence.
    """
    Protein_globularity = "edam:data_1526"
    """
    Data on the stability, intrinsic disorder or globularity of a protein sequence.
    """
    Protein_titration_curve = "edam:data_1527"
    """
    The titration curve of a protein.
    """
    Protein_isoelectric_point = "edam:data_1528"
    """
    The isoelectric point of one proteins.
    """
    Protein_pKa_value = "edam:data_1529"
    """
    The pKa value of a protein.
    """
    Protein_hydrogen_exchange_rate = "edam:data_1530"
    """
    The hydrogen exchange rate of a protein.
    """
    Protein_extinction_coefficient = "edam:data_1531"
    """
    The extinction coefficient of a protein.
    """
    Protein_optical_density = "edam:data_1532"
    """
    The optical density of a protein.
    """
    Peptide_immunogenicity_data = "edam:data_1534"
    """
    An report on allergenicity / immunogenicity of peptides and proteins.
    """
    Protein_structure_report = "edam:data_1537"
    """
    A human-readable collection of information about one or more specific protein 3D structure(s) or structural domains.
    """
    Protein_structural_quality_report = "edam:data_1539"
    """
    Report on the quality of a protein three-dimensional model.
    """
    Protein_solvent_accessibility = "edam:data_1542"
    """
    Data on the solvent accessible or buried surface area of a protein structure.
    """
    Ramachandran_plot = "edam:data_1544"
    """
    Phi/psi angle data or a Ramachandran plot of a protein structure.
    """
    Protein_dipole_moment = "edam:data_1545"
    """
    Data on the net charge distribution (dipole moment) of a protein structure.
    """
    Protein_distance_matrix = "edam:data_1546"
    """
    A matrix of distances between amino acid residues (for example the C-alpha atoms) in a protein structure.
    """
    Protein_contact_map = "edam:data_1547"
    """
    An amino acid residue contact map for a protein structure.
    """
    Protein_residue_3D_cluster = "edam:data_1548"
    """
    Report on clusters of contacting residues in protein structures such as a key structural residue network.
    """
    Protein_hydrogen_bonds = "edam:data_1549"
    """
    Patterns of hydrogen bonding in protein structures.
    """
    Protein_ligand_interaction_report = "edam:data_1566"
    """
    An informative report on protein-ligand (small molecule) interaction(s).
    """
    Nucleic_acid_melting_profile = "edam:data_1583"
    """
    Data on the dissociation characteristics of a double-stranded nucleic acid molecule (DNA or a DNA/RNA hybrid) during heating.
    """
    Nucleic_acid_enthalpy = "edam:data_1584"
    """
    Enthalpy of hybridised or double stranded nucleic acid (DNA or RNA/DNA).
    """
    Nucleic_acid_entropy = "edam:data_1585"
    """
    Entropy of hybridised or double stranded nucleic acid (DNA or RNA/DNA).
    """
    DNA_base_pair_stacking_energies_data = "edam:data_1588"
    """
    DNA base pair stacking energies data.
    """
    DNA_base_pair_twist_angle_data = "edam:data_1589"
    """
    DNA base pair twist angle data.
    """
    DNA_base_trimer_roll_angles_data = "edam:data_1590"
    """
    DNA base trimer roll angles data.
    """
    Base_pairing_probability_matrix_dotplot = "edam:data_1595"
    """
    Dotplot of RNA base pairing probability matrix.
    """
    Nucleic_acid_folding_report = "edam:data_1596"
    """
    A human-readable collection of information about RNA/DNA folding, minimum folding energies for DNA or RNA sequences, energy landscape of RNA mutants etc.
    """
    Codon_usage_table = "edam:data_1597"
    """
    Table of codon usage data calculated from one or more nucleic acid sequences.
    """
    Genetic_code = "edam:data_1598"
    """
    A genetic code for an organism.
    """
    Codon_usage_bias_plot = "edam:data_1600"
    """
    A plot of the synonymous codon usage calculated for windows over a nucleotide sequence.
    """
    Codon_usage_fraction_difference = "edam:data_1602"
    """
    The differences in codon usage fractions between two codon usage tables.
    """
    Pharmacogenomic_test_report = "edam:data_1621"
    """
    A human-readable collection of information about the influence of genotype on drug response.
    """
    Disease_report = "edam:data_1622"
    """
    A human-readable collection of information about a specific disease.
    """
    Heat_map = "edam:data_1636"
    """
    A graphical 2D tabular representation of expression data, typically derived from an omics experiment. A heat map is a table where rows and columns correspond to different features and contexts (for example, cells or samples) and the cell colour represents the level of expression of a gene that context.
    """
    E_value = "edam:data_1667"
    """
    A simple floating point number defining the lower or upper limit of an expectation value (E-value).
    """
    Z_value = "edam:data_1668"
    """
    The z-value is the number of standard deviations a data value is above or below a mean value.
    """
    P_value = "edam:data_1669"
    """
    The P-value is the probability of obtaining by random chance a result that is at least as extreme as an observed result, assuming a NULL hypothesis is true.
    """
    Username = "edam:data_1689"
    """
    A username on a computer system or a website.
    """
    Password = "edam:data_1690"
    """
    A password on a computer system, or a website.
    """
    Email_address = "edam:data_1691"
    """
    A valid email address of an end-user.
    """
    Person_name = "edam:data_1692"
    """
    The name of a person.
    """
    Drug_report = "edam:data_1696"
    """
    A human-readable collection of information about a specific drug.
    """
    Phylogenetic_tree_image = "edam:data_1707"
    """
    An image (for viewing or printing) of a phylogenetic tree including (typically) a plot of rooted or unrooted phylogenies, cladograms, circular trees or phenograms and associated information.
    """
    RNA_secondary_structure_image = "edam:data_1708"
    """
    Image of RNA secondary structure, knots, pseudoknots etc.
    """
    Protein_secondary_structure_image = "edam:data_1709"
    """
    Image of protein secondary structure.
    """
    Structure_image = "edam:data_1710"
    """
    Image of one or more molecular tertiary (3D) structures.
    """
    Sequence_alignment_image = "edam:data_1711"
    """
    Image of two or more aligned molecular sequences possibly annotated with alignment features.
    """
    Chemical_structure_image = "edam:data_1712"
    """
    An image of the structure of a small chemical compound.
    """
    Fate_map = "edam:data_1713"
    """
    A fate map is a plan of early stage of an embryo such as a blastula, showing areas that are significance to development.
    """
    Microarray_spots_image = "edam:data_1714"
    """
    An image of spots from a microarray experiment.
    """
    Ontology_concept_definition = "edam:data_1731"
    """
    The definition of a concept from an ontology.
    """
    PDB_residue_number = "edam:data_1742"
    """
    A residue identifier (a string) from a PDB file.
    """
    Atomic_coordinate = "edam:data_1743"
    """
    Cartesian coordinate of an atom (in a molecular structure).
    """
    PDB_atom_name = "edam:data_1748"
    """
    Identifier (a string) of a specific atom from a PDB file for a molecular structure.
    """
    Protein_atom = "edam:data_1755"
    """
    Data on a single atom from a protein structure.
    """
    Protein_residue = "edam:data_1756"
    """
    Data on a single amino acid residue position in a protein structure.
    """
    Atom_name = "edam:data_1757"
    """
    Name of an atom.
    """
    PDB_residue_name = "edam:data_1758"
    """
    Three-letter amino acid residue names as used in PDB files.
    """
    PDB_model_number = "edam:data_1759"
    """
    Identifier of a model structure from a PDB file.
    """
    Sequence_version = "edam:data_1771"
    """
    Information on an molecular sequence version.
    """
    Score = "edam:data_1772"
    """
    A numerical value, that is some type of scored value arising for example from a prediction method.
    """
    Gene_ID_LEFT_PARENTHESISPlasmoDBRIGHT_PARENTHESIS = "edam:data_1794"
    """
    Identifier of a gene from PlasmoDB Plasmodium Genome Resource.
    """
    Gene_ID_LEFT_PARENTHESISEcoGeneRIGHT_PARENTHESIS = "edam:data_1795"
    """
    Identifier of a gene from EcoGene Database.
    """
    Gene_ID_LEFT_PARENTHESISFlyBaseRIGHT_PARENTHESIS = "edam:data_1796"
    """
    Gene identifier from FlyBase database.
    """
    Gene_ID_LEFT_PARENTHESISGrameneRIGHT_PARENTHESIS = "edam:data_1802"
    """
    Gene identifier from Gramene database.
    """
    Gene_ID_LEFT_PARENTHESISVirginia_microbialRIGHT_PARENTHESIS = "edam:data_1803"
    """
    Gene identifier from Virginia Bioinformatics Institute microbial database.
    """
    Gene_ID_LEFT_PARENTHESISSGNRIGHT_PARENTHESIS = "edam:data_1804"
    """
    Gene identifier from Sol Genomics Network.
    """
    Gene_ID_LEFT_PARENTHESISWormBaseRIGHT_PARENTHESIS = "edam:data_1805"
    """
    Gene identifier used by WormBase database.
    """
    ORF_name = "edam:data_1807"
    """
    The name of an open reading frame attributed by a sequencing project.
    """
    Clone_ID = "edam:data_1855"
    """
    An identifier of a clone (cloned molecular sequence) from a database.
    """
    PDB_insertion_code = "edam:data_1856"
    """
    An insertion code (part of the residue number) for an amino acid residue from a PDB file.
    """
    Atomic_occupancy = "edam:data_1857"
    """
    The fraction of an atom type present at a site in a molecular structure.
    """
    Isotropic_B_factor = "edam:data_1858"
    """
    Isotropic B factor (atomic displacement parameter) for an atom from a PDB file.
    """
    Deletion_map = "edam:data_1859"
    """
    A cytogenetic map showing chromosome banding patterns in mutant cell lines relative to the wild type.
    """
    QTL_map = "edam:data_1860"
    """
    A genetic map which shows the approximate location of quantitative trait loci (QTL) between two or more markers.
    """
    Haplotype_map = "edam:data_1863"
    """
    A map of haplotypes in a genome or other sequence, describing common patterns of genetic variation.
    """
    Protein_fold_name = "edam:data_1867"
    """
    The name of a protein fold.
    """
    Taxon = "edam:data_1868"
    """
    The name of a group of organisms belonging to the same taxonomic rank.
    """
    Organism_identifier = "edam:data_1869"
    """
    A unique identifier of a (group of) organisms.
    """
    Genus_name = "edam:data_1870"
    """
    The name of a genus of organism.
    """
    Taxonomic_classification = "edam:data_1872"
    """
    The full name for a group of organisms, reflecting their biological classification and (usually) conforming to a standard nomenclature.
    """
    iHOP_organism_ID = "edam:data_1873"
    """
    A unique identifier for an organism used in the iHOP database.
    """
    Genbank_common_name = "edam:data_1874"
    """
    Common name for an organism as used in the GenBank database.
    """
    NCBI_taxon = "edam:data_1875"
    """
    The name of a taxon from the NCBI taxonomy database.
    """
    Author_ID = "edam:data_1881"
    """
    Information on the authors of a published work.
    """
    DragonDB_author_identifier = "edam:data_1882"
    """
    An identifier representing an author in the DragonDB database.
    """
    Annotated_URI = "edam:data_1883"
    """
    A URI along with annotation describing the data found at the address.
    """
    Gene_ID_LEFT_PARENTHESISGeneFarmRIGHT_PARENTHESIS = "edam:data_1885"
    """
    Identifier of a gene from the GeneFarm database.
    """
    Blattner_number = "edam:data_1886"
    """
    The blattner identifier for a gene.
    """
    iHOP_symbol = "edam:data_1891"
    """
    A unique identifier of a protein or gene used in the iHOP database.
    """
    Locus_ID = "edam:data_1893"
    """
    A unique name or other identifier of a genetic locus, typically conforming to a scheme that names loci (such as predicted genes) depending on their position in a molecular sequence, for example a completely sequenced genome or chromosome.
    """
    Locus_ID_LEFT_PARENTHESISAGIRIGHT_PARENTHESIS = "edam:data_1895"
    """
    Locus identifier for Arabidopsis Genome Initiative (TAIR, TIGR and MIPS databases).
    """
    Locus_ID_LEFT_PARENTHESISASPGDRIGHT_PARENTHESIS = "edam:data_1896"
    """
    Identifier for loci from ASPGD (Aspergillus Genome Database).
    """
    Locus_ID_LEFT_PARENTHESISMGGRIGHT_PARENTHESIS = "edam:data_1897"
    """
    Identifier for loci from Magnaporthe grisea Database at the Broad Institute.
    """
    Locus_ID_LEFT_PARENTHESISCGDRIGHT_PARENTHESIS = "edam:data_1898"
    """
    Identifier for loci from CGD (Candida Genome Database).
    """
    Locus_ID_LEFT_PARENTHESISCMRRIGHT_PARENTHESIS = "edam:data_1899"
    """
    Locus identifier for Comprehensive Microbial Resource at the J. Craig Venter Institute.
    """
    NCBI_locus_tag = "edam:data_1900"
    """
    Identifier for loci from NCBI database.
    """
    Locus_ID_LEFT_PARENTHESISSGDRIGHT_PARENTHESIS = "edam:data_1901"
    """
    Identifier for loci from SGD (Saccharomyces Genome Database).
    """
    Locus_ID_LEFT_PARENTHESISMMPRIGHT_PARENTHESIS = "edam:data_1902"
    """
    Identifier of loci from Maize Mapping Project.
    """
    Locus_ID_LEFT_PARENTHESISDictyBaseRIGHT_PARENTHESIS = "edam:data_1903"
    """
    Identifier of locus from DictyBase (Dictyostelium discoideum).
    """
    Locus_ID_LEFT_PARENTHESISEntrezGeneRIGHT_PARENTHESIS = "edam:data_1904"
    """
    Identifier of a locus from EntrezGene database.
    """
    Locus_ID_LEFT_PARENTHESISMaizeGDBRIGHT_PARENTHESIS = "edam:data_1905"
    """
    Identifier of locus from MaizeGDB (Maize genome database).
    """
    Gene_ID_LEFT_PARENTHESISKOMERIGHT_PARENTHESIS = "edam:data_1907"
    """
    Identifier of a gene from the KOME database.
    """
    Locus_ID_LEFT_PARENTHESISTropgeneRIGHT_PARENTHESIS = "edam:data_1908"
    """
    Identifier of a locus from the Tropgene database.
    """
    Alignment = "edam:data_1916"
    """
    An alignment of molecular sequences, structures or profiles derived from them.
    """
    Atomic_property = "edam:data_1917"
    """
    Data for an atom (in a molecular structure).
    """
    UniProt_keyword = "edam:data_2007"
    """
    A word or phrase that can appear in the keywords field (KW line) of entries from the UniProt database.
    """
    Sequence_coordinates = "edam:data_2012"
    """
    A position in a map (for example a genetic map), either a single position (point) or a region / interval.
    """
    Amino_acid_property = "edam:data_2016"
    """
    Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all amino acids.
    """
    Map_data = "edam:data_2019"
    """
    Data describing a molecular map (genetic or physical) or a set of such maps, including various attributes of, data extracted from or derived from the analysis of them, but excluding the map(s) themselves. This includes metadata for map sets that share a common set of features which are mapped.
    """
    Enzyme_kinetics_data = "edam:data_2024"
    """
    Data concerning chemical reaction(s) catalysed by enzyme(s).
    """
    Michaelis_Menten_plot = "edam:data_2025"
    """
    A plot giving an approximation of the kinetics of an enzyme-catalysed reaction, assuming simple kinetics (i.e. no intermediate or product inhibition, allostericity or cooperativity). It plots initial reaction rate to the substrate concentration (S) from which the maximum rate (vmax) is apparent.
    """
    Hanes_Woolf_plot = "edam:data_2026"
    """
    A plot based on the Michaelis Menten equation of enzyme kinetics plotting the ratio of the initial substrate concentration (S) against the reaction velocity (v).
    """
    Evidence = "edam:data_2042"
    """
    Typically a human-readable summary of body of facts or information indicating why a statement is true or valid. This may include a computational prediction, laboratory experiment, literature reference etc.
    """
    Sequence = "edam:data_2044"
    """
    One or more molecular sequences, possibly with associated annotation.
    """
    Report = "edam:data_2048"
    """
    A human-readable collection of information including annotation on a biological entity or phenomena, computer-generated reports of analysis of primary data (e.g. sequence or structural), and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself.
    """
    Molecular_property_LEFT_PARENTHESISgeneralRIGHT_PARENTHESIS = "edam:data_2050"
    """
    General data for a molecule.
    """
    Sequence_motif_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "edam:data_2070"
    """
    A nucleotide sequence motif.
    """
    Sequence_motif_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:data_2071"
    """
    An amino acid sequence motif.
    """
    Database_search_results = "edam:data_2080"
    """
    A report of hits from searching a database of some type.
    """
    Matrix = "edam:data_2082"
    """
    An array of numerical values.
    """
    Nucleic_acid_report = "edam:data_2084"
    """
    A human-readable collection of information about one or more specific nucleic acid molecules.
    """
    Structure_report = "edam:data_2085"
    """
    A human-readable collection of information about one or more molecular tertiary (3D) structures. It might include annotation on the structure, a computer-generated report of analysis of structural data, and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself.
    """
    Molecular_property = "edam:data_2087"
    """
    A report on the physical (e.g. structural) or chemical properties of molecules, or parts of a molecule.
    """
    DNA_base_structural_data = "edam:data_2088"
    """
    Structural data for DNA base pairs or runs of bases, such as energy or angle data.
    """
    Accession = "edam:data_2091"
    """
    A persistent (stable) and unique identifier, typically identifying an object (entry) from a database.
    """
    Data_reference = "edam:data_2093"
    """
    Reference to a dataset (or a cross-reference between two datasets), typically one or more entries in a biological database or ontology.
    """
    Job_identifier = "edam:data_2098"
    """
    An identifier of a submitted job.
    """
    Name = "edam:data_2099"
    """
    A name of a thing, which need not necessarily uniquely identify it.
    """
    Account_authentication = "edam:data_2101"
    """
    Authentication data usually used to log in into an account on an information system such as a web application or a database.
    """
    KEGG_organism_code = "edam:data_2102"
    """
    A three-letter code used in the KEGG databases to uniquely identify organisms.
    """
    BioCyc_ID = "edam:data_2104"
    """
    Identifier of an object from one of the BioCyc databases.
    """
    Compound_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "edam:data_2105"
    """
    Identifier of a compound from the BioCyc chemical compounds database.
    """
    Reaction_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "edam:data_2106"
    """
    Identifier of a biological reaction from the BioCyc reactions database.
    """
    Enzyme_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "edam:data_2107"
    """
    Identifier of an enzyme from the BioCyc enzymes database.
    """
    Reaction_ID = "edam:data_2108"
    """
    Identifier of a biological reaction from a database.
    """
    Identifier_LEFT_PARENTHESIShybridRIGHT_PARENTHESIS = "edam:data_2109"
    """
    An identifier that is reused for data objects of fundamentally different types (typically served from a single database).
    """
    Molecular_property_identifier = "edam:data_2110"
    """
    Identifier of a molecular property.
    """
    Codon_usage_table_ID = "edam:data_2111"
    """
    Identifier of a codon usage table, for example a genetic code.
    """
    FlyBase_primary_identifier = "edam:data_2112"
    """
    Primary identifier of an object from the FlyBase database.
    """
    WormBase_identifier = "edam:data_2113"
    """
    Identifier of an object from the WormBase database.
    """
    WormBase_wormpep_ID = "edam:data_2114"
    """
    Protein identifier used by WormBase database.
    """
    Map_identifier = "edam:data_2117"
    """
    An identifier of a map of a molecular sequence.
    """
    Person_identifier = "edam:data_2118"
    """
    An identifier of a software end-user on a website or a database (typically a person or an entity).
    """
    Nucleic_acid_identifier = "edam:data_2119"
    """
    Name or other identifier of a nucleic acid molecule.
    """
    Genetic_code_identifier = "edam:data_2127"
    """
    An identifier of a genetic code.
    """
    Genetic_code_name = "edam:data_2128"
    """
    Informal name for a genetic code, typically an organism name.
    """
    File_format_name = "edam:data_2129"
    """
    Name of a file format such as HTML, PNG, PDF, EMBL, GenBank and so on.
    """
    Operating_system_name = "edam:data_2131"
    """
    Name of a computer operating system such as Linux, PC or Mac.
    """
    Logical_operator = "edam:data_2133"
    """
    A logical operator such as OR, AND, XOR, and NOT.
    """
    Gap_penalty = "edam:data_2137"
    """
    A penalty for introducing or extending a gap in an alignment.
    """
    Nucleic_acid_melting_temperature = "edam:data_2139"
    """
    A temperature concerning nucleic acid denaturation, typically the temperature at which the two strands of a hybridised or double stranded nucleic acid (DNA or RNA/DNA) molecule separate.
    """
    Concentration = "edam:data_2140"
    """
    The concentration of a chemical compound.
    """
    Sequence_name = "edam:data_2154"
    """
    Any arbitrary name of a molecular sequence.
    """
    Fickett_testcode_plot = "edam:data_2160"
    """
    A plot of Fickett testcode statistic (identifying protein coding regions) in a nucleotide sequences.
    """
    Sequence_similarity_plot = "edam:data_2161"
    """
    A plot of sequence similarities identified from word-matching or character comparison.
    """
    Helical_wheel = "edam:data_2162"
    """
    An image of peptide sequence sequence looking down the axis of the helix for highlighting amphipathicity and other properties.
    """
    Helical_net = "edam:data_2163"
    """
    An image of peptide sequence sequence in a simple 3,4,3,4 repeating pattern that emulates at a simple level the arrangement of residues around an alpha helix.
    """
    Protein_ionisation_curve = "edam:data_2165"
    """
    A plot of pK versus pH for a protein.
    """
    Sequence_composition_plot = "edam:data_2166"
    """
    A plot of character or word composition / frequency of a molecular sequence.
    """
    Nucleic_acid_density_plot = "edam:data_2167"
    """
    Density plot (of base composition) for a nucleotide sequence.
    """
    Sequence_trace_image = "edam:data_2168"
    """
    Image of a sequence trace (nucleotide sequence versus probabilities of each of the 4 bases).
    """
    FlyBase_secondary_identifier = "edam:data_2174"
    """
    Secondary identifier of an object from the FlyBase database.
    """
    Sequence_checksum = "edam:data_2190"
    """
    A fixed-size datum calculated (by using a hash function) for a molecular sequence, typically for purposes of error detection or indexing.
    """
    Database_entry_metadata = "edam:data_2193"
    """
    Basic information on any arbitrary database entry.
    """
    Plasmid_identifier = "edam:data_2208"
    """
    An identifier of a plasmid in a database.
    """
    Mutation_ID = "edam:data_2209"
    """
    A unique identifier of a specific mutation catalogued in a database.
    """
    Codon_number = "edam:data_2216"
    """
    The number of a codon, for instance, at which a mutation is located.
    """
    Database_field_name = "edam:data_2219"
    """
    The name of a field in a database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISSYSTERSRIGHT_PARENTHESIS = "edam:data_2220"
    """
    Unique identifier of a sequence cluster from the SYSTERS database.
    """
    Ontology_metadata = "edam:data_2223"
    """
    Data concerning a biological ontology.
    """
    Data_resource_definition_name = "edam:data_2253"
    """
    The name of a data type.
    """
    OBO_file_format_name = "edam:data_2254"
    """
    Name of an OBO file format such as OBO-XML, plain and so on.
    """
    Gene_ID_LEFT_PARENTHESISMIPSRIGHT_PARENTHESIS = "edam:data_2285"
    """
    Identifier for genetic elements in MIPS database.
    """
    EMBL_accession = "edam:data_2290"
    """
    An accession number of an entry from the EMBL sequence database.
    """
    UniProt_ID = "edam:data_2291"
    """
    An identifier of a polypeptide in the UniProt database.
    """
    GenBank_accession = "edam:data_2292"
    """
    Accession number of an entry from the GenBank sequence database.
    """
    Gramene_secondary_identifier = "edam:data_2293"
    """
    Secondary (internal) identifier of a Gramene database entry.
    """
    Sequence_variation_ID = "edam:data_2294"
    """
    An identifier of an entry from a database of molecular sequence variation.
    """
    Gene_ID = "edam:data_2295"
    """
    A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol.
    """
    Gene_ID_LEFT_PARENTHESISECKRIGHT_PARENTHESIS = "edam:data_2297"
    """
    Identifier of an E. coli K-12 gene from EcoGene Database.
    """
    Gene_ID_LEFT_PARENTHESISHGNCRIGHT_PARENTHESIS = "edam:data_2298"
    """
    Identifier for a gene approved by the HUGO Gene Nomenclature Committee.
    """
    Gene_name = "edam:data_2299"
    """
    The name of a gene, (typically) assigned by a person and/or according to a naming scheme. It may contain white space characters and is typically more intuitive and readable than a gene symbol. It (typically) may be used to identify similar genes in different species and to derive a gene symbol.
    """
    SMILES_string = "edam:data_2301"
    """
    A specification of a chemical structure in SMILES format.
    """
    STRING_ID = "edam:data_2302"
    """
    Unique identifier of an entry from the STRING database of protein-protein interactions.
    """
    Reaction_ID_LEFT_PARENTHESISSABIO_RKRIGHT_PARENTHESIS = "edam:data_2309"
    """
    Identifier of a biological reaction from the SABIO-RK reactions database.
    """
    Carbohydrate_report = "edam:data_2313"
    """
    A human-readable collection of information about one or more specific carbohydrate 3D structure(s).
    """
    GI_number = "edam:data_2314"
    """
    A series of digits that are assigned consecutively to each sequence record processed by NCBI. The GI number bears no resemblance to the Accession number of the sequence record.
    """
    NCBI_version = "edam:data_2315"
    """
    An identifier assigned to sequence records processed by NCBI, made of the accession number of the database record followed by a dot and a version number.
    """
    Cell_line_name = "edam:data_2316"
    """
    The name of a cell line.
    """
    Cell_line_name_LEFT_PARENTHESISexactRIGHT_PARENTHESIS = "edam:data_2317"
    """
    The exact name of a cell line.
    """
    Cell_line_name_LEFT_PARENTHESIStruncatedRIGHT_PARENTHESIS = "edam:data_2318"
    """
    The truncated name of a cell line.
    """
    Cell_line_name_LEFT_PARENTHESISno_punctuationRIGHT_PARENTHESIS = "edam:data_2319"
    """
    The name of a cell line without any punctuation.
    """
    Cell_line_name_LEFT_PARENTHESISassonantRIGHT_PARENTHESIS = "edam:data_2320"
    """
    The assonant name of a cell line.
    """
    Enzyme_ID = "edam:data_2321"
    """
    A unique, persistent identifier of an enzyme.
    """
    REBASE_enzyme_number = "edam:data_2325"
    """
    Identifier of an enzyme from the REBASE enzymes database.
    """
    DrugBank_ID = "edam:data_2326"
    """
    Unique identifier of a drug from the DrugBank database.
    """
    GI_number_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:data_2327"
    """
    A unique identifier assigned to NCBI protein sequence records.
    """
    Bit_score = "edam:data_2335"
    """
    A score derived from the alignment of two sequences, which is then normalised with respect to the scoring system.
    """
    Resource_metadata = "edam:data_2337"
    """
    Data concerning or describing some core computational resource, as distinct from primary data. This includes metadata on the origin, source, history, ownership or location of some thing.
    """
    Ontology_identifier = "edam:data_2338"
    """
    Any arbitrary identifier of an ontology.
    """
    Ontology_concept_name = "edam:data_2339"
    """
    The name of a concept in an ontology.
    """
    Genome_build_identifier = "edam:data_2340"
    """
    An identifier of a build of a particular genome.
    """
    Pathway_or_network_name = "edam:data_2342"
    """
    The name of a biological pathway or network.
    """
    Pathway_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "edam:data_2343"
    """
    Identifier of a pathway from the KEGG pathway database.
    """
    Pathway_ID_LEFT_PARENTHESISNCI_NatureRIGHT_PARENTHESIS = "edam:data_2344"
    """
    Identifier of a pathway from the NCI-Nature pathway database.
    """
    Pathway_ID_LEFT_PARENTHESISConsensusPathDBRIGHT_PARENTHESIS = "edam:data_2345"
    """
    Identifier of a pathway from the ConsensusPathDB pathway database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRefRIGHT_PARENTHESIS = "edam:data_2346"
    """
    Unique identifier of an entry from the UniRef database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRef100RIGHT_PARENTHESIS = "edam:data_2347"
    """
    Unique identifier of an entry from the UniRef100 database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRef90RIGHT_PARENTHESIS = "edam:data_2348"
    """
    Unique identifier of an entry from the UniRef90 database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRef50RIGHT_PARENTHESIS = "edam:data_2349"
    """
    Unique identifier of an entry from the UniRef50 database.
    """
    Ontology_data = "edam:data_2353"
    """
    Data concerning or derived from an ontology.
    """
    RNA_family_report = "edam:data_2354"
    """
    A human-readable collection of information about a specific RNA family or other group of classified RNA sequences.
    """
    RNA_family_identifier = "edam:data_2355"
    """
    Identifier of an RNA family, typically an entry from a RNA sequence classification database.
    """
    RFAM_accession = "edam:data_2356"
    """
    Stable accession number of an entry (RNA family) from the RFAM database.
    """
    Sequence_accession_LEFT_PARENTHESIShybridRIGHT_PARENTHESIS = "edam:data_2362"
    """
    Accession number of a nucleotide or protein sequence database entry.
    """
    Pathway_or_network_accession = "edam:data_2365"
    """
    A persistent, unique identifier of a biological pathway or network (typically a database entry).
    """
    Secondary_structure_alignment = "edam:data_2366"
    """
    Alignment of the (1D representations of) secondary structure of two or more molecules.
    """
    ASTD_ID = "edam:data_2367"
    """
    Identifier of an object from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESISexonRIGHT_PARENTHESIS = "edam:data_2368"
    """
    Identifier of an exon from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESISintronRIGHT_PARENTHESIS = "edam:data_2369"
    """
    Identifier of an intron from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESISpolyaRIGHT_PARENTHESIS = "edam:data_2370"
    """
    Identifier of a polyA signal from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESIStssRIGHT_PARENTHESIS = "edam:data_2371"
    """
    Identifier of a transcription start site from the ASTD database.
    """
    Spot_ID = "edam:data_2373"
    """
    Unique identifier of a spot from a two-dimensional (protein) gel.
    """
    Spot_serial_number = "edam:data_2374"
    """
    Unique identifier of a spot from a two-dimensional (protein) gel in the SWISS-2DPAGE database.
    """
    Spot_ID_LEFT_PARENTHESISHSC_2DPAGERIGHT_PARENTHESIS = "edam:data_2375"
    """
    Unique identifier of a spot from a two-dimensional (protein) gel from a HSC-2DPAGE database.
    """
    Strain_identifier = "edam:data_2379"
    """
    Identifier of a strain of an organism variant, typically a plant, virus or bacterium.
    """
    CABRI_accession = "edam:data_2380"
    """
    A unique identifier of an item from the CABRI database.
    """
    Genotype_experiment_ID = "edam:data_2382"
    """
    Identifier of an entry from a database of genotype experiment metadata.
    """
    EGA_accession = "edam:data_2383"
    """
    Identifier of an entry from the EGA database.
    """
    IPI_protein_ID = "edam:data_2384"
    """
    Identifier of a protein entry catalogued in the International Protein Index (IPI) database.
    """
    RefSeq_accession_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:data_2385"
    """
    Accession number of a protein from the RefSeq database.
    """
    EPD_ID = "edam:data_2386"
    """
    Identifier of an entry (promoter) from the EPD database.
    """
    TAIR_accession = "edam:data_2387"
    """
    Identifier of an entry from the TAIR database.
    """
    TAIR_accession_LEFT_PARENTHESISAt_geneRIGHT_PARENTHESIS = "edam:data_2388"
    """
    Identifier of an Arabidopsis thaliana gene from the TAIR database.
    """
    UniSTS_accession = "edam:data_2389"
    """
    Identifier of an entry from the UniSTS database.
    """
    UNITE_accession = "edam:data_2390"
    """
    Identifier of an entry from the UNITE database.
    """
    UTR_accession = "edam:data_2391"
    """
    Identifier of an entry from the UTR database.
    """
    UniParc_accession = "edam:data_2392"
    """
    Accession number of a UniParc (protein sequence) database entry.
    """
    mFLJSOLIDUSmKIAA_number = "edam:data_2393"
    """
    Identifier of an entry from the Rouge or HUGE databases.
    """
    Ensembl_protein_ID = "edam:data_2398"
    """
    Unique identifier for a protein from the Ensembl database.
    """
    Phylogenetic_data = "edam:data_2523"
    """
    Data concerning phylogeny, typically of molecular sequences, including reports of information concerning or derived from a phylogenetic tree, or from comparing two or more phylogenetic trees.
    """
    Text_data = "edam:data_2526"
    """
    Data concerning, extracted from, or derived from the analysis of a scientific text (or texts) such as a full text article from a scientific journal.
    """
    Organism_report = "edam:data_2530"
    """
    A human-readable collection of information about a specific organism.
    """
    Protocol = "edam:data_2531"
    """
    A human-readable collection of information about about how a scientific experiment or analysis was carried out that results in a specific set of data or results used for further analysis or to test a specific hypothesis.
    """
    Sequence_attribute = "edam:data_2534"
    """
    An attribute of a molecular sequence, possibly in reference to some other sequence.
    """
    Sequence_tag_profile = "edam:data_2535"
    """
    Output from a serial analysis of gene expression (SAGE), massively parallel signature sequencing (MPSS) or sequencing by synthesis (SBS) experiment. In all cases this is a list of short sequence tags and the number of times it is observed.
    """
    Mass_spectrometry_data = "edam:data_2536"
    """
    Data concerning a mass spectrometry measurement.
    """
    Protein_structure_raw_data = "edam:data_2537"
    """
    Raw data from experimental methods for determining protein structure.
    """
    Mutation_identifier = "edam:data_2538"
    """
    An identifier of a mutation.
    """
    Amino_acid_name_LEFT_PARENTHESISsingle_letterRIGHT_PARENTHESIS = "edam:data_2563"
    """
    Single letter amino acid identifier, e.g. G.
    """
    Amino_acid_name_LEFT_PARENTHESISthree_letterRIGHT_PARENTHESIS = "edam:data_2564"
    """
    Three letter amino acid identifier, e.g. GLY.
    """
    Amino_acid_name_LEFT_PARENTHESISfull_nameRIGHT_PARENTHESIS = "edam:data_2565"
    """
    Full name of an amino acid, e.g. Glycine.
    """
    Toxin_identifier = "edam:data_2576"
    """
    Identifier of a toxin.
    """
    ArachnoServer_ID = "edam:data_2578"
    """
    Unique identifier of a toxin from the ArachnoServer database.
    """
    BindingDB_Monomer_ID = "edam:data_2580"
    """
    Unique identifier of a monomer from the BindingDB database.
    """
    GO_concept_ID_LEFT_PARENTHESISbiological_processRIGHT_PARENTHESIS = "edam:data_2582"
    """
    An identifier of a 'biological process' concept from the the Gene Ontology.
    """
    GO_concept_ID_LEFT_PARENTHESISmolecular_functionRIGHT_PARENTHESIS = "edam:data_2583"
    """
    An identifier of a 'molecular function' concept from the the Gene Ontology.
    """
    Northern_blot_image = "edam:data_2586"
    """
    An image arising from a Northern Blot experiment.
    """
    Blot_ID = "edam:data_2587"
    """
    Unique identifier of a blot from a Northern Blot.
    """
    BlotBase_blot_ID = "edam:data_2588"
    """
    Unique identifier of a blot from a Northern Blot from the BlotBase database.
    """
    Hierarchy = "edam:data_2589"
    """
    Raw data on a biological hierarchy, describing the hierarchy proper, hierarchy components and possibly associated annotation.
    """
    Brite_hierarchy_ID = "edam:data_2591"
    """
    Identifier of an entry from the Brite database of biological hierarchies.
    """
    BRENDA_organism_ID = "edam:data_2593"
    """
    A unique identifier for an organism used in the BRENDA database.
    """
    UniGene_taxon = "edam:data_2594"
    """
    The name of a taxon using the controlled vocabulary of the UniGene database.
    """
    UTRdb_taxon = "edam:data_2595"
    """
    The name of a taxon using the controlled vocabulary of the UTRdb database.
    """
    Catalogue_ID = "edam:data_2596"
    """
    An identifier of a catalogue of biological resources.
    """
    CABRI_catalogue_name = "edam:data_2597"
    """
    The name of a catalogue of biological resources from the CABRI database.
    """
    Pathway_or_network = "edam:data_2600"
    """
    Primary data about a specific biological pathway or network (the nodes and connections within the pathway or network).
    """
    Expression_data = "edam:data_2603"
    """
    Image, hybridisation or some other data arising from a study of feature/molecule expression, typically profiling or quantification.
    """
    Compound_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "edam:data_2605"
    """
    Unique identifier of a chemical compound from the KEGG database.
    """
    RFAM_name = "edam:data_2606"
    """
    Name (not necessarily stable) an entry (RNA family) from the RFAM database.
    """
    Reaction_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "edam:data_2608"
    """
    Identifier of a biological reaction from the KEGG reactions database.
    """
    Drug_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "edam:data_2609"
    """
    Unique identifier of a drug from the KEGG Drug database.
    """
    Ensembl_ID = "edam:data_2610"
    """
    Identifier of an entry (exon, gene, transcript or protein) from the Ensembl database.
    """
    ICD_identifier = "edam:data_2611"
    """
    An identifier of a disease from the International Classification of Diseases (ICD) database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISCluSTrRIGHT_PARENTHESIS = "edam:data_2612"
    """
    Unique identifier of a sequence cluster from the CluSTr database.
    """
    KEGG_Glycan_ID = "edam:data_2613"
    """
    Unique identifier of a glycan ligand from the KEGG GLYCAN database (a subset of KEGG LIGAND).
    """
    TCDB_ID = "edam:data_2614"
    """
    A unique identifier of a family from the transport classification database (TCDB) of membrane transport proteins.
    """
    MINT_ID = "edam:data_2615"
    """
    Unique identifier of an entry from the MINT database of protein-protein interactions.
    """
    DIP_ID = "edam:data_2616"
    """
    Unique identifier of an entry from the DIP database of protein-protein interactions.
    """
    Signaling_Gateway_protein_ID = "edam:data_2617"
    """
    Unique identifier of a protein listed in the UCSD-Nature Signaling Gateway Molecule Pages database.
    """
    Protein_modification_ID = "edam:data_2618"
    """
    Identifier of a protein modification catalogued in a database.
    """
    RESID_ID = "edam:data_2619"
    """
    Identifier of a protein modification catalogued in the RESID database.
    """
    RGD_ID = "edam:data_2620"
    """
    Identifier of an entry from the RGD database.
    """
    TAIR_accession_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:data_2621"
    """
    Identifier of a protein sequence from the TAIR database.
    """
    Compound_ID_LEFT_PARENTHESISHMDBRIGHT_PARENTHESIS = "edam:data_2622"
    """
    Identifier of a small molecule metabolite from the Human Metabolome Database (HMDB).
    """
    LIPID_MAPS_ID = "edam:data_2625"
    """
    Identifier of an entry from the LIPID MAPS database.
    """
    PeptideAtlas_ID = "edam:data_2626"
    """
    Identifier of a peptide from the PeptideAtlas peptide databases.
    """
    BioGRID_interaction_ID = "edam:data_2628"
    """
    A unique identifier of an interaction from the BioGRID database.
    """
    Enzyme_ID_LEFT_PARENTHESISMEROPSRIGHT_PARENTHESIS = "edam:data_2629"
    """
    Unique identifier of a peptidase enzyme from the MEROPS database.
    """
    Mobile_genetic_element_ID = "edam:data_2630"
    """
    An identifier of a mobile genetic element.
    """
    ACLAME_ID = "edam:data_2631"
    """
    An identifier of a mobile genetic element from the Aclame database.
    """
    SGD_ID = "edam:data_2632"
    """
    Identifier of an entry from the Saccharomyces genome database (SGD).
    """
    Book_ID = "edam:data_2633"
    """
    Unique identifier of a book.
    """
    ISBN = "edam:data_2634"
    """
    The International Standard Book Number (ISBN) is for identifying printed books.
    """
    Compound_ID_LEFT_PARENTHESIS3DMETRIGHT_PARENTHESIS = "edam:data_2635"
    """
    Identifier of a metabolite from the 3DMET database.
    """
    MatrixDB_interaction_ID = "edam:data_2636"
    """
    A unique identifier of an interaction from the MatrixDB database.
    """
    cPath_ID = "edam:data_2637"
    """
    A unique identifier for pathways, reactions, complexes and small molecules from the cPath (Pathway Commons) database.
    """
    PubChem_bioassay_ID = "edam:data_2638"
    """
    Identifier of an assay from the PubChem database.
    """
    PubChem_ID = "edam:data_2639"
    """
    Identifier of an entry from the PubChem database.
    """
    Reaction_ID_LEFT_PARENTHESISMACieRIGHT_PARENTHESIS = "edam:data_2641"
    """
    Identifier of an enzyme reaction mechanism from the MACie database.
    """
    Gene_ID_LEFT_PARENTHESISmiRBaseRIGHT_PARENTHESIS = "edam:data_2642"
    """
    Identifier for a gene from the miRBase database.
    """
    Gene_ID_LEFT_PARENTHESISZFINRIGHT_PARENTHESIS = "edam:data_2643"
    """
    Identifier for a gene from the Zebrafish information network genome (ZFIN) database.
    """
    Reaction_ID_LEFT_PARENTHESISRheaRIGHT_PARENTHESIS = "edam:data_2644"
    """
    Identifier of an enzyme-catalysed reaction from the Rhea database.
    """
    Pathway_ID_LEFT_PARENTHESISUnipathwayRIGHT_PARENTHESIS = "edam:data_2645"
    """
    Identifier of a biological pathway from the Unipathway database.
    """
    Compound_ID_LEFT_PARENTHESISChEMBLRIGHT_PARENTHESIS = "edam:data_2646"
    """
    Identifier of a small molecular from the ChEMBL database.
    """
    LGICdb_identifier = "edam:data_2647"
    """
    Unique identifier of an entry from the Ligand-gated ion channel (LGICdb) database.
    """
    Reaction_kinetics_ID_LEFT_PARENTHESISSABIO_RKRIGHT_PARENTHESIS = "edam:data_2648"
    """
    Identifier of a biological reaction (kinetics entry) from the SABIO-RK reactions database.
    """
    PharmGKB_ID = "edam:data_2649"
    """
    Identifier of an entry from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Pathway_ID_LEFT_PARENTHESISPharmGKBRIGHT_PARENTHESIS = "edam:data_2650"
    """
    Identifier of a pathway from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Disease_ID_LEFT_PARENTHESISPharmGKBRIGHT_PARENTHESIS = "edam:data_2651"
    """
    Identifier of a disease from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Drug_ID_LEFT_PARENTHESISPharmGKBRIGHT_PARENTHESIS = "edam:data_2652"
    """
    Identifier of a drug from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Drug_ID_LEFT_PARENTHESISTTDRIGHT_PARENTHESIS = "edam:data_2653"
    """
    Identifier of a drug from the Therapeutic Target Database (TTD).
    """
    Target_ID_LEFT_PARENTHESISTTDRIGHT_PARENTHESIS = "edam:data_2654"
    """
    Identifier of a target protein from the Therapeutic Target Database (TTD).
    """
    Cell_type_identifier = "edam:data_2655"
    """
    A unique identifier of a type or group of cells.
    """
    NeuronDB_ID = "edam:data_2656"
    """
    A unique identifier of a neuron from the NeuronDB database.
    """
    NeuroMorpho_ID = "edam:data_2657"
    """
    A unique identifier of a neuron from the NeuroMorpho database.
    """
    Compound_ID_LEFT_PARENTHESISChemIDplusRIGHT_PARENTHESIS = "edam:data_2658"
    """
    Identifier of a chemical from the ChemIDplus database.
    """
    Pathway_ID_LEFT_PARENTHESISSMPDBRIGHT_PARENTHESIS = "edam:data_2659"
    """
    Identifier of a pathway from the Small Molecule Pathway Database (SMPDB).
    """
    BioNumbers_ID = "edam:data_2660"
    """
    Identifier of an entry from the BioNumbers database of key numbers and associated data in molecular biology.
    """
    T3DB_ID = "edam:data_2662"
    """
    Unique identifier of a toxin from the Toxin and Toxin Target Database (T3DB) database.
    """
    Carbohydrate_identifier = "edam:data_2663"
    """
    Identifier of a carbohydrate.
    """
    GlycomeDB_ID = "edam:data_2664"
    """
    Identifier of an entry from the GlycomeDB database.
    """
    LipidBank_ID = "edam:data_2665"
    """
    Identifier of an entry from the LipidBank database.
    """
    CDD_ID = "edam:data_2666"
    """
    Identifier of a conserved domain from the Conserved Domain Database.
    """
    MMDB_ID = "edam:data_2667"
    """
    An identifier of an entry from the MMDB database.
    """
    iRefIndex_ID = "edam:data_2668"
    """
    Unique identifier of an entry from the iRefIndex database of protein-protein interactions.
    """
    ModelDB_ID = "edam:data_2669"
    """
    Unique identifier of an entry from the ModelDB database.
    """
    Pathway_ID_LEFT_PARENTHESISDQCSRIGHT_PARENTHESIS = "edam:data_2670"
    """
    Identifier of a signaling pathway from the Database of Quantitative Cellular Signaling (DQCS).
    """
    CATH_identifier = "edam:data_2700"
    """
    Identifier of a protein domain (or other node) from the CATH database.
    """
    CATH_node_ID_LEFT_PARENTHESISfamilyRIGHT_PARENTHESIS = "edam:data_2701"
    """
    A code number identifying a family from the CATH database.
    """
    Enzyme_ID_LEFT_PARENTHESISCAZyRIGHT_PARENTHESIS = "edam:data_2702"
    """
    Identifier of an enzyme from the CAZy enzymes database.
    """
    Clone_ID_LEFT_PARENTHESISIMAGERIGHT_PARENTHESIS = "edam:data_2704"
    """
    A unique identifier assigned by the I.M.A.G.E. consortium to a clone (cloned molecular sequence).
    """
    GO_concept_ID_LEFT_PARENTHESIScellular_componentRIGHT_PARENTHESIS = "edam:data_2705"
    """
    An identifier of a 'cellular component' concept from the Gene Ontology.
    """
    Chromosome_name_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "edam:data_2706"
    """
    Name of a chromosome as used in the BioCyc database.
    """
    CleanEx_entry_name = "edam:data_2709"
    """
    An identifier of a gene expression profile from the CleanEx database.
    """
    CleanEx_dataset_code = "edam:data_2710"
    """
    An identifier of (typically a list of) gene expression experiments catalogued in the CleanEx database.
    """
    Genome_report = "edam:data_2711"
    """
    A human-readable collection of information concerning a genome as a whole.
    """
    Protein_ID_LEFT_PARENTHESISCORUMRIGHT_PARENTHESIS = "edam:data_2713"
    """
    Unique identifier for a protein complex from the CORUM database.
    """
    CDD_PSSM_ID = "edam:data_2714"
    """
    Unique identifier of a position-specific scoring matrix from the CDD database.
    """
    Protein_ID_LEFT_PARENTHESISCuticleDBRIGHT_PARENTHESIS = "edam:data_2715"
    """
    Unique identifier for a protein from the CuticleDB database.
    """
    DBD_ID = "edam:data_2716"
    """
    Identifier of a predicted transcription factor from the DBD database.
    """
    Oligonucleotide_probe_annotation = "edam:data_2717"
    """
    General annotation on an oligonucleotide probe, or a set of probes.
    """
    Oligonucleotide_ID = "edam:data_2718"
    """
    Identifier of an oligonucleotide from a database.
    """
    dbProbe_ID = "edam:data_2719"
    """
    Identifier of an oligonucleotide probe from the dbProbe database.
    """
    Dinucleotide_property = "edam:data_2720"
    """
    Physicochemical property data for one or more dinucleotides.
    """
    DiProDB_ID = "edam:data_2721"
    """
    Identifier of an dinucleotide property from the DiProDB database.
    """
    Protein_ID_LEFT_PARENTHESISDisProtRIGHT_PARENTHESIS = "edam:data_2723"
    """
    Unique identifier for a protein from the DisProt database.
    """
    Ensembl_transcript_ID = "edam:data_2725"
    """
    Unique identifier for a gene transcript from the Ensembl database.
    """
    Promoter_ID = "edam:data_2727"
    """
    An identifier of a promoter of a gene that is catalogued in a database.
    """
    EST_accession = "edam:data_2728"
    """
    Identifier of an EST sequence.
    """
    COGEME_EST_ID = "edam:data_2729"
    """
    Identifier of an EST sequence from the COGEME database.
    """
    COGEME_unisequence_ID = "edam:data_2730"
    """
    Identifier of a unisequence from the COGEME database.
    """
    Protein_family_ID_LEFT_PARENTHESISGeneFarmRIGHT_PARENTHESIS = "edam:data_2731"
    """
    Accession number of an entry (protein family) from the GeneFarm database.
    """
    Family_name = "edam:data_2732"
    """
    The name of a family of organism.
    """
    Sequence_feature_ID_LEFT_PARENTHESISSwissRegulonRIGHT_PARENTHESIS = "edam:data_2736"
    """
    A feature identifier as used in the SwissRegulon database.
    """
    FIG_ID = "edam:data_2737"
    """
    A unique identifier of gene in the NMPDR database.
    """
    Gene_ID_LEFT_PARENTHESISXenbaseRIGHT_PARENTHESIS = "edam:data_2738"
    """
    A unique identifier of gene in the Xenbase database.
    """
    Gene_ID_LEFT_PARENTHESISGenolistRIGHT_PARENTHESIS = "edam:data_2739"
    """
    A unique identifier of gene in the Genolist database.
    """
    ABS_ID = "edam:data_2741"
    """
    Identifier of an entry (promoter) from the ABS database.
    """
    AraC_XylS_ID = "edam:data_2742"
    """
    Identifier of a transcription factor from the AraC-XylS database.
    """
    Locus_ID_LEFT_PARENTHESISPseudoCAPRIGHT_PARENTHESIS = "edam:data_2744"
    """
    Identifier of a locus from the PseudoCAP database.
    """
    Locus_ID_LEFT_PARENTHESISUTRRIGHT_PARENTHESIS = "edam:data_2745"
    """
    Identifier of a locus from the UTR database.
    """
    MonosaccharideDB_ID = "edam:data_2746"
    """
    Unique identifier of a monosaccharide from the MonosaccharideDB database.
    """
    Genome_identifier = "edam:data_2749"
    """
    An identifier of a particular genome.
    """
    GlycoMap_ID = "edam:data_2752"
    """
    Identifier of an entry from the GlycoMapsDB (Glycosciences.de) database.
    """
    Carbohydrate_conformational_map = "edam:data_2753"
    """
    A conformational energy map of the glycosidic linkages in a carbohydrate molecule.
    """
    Transcription_factor_name = "edam:data_2755"
    """
    The name of a transcription factor.
    """
    TCID = "edam:data_2756"
    """
    Identifier of a membrane transport proteins from the transport classification database (TCDB).
    """
    Pfam_domain_name = "edam:data_2757"
    """
    Name of a domain from the Pfam database.
    """
    Pfam_clan_ID = "edam:data_2758"
    """
    Accession number of a Pfam clan.
    """
    Gene_ID_LEFT_PARENTHESISVectorBaseRIGHT_PARENTHESIS = "edam:data_2759"
    """
    Identifier for a gene from the VectorBase database.
    """
    UTRSite_ID = "edam:data_2761"
    """
    Identifier of an entry from the UTRSite database of regulatory motifs in eukaryotic UTRs.
    """
    Sequence_signature_report = "edam:data_2762"
    """
    An informative report about a specific or conserved pattern in a molecular sequence, such as its context in genes or proteins, its role, origin or method of construction, etc.
    """
    Protein_name_LEFT_PARENTHESISUniProtRIGHT_PARENTHESIS = "edam:data_2764"
    """
    Official name of a protein as used in the UniProt database.
    """
    HAMAP_ID = "edam:data_2766"
    """
    Name of a protein family from the HAMAP database.
    """
    Transcript_ID = "edam:data_2769"
    """
    Identifier of a RNA transcript.
    """
    HIT_ID = "edam:data_2770"
    """
    Identifier of an RNA transcript from the H-InvDB database.
    """
    HIX_ID = "edam:data_2771"
    """
    A unique identifier of gene cluster in the H-InvDB database.
    """
    HPA_antibody_id = "edam:data_2772"
    """
    Identifier of a antibody from the HPA database.
    """
    IMGTSOLIDUSHLA_ID = "edam:data_2773"
    """
    Identifier of a human major histocompatibility complex (HLA) or other protein from the IMGT/HLA database.
    """
    Gene_ID_LEFT_PARENTHESISJCVIRIGHT_PARENTHESIS = "edam:data_2774"
    """
    A unique identifier of gene assigned by the J. Craig Venter Institute (JCVI).
    """
    Kinase_name = "edam:data_2775"
    """
    The name of a kinase protein.
    """
    ConsensusPathDB_entity_ID = "edam:data_2776"
    """
    Identifier of a physical entity from the ConsensusPathDB database.
    """
    ConsensusPathDB_entity_name = "edam:data_2777"
    """
    Name of a physical entity from the ConsensusPathDB database.
    """
    CCAP_strain_number = "edam:data_2778"
    """
    The number of a strain of algae and protozoa from the CCAP database.
    """
    Stock_number = "edam:data_2779"
    """
    An identifier of stock from a catalogue of biological resources.
    """
    Stock_number_LEFT_PARENTHESISTAIRRIGHT_PARENTHESIS = "edam:data_2780"
    """
    A stock number from The Arabidopsis information resource (TAIR).
    """
    REDIdb_ID = "edam:data_2781"
    """
    Identifier of an entry from the RNA editing database (REDIdb).
    """
    SMART_domain_name = "edam:data_2782"
    """
    Name of a domain from the SMART database.
    """
    Protein_family_ID_LEFT_PARENTHESISPANTHERRIGHT_PARENTHESIS = "edam:data_2783"
    """
    Accession number of an entry (family) from the PANTHER database.
    """
    RNAVirusDB_ID = "edam:data_2784"
    """
    A unique identifier for a virus from the RNAVirusDB database.
    """
    Virus_identifier = "edam:data_2785"
    """
    An accession of annotation on a (group of) viruses (catalogued in a database).
    """
    NCBI_Genome_Project_ID = "edam:data_2786"
    """
    An identifier of a genome project assigned by NCBI.
    """
    NCBI_genome_accession = "edam:data_2787"
    """
    A unique identifier of a whole genome assigned by the NCBI.
    """
    Protein_ID_LEFT_PARENTHESISTopDBRIGHT_PARENTHESIS = "edam:data_2789"
    """
    Unique identifier for a membrane protein from the TopDB database.
    """
    Gel_ID = "edam:data_2790"
    """
    Identifier of a two-dimensional (protein) gel.
    """
    Reference_map_name_LEFT_PARENTHESISSWISS_2DPAGERIGHT_PARENTHESIS = "edam:data_2791"
    """
    Name of a reference map gel from the SWISS-2DPAGE database.
    """
    Protein_ID_LEFT_PARENTHESISPeroxiBaseRIGHT_PARENTHESIS = "edam:data_2792"
    """
    Unique identifier for a peroxidase protein from the PeroxiBase database.
    """
    SISYPHUS_ID = "edam:data_2793"
    """
    Identifier of an entry from the SISYPHUS database of tertiary structure alignments.
    """
    ORF_ID = "edam:data_2794"
    """
    Accession of an open reading frame (catalogued in a database).
    """
    ORF_identifier = "edam:data_2795"
    """
    An identifier of an open reading frame.
    """
    LINUCS_ID = "edam:data_2796"
    """
    Identifier of an entry from the GlycosciencesDB database.
    """
    Protein_ID_LEFT_PARENTHESISLGICdbRIGHT_PARENTHESIS = "edam:data_2797"
    """
    Unique identifier for a ligand-gated ion channel protein from the LGICdb database.
    """
    MaizeDB_ID = "edam:data_2798"
    """
    Identifier of an EST sequence from the MaizeDB database.
    """
    Gene_ID_LEFT_PARENTHESISMfunGDRIGHT_PARENTHESIS = "edam:data_2799"
    """
    A unique identifier of gene in the MfunGD database.
    """
    Orpha_number = "edam:data_2800"
    """
    An identifier of a disease from the Orpha database.
    """
    Protein_ID_LEFT_PARENTHESISEcIDRIGHT_PARENTHESIS = "edam:data_2802"
    """
    Unique identifier for a protein from the EcID database.
    """
    Clone_ID_LEFT_PARENTHESISRefSeqRIGHT_PARENTHESIS = "edam:data_2803"
    """
    A unique identifier of a cDNA molecule catalogued in the RefSeq database.
    """
    Protein_ID_LEFT_PARENTHESISConoServerRIGHT_PARENTHESIS = "edam:data_2804"
    """
    Unique identifier for a cone snail toxin protein from the ConoServer database.
    """
    GeneSNP_ID = "edam:data_2805"
    """
    Identifier of a GeneSNP database entry.
    """
    Lipid_identifier = "edam:data_2812"
    """
    Identifier of a lipid.
    """
    Gene_ID_LEFT_PARENTHESISVBASE2RIGHT_PARENTHESIS = "edam:data_2835"
    """
    Identifier for a gene from the VBASE2 database.
    """
    DPVweb_ID = "edam:data_2836"
    """
    A unique identifier for a virus from the DPVweb database.
    """
    Pathway_ID_LEFT_PARENTHESISBioSystemsRIGHT_PARENTHESIS = "edam:data_2837"
    """
    Identifier of a pathway from the BioSystems pathway database.
    """
    Abstract = "edam:data_2849"
    """
    An abstract of a scientific article.
    """
    Lipid_structure = "edam:data_2850"
    """
    3D coordinate and associated data for a lipid structure.
    """
    Drug_structure = "edam:data_2851"
    """
    3D coordinate and associated data for the (3D) structure of a drug.
    """
    Toxin_structure = "edam:data_2852"
    """
    3D coordinate and associated data for the (3D) structure of a toxin.
    """
    Position_specific_scoring_matrix = "edam:data_2854"
    """
    A simple matrix of numbers, where each value (or column of values) is derived derived from analysis of the corresponding position in a sequence alignment.
    """
    Distance_matrix = "edam:data_2855"
    """
    A matrix of distances between molecular entities, where a value (distance) is (typically) derived from comparison of two entities and reflects their similarity.
    """
    Structural_distance_matrix = "edam:data_2856"
    """
    Distances (values representing similarity) between a group of molecular structures.
    """
    Ontology_concept = "edam:data_2858"
    """
    A concept from a biological ontology.
    """
    Codon_usage_bias = "edam:data_2865"
    """
    A numerical measure of differences in the frequency of occurrence of synonymous codons in DNA sequences.
    """
    Radiation_hybrid_map = "edam:data_2870"
    """
    A map showing distance between genetic markers estimated by radiation-induced breaks in a chromosome.
    """
    ID_list = "edam:data_2872"
    """
    A simple list of data identifiers (such as database accessions), possibly with additional basic information on the addressed data.
    """
    Phylogenetic_gene_frequencies_data = "edam:data_2873"
    """
    Gene frequencies data that may be read during phylogenetic tree calculation.
    """
    Protein_complex = "edam:data_2877"
    """
    3D coordinate and associated data for a multi-protein complex; two or more polypeptides chains in a stable, functional association with one another.
    """
    Protein_structural_motif = "edam:data_2878"
    """
    3D coordinate and associated data for a protein (3D) structural motif; any group of contiguous or non-contiguous amino acid residues but typically those forming a feature with a structural or functional role.
    """
    Lipid_report = "edam:data_2879"
    """
    A human-readable collection of information about one or more specific lipid 3D structure(s).
    """
    Plot = "edam:data_2884"
    """
    Biological data that has been plotted as a graph of some type, or plotting instructions for rendering such a graph.
    """
    Protein_sequence_record = "edam:data_2886"
    """
    A protein sequence and associated metadata.
    """
    Nucleic_acid_sequence_record = "edam:data_2887"
    """
    A nucleic acid sequence and associated metadata.
    """
    Biological_model_accession = "edam:data_2891"
    """
    Accession of a mathematical model, typically an entry from a database.
    """
    Cell_type_name = "edam:data_2892"
    """
    The name of a type or group of cells.
    """
    Cell_type_accession = "edam:data_2893"
    """
    Accession of a type or group of cells (catalogued in a database).
    """
    Compound_accession = "edam:data_2894"
    """
    Accession of an entry from a database of chemicals.
    """
    Drug_accession = "edam:data_2895"
    """
    Accession of a drug.
    """
    Toxin_name = "edam:data_2896"
    """
    Name of a toxin.
    """
    Toxin_accession = "edam:data_2897"
    """
    Accession of a toxin (catalogued in a database).
    """
    Monosaccharide_accession = "edam:data_2898"
    """
    Accession of a monosaccharide (catalogued in a database).
    """
    Drug_name = "edam:data_2899"
    """
    Common name of a drug.
    """
    Carbohydrate_accession = "edam:data_2900"
    """
    Accession of an entry from a database of carbohydrates.
    """
    Molecule_accession = "edam:data_2901"
    """
    Molecule accession is any persistent, unique identifier of a specific molecule (catalogued in a database).
    """
    Data_resource_definition_accession = "edam:data_2902"
    """
    Accession of a data definition (catalogued in a database).
    """
    Genome_accession = "edam:data_2903"
    """
    An accession of a particular genome (in a database).
    """
    Map_accession = "edam:data_2904"
    """
    An accession of a map of a molecular sequence (deposited in a database).
    """
    Lipid_accession = "edam:data_2905"
    """
    Accession of an entry from a database of lipids.
    """
    Peptide_ID = "edam:data_2906"
    """
    Accession of a peptide deposited in a database.
    """
    Protein_accession = "edam:data_2907"
    """
    Accession of a protein deposited in a database.
    """
    Organism_accession = "edam:data_2908"
    """
    An accession of annotation on a (group of) organisms (catalogued in a database).
    """
    Organism_name = "edam:data_2909"
    """
    The name of an organism (or group of organisms).
    """
    Protein_family_accession = "edam:data_2910"
    """
    Accession of a protein family (that is deposited in a database).
    """
    Transcription_factor_accession = "edam:data_2911"
    """
    Accession of an entry from a database of transcription factors or binding sites.
    """
    Strain_accession = "edam:data_2912"
    """
    Accession number of a strain of an organism variant, typically a plant, virus or bacterium.
    """
    Sequence_features_metadata = "edam:data_2914"
    """
    Metadata on sequence features.
    """
    Gramene_identifier = "edam:data_2915"
    """
    Identifier of a Gramene database entry.
    """
    DDBJ_accession = "edam:data_2916"
    """
    An identifier of an entry from the DDBJ sequence database.
    """
    ConsensusPathDB_identifier = "edam:data_2917"
    """
    An identifier of an entity from the ConsensusPathDB database.
    """
    Sequence_report = "edam:data_2955"
    """
    An informative report of information about molecular sequence(s), including basic information (metadata), and reports generated from molecular sequence analysis, including positional features and non-positional properties.
    """
    Protein_secondary_structure = "edam:data_2956"
    """
    Data concerning the properties or features of one or more protein secondary structures.
    """
    Hopp_and_Woods_plot = "edam:data_2957"
    """
    A Hopp and Woods plot of predicted antigenicity of a peptide or protein.
    """
    Image = "edam:data_2968"
    """
    Data (typically biological or biomedical) that has been rendered into an image, typically for display on screen.
    """
    Sequence_image = "edam:data_2969"
    """
    Image of a molecular sequence, possibly with sequence features or properties shown.
    """
    Protein_hydropathy_data = "edam:data_2970"
    """
    A report on protein properties concerning hydropathy.
    """
    Protein_sequence = "edam:data_2976"
    """
    One or more protein sequences, possibly with associated annotation.
    """
    Nucleic_acid_sequence = "edam:data_2977"
    """
    One or more nucleic acid sequences, possibly with associated annotation.
    """
    Reaction_data = "edam:data_2978"
    """
    Data concerning a biochemical reaction, typically data and more general annotation on the kinetics of enzyme-catalysed reaction.
    """
    Peptide_property = "edam:data_2979"
    """
    Data concerning small peptides.
    """
    Pathway_or_network_report = "edam:data_2984"
    """
    An informative report concerning or derived from the analysis of a biological pathway or network, such as a map (diagram) or annotation.
    """
    Nucleic_acid_thermodynamic_data = "edam:data_2985"
    """
    A thermodynamic or kinetic property of a nucleic acid molecule.
    """
    Protein_geometry_data = "edam:data_2991"
    """
    Geometry data for a protein structure, for example bond lengths, bond angles, torsion angles, chiralities, planaraties etc.
    """
    Protein_structure_image = "edam:data_2992"
    """
    An image of protein structure.
    """
    Phylogenetic_character_weights = "edam:data_2994"
    """
    Weights for sequence positions or characters in phylogenetic analysis where zero is defined as unweighted.
    """
    Annotation_track = "edam:data_3002"
    """
    Annotation of one particular positional feature on a biomolecular (typically genome) sequence, suitable for import and display in a genome browser.
    """
    UniProt_accession = "edam:data_3021"
    """
    Accession number of a UniProt (protein sequence) database entry.
    """
    NCBI_genetic_code_ID = "edam:data_3022"
    """
    Identifier of a genetic code in the NCBI list of genetic codes.
    """
    Ontology_concept_identifier = "edam:data_3025"
    """
    Identifier of a concept in an ontology of biological or bioinformatics concepts and relations.
    """
    Taxonomy = "edam:data_3028"
    """
    Data concerning the classification, identification and naming of organisms.
    """
    Protein_ID_LEFT_PARENTHESISEMBLSOLIDUSGenBankSOLIDUSDDBJRIGHT_PARENTHESIS = "edam:data_3029"
    """
    EMBL/GENBANK/DDBJ coding feature protein identifier, issued by International collaborators.
    """
    Sequence_feature_identifier = "edam:data_3034"
    """
    Name or other identifier of molecular sequence feature(s).
    """
    Structure_identifier = "edam:data_3035"
    """
    An identifier of a molecular tertiary structure, typically an entry from a structure database.
    """
    Matrix_identifier = "edam:data_3036"
    """
    An identifier of an array of numerical values, such as a comparison matrix.
    """
    ATC_code = "edam:data_3103"
    """
    Unique identifier of a drug conforming to the Anatomical Therapeutic Chemical (ATC) Classification System, a drug classification system controlled by the WHO Collaborating Centre for Drug Statistics Methodology (WHOCC).
    """
    UNII = "edam:data_3104"
    """
    A unique, unambiguous, alphanumeric identifier of a chemical substance as catalogued by the Substance Registration System of the Food and Drug Administration (FDA).
    """
    System_metadata = "edam:data_3106"
    """
    Metadata concerning the software, hardware or other aspects of a computer system.
    """
    Experimental_measurement = "edam:data_3108"
    """
    Raw data such as measurements or other results from laboratory experiments, as generated from laboratory hardware.
    """
    Raw_microarray_data = "edam:data_3110"
    """
    Raw data (typically MIAME-compliant) for hybridisations from a microarray experiment.
    """
    Processed_microarray_data = "edam:data_3111"
    """
    Data generated from processing and analysis of probe set data from a microarray experiment.
    """
    Gene_expression_matrix = "edam:data_3112"
    """
    The final processed (normalised) data for a set of hybridisations in a microarray experiment.
    """
    Sample_annotation = "edam:data_3113"
    """
    Annotation on a biological sample, for example experimental factors and their values.
    """
    Microarray_metadata = "edam:data_3115"
    """
    Annotation on the array itself used in a microarray experiment.
    """
    Microarray_hybridisation_data = "edam:data_3117"
    """
    Data concerning the hybridisations measured during a microarray experiment.
    """
    Nucleic_acid_structure_report = "edam:data_3128"
    """
    A human-readable collection of information about regions within a nucleic acid sequence which form secondary or tertiary (3D) structures.
    """
    Gene_transcript_report = "edam:data_3134"
    """
    An informative report on features of a messenger RNA (mRNA) molecules including precursor RNA, primary (unprocessed) transcript and fully processed molecules. This includes reports on a specific gene transcript, clone or EST.
    """
    Gene_family_report = "edam:data_3148"
    """
    A human-readable collection of information about a particular family of genes, typically a set of genes with similar sequence that originate from duplication of a common ancestor gene, or any other classification of nucleic acid sequences or structures that reflects gene structure.
    """
    Protein_image = "edam:data_3153"
    """
    An image of a protein.
    """
    Sequence_assembly_report = "edam:data_3181"
    """
    An informative report about a DNA sequence assembly.
    """
    Genome_index = "edam:data_3210"
    """
    An index of a genome sequence.
    """
    Cytoband_position = "edam:data_3236"
    """
    The position of a cytogenetic band in a genome.
    """
    Cell_type_ontology_ID = "edam:data_3238"
    """
    Cell type ontology concept ID.
    """
    Kinetic_model = "edam:data_3241"
    """
    Mathematical model of a network, that contains biochemical kinetics.
    """
    COSMIC_ID = "edam:data_3264"
    """
    Identifier of a COSMIC database entry.
    """
    HGMD_ID = "edam:data_3265"
    """
    Identifier of a HGMD database entry.
    """
    Sequence_assembly_ID = "edam:data_3266"
    """
    Unique identifier of sequence assembly.
    """
    Ensembl_gene_tree_ID = "edam:data_3270"
    """
    Unique identifier for a gene tree from the Ensembl database.
    """
    Gene_tree = "edam:data_3271"
    """
    A phylogenetic tree that is an estimate of the character's phylogeny.
    """
    Species_tree = "edam:data_3272"
    """
    A phylogenetic tree that reflects phylogeny of the taxa from which the characters (used in calculating the tree) were sampled.
    """
    Sample_ID = "edam:data_3273"
    """
    Name or other identifier of an entry from a biosample database.
    """
    MGI_accession = "edam:data_3274"
    """
    Identifier of an object from the MGI database.
    """
    Phenotype_name = "edam:data_3275"
    """
    Name of a phenotype.
    """
    Transition_matrix = "edam:data_3354"
    """
    A HMM transition matrix contains the probabilities of switching from one HMM state to another.
    """
    Emission_matrix = "edam:data_3355"
    """
    A HMM emission matrix holds the probabilities of choosing the four nucleotides (A, C, G and T) in each of the states of a HMM.
    """
    Format_identifier = "edam:data_3358"
    """
    An identifier of a data format.
    """
    Raw_image = "edam:data_3424"
    """
    Raw biological or biomedical image generated by some experimental technique.
    """
    Carbohydrate_property = "edam:data_3425"
    """
    Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all carbohydrates.
    """
    MRI_image = "edam:data_3442"
    """
    An imaging technique that uses magnetic fields and radiowaves to form images, typically to investigate the anatomy and physiology of the human body.
    """
    Cell_migration_track_image = "edam:data_3449"
    """
    An image from a cell migration track assay.
    """
    Rate_of_association = "edam:data_3451"
    """
    Rate of association of a protein with another protein or some other molecule.
    """
    Gene_order = "edam:data_3479"
    """
    Multiple gene identifiers in a specific order.
    """
    Spectrum = "edam:data_3483"
    """
    The spectrum of frequencies of electromagnetic radiation emitted from a molecule as a result of some spectroscopy experiment.
    """
    NMR_spectrum = "edam:data_3488"
    """
    Spectral information for a molecule from a nuclear magnetic resonance experiment.
    """
    Nucleic_acid_signature = "edam:data_3492"
    """
    An informative report about a specific or conserved nucleic acid sequence pattern.
    """
    DNA_sequence = "edam:data_3494"
    """
    A DNA sequence.
    """
    RNA_sequence = "edam:data_3495"
    """
    An RNA sequence.
    """
    Sequence_variations = "edam:data_3498"
    """
    Data on gene sequence variations resulting large-scale genotyping and DNA sequencing projects.
    """
    Bibliography = "edam:data_3505"
    """
    A list of publications such as scientic papers or books.
    """
    Ontology_mapping = "edam:data_3509"
    """
    A mapping of supplied textual terms or phrases to ontology concepts (URIs).
    """
    Image_metadata = "edam:data_3546"
    """
    Any data concerning a specific biological or biomedical image.
    """
    Clinical_trial_report = "edam:data_3558"
    """
    A human-readable collection of information concerning a clinical trial.
    """
    Reference_sample_report = "edam:data_3567"
    """
    A report about a biosample.
    """
    Gene_Expression_Atlas_Experiment_ID = "edam:data_3568"
    """
    Accession number of an entry from the Gene Expression Atlas.
    """
    Disease_identifier = "edam:data_3667"
    """
    Identifier of an entry from a database of disease.
    """
    Disease_name = "edam:data_3668"
    """
    The name of some disease.
    """
    Learning_material = "edam:data_3669"
    """
    Learning material is a document or another digital object that is designed for learning (educational, training) purposes.
    """
    Online_course = "edam:data_3670"
    """
    A training course available for use on the Web.
    """
    Text = "edam:data_3671"
    """
    Any free or plain text, typically for human consumption and in English. Can instantiate also as a textual search query.
    """
    Biodiversity_data = "edam:data_3707"
    """
    Machine-readable biodiversity data.
    """
    Biosafety_report = "edam:data_3716"
    """
    A human-readable collection of information concerning biosafety data.
    """
    Isolation_report = "edam:data_3717"
    """
    A report about any kind of isolation of biological material.
    """
    Pathogenicity_report = "edam:data_3718"
    """
    Information about the ability of an organism to cause disease in a corresponding host.
    """
    Biosafety_classification = "edam:data_3719"
    """
    Information about the biosafety classification of an organism according to corresponding law.
    """
    Geographic_location = "edam:data_3720"
    """
    A report about localisation of the isolaton of biological material e.g. country or coordinates.
    """
    Isolation_source = "edam:data_3721"
    """
    A report about any kind of isolation source of biological material e.g. blood, water, soil.
    """
    Physiology_parameter = "edam:data_3722"
    """
    Experimentally determined parameter of the physiology of an organism, e.g. substrate spectrum.
    """
    Morphology_parameter = "edam:data_3723"
    """
    Experimentally determined parameter of the morphology of an organism, e.g. size & shape.
    """
    Cultivation_parameter = "edam:data_3724"
    """
    Experimental determined parameter for the cultivation of an organism.
    """
    Sequencing_metadata_name = "edam:data_3732"
    """
    Data concerning a sequencing experiment, that may be specified as an input to some tool.
    """
    Flow_cell_identifier = "edam:data_3733"
    """
    An identifier of a flow cell of a sequencing machine.
    """
    Lane_identifier = "edam:data_3734"
    """
    An identifier of a lane within a flow cell of a sequencing machine, within which millions of sequences are immobilised, amplified and sequenced.
    """
    Run_number = "edam:data_3735"
    """
    A number corresponding to the number of an analysis performed by a sequencing machine. For example, if it's the 13th analysis, the run is 13.
    """
    Ecological_data = "edam:data_3736"
    """
    Data concerning ecology; for example measurements and reports from the study of interactions among organisms and their environment.
    """
    Alpha_diversity_data = "edam:data_3737"
    """
    The mean species diversity in sites or habitats at a local scale.
    """
    Beta_diversity_data = "edam:data_3738"
    """
    The ratio between regional and local species diversity.
    """
    Gamma_diversity_data = "edam:data_3739"
    """
    The total species diversity in a landscape.
    """
    Ordination_plot = "edam:data_3743"
    """
    A plot in which community data (e.g. species abundance data) is summarised. Similar species and samples are plotted close together, and dissimilar species and samples are plotted placed far apart.
    """
    Over_representation_data = "edam:data_3753"
    """
    A ranked list of categories (usually ontology concepts), each associated with a statistical metric of over-/under-representation within the studied data.
    """
    GO_term_enrichment_data = "edam:data_3754"
    """
    A ranked list of Gene Ontology concepts, each associated with a p-value, concerning or derived from the analysis of e.g. a set of genes or proteins.
    """
    Localisation_score = "edam:data_3756"
    """
    Score for localization of one or more post-translational modifications in peptide sequence measured by mass spectrometry.
    """
    Unimod_ID = "edam:data_3757"
    """
    Identifier of a protein modification catalogued in the Unimod database.
    """
    ProteomeXchange_ID = "edam:data_3759"
    """
    Identifier for mass spectrometry proteomics data in the proteomexchange.org repository.
    """
    Clustered_expression_profiles = "edam:data_3768"
    """
    Groupings of expression profiles according to a clustering algorithm.
    """
    BRENDA_ontology_concept_ID = "edam:data_3769"
    """
    An identifier of a concept from the BRENDA ontology.
    """
    Annotated_text = "edam:data_3779"
    """
    A text (such as a scientific article), annotated with notes, data and metadata, such as recognised entities, concepts, and their relations.
    """
    Query_script = "edam:data_3786"
    """
    A structured query, in form of a script, that defines a database search task.
    """
    number_3D_EM_Map = "edam:data_3805"
    """
    Structural 3D model (volume map) from electron microscopy.
    """
    number_3D_EM_Mask = "edam:data_3806"
    """
    Annotation on a structural 3D EM Map from electron microscopy. This might include one or several locations in the map of the known features of a particular macromolecule.
    """
    EM_Movie = "edam:data_3807"
    """
    Raw DDD movie acquisition from electron microscopy.
    """
    EM_Micrograph = "edam:data_3808"
    """
    Raw acquisition from electron microscopy or average of an aligned DDD movie.
    """
    Molecular_simulation_data = "edam:data_3842"
    """
    Data coming from molecular simulations, computer "experiments" on model molecules.
    """
    RNA_central_ID = "edam:data_3856"
    """
    Identifier of an entry from the RNA central database of annotated human miRNAs.
    """
    Electronic_health_record = "edam:data_3861"
    """
    A human-readable systematic collection of patient (or population) health information in a digital format.
    """
    Simulation = "edam:data_3869"
    """
    Data coming from molecular simulations, computer "experiments" on model molecules. Typically formed by two separated but indivisible pieces of information: topology data (static) and trajectory data (dynamic).
    """
    Trajectory_data = "edam:data_3870"
    """
    Dynamic information of a structure molecular system coming from a molecular simulation: XYZ 3D coordinates (sometimes with their associated velocities) for every atom along time.
    """
    Forcefield_parameters = "edam:data_3871"
    """
    Force field parameters: charges, masses, radii, bond lengths, bond dihedrals, etc. define the structural molecular system, and are essential for the proper description and simulation of a molecular system.
    """
    Topology_data = "edam:data_3872"
    """
    Static information of a structure molecular system that is needed for a molecular simulation: the list of atoms, their non-bonded parameters for Van der Waals and electrostatic interactions, and the complete connectivity in terms of bonds, angles and dihedrals.
    """
    Histogram = "edam:data_3905"
    """
    Visualization of distribution of quantitative data, e.g. expression data, by histograms, violin plots and density plots.
    """
    Quality_control_report = "edam:data_3914"
    """
    Report of the quality control review that was made of factors involved in a procedure.
    """
    Count_matrix = "edam:data_3917"
    """
    A table of unnormalized values representing summarised read counts per genomic region (e.g. gene, transcript, peak).
    """
    DNA_structure_alignment = "edam:data_3924"
    """
    Alignment (superimposition) of DNA tertiary (3D) structures.
    """
    Q_value = "edam:data_3932"
    """
    A score derived from the P-value to ensure correction for multiple tests. The Q-value provides an estimate of the positive False Discovery Rate (pFDR), i.e. the rate of false positives among all the cases reported positive: pFDR = FP / (FP + TP).
    """
    Profile_HMM = "edam:data_3949"
    """
    A profile HMM is a variant of a Hidden Markov model that is derived specifically from a set of (aligned) biological sequences. Profile HMMs provide the basis for a position-specific scoring system, which can be used to align sequences and search databases for related sequences.
    """
    Pathway_ID_LEFT_PARENTHESISWikiPathwaysRIGHT_PARENTHESIS = "edam:data_3952"
    """
    Identifier of a pathway from the WikiPathways pathway database.
    """
    Pathway_overrepresentation_data = "edam:data_3953"
    """
    A ranked list of pathways, each associated with z-score, p-value or similar, concerning or derived from the analysis of e.g. a set of genes or proteins.
    """
    ORCID_Identifier = "edam:data_4022"
    """
    Identifier of a researcher registered with the ORCID database. Used to identify author IDs.
    """
    Data_management_plan = "edam:data_4040"
    """
    Data management plan is a document describing the data management of a project or an organisation, including acquisition, reuse, structure, processing, storage, documentation, sharing, and preservation of data. This may include budgeting for these operations.
    """
    RefMet_ID = "edam:data_4075"
    """
    RefMet ID is the unique, persistent identifier used by the RefMet database (A Reference list of Metabolite names), a standardised reference nomenclature for metabolites.
    """


class EnumEDAMFormats(str, Enum):
    """
    Data formats from the EDAM ontology.
    """
    SMILES = "edam:format_1196"
    """
    Chemical structure specified in Simplified Molecular Input Line Entry System (SMILES) line notation.
    """
    InChI = "edam:format_1197"
    """
    Chemical structure specified in IUPAC International Chemical Identifier (InChI) line notation.
    """
    mf = "edam:format_1198"
    """
    Chemical structure specified by Molecular Formula (MF), including a count of each element in a compound.
    """
    InChIKey = "edam:format_1199"
    """
    The InChIKey (hashed InChI) is a fixed length (25 character) condensed digital representation of an InChI chemical structure specification. It uniquely identifies a chemical compound.
    """
    smarts = "edam:format_1200"
    """
    SMILES ARbitrary Target Specification (SMARTS) format for chemical structure specification, which is a subset of the SMILES line notation.
    """
    unambiguous_pure = "edam:format_1206"
    """
    Alphabet for a molecular sequence with possible unknown positions but without ambiguity or non-sequence characters.
    """
    nucleotide = "edam:format_1207"
    """
    Alphabet for a nucleotide sequence with possible ambiguity, unknown positions and non-sequence characters.
    """
    protein = "edam:format_1208"
    """
    Alphabet for a protein sequence with possible ambiguity, unknown positions and non-sequence characters.
    """
    consensus = "edam:format_1209"
    """
    Alphabet for the consensus of two or more molecular sequences.
    """
    pure_nucleotide = "edam:format_1210"
    """
    Alphabet for a nucleotide sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    unambiguous_pure_nucleotide = "edam:format_1211"
    """
    Alphabet for a nucleotide sequence (characters ACGTU only) with possible unknown positions but without ambiguity or non-sequence characters .
    """
    dna = "edam:format_1212"
    """
    Alphabet for a DNA sequence with possible ambiguity, unknown positions and non-sequence characters.
    """
    rna = "edam:format_1213"
    """
    Alphabet for an RNA sequence with possible ambiguity, unknown positions and non-sequence characters.
    """
    unambiguous_pure_dna = "edam:format_1214"
    """
    Alphabet for a DNA sequence (characters ACGT only) with possible unknown positions but without ambiguity or non-sequence characters.
    """
    pure_dna = "edam:format_1215"
    """
    Alphabet for a DNA sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    unambiguous_pure_rna_sequence = "edam:format_1216"
    """
    Alphabet for an RNA sequence (characters ACGU only) with possible unknown positions but without ambiguity or non-sequence characters.
    """
    pure_rna = "edam:format_1217"
    """
    Alphabet for an RNA sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    unambiguous_pure_protein = "edam:format_1218"
    """
    Alphabet for any protein sequence with possible unknown positions but without ambiguity or non-sequence characters.
    """
    pure_protein = "edam:format_1219"
    """
    Alphabet for any protein sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    EMBL_feature_location = "edam:format_1248"
    """
    Format for sequence positions (feature location) as used in DDBJ/EMBL/GenBank database.
    """
    quicktandem = "edam:format_1295"
    """
    Report format for tandem repeats in a nucleotide sequence (format generated by the Sanger Centre quicktandem program).
    """
    Sanger_inverted_repeats = "edam:format_1296"
    """
    Report format for inverted repeats in a nucleotide sequence (format generated by the Sanger Centre inverted program).
    """
    EMBOSS_repeat = "edam:format_1297"
    """
    Report format for tandem repeats in a sequence (an EMBOSS report format).
    """
    est2genome_format = "edam:format_1316"
    """
    Format of a report on exon-intron structure generated by EMBOSS est2genome.
    """
    restrict_format = "edam:format_1318"
    """
    Report format for restriction enzyme recognition sites used by EMBOSS restrict program.
    """
    restover_format = "edam:format_1319"
    """
    Report format for restriction enzyme recognition sites used by EMBOSS restover program.
    """
    REBASE_restriction_sites = "edam:format_1320"
    """
    Report format for restriction enzyme recognition sites used by REBASE database.
    """
    FASTA_search_results_format = "edam:format_1332"
    """
    Format of results of a sequence database search using FASTA.
    """
    BLAST_results = "edam:format_1333"
    """
    Format of results of a sequence database search using some variant of BLAST.
    """
    mspcrunch = "edam:format_1334"
    """
    Format of results of a sequence database search using some variant of MSPCrunch.
    """
    Smith_Waterman_format = "edam:format_1335"
    """
    Format of results of a sequence database search using some variant of Smith Waterman.
    """
    dhf = "edam:format_1336"
    """
    Format of EMBASSY domain hits file (DHF) of hits (sequences) with domain classification information.
    """
    lhf = "edam:format_1337"
    """
    Format of EMBASSY ligand hits file (LHF) of database hits (sequences) with ligand classification information.
    """
    InterPro_hits_format = "edam:format_1341"
    """
    Results format for searches of the InterPro database.
    """
    InterPro_protein_view_report_format = "edam:format_1342"
    """
    Format of results of a search of the InterPro database showing matches of query protein sequence(s) to InterPro entries.
    """
    InterPro_match_table_format = "edam:format_1343"
    """
    Format of results of a search of the InterPro database showing matches between protein sequence(s) and signatures for an InterPro entry.
    """
    HMMER_Dirichlet_prior = "edam:format_1349"
    """
    Dirichlet distribution HMMER format.
    """
    MEME_Dirichlet_prior = "edam:format_1350"
    """
    Dirichlet distribution MEME format.
    """
    HMMER_emission_and_transition = "edam:format_1351"
    """
    Format of a report from the HMMER package on the emission and transition counts of a hidden Markov model.
    """
    prosite_pattern = "edam:format_1356"
    """
    Format of a regular expression pattern from the Prosite database.
    """
    EMBOSS_sequence_pattern = "edam:format_1357"
    """
    Format of an EMBOSS sequence pattern.
    """
    meme_motif = "edam:format_1360"
    """
    A motif in the format generated by the MEME program.
    """
    prosite_profile = "edam:format_1366"
    """
    Sequence profile (sequence classifier) format used in the PROSITE database.
    """
    JASPAR_format = "edam:format_1367"
    """
    A profile (sequence classifier) in the format used in the JASPAR database.
    """
    MEME_background_Markov_model = "edam:format_1369"
    """
    Format of the model of random sequences used by MEME.
    """
    HMMER_format = "edam:format_1370"
    """
    Format of a hidden Markov model representation used by the HMMER package.
    """
    HMMER_aln = "edam:format_1391"
    """
    FASTA-style format for multiple sequences aligned by HMMER package to an HMM.
    """
    DIALIGN_format = "edam:format_1392"
    """
    Format of multiple sequences aligned by DIALIGN package.
    """
    daf = "edam:format_1393"
    """
    EMBASSY 'domain alignment file' (DAF) format, containing a sequence alignment of protein domains belonging to the same SCOP or CATH family.
    """
    Sequence_MEME_profile_alignment = "edam:format_1419"
    """
    Format for alignment of molecular sequences to MEME profiles (position-dependent scoring matrices) as generated by the MAST tool from the MEME package.
    """
    HMMER_profile_alignment_LEFT_PARENTHESISsequences_versus_HMMsRIGHT_PARENTHESIS = "edam:format_1421"
    """
    Format used by the HMMER package for an alignment of a sequence against a hidden Markov model database.
    """
    HMMER_profile_alignment_LEFT_PARENTHESISHMM_versus_sequencesRIGHT_PARENTHESIS = "edam:format_1422"
    """
    Format used by the HMMER package for of an alignment of a hidden Markov model against a sequence database.
    """
    Phylip_distance_matrix = "edam:format_1423"
    """
    Format of PHYLIP phylogenetic distance matrix data.
    """
    ClustalW_dendrogram = "edam:format_1424"
    """
    Dendrogram (tree file) format generated by ClustalW.
    """
    Phylip_tree_raw = "edam:format_1425"
    """
    Raw data file format used by Phylip from which a phylogenetic tree is directly generated or plotted.
    """
    Phylip_continuous_quantitative_characters = "edam:format_1430"
    """
    PHYLIP file format for continuous quantitative character data.
    """
    Phylip_character_frequencies_format = "edam:format_1432"
    """
    PHYLIP file format for phylogenetics character frequency data.
    """
    Phylip_discrete_states_format = "edam:format_1433"
    """
    Format of PHYLIP discrete states data.
    """
    Phylip_cliques_format = "edam:format_1434"
    """
    Format of PHYLIP cliques data.
    """
    Phylip_tree_format = "edam:format_1435"
    """
    Phylogenetic tree data format used by the PHYLIP program.
    """
    TreeBASE_format = "edam:format_1436"
    """
    The format of an entry from the TreeBASE database of phylogenetic data.
    """
    TreeFam_format = "edam:format_1437"
    """
    The format of an entry from the TreeFam database of phylogenetic data.
    """
    Phylip_tree_distance_format = "edam:format_1445"
    """
    Format for distances, such as Branch Score distance, between two or more phylogenetic trees as used by the Phylip package.
    """
    dssp = "edam:format_1454"
    """
    Format of an entry from the DSSP database (Dictionary of Secondary Structure in Proteins).
    """
    hssp = "edam:format_1455"
    """
    Entry format of the HSSP database (Homology-derived Secondary Structure in Proteins).
    """
    Dot_bracket_format = "edam:format_1457"
    """
    Format of RNA secondary structure in dot-bracket notation, originally generated by the Vienna RNA package/server.
    """
    Vienna_local_RNA_secondary_structure_format = "edam:format_1458"
    """
    Format of local RNA secondary structure components with free energy values, generated by the Vienna RNA package/server.
    """
    PDB_database_entry_format = "edam:format_1475"
    """
    Format of an entry (or part of an entry) from the PDB database.
    """
    PDB = "edam:format_1476"
    """
    Entry format of PDB database in PDB format.
    """
    mmCIF = "edam:format_1477"
    """
    Entry format of PDB database in mmCIF format.
    """
    PDBML = "edam:format_1478"
    """
    Entry format of PDB database in PDBML (XML) format.
    """
    aaindex = "edam:format_1504"
    """
    Amino acid index format used by the AAindex database.
    """
    Pcons_report_format = "edam:format_1551"
    """
    Format of output of the Pcons Model Quality Assessment Program (MQAP).
    """
    ProQ_report_format = "edam:format_1552"
    """
    Format of output of the ProQ protein model quality predictor.
    """
    findkm = "edam:format_1582"
    """
    A report format for the kinetics of enzyme-catalysed reaction(s) in a format generated by EMBOSS findkm. This includes Michaelis Menten plot, Hanes Woolf plot, Michaelis Menten constant (Km) and maximum velocity (Vmax).
    """
    Primer3_primer = "edam:format_1627"
    """
    Report format on PCR primers and hybridisation oligos as generated by Whitehead primer3 program.
    """
    ABI = "edam:format_1628"
    """
    A format of raw sequence read data from an Applied Biosystems sequencing machine.
    """
    mira = "edam:format_1629"
    """
    Format of MIRA sequence trace information file.
    """
    CAF = "edam:format_1630"
    """
    Common Assembly Format (CAF). A sequence assembly format including contigs, base-call qualities, and other metadata.
    """
    EXP = "edam:format_1631"
    """
    Sequence assembly project file EXP format.
    """
    SCF = "edam:format_1632"
    """
    Staden Chromatogram Files format (SCF) of base-called sequence reads, qualities, and other metadata.
    """
    PHD = "edam:format_1633"
    """
    PHD sequence trace format to store serialised chromatogram data (reads).
    """
    dat = "edam:format_1637"
    """
    Format of Affymetrix data file of raw image data.
    """
    cel = "edam:format_1638"
    """
    Format of Affymetrix data file of information about (raw) expression levels of the individual probes.
    """
    affymetrix = "edam:format_1639"
    """
    Format of affymetrix gene cluster files (hc-genes.txt, hc-chips.txt) from hierarchical clustering.
    """
    affymetrix_exp = "edam:format_1641"
    """
    Affymetrix data file format for information about experimental conditions and protocols.
    """
    CHP = "edam:format_1644"
    """
    Format of Affymetrix data file of information about (normalised) expression levels of the individual probes.
    """
    Taverna_workflow_format = "edam:format_1665"
    """
    Format of Taverna workflows.
    """
    HET_group_dictionary_entry_format = "edam:format_1705"
    """
    The format of an entry from the HET group dictionary (HET groups from PDB files).
    """
    PubMed_citation = "edam:format_1734"
    """
    Format of bibliographic reference as used by the PubMed database.
    """
    Medline_Display_Format = "edam:format_1735"
    """
    Format for abstracts of scientific articles from the Medline database.
    """
    CiteXplore_core = "edam:format_1736"
    """
    CiteXplore 'core' citation format including title, journal, authors and abstract.
    """
    CiteXplore_all = "edam:format_1737"
    """
    CiteXplore 'all' citation format includes all known details such as Mesh terms and cross-references.
    """
    pmc = "edam:format_1739"
    """
    Article format of the PubMed Central database.
    """
    iHOP_format = "edam:format_1740"
    """
    The format of iHOP (Information Hyperlinked over Proteins) text-mining result.
    """
    OSCAR_format = "edam:format_1741"
    """
    OSCAR format of annotated chemical text.
    """
    PlasMapper_TextMap = "edam:format_1861"
    """
    Map of a plasmid (circular DNA) in PlasMapper TextMap format.
    """
    newick = "edam:format_1910"
    """
    Phylogenetic tree Newick (text) format.
    """
    TreeCon_format = "edam:format_1911"
    """
    Phylogenetic tree TreeCon (text) format.
    """
    Nexus_format = "edam:format_1912"
    """
    Phylogenetic tree Nexus (text) format.
    """
    Sequence_record_format = "edam:format_1919"
    """
    Data format for a molecular sequence record.
    """
    Sequence_feature_annotation_format = "edam:format_1920"
    """
    Data format for molecular sequence feature information.
    """
    Alignment_format = "edam:format_1921"
    """
    Data format for molecular sequence alignment information.
    """
    acedb = "edam:format_1923"
    """
    ACEDB sequence format.
    """
    codata = "edam:format_1925"
    """
    Codata entry format.
    """
    dbid = "edam:format_1926"
    """
    Fasta format variant with database name before ID.
    """
    EMBL_format = "edam:format_1927"
    """
    EMBL entry format.
    """
    Staden_experiment_format = "edam:format_1928"
    """
    Staden experiment file format.
    """
    FASTA = "edam:format_1929"
    """
    FASTA format including NCBI-style IDs.
    """
    FASTQ = "edam:format_1930"
    """
    FASTQ short read format ignoring quality scores.
    """
    FASTQ_illumina = "edam:format_1931"
    """
    FASTQ Illumina 1.3 short read format.
    """
    FASTQ_sanger = "edam:format_1932"
    """
    FASTQ short read format with phred quality.
    """
    FASTQ_solexa = "edam:format_1933"
    """
    FASTQ Solexa/Illumina 1.0 short read format.
    """
    fitch_program = "edam:format_1934"
    """
    Fitch program format.
    """
    GCG = "edam:format_1935"
    """
    GCG sequence file format.
    """
    GenBank_format = "edam:format_1936"
    """
    Genbank entry format.
    """
    genpept = "edam:format_1937"
    """
    Genpept protein entry format.
    """
    GFF2_seq = "edam:format_1938"
    """
    GFF feature file format with sequence in the header.
    """
    GFF3_seq = "edam:format_1939"
    """
    GFF3 feature file format with sequence.
    """
    giFASTA_format = "edam:format_1940"
    """
    FASTA sequence format including NCBI-style GIs.
    """
    hennig86 = "edam:format_1941"
    """
    Hennig86 output sequence format.
    """
    ig = "edam:format_1942"
    """
    Intelligenetics sequence format.
    """
    igstrict = "edam:format_1943"
    """
    Intelligenetics sequence format (strict version).
    """
    jackknifer = "edam:format_1944"
    """
    Jackknifer interleaved and non-interleaved sequence format.
    """
    mase_format = "edam:format_1945"
    """
    Mase program sequence format.
    """
    mega_seq = "edam:format_1946"
    """
    Mega interleaved and non-interleaved sequence format.
    """
    GCG_MSF = "edam:format_1947"
    """
    GCG MSF (multiple sequence file) file format.
    """
    nbrfSOLIDUSpir = "edam:format_1948"
    """
    NBRF/PIR entry sequence format.
    """
    nexus_seq = "edam:format_1949"
    """
    Nexus/paup interleaved sequence format.
    """
    pdbatom = "edam:format_1950"
    """
    PDB sequence format (ATOM lines).
    """
    pdbatomnuc = "edam:format_1951"
    """
    PDB nucleotide sequence format (ATOM lines).
    """
    pdbseqresnuc = "edam:format_1952"
    """
    PDB nucleotide sequence format (SEQRES lines).
    """
    pdbseqres = "edam:format_1953"
    """
    PDB sequence format (SEQRES lines).
    """
    Pearson_format = "edam:format_1954"
    """
    Plain old FASTA sequence format (unspecified format for IDs).
    """
    raw = "edam:format_1957"
    """
    Raw sequence format with no non-sequence characters.
    """
    refseqp = "edam:format_1958"
    """
    Refseq protein entry sequence format.
    """
    Staden_format = "edam:format_1960"
    """
    Staden suite sequence format.
    """
    Stockholm_format = "edam:format_1961"
    """
    Stockholm multiple sequence alignment format (used by Pfam and Rfam).
    """
    strider_format = "edam:format_1962"
    """
    DNA strider output sequence format.
    """
    UniProtKB_format = "edam:format_1963"
    """
    UniProtKB entry sequence format.
    """
    plain_text_format_LEFT_PARENTHESISunformattedRIGHT_PARENTHESIS = "edam:format_1964"
    """
    Plain text sequence format (essentially unformatted).
    """
    ASNFULL_STOP1_sequence_format = "edam:format_1966"
    """
    NCBI ASN.1-based sequence format.
    """
    DAS_format = "edam:format_1967"
    """
    DAS sequence (XML) format (any type).
    """
    dasdna = "edam:format_1968"
    """
    DAS sequence (XML) format (nucleotide-only).
    """
    debug_seq = "edam:format_1969"
    """
    EMBOSS debugging trace sequence format of full internal data content.
    """
    jackknifernon = "edam:format_1970"
    """
    Jackknifer output sequence non-interleaved format.
    """
    NCBI_format = "edam:format_1972"
    """
    NCBI FASTA sequence format with NCBI-style IDs.
    """
    nexusnon = "edam:format_1973"
    """
    Nexus/paup non-interleaved sequence format.
    """
    GFF2 = "edam:format_1974"
    """
    General Feature Format (GFF) of sequence features.
    """
    GFF3 = "edam:format_1975"
    """
    Generic Feature Format version 3 (GFF3) of sequence features.
    """
    DASGFF = "edam:format_1978"
    """
    DAS GFF (XML) feature format.
    """
    debug_feat = "edam:format_1979"
    """
    EMBOSS debugging trace feature format of full internal data content.
    """
    ClustalW_format = "edam:format_1982"
    """
    ClustalW format for (aligned) sequences.
    """
    debug = "edam:format_1983"
    """
    EMBOSS alignment format for debugging trace of full internal data content.
    """
    FASTA_aln = "edam:format_1984"
    """
    Fasta format for (aligned) sequences.
    """
    markx0 = "edam:format_1985"
    """
    Pearson MARKX0 alignment format.
    """
    markx1 = "edam:format_1986"
    """
    Pearson MARKX1 alignment format.
    """
    markx10 = "edam:format_1987"
    """
    Pearson MARKX10 alignment format.
    """
    markx2 = "edam:format_1988"
    """
    Pearson MARKX2 alignment format.
    """
    markx3 = "edam:format_1989"
    """
    Pearson MARKX3 alignment format.
    """
    match = "edam:format_1990"
    """
    Alignment format for start and end of matches between sequence pairs.
    """
    mega = "edam:format_1991"
    """
    Mega format for (typically aligned) sequences.
    """
    meganon = "edam:format_1992"
    """
    Mega non-interleaved format for (typically aligned) sequences.
    """
    pair = "edam:format_1996"
    """
    EMBOSS simple sequence pairwise alignment format.
    """
    PHYLIP_format = "edam:format_1997"
    """
    Phylip format for (aligned) sequences.
    """
    PHYLIP_sequential = "edam:format_1998"
    """
    Phylip non-interleaved format for (aligned) sequences.
    """
    scores_format = "edam:format_1999"
    """
    Alignment format for score values for pairs of sequences.
    """
    selex = "edam:format_2000"
    """
    SELEX format for (aligned) sequences.
    """
    EMBOSS_simple_format = "edam:format_2001"
    """
    EMBOSS simple multiple alignment format.
    """
    srs_format = "edam:format_2002"
    """
    Simple multiple sequence (alignment) format for SRS.
    """
    srspair = "edam:format_2003"
    """
    Simple sequence pair (alignment) format for SRS.
    """
    T_Coffee_format = "edam:format_2004"
    """
    T-Coffee program alignment format.
    """
    TreeCon_seq = "edam:format_2005"
    """
    Treecon format for (aligned) sequences.
    """
    Phylogenetic_tree_format = "edam:format_2006"
    """
    Data format for a phylogenetic tree.
    """
    Biological_pathway_or_network_format = "edam:format_2013"
    """
    Data format for a biological pathway or network.
    """
    Sequence_profile_alignment_format = "edam:format_2014"
    """
    Data format for a sequence-profile alignment.
    """
    Amino_acid_index_format = "edam:format_2017"
    """
    Data format for an amino acid index.
    """
    Article_format = "edam:format_2020"
    """
    Data format for a full-text scientific article.
    """
    Text_mining_report_format = "edam:format_2021"
    """
    Data format of a report from text mining.
    """
    Enzyme_kinetics_report_format = "edam:format_2027"
    """
    Data format for reports on enzyme kinetics.
    """
    Chemical_data_format = "edam:format_2030"
    """
    Format of a report on a chemical compound.
    """
    Gene_annotation_format = "edam:format_2031"
    """
    Format of a report on a particular locus, gene, gene system or groups of genes.
    """
    Workflow_format = "edam:format_2032"
    """
    Format of a workflow.
    """
    Tertiary_structure_format = "edam:format_2033"
    """
    Data format for a molecular tertiary structure.
    """
    Chemical_formula_format = "edam:format_2035"
    """
    Text format of a chemical formula.
    """
    Phylogenetic_character_data_format = "edam:format_2036"
    """
    Format of raw (unplotted) phylogenetic data.
    """
    Phylogenetic_continuous_quantitative_character_format = "edam:format_2037"
    """
    Format of phylogenetic continuous quantitative character data.
    """
    Phylogenetic_discrete_states_format = "edam:format_2038"
    """
    Format of phylogenetic discrete states data.
    """
    Phylogenetic_tree_report_LEFT_PARENTHESIScliquesRIGHT_PARENTHESIS_format = "edam:format_2039"
    """
    Format of phylogenetic cliques data.
    """
    Phylogenetic_tree_report_LEFT_PARENTHESISinvariantsRIGHT_PARENTHESIS_format = "edam:format_2040"
    """
    Format of phylogenetic invariants data.
    """
    Phylogenetic_tree_report_LEFT_PARENTHESIStree_distancesRIGHT_PARENTHESIS_format = "edam:format_2049"
    """
    Format for phylogenetic tree distance data.
    """
    Protein_family_report_format = "edam:format_2052"
    """
    Format for reports on a protein family.
    """
    Protein_interaction_format = "edam:format_2054"
    """
    Format for molecular interaction data.
    """
    Sequence_assembly_format = "edam:format_2055"
    """
    Format for sequence assembly data.
    """
    Microarray_experiment_data_format = "edam:format_2056"
    """
    Format for information about a microarray experimental per se (not the data generated from that experiment).
    """
    Sequence_trace_format = "edam:format_2057"
    """
    Format for sequence trace data (i.e. including base call information).
    """
    Gene_expression_report_format = "edam:format_2058"
    """
    Format of a file of gene expression data, e.g. a gene expression matrix or profile.
    """
    Map_format = "edam:format_2060"
    """
    Format of a map of (typically one) molecular sequence annotated with features.
    """
    Nucleic_acid_features_LEFT_PARENTHESISprimersRIGHT_PARENTHESIS_format = "edam:format_2061"
    """
    Format of a report on PCR primers or hybridisation oligos in a nucleic acid sequence.
    """
    Protein_report_format = "edam:format_2062"
    """
    Format of a report of general information about a specific protein.
    """
    number_3D_1D_scoring_matrix_format = "edam:format_2064"
    """
    Format of a matrix of 3D-1D scores (amino acid environment probabilities).
    """
    Protein_structure_report_LEFT_PARENTHESISquality_evaluationRIGHT_PARENTHESIS_format = "edam:format_2065"
    """
    Format of a report on the quality of a protein three-dimensional model.
    """
    Database_hits_LEFT_PARENTHESISsequenceRIGHT_PARENTHESIS_format = "edam:format_2066"
    """
    Format of a report on sequence hits and associated data from searching a sequence database.
    """
    Sequence_distance_matrix_format = "edam:format_2067"
    """
    Format of a matrix of genetic distances between molecular sequences.
    """
    Sequence_motif_format = "edam:format_2068"
    """
    Format of a sequence motif.
    """
    Sequence_profile_format = "edam:format_2069"
    """
    Format of a sequence profile.
    """
    Hidden_Markov_model_format = "edam:format_2072"
    """
    Format of a hidden Markov model.
    """
    Dirichlet_distribution_format = "edam:format_2074"
    """
    Data format of a dirichlet distribution.
    """
    HMM_emission_and_transition_counts_format = "edam:format_2075"
    """
    Data format for the emission and transition counts of a hidden Markov model.
    """
    RNA_secondary_structure_format = "edam:format_2076"
    """
    Format for secondary structure (predicted or real) of an RNA molecule.
    """
    Protein_secondary_structure_format = "edam:format_2077"
    """
    Format for secondary structure (predicted or real) of a protein molecule.
    """
    Sequence_range_format = "edam:format_2078"
    """
    Format used to specify range(s) of sequence positions.
    """
    pure = "edam:format_2094"
    """
    Alphabet for molecular sequence with possible unknown positions but without non-sequence characters.
    """
    unpure = "edam:format_2095"
    """
    Alphabet for a molecular sequence with possible unknown positions but possibly with non-sequence characters.
    """
    unambiguous_sequence = "edam:format_2096"
    """
    Alphabet for a molecular sequence with possible unknown positions but without ambiguity characters.
    """
    ambiguous = "edam:format_2097"
    """
    Alphabet for a molecular sequence with possible unknown positions and possible ambiguity characters.
    """
    Sequence_features_LEFT_PARENTHESISrepeatsRIGHT_PARENTHESIS_format = "edam:format_2155"
    """
    Format used for map of repeats in molecular (typically nucleotide) sequences.
    """
    Nucleic_acid_features_LEFT_PARENTHESISrestriction_sitesRIGHT_PARENTHESIS_format = "edam:format_2158"
    """
    Format used for report on restriction enzyme recognition sites in nucleotide sequences.
    """
    Sequence_cluster_format = "edam:format_2170"
    """
    Format used for clusters of molecular sequences.
    """
    Sequence_cluster_format_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "edam:format_2171"
    """
    Format used for clusters of protein sequences.
    """
    Sequence_cluster_format_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "edam:format_2172"
    """
    Format used for clusters of nucleotide sequences.
    """
    EMBL_like_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2181"
    """
    A text format resembling EMBL entry format.
    """
    FASTQ_like_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2182"
    """
    A text format resembling FASTQ short read format.
    """
    EMBLXML = "edam:format_2183"
    """
    XML format for EMBL entries.
    """
    cdsxml = "edam:format_2184"
    """
    Specific XML format for EMBL entries (only uses certain sections).
    """
    INSDSeq = "edam:format_2185"
    """
    INSDSeq provides the elements of a sequence as presented in the GenBank/EMBL/DDBJ-style flatfile formats, with a small amount of additional structure.
    """
    geneseq = "edam:format_2186"
    """
    Geneseq sequence format.
    """
    UniProt_like_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2187"
    """
    A text sequence format resembling uniprotkb entry format.
    """
    medline = "edam:format_2194"
    """
    Abstract format used by MedLine database.
    """
    Ontology_format = "edam:format_2195"
    """
    Format used for ontologies.
    """
    OBO_format = "edam:format_2196"
    """
    A serialisation format conforming to the Open Biomedical Ontologies (OBO) model.
    """
    OWL_format = "edam:format_2197"
    """
    A serialisation format conforming to the Web Ontology Language (OWL) model.
    """
    FASTA_like_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2200"
    """
    A text format resembling FASTA format.
    """
    EMBL_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2204"
    """
    An XML format for EMBL entries.
    """
    GenBank_like_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2205"
    """
    A text format resembling GenBank entry (plain text) format.
    """
    Sequence_feature_table_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2206"
    """
    Text format for a sequence feature table.
    """
    STRING_entry_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2304"
    """
    Entry format (XML) for the STRING database of protein interaction.
    """
    GFF = "edam:format_2305"
    """
    GFF feature format (of indeterminate version).
    """
    GTF = "edam:format_2306"
    """
    Gene Transfer Format (GTF), a restricted version of GFF.
    """
    FASTA_HTML = "edam:format_2310"
    """
    FASTA format wrapped in HTML elements.
    """
    EMBL_HTML = "edam:format_2311"
    """
    EMBL entry format wrapped in HTML elements.
    """
    Textual_format = "edam:format_2330"
    """
    Textual format.
    """
    HTML = "edam:format_2331"
    """
    HTML format.
    """
    XML = "edam:format_2332"
    """
    eXtensible Markup Language (XML) format.
    """
    Binary_format = "edam:format_2333"
    """
    Binary format.
    """
    Format_LEFT_PARENTHESISby_type_of_dataRIGHT_PARENTHESIS = "edam:format_2350"
    """
    A placeholder concept for visual navigation by dividing data formats by the content of the data that is represented.
    """
    BioXSD_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2352"
    """
    BioXSD-schema-based XML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, Web services, and object-oriented programming.
    """
    RDF_format = "edam:format_2376"
    """
    A serialisation format conforming to the Resource Description Framework (RDF) model.
    """
    GenBank_HTML = "edam:format_2532"
    """
    Genbank entry format wrapped in HTML elements.
    """
    EMBL_like_format = "edam:format_2543"
    """
    A format resembling EMBL entry (plain text) format.
    """
    FASTQ_like_format = "edam:format_2545"
    """
    A format resembling FASTQ short read format.
    """
    FASTA_like = "edam:format_2546"
    """
    A format resembling FASTA format.
    """
    uniprotkb_like_format = "edam:format_2547"
    """
    A sequence format resembling uniprotkb entry format.
    """
    Sequence_feature_table_format = "edam:format_2548"
    """
    Format for a sequence feature table.
    """
    OBO = "edam:format_2549"
    """
    OBO ontology text format.
    """
    OBO_XML = "edam:format_2550"
    """
    OBO ontology XML format.
    """
    Sequence_record_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2551"
    """
    Data format for a molecular sequence record (text).
    """
    Sequence_record_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2552"
    """
    Data format for a molecular sequence record (XML).
    """
    Sequence_feature_table_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2553"
    """
    XML format for a sequence feature table.
    """
    Alignment_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2554"
    """
    Text format for molecular sequence alignment information.
    """
    Alignment_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2555"
    """
    XML format for molecular sequence alignment information.
    """
    Phylogenetic_tree_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2556"
    """
    Text format for a phylogenetic tree.
    """
    Phylogenetic_tree_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2557"
    """
    XML format for a phylogenetic tree.
    """
    EMBL_like_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "edam:format_2558"
    """
    An XML format resembling EMBL entry format.
    """
    GenBank_like_format = "edam:format_2559"
    """
    A format resembling GenBank entry (plain text) format.
    """
    Sequence_assembly_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_2561"
    """
    Text format for sequence assembly data.
    """
    completely_unambiguous = "edam:format_2566"
    """
    Alphabet for a molecular sequence without any unknown positions or ambiguity characters.
    """
    completely_unambiguous_pure = "edam:format_2567"
    """
    Alphabet for a molecular sequence without unknown positions, ambiguity or non-sequence characters.
    """
    completely_unambiguous_pure_nucleotide = "edam:format_2568"
    """
    Alphabet for a nucleotide sequence (characters ACGTU only) without unknown positions, ambiguity or non-sequence characters .
    """
    completely_unambiguous_pure_dna = "edam:format_2569"
    """
    Alphabet for a DNA sequence (characters ACGT only) without unknown positions, ambiguity or non-sequence characters.
    """
    completely_unambiguous_pure_rna_sequence = "edam:format_2570"
    """
    Alphabet for an RNA sequence (characters ACGU only) without unknown positions, ambiguity or non-sequence characters.
    """
    Raw_sequence_format = "edam:format_2571"
    """
    Format of a raw molecular sequence (i.e. the alphabet used).
    """
    BAM = "edam:format_2572"
    """
    BAM format, the binary, BGZF-formatted compressed version of SAM format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.
    """
    SAM = "edam:format_2573"
    """
    Sequence Alignment/Map (SAM) format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.
    """
    SBML = "edam:format_2585"
    """
    Systems Biology Markup Language (SBML), the standard XML format for models of biological processes such as for example metabolism, cell signaling, and gene regulation.
    """
    completely_unambiguous_pure_protein = "edam:format_2607"
    """
    Alphabet for any protein sequence without unknown positions, ambiguity or non-sequence characters.
    """
    Bibliographic_reference_format = "edam:format_2848"
    """
    Format of a bibliographic reference.
    """
    Sequence_annotation_track_format = "edam:format_2919"
    """
    Format of a sequence annotation track.
    """
    Alignment_format_LEFT_PARENTHESISpair_onlyRIGHT_PARENTHESIS = "edam:format_2920"
    """
    Data format for molecular sequence alignment information that can hold sequence alignment(s) of only 2 sequences.
    """
    Sequence_variation_annotation_format = "edam:format_2921"
    """
    Format of sequence variation annotation.
    """
    markx0_variant = "edam:format_2922"
    """
    Some variant of Pearson MARKX alignment format.
    """
    mega_variant = "edam:format_2923"
    """
    Some variant of Mega format for (typically aligned) sequences.
    """
    Phylip_format_variant = "edam:format_2924"
    """
    Some variant of Phylip format for (aligned) sequences.
    """
    AB1 = "edam:format_3000"
    """
    AB1 binary format of raw DNA sequence reads (output of Applied Biosystems' sequencing analysis software). Contains an electropherogram and the DNA base sequence.
    """
    ACE = "edam:format_3001"
    """
    ACE sequence assembly format including contigs, base-call qualities, and other metadata (version Aug 1998 and onwards).
    """
    BED = "edam:format_3003"
    """
    Browser Extensible Data (BED) format of sequence annotation track, typically to be displayed in a genome browser.
    """
    bigBed = "edam:format_3004"
    """
    bigBed format for large sequence annotation tracks, similar to textual BED format.
    """
    WIG = "edam:format_3005"
    """
    Wiggle format (WIG) of a sequence annotation track that consists of a value for each sequence position. Typically to be displayed in a genome browser.
    """
    bigWig = "edam:format_3006"
    """
    bigWig format for large sequence annotation tracks that consist of a value for each sequence position. Similar to textual WIG format.
    """
    PSL = "edam:format_3007"
    """
    PSL format of alignments, typically generated by BLAT or psLayout. Can be displayed in a genome browser like a sequence annotation track.
    """
    MAF = "edam:format_3008"
    """
    Multiple Alignment Format (MAF) supporting alignments of whole genomes with rearrangements, directions, multiple pieces to the alignment, and so forth.
    """
    number_2bit = "edam:format_3009"
    """
    2bit binary format of nucleotide sequences using 2 bits per nucleotide. In addition encodes unknown nucleotides and lower-case 'masking'.
    """
    FULL_STOPnib = "edam:format_3010"
    """
    .nib (nibble) binary format of a nucleotide sequence using 4 bits per nucleotide (including unknown) and its lower-case 'masking'.
    """
    genePred = "edam:format_3011"
    """
    genePred table format for gene prediction tracks.
    """
    pgSnp = "edam:format_3012"
    """
    Personal Genome SNP (pgSnp) format for sequence variation tracks (indels and polymorphisms), supported by the UCSC Genome Browser.
    """
    axt = "edam:format_3013"
    """
    axt format of alignments, typically produced from BLASTZ.
    """
    LAV = "edam:format_3014"
    """
    LAV format of alignments generated by BLASTZ and LASTZ.
    """
    Pileup = "edam:format_3015"
    """
    Pileup format of alignment of sequences (e.g. sequencing reads) to (a) reference sequence(s). Contains aligned bases per base of the reference sequence(s).
    """
    VCF = "edam:format_3016"
    """
    Variant Call Format (VCF) is tabular format for storing genomic sequence variations.
    """
    SRF = "edam:format_3017"
    """
    Sequence Read Format (SRF) of sequence trace data. Supports submission to the NCBI Short Read Archive.
    """
    ZTR = "edam:format_3018"
    """
    ZTR format for storing chromatogram data from DNA sequencing instruments.
    """
    GVF = "edam:format_3019"
    """
    Genome Variation Format (GVF). A GFF3-compatible format with defined header and attribute tags for sequence variation.
    """
    BCF = "edam:format_3020"
    """
    BCF is the binary version of Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation).
    """
    Matrix_format = "edam:format_3033"
    """
    Format of a matrix (array) of numerical values.
    """
    Protein_domain_classification_format = "edam:format_3097"
    """
    Format of data concerning the classification of the sequences and/or structures of protein structural domain(s).
    """
    Raw_SCOP_domain_classification_format = "edam:format_3098"
    """
    Format of raw SCOP domain classification data files.
    """
    Raw_CATH_domain_classification_format = "edam:format_3099"
    """
    Format of raw CATH domain classification data files.
    """
    CATH_domain_report_format = "edam:format_3100"
    """
    Format of summary of domain classification information for a CATH domain.
    """
    SBRML = "edam:format_3155"
    """
    Systems Biology Result Markup Language (SBRML), the standard XML format for simulated or calculated results (e.g. trajectories) of systems biology models.
    """
    BioPAX = "edam:format_3156"
    """
    BioPAX is an exchange format for pathway data, with its data model defined in OWL.
    """
    EBI_Application_Result_XML = "edam:format_3157"
    """
    EBI Application Result XML is a format returned by sequence similarity search Web services at EBI.
    """
    PSI_MI_XML_LEFT_PARENTHESISMIFRIGHT_PARENTHESIS = "edam:format_3158"
    """
    XML Molecular Interaction Format (MIF), standardised by HUPO PSI MI.
    """
    phyloXML = "edam:format_3159"
    """
    phyloXML is a standardised XML format for phylogenetic trees, networks, and associated data.
    """
    NeXML = "edam:format_3160"
    """
    NeXML is a standardised XML format for rich phyloinformatic data.
    """
    MAGE_ML = "edam:format_3161"
    """
    MAGE-ML XML format for microarray expression data, standardised by MGED (now FGED).
    """
    MAGE_TAB = "edam:format_3162"
    """
    MAGE-TAB textual format for microarray expression data, standardised by MGED (now FGED).
    """
    GCDML = "edam:format_3163"
    """
    GCDML XML format for genome and metagenome metadata according to MIGS/MIMS/MIMARKS information standards, standardised by the Genomic Standards Consortium (GSC).
    """
    GTrack = "edam:format_3164"
    """
    GTrack is a generic and optimised tabular format for genome or sequence feature tracks. GTrack unifies the power of other track formats (e.g. GFF3, BED, WIG), and while optimised in size, adds more flexibility, customisation, and automation ("machine understandability").
    """
    Biological_pathway_or_network_report_format = "edam:format_3166"
    """
    Data format for a report of information derived from a biological pathway or network.
    """
    Experiment_annotation_format = "edam:format_3167"
    """
    Data format for annotation on a laboratory experiment.
    """
    Cytoband_format = "edam:format_3235"
    """
    Cytoband format for chromosome cytobands.
    """
    CopasiML = "edam:format_3239"
    """
    CopasiML, the native format of COPASI.
    """
    CellML = "edam:format_3240"
    """
    CellML, the format for mathematical models of biological and other networks.
    """
    PSI_MI_TAB_LEFT_PARENTHESISMITABRIGHT_PARENTHESIS = "edam:format_3242"
    """
    Tabular Molecular Interaction format (MITAB), standardised by HUPO PSI MI.
    """
    PSI_PAR = "edam:format_3243"
    """
    Protein affinity format (PSI-PAR), standardised by HUPO PSI MI. It is compatible with PSI MI XML (MIF) and uses the same XML Schema.
    """
    mzML = "edam:format_3244"
    """
    mzML format for raw spectrometer output data, standardised by HUPO PSI MSS.
    """
    Mass_spectrometry_data_format = "edam:format_3245"
    """
    Format for mass pectra and derived data, include peptide sequences etc.
    """
    TraML = "edam:format_3246"
    """
    TraML (Transition Markup Language) is the format for mass spectrometry transitions, standardised by HUPO PSI MSS.
    """
    mzIdentML = "edam:format_3247"
    """
    mzIdentML is the exchange format for peptides and proteins identified from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of proteomics search engines.
    """
    mzQuantML = "edam:format_3248"
    """
    mzQuantML is the format for quantitation values associated with peptides, proteins and small molecules from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of quantitation software for proteomics.
    """
    GelML = "edam:format_3249"
    """
    GelML is the format for describing the process of gel electrophoresis, standardised by HUPO PSI PS.
    """
    spML = "edam:format_3250"
    """
    spML is the format for describing proteomics sample processing, other than using gels, prior to mass spectrometric protein identification, standardised by HUPO PSI PS. It may also be applicable for metabolomics.
    """
    OWL_Functional_Syntax = "edam:format_3252"
    """
    A human-readable encoding for the Web Ontology Language (OWL).
    """
    Manchester_OWL_Syntax = "edam:format_3253"
    """
    A syntax for writing OWL class expressions.
    """
    KRSS2_Syntax = "edam:format_3254"
    """
    A superset of the "Description-Logic Knowledge Representation System Specification from the KRSS Group of the ARPA Knowledge Sharing Effort".
    """
    Turtle = "edam:format_3255"
    """
    The Terse RDF Triple Language (Turtle) is a human-friendly serialisation format for RDF (Resource Description Framework) graphs.
    """
    N_Triples = "edam:format_3256"
    """
    A plain text serialisation format for RDF (Resource Description Framework) graphs, and a subset of the Turtle (Terse RDF Triple Language) format.
    """
    Notation3 = "edam:format_3257"
    """
    A shorthand non-XML serialisation of Resource Description Framework model, designed with human-readability in mind.
    """
    RDFSOLIDUSXML = "edam:format_3261"
    """
    Resource Description Framework (RDF) XML format.
    """
    OWLSOLIDUSXML = "edam:format_3262"
    """
    OWL ontology XML serialisation format.
    """
    A2M = "edam:format_3281"
    """
    The A2M format is used as the primary format for multiple alignments of protein or nucleic-acid sequences in the SAM suite of tools. It is a small modification of FASTA format for sequences and is compatible with most tools that read FASTA.
    """
    SFF = "edam:format_3284"
    """
    Standard flowgram format (SFF) is a binary file format used to encode results of pyrosequencing from the 454 Life Sciences platform for high-throughput sequencing.
    """
    MAP = "edam:format_3285"
    """
    The MAP file describes SNPs and is used by the Plink package.
    """
    PED = "edam:format_3286"
    """
    The PED file describes individuals and genetic data and is used by the Plink package.
    """
    Individual_genetic_data_format = "edam:format_3287"
    """
    Data format for a metadata on an individual and their genetic data.
    """
    PEDSOLIDUSMAP = "edam:format_3288"
    """
    The PED/MAP file describes data used by the Plink package.
    """
    CT = "edam:format_3309"
    """
    File format of a CT (Connectivity Table) file from the RNAstructure package.
    """
    SS = "edam:format_3310"
    """
    XRNA old input style format.
    """
    RNAML = "edam:format_3311"
    """
    RNA Markup Language.
    """
    GDE = "edam:format_3312"
    """
    Format for the Genetic Data Environment (GDE).
    """
    BLC = "edam:format_3313"
    """
    A multiple alignment in vertical format, as used in the AMPS (Alignment of Multiple Protein Sequences) package.
    """
    Data_index_format = "edam:format_3326"
    """
    Format of a data index of some type.
    """
    BAI = "edam:format_3327"
    """
    BAM indexing format.
    """
    HMMER2 = "edam:format_3328"
    """
    HMMER profile HMM file for HMMER versions 2.x.
    """
    HMMER3 = "edam:format_3329"
    """
    HMMER profile HMM file for HMMER versions 3.x.
    """
    PO = "edam:format_3330"
    """
    PO is the output format of Partial Order Alignment program (POA) performing Multiple Sequence Alignment (MSA).
    """
    BLAST_XML_results_format = "edam:format_3331"
    """
    XML format as produced by the NCBI Blast package.
    """
    CRAM = "edam:format_3462"
    """
    Reference-based compression of alignment format.
    """
    JSON = "edam:format_3464"
    """
    JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs.
    """
    EPS = "edam:format_3466"
    """
    Encapsulated PostScript format.
    """
    GIF = "edam:format_3467"
    """
    Graphics Interchange Format.
    """
    xls = "edam:format_3468"
    """
    Microsoft Excel spreadsheet format.
    """
    TSV = "edam:format_3475"
    """
    Tabular data represented as tab-separated values in a text file.
    """
    Cytoscape_input_file_format = "edam:format_3477"
    """
    Format of the cytoscape input file of gene expression ratios or values are specified over one or more experiments.
    """
    ebwt = "edam:format_3484"
    """
    Bowtie format for indexed reference genome for "small" genomes.
    """
    RSF = "edam:format_3485"
    """
    Rich sequence format.
    """
    GCG_format_variant = "edam:format_3486"
    """
    Some format based on the GCG format.
    """
    BSML = "edam:format_3487"
    """
    Bioinformatics Sequence Markup Language format.
    """
    ebwtl = "edam:format_3491"
    """
    Bowtie format for indexed reference genome for "large" genomes.
    """
    Ensembl_variation_file_format = "edam:format_3499"
    """
    Ensembl standard format for variation data.
    """
    docx = "edam:format_3506"
    """
    Microsoft Word format.
    """
    Document_format = "edam:format_3507"
    """
    Format of documents including word processor, spreadsheet and presentation.
    """
    PDF = "edam:format_3508"
    """
    Portable Document Format.
    """
    Image_format = "edam:format_3547"
    """
    Format used for images and image metadata.
    """
    DICOM_format = "edam:format_3548"
    """
    Medical image format corresponding to the Digital Imaging and Communications in Medicine (DICOM) standard.
    """
    nii = "edam:format_3549"
    """
    An open file format from the Neuroimaging Informatics Technology Initiative (NIfTI) commonly used to store brain imaging data obtained using Magnetic Resonance Imaging (MRI) methods.
    """
    mhd = "edam:format_3550"
    """
    Text-based tagged file format for medical images generated using the MetaImage software package.
    """
    nrrd = "edam:format_3551"
    """
    Nearly Raw Rasta Data format designed to support scientific visualisation and image processing involving N-dimensional raster data.
    """
    R_file_format = "edam:format_3554"
    """
    File format used for scripts written in the R programming language for execution within the R software environment, typically for statistical computation and graphics.
    """
    SPSS = "edam:format_3555"
    """
    File format used for scripts for the Statistical Package for the Social Sciences.
    """
    MHTML = "edam:format_3556"
    """
    MIME HTML format for Web pages, which can include external resources, including images, Flash animations and so on.
    """
    IDAT = "edam:format_3578"
    """
    Proprietary file format for (raw) BeadArray data used by genomewide profiling platforms from Illumina Inc. This format is output directly from the scanner and stores summary intensities for each probe-type on an array.
    """
    JPG = "edam:format_3579"
    """
    Joint Picture Group file format for lossy graphics file.
    """
    rcc = "edam:format_3580"
    """
    Reporter Code Count-A data file (.csv) output by the Nanostring nCounter Digital Analyzer, which contains gene sample information, probe information and probe counts.
    """
    arff = "edam:format_3581"
    """
    ARFF (Attribute-Relation File Format) is an ASCII text file format that describes a list of instances sharing a set of attributes.
    """
    afg = "edam:format_3582"
    """
    AFG is a single text-based file assembly format that holds read and consensus information together.
    """
    bedgraph = "edam:format_3583"
    """
    The bedGraph format allows display of continuous-valued data in track format. This display type is useful for probability scores and transcriptome data.
    """
    bedstrict = "edam:format_3584"
    """
    Browser Extensible Data (BED) format of sequence annotation track that strictly does not contain non-standard fields beyond the first 3 columns.
    """
    bed6 = "edam:format_3585"
    """
    BED file format where each feature is described by chromosome, start, end, name, score, and strand.
    """
    bed12 = "edam:format_3586"
    """
    A BED file where each feature is described by all twelve columns.
    """
    chrominfo = "edam:format_3587"
    """
    Tabular format of chromosome names and sizes used by Galaxy.
    """
    customtrack = "edam:format_3588"
    """
    Custom Sequence annotation track format used by Galaxy.
    """
    csfasta = "edam:format_3589"
    """
    Color space FASTA format sequence variant.
    """
    HDF5 = "edam:format_3590"
    """
    HDF5 is a data model, library, and file format for storing and managing data, based on Hierarchical Data Format (HDF).
    """
    TIFF = "edam:format_3591"
    """
    A versatile bitmap format.
    """
    BMP = "edam:format_3592"
    """
    Standard bitmap storage format in the Microsoft Windows environment.
    """
    im = "edam:format_3593"
    """
    IM is a format used by LabEye and other applications based on the IFUNC image processing library.
    """
    pcd = "edam:format_3594"
    """
    Photo CD format, which is the highest resolution format for images on a CD.
    """
    pcx = "edam:format_3595"
    """
    PCX is an image file format that uses a simple form of run-length encoding. It is lossless.
    """
    ppm = "edam:format_3596"
    """
    The PPM format is a lowest common denominator color image file format.
    """
    psd = "edam:format_3597"
    """
    PSD (Photoshop Document) is a proprietary file that allows the user to work with the images' individual layers even after the file has been saved.
    """
    xbm = "edam:format_3598"
    """
    X BitMap is a plain text binary image format used by the X Window System used for storing cursor and icon bitmaps used in the X GUI.
    """
    xpm = "edam:format_3599"
    """
    X PixMap (XPM) is an image file format used by the X Window System, it is intended primarily for creating icon pixmaps, and supports transparent pixels.
    """
    rgb = "edam:format_3600"
    """
    RGB file format is the native raster graphics file format for Silicon Graphics workstations.
    """
    pbm = "edam:format_3601"
    """
    The PBM format is a lowest common denominator monochrome file format. It serves as the common language of a large family of bitmap image conversion filters.
    """
    pgm = "edam:format_3602"
    """
    The PGM format is a lowest common denominator grayscale file format.
    """
    PNG = "edam:format_3603"
    """
    PNG is a file format for image compression.
    """
    SVG = "edam:format_3604"
    """
    Scalable Vector Graphics (SVG) is an XML-based vector image format for two-dimensional graphics with support for interactivity and animation.
    """
    rast = "edam:format_3605"
    """
    Sun Raster is a raster graphics file format used on SunOS by Sun Microsystems.
    """
    Sequence_quality_report_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_3606"
    """
    Textual report format for sequence quality for reports from sequencing machines.
    """
    qual = "edam:format_3607"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences).
    """
    qualsolexa = "edam:format_3608"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) for Solexa/Illumina 1.0 format.
    """
    qualillumina = "edam:format_3609"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) from Illumina 1.5 and before Illumina 1.8.
    """
    qualsolid = "edam:format_3610"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) for SOLiD data.
    """
    qual454 = "edam:format_3611"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) from 454 sequencers.
    """
    ENCODE_peak_format = "edam:format_3612"
    """
    Human ENCODE peak format.
    """
    ENCODE_narrow_peak_format = "edam:format_3613"
    """
    Human ENCODE narrow peak format.
    """
    ENCODE_broad_peak_format = "edam:format_3614"
    """
    Human ENCODE broad peak format.
    """
    bgzip = "edam:format_3615"
    """
    Blocked GNU Zip format.
    """
    tabix = "edam:format_3616"
    """
    TAB-delimited genome position file index format.
    """
    Graph_format = "edam:format_3617"
    """
    Data format for graph data.
    """
    xgmml = "edam:format_3618"
    """
    XML-based format used to store graph descriptions within Galaxy.
    """
    sif = "edam:format_3619"
    """
    SIF (simple interaction file) Format - a network/pathway format used for instance in cytoscape.
    """
    xlsx = "edam:format_3620"
    """
    MS Excel spreadsheet format consisting of a set of XML documents stored in a ZIP-compressed file.
    """
    SQLite_format = "edam:format_3621"
    """
    Data format used by the SQLite database.
    """
    Gemini_SQLite_format = "edam:format_3622"
    """
    Data format used by the SQLite database conformant to the Gemini schema.
    """
    snpeffdb = "edam:format_3624"
    """
    An index of a genome database, indexed for use by the snpeff tool.
    """
    MAT = "edam:format_3626"
    """
    Binary format used by MATLAB files to store workspace variables.
    """
    NetCDF = "edam:format_3650"
    """
    Format used by netCDF software library for writing and reading chromatography-MS data files. Also used to store trajectory atom coordinates information, such as the ones obtained by Molecular Dynamics simulations.
    """
    MGF = "edam:format_3651"
    """
    Mascot Generic Format. Encodes multiple MS/MS spectra in a single file.
    """
    dta = "edam:format_3652"
    """
    Spectral data format file where each spectrum is written to a separate file.
    """
    pkl = "edam:format_3653"
    """
    Spectral data file similar to dta.
    """
    mzXML = "edam:format_3654"
    """
    Common file format for proteomics mass spectrometric data developed at the Seattle Proteome Center/Institute for Systems Biology.
    """
    pepXML = "edam:format_3655"
    """
    Open data format for the storage, exchange, and processing of peptide sequence assignments of MS/MS scans, intended to provide a common data output format for many different MS/MS search engines and subsequent peptide-level analyses.
    """
    GPML = "edam:format_3657"
    """
    Graphical Pathway Markup Language (GPML) is an XML format used for exchanging biological pathways.
    """
    K_mer_countgraph = "edam:format_3665"
    """
    A list of k-mers and their occurrences in a dataset. Can also be used as an implicit De Bruijn graph.
    """
    mzTab = "edam:format_3681"
    """
    mzTab is a light-weight, tab-delimited format for mass spectrometry-based proteomics data.
    """
    imzML_metadata_file = "edam:format_3682"
    """
    imzML metadata is a data format for mass spectrometry imaging metadata.
    """
    qcML = "edam:format_3683"
    """
    qcML is an XML format for quality-related data of mass spectrometry and other high-throughput measurements.
    """
    PRIDE_XML = "edam:format_3684"
    """
    PRIDE XML is an XML format for mass spectra, peptide and protein identifications, and metadata about a corresponding measurement, sample, experiment.
    """
    SED_ML = "edam:format_3685"
    """
    Simulation Experiment Description Markup Language (SED-ML) is an XML format for encoding simulation setups, according to the MIASE (Minimum Information About a Simulation Experiment) requirements.
    """
    COMBINE_OMEX = "edam:format_3686"
    """
    Open Modeling EXchange format (OMEX) is a ZIPped format for encapsulating all information necessary for a modeling and simulation project in systems biology.
    """
    ISA_Tab = "edam:format_3687"
    """
    ISA-Tab stands for Investigation / Study / Assay (ISA) tab-delimited (Tab) format, and it is comprised of metadata describing observational or experimental scientific studies.
    """
    SBtab = "edam:format_3688"
    """
    SBtab is a tabular format for biochemical network models.
    """
    BCML = "edam:format_3689"
    """
    Biological Connection Markup Language (BCML) is an XML format for biological pathways.
    """
    BDML = "edam:format_3690"
    """
    Biological Dynamics Markup Language (BDML) is an XML format for quantitative data describing biological dynamics.
    """
    BEL = "edam:format_3691"
    """
    Biological Expression Language (BEL) is a textual format for representing scientific findings in life sciences in a computable form.
    """
    SBGN_ML = "edam:format_3692"
    """
    SBGN-ML is an XML format for Systems Biology Graphical Notation (SBGN) diagrams of biological pathways or networks.
    """
    AGP = "edam:format_3693"
    """
    AGP is a tabular format for a sequence assembly (a contig, a scaffold/supercontig, or a chromosome).
    """
    PS = "edam:format_3696"
    """
    PostScript format.
    """
    SRA_format = "edam:format_3698"
    """
    SRA archive format (SRA) is the archive format used for input to the NCBI Sequence Read Archive.
    """
    VDB = "edam:format_3699"
    """
    VDB ('vertical database') is the native format used for export from the NCBI Sequence Read Archive.
    """
    Sequin_format = "edam:format_3701"
    """
    A five-column, tab-delimited table of feature locations and qualifiers for importing annotation into an existing Sequin submission (an NCBI tool for submitting and updating GenBank entries).
    """
    MSF = "edam:format_3702"
    """
    Proprietary mass-spectrometry format of Thermo Scientific's ProteomeDiscoverer software.
    """
    Biodiversity_data_format = "edam:format_3706"
    """
    Data format for biodiversity data.
    """
    ABCD_format = "edam:format_3708"
    """
    Exchange format of the Access to Biological Collections Data (ABCD) Schema; a standard for the access to and exchange of data about specimens and observations (primary biodiversity data).
    """
    GCTSOLIDUSRes_format = "edam:format_3709"
    """
    Tab-delimited text files of GenePattern that contain a column for each sample, a row for each gene, and an expression value for each gene in each sample.
    """
    WIFF_format = "edam:format_3710"
    """
    Mass spectrum file format from QSTAR and QTRAP instruments (ABI/Sciex).
    """
    XEXCLAMATION_MARKTandem_XML = "edam:format_3711"
    """
    Output format used by X! series search engines that is based on the XML language BIOML.
    """
    Thermo_RAW = "edam:format_3712"
    """
    Proprietary file format for mass spectrometry data from Thermo Scientific.
    """
    Mascot_FULL_STOPdat_file = "edam:format_3713"
    """
    "Raw" result file from Mascot database search.
    """
    MaxQuant_APL_peaklist_format = "edam:format_3714"
    """
    Format of peak list files from Andromeda search engine (MaxQuant) that consist of arbitrarily many spectra.
    """
    SBOL = "edam:format_3725"
    """
    Synthetic Biology Open Language (SBOL) is an XML format for the specification and exchange of biological design information in synthetic biology.
    """
    PMML = "edam:format_3726"
    """
    PMML uses XML to represent mining models. The structure of the models is described by an XML Schema.
    """
    OME_TIFF = "edam:format_3727"
    """
    Image file format used by the Open Microscopy Environment (OME).
    """
    LocARNA_PP = "edam:format_3728"
    """
    The LocARNA PP format combines sequence or alignment information and (respectively, single or consensus) ensemble probabilities into an PP 2.0 record.
    """
    dbGaP_format = "edam:format_3729"
    """
    Input format used by the Database of Genotypes and Phenotypes (dbGaP).
    """
    BIOM_format = "edam:format_3746"
    """
    The BIological Observation Matrix (BIOM) is a format for representing biological sample by observation contingency tables in broad areas of comparative omics. The primary use of this format is to represent OTU tables and metagenome tables.
    """
    protXML = "edam:format_3747"
    """
    A format for storage, exchange, and processing of protein identifications created from ms/ms-derived peptide sequence data.
    """
    Linked_data_format = "edam:format_3748"
    """
    A linked data format enables publishing structured data as linked data (Linked Data), so that the data can be interlinked and become more useful through semantic queries.
    """
    JSON_LD = "edam:format_3749"
    """
    JSON-LD, or JavaScript Object Notation for Linked Data, is a method of encoding Linked Data using JSON.
    """
    YAML = "edam:format_3750"
    """
    YAML (YAML Ain't Markup Language) is a human-readable tree-structured data serialisation language.
    """
    DSV = "edam:format_3751"
    """
    Tabular data represented as values in a text file delimited by some character.
    """
    CSV = "edam:format_3752"
    """
    Tabular data represented as comma-separated values in a text file.
    """
    SEQUEST_FULL_STOPout_file = "edam:format_3758"
    """
    "Raw" result file from SEQUEST database search.
    """
    idXML = "edam:format_3764"
    """
    XML file format for files containing information about peptide identifications from mass spectrometry data analysis carried out with OpenMS.
    """
    KNIME_datatable_format = "edam:format_3765"
    """
    Data table formatted such that it can be passed/streamed within the KNIME platform.
    """
    UniProtKB_XML = "edam:format_3770"
    """
    UniProtKB XML sequence features format is an XML format available for downloading UniProt entries.
    """
    UniProtKB_RDF = "edam:format_3771"
    """
    UniProtKB RDF sequence features format is an RDF format available for downloading UniProt entries (in RDF/XML).
    """
    BioJSON_LEFT_PARENTHESISBioXSDRIGHT_PARENTHESIS = "edam:format_3772"
    """
    BioJSON is a BioXSD-schema-based JSON format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web applications and APIs, and object-oriented programming.
    """
    BioYAML = "edam:format_3773"
    """
    BioYAML is a BioXSD-schema-based YAML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web APIs, human readability and editing, and object-oriented programming.
    """
    BioJSON_LEFT_PARENTHESISJalviewRIGHT_PARENTHESIS = "edam:format_3774"
    """
    BioJSON is a JSON format of single multiple sequence alignments, with their annotations, features, and custom visualisation and application settings for the Jalview workbench.
    """
    GSuite = "edam:format_3775"
    """
    GSuite is a tabular format for collections of genome or sequence feature tracks, suitable for integrative multi-track analysis. GSuite contains links to genome/sequence tracks, with additional metadata.
    """
    BTrack = "edam:format_3776"
    """
    BTrack is an HDF5-based binary format for genome or sequence feature tracks and their collections, suitable for integrative multi-track analysis. BTrack is a binary, compressed alternative to the GTrack and GSuite formats.
    """
    MCPD = "edam:format_3777"
    """
    The FAO/Bioversity/IPGRI Multi-Crop Passport Descriptors (MCPD) is an international standard format for exchange of germplasm information.
    """
    Annotated_text_format = "edam:format_3780"
    """
    Data format of an annotated text, e.g. with recognised entities, concepts, and relations.
    """
    PubAnnotation_format = "edam:format_3781"
    """
    JSON format of annotated scientific text used by PubAnnotations and other tools.
    """
    BioC = "edam:format_3782"
    """
    BioC is a standardised XML format for sharing and integrating text data and annotations.
    """
    PubTator_format = "edam:format_3783"
    """
    Native textual export format of annotated scientific text from PubTator.
    """
    Open_Annotation_format = "edam:format_3784"
    """
    A format of text annotation using the linked-data Open Annotation Data Model, serialised typically in RDF or JSON-LD.
    """
    BioNLP_Shared_Task_format = "edam:format_3785"
    """
    A family of similar formats of text annotation, used by BRAT and other tools, known as BioNLP Shared Task format (BioNLP 2009 Shared Task on Event Extraction, BioNLP Shared Task 2011, BioNLP Shared Task 2013), BRAT format, BRAT standoff format, and similar.
    """
    Query_language = "edam:format_3787"
    """
    A query language (format) for structured database queries.
    """
    SQL = "edam:format_3788"
    """
    SQL (Structured Query Language) is the de-facto standard query language (format of queries) for querying and manipulating data in relational databases.
    """
    XQuery = "edam:format_3789"
    """
    XQuery (XML Query) is a query language (format of queries) for querying and manipulating structured and unstructured data, usually in the form of XML, text, and with vendor-specific extensions for other data formats (JSON, binary, etc.).
    """
    SPARQL = "edam:format_3790"
    """
    SPARQL (SPARQL Protocol and RDF Query Language) is a semantic query language for querying and manipulating data stored in Resource Description Framework (RDF) format.
    """
    xsd = "edam:format_3804"
    """
    XML format for XML Schema.
    """
    XMFA = "edam:format_3811"
    """
    XMFA format stands for eXtended Multi-FastA format and is used to store collinear sub-alignments that constitute a single genome alignment.
    """
    GEN = "edam:format_3812"
    """
    The GEN file format contains genetic data and describes SNPs.
    """
    SAMPLE_file_format = "edam:format_3813"
    """
    The SAMPLE file format contains information about each individual i.e. individual IDs, covariates, phenotypes and missing data proportions, from a GWAS study.
    """
    SDF = "edam:format_3814"
    """
    SDF is one of a family of chemical-data file formats developed by MDL Information Systems; it is intended especially for structural information.
    """
    Molfile = "edam:format_3815"
    """
    An MDL Molfile is a file format for holding information about the atoms, bonds, connectivity and coordinates of a molecule.
    """
    Mol2 = "edam:format_3816"
    """
    Complete, portable representation of a SYBYL molecule. ASCII file which contains all the information needed to reconstruct a SYBYL molecule.
    """
    latex = "edam:format_3817"
    """
    format for the LaTeX document preparation system.
    """
    ELAND_format = "edam:format_3818"
    """
    Tab-delimited text file format used by Eland - the read-mapping program distributed by Illumina with its sequencing analysis pipeline - which maps short Solexa sequence reads to the human reference genome.
    """
    Relaxed_PHYLIP_Interleaved = "edam:format_3819"
    """
    Phylip multiple alignment sequence format, less stringent than PHYLIP format.
    """
    Relaxed_PHYLIP_Sequential = "edam:format_3820"
    """
    Phylip multiple alignment sequence format, less stringent than PHYLIP sequential format (format_1998).
    """
    VisML = "edam:format_3821"
    """
    Default XML format of VisANT, containing all the network information.
    """
    GML = "edam:format_3822"
    """
    GML (Graph Modeling Language) is a text file format supporting network data with a very easy syntax. It is used by Graphlet, Pajek, yEd, LEDA and NetworkX.
    """
    FASTG = "edam:format_3823"
    """
    FASTG is a format for faithfully representing genome assemblies in the face of allelic polymorphism and assembly uncertainty.
    """
    NMR_data_format = "edam:format_3824"
    """
    Data format for raw data from a nuclear magnetic resonance (NMR) spectroscopy experiment.
    """
    nmrML = "edam:format_3825"
    """
    nmrML is an MSI supported XML-based open access format for metabolomics NMR raw and processed spectral data. It is accompanies by an nmrCV (controlled vocabulary) to allow ontology-based annotations.
    """
    proBAM = "edam:format_3826"
    """
    . proBAM is an adaptation of BAM (format_2572), which was extended to meet specific requirements entailed by proteomics data.
    """
    proBED = "edam:format_3827"
    """
    . proBED is an adaptation of BED (format_3003), which was extended to meet specific requirements entailed by proteomics data.
    """
    Raw_microarray_data_format = "edam:format_3828"
    """
    Data format for raw microarray data.
    """
    GPR = "edam:format_3829"
    """
    GenePix Results (GPR) text file format developed by Axon Instruments that is used to save GenePix Results data.
    """
    ARB = "edam:format_3830"
    """
    Binary format used by the ARB software suite.
    """
    consensusXML = "edam:format_3832"
    """
    OpenMS format for grouping features in one map or across several maps.
    """
    featureXML = "edam:format_3833"
    """
    OpenMS format for quantitation results (LC/MS features).
    """
    mzData = "edam:format_3834"
    """
    Now deprecated data format of the HUPO Proteomics Standards Initiative. Replaced by mzML (format_3244).
    """
    TIDE_TXT = "edam:format_3835"
    """
    Format supported by the Tide tool for identifying peptides from tandem mass spectra.
    """
    BLAST_XML_v2_results_format = "edam:format_3836"
    """
    XML format as produced by the NCBI Blast package v2.
    """
    pptx = "edam:format_3838"
    """
    Microsoft Powerpoint format.
    """
    ibd = "edam:format_3839"
    """
    ibd is a data format for mass spectrometry imaging data.
    """
    NLP_format = "edam:format_3841"
    """
    Data format used in Natural Language Processing.
    """
    BEAST = "edam:format_3843"
    """
    XML input file format for BEAST Software (Bayesian Evolutionary Analysis Sampling Trees).
    """
    Chado_XML = "edam:format_3844"
    """
    Chado-XML format is a direct mapping of the Chado relational schema into XML.
    """
    HSAML = "edam:format_3845"
    """
    An alignment format generated by PRANK/PRANKSTER consisting of four elements: newick, nodes, selection and model.
    """
    InterProScan_XML = "edam:format_3846"
    """
    Output xml file from the InterProScan sequence analysis application.
    """
    KGML = "edam:format_3847"
    """
    The KEGG Markup Language (KGML) is an exchange format of the KEGG pathway maps, which is converted from internally used KGML+ (KGML+SVG) format.
    """
    PubMed_XML = "edam:format_3848"
    """
    XML format for collected entries from bibliographic databases MEDLINE and PubMed.
    """
    MSAML = "edam:format_3849"
    """
    A set of XML compliant markup components for describing multiple sequence alignments.
    """
    OrthoXML = "edam:format_3850"
    """
    OrthoXML is designed broadly to allow the storage and comparison of orthology data from any ortholog database. It establishes a structure for describing orthology relationships while still allowing flexibility for database-specific information to be encapsulated in the same format.
    """
    PSDML = "edam:format_3851"
    """
    Tree structure of Protein Sequence Database Markup Language generated using Matra software.
    """
    SeqXML = "edam:format_3852"
    """
    SeqXML is an XML Schema to describe biological sequences, developed by the Stockholm Bioinformatics Centre.
    """
    UniParc_XML = "edam:format_3853"
    """
    XML format for the UniParc database.
    """
    UniRef_XML = "edam:format_3854"
    """
    XML format for the UniRef reference clusters.
    """
    CWL = "edam:format_3857"
    """
    Common Workflow Language (CWL) format for description of command-line tools and workflows.
    """
    Waters_RAW = "edam:format_3858"
    """
    Proprietary file format for mass spectrometry data from Waters.
    """
    JCAMP_DX = "edam:format_3859"
    """
    A standardized file format for data exchange in mass spectrometry, initially developed for infrared spectrometry.
    """
    NLP_annotation_format = "edam:format_3862"
    """
    An NLP format used for annotated textual documents.
    """
    NLP_corpus_format = "edam:format_3863"
    """
    NLP format used by a specific type of corpus (collection of texts).
    """
    mirGFF3 = "edam:format_3864"
    """
    mirGFF3 is a common format for microRNA data resulting from small-RNA RNA-Seq workflows.
    """
    RNA_annotation_format = "edam:format_3865"
    """
    A "placeholder" concept for formats of annotated RNA data, including e.g. microRNA and RNA-Seq data.
    """
    Trajectory_format = "edam:format_3866"
    """
    File format to store trajectory information for a 3D structure .
    """
    Trajectory_format_LEFT_PARENTHESISbinaryRIGHT_PARENTHESIS = "edam:format_3867"
    """
    Binary file format to store trajectory information for a 3D structure .
    """
    Trajectory_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "edam:format_3868"
    """
    Textual file format to store trajectory information for a 3D structure .
    """
    HDF = "edam:format_3873"
    """
    HDF is the name of a set of file formats and libraries designed to store and organize large amounts of numerical data, originally developed at the National Center for Supercomputing Applications at the University of Illinois.
    """
    PCAzip = "edam:format_3874"
    """
    PCAZip format is a binary compressed file to store atom coordinates based on Essential Dynamics (ED) and Principal Component Analysis (PCA).
    """
    XTC = "edam:format_3875"
    """
    Portable binary format for trajectories produced by GROMACS package.
    """
    TNG = "edam:format_3876"
    """
    Trajectory Next Generation (TNG) is a format for storage of molecular simulation data. It is designed and implemented by the GROMACS development group, and it is called to be the substitute of the XTC format.
    """
    XYZ = "edam:format_3877"
    """
    The XYZ chemical file format is widely supported by many programs, although many slightly different XYZ file formats coexist (Tinker XYZ, UniChem XYZ, etc.). Basic information stored for each atom in the system are x, y and z coordinates and atom element/atomic number.
    """
    mdcrd = "edam:format_3878"
    """
    AMBER trajectory (also called mdcrd), with 10 coordinates per line and format F8.3 (fixed point notation with field width 8 and 3 decimal places).
    """
    Topology_format = "edam:format_3879"
    """
    Format of topology files; containing the static information of a structure molecular system that is needed for a molecular simulation.
    """
    GROMACS_top = "edam:format_3880"
    """
    GROMACS MD package top textual files define an entire structure system topology, either directly, or by including itp files.
    """
    AMBER_top = "edam:format_3881"
    """
    AMBER Prmtop file (version 7) is a structure topology text file divided in several sections designed to be parsed easily using simple Fortran code. Each section contains particular topology information, such as atom name, charge, mass, angles, dihedrals, etc.
    """
    PSF = "edam:format_3882"
    """
    X-Plor Protein Structure Files (PSF) are structure topology files used by NAMD and CHARMM molecular simulations programs. PSF files contain six main sections of interest: atoms, bonds, angles, dihedrals, improper dihedrals (force terms used to maintain planarity) and cross-terms.
    """
    GROMACS_itp = "edam:format_3883"
    """
    GROMACS itp files (include topology) contain structure topology information, and are typically included in GROMACS topology files (GROMACS top). Itp files are used to define individual (or multiple) components of a topology as a separate file. This is particularly useful if there is a molecule that is used frequently, and also reduces the size of the system topology file, splitting it in different parts.
    """
    FF_parameter_format = "edam:format_3884"
    """
    Format of force field parameter files, which store the set of parameters (charges, masses, radii, bond lengths, bond dihedrals, etc.) that are essential for the proper description and simulation of a molecular system.
    """
    BinPos = "edam:format_3885"
    """
    Scripps Research Institute BinPos format is a binary formatted file to store atom coordinates.
    """
    RST = "edam:format_3886"
    """
    AMBER coordinate/restart file with 6 coordinates per line and decimal format F12.7 (fixed point notation with field width 12 and 7 decimal places).
    """
    CHARMM_rtf = "edam:format_3887"
    """
    Format of CHARMM Residue Topology Files (RTF), which define groups by including the atoms, the properties of the group, and bond and charge information.
    """
    AMBER_frcmod = "edam:format_3888"
    """
    AMBER frcmod (Force field Modification) is a file format to store any modification to the standard force field needed for a particular molecule to be properly represented in the simulation.
    """
    AMBER_off = "edam:format_3889"
    """
    AMBER Object File Format library files (OFF library files) store residue libraries (forcefield residue parameters).
    """
    NMReDATA = "edam:format_3906"
    """
    MReData is a text based data standard for processed NMR data. It is relying on SDF molecule data and allows to store assignments of NMR peaks to molecule features. The NMR-extracted data (or "NMReDATA") includes: Chemical shift,scalar coupling, 2D correlation, assignment, etc.
    """
    BpForms = "edam:format_3909"
    """
    BpForms is a string format for concretely representing the primary structures of biopolymers, including DNA, RNA, and proteins that include non-canonical nucleic and amino acids. See https://www.bpforms.org for more information.
    """
    trr = "edam:format_3910"
    """
    Format of trr files that contain the trajectory of a simulation experiment used by GROMACS.
    """
    msh = "edam:format_3911"
    """
    Mash sketch is a format for sequence / sequence checksum information. To make a sketch, each k-mer in a sequence is hashed, which creates a pseudo-random identifier. By sorting these hashes, a small subset from the top of the sorted list can represent the entire sequence.
    """
    Loom = "edam:format_3913"
    """
    The Loom file format is based on HDF5, a standard for storing large numerical datasets. The Loom format is designed to efficiently hold large omics datasets. Typically, such data takes the form of a large matrix of numbers, along with metadata for the rows and columns.
    """
    Zarr = "edam:format_3915"
    """
    The Zarr format is an implementation of chunked, compressed, N-dimensional arrays for storing data.
    """
    MTX = "edam:format_3916"
    """
    The Matrix Market matrix (MTX) format stores numerical or pattern matrices in a dense (array format) or sparse (coordinate format) representation.
    """
    BcForms = "edam:format_3951"
    """
    BcForms is a format for abstractly describing the molecular structure (atoms and bonds) of macromolecular complexes as a collection of subunits and crosslinks. Each subunit can be described with BpForms (http://edamontology.org/format_3909) or SMILES (http://edamontology.org/data_2301). BcForms uses an ontology of crosslinks to abstract the chemical details of crosslinks from the descriptions of complexes (see https://bpforms.org/crosslink.html).
    """
    N_Quads = "edam:format_3956"
    """
    N-Quads is a line-based, plain text format for encoding an RDF dataset. It includes information about the graph each triple belongs to.
    """
    Vega = "edam:format_3969"
    """
    Vega is a visualization grammar, a declarative language for creating, saving, and sharing interactive visualization designs. With Vega, you can describe the visual appearance and interactive behavior of a visualization in a JSON format, and generate web-based views using Canvas or SVG.
    """
    Vega_lite = "edam:format_3970"
    """
    Vega-Lite is a high-level grammar of interactive graphics. It provides a concise JSON syntax for rapidly generating visualizations to support analysis. Vega-Lite specifications can be compiled to Vega specifications.
    """
    NeuroML = "edam:format_3971"
    """
    A model description language for computational neuroscience.
    """
    BNGL = "edam:format_3972"
    """
    BioNetGen is a format for the specification and simulation of rule-based models of biochemical systems, including signal transduction, metabolic, and genetic regulatory networks.
    """
    Docker_image = "edam:format_3973"
    """
    A Docker image is a file, comprised of multiple layers, that is used to execute code in a Docker container. An image is essentially built from the instructions for a complete and executable version of an application, which relies on the host OS kernel.
    """
    GFA_1 = "edam:format_3975"
    """
    Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology.
    """
    GFA_2 = "edam:format_3976"
    """
    Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology. GFA2 is an update of GFA1 which is not compatible with GFA1.
    """
    ObjTables = "edam:format_3977"
    """
    ObjTables is a toolkit for creating reusable datasets that are both human and machine-readable, combining the ease of spreadsheets (e.g., Excel workbooks) with the rigor of schemas (classes, their attributes, the type of each attribute, and the possible relationships between instances of classes). ObjTables consists of a format for describing schemas for spreadsheets, numerous data types for science, a syntax for indicating the class and attribute represented by each table and column in a workbook, and software for using schemas to rigorously validate, merge, split, compare, and revision datasets.
    """
    CONTIG = "edam:format_3978"
    """
    The CONTIG format used for output of the SOAPdenovo alignment program. It contains contig sequences generated without using mate pair information.
    """
    WEGO = "edam:format_3979"
    """
    WEGO native format used by the Web Gene Ontology Annotation Plot application.   Tab-delimited format with gene names and others GO IDs (columns) with one annotation record per line.
    """
    RPKM = "edam:format_3980"
    """
    Tab-delimited format for gene expression levels table, calculated as Reads Per Kilobase per Million (RPKM) mapped reads.
    """
    TAR_format = "edam:format_3981"
    """
    TAR archive file format generated by the Unix-based utility tar.
    """
    CHAIN = "edam:format_3982"
    """
    The CHAIN format describes a pairwise alignment that allow gaps in both sequences simultaneously and is used by the UCSC Genome Browser.
    """
    NET = "edam:format_3983"
    """
    The NET file format is used to describe the data that underlie the net alignment annotations in the UCSC Genome Browser.
    """
    QMAP = "edam:format_3984"
    """
    Format of QMAP files generated for methylation data from an internal BGI pipeline.
    """
    gxformat2 = "edam:format_3985"
    """
    An emerging format for high-level Galaxy workflow description.
    """
    WMV = "edam:format_3986"
    """
    The proprietary native video format of various Microsoft programs such as Windows Media Player.
    """
    ZIP_format = "edam:format_3987"
    """
    ZIP is an archive file format that supports lossless data compression.
    """
    LSM = "edam:format_3988"
    """
    Zeiss' proprietary image format based on TIFF.
    """
    GZIP_format = "edam:format_3989"
    """
    GNU zip compressed file format common to Unix-based operating systems.
    """
    AVI = "edam:format_3990"
    """
    Audio Video Interleaved (AVI) format is a multimedia container format for AVI files, that allows synchronous audio-with-video playback.
    """
    TrackDB = "edam:format_3991"
    """
    A declaration file format for UCSC browsers track dataset display characteristics.
    """
    CIGAR_format = "edam:format_3992"
    """
    Compact Idiosyncratic Gapped Alignment Report format is a compressed (run-length encoded) pairwise alignment format. It is useful for representing long (e.g. genomic) pairwise alignments.
    """
    Stereolithography_format = "edam:format_3993"
    """
    STL is a file format native to the stereolithography CAD software created by 3D Systems. The format is used to save and share surface-rendered 3D images and also for 3D printing.
    """
    U3D = "edam:format_3994"
    """
    U3D (Universal 3D) is a compressed file format and data structure for 3D computer graphics. It contains 3D model information such as triangle meshes, lighting, shading, motion data, lines and points with color and structure.
    """
    Texture_file_format = "edam:format_3995"
    """
    Bitmap image format used for storing textures.
    """
    Python_script = "edam:format_3996"
    """
    Format for scripts writtenin Python - a widely used high-level programming language for general-purpose programming.
    """
    MPEG_4 = "edam:format_3997"
    """
    A digital multimedia container format most commonly used to store video and audio.
    """
    Perl_script = "edam:format_3998"
    """
    Format for scripts written in Perl - a family of high-level, general-purpose, interpreted, dynamic programming languages.
    """
    R_script = "edam:format_3999"
    """
    Format for scripts written in the R language - an open source programming language and software environment for statistical computing and graphics that is supported by the R Foundation for Statistical Computing.
    """
    R_markdown = "edam:format_4000"
    """
    A file format for making dynamic documents (R Markdown scripts) with the R language.
    """
    pickle = "edam:format_4002"
    """
    Format used by Python pickle module for serializing and de-serializing a Python object structure.
    """
    NumPy_format = "edam:format_4003"
    """
    The standard binary file format used by NumPy - a fundamental package for scientific computing with Python - for persisting a single arbitrary NumPy array on disk. The format stores all of the shape and dtype information necessary to reconstruct the array correctly.
    """
    SimTools_repertoire_file_format = "edam:format_4004"
    """
    Format of repertoire (archive) files that can be read by SimToolbox (a MATLAB toolbox for structured illumination fluorescence microscopy) or alternatively extracted with zip file archiver software.
    """
    Configuration_file_format = "edam:format_4005"
    """
    A configuration file used by various programs to store settings that are specific to their respective software.
    """
    Zstandard_format = "edam:format_4006"
    """
    Format used by the Zstandard real-time compression algorithm.
    """
    MATLAB_script = "edam:format_4007"
    """
    The file format for MATLAB scripts or functions.
    """
    PEtab = "edam:format_4015"
    """
    A data format for specifying parameter estimation problems in systems biology.
    """
    gVCF = "edam:format_4018"
    """
    Genomic Variant Call Format (gVCF) is a version of VCF that includes not only the positions that are variant when compared to a reference genome, but also the non-variant positions as ranges, including metrics of confidence that the positions in the range are actually non-variant e.g. minimum read-depth and genotype quality.
    """
    cml = "edam:format_4023"
    """
    Chemical Markup Language (CML) is an XML-based format for encoding detailed information about a wide range of chemical concepts.
    """
    cif = "edam:format_4024"
    """
    Crystallographic Information File (CIF) is a data exchange standard file format for Crystallographic Information and related Structural Science data.
    """
    BioSimulators_format_for_the_specifications_of_biosimulation_tools = "edam:format_4025"
    """
    Format for describing the capabilities of a biosimulation tool including the modeling frameworks, simulation algorithms, and modeling formats that it supports, as well as metadata such as a list of the interfaces, programming languages, and operating systems supported by the tool; a link to download the tool; a list of the authors of the tool; and the license to the tool.
    """
    BioSimulators_standard_for_command_line_interfaces_for_biosimulation_tools = "edam:format_4026"
    """
    Outlines the syntax and semantics of the input and output arguments for command-line interfaces for biosimulation tools.
    """
    PQR = "edam:format_4035"
    """
    Data format derived from the standard PDB format, which enables user to incorporate parameters for charge and radius to the existing PDB data file.
    """
    PDBQT = "edam:format_4036"
    """
    Data format used in AutoDock 4 for storing atomic coordinates, partial atomic charges and AutoDock atom types for both receptors and ligands.
    """
    MSP = "edam:format_4039"
    """
    MSP is a data format for mass spectrometry data.
    """
    maDMP = "edam:format_4041"
    """
    maDMP stands for machine-actionable data management plan, a standard for DMPs developed by the Research Data Alliance (RDA).
    """
    Nextflow = "edam:format_4048"
    """
    Nextflow is a workflow system for creating scalable, portable, and reproducible workflows.
    """
    Snakemake = "edam:format_4049"
    """
    The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.
    """
    SDRF = "edam:format_4050"
    """
    Sample and Data Relationship File for a proteomics experiment.
    """
    mzTab_M = "edam:format_4058"
    """
    mzTab-M is a light-weight, tab-delimited format for mass spectrometry-based chemical profiling data, including metabolomics.
    """
    mzTab_L = "edam:format_4059"
    """
    mzTab-L is a light-weight, tab-delimited format for mass spectrometry-based lipidomics data. It is a compatible version of mzTab-M, with additional rules and information standard (reporting guidelines).
    """
    ISA_Tab_Investigation_file = "edam:format_4066"
    """
    ISA-Tab Investigation file (i_Investigation.txt) contains metadata describing the overall goals, means, and context of an investigation/experiment, including references to associated Study and Assay files.
    """
    ISA_Tab_Study_file = "edam:format_4067"
    """
    ISA-Tab Study file (s_*.txt) contains sample metadata describing the subjects under study, their sources, characteristics, sampling methodology, and any treatments or manipulations applied.
    """
    ISA_Tab_Assay_file = "edam:format_4068"
    """
    ISA-Tab Assay file (a_*.txt) contains assay metadata describing test steps and analytical measurements performed on the sample material, including measurement types, technology used, and references to raw and derived data files.
    """
    ISA_JSON = "edam:format_4069"
    """
    ISA-JSON stands for Investigation / Study / Assay (ISA) JavaScript Object Notation (JSON) format, and it is comprised of metadata describing observational or experimental scientific studies.
    """
    mwTab = "edam:format_4070"
    """
    mwTab is a tab-delimited text format developed by the Metabolomics Workbench to facilitate programmatic processing of metabolomics data and metadata suitable for submission to the repository.
    """
    MHD = "edam:format_4071"
    """
    MHD (MetabolomicsHub Common Data Model) is a JSON-based format providing a standardised, FAIR-compliant data model for the exchange, discovery, and reuse of metabolomics dataset metadata across international repositories.
    """
    MHD_announcement = "edam:format_4072"
    """
    The MHD announcement file is a JSON-based format used to notify MetabolomicsHub of new or updated dataset submissions, serving as a manifest or notification file within the MHD data flow.
    """
    MetaboLights_MAF = "edam:format_4073"
    """
    MetaboLights MAF (Metabolite Annotation File) is a tab-separated file format used to report metabolites identified or annotated in a metabolomics study, including compound identifiers, chemical structure representations, mass-to-charge ratios, retention times, and per-sample quantitative measurements.
    """


class EnumEthnicity(str, Enum):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    Hispanic_or_Latino = "CDCREC:2135-2"
    Not_Hispanic_or_Latino = "CDCREC:2186-5"


class EnumFamilyRelation(str):
    """
    Definitions of family relations as provided by KIN Ontology.
    """
    pass


class EnumFamilyRole(str, Enum):
    """
    Example terms related to an individual's role in a family study.
    """
    Proband = "snomedct:85900004"
    isBiologicalMotherOf = "KIN:027"
    """
    A relation that indicates that a person is the biological mother of another person.
    """
    Mother = "snomedct:72705000"


class EnumFamilyType(str, Enum):
    """
    Enumerations describing research family type
    """
    ParentLEFT_PARENTHESISsRIGHT_PARENTHESIS_and_ChildLEFT_PARENTHESISrenRIGHT_PARENTHESIS = "CAMO:0000002"
    """
    This family study includes at a minimum one parent and one child.
    """
    Duo = "CAMO:0000003"
    """
    This family study includes at a minimum one parent and one affected child.
    """
    Trio = "CAMO:0000004"
    """
    This family study includes at a minimum two parents of one affected child.
    """
    TrioPLUS_SIGN = "CAMO:0000005"
    """
    This family study includes at a minimum two parents of one affected child and at least one other child.
    """
    Case_Only = "CAMO:0000006"
    """
    This family study includes only one or more cases.
    """
    Proband_Only = "CAMO:0000007"
    """
    This family study includes only one or more probands.
    """
    Control_Only = "CAMO:0000008"
    """
    This family study includes only one or more controls.
    """


class EnumFileHashType(str, Enum):
    """
    Types of file hashes supported.
    """
    MD5 = "MS:1000568"
    """
    MD5 (Message-Digest algorithm 5) is a (now deprecated) cryptographic hash function with a 128-bit hash value used to check the integrity of files.
    """
    ETag = "CAMO:0000022"
    """
    The entity tag is a hash of the object. The ETag reflects changes only to the contents of an object, not its metadata. The ETag may or may not be an MD5 digest of the object data.
    """
    SHA_1 = "MS:1000569"
    """
    SHA-1 (Secure Hash Algorithm-1) is a cryptographic hash function designed by the National Security Agency (NSA). It is also used to verify file integrity. Since 2011 it has been deprecated by the NIST as a U. S. government standard.
    """
    SHA_256 = "MS:1003151"
    """
    SHA-256 (member of Secure Hash Algorithm-2 family) is a cryptographic hash function designed by the National Security Agency (NSA) and published by the NIST as a U. S. government standard. It is also used to verify file integrity.
    """


class EnumLaterality(str):
    """
    Laterality information for the site
    """
    pass


class EnumOrganism(str, Enum):
    """
    Common Organism types.
    """
    Human = "NCBITaxon:9606"
    Mus_musculus = "NCBITaxon:10090"


class EnumParticipantLifespanStage(str):
    """
    Stages of life during which participants may be recruited. From NICHD Pediatric Terminology. https://evs.nci.nih.gov/ftp1/Pediatric_Terminologies/NICHD/About.html
    """
    pass


class EnumPresentAbsent(str, Enum):
    """
    Options for describing presence or absence. Derived from SNOMED CT Known codes. The "Known" codes and "Not suspected" are the broadest terms and suitable for general use.
    """
    Known_present = "snomedct:410515003"
    Known_absent = "snomedct:410516002"
    Known_possible = "snomedct:410590009"
    Definitely_present = "snomedct:410591008"
    Probably_present = "snomedct:410592001"
    Probably_not_present = "snomedct:410593006"
    Definitely_not_present = "snomedct:410594000"
    Confirmed_present = "snomedct:410605003"
    Suspected = "snomedct:415684004"
    Not_suspected = "snomedct:428263003"
    Refuted = "snomedct:723511001"


class EnumProgram(str, Enum):
    """
    Specific funding program examples.
    """
    INCLUDE = "https://www.nih.gov/include-project"
    """
    The INCLUDE (INvestigation of Co-occurring conditions across the Lifespan to Understand Down syndromE) Project was launched in June 2018 in support of a Congressional directive in the fiscal year (FY) 2018 Omnibus Appropriations. The directive called for a new trans-NIH research initiative on critical health and quality-of-life needs for individuals with Down syndrome.
    """
    Kids_First = "https://commonfund.nih.gov/KidsFirst"
    """
    The goal of the Gabriella Miller Kids First Pediatric Research Program (Kids First) is to help researchers uncover new insights into the biology of childhood cancer and congenital anomalies, including the discovery of shared genetic pathways between these disorders. Children with birth defects have an increased risk of developing childhood cancer. This suggests there are shared genetic pathways underlying some types of childhood cancer and congenital anomalies.
    """


class EnumRace(str, Enum):
    """
    Participant Race
    """
    American_Indian_or_Alaska_Native = "CDCREC:1002-5"
    Asian = "CDCREC:2028-9"
    Black_or_African_American = "CDCREC:2054-5"
    Native_Hawaiian_or_Other_Pacific_Islander = "CDCREC:2076-8"
    White = "CDCREC:2106-3"
    Middle_Eastern_or_North_African = "CDCREC:2118-8"


class EnumResearchDomain(str, Enum):
    """
    Domains of research activities.
    """
    Behavior_and_Behavior_Mechanisms = "mesh:D001520"
    Congenital_Heart_Defects = "mesh:D006330"
    Immune_System_Diseases = "mesh:D007154"
    Hematologic_Diseases = "mesh:D006402"
    Neurodevelopment = "mesh:D065886"
    Sleep_Wake_Disorders = "mesh:D012893"
    All_Co_occurring_Conditions = "mesh:D013568"
    Physical_Fitness = "mesh:D010809"


class EnumSampleCollectionMethod(str):
    """
    The approach used to collect the biospecimen.
    """
    pass


class EnumSex(str, Enum):
    """
    Subject Sex
    """
    Female = "snomedct:248152002"
    Male = "snomedct:248153007"


class EnumSite(str):
    """
    The location of the specimen collection.
    """
    pass


class EnumSpatialQualifiers(str, Enum):
    """
    Any spatial/location qualifiers.
    """
    Long_axis = "snomedct:103339001"
    Short_axis = "snomedct:103340004"
    Off_axis = "snomedct:103341000"
    Mid_longitudinal = "snomedct:103342007"
    Parasagittal = "snomedct:103343002"
    Transvesical = "snomedct:103344008"
    Transthecal = "snomedct:103345009"
    Transsplenic = "snomedct:103346005"
    Transrenal = "snomedct:103347001"
    Transpleural = "snomedct:103348006"
    Transpancreatic = "snomedct:103349003"
    Transgastric = "snomedct:103353001"
    Transmural = "snomedct:103354007"
    Capsular = "snomedct:11070000"
    Arcuate = "snomedct:1146002"
    Intermediate = "snomedct:11896004"
    Non_adjacent = "snomedct:1217011006"
    Intra_articular = "snomedct:131183008"
    Area_of_defined_region = "snomedct:131184002"
    Vertical_long_axis = "snomedct:131185001"
    Horizontal_long_axis = "snomedct:131186000"
    Major_Axis = "snomedct:131187009"
    Minor_Axis = "snomedct:131188004"
    Perpendicular_axis = "snomedct:131189007"
    Radius = "snomedct:131190003"
    Perimeter = "snomedct:131191004"
    Peripheral = "snomedct:14414005"
    Angular = "snomedct:1483009"
    Juxta_posed = "snomedct:18769003"
    Hemispheric = "snomedct:21006006"
    Over = "snomedct:21481007"
    Horizontal = "snomedct:24020000"
    Right = "snomedct:24028007"
    Axial = "snomedct:24422004"
    Horizontal___3_and_9 = "snomedct:255527003"
    Horizontal_and_vertical = "snomedct:255528008"
    Mediolateral = "snomedct:261129000"
    Central = "snomedct:26216008"
    Superficial = "snomedct:26283006"
    Bony_extra_articular = "snomedct:263687007"
    Bony_intra_articular = "snomedct:263688002"
    Lateral_to_the_left = "snomedct:264731004"
    Lateral_to_the_right = "snomedct:264732006"
    Linear_longitudinal = "snomedct:264733001"
    Linear_transverse = "snomedct:264737000"
    Posterolateral_to_the_left = "snomedct:264741001"
    Posterolateral_to_the_right = "snomedct:264742008"
    Horizontal_cleavage = "snomedct:264839005"
    Triangular = "snomedct:27237009"
    Rhomboid = "snomedct:28241006"
    Right_curve = "snomedct:28947002"
    Sagittal = "snomedct:30730003"
    Quadrangular = "snomedct:30899007"
    Portal = "snomedct:32381004"
    Preaxial = "snomedct:32400000"
    Vertical = "snomedct:33096000"
    Efferent = "snomedct:33843005"
    Behind = "snomedct:350722008"
    Below = "snomedct:351726001"
    Supra_ = "snomedct:352730000"
    Upward = "snomedct:353734004"
    Circular = "snomedct:354652004"
    Surrounding = "snomedct:355648006"
    Anterolateral = "snomedct:37197008"
    Longitudinal = "snomedct:38717003"
    Bent = "snomedct:39187007"
    Proximal = "snomedct:40415009"
    Regional = "snomedct:410674003"
    Surface = "snomedct:410679008"
    Area = "snomedct:42798000"
    Apical = "snomedct:43674008"
    Cylindrical = "snomedct:45226003"
    Distal = "snomedct:46053002"
    Left_curve = "snomedct:47021000"
    Lateral = "snomedct:49370004"
    Afferent = "snomedct:49530007"
    Linear = "snomedct:50009006"
    Stellate = "snomedct:50362007"
    Junctional = "snomedct:50974003"
    Right_and_left = "snomedct:51440002"
    Remote = "snomedct:5686001"
    Square = "snomedct:56924007"
    Along_edge = "snomedct:57183005"
    Basal = "snomedct:57195005"
    Rectangular = "snomedct:59410002"
    Curved = "snomedct:60301000"
    Postaxial = "snomedct:60583000"
    Subcapsular = "snomedct:61397002"
    Sectional = "snomedct:62083003"
    Segmental = "snomedct:62372003"
    Transverse = "snomedct:62824007"
    Cephalic = "snomedct:66787007"
    Gutter = "snomedct:68493006"
    Extracellular = "snomedct:69320009"
    Saccular = "snomedct:69389007"
    Incisal = "snomedct:710097009"
    Occlusal = "snomedct:710098004"
    Mesial = "snomedct:710099007"
    Left = "snomedct:7771000"
    Deep = "snomedct:795002"
    Coronal = "snomedct:81654009"
    Intracellular = "snomedct:83167003"
    Straddling = "snomedct:84177009"
    Extra_articular = "snomedct:87687004"
    Posterolateral = "snomedct:90069004"
    Marginal = "snomedct:112233002"
    Intercostal = "snomedct:1197041002"
    Intralobular = "snomedct:1285325005"
    Anatomical_reference_point_of_right_atrium = "snomedct:128590009"
    Inlet_projection = "snomedct:1362012009"
    Unilobar = "snomedct:1363295008"
    Ipsilateral_multilobar = "snomedct:1363296009"
    Side = "snomedct:182353008"
    Sublingual = "snomedct:225780003"
    Intra_arterial = "snomedct:229801003"
    Ipsilateral = "snomedct:255208005"
    Contralateral = "snomedct:255209002"
    Inframammary = "snomedct:255348000"
    Panretinal = "snomedct:255472009"
    Left_upper_segment = "snomedct:255482005"
    Lower_segment = "snomedct:255486008"
    Right_lower_segment = "snomedct:255496004"
    Right_upper_segment = "snomedct:255499006"
    Upper_segment = "snomedct:255501003"
    Underlay = "snomedct:255546002"
    Overlay = "snomedct:255547006"
    Sandwich_graft = "snomedct:255548001"
    Anterior = "snomedct:255549009"
    Anterior_to_epiglottis = "snomedct:255550009"
    Posterior = "snomedct:255551008"
    Posterior_to_epiglottis = "snomedct:255552001"
    Dorsal = "snomedct:255554000"
    Intracerebral = "snomedct:255557007"
    Intragastric = "snomedct:255558002"
    Intramuscular = "snomedct:255559005"
    Intravenous = "snomedct:255560000"
    Medial = "snomedct:255561001"
    Mid = "snomedct:255562008"
    Mid_zone = "snomedct:255563003"
    Perivascular = "snomedct:255564009"
    Peripapillary = "snomedct:255565005"
    Postauricular = "snomedct:255567002"
    Retrosternal = "snomedct:255568007"
    Suprasternal = "snomedct:255569004"
    Palatal_lingual = "snomedct:255579002"
    Septal = "snomedct:255584008"
    Drug_in_contact_with_skin = "snomedct:255690001"
    Via_collaterals = "snomedct:258186003"
    Via_native_vessel___graft_impaired = "snomedct:258187007"
    Via_native_vessel___graft_occluded = "snomedct:258188002"
    Via_skip_graft = "snomedct:258189005"
    Supratentorial = "snomedct:258329003"
    Infratentorial = "snomedct:258330008"
    Interdental = "snomedct:260240005"
    number_1_oAPOSTROPHEclock_position = "snomedct:260318004"
    number_1FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260319007"
    number_10_oAPOSTROPHEclock_position = "snomedct:260322009"
    number_10FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260323004"
    number_11_oAPOSTROPHEclock_position = "snomedct:260324005"
    number_11FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260325006"
    number_12_oAPOSTROPHEclock_position = "snomedct:260326007"
    number_12FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260327003"
    number_2_oAPOSTROPHEclock_position = "snomedct:260328008"
    number_2FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260329000"
    number_3_oAPOSTROPHEclock_position = "snomedct:260330005"
    number_3FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260331009"
    number_4_oAPOSTROPHEclock_position = "snomedct:260333007"
    number_4FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260334001"
    number_5_oAPOSTROPHEclock_position = "snomedct:260335000"
    number_5FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260336004"
    number_6_oAPOSTROPHEclock_position = "snomedct:260337008"
    number_6FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260338003"
    number_7_oAPOSTROPHEclock_position = "snomedct:260339006"
    number_7FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260340008"
    number_8_oAPOSTROPHEclock_position = "snomedct:260341007"
    number_8FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260342000"
    number_9_oAPOSTROPHEclock_position = "snomedct:260343005"
    number_9FULL_STOP30_oAPOSTROPHEclock_position = "snomedct:260344004"
    Projection = "snomedct:260419006"
    Left_lateral_oblique = "snomedct:260421001"
    C1_C2_left_oblique = "snomedct:260422008"
    Right_lateral_oblique = "snomedct:260424009"
    C1_C2_right_oblique = "snomedct:260425005"
    Medial_oblique = "snomedct:260426006"
    Oblique_lateral = "snomedct:260427002"
    Mandible_X_ray___lateral_oblique = "snomedct:260428007"
    Anteroposterior_left_lateral_decubitus = "snomedct:260430009"
    C1_C2_left_lateral = "snomedct:260431008"
    Left_true_lateral = "snomedct:260432001"
    Anteroposterior_right_lateral_decubitus = "snomedct:260434000"
    C1_C2_right_lateral = "snomedct:260435004"
    Right_true_lateral = "snomedct:260436003"
    Lateral_vertical_beam = "snomedct:260437007"
    Lateral_horizontal_beam = "snomedct:260438002"
    Lateral_inverted = "snomedct:260439005"
    True_lateral_of_mandible = "snomedct:260440007"
    Frog_lateral = "snomedct:260441006"
    Erect_lateral = "snomedct:260442004"
    Anteroposterior_inverted = "snomedct:260443009"
    Rotated_posteroanterior = "snomedct:260444003"
    Posteroanterior_20_degree = "snomedct:260445002"
    Posteroanterior_in_ulnar_deviation = "snomedct:260446001"
    Penetrated_posteroanterior = "snomedct:260447005"
    Lordotic_projection = "snomedct:260450008"
    Supine_decubitus = "snomedct:260451007"
    Decubitus = "snomedct:260452000"
    InternalSOLIDUSexternal_rotation = "snomedct:260453005"
    number_45_degree_projection = "snomedct:260454004"
    Head_and_neck_projection = "snomedct:260455003"
    Slit_TowneAPOSTROPHEs = "snomedct:260458001"
    Reverse_TowneAPOSTROPHEs = "snomedct:260459009"
    Slit_35_degree_fronto_occipital = "snomedct:260460004"
    Vertex_projection = "snomedct:260461000"
    Left_StenverAPOSTROPHEs = "snomedct:260463002"
    Right_StenverAPOSTROPHEs = "snomedct:260464008"
    Occipitofrontal_projection = "snomedct:260465009"
    Occipitomental_projection = "snomedct:260466005"
    Occipitomental___erect = "snomedct:260467001"
    Occipitomental___tilted = "snomedct:260468006"
    Occipitomental___prone = "snomedct:260469003"
    Occipitomental___15_degree = "snomedct:260470002"
    Occipitomental___30_degree = "snomedct:260471003"
    Occipitomental___45_degree = "snomedct:260472005"
    Waters___35_degree_tilt_to_radiographic_baseline = "snomedct:260473000"
    Submentovertical_reduced_exposure_for_zygomatic_arches = "snomedct:260475007"
    Slit_submentovertical = "snomedct:260476008"
    DentalSOLIDUSoral_projection = "snomedct:260477004"
    Body___molar = "snomedct:260478009"
    Body___premolar = "snomedct:260479001"
    Ramus_projection = "snomedct:260481004"
    Bimolar_projection = "snomedct:260482006"
    Transpharyngeal_projection = "snomedct:260483001"
    Transmaxillary_projection = "snomedct:260484007"
    Temporomandibular_joint_setting = "snomedct:260485008"
    Maxillary_sinus_setting = "snomedct:260486009"
    Dental_panoramic = "snomedct:260487000"
    Implant_setting_projection = "snomedct:260489002"
    Segmental_setting = "snomedct:260490006"
    Axial_view_for_sesamoid_bones = "snomedct:260491005"
    BrewertonAPOSTROPHEs_projection = "snomedct:260492003"
    Harris_Beath_axial_projection = "snomedct:260493008"
    Intercondylar_projection = "snomedct:260494002"
    Judet_projection = "snomedct:260496000"
    Mortice_projection = "snomedct:260497009"
    Occlusal_projection = "snomedct:260499007"
    Projected_oblique_occlusal = "snomedct:260500003"
    Lower_true_occlusal = "snomedct:260501004"
    Power_grip_series = "snomedct:260502006"
    Radial_head_projection = "snomedct:260503001"
    Skyline_projection = "snomedct:260504007"
    Van_Rosen_projection = "snomedct:260506009"
    Via_body_reference_line = "snomedct:260514003"
    Extracorporeal = "snomedct:260520002"
    Internal = "snomedct:260521003"
    Median = "snomedct:260528009"
    Vectors = "snomedct:260529001"
    Via_body_region = "snomedct:260530006"
    Thoracoabdominal = "snomedct:260532003"
    Lateral_extrapleural = "snomedct:260535001"
    Nasopancreatic = "snomedct:260541008"
    Endobronchial = "snomedct:260544000"
    Orogastric = "snomedct:260549005"
    Via_cardiovascular_system = "snomedct:260568008"
    Via_superficialized_vessel_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:260602004"
    Postaural_approach = "snomedct:260620008"
    Sublabial_transseptal = "snomedct:260637001"
    Extraperitoneal = "snomedct:260641002"
    Retroperitoneal = "snomedct:260642009"
    Venovenous = "snomedct:260668002"
    Anterior_dorsal = "snomedct:261045000"
    Aortocoronary = "snomedct:261052003"
    Arterio_arterial = "snomedct:261054002"
    Arteriovenous = "snomedct:261055001"
    Between_intestinal_loops = "snomedct:261057009"
    Bicoronal = "snomedct:261059007"
    Circumareolar = "snomedct:261065007"
    Dorsal_part = "snomedct:261067004"
    Epicardial = "snomedct:261073003"
    External = "snomedct:261074009"
    Extra_amniotic = "snomedct:261075005"
    Extracoronal = "snomedct:261076006"
    Inferior = "snomedct:261089000"
    Into_urinary_bladder = "snomedct:261094000"
    Into_ureter = "snomedct:261095004"
    Intracoronal = "snomedct:261097007"
    Intraperitoneal = "snomedct:261100002"
    Intravascular = "snomedct:261101003"
    Laryngotracheal = "snomedct:261117009"
    Lateral_part = "snomedct:261119007"
    Lower = "snomedct:261122009"
    Lower_anterior = "snomedct:261123004"
    Medial_part = "snomedct:261128008"
    Midaxillary = "snomedct:261131009"
    Midclavicular = "snomedct:261132002"
    Middle_third = "snomedct:261133007"
    Mural = "snomedct:261136004"
    Musculocutaneous = "snomedct:261137008"
    Para_aortic = "snomedct:261146002"
    Paracolic = "snomedct:261147006"
    Paraspinal = "snomedct:261148001"
    Parasternal = "snomedct:261149009"
    Penis_and_urinary_bladder_neck = "snomedct:261154000"
    Periadrenal = "snomedct:261156003"
    Posterior_dorsal = "snomedct:261165005"
    Proximal_third = "snomedct:261172006"
    Retrocecal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:261174007"
    Retroduodenal = "snomedct:261175008"
    Tracheobronchial = "snomedct:261181000"
    Upper = "snomedct:261183002"
    Upper_anterior = "snomedct:261184008"
    Venoarterial = "snomedct:261185009"
    Ventral_part = "snomedct:261186005"
    Distal_third = "snomedct:261411001"
    Transpulmonary_annulus = "snomedct:261446009"
    Via_intrapulmonary_trunk_tunnel = "snomedct:261466000"
    Via_orbitotomy = "snomedct:261469007"
    Deep_to_rectus_abdominis = "snomedct:261760007"
    Exteriorized_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:261788001"
    From_existing_graft_to_coronary_artery = "snomedct:261799004"
    Intracervical = "snomedct:261847009"
    Internally_to_bladder = "snomedct:261851006"
    Mixed_venoarterial_and_venovenous = "snomedct:261945002"
    Muscle_fibers_only_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:261964008"
    Neuromuscular_junction_only = "snomedct:261980003"
    Dominant_side = "snomedct:262379005"
    Non_dominant_side = "snomedct:262458006"
    Anocutaneous = "snomedct:263672002"
    Anovestibular = "snomedct:263674001"
    Foraminal = "snomedct:263759007"
    Left_side_by_side = "snomedct:263794000"
    Left_sided = "snomedct:263795004"
    Panacinar = "snomedct:263830001"
    Panlobular = "snomedct:263831002"
    Periacinar = "snomedct:263838008"
    Prevascular = "snomedct:263846009"
    Proximal_acinar = "snomedct:263848005"
    Separate = "snomedct:263869007"
    Subcutaneous = "snomedct:263887005"
    Above_middle_turbinate = "snomedct:263938007"
    Anterior_segment = "snomedct:263942005"
    Anterior_wall = "snomedct:263943000"
    Periorbital = "snomedct:263952009"
    Perioral = "snomedct:263953004"
    Atlantoaxial = "snomedct:263955006"
    Between_left_common_carotid_and_brachiocephalic_arteries = "snomedct:263958008"
    Between_left_subclavian_and_common_carotid_arteries = "snomedct:263959000"
    Bronchocutaneous = "snomedct:263965000"
    Bronchopleural = "snomedct:263966004"
    Centriacinar = "snomedct:263969006"
    Centrilobular = "snomedct:263970007"
    Cervicothoracic = "snomedct:263974003"
    Cervicothoracolumbar = "snomedct:263975002"
    Distal_to_left_subclavian_artery = "snomedct:263981005"
    Duodenoduodenal = "snomedct:263990003"
    Duodenojejunal = "snomedct:263991004"
    Extrafoveal = "snomedct:263996009"
    Extraureteric = "snomedct:263997000"
    Extravaginal = "snomedct:263998005"
    From_anterosuperior_superior_bridging_leaflet_commissure = "snomedct:263999002"
    From_left_inferior_bridging_leaflet_lateral_commissure = "snomedct:264000000"
    From_left_septal_commissure = "snomedct:264001001"
    From_left_superior_bridging_leaflet_lateral_commissure = "snomedct:264002008"
    From_left_ventricular_component = "snomedct:264004009"
    From_right_anterosuperior_inferior_commissure = "snomedct:264005005"
    From_right_inferior_bridging_leaflet_inferior_commissure = "snomedct:264006006"
    From_right_septal_commissure = "snomedct:264007002"
    From_right_ventricular_component = "snomedct:264008007"
    Gastroduodenal = "snomedct:264011008"
    Gastrogastric = "snomedct:264012001"
    Hepatopleural = "snomedct:264015004"
    Ileocecal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:264023002"
    Ileocolic = "snomedct:264024008"
    Iliofemoral_vein_zone = "snomedct:264025009"
    Ileo_ileal = "snomedct:264026005"
    Ileorectal = "snomedct:264027001"
    In_joint = "snomedct:264030008"
    In_situ = "snomedct:264031007"
    Infracardiac = "snomedct:264034004"
    Infravesical = "snomedct:264035003"
    Interchordal = "snomedct:264040006"
    Interdigital = "snomedct:264041005"
    Intervertebral = "snomedct:264042003"
    Intraligamentous = "snomedct:264043008"
    Intracardiac = "snomedct:264044002"
    Intraluminal = "snomedct:264045001"
    Intramammary = "snomedct:264046000"
    Intrapulmonary = "snomedct:264047009"
    Intravaginal = "snomedct:264049007"
    Lateral_column = "snomedct:264056001"
    Lateral_segment = "snomedct:264060003"
    Left_anterior = "snomedct:264065008"
    Left_lateral_wall = "snomedct:264067000"
    Left_lower_segment = "snomedct:264068005"
    Lower_left_parasternal = "snomedct:264076007"
    Lower_third = "snomedct:264081003"
    Lumbosacral = "snomedct:264083000"
    Medial_segment = "snomedct:264096004"
    Midtarsal = "snomedct:264103001"
    Paravertebral = "snomedct:264107000"
    Esophagocolonic_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:264110007"
    Esophagogastric_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:264111006"
    Esophagojejunal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:264112004"
    Ostium = "snomedct:264114003"
    Paraesophageal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:264117005"
    Paraduodenal = "snomedct:264118000"
    Parafoveal = "snomedct:264119008"
    Paramacular = "snomedct:264121003"
    Paraseptal = "snomedct:264123000"
    Paraumbilical = "snomedct:264124006"
    Paravascular = "snomedct:264126008"
    Paraovarian = "snomedct:264127004"
    Paratracheal = "snomedct:264128009"
    Peri_intestinal = "snomedct:264131005"
    Perianal = "snomedct:264133008"
    Perihepatic = "snomedct:264136000"
    Perinephric = "snomedct:264137009"
    Peripancreatic = "snomedct:264139007"
    Perisplenic = "snomedct:264142001"
    Posterior_pole = "snomedct:264153007"
    Posterior_segment = "snomedct:264154001"
    Posterior_wall = "snomedct:264159006"
    Rectocloacal = "snomedct:264168008"
    Rectocutaneous = "snomedct:264169000"
    Rectourethral = "snomedct:264170004"
    Rectovaginal = "snomedct:264171000"
    Rectovesical = "snomedct:264172007"
    Rectovulval = "snomedct:264173002"
    Retromammary = "snomedct:264174008"
    Retrocolumellar = "snomedct:264175009"
    Right_anterior = "snomedct:264176005"
    Right_lateral_wall = "snomedct:264178006"
    Right_side_by_side = "snomedct:264179003"
    Right_sided = "snomedct:264180000"
    Segment = "snomedct:264193005"
    Sternocostal = "snomedct:264201006"
    Subaortic = "snomedct:264202004"
    Subareolar = "snomedct:264205002"
    Subconjunctival = "snomedct:264206001"
    Subcostal = "snomedct:264208000"
    Subfoveal = "snomedct:264209008"
    Superficial_to_rectus_abdominis = "snomedct:264216009"
    Superior = "snomedct:264217000"
    Supraumbilical = "snomedct:264221007"
    Supracardiac = "snomedct:264222000"
    Supraglottic = "snomedct:264224004"
    Suprahepatic = "snomedct:264225003"
    Tarsometatarsal = "snomedct:264227006"
    Thoracolumbar = "snomedct:264232007"
    Upper_left_parasternal = "snomedct:264245006"
    Upper_third = "snomedct:264253003"
    Cholecystoduodenal = "snomedct:264261008"
    Cholecystenteric_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:264262001"
    Cholecystogastric = "snomedct:264263006"
    Choledochoduodenal = "snomedct:264264000"
    Colocolic = "snomedct:264266003"
    Colorectal = "snomedct:264267007"
    Epitrochlear = "snomedct:264463009"
    Under_inferior_bridging_leaflet = "snomedct:264940008"
    Under_superior_bridging_leaflet = "snomedct:264941007"
    Onlay = "snomedct:272288000"
    General_site_descriptor = "snomedct:272425003"
    Anatomical_part_descriptor = "snomedct:272427006"
    Anatomical_third = "snomedct:272428001"
    Part_structure = "snomedct:272429009"
    Column_structure = "snomedct:272430004"
    Segment_structure = "snomedct:272431000"
    Wall_structure = "snomedct:272432007"
    Anatomical_relationship_descriptor = "snomedct:272434008"
    Centri_location = "snomedct:272435009"
    Circum_location = "snomedct:272436005"
    Extra_location = "snomedct:272437001"
    Extrapleural = "snomedct:272438006"
    Infra_location = "snomedct:272439003"
    Inter_location = "snomedct:272440001"
    Intra_location = "snomedct:272441002"
    Mid_location = "snomedct:272442009"
    Pan_location = "snomedct:272443004"
    Para_location = "snomedct:272444005"
    Per_location = "snomedct:272446007"
    Peri_location = "snomedct:272447003"
    Post_location = "snomedct:272448008"
    Pre_location = "snomedct:272449000"
    Retro_location = "snomedct:272450000"
    Sub_location = "snomedct:272451001"
    Supra_location = "snomedct:272452008"
    Inferosuperior_projection = "snomedct:272455005"
    Apical_projection = "snomedct:272456006"
    Vertical_projection = "snomedct:272457002"
    Prone_projection = "snomedct:272458007"
    Supine_projection = "snomedct:272459004"
    Anterior_projection = "snomedct:272460009"
    Right_posterior_projection = "snomedct:272461008"
    Left_posterior_projection = "snomedct:272462001"
    Perorbital_projection = "snomedct:272464000"
    Temporomandibular_joint_projection = "snomedct:272465004"
    Optic_foramen_projection = "snomedct:272466003"
    Lateral_facial_skeleton_projection = "snomedct:272467007"
    Ear_projection = "snomedct:272468002"
    Mid_face_projection = "snomedct:272469005"
    Cervical_spine_projection = "snomedct:272470006"
    Macro_projection = "snomedct:272472003"
    Outlet_projection = "snomedct:272473008"
    SwimmerAPOSTROPHEs_projection = "snomedct:272474002"
    Tibial_tuberosity_projection = "snomedct:272475001"
    Transthoracic_projection = "snomedct:272476000"
    Transcranial_projection = "snomedct:272478004"
    Posteroanterior_projection = "snomedct:272479007"
    Horizontal_projection = "snomedct:272480005"
    Erect_projection = "snomedct:272481009"
    Adduction_projection = "snomedct:272482002"
    True_projection = "snomedct:272483007"
    Contralateral_projection = "snomedct:272484001"
    Clockface_position = "snomedct:272485000"
    Trans_direction = "snomedct:272486004"
    Into_structure = "snomedct:272487008"
    From_structure = "snomedct:272488003"
    Via_values = "snomedct:272489006"
    Via_incision = "snomedct:272496008"
    Epi_location = "snomedct:276749003"
    Overlapping_sites = "snomedct:276825009"
    Aortoiliac = "snomedct:276979001"
    Endo_location = "snomedct:277292000"
    Deep_locations = "snomedct:277407002"
    Superficial_locations = "snomedct:277409004"
    Anterior_locations = "snomedct:277410009"
    Posterior_locations = "snomedct:277411008"
    Proximal_locations = "snomedct:277412001"
    Distal_locations = "snomedct:277413006"
    Between_locations = "snomedct:277414000"
    Above_locations = "snomedct:277415004"
    Right_posterior = "snomedct:277593009"
    Left_posterior = "snomedct:277594003"
    Intrastomal = "snomedct:277681008"
    Tubo_ovarian = "snomedct:277685004"
    Peritubular = "snomedct:277686003"
    Sidedness = "snomedct:277806003"
    Limited_structures = "snomedct:278227002"
    Posterior_projection = "snomedct:278255003"
    Abduction_projection = "snomedct:278267001"
    Transorbital_projection = "snomedct:278318001"
    Periumbilical = "snomedct:278701003"
    Transumbilical = "snomedct:278702005"
    Subcuticular = "snomedct:285418008"
    Orthotopic = "snomedct:298107004"
    Heterotopic = "snomedct:298108009"
    Ectopic = "snomedct:298109001"
    Subfascial = "snomedct:303218009"
    Intracranial = "snomedct:303231004"
    Extracranial = "snomedct:303232006"
    Subcranial = "snomedct:303483009"
    Transannular = "snomedct:304047000"
    Endocardial = "snomedct:304059001"
    Low___site_descriptor = "snomedct:306766009"
    High___site_descriptor = "snomedct:306767000"
    Periapical = "snomedct:312206004"
    Caudal = "snomedct:3583002"
    Intracavitary = "snomedct:373863008"
    Collateral_branch_of_vessel = "snomedct:397406000"
    Vessel_origin = "snomedct:397421006"
    Intrauterine = "snomedct:398236008"
    Five_chamber_view = "snomedct:398994001"
    Leonard_George_projection = "snomedct:398996004"
    Right_ventricular_inflow_tract_view = "snomedct:398998003"
    Mayer_projection = "snomedct:399000008"
    Posterior_emissive_projection = "snomedct:399001007"
    Nolke_projection = "snomedct:399002000"
    Hughston_projection = "snomedct:399003005"
    Oblique_axial_projection = "snomedct:399004004"
    Miller_projection = "snomedct:399005003"
    Left_posterior_oblique_projection = "snomedct:399006002"
    Axillary_tail_mammography_view = "snomedct:399011000"
    Medial_lateral_emissive_projection = "snomedct:399012007"
    Chassard_Lapin_projection = "snomedct:399013002"
    Pirie_projection = "snomedct:399022001"
    May_projection = "snomedct:399024000"
    Ischerwood_projection = "snomedct:399025004"
    Zanelli_projection = "snomedct:399026003"
    Clements_projection = "snomedct:399028002"
    Frontal_projection = "snomedct:399033003"
    Parasternal_short_axis_view_at_the_mitral_valve_level = "snomedct:399036006"
    Lewis_projection = "snomedct:399037002"
    Right_posterior_oblique_projection = "snomedct:399038007"
    Cardiac_imaging_views = "snomedct:399043000"
    Postero_anterior_oblique_projection = "snomedct:399059000"
    Axial_projection = "snomedct:399061009"
    Causton_projection = "snomedct:399065000"
    Lateral_projection = "snomedct:399067008"
    Plantodorsal_projection = "snomedct:399071006"
    Fuchs_projection = "snomedct:399073009"
    Left_anterior_oblique_emissive_projection = "snomedct:399074003"
    Right_posterior_oblique_emissive_projection = "snomedct:399075002"
    Kuchendorf_projection = "snomedct:399080006"
    Gaynor_Hart_projection = "snomedct:399082003"
    Hsieh_projection = "snomedct:399083008"
    Oblique_axial_emissive_projection = "snomedct:399089007"
    Staunig_projection = "snomedct:399098005"
    Latero_medial_oblique_projection = "snomedct:399099002"
    Cranio_caudal_projection_exaggerated_medially = "snomedct:399101009"
    Friedman_projection = "snomedct:399103007"
    Suprasternal_long_axis_view = "snomedct:399106004"
    Right_anterior_oblique_emissive_projection = "snomedct:399108003"
    Tangential_projection = "snomedct:399110001"
    Eponymous_projection = "snomedct:399113004"
    Left_lateral_emissive_projection = "snomedct:399118008"
    Twining_projection = "snomedct:399125001"
    Teufel_projection = "snomedct:399127009"
    Holly_projection = "snomedct:399129007"
    West_Point_projection = "snomedct:399130002"
    Frontal_oblique_axial_projection = "snomedct:399132005"
    Left_anterior_oblique_projection = "snomedct:399135007"
    Left_posterior_oblique_emissive_projection = "snomedct:399136008"
    Penner_projection = "snomedct:399138009"
    Parasternal_long_axis_view = "snomedct:399139001"
    Albers_Schönberg_projection = "snomedct:399142007"
    Suprasternal_short_axis_view = "snomedct:399145009"
    Grashey_projection = "snomedct:399146005"
    Chamberlain_projection = "snomedct:399148006"
    Kandel_projection = "snomedct:399152006"
    Laquerriere_Pierquin_projection = "snomedct:399156009"
    NorgaardAPOSTROPHEs_projection = "snomedct:399157000"
    Latero_medial_oblique_emissive_projection = "snomedct:399159002"
    Frontal_oblique_projection = "snomedct:399160007"
    Cleavage_mammography_view = "snomedct:399161006"
    Cranio_caudal_projection = "snomedct:399162004"
    Magnified_projection = "snomedct:399163009"
    Hough_projection = "snomedct:399168000"
    Lauenstein_projection = "snomedct:399169008"
    Ottonello_projection = "snomedct:399171008"
    Left_lateral_projection = "snomedct:399173006"
    Lawrence_projection = "snomedct:399179005"
    Pawlow_projection = "snomedct:399181007"
    Oblique_projection = "snomedct:399182000"
    Left_oblique_projection = "snomedct:399184004"
    Superolateral_to_inferomedial_oblique_projection = "snomedct:399188001"
    Cranio_caudal_projection_exaggerated_laterally = "snomedct:399192008"
    Right_ventricular_outflow_tract_view = "snomedct:399195005"
    Caudo_cranial_projection = "snomedct:399196006"
    Right_lateral_projection = "snomedct:399198007"
    Henschen_projection = "snomedct:399199004"
    Subcostal_short_axis_view = "snomedct:399200001"
    Judd_projection = "snomedct:399201002"
    Law_projection = "snomedct:399206007"
    Camp_Coventry_projection = "snomedct:399212002"
    Apical_four_chamber_view = "snomedct:399214001"
    Wigby_Taylor_projection = "snomedct:399215000"
    Arcelin_projection = "snomedct:399218003"
    Oblique_caudo_cranial_projection = "snomedct:399225005"
    Kemp_Harper_projection = "snomedct:399227002"
    Apical_two_chamber_view = "snomedct:399232001"
    Rhese_projection = "snomedct:399234000"
    Right_oblique_projection = "snomedct:399236003"
    Alexander_projection = "snomedct:399237007"
    Parasternal_short_axis_view_at_the_aortic_valve_level = "snomedct:399239005"
    Titterington_projection = "snomedct:399241006"
    Acanthioparietal_projection = "snomedct:399242004"
    Settegast_projection = "snomedct:399243009"
    Cleaves_projection = "snomedct:399245002"
    Blackett_Healy_projection = "snomedct:399246001"
    Tarrant_projection = "snomedct:399247005"
    Lorenz_projection = "snomedct:399251007"
    Submentovertical_projection = "snomedct:399255003"
    Mediolateral_projection = "snomedct:399260004"
    Beclere_projection = "snomedct:399263002"
    Exaggerated_cranio_caudal_projection = "snomedct:399265009"
    Medio_lateral_oblique_emissive_projection = "snomedct:399268006"
    TowneAPOSTROPHEs_projection = "snomedct:399270002"
    Parasternal_short_axis_view_at_the_papillary_muscle_level = "snomedct:399271003"
    Parietoacanthial_projection = "snomedct:399272005"
    Sagittal_oblique_axial_emissive_projection = "snomedct:399273000"
    Hickey_projection = "snomedct:399277004"
    Cahoon_projection = "snomedct:399278009"
    Kasabach_projection = "snomedct:399280003"
    Fleischner_projection = "snomedct:399281004"
    Merchant_projection = "snomedct:399284007"
    Holmblad_projection = "snomedct:399285008"
    Oblique_cranio_caudal_projection = "snomedct:399288005"
    Schüller_projection = "snomedct:399290006"
    Stecher_projection = "snomedct:399292003"
    Taylor_projection = "snomedct:399296000"
    Right_lateral_emissive_projection = "snomedct:399297009"
    Lateral_medial_emissive_projection = "snomedct:399300004"
    Dunlap_projection = "snomedct:399303002"
    Parasternal_short_axis_view = "snomedct:399306005"
    Lindblom_projection = "snomedct:399308006"
    Subcostal_long_axis_view = "snomedct:399310008"
    Grandy_projection = "snomedct:399311007"
    Antero_posterior_oblique_projection = "snomedct:399312000"
    Swanson_projection = "snomedct:399313005"
    Parieto_orbital_projection = "snomedct:399316002"
    Kovacs_projection = "snomedct:399318001"
    Clements_Nakayama_projection = "snomedct:399320003"
    Anterior_emissive_projection = "snomedct:399321004"
    Sagittal_oblique_axial_projection = "snomedct:399325008"
    Low_Beer_projection = "snomedct:399327000"
    Valdini_projection = "snomedct:399330007"
    Kurzbauer_projection = "snomedct:399332004"
    Dorsoplantar_projection = "snomedct:399335002"
    Apical_long_axis = "snomedct:399339008"
    Haas_projection = "snomedct:399341009"
    Lilienfeld_projection = "snomedct:399342002"
    Broden_projection = "snomedct:399344001"
    Antero_posterior_projection = "snomedct:399348003"
    StenverAPOSTROPHEs_projection = "snomedct:399349006"
    Orbito_parietal_projection = "snomedct:399351005"
    Lateral_medial_projection = "snomedct:399352003"
    Chausse_projection = "snomedct:399355001"
    Right_anterior_oblique_projection = "snomedct:399356000"
    Caldwell_projection = "snomedct:399358004"
    Verticosubmental_projection = "snomedct:399360002"
    Nuclear_medicine_projection = "snomedct:399361003"
    Bertel_projection = "snomedct:399362005"
    Pearson_projection = "snomedct:399365007"
    Medio_lateral_oblique_projection = "snomedct:399368009"
    Lysholm_projection = "snomedct:399370000"
    Parasternal_short_axis_view_at_the_level_of_the_mitral_chords = "snomedct:399371001"
    Ferguson_projection = "snomedct:399372008"
    Midline = "snomedct:399488007"
    Cranial_LAO = "snomedct:408723005"
    Caudal_LAO = "snomedct:408724004"
    Cranial_RAO = "snomedct:408725003"
    Caudal_RAO = "snomedct:408726002"
    Bottom = "snomedct:421610009"
    Top = "snomedct:421812003"
    Rafert_Long_projection = "snomedct:422534007"
    Moore_projection = "snomedct:422568001"
    Apple_projection = "snomedct:422670003"
    Neer_projection = "snomedct:422795009"
    Burman_projection = "snomedct:422861003"
    Stryker_projection = "snomedct:422954003"
    Wolf_projection = "snomedct:422996004"
    Colcher_Sussman_projection = "snomedct:423091003"
    Rafer_projection = "snomedct:423720000"
    Hirtz_Modification_projection = "snomedct:424086005"
    Eraso_Modification_projection = "snomedct:424655003"
    Danelius_Miller_projection = "snomedct:424811006"
    Fisk_projection = "snomedct:424962005"
    Kite_projection = "snomedct:425030002"
    Robert_projection = "snomedct:425035007"
    Rosenberg_projection = "snomedct:425042007"
    Folio_projection = "snomedct:425157002"
    Garth_projection = "snomedct:425188003"
    Dorsopalmar_projection = "snomedct:441505008"
    Inferomedial_to_superolateral_oblique_view = "snomedct:441555000"
    Dorso_ventral_projection = "snomedct:441672003"
    Mammography_view = "snomedct:441753009"
    Stereoscopic_view = "snomedct:442361004"
    Ventro_dorsal_projection = "snomedct:442441009"
    Axillary_tissue_mammography_view = "snomedct:442580003"
    Nipple_in_profile_mammography_view = "snomedct:442581004"
    Infra_mammary_fold_mammography_view = "snomedct:442593008"
    Right_stereoscopic_view = "snomedct:442594002"
    Left_stereoscopic_view = "snomedct:442640004"
    Stereoscopic_view_incremented_from_baseline = "snomedct:442653001"
    Stereoscopic_view_decremented_from_baseline = "snomedct:442667005"
    Parasternal_long_axis_view_of_right_ventricular_inflow_tract = "snomedct:443082005"
    Parasternal_long_axis_view_of_right_ventricular_outflow_tract = "snomedct:443083000"
    Subcostal_view_of_cardiac_outlets_directed_anteriorly = "snomedct:443100003"
    Subcostal_short_axis_view_at_papillary_muscle_level = "snomedct:443160001"
    Suprasternal_coronal_view = "snomedct:443162009"
    Suprasternal_sagittal_view = "snomedct:443163004"
    Transgastric_short_axis_view = "snomedct:443293000"
    Intramedullary = "snomedct:443459002"
    Subcostal_short_axis_view_at_mitral_valve_level = "snomedct:443499004"
    Subcostal_short_axis_view_at_venous_inflow_level = "snomedct:443500008"
    Suprasternal_long_axis_view_of_aortic_arch = "snomedct:443562002"
    Subcostal_short_axis_view_at_aortic_valve_level = "snomedct:443609003"
    Subcostal_oblique_coronal_view = "snomedct:443640005"
    Transesophageal_four_chamber_view_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:443662005"
    Transesophageal_short_axis_view_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "snomedct:443698002"
    Contiguous = "snomedct:65424008"
    Unilateral = "snomedct:66459002"
    Common = "snomedct:72906007"
    Dorsoventral = "snomedct:741000124103"
    Dorsolateral = "snomedct:761000124104"
    Ventrolateral = "snomedct:771000124106"
    Palmar = "snomedct:781000124109"


class EnumStudyDesign(str, Enum):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    Cross_Sectional_Studies = "mesh:D003430"
    """
    Studies in which the presence or absence of disease or other health-related variables are determined in each member of the study population or in a representative sample at one particular time. This contrasts with LONGITUDINAL STUDIES which are followed over a period of time.
    """
    Follow_Up_Studies = "mesh:D005500"
    """
    Studies in which individuals or populations are followed to assess the outcome of exposures, procedures, or effects of a characteristic, e.g., occurrence of disease.
    """
    Longitudinal_Studies = "mesh:D008137"
    """
    Studies in which variables relating to an individual or group of individuals are assessed over a period of time.
    """
    Prospective_Studies = "mesh:D011446"
    """
    Observation of a population for a sufficient number of persons over a sufficient number of years to generate incidence or mortality rates subsequent to the selection of the study group.
    """
    Retrospective_Studies = "mesh:D012189"
    """
    Studies used to test etiologic hypotheses in which inferences about an exposure to putative causal factors are derived from data relating to characteristics of persons under study or to events or experiences in their past. The essential feature is that some of the persons under study have the disease or outcome of interest and their characteristics are compared with those of unaffected persons.
    """
    Cohort_Studies = "mesh:D015331"
    """
    Studies in which subsets of a defined population are identified. These groups may or may not be exposed to factors hypothesized to influence the probability of the occurrence of a particular disease or other outcome. Cohorts are defined populations which, as a whole, are followed in an attempt to determine distinguishing subgroup characteristics.
    """
    HIV_Seroprevalence = "mesh:D015528"
    """
    Studies of the number of cases where human immunodeficiency virus (HIV) is present in a specific population at a designated time. The presence in a given individual is determined by the finding of HIV antibodies in the serum (HIV SEROPOSITIVITY).
    """
    Case_Control_Studies = "mesh:D016022"
    """
    Comparisons that start with the identification of persons with the disease or outcome of interest and a control (comparison, referent) group without the disease or outcome of interest. The relationship of an attribute is examined by comparing both groups with regard to the frequency or levels of outcome over time.
    """
    Seroepidemiologic_Studies = "mesh:D016036"
    """
    EPIDEMIOLOGIC STUDIES based on the detection through serological testing of characteristic change in the serum level of specific ANTIBODIES. Latent subclinical infections and carrier states can thus be detected in addition to clinically overt cases.
    """
    National_Longitudinal_Study_of_Adolescent_Health = "mesh:D063588"
    """
    Longitudinal study of a nationally representative sample of adolescents in grades 7-12 in the United States during the 1994-95 school year. The Add Health cohort has been followed into young adulthood. (from http://www.cpc.unc.edu/projects/addhealth accessed 08/2012)
    """
    Interrupted_Time_Series_Analysis = "mesh:D065186"
    """
    A study that uses observations at multiple time points before and after an intervention (the interruption), in an attempt to detect whether the intervention has had an effect significantly greater than any underlying trend over time.
    """
    Controlled_Before_After_Studies = "mesh:D065187"
    """
    A study in which observations are made before and after an intervention, both in a group that receives the intervention and in a control group that does not.
    """
    Historically_Controlled_Study = "mesh:D065386"
    """
    A study that compares a group of participants receiving an intervention with a similar group from the past who did not.
    """
    Clinical_Study = "mesh:D000068397"
    """
    A work that reports on the results of a research study to evaluate interventions or exposures on biomedical or health-related outcomes.  The two main types of clinical studies are interventional studies (clinical trials) and observational studies. While most clinical studies concern humans, this publication type may be used for clinical veterinary articles meeting the requisites for humans.
    """
    Equivalence_Trial = "mesh:D000073843"
    """
    Trial that aims to show a new treatment is no better and no worse than the standard treatment.
    """
    Adaptive_Clinical_Trial = "mesh:D000076362"
    """
    Clinical study in which a prospectively planned opportunity is included to modify trial designs and hypotheses based on analysis of data from subjects in the study.
    """
    Clinical_Trial_Veterinary = "mesh:D000077522"
    """
    A work in which animal participants are assigned to receive one or more interventions so that researchers can evaluate the interventions on biomedical or health-related outcomes. The assignments are determined by the study protocol.
    """
    Systematic_Review = "mesh:D000078182"
    """
    A review of primary literature in health and health policy that attempts to identify, appraise, and synthesize all the empirical evidence that meets specified eligibility criteria to answer a given research question.  Its conduct uses explicit methods aimed at minimizing bias in order to produce more reliable findings regarding the effects of interventions for prevention, treatment, and rehabilitation that can be used to inform decision making.
    """
    Observational_Study_Veterinary = "mesh:D000078323"
    """
    Reports on studies of the results of a clinical study in which animal subjects may receive diagnostic, therapeutic, or other types of interventions, where the investigator does not assign participants to specific interventions.
    """
    Clinical_Trial_Protocol = "mesh:D000078325"
    """
    The written description of a clinical study. It contains the study's objectives, design, and methods including subject target and/or enrollment criteria. It may also present relevant scientific background and statistical information.
    """
    Randomized_Controlled_Trial_Veterinary = "mesh:D000081262"
    """
    A work that reports on a clinical trial with animal subjects that involves at least one test treatment and one control treatment, concurrent enrollment and follow-up of the test- and control-treated groups, and in which the treatments to be administered are selected by a random process, such as the use of a random-numbers table.
    """
    Human_Challenge_Trials = "mesh:D000098368"
    """
    Trials in which participants are intentionally challenged (whether or not they have been vaccinated) with exposure to an infectious disease organism.
    """
    Scoping_Review = "mesh:D000098583"
    """
    Review to identify knowledge gaps, scope a body of literature, clarify concepts or to investigate research conduct.
    """
    Network_Meta_Analysis = "mesh:D000099094"
    """
    Works consisting of meta-analysis of randomized trials in which estimates of comparative treatment effects are visualized and interpreted from a network of interventions that may or may not have been evaluated directly against each other. Common considerations in network meta-analysis include conceptual and statistical heterogeneity and incoherence.
    """
    Case_Reports = "mesh:D002363"
    """
    Clinical presentations that may be followed by evaluative studies that eventually lead to a diagnosis.
    """
    Comparative_Study = "mesh:D003160"
    """
    Comparison of outcomes, results, responses, etc for different techniques, therapeutic approaches or other inputs.
    """
    Scientific_Integrity_Review = "mesh:D016426"
    """
    Work consisting of reports by the United States Office of Research Integrity, identifying questionable research published in articles or books. Notification of the questionable data is carried in the NIH Guide for Grants and Contracts.
    """
    Clinical_Conference = "mesh:D016429"
    """
    Work that consists of a conference of physicians on their observations of a patient at the bedside, regarding the physical state, laboratory and other diagnostic findings, clinical manifestations, results of current therapy, etc. A clinical conference usually ends with a confirmation or correction of clinical findings by a pathological diagnosis performed by a pathologist. Clinical conference is often referred to as a clinico-pathological conference.
    """
    Clinical_Trial = "mesh:D016430"
    """
    A work that reports on the results of a clinical study in which participants are assigned to receive one or more interventions so that researchers can evaluate the interventions on biomedical or health-related outcomes. The assignments are determined by the study protocol. Participants may receive diagnostic, therapeutic, or other types of interventions. For clinical trials on  veterinary animals see CLINICAL TRIAL, VETERINARY. Clinical Trials was used for both humans and non-humans prior to 2019.
    """
    Consensus_Development_Conference = "mesh:D016446"
    """
    Official statements of the findings or recommendations expressing the outcome of a meeting convened to evaluate current thought and research on a subject of interest.
    """
    Consensus_Development_Conference_NIH = "mesh:D016447"
    """
    Official statements of the finding or recommendations expressing the outcome from a conference sponsored by NIH.
    """
    Multicenter_Study = "mesh:D016448"
    """
    A work that reports on a study executed by several cooperating institutions.
    """
    Randomized_Controlled_Trial = "mesh:D016449"
    """
    A work that reports on a clinical trial that involves at least one test treatment and one control treatment, concurrent enrollment and follow-up of the test- and control-treated groups, and in which the treatments to be administered are selected by a random process, such as the use of a random-numbers table.
    """
    Meta_Analysis = "mesh:D017418"
    """
    Works consisting of studies using a quantitative method of combining the results of independent studies (usually drawn from the published literature) and synthesizing summaries and conclusions which may be used to evaluate therapeutic effectiveness, plan new studies, etc. It is often an overview of clinical trials. It is usually called a meta-analysis by the author or sponsoring body and should be differentiated from reviews of literature.
    """
    Clinical_Trial_Phase_I = "mesh:D017426"
    """
    Work that is the report of a pre-planned, usually controlled, clinical study of the safety and efficacy of diagnostic, therapeutic, or prophylactic drugs, devices, or techniques based on a small number of healthy persons and conducted over the period of about a year in either the United States or a foreign country.
    """
    Clinical_Trial_Phase_II = "mesh:D017427"
    """
    Work that is a report of a pre-planned, usually controlled, clinical study of the safety and efficacy of diagnostic, therapeutic, or prophylactic drugs, devices, or techniques based on several hundred volunteers, including a limited number of patients, and conducted over a period of about two years in either the United States or a foreign country.
    """
    Clinical_Trial_Phase_III = "mesh:D017428"
    """
    Work that is a report of a pre-planned, usually controlled, clinical study of the safety and efficacy of diagnostic, therapeutic, or prophylactic drugs, devices, or techniques after phase II trials. A large enough group of patients is studied and closely monitored by physicians for adverse response to long-term exposure, over a period of about three years in either the United States or a foreign country.
    """
    Clinical_Trial_Phase_IV = "mesh:D017429"
    """
    Work that is a report of a planned post-marketing study of diagnostic, therapeutic, or prophylactic drugs, devices, or techniques that have been approved for general sale after clinical trials, phases I, II, and III. These studies, conducted in the United States or a foreign country, often garner additional data about the safety and efficacy of a product.
    """
    Twin_Study = "mesh:D018486"
    """
    Work consisting of reporting using a method of detecting genetic causes in human traits and genetic factors in behavior using sets of twins.
    """
    Controlled_Clinical_Trial = "mesh:D018848"
    """
    A work that reports on a clinical trial involving one or more test treatments, at least one control treatment, specified outcome measures for evaluating the studied intervention, and a bias-free method for assigning patients to the test treatment. The treatment may be drugs, devices, or procedures studied for diagnostic, therapeutic, or prophylactic effectiveness. Control measures include placebos, active medicine, no-treatment, dosage forms and regimens, historical comparisons, etc. When randomization using mathematical techniques, such as the use of a random numbers table, is employed to assign patients to test or control treatments, the trial is characterized as a RANDOMIZED CONTROLLED TRIAL.
    """
    Validation_Study = "mesh:D023361"
    """
    Works consisting of research using processes by which the reliability and relevance of a procedure for a specific purpose are established.
    """
    Evaluation_Study = "mesh:D023362"
    """
    Works consisting of studies determining the effectiveness or utility of processes, personnel, and equipment.
    """
    Observational_Study = "mesh:D064888"
    """
    A work that reports on the results of a clinical study in which participants may receive diagnostic, therapeutic, or other types of interventions, but the investigator does not assign participants to specific interventions (as in an interventional study).
    """
    Pragmatic_Clinical_Trial = "mesh:D065007"
    """
    Randomized clinical trials that compare interventions in clinical settings and which look at a range of effectiveness outcomes and impacts.
    """


class EnumSubjectType(str, Enum):
    """
    Types of Subject entities
    """
    Participant = "CAMO:0000024"
    """
    Study participant with consent, assent, or waiver of consent.
    """
    Non_Participant = "CAMO:0000025"
    """
    An individual not directly participating in a study, eg, the subject of a reported family history.
    """
    Cell_Line = "CAMO:0000026"
    Animal_Model = "CAMO:0000027"
    Group = "CAMO:0000028"
    """
    A group of entities or things being assessed as a whole.
    """


class EnumUnknown(str, Enum):
    """
    Base enumeration providing an Unknown option.
    """
    Unknown = "snomedct:261665006"


class EnumUnknownOther(str, Enum):
    """
    Base enumeration providing Unknown and Other options.
    """
    Unknown = "snomedct:261665006"
    Other = "snomedct:74964007"


class EnumVitalStatus(str, Enum):
    """
    Descriptions of a Subject's vital status
    """
    Dead = "snomedct:419099009"
    Alive = "snomedct:438949009"



class Record(ConfiguredBaseModel):
    """
    One row / entity within the database
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://includedcc.org/common-access-model',
         'title': 'Record'})

    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class AccessPolicy(ConfiguredBaseModel):
    """
    The access policy that describes the controls around use of data
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'slot_usage': {'access_policy_id': {'identifier': True,
                                             'name': 'access_policy_id',
                                             'range': 'coGlobalID',
                                             'required': True}},
         'title': 'Access Policy'})

    access_policy_id: str = Field(default=..., title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    data_use_accession: Optional[str] = Field(default=None, title="Data Use Accession", description="""Accession used to provision access to the record, eg, a dbGaP phsID.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    data_use_permission: EnumDataUsePermission = Field(default=..., title="Data Use Permission", description="""Broad category of restrictions on data use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    data_use_modifier: Optional[EnumDataUseModifier] = Field(default=None, title="Data Use Modifier", description="""Additional modifiers that limit data use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    disease_limitation: Optional[str] = Field(default=None, title="Data Use Disease Limitation", description="""If the access is limited to a specific disease purpose, it is specified here.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    access_description: Optional[str] = Field(default=None, title="Access Description", description="""Any additional information to support access requests.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website with more information about this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'Study', 'VirtualBiorepository', 'Publication']} })


class Study(Record):
    """
    Study Metadata
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'study_id': {'identifier': True,
                                     'name': 'study_id',
                                     'range': 'sdGlobalID',
                                     'required': True}},
         'title': 'Research Study'})

    parent_study: Optional[str] = Field(default=None, title="Parent Study", description="""The parent study for this study, if it is a nested study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_title: str = Field(default=..., description="""Full Study Title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_code: str = Field(default=..., title="Study Code", description="""Unique identifier for the study (generally a short acronym)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    study_short_name: Optional[str] = Field(default=None, title="Study Code", description="""Short name for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    program: list[Union[EnumProgram, str]] = Field(default=..., title="Program", description="""Funding source(s) for the study""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'uriorcurie'}, {'range': 'EnumProgram'}],
         'domain_of': ['Study']} })
    funding_source: Optional[list[str]] = Field(default=None, title="Funding Source", description="""The funding source(s) of the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    principal_investigator: list[Investigator] = Field(default=..., title="Principal Investigator", description="""The Principal Investigator(s) responsible for the study.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    contact: list[Investigator] = Field(default=..., title="Contact Person", description="""The individual to contact with questions about this record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository']} })
    study_description: str = Field(default=..., title="Study Description", description="""Brief description of the study (2-4 sentences)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website with more information about this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'Study', 'VirtualBiorepository', 'Publication']} })
    publication: Optional[list[Publication]] = Field(default=None, title="Publication", description="""Publications associated with this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'Dataset']} })
    acknowledgments: Optional[str] = Field(default=None, title="Acknowledgments", description="""Funding statement and acknowledgments for this study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    citation_statement: Optional[str] = Field(default=None, title="Citation Statement", description="""Statement that secondary data users should use to acknowledge use of this study or dataset. E.g., \"The results analyzed and <published or shown> here are based in whole or in part upon data generated by the INCLUDE (INvestigation of Co-occurring conditions across the Lifespan to Understand Down syndromeE) Project <insert accession number(s) and/or study DOI(s)>, and were accessed from the INCLUDE Data Hub and <insert other database(s)>.\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study']} })
    do_id: Optional[str] = Field(default=None, title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI', 'Dataset']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class StudyMetadata(Record):
    """
    Additional features about studies that may not apply to all studies
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'data_category': {'multivalued': True,
                                          'name': 'data_category',
                                          'required': True},
                        'study_id': {'identifier': True,
                                     'name': 'study_id',
                                     'required': True}},
         'title': 'Study Metadata'})

    study_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })
    participant_lifespan_stage: list[EnumParticipantLifespanStage] = Field(default=..., title="Participant Lifespan Stage", description="""Focus age group(s) of the study population""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    selection_criteria: Optional[str] = Field(default=None, title="Selection Criteria", description="""Brief description of inclusion and/or exclusion criteria for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    study_design: list[Union[EnumStudyDesign, str]] = Field(default=..., title="Study Design", description="""Overall design of study, including whether it is longitudinal and whether family members/unrelated controls are also enrolled""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumStudyDesign'}],
         'domain_of': ['StudyMetadata']} })
    clinical_data_source_type: list[EnumDataSourceType] = Field(default=..., title="Clinical Data Source Type", description="""Source(s) of data collected from study participants""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    data_category: list[Union[EnumDataCategory, str]] = Field(default=..., title="Data Category", description="""General category of data in this Record (e.g. Clinical, Genomics, etc)""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumDataCategory'}],
         'domain_of': ['StudyMetadata', 'File']} })
    vbr_id: Optional[str] = Field(default=None, title="Virtual Biorepository", description="""Information about the study's Virtual Biorepository, if participating""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata', 'VirtualBiorepository']} })
    research_domain: list[Union[EnumResearchDomain, str]] = Field(default=..., description="""Main research domain(s) of the study""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumResearchDomain'}],
         'domain_of': ['StudyMetadata']} })
    expected_number_of_participants: int = Field(default=..., title="Expected Number of Participants", description="""Total expected number of participants to be recruited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    actual_number_of_participants: int = Field(default=..., title="Actual Number of Participants", description="""Total participants included at this time.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })


class VirtualBiorepository(Record):
    """
    An organization that can provide access to specimen for further analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'vbr_id': {'identifier': True,
                                   'name': 'vbr_id',
                                   'range': 'orGlobalID',
                                   'required': True}},
         'title': 'Virtual BioRepository (VBR)'})

    vbr_id: str = Field(default=..., title="Virtual Biorepository", description="""Information about the study's Virtual Biorepository, if participating""", json_schema_extra = { "linkml_meta": {'domain_of': ['StudyMetadata', 'VirtualBiorepository']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    institution: Optional[str] = Field(default=None, title="Institution", description="""Name of the institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository', 'Investigator']} })
    contact: list[Investigator] = Field(default=..., title="Contact Person", description="""The individual to contact with questions about this record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'VirtualBiorepository']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website with more information about this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'Study', 'VirtualBiorepository', 'Publication']} })
    vbr_readme: Optional[str] = Field(default=None, title="VBR Readme", description="""Instructions for contacting or requesting samples from Virtual Biorepository, if participating""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class DOI(Record):
    """
    A DOI is a permanent reference with metadata about a digital object.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'do_id': {'identifier': True,
                                  'name': 'do_id',
                                  'range': 'string',
                                  'required': True}},
         'title': 'Digital Object Identifier (DOI)'})

    do_id: str = Field(default=..., title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI', 'Dataset']} })
    bibliographic_reference: Optional[str] = Field(default=None, title="Bibiliographic Reference", description="""Text use to reference this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DOI', 'Publication']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Investigator(Record):
    """
    An individual who made contributions to the collection, analysis, or sharing of data.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'title': 'Investigator'})

    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    institution: Optional[str] = Field(default=None, title="Institution", description="""Name of the institution this record is associated with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository', 'Investigator']} })
    investigator_title: Optional[str] = Field(default=None, title="Investigator Title", description="""The title of the Investigator, eg, \"Assistant Professor\"""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigator']} })
    email: Optional[str] = Field(default=None, title="Email Address", description="""An email address to reach the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Investigator']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Publication(Record):
    """
    Information about a specific publication.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'title': 'Publication'})

    bibliographic_reference: Optional[str] = Field(default=None, title="Bibiliographic Reference", description="""Text use to reference this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['DOI', 'Publication']} })
    website: Optional[str] = Field(default=None, title="Website", description="""Website with more information about this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AccessPolicy', 'Study', 'VirtualBiorepository', 'Publication']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Subject(Record):
    """
    This entity is the subject about which data or references are recorded. This includes the idea of a human participant in a study, a cell line, an animal model, or any other similar entity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'subject_id': {'identifier': True,
                                       'name': 'subject_id',
                                       'range': 'ptGlobalID',
                                       'required': True}},
         'title': 'Subject'})

    subject_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    subject_type: Union[EnumSubjectType, EnumUnknownOther] = Field(default=..., title="Subject Type", description="""Type of entity this record represents""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'EnumSubjectType'}, {'range': 'EnumUnknownOther'}],
         'domain_of': ['Subject']} })
    organism_type: Optional[Union[EnumOrganism, str]] = Field(default=None, title="Organism Type", description="""Organism Type, typically from NCBITaxon.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'uriorcurie'}, {'range': 'EnumOrganism'}],
         'domain_of': ['Subject']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Demographics(Record):
    """
    Basic participant demographics summary
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'subject_id': {'identifier': True,
                                       'name': 'subject_id',
                                       'required': True}},
         'title': 'Demographics'})

    subject_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    sex: Union[EnumSex, EnumUnknownOther] = Field(default=..., title="Sex", description="""Sex of Participant""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'EnumSex'}, {'range': 'EnumUnknownOther'}],
         'domain_of': ['Demographics']} })
    race: list[Union[EnumRace, EnumUnknownOther]] = Field(default=..., title="Race", description="""Race of Participant""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'EnumRace'}, {'range': 'EnumUnknownOther'}],
         'domain_of': ['Demographics']} })
    ethnicity: Union[EnumEthnicity, EnumUnknownOther] = Field(default=..., title="Ethnicity", description="""Ethnicity of Participant""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'EnumEthnicity'}, {'range': 'EnumUnknownOther'}],
         'domain_of': ['Demographics']} })
    age_at_last_vital_status: Optional[int] = Field(default=None, title="Age at Last Vital Status", description="""Age in days when participant's vital status was last recorded""", ge=-365, le=32507, json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics'], 'unit': {'ucum_code': 'd'}} })
    vital_status: Optional[Union[EnumUnknown, EnumVitalStatus]] = Field(default=None, title="Vital Status", description="""Whether participant is alive or dead""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'EnumVitalStatus'}, {'range': 'EnumUnknown'}],
         'domain_of': ['Demographics']} })
    age_at_first_engagement: Optional[int] = Field(default=None, title="Age at First Participant Engagement", description="""Age in days of Participant at first recorded study event (enrollment, visit, observation, sample collection, survey completion, etc.). Age at enrollment is preferred, if available.""", ge=-365, le=32507, json_schema_extra = { "linkml_meta": {'domain_of': ['Demographics'], 'unit': {'ucum_code': 'd'}} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Family(Record):
    """
    A group of individuals of some relation who are grouped together in a study.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'family_id': {'identifier': True,
                                      'name': 'family_id',
                                      'range': 'grGlobalID',
                                      'required': True}},
         'title': 'Family'})

    family_id: str = Field(default=..., title="Family ID", description="""Global ID for the Family""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family', 'FamilyMembership']} })
    family_type: Optional[EnumFamilyType] = Field(default=None, description="""Describes the 'type' of study family, eg, trio.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    family_description: Optional[str] = Field(default=None, description="""Free text describing the study family, such as potential inheritance or details about consanguinity""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    consanguinity: Optional[EnumPresentAbsent] = Field(default=None, description="""Is there known or suspected consanguinity in this study family?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    family_study_focus: Optional[str] = Field(default=None, description="""The specific focus of the investigation, eg, a condition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class FamilyRelationship(Record):
    """
    A relationship between two Subjects. Directed as follows <family_member_id> <relationship> <subject_id> <Mother's id> <KIN:027 \"isBiologicalMotherOf\"> <subject_id>
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'family_relationship_id': {'identifier': True,
                                                   'name': 'family_relationship_id',
                                                   'range': 'fmGlobalID',
                                                   'required': True},
                        'subject_id': {'description': 'The family member Subject who '
                                                      'is the relationship "object".',
                                       'name': 'subject_id',
                                       'required': True}},
         'title': 'Family Member Relationship'})

    family_relationship_id: str = Field(default=..., title="Family Relationship ID", description="""Global ID for the Family Relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyRelationship']} })
    family_member_id: str = Field(default=..., description="""The family member Subject who is the relationship \"subject\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyRelationship']} })
    relation: Union[EnumFamilyRelation, EnumUnknown] = Field(default=..., description="""Code definting the relationship predicate. Relationship of the \"Family Member\" to the \"Subject\", eg, mother of. Ideally uses KIN ontology.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'EnumFamilyRelation'}, {'range': 'EnumUnknown'}],
         'domain_of': ['FamilyRelationship']} })
    subject_id: str = Field(default=..., title="Study ID", description="""The family member Subject who is the relationship \"object\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class FamilyMembership(Record):
    """
    Designates a Subject as a member of a family with a specified role.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'family_id': {'name': 'family_id', 'required': True},
                        'family_membership_id': {'identifier': True,
                                                 'name': 'family_membership_id',
                                                 'range': 'string',
                                                 'required': True},
                        'subject_id': {'name': 'subject_id', 'required': True}},
         'title': 'Family Membership'})

    family_membership_id: str = Field(default=..., title="Family Relationship ID", description="""ID for the Family Relationship""", json_schema_extra = { "linkml_meta": {'domain_of': ['FamilyMembership']} })
    family_id: str = Field(default=..., title="Family ID", description="""Global ID for the Family""", json_schema_extra = { "linkml_meta": {'domain_of': ['Family', 'FamilyMembership']} })
    subject_id: str = Field(default=..., title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    family_role: Optional[Union[EnumFamilyRole, str]] = Field(default=None, description="""The \"role\" of this individual in this family. Could include terms like \"proband\", \"mother\", etc.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumFamilyRole'}],
         'domain_of': ['FamilyMembership']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class SubjectAssertion(Record):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'assertion_id': {'any_of': [{'range': 'obGlobalID'},
                                                    {'range': 'deGlobalID'},
                                                    {'range': 'msGlobalID'}],
                                         'identifier': True,
                                         'name': 'assertion_id',
                                         'range': 'string',
                                         'required': True}},
         'title': 'Subject Assertion'})

    assertion_id: str = Field(default=..., title="Assertion ID", description="""INCLUDE Global ID for the Assertion""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'obGlobalID'},
                    {'range': 'deGlobalID'},
                    {'range': 'msGlobalID'}],
         'domain_of': ['SubjectAssertion']} })
    subject_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    encounter_id: Optional[str] = Field(default=None, title="Encounter ID", description="""Unique identifier for this Encounter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'BiospecimenCollection', 'Encounter']} })
    asserter_type: Optional[EnumAsserterType] = Field(default=None, title="Asserter Type", description="""The original asserter of this information""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    assertion_source_type: Optional[EnumDataSourceType] = Field(default=None, title="Assertion Source", description="""The source of this assertion from the original data""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    age_at_assertion: Optional[int] = Field(default=None, title="Age at assertion", description="""The age in days of the Subject when the assertion was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion'], 'unit': {'ucum_code': 'd'}} })
    age_at_event: Optional[int] = Field(default=None, title="Age at event", description="""The age in days of the Subject at the time point which the assertion describes, eg, age of onset or when a measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'Encounter'], 'unit': {'ucum_code': 'd'}} })
    age_at_resolution: Optional[int] = Field(default=None, title="Age at resolution", description="""The age in days of the Subject when the asserted state was resolved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion'], 'unit': {'ucum_code': 'd'}} })
    concept: Optional[list[str]] = Field(default=None, title="Concept", description="""The structured term defining the meaning of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    concept_source: Optional[str] = Field(default=None, title="Concept Source Text", description="""The source text yielding the standardized concept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_concept: Optional[list[Union[EnumPresentAbsent, str]]] = Field(default=None, title="Value concept", description="""The structured term defining the value of the assertion.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumPresentAbsent'}],
         'domain_of': ['SubjectAssertion']} })
    value_number: Optional[float] = Field(default=None, title="Value Number", description="""The numeric value of the assertion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_source: Optional[str] = Field(default=None, title="Value Source Text", description="""The source text yielding the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_unit: Optional[str] = Field(default=None, title="Value Units", description="""The structured term defining the units of the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    value_unit_source: Optional[str] = Field(default=None, title="Value Units Source Text", description="""The source text yielding the value's units.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Concept(ConfiguredBaseModel):
    """
    A standardized concept with display information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'slot_usage': {'concept_curie': {'identifier': True,
                                          'name': 'concept_curie',
                                          'required': True}},
         'title': 'Concept'})

    concept_curie: str = Field(default=..., title="Concept Curie", description="""The standardized curie for the term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })
    display: Optional[str] = Field(default=None, title="Display String", description="""The friendly display string of the coded term.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Concept']} })


class Sample(Record):
    """
    A functionally equivalent specimen taken from a participant or processed from such a sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'biospecimen_collection_id': {'description': 'Biospecimen '
                                                                     'Collection '
                                                                     'during which '
                                                                     'this sample was '
                                                                     'generated.',
                                                      'name': 'biospecimen_collection_id'},
                        'sample_id': {'identifier': True,
                                      'name': 'sample_id',
                                      'range': 'bsGlobalID',
                                      'required': True}},
         'title': 'Sample'})

    sample_id: str = Field(default=..., title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'Assay']} })
    biospecimen_collection_id: Optional[str] = Field(default=None, title="Biospecimen Collection ID", description="""Biospecimen Collection during which this sample was generated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'BiospecimenCollection']} })
    parent_sample_id: Optional[str] = Field(default=None, title="Parent Sample ID", description="""Sample from which this sample is derived""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    sample_type: str = Field(default=..., title="Sample Type", description="""Type of material of which this Sample is comprised. UBERON is recommended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    processing: Optional[list[str]] = Field(default=None, title="Sample Processing", description="""Processing that was applied to the Parent Sample or from the Biospecimen Collection that yielded this distinct sample. OBI is recommended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    availability_status: Optional[EnumAvailabilityStatus] = Field(default=None, title="Sample Availability", description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    storage_method: Optional[list[str]] = Field(default=None, title="Sample Storage Method", description="""Sample storage method, eg, Frozen or with additives. OBI may be suitable, or ChEBI for additives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample']} })
    quantity_number: Optional[float] = Field(default=None, title="Quantity", description="""The total quantity of the specimen""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_unit: Optional[str] = Field(default=None, title="Quantity Units", description="""The structured term defining the units of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class BiospecimenCollection(Record):
    """
    A biospecimen collection event which yields one or more Samples.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'biospecimen_collection_id': {'identifier': True,
                                                      'name': 'biospecimen_collection_id',
                                                      'range': 'string',
                                                      'required': True}},
         'title': 'BiospecimenCollection'})

    biospecimen_collection_id: str = Field(default=..., title="Biospecimen Collection ID", description="""Unique identifier for this Biospecimen Collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'BiospecimenCollection']} })
    age_at_collection: Optional[float] = Field(default=None, title="Age at Biospecimen Collection", description="""The age at which this biospecimen was collected in decimal years.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection'], 'unit': {'ucum_code': 'a'}} })
    method: Optional[EnumSampleCollectionMethod] = Field(default=None, title="Biospecimen Collection Method", description="""The approach used to collect the biospecimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['BiospecimenCollection']} })
    site: Optional[Union[EnumSite, str]] = Field(default=None, title="Biospecimen Collection Site", description="""The location of the specimen collection.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumSite'}],
         'domain_of': ['BiospecimenCollection']} })
    spatial_qualifier: Optional[Union[EnumSpatialQualifiers, str]] = Field(default=None, title="Spatial Qualifier", description="""Qualifier that further refine the specific location of biospecimen collection""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumSpatialQualifiers'}],
         'domain_of': ['BiospecimenCollection']} })
    laterality: Optional[Union[EnumLaterality, str]] = Field(default=None, title="Location Laterality", description="""Laterality that further refine the specific location of biospecimen collection""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumLaterality'}],
         'domain_of': ['BiospecimenCollection']} })
    encounter_id: Optional[str] = Field(default=None, title="Encounter ID", description="""Unique identifier for this Encounter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'BiospecimenCollection', 'Encounter']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Aliquot(Record):
    """
    A specific tube or amount of a biospecimen associated with a Sample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'aliquot_id': {'identifier': True,
                                       'name': 'aliquot_id',
                                       'range': 'string',
                                       'required': True}},
         'title': 'Aliquot'})

    aliquot_id: str = Field(default=..., title="Aliquot ID", description="""Unique identifier for an Aliquot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    sample_id: Optional[str] = Field(default=None, title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'Assay']} })
    availability_status: Optional[EnumAvailabilityStatus] = Field(default=None, title="Sample Availability", description="""Can this Sample be requested for further analysis?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_number: Optional[float] = Field(default=None, title="Quantity", description="""The total quantity of the specimen""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    quantity_unit: Optional[str] = Field(default=None, title="Quantity Units", description="""The structured term defining the units of the quantity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot']} })
    concentration_number: Optional[float] = Field(default=None, title="Concentration", description="""What is the concentration of the analyte in the Aliquot?""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    concentration_unit: Optional[str] = Field(default=None, title="Concentration Units", description="""Units associated with the concentration of the analyte in the Aliquot.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Aliquot']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Encounter(Record):
    """
    An event at which data was collected about a participant, an intervention was made, or information about a participant was recorded.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'encounter_id': {'identifier': True,
                                         'name': 'encounter_id',
                                         'range': 'enGlobalID',
                                         'required': True}},
         'title': 'Participant Encounter'})

    encounter_id: str = Field(default=..., title="Encounter ID", description="""Unique identifier for this Encounter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'BiospecimenCollection', 'Encounter']} })
    subject_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    encounter_definition_id: Optional[str] = Field(default=None, title="Encounter Definition ID", description="""Unique identifier for this Encounter Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Encounter', 'EncounterDefinition']} })
    age_at_event: Optional[int] = Field(default=None, title="Age at event", description="""The age in days of the Subject at the time point which the assertion describes, eg, age of onset or when a measurement was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SubjectAssertion', 'Encounter'], 'unit': {'ucum_code': 'd'}} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class EncounterDefinition(Record):
    """
    A definition of an encounter type in this study, ie, an event at which data was collected about a participant, an intervention was made, or information about a participant was recorded. This may be something planned by a study or a type of data collection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'activity_definition_id': {'multivalued': True,
                                                   'name': 'activity_definition_id'},
                        'encounter_definition_id': {'identifier': True,
                                                    'name': 'encounter_definition_id',
                                                    'range': 'pdGlobalID',
                                                    'required': True}},
         'title': 'Encounter Definition'})

    encounter_definition_id: str = Field(default=..., title="Encounter Definition ID", description="""Unique identifier for this Encounter Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Encounter', 'EncounterDefinition']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Description for this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Dataset']} })
    activity_definition_id: Optional[list[str]] = Field(default=None, title="Activity Definition ID", description="""Unique identifier for this Activity Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Assay']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class ActivityDefinition(Record):
    """
    A definition of an activity in this study, eg, a biospecimen collection, assay, intervention, survey, or assessment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'activity_definition_id': {'identifier': True,
                                                   'name': 'activity_definition_id',
                                                   'range': 'adGlobalID',
                                                   'required': True}},
         'title': 'Activity Definition'})

    activity_definition_id: str = Field(default=..., title="Activity Definition ID", description="""Unique identifier for this Activity Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Assay']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Description for this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Dataset']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class File(Record):
    """
    File
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'file_id': {'identifier': True,
                                    'name': 'file_id',
                                    'range': 'drGlobalID',
                                    'required': True},
                        'sample_id': {'multivalued': True, 'name': 'sample_id'},
                        'subject_id': {'multivalued': True, 'name': 'subject_id'}},
         'title': 'File'})

    file_id: str = Field(default=..., title="File ID", description="""Unique identifier for this File.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'Assay', 'Dataset']} })
    subject_id: Optional[list[str]] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    sample_id: Optional[list[str]] = Field(default=None, title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'Assay']} })
    filename: Optional[str] = Field(default=None, title="Filename", description="""The name of the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    format: Optional[EnumEDAMFormats] = Field(default=None, title="File Format", description="""The format of the file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    file_extension: str = Field(default=..., title="File Extension", description="""Typically a 3-4 letter code at the end of a filename that identifies the file format. Empty string for no extension.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    data_category: Optional[Union[EnumDataCategory, str]] = Field(default=None, title="Data Category", description="""General category of data in this Record (e.g. Clinical, Genomics, etc)""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'Concept'}, {'range': 'EnumDataCategory'}],
         'domain_of': ['StudyMetadata', 'File']} })
    data_type: Optional[EnumEDAMDataTypes] = Field(default=None, title="Data Type", description="""The type of data within this file.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    size: Optional[int] = Field(default=None, title="File Size", description="""Size of the file, in Bytes. May require BigInt or similar.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File'], 'unit': {'ucum_code': 'By'}} })
    internal_uri: Optional[str] = Field(default=None, title="Internal Staging Location", description="""URI/URL for internal access to the data. May be temporary.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    release_uri: Optional[str] = Field(default=None, title="Release Location", description="""URI/URL for controlled or open access to the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    drs_uri: Optional[str] = Field(default=None, title="DRS URI", description="""DRS location to access the data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    storage_class: Optional[str] = Field(default=None, title="Storage Class", description="""Storage class of the object, reflecting cost and access characteristics.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    hash: Optional[list[FileHash]] = Field(default=None, title="File Hash", description="""File hash information""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    availability: Optional[EnumAvailabilityStatus] = Field(default=None, title="File Availability", description="""Is or was this file available to users?""", json_schema_extra = { "linkml_meta": {'domain_of': ['File']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class FileHash(ConfiguredBaseModel):
    """
    Type and value of a file content hash.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'title': 'File Hash'})

    hash_type: Optional[EnumFileHashType] = Field(default=None, title="File Hash Type", description="""The type of file hash, eg, md5""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileHash']} })
    hash_value: Optional[str] = Field(default=None, title="File Hash Value", description="""The value of the file hash""", json_schema_extra = { "linkml_meta": {'domain_of': ['FileHash']} })


class Assay(Record):
    """
    A specific assay that was performed on given subject(s) or sample(s).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'mixins': ['Record'],
         'slot_usage': {'assay_id': {'identifier': True,
                                     'name': 'assay_id',
                                     'range': 'diGlobalID',
                                     'required': True},
                        'assay_type': {'name': 'assay_type', 'required': True},
                        'file_id': {'multivalued': True, 'name': 'file_id'},
                        'sample_id': {'multivalued': True, 'name': 'sample_id'},
                        'subject_id': {'multivalued': True, 'name': 'subject_id'}},
         'title': 'Assay'})

    assay_id: str = Field(default=..., title="Assay ID", description="""The unique identifier for the Assay.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    subject_id: Optional[list[str]] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the Subject""", json_schema_extra = { "linkml_meta": {'domain_of': ['Subject',
                       'Demographics',
                       'FamilyRelationship',
                       'FamilyMembership',
                       'SubjectAssertion',
                       'Encounter',
                       'File',
                       'Assay']} })
    sample_id: Optional[list[str]] = Field(default=None, title="Sample ID", description="""The unique identifier for this Sample.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sample', 'Aliquot', 'File', 'Assay']} })
    file_id: Optional[list[str]] = Field(default=None, title="File ID", description="""Unique identifier for this File.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'Assay', 'Dataset']} })
    assay_type: EnumAssayType = Field(default=..., title="Assay Type", description="""The type of assay performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    assay_source: Optional[str] = Field(default=None, title="Assay Source Text", description="""The original description of the Assay performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Assay']} })
    activity_definition_id: Optional[str] = Field(default=None, title="Activity Definition ID", description="""Unique identifier for this Activity Definition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Assay']} })
    external_id: Optional[list[str]] = Field(default=None, title="External Identifiers", description="""Other identifiers for this entity, eg, from the submitting study or in systems like dbGaP""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record']} })
    access_policy_id: Optional[str] = Field(default=None, title="Access Policy ID", description="""Global identifier for the access policy that applies to this row of data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'AccessPolicy']} })
    study_id: Optional[str] = Field(default=None, title="Study ID", description="""INCLUDE Global ID for the study""", json_schema_extra = { "linkml_meta": {'domain_of': ['Record', 'StudyMetadata']} })


class Dataset(ConfiguredBaseModel):
    """
    Set of files grouped together for release.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/common-access-model',
         'slot_usage': {'dataset_id': {'identifier': True,
                                       'name': 'dataset_id',
                                       'range': 'lsGlobalID',
                                       'required': True},
                        'file_id': {'description': 'The list of files comprising this '
                                                   'dataset.',
                                    'multivalued': True,
                                    'name': 'file_id'}},
         'title': 'Dataset'})

    dataset_id: str = Field(default=..., title="Dataset ID", description="""Unique identifier for a Dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    name: Optional[str] = Field(default=None, title="Name", description="""Name of the entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VirtualBiorepository',
                       'Investigator',
                       'EncounterDefinition',
                       'ActivityDefinition',
                       'Dataset']} })
    description: Optional[str] = Field(default=None, title="Description", description="""Description for this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['EncounterDefinition', 'ActivityDefinition', 'Dataset']} })
    do_id: Optional[str] = Field(default=None, title="DOI", description="""Digital Object Identifier (DOI) for this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'DOI', 'Dataset']} })
    file_id: Optional[list[str]] = Field(default=None, title="File ID", description="""The list of files comprising this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['File', 'Assay', 'Dataset']} })
    publication: Optional[list[Publication]] = Field(default=None, title="Publication", description="""Publications associated with this Record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Study', 'Dataset']} })
    data_collection_start: Optional[str] = Field(default=None, title="Data Collection Start", description="""The date that data collection started. May include only a year.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    data_collection_end: Optional[str] = Field(default=None, title="Data Collection End", description="""The date that data collection started. May include only a year.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Record.model_rebuild()
AccessPolicy.model_rebuild()
Study.model_rebuild()
StudyMetadata.model_rebuild()
VirtualBiorepository.model_rebuild()
DOI.model_rebuild()
Investigator.model_rebuild()
Publication.model_rebuild()
Subject.model_rebuild()
Demographics.model_rebuild()
Family.model_rebuild()
FamilyRelationship.model_rebuild()
FamilyMembership.model_rebuild()
SubjectAssertion.model_rebuild()
Concept.model_rebuild()
Sample.model_rebuild()
BiospecimenCollection.model_rebuild()
Aliquot.model_rebuild()
Encounter.model_rebuild()
EncounterDefinition.model_rebuild()
ActivityDefinition.model_rebuild()
File.model_rebuild()
FileHash.model_rebuild()
Assay.model_rebuild()
Dataset.model_rebuild()
