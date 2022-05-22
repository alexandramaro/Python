""" ex082: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
impares digitados respectivamente.
Ao final mostre o conteúdo das três listas geradas."""

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S|N] '))
    if resp in 'Nn':
        break
for indice, valor in enumerate(num):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print('-=' * 30)
print(f'A lista completa é {sorted(num)}.')
print(f'A lista de pares é {sorted(pares)}.')
print(f'A lista de ímpares é {sorted(impares)}.')

