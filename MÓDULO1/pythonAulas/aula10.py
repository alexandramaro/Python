# CONDIÇÃO:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')
print('--FIM--')


# CONDIÇÃO SIMPLIFICADA:
tempo = int(input('Quantos anos tem seu carro? '))
print('Carro Novo' if tempo <= 3 else 'Carro Velho')
print('--FIM--')
