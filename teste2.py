import tkinter as tk

# Função para mudar o texto do botão
def alterar_texto():
    botao.config(text="Novo Texto")

# Crie a janela principal
root = tk.Tk()

# Crie um botão
botao = tk.Button(root, text="Meu Botão")
botao.grid(row=0, column=0)

# Crie uma etiqueta de texto
etiqueta = tk.Label(root, text="Texto Abaixo")
etiqueta.grid(row=1, column=0)

# Crie um botão para alterar o texto
alterar_botao = tk.Button(root, text="Alterar Texto", command=alterar_texto)
alterar_botao.grid(row=2, column=0)

# Inicie o loop principal
root.mainloop()
