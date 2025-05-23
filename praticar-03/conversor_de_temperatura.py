"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

 
print("Escolha a conversão:")
print("1 - Celsius para Fahrenheit")
print("2 - Celsius para Kelvin")
print("3 - Fahrenheit para Celsius")

opcao = input("Digite a opção (1, 2 ou 3): ")

if opcao == "1":
    c = float(input("Digite a temperatura em Celsius: "))
    f = c * 9/5 + 32
    print(f"Fahrenheit: {f:.2f}")

elif opcao == "2":
    c = float(input("Digite a temperatura em Celsius: "))
    k = c + 273.15
    print(f"Kelvin: {k:.2f}")

elif opcao == "3":
    f = float(input("Digite a temperatura em Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Celsius: {c:.2f}")

else:
    print("Opção inválida")
