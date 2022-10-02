import pandas as pd
import numpy as np

# Read Dataset format Dataframe
df = pd.read_csv('invertedIndexMhs.csv')
df.head(None)

# Membuat dataframe baru
df_dict = pd.DataFrame(columns = ["Freq","Posting_ptr","Terms_ptr"])

df_dict["Freq"] = df["docFreq"]
df_dict["Posting_ptr"] = df["postList"]

print(df_dict)

# Membuat term string dan term pointer
term_str = ""
term_counter = 0
for i in range(194):
    term = df["Terms"].iloc[i]
    term_str += term
    df_dict["Terms_ptr"].iloc[i] = term_counter
    term_counter += len(term)

print(term_str)
print(df_dict)

# Export to csv
df_dict.to_csv('compressed_index_dict.csv',index=False)
text_file = open("term.txt", "w")
text_file.write(term_str)
text_file.close()

