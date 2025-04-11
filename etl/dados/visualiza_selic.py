import pandas as pd
import matplotlib.pyplot as plt

def visualizar_dados():
 
    df = pd.read_csv(r'C:\Users\Gustavo\Documents\fin-data\fin-data\dados\Selic_diaria.csv')

    df['data'] = pd.to_datetime(df['data']) 

    plt.figure(figsize=(12, 6))
    plt.plot(df['data'], df['valor'], color='blue', linewidth=2)
    plt.title('Taxa SELIC ao longo do tempo', fontsize=16)
    plt.xlabel('Data', fontsize=12)
    plt.ylabel('Taxa SELIC (%)', fontsize=12)
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    input("Pressione Enter para sair...")

visualizar_dados()
