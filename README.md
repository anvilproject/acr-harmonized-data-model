<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# acr-harmonized-data-model

LinkML Schema for ACR Harmonized Data. This model under development is intended to capture useful cross-study data in the AnVIL data repository.

## Documentation Website

[https://anvilproject.github.io/acr-harmonized-data-model](https://anvilproject.github.io/acr-harmonized-data-model)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [acr_harmonized_data_model](src/acr_harmonized_data_model)
    * [schema/](src/acr_harmonized_data_model/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/acr_harmonized_data_model/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/).
To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
