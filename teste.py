import tkinter as tk
from tkinter import ttk

# Crie a janela principal
root = tk.Tk()
root.geometry("400x300")

# Crie um canvas
canvas = tk.Canvas(root)
canvas.pack(fill="both", expand=True)

# Crie um quadro dentro do canvas
timeFun = tk.Frame(canvas)
canvas.create_window((0, 0), window=timeFun, anchor="nw")

# Adicione widgets (botoes) ao quadro (você pode adicionar quantos quiser)
for i in range(20):
    botao = tk.Button(timeFun, text=f"Botão {i}")
    botao.pack(side="left", padx=5, pady=5)

# Crie uma barra de rolagem horizontal
scrollbar = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
scrollbar.pack(side="bottom", fill="x")

# Configure o canvas para usar a barra de rolagem horizontal
canvas.configure(xscrollcommand=scrollbar.set)

# Inicie o loop principal
root.mainloop()
