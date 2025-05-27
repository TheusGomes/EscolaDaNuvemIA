def registrar_notas():
    nota_lista = []
    while True:
        try:
            entrada = input("Digite uma nota ou digite 'fim' para encerrar: ")
            if entrada.lower() == 'fim':
                break
            nota = float(entrada)
            if 0 <= nota <= 10:
                nota_lista.append(nota)
            else:
                print("Nota inválida: digite um valor entre 0 e 10: ")
            continue
        except ValueError:
            print("Entrada inálida. Insira, por favor, um número cálido ou digite 'fim' para encerrar: ")

    if nota_lista:
        media = sum(nota_lista) / len(nota_lista)
        print(f"\nA media da turma é: {media:.2f}")
        print(f"O total de notas válidas é: {len(nota_lista)}")
    else:
        print("Nenhuma nota foi registrada ainda.")

registrar_notas()