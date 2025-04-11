import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from datetime import datetime, timedelta

def visualizar_dados():
    try:
        # Lista de possíveis caminhos para o arquivo
        possible_paths = [
            r'C:\Users\Gustavo\Documents\fin-data\fin-data\dados\Selic_diaria.csv',
            r'C:\Users\Gustavo\Documents\fin-data\fin-data\etl\dados\Selic_diaria.csv',
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Selic_diaria.csv'),
            os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'dados', 'Selic_diaria.csv')
        ]
        
        # Verificar cada caminho
        csv_path = None
        for path in possible_paths:
            if os.path.exists(path):
                csv_path = path
                print(f"Arquivo encontrado em: {csv_path}")
                break
        
    
        if csv_path is None:
            print("Arquivo não encontrado.")
             
        else:
            # Carregar os dados do arquivo existente
            df = pd.read_csv(csv_path)
        
        # Verificar se há dados
        if df.empty:
            print("O arquivo CSV está vazio!")
            return
            
        print(f"Dados carregados com sucesso. Formato: {df.shape}")
        
        # Converter a coluna de data
        df['data'] = pd.to_datetime(df['data'])
        
        # Criar o gráfico
        plt.figure(figsize=(12, 6))
        plt.plot(df['data'], df['valor'], color='blue', linewidth=2)
        plt.title('Taxa SELIC ao longo do tempo', fontsize=16)
        plt.xlabel('Data', fontsize=12)
        plt.ylabel('Taxa SELIC (%)', fontsize=12)
        plt.grid(True)
        plt.tight_layout()
        

        print("Exibindo o gráfico...")
        plt.show()
        
        input("Pressione Enter para sair...")
        
    except Exception as e:
        print(f"Erro ao visualizar dados: {e}")
        import traceback
        traceback.print_exc()
        input("Ocorreu um erro. Pressione Enter para sair...")

if __name__ == "__main__":
    visualizar_dados()