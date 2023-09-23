import pandas as pd

# Carregue o arquivo CSV em um DataFrame do Pandas
df = pd.read_csv('F:\pedro\Documents\Programação\ProjetoIA\I1.csv')

# Acesse a coluna desejada pelo nome
coluna_desejada = df['Time']
# Ou pelo índice
# coluna_desejada = df.iloc[:, indice_da_coluna]

# Agora você pode usar coluna_desejada como uma série de dados do Pandas
print(coluna_desejada)


#Iniciando o database
db = mysql.connector.connect(
    host="localhost",
    user="adm",
    password="adm",
    database="datafiles"
)

# Criar a tabela de clientes
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), endereco VARCHAR(255), cpf VARCHAR(11), telefone VARCHAR(11))")
