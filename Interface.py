import tkinter as tk
import pandas as pd
import mysql.connector
from tkinter import ttk
import os

#Iniciando o database
db = mysql.connector.connect(
    host="localhost",
    user="adm",
    password="adm",
    database="datafiles"
)

#Pegando os itens da data base
CSVPath = "./DataBase"
CSVFiles = os.listdir(CSVPath)

# Criar as tabelas
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS times (Nome VARCHAR(255) PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS campeonatos (id INT AUTO_INCREMENT PRIMARY KEY, Ano INT, Regiao VARCHAR(255), Divisao VARCHAR(3))")

def atualizar_db():
    atualizar_times()
    atualizar_camp()

#Filtrando todos os times existentes.
def atualizar_times():
    cursor = db.cursor()
    for arquivos_csv in CSVFiles:
        df = pd.read_csv(os.path.join(CSVPath, arquivos_csv))
        for index, row in df.iterrows():
            home_team = row['HomeTeam']
            away_team = row['AwayTeam']
            cursor.execute("INSERT IGNORE INTO times (Nome) VALUES (%s)", (home_team,))
            cursor.execute("INSERT IGNORE INTO times (Nome) VALUES (%s)", (away_team,))
    db.commit()        
    
def atualizar_camp():
    cursor = db.cursor()

    #?Filtrar as regiões pelas div dos mesmos.
    div_to_regiao = {
    'B': 'Belgica',
    'D': 'Alemanha',
    'E': 'Inglaterra',
    'F': 'França',
    'G': 'Grecia',
    'I': 'Italia',
    'N': 'Holanda',
    'P': 'Portugal',
    'SC': 'Escocia',
    'SP': 'Espanha',
    'T': 'Turquia',
}
    
    for arquivos_csv in CSVFiles:
        df = pd.read_csv(os.path.join(CSVPath, arquivos_csv))
        df['Regiao'] = df['Div'].str.extract(r'(\D{1,2})\d?')[0].map(div_to_regiao)
        df['Ano'] = df['Date'].str.extract(r'(\d{4})')

        for index, row in df.iterrows():
            div = row['Div']
            regiao = row['Regiao']
            ano = row['Ano']
            cursor.execute("INSERT IGNORE INTO campeonatos (Ano, Regiao, Divisao) VALUES (%s, %s, %s)", (ano, regiao, div))

    db.commit() 

def deletarTudo():
    try:
        cursor.execute("DELETE FROM times")
        cursor.execute("DELETE FROM campeonatos")
        db.commit()
    except Exception as e:
        print(f"Erro ao excluir tabelas: {e}")
    
    root.destroy()









#Inicia-se a janela principal
root = tk.Tk()
root.geometry("900x600") #Define o tamanho inicial da janela
root.title("Projeto IA - Protótipo") #Titulo da janela
root.iconbitmap("./Interface/IFTM.ico") #Icon da janela
root.minsize(700, 400) #Define o tamanho minimo da janela
root.protocol("WM_DELETE_WINDOW", deletarTudo) #!RESOLVER!!----------------------------------------------

#As configurações de expansão
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)

#====================================================

#?Definir os frames da janela
textosLabel = tk.Frame(root, bg = "lightgray") #Container que contêm os labels do programa
funcaoBox = tk.Frame(root, bg = "lightgray") #Container que contêm as funções de navegação e opção


#Suas posições na janela
textosLabel.grid(row = 0, column = 0, sticky = "wns", padx = 20, pady = 20)
funcaoBox.grid(row = 0, column = 1, sticky="nsew", padx = 20, pady = 20)
#====================================================

#?Definir os objetos da janela
#parte esquerda da tela, as labels
campLabel = tk.Label(textosLabel, text="Campeonato", padx = 3, pady = 3)
timeLabel = tk.Label(textosLabel, text="Times", padx = 15, pady = 15)
jogosLabel = tk.Label(textosLabel, text="Jogos", padx = 15, pady = 15)

#Suas posições na janela
campLabel.pack(padx = 5, pady = 5, expand = False, fill = "both")
timeLabel.pack(padx = 5, pady = 5, expand = True, fill = "both")
jogosLabel.pack(padx = 5, pady = 5, expand = True, fill = "both")

#parte direita da tela, as caixas funcionais
campCombo = tk.ttk.Combobox(funcaoBox)
timeFun = tk.Button(funcaoBox, text = "Protótipo")
jogosFun = tk.Button(funcaoBox, text = "Protótipo")

#Suas posições na janela
campCombo.pack(padx = 5, pady = 5, expand = False, fill = "both")
timeFun.pack(padx = 5, pady = 5, expand = True, fill = "both")
jogosFun.pack(padx = 5, pady = 5, expand = True, fill = "both")

#====================================================

root.mainloop() #Inicializa a janela principal 
atualizar_db()