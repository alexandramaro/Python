""" ex084: Faça um programa que leia nome e peso da várias pessoas, guardando tudo em uma lista.
No final mostre:
a) Quantas pessoas foram registadas?
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves."""

temp = []  # lista temporária que guarda os dados temporáriamente antes de ir para a lista principal.
princ = []  #  lista principal
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S|N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
# a)  Quantas pessoas foram registadas?
print(f'Ao todo, você registou {len(princ)} pessoas.')
# b) Uma listagem com as pessoas mais pesadas.
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for pessoa in princ:
    if pessoa[1] == mai:
        print(f'{pessoa[0]}', end='')
print()
# c) Uma listagem com as pessoas mais leves.
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for pessoa in princ:
    if pessoa[1] == men:
        print(f'{pessoa[0]}', end='')
