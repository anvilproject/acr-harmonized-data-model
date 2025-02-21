# acr-harmonized-data-model
LinkML Schema for ACR Harmonmized Data. 

# Tools Required
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

Users can probably get away with slightly older versions but be aware that later versions of LinkML do require pydantic >= 2.x.x

# Creating the anvil project
Here is the command to [generate default artifacts](https://linkml.io/linkml/generators/project-generator.html) if there is a need. 

```
gen-project -d anvil data-model/anvil.yaml
```

# Creating the docs
```
gen-doc -d docs data-model/anvil.yaml
mkdocs build
```

# Validating Test Data
```
linkml-validate -s data-model/participant.yaml test-data/participant.csv -C Participant
```
