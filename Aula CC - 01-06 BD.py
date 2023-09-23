import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

# Conectar ao banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="aluno",
    password="aluno",
    database="supermercado"
)

# Criar a tabela de clientes
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), endereco VARCHAR(255), cpf VARCHAR(11), telefone VARCHAR(11))")

def atualizarCombo():
    # Carregar os clientes no ComboBox
    cursor = db.cursor()
    cursor.execute("SELECT nome FROM clientes")
    clientes = cursor.fetchall()
    clientesLista = []
    for i in clientes:
        clientesLista.append(i[0])
    print(clientesLista)
    combo_clientes["values"] = clientesLista


def adicionar_cliente():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()

    if nome == "" or endereco == "" or cpf == "" or telefone == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    cursor = db.cursor()
    sql = "INSERT INTO clientes (nome, endereco, cpf, telefone) VALUES (%s, %s, %s, %s)"
    val = (nome, endereco, cpf, telefone)
    cursor.execute(sql, val)
    db.commit()

    messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso.")

    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    atualizarCombo()

def atualizar_cliente():
    cliente_selecionado = combo_clientes.get()

    if cliente_selecionado == "":
        messagebox.showerror("Erro", "Por favor, selecione um cliente para atualizar.")
        return

    nome = entry_nome.get()
    endereco = entry_endereco.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()

    if nome == "" or endereco == "" or cpf == "" or telefone == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return

    cursor = db.cursor()
    sql = "UPDATE clientes SET nome = %s, endereco = %s, cpf = %s, telefone = %s WHERE nome = %s"
    val = (nome, endereco, cpf, telefone, cliente_selecionado)
    cursor.execute(sql, val)
    db.commit()

    messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso.")

    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)
    combo_clientes.set("")
    atualizarCombo()

def deletar_cliente():
    cliente_selecionado = combo_clientes.get()

    if cliente_selecionado == "":
        messagebox.showerror("Erro", "Por favor, selecione um cliente para deletar.")
        return

    if messagebox.askyesno("Confirmação", f"Tem certeza que deseja deletar o cliente {cliente_selecionado}?"):
        cursor = db.cursor()
        sql = "DELETE FROM clientes WHERE nome = %s"
        val = (cliente_selecionado,)
        cursor.execute(sql, val)
        db.commit()

        messagebox.showinfo("Sucesso", "Cliente deletado com sucesso.")

        entry_nome.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        combo_clientes.set("")

    atualizarCombo()

def selecionar_cliente(event):
    cliente_selecionado = combo_clientes.get()

    if cliente_selecionado == "":
        entry_nome.delete(0, tk.END)
        entry_endereco.delete(0, tk.END)
        entry_cpf.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        return

    cursor = db.cursor()
    sql = "SELECT * FROM clientes WHERE nome = %s"
    val = (cliente_selecionado,)
    cursor.execute(sql, val)
    resultado = cursor.fetchone()

    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

    if resultado:
        entry_nome.insert(tk.END, resultado[1])
        entry_endereco.insert(tk.END, resultado[2])
        entry_cpf.insert(tk.END, resultado[3])
        entry_telefone.insert(tk.END, resultado[4])

# Criar a janela principal
window = tk.Tk()
window.title("CRUD de Clientes")

# Criar os campos de entrada e rótulos
label_nome = tk.Label(window, text="Nome:")
label_nome.grid(row=0, column=0, sticky=tk.W)
entry_nome = tk.Entry(window)
entry_nome.grid(row=0, column=1)

label_endereco = tk.Label(window, text="Endereço:")
label_endereco.grid(row=1, column=0, sticky=tk.W)
entry_endereco = tk.Entry(window)
entry_endereco.grid(row=1, column=1)

label_cpf = tk.Label(window, text="CPF:")
label_cpf.grid(row=2, column=0, sticky=tk.W)
entry_cpf = tk.Entry(window)
entry_cpf.grid(row=2, column=1)

label_telefone = tk.Label(window, text="Telefone:")
label_telefone.grid(row=3, column=0, sticky=tk.W)
entry_telefone = tk.Entry(window)
entry_telefone.grid(row=3, column=1)

# Criar o botão "Adicionar"
button_adicionar = tk.Button(window, text="Adicionar", command=adicionar_cliente)
button_adicionar.grid(row=4, column=0)

# Criar o botão "Atualizar"
button_atualizar = tk.Button(window, text="Atualizar", command=atualizar_cliente)
button_atualizar.grid(row=4, column=1)

# Criar o botão "Deletar"
button_deletar = tk.Button(window, text="Deletar", command=deletar_cliente)
button_deletar.grid(row=4, column=2)

# Criar o ComboBox para selecionar o cliente
label_cliente = tk.Label(window, text="Selecione o cliente:")
label_cliente.grid(row=5, column=0, sticky=tk.W)
combo_clientes = tk.ttk.Combobox(window)
combo_clientes.grid(row=5, column=1)
combo_clientes.bind("<<ComboboxSelected>>", selecionar_cliente)

atualizarCombo()

# Iniciar a interface da aplicação
window.mainloop()