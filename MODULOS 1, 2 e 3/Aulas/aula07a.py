n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {}, a divisão é {:.3f}'.format(s, m, d), end=', ')
print(f'a divisão inteira é {di}, a potência é {e}')
print(f'A soma é {s}, o produto é {m}, a divisão é {d}')
print('A divisão inteira é {}, a potência é {}'.format(di, e))
