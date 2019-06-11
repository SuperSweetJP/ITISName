import pandas as pd
import numpy as np
import phonetics


name1 = "Janis Plavins"

df = pd.read_csv("longnames", delimiter="|", header=None, index_col=0)



print(df.head())