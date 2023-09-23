import pandas as pd
import os

# Especifique o caminho do diretório que contém o arquivo CSV
diretorio = "./DataBase"

# Liste os arquivos no diretório
arquivos_no_diretorio = os.listdir(diretorio)

# Verifique se há arquivos CSV no diretório
arquivos_csv = [arquivo for arquivo in arquivos_no_diretorio if arquivo.endswith('.csv')]

# Verifique se pelo menos um arquivo CSV foi encontrado
if arquivos_csv:
    # Construa o caminho completo para o primeiro arquivo CSV encontrado
    caminho_do_csv = os.path.join(diretorio, arquivos_csv[0])

    # Carregue o arquivo CSV em um DataFrame do Pandas
    df = pd.read_csv(caminho_do_csv)

    # Acesse a coluna desejada pelo nome
    coluna_desejada = df['Time']

    # Agora você pode usar coluna_desejada como uma série de dados do Pandas
    print(coluna_desejada)
else:
    print("Nenhum arquivo CSV encontrado no diretório.")
