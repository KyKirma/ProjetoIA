import tkinter as tk

#Inicia-se a janela principal
root = tk.Tk();
root.geometry("900x600") #Define o tamanho inicial da janela
root.title("Projeto IA - Protótipo") #Titulo da janela
root.iconbitmap("./Interface/IFTM.ico") #Icon da janela

#As configurações de expansão
root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)

#====================================================

#?Definir os frames da janela
textosLabel = tk.Frame(root, bg = "lightgray", highlightbackground="blue", highlightcolor="blue", highlightthickness=2) #Container que contêm os labels do programa
funcaoBox = tk.Frame(root, bg = "lightgray", highlightbackground="blue", highlightcolor="blue", highlightthickness=2) #Container que contêm as funções de navegação e opção


#Suas posições na janela
textosLabel.grid(row = 0, column = 0, sticky = "wns", padx = 20, pady = 20)
funcaoBox.grid(row = 0, column = 1, sticky="nsew", padx = 20, pady = 20)
#====================================================

#?Definir os objetos da janela
#parte esquerda da tela, as labels
campLabel = tk.Label(textosLabel, text="Campeonato", padx = 15, pady = 15)
timeLabel = tk.Label(textosLabel, text="Times", padx = 15, pady = 15)
jogosLabel = tk.Label(textosLabel, text="Jogos", padx = 15, pady = 15)

#Suas posições na janela
campLabel.pack(padx = 5, pady = 5, expand = True, fill = "both")
timeLabel.pack(padx = 5, pady = 5, expand = True, fill = "both")
jogosLabel.pack(padx = 5, pady = 5, expand = True, fill = "both")

#parte direita da tela, as caixas funcionais
campFun = tk.Button(funcaoBox, text = "Protótipo")
timeFun = tk.Button(funcaoBox, text = "Protótipo")
jogosFun = tk.Button(funcaoBox, text = "Protótipo")

#Suas posições na janela
campFun.pack(padx = 5, pady = 5, expand = True, fill = "both")
timeFun.pack(padx = 5, pady = 5, expand = True, fill = "both")
jogosFun.pack(padx = 5, pady = 5, expand = True, fill = "both")


#====================================================

root.mainloop() #Inicializa a janela principal 