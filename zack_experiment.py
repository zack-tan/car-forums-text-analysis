import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

df = pd.read_csv("data.csv")
df = df.drop(['Unnamed: 0'],axis=1)

np.where(df["col1"] == df["col2"], True, False)
pass

# Extract text from each column - Subset df to only message
df_text = df['Message']

################## Preprocessing ##################

# Remove leading carriage returns and newline characters (Note: Does not apply this to \r\n within text. We can replace this later)
df_text = df_text.apply(lambda x : x.strip())

# NOTE: If you want to remove ALL \r\n - Use this: df_text[x].replace("\r\n", "")


# Remove stopwords?


# Stem/Lem?



################## Lookup ##################

# Find replacement texts - probably create some sort of lookup table?

# 

