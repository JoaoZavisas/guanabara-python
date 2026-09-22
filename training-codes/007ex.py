nota01 = float(input('Digite sua primeira nota: '))
nota02 = float(input('Digite sua segunda nota: '))

lista_notas = [nota01, nota02]

media = sum(lista_notas) / len(lista_notas)

print('Sua media é {}'.format(media))