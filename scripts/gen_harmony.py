import csv
import re
import sys
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView


def generate_harmony_files(schema_path, output_base):
    view = SchemaView(schema_path)
    csv_path = Path(f"{output_base}.csv")
    md_path = Path(f"{output_base}.md")

    headers = [
        "local_code",
        "local_display",
        "local_system",
        "target_code",
        "target_system",
        "target_display",
    ]

    find_ncpi_ig = re.compile(r"^https://nih-ncpi\.github\.io/ncpi-fhir-ig-2")
    is_http = re.compile(r"^http")
    data_rows = []

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
                    # import pdb

                    # pdb.set_trace()
                    md_link = f"[{system}](https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem-{igsystem.split('/')[-1]})"
                else:
                    if is_http.match(system):
                        md_link = f"[{system}]({system})"
                    else:
                        md_link = system
                data_rows.append(
                    {
                        "local_code": pv_name,
                        "local_display": pv_def.title or pv_name,
                        "local_system": enum_name,
                        "target_code": code,
                        "target_system": system,
                        "system_link": md_link,
                        "target_display": pv_def.description or "",
                    }
                )
    pretty_headers = [
        "Local Code",
        "Local Display",
        "Local System",
        "Target Code",
        "Target System",
        "Target Display",
    ]
    # 2. Write CSV File
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data_rows)

    # Get the link for the MD page
    headers = ["system_link" if x == "target_system" else x for x in headers]
    # 3. Write Markdown File for MkDocs
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Harmony Mappings\n\n")
        f.write(
            "Mappings between internal Enums and external terminologies for Whistle.\n\n"
        )
        f.write(f"[Download Raw CSV](./{csv_path.name})\n\n")

        # Build Markdown Table
        f.write("| " + " | ".join(pretty_headers) + " |\n")
        f.write("| " + " | ".join(["---"] * len(pretty_headers)) + " |\n")
        for row in data_rows:
            f.write("| " + " | ".join(str(row[h]) for h in headers) + " |\n")

    print(f"Generated: {csv_path} and {md_path}")


if __name__ == "__main__":
    # Usage: python gen_harmony.py src/schema/model.yaml docs/harmony
    generate_harmony_files(sys.argv[1], sys.argv[2])
