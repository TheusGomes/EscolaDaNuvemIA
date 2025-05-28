def is_palidromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]


expressao = str(input("Insira uma expressão para verificação: "))
resultado = is_palidromo(expressao)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"A expressão {expressao} é um palidromo? {resposta}")

