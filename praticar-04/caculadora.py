while True:
    try:
        num1 = float(input("Digite seu 1 numero: "))
        num2 = float(input("Digite seu 2 numero: "))

        operacao = input("Digite a operação (+, -, *, /): ").strip()
    
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida")
        
        print(f"O resultado é: {resultado}")
        break

    except ZeroDivisionError:
        print(f"Erro: divisão por zero não é permitida. por favor, tente novamente.")

    except ValueError as e:
        print(f"Erro: {e}  . por favor, tente novamente")