import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("etl/dados/Selic_diaria.csv")
df['data'] = pd.to_datetime(df['data'])
df['valor'] = df['valor'].astype(str).str.replace(',', '.').astype(float)
print(df.head())

print("\n informações do DataFrame: ")
print(df.info())
print("\nEstatísticas descritivas:")
print(df.describe())
dias_zero = df[df['valor'] == 0]
print(f"\nDias com SELIC igual a 0: {len(dias_zero)}")

#media, moda, minimo e maximo
print(f"\nMínima: {df['valor'].min()}%")
print(f"Máxima: {df['valor'].max()}%")
print(f"Média: {df['valor'].mean():.2f}%")
print(f"Moda: {df['valor'].mode()[0]}%")

df['ano'] = df['data'].dt.year
media_ano = df.groupby('ano')['valor'].mean()
print("\nMédia anual da SELIC:")
print(media_ano)


plt.figure(figsize=(10, 5))
plt.plot(media_ano.index, media_ano.values*100, marker='o', linestyle='-', color='green')
plt.title('Média anual da SELIC')
plt.xlabel('Ano')
plt.ylabel('Taxa média (%)')
plt.grid(True)
plt.tight_layout()
plt.show()