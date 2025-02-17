# acr-harmonized-data-model
LinkML Schema for ACR Harmonmized Data. 

# Tools Required
* LinkML 1.8.6
* Pydantic 2.10.6
* [mkdocs](https://www.mkdocs.org/) required to generate the documentation website

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
linkml-validate -s data-model/participant.yaml test-data/participant.csv -C Participant
