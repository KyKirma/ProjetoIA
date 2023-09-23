import os

# Especifique o caminho do diretório que deseja verificar
caminho_do_diretorio = "./DataBase"

# Verifique se o caminho é um diretório válido
if os.path.isdir(caminho_do_diretorio):
    # Liste os itens no diretório
    itens_no_diretorio = os.listdir(caminho_do_diretorio)

    # Verifique se há itens no diretório
    if itens_no_diretorio:
        # Pegue o primeiro item
        primeiro_item = itens_no_diretorio[0]
        print(f"O primeiro item no diretório é: {primeiro_item}")
    else:
        print("O diretório está vazio.")
else:
    print("O caminho especificado não é um diretório válido.")
