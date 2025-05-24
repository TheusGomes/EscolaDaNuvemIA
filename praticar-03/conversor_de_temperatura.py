"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""


temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if origem == destino:
    resultado = temp
elif origem == "C":
    if destino == "F":
        resultado = (temp * 9/5) + 32
    else:
        resultado = temp + 273.15

elif origem == "F":
    if destino == "C":
        resultado = (temp - 32) / 9/5
    else:
        resultado = (temp - 32) / 9/5 + 273.15
else:
    if destino == "C":
        resultado = temp - 273.15
    else:
        resultado = (temp - 273.15) * 9/5 + 32

print(f"A temperarura {temp} {origem} é igual a {resultado:.2f} {destino}")
