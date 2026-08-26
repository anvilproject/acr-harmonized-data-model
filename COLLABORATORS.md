## Welcome to the {program} Access Model 🚀

This repository serves as a downstream model designed to specialize the
[Common Access Model](https://github.com/include-dcc/common-access-model). A
pinned version of this upstream model is captured in
src/kf_access_model/schema/upstream-models/common_access_model*.yaml.

The purpose of this model is to build out a program-specific extension (or
profile) by importing the core elements and layering the Kids First unique data
requirements on top.

## Key Integration Guidelines

- The upstream-models/common_access_model.yaml should never be updated. This
  should be treated like any other machine generated file and left alone. If
  changes must be made to the upstream model, they should be made directly to
  that model, a release published and the local version updated using the
  tooling proved.
- Leverage Imports: At this time, the current model imports the
  common_access_model.yaml directly within the main model definition.
- Extend via Inheritance: Use the is_a or mixins keys to create program-specific
  subclasses that inherit core slots while allowing you to add local attributes.
- Refine via Slot Usage: If you need to restrict or change the behavior of an
  inherited core slot just for your program's classes, use the slot_usage
  feature.

## Updating to the newest common_access_model

Upon new releases in the common_access_model, a flattened version of the model
is generated and made available immediately. Tooling is provided to
automatically pull the newest version down and link it correctly to work without
making any changes to the local model's yaml.

```bash
just update-cam
```

This recipe will download the newest version to the directory,
src/kf_access_model/schema/upstream-models and create a symbolic link from the
common name, common_access_model.yaml. As a result, once that one entry has been
made to the local model, subsequent updates should work without further updates
to the model itself.

```model-yaml
imports:
  - upstream-models/common_access_model
```

The current version of the common_access_model and the symbolic link should be
properly managed by git so that all collaborators will be working on the same
core model.

> [WARNING] This will bring the upstream model to the most current version and,
> as such, should only be performed according to planned upgrades.

## Release Artifacts

There are a number of artifacts which are used by various scripts including the
dbt utilities which are built via github actions during release. To trigger the
build, create releases linked to a semantic version preceded with a v (i.e.
v1.0.1).

These artifacts include:

- SQL Alchemy model
- dbt model yml file
- SQL Schema
- data dictionary conformant to the current FTD spec
- enumerations csv file extracted from all of the permissible values

The last two are used by this group's dbt utilities tooling. The SQL Alchemy
model is used by a handful of other scripts.
