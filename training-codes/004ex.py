n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('\n A soma é {}, \n o produto é {} \n e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('\n A divisão inteira é {} \n e potencia é {}'.format(di, e))