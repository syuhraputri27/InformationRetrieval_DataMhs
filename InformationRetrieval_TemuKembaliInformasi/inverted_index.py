import pandas as pd
import numpy

#Read Dataset format Dataframe
df = pd.read_csv('crawlDataMhs.csv')
df.head(None)
# print(df['Nama'],df['Organisasi/UKM & Periode'])

#Tokenisasi
df_parse = df.copy()

cols = ["Nama","NIM","Organisasi/UKM & Periode"]
for col in cols:
    df_parse[col] = df_parse[col].str.split()
# print(df_parse)

#Merge setiap kolom menjadi satu dokumen terms
df_mergeparse = pd.DataFrame(columns = ["dokumen"])

temp = df_parse["Nama"]

cols = ["NIM","Organisasi/UKM & Periode"]
for col in cols:
    temp = temp + df_parse[col]
    df_mergeparse["dokumen"] = temp
# print(df_mergeparse)

#Term with ID
df_term = pd.DataFrame(columns = ["Terms","ID"])

size = df_mergeparse.shape[0]
for y in range(size):
    row = df_mergeparse["dokumen"].iloc[y]

    for item in row:
        # df_term = pd.concat([df_term,{"Terms":item,"ID":y}], ignore_index=True)
        df_term = df_term.append({"Terms":item,"ID":y}, ignore_index=True)
        # https://www.balioglu.net/solved-how-to-convert-frame-append-to-pandas-concat/

        # pd.concat([pd.DataFrame([y], columns=["Terms","ID"]) for i in range(size)],ignore_index=True)

# print(df_term.head(None))

# Sort Term berdasar alfabet
df_term_sorted = df_term.sort_values(by="Terms")

# print(df_term_sorted.tail(10))
# print(df_term_sorted.shape[0])

# inisialisasi inverted index
df_invertedindex = pd.DataFrame(columns = ["Terms","docFreq","postList"])
# copy nila term unik
size = df_term_sorted.shape[0]
df_invertedindex['Terms'] = df_term_sorted['Terms'].unique()

# print(df_invertedindex.tail(50))

# inisialisasi nilai
df_invertedindex["docFreq"]=0
# print(df_invertedindex.tail(50))

# inverted index
size = df_term_sorted.shape[0]
invertedIndexCounter = 0
temp_list = []
for i in range(size):
    if (df_term_sorted['Terms'].iloc[i] == df_invertedindex['Terms'].iloc[invertedIndexCounter]):
        df_invertedindex["docFreq"].iloc[invertedIndexCounter]+=1
        temp_list.append(df_term_sorted["ID"].iloc[i])
        df_invertedindex["postList"].iloc[invertedIndexCounter] = temp_list
    else :
        temp_list = []
        invertedIndexCounter += 1
        df_invertedindex["docFreq"].iloc[invertedIndexCounter] += 1
        temp_list.append(df_term_sorted["ID"].iloc[i])
        df_invertedindex["postList"].iloc[invertedIndexCounter] = temp_list

# print(df_invertedindex.iloc[1:200])

# Export to CSV
print(df_invertedindex.to_csv("invertedIndexMhs.csv",index=False))