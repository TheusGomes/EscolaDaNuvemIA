# Este é um cometário de linha única (comment strings)

""" (docs strings)
este é um comentário
de mútiplas linhas
"""

# Este é um comentário

if True:
    print("Indentado corretamente") # imprime que está indentado corretamente
    if True:
        print("Bloco aninhado")
else:
    print("Bloco else")

nome = "Matheus"
print(f"Meu nome é {nome}") #f strings




a = 10 # int
b = 10.10 # float
c = "10" # str
d = True # bool




variavel = 10
print(type(variavel))

variavel = "Agora souuma string"
print(type(variavel))



a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)