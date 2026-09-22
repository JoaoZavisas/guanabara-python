print('====== CONVERSÃO EM DÓLAR ======\n')
valor = float(input('Qual valor voce possui na sua carteira: '))

cotacao_dolar = 5.09
valor_dolares = valor / cotacao_dolar

print(f'\n A cotação do dolar está em {cotacao_dolar} Real brasileiro')
##print('Voce pode comprar em dolares o total de {:.2f}'.format(conversao)) teste com o antigo format
print(f'Voce pode comprar em dolares o total de {valor_dolares:.2f}')