try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print(conteudo)
except FileExistsError:
    print("Arquivos não encontrado!")
finally:
    arquivo.close()
    print("Arquivo fechado")