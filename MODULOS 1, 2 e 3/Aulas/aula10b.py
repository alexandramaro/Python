n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A média foi {m}')
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi má! ESTUDE MAIS!')

# ESTRUTURA CONDICIONAL SIMPLIFICADA:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A média foi {m}')
print('Sua média foi boa! PARABÉNS!' if m>=6.0 else 'Sua média foi má! ESTUDE MAIS!')
