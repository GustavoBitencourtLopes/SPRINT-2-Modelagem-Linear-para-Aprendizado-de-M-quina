import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("base_recarga_veiculos_eletricos_convertido.csv")
print(df)

print(df.head())

print(df.info())

print(df.describe())

