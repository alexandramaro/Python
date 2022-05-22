""" ex078: Faça um programa que leia 5 valores e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respetivas
posições na lista."""

listanum = []
maior = menor = 0
for count in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {count}: ')))
    if count == 0:
        maior = menor = listanum[count]
    else:
        if listanum[count] > maior:
            maior = listanum[count]
        if listanum[count] < menor:
            menor = listanum[count]
print('\033[35m=-\033[m' * 30)
print(f'Você digitou os valores: {listanum}')
print(f'O \033[31mmaior\033[m valor digitado foi: \033[31m{maior}\033[m, na(s) posição(ões) ', end='')
for index, valores in enumerate(listanum):
    if valores == maior:
        print(f'{index}...', end='')
print(f'\nO \033[32mmenor\033[m valor digitado foi: \033[32m{menor}\033[m, na(s) posição(ões) ', end='')
for index, valores in enumerate(listanum):
    if valores == menor:
        print(f'{index}...', end='')