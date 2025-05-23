# Captura a idade do usário
idade = int(input("Digite a sua idade: "))

# Verificação de idade
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é adolescente.")
else:
    print("Você não é maior de idade")