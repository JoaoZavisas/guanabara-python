lista_notas = []

print("=== CALCULADORA DE MÉDIA AUTOMÁTICA ===")
print("Digite as notas uma por uma. Quando terminar, digite -1 para ver o resultado.\n")

while True:
    entrada = float(input('Digite uma nota (ou -1 para ver o resultado\n)'))

    if entrada == -1:
        break

    lista_notas.append(entrada)

if len(lista_notas) > 0:
    media = sum(lista_notas) / len(lista_notas)
    print("\n--- RESULTADO FINAL ---")
    print('Voce digitou um total de {} notas.'.format(len(lista_notas)))
    print('A media final do aluno é {:.2f}'.format(media))
else:
    print("\nNenhuma nota foi digitada.")
