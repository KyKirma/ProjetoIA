import tkinter as tk
import pandas as pd
import mysql.connector
from tkinter import ttk
from tkinter import Canvas
import os
import re

#Iniciando o database
db = mysql.connector.connect(
    host="localhost",
    user="adm",
    password="adm",
    database="datafiles"
)

cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS campeonatos (Divisao VARCHAR(3), Ano INT, Regiao VARCHAR(20), Nome VARCHAR(255), PRIMARY KEY (Divisao, Ano))")
cursor.execute("CREATE TABLE IF NOT EXISTS times (Nome VARCHAR(255) PRIMARY KEY)")
cursor.execute("CREATE TABLE IF NOT EXISTS TPC (CampAno INT, Divisao VARCHAR(3), Time VARCHAR(255), PRIMARY KEY (CampAno, Divisao, Time))")

#Pegando os itens da data base
CSVPath = "./DataBase"
CSVFiles = os.listdir(CSVPath)

# Criar as tabelas
def atualizar_db():
    atualizar_camp()


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
            #Tabela Times
            home_team = row['HomeTeam']
            away_team = row['AwayTeam']
            cursor.execute("INSERT IGNORE INTO times (Nome) VALUES (%s)", (home_team,))
            cursor.execute("INSERT IGNORE INTO times (Nome) VALUES (%s)", (away_team,))

            #Campeonatos
            div = row['Div']
            regiao = row['Regiao']
            ano = row['Ano']
            nome = "{} {} {}".format(div, regiao, ano)
            cursor.execute("INSERT IGNORE INTO campeonatos (Divisao, Ano, Regiao, Nome) VALUES (%s, %s, %s, %s)", (div, ano, regiao, nome))

            cursor.execute("INSERT IGNORE INTO TPC (CampAno, Divisao, Time) VALUES (%s, %s, %s)", (ano, div, home_team))
            cursor.execute("INSERT IGNORE INTO TPC (CampAno, Divisao, Time) VALUES (%s, %s, %s)", (ano, div, away_team))

    db.commit()

def deletarTudo():
    db.close()
    root.destroy()


def atualizarComboCamp():
    # Carregar os campeonatos no ComboBox
    cursor = db.cursor()
    cursor.execute("SELECT nome FROM campeonatos")
    campeonatos = cursor.fetchall()
    campeonatosLista = []
    for i in campeonatos:
        campeonatosLista.append(i[0])
    campCombo["values"] = campeonatosLista

def atualizarComboTime(frame):
    cursor = db.cursor()
    #Verifica se o valor selecionado na combo existe em alguma div do TPC
    cursor.execute("SELECT Divisao FROM campeonatos WHERE Nome = %s", (campCombo.get(),))
    camp_selecionado = cursor.fetchone()
    cursor.execute("SELECT Time FROM TPC WHERE Divisao = %s", (camp_selecionado[0],)) #por ser uma tupla, devemos selecionar o indice para o acesso do dado
    times = cursor.fetchall()
    timesNaDiv = [time[0] for time in times] #converte a tupla para uma lista
    timesLista = []
    for item in timesNaDiv:
        timesLista.append(item[0])
    timeFun["values"] = timesLista


#Inicia-se a janela principal
root = tk.Tk()
root.geometry("900x600") #Define o tamanho inicial da janela
root.title("Projeto IA - Protótipo") #Titulo da janela
root.iconbitmap("./Interface/IFTM.ico") #Icon da janela
root.minsize(700, 400) #Define o tamanho minimo da janela
root.protocol("WM_DELETE_WINDOW", ) #!RESOLVER!!----------------------------------------------

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
timeLabel = tk.Label(textosLabel, text="Times", padx = 3, pady = 3)
jogosLabel = tk.Label(textosLabel, text="Jogos", padx = 15, pady = 15)

#Suas posições na janela
campLabel.pack(padx = 5, pady = 5, expand = False, fill = "both")
timeLabel.pack(padx = 5, pady = 5, expand = False, fill = "both")
jogosLabel.pack(padx = 5, pady = 5, expand = True, fill = "both")

#parte direita da tela, as caixas funcionais
campCombo = tk.ttk.Combobox(funcaoBox)
atualizarComboCamp()

timeFun = tk.ttk.Combobox(funcaoBox)

jogosFun = tk.Button(funcaoBox, text = "Protótipo")

campCombo.bind("<<ComboboxSelected>>", lambda event, frame=timeFun: atualizarComboTime(frame))


#Suas posições na janela
campCombo.pack(padx = 5, pady = 5, expand = False, fill = "both")
timeFun.pack(padx = 5, pady = 5, expand = False, fill = "both")
jogosFun.pack(padx = 5, pady = 5, expand = True, fill = "both")

#====================================================

root.mainloop() #Inicializa a janela principal 
atualizar_db()