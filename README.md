# acr-harmonized-data-model

LinkML Schema for ACR Harmonized Data. This model under development is intended to capture useful cross-study data in the AnVIL data repository. 

## Website

[https://anvilproject.github.io/acr-harmonized-data-model](https://anvilproject.github.io/acr-harmonized-data-model)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [acr_harmonized_data_model](src/acr_harmonized_data_model)
    * [schema](src/acr_harmonized_data_model/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/acr_harmonized_data_model/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation
You can build the model using link-ml calls or using the makefile/justfile.

### Linkml tools
<details>

#### Tools Required
* Python 3.12 (3.13 support [coming for linkml](https://github.com/linkml/linkml-runtime/pull/345))
* LinkML 1.8.6
* Pydantic 2.10.6
* [mkdocs](https://www.mkdocs.org/) required to generate the documentation website

Tools to install:
```
pip install linkml
pip install mkdocs
pip install mkdocs-mermaid2-plugin
```

#### Checking for convention compliance
It can be helpful to review the [schema for compliance with linkml conventions](https://linkml.io/linkml/schemas/linter.html). To run a check for all files against the default standards the following command can be run.
```
linkml-lint ./src/acr_harmonized_data_model
```

#### Creating the anvil project
Here is the command to [generate default artifacts](https://linkml.io/linkml/generators/project-generator.html) if there is a need. 

```
gen-project -d anvil ./src/acr_harmonized_data_model/schema/acr_harmonized_data_model.yaml
```

#### Creating the docs
```
gen-doc -d docs ./src/acr_harmonized_data_model/schema/acr_harmonized_data_model.yaml
mkdocs build
```
</details>

#### Manually building the Map Dragon formatted Data Dictionary
The DD export uses [ftd-dd](https://github.com/carrollaboratory/ftd-dd) library to generate the CSV Files. This has been integrated into the command <b>make site</b>, but can also be run manually. 

You can install this library using pip: 

```
pip install -r requirements.txt 
```

or via the makefile
```
make install
```

Once installed, the dd-files can be built manually:
```
linkml_extract_dd src/acr_harmonized_data_model/schema/acr_harmonized_data_model.yaml
```

Otherwise, just build the site as usual and the data-dictionary will be created alongside the rest of the artifacts. 

```
make site
```

Resulting DD files can be found in: project/data-dictionary


### Makefile / Justfile

<details>

To run commands you may use good old make or the command runner [just](https://github.com/casey/just/) which is a better choice on Windows.
Use the `make` command or `duty` commands to generate project artefacts:
* `make help` or `just --list`: list all pre-defined tasks
* `make all` or `just all`: make everything
* `make deploy` or `just deploy`: deploys site
* `make test` or `just test`: run tests on the model and examples

</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
