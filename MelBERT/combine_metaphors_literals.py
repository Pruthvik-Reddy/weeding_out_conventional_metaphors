import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

columns=["label","sentence","pos","v_index"]
conventional_df=pd.read_csv("../conventional.tsv",sep="\t",names=columns)
novel_df=pd.read_csv("../novel.tsv",sep="\t",names=columns)
literals_df=pd.read_csv("../literals.tsv",sep="\t",names=columns)

lit_90, lit_10 = train_test_split(literals_df, test_size=0.1, random_state=42)

conventional_combined_df = pd.concat([conventional_df, lit_90], ignore_index=True)
novel_combined_df = pd.concat([novel_df, lit_10], ignore_index=True)

conventional_combined_df.to_csv("conventional_with_literals.tsv",sep="\t",columns=columns)
novel_combined_df.to_csv("novel_with_literals.tsv",sep="\t",columns=columns)



