In the previous file, we created the files conventional.tsv, containing conventional metaphors from VUAMC
- novel.tsv, containing novel metaphors from VUAMC
- literals.tsv, containing literals from VUAMC ( only sentences containing verbs )

In order to pass them to MelBERT, 
- 90% of literals are added to conventional and other 10% literals are added to novel. 
- Once those files are created, they are copied to MelBERT where they are split to 10 dataframes
