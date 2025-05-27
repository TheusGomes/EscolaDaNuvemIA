try:
    numerador = int(input("Digite o numerador: "))
    denomidador = int(input("Digite o denomidador: "))
    resultado = numerador / denomidador
    print("O resultado é: ", resultado)
except ValueError:
    print("Por favor, insira apenas números.")
except ZeroDivisionError:
    print("Erro! Não é possível dividir por zero.")