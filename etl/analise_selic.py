import pandas as pd


df = pd.read_csv("Selic_diaria.csv")
df['data'] = pd.to_datetime(df['data'])
df ['valor'] = df['valor'].str.replace (',', '.').astype(float)

print(df.head())

print("\n informações do DataFrame: ")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())
dias_zero = df[df['valor'] == 0]
print(f"\nDias com SELIC igual a 0: {len(dias_zero)}")