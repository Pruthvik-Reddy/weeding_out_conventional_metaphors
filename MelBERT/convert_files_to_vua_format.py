import pandas as pd

file_path = 'conventional_with_literals.tsv'
df = pd.read_csv(file_path, sep='\t')
df_2=pd.read_csv("novel_with_literals.tsv",sep="\t")

new_cols=["index","label","sentence","POS","FGPOS","w_index"]

old_cols=["index","label","sentence","pos","v_index"]

df["w_index"] = df["v_index"]
df["pos"] = df["POS"]
df["FGPOS"] = "VBZ"

df_2["w_index"] = df_2["v_index"]
df_2["pos"] = df_2["POS"]
df_2["FGPOS"] = "VBZ"





# Specify the file paths for the separated dataframes
file_path_01 = 'conventional_with_literals_vua.tsv'
file_path_23 = 'novel_with_literals_vua.tsv'

# Save the separated DataFrames to tab-separated files
df[new_cols].to_csv(file_path_01, sep='\t', index=False)
df_2[new_cols].to_csv(file_path_23, sep='\t', index=False)

print("DataFrame with [0.0, 1.0] values saved to", file_path_01)
print("DataFrame with [2.0, 3.0] values saved to", file_path_23)
