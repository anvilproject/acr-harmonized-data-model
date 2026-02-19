## Add your own just recipes here. This is imported by the main justfile.
# Generate erd for the overall schema and add it to the docs
[group('model development')]
_gen_ftddd:
  uv run linkml_extract_dd {{source_schema_path}}
