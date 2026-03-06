import csv
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import NamedTuple, Optional

from linkml_runtime.utils.schemaview import SchemaView


class SlotInfo(NamedTuple):
    slot_name: str
    class_name: str
    enum_range: str
    description: Optional[str] = None
    title: Optional[str] = None


class EnumeratedValue:
    def __init__(self, local_code, local_display, local_system, **kwargs):

        self.local_code = local_code
        self.local_display = local_display
        self.local_system = local_system

        # Support for more than one mapping
        self.mappings = []

        # SlotInfo 0..*
        self.slots = []

    @classmethod
    def harmony_header(cls):
        return [
            "local_code",
            "text",
            "table_name",
            "parent_varname",
            "local_code_system",
            "code",
            "display",
            "code_system",
            "comment",
        ]

    def write_harmony(
        self, writer, mapped_code, mapped_system, mapped_display, slot_details=None
    ):
        writer.writerow(
            [
                self.local_code,
                self.local_display,
                self.local_system,
                "" if slot_details is None else slot_details.class_name,
                "" if slot_details is None else slot_details.slot_name,
                mapped_code,
                mapped_system,
                mapped_display,
                "LinkML gen-harmony",
            ]
        )

    def append_to_harmony(self, writer):
        if len(self.mappings) > 0:
            for mapping in self.mappings:
                if len(self.slots) > 0:
                    for slot in self.slots:
                        self.write_harmony(
                            writer,
                            mapped_code=mapping["code"],
                            mapped_system=mapping["system"],
                            mapped_display=mapping["display"],
                            slot_details=slot,
                        )
                else:
                    self.write_harmony(
                        writer,
                        mapped_code=mapping["code"],
                        mapped_system=mapping["system"],
                        mapped_display=mapping["display"],
                    )

    @classmethod
    def md_header(cls):
        return [
            "Local Code",
            "Local Display",
            "Class Name",
            "Slot Name",
            "Target Code",
            "Target System",
        ]

    def write_markdown(
        self, writer, mapped_code, mapped_display, mapped_system, slot_details=None
    ):
        writer.write(
            "| "
            + " | ".join(
                [
                    self.local_code,
                    self.local_display,
                    "" if slot_details is None else slot_details.class_name,
                    "" if slot_details is None else slot_details.slot_name,
                    mapped_code,
                    mapped_system,
                ]
            )
            + "\n"
        )

    def append_to_markdown(self, writer):
        # We can skip anything that has no mappings
        if len(self.mappings) > 0:
            for mapping in self.mappings:
                if len(self.slots) > 0:
                    for slot in self.slots:
                        self.write_markdown(
                            writer,
                            mapped_code=mapping["code"],
                            mapped_system=mapping["md_link"],
                            mapped_display=mapping["display"],
                            slot_details=slot,
                        )
                else:
                    self.write_harmony(
                        writer,
                        mapped_code=mapping["code"],
                        mapped_system=mapping["md_link"],
                        mapped_display=mapping["display"],
                    )
        else:
            print(f"No mappings for {self.local_code}, {self.local_display}")


def generate_harmony_files(schema_path, output_base):
    view = SchemaView(schema_path)
    csv_path = Path(f"{output_base}.csv")
    md_path = Path(f"{output_base}.md")

    enumerated_slots = defaultdict(list)

    # Gather slots associated with enums to tag our enums correctly
    for class_name, class_def in view.all_classes().items():
        for slot_name in view.class_slots(class_name):
            slot_def = view.induced_slot(slot_name, class_name)

            if slot_def.range in view.all_enums():
                enumerated_slots[slot_def.range].append(
                    SlotInfo(
                        slot_name=slot_name,
                        class_name=class_name,
                        enum_range=slot_def.range,
                        description=slot_def.description,
                        title=slot_def.title,
                    )
                )

    find_ncpi_ig = re.compile(r"^https://nih-ncpi\.github\.io/ncpi-fhir-ig-2")
    is_http = re.compile(r"^http")

    enumerated_values = []
    # data_rows = []

    # 1. Extract data from Schema
    for enum_name, enum_def in view.all_enums().items():
        # Use enum title if available, otherwise fallback to name
        enum_label = enum_def.title or enum_name

        for pv_name, pv_def in enum_def.permissible_values.items():
            if pv_def.meaning:
                curie = pv_def.meaning
                full_uri = view.expand_curie(curie)

                # Split CURIE to separate code from the base system URI
                if ":" in curie:
                    _, code = curie.split(":", 1)
                    system = full_uri.replace(code, "")
                else:
                    system, code = full_uri, curie

                # Our IG systems don't resolve correctly
                if find_ncpi_ig.match(system):
                    igsystem = system
                    if system[-1] == "/":
                        igsystem = system[0:-1]
                    md_link = f"[{system}](https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem-{igsystem.split('/')[-1]})"
                else:
                    if is_http.match(system):
                        md_link = f"[{system}]({system})"
                    else:
                        md_link = system

                enum_val = EnumeratedValue(
                    local_code=pv_name,
                    local_display=pv_def.title or pv_name,
                    local_system=enum_name,
                )
                enum_val.mappings.append(
                    {
                        "code": code,
                        "display": pv_def.description or "",
                        "system": system,
                        "md_link": md_link,
                    }
                )

                # Find any slots that use this enum
                if enum_name in enumerated_slots:
                    enum_val.slots = enumerated_slots[enum_name]

                enumerated_values.append(enum_val)

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # writer = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        writer.writerow(EnumeratedValue.harmony_header())

        for ev in enumerated_values:
            ev.append_to_harmony(writer)

    # Get the link for the MD page
    # headers = ["system_link" if x == "target_system" else x for x in headers]
    # 3. Write Markdown File for MkDocs
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write("hide:\n")
        f.write(" - toc\n")
        f.write("---\n\n")
        f.write("# Harmony Mappings\n\n")
        f.write(
            "Mappings between internal Enums and external terminologies for DBT FHIR ETL.\n\n"
        )
        f.write(
            f"[Download Contents in Map Dragon Harmony CSV format](./{csv_path.name})\n\n"
        )

        # Build Markdown Table
        md_headers = EnumeratedValue.md_header()

        f.write("| " + " | ".join(md_headers) + " |\n")
        f.write("| " + " | ".join(["---"] * len(md_headers)) + " |\n")
        for ev in enumerated_values:
            ev.append_to_markdown(f)

    print(f"Generated: {csv_path} and {md_path}")


if __name__ == "__main__":
    # Usage: python gen_harmony.py src/schema/model.yaml docs/harmony
    generate_harmony_files(sys.argv[1], sys.argv[2])
