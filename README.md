# R-ICI_MNB_Survival

This repository contains scripts and data that support the publication: 'Prediction of Response to Immune Checkpoint Blockade in Patients with Metastatic Colorectal Cancer with Microsatellite Instability'.

## Repository structure

```
R-ICI_MNB_Survival
README.md
|-- Data
|   |-- ImmunoMSI
|   |   |-- MSICare
|   |   |-- RNA_count
|   |   |-- VC_mutect2
|   |-- Nipicol
|   |   |-- MSICare
|   |   |-- RNA_count
|   |   |-- VC_mutect2
|
|-- Naive_Bayes_model
|   |-- Preprocessed_data
|   |-- Scripts_and_notebooks

```
- **Data** : For Nipicol and ImmunoMSI cohorts, the record contains variant calling in repeated and non-repeated sequence from exome sequencing and contains feature counts from RNA-sequencing.
- **Naive_Bayes_model** : Repository containing interactive Python notebooks for feature selection on pre-processed data (included) and implementation of the Naive Bayes (NB) model.

## Guidelines

**In Scripts_and_notebooks** : 
- *Features_selection.ipynb* is the notebook used to select the most informative microsatellites.
- *Prediction.ipynb* load the NB published model and use it on formatted data to predict ICI resistance.

Specific instructions are in the notebooks.

## Additional software packages
We used Scikit-learn v 1.1.3 for the NB model using default parameter except for the alpha=0.1.

pandas v 1.4.2

numpy v 1.21.5

pickle v 4.0
