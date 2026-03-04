## Add your own just recipes here. This is imported by the main justfile.
# Generate erd for the overall schema and add it to the docs
[group('model development')]
_gen_ftddd:
  uv run linkml_extract_dd {{source_schema_path}}

[group('model development')]
_gen_sqla:
    mkdir -p {{dest}}/sqlalchemy && \
    uv run gen-sqla {{source_schema_path}} --declarative > {{dest}}/sqlalchemy/{{schema_name}}.py

[group('model development')]
_gen_harmony:
  python scripts/gen_harmony.py {{source_schema_path}} docs/harmony
