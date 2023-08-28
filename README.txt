The dataset and initial codes are obtained from the link in the paper "Weeding out Conventional Metaphors"

Once we have the XML file containing sentences, we generate conventional.tsv, novel.tsv and literals.tsv from 
VUAMC_with_novelty_scores.xml using generate_conventional_novel_files.py

- Once those files are generated, we want to test it on MelBERT. So to make the dataset suitable as input for MelBERT
the code is in the folder MelBERT
