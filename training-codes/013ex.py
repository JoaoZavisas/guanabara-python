preco = float(input('Digite o valor do produto: '))
desconto = preco * 0.20
preco_final = preco - desconto 

print(f'O produto possui {desconto:.2f}% de desconto, seu valor final é {preco_final:.2f} Reais')