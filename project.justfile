## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Support for various dbt related tasks
[group('model development')]
dbt: gen-sqla gen-ftddd gen-dbtmodel

# SQL Alchemy model
[group('model development')]
gen-sqla:
    mkdir -p {{dest}}/sqlalchemy && \
    uv run gen-sqla {{source_schema_path}} --declarative > {{dest}}/sqlalchemy/{{schema_name}}.py


[group('model development')]
gen-ftddd:
  uv run linkml_extract_dd {{source_schema_path}}

[group('model development')]
gen-dbtmodel:
  uv run gen-dbtmodel

[group('model development')]
update-cam:
  uv run update-cam -d src/acr_harmonized_data_model/schema/upstream-models
