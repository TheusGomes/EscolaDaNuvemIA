try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido! Por favor, insira um número.")
print(f"O valor é: {numero}")