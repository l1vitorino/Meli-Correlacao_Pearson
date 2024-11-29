import pandas as pd
import numpy as np

df = pd.read_excel('data\Argentina.xlsx')
columns_names = { x: x.split(' [YR')[0]  if ' [YR' in x else x for x in df.columns } 

df = df.rename(columns= columns_names )

countyears = df.iloc[:, 1:].notna().sum(axis=1)

df = df[countyears > 10]

df = df.set_index("Series Name").T
df = df.corr('pearson')["Individuals using the Internet (% of population)"].reset_index()

df['Cluster'] =pd.cut(
    np.abs(df['Individuals using the Internet (% of population)']),
    bins=[0, 0.3, 0.7, 1],
    labels=['Fraca', 'Média', 'Forte']
)
print(df.head())

df.to_excel('data/result.xlsx', sheet_name= 'a1')