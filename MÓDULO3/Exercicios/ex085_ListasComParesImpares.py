"""Crie um programa onde o utilizador possa escrever 7 números inteiros e registe-os
numa lista única que mantenha separados os valores pares e ímpares.
No final mostre os valores pares e os ímpares em ordem crescente."""

num = [[], []]  # uma lista com 2 listas internas, para par e ímpar
valor = 0
for count in range(1, 8):
    valor = int(input(f'Digite o {count}ª valor: '))
    if valor % 2 == 0:          # se o número for par
        num[0].append(valor)    # coloca na 1ª lista
    else:                       # se o número for ímpar
        num[1].append(valor)    # coloca na 2ª lista
print('-=' * 30)
print(f'\033[32mTodos\033[m os valores: \033[31m{num}\033[m')
num[0].sort()                   # coloca os números pares em ordem
num[1].sort()                   # coloca os números ímpares em ordem
print(f'Os valores \033[32mpares\033[m digitados foram: \033[34m{num[0]}\033[m\n'
      f'Os valores \033[32mímpares\033[m digitados foram: \033[34m{num[1]}\033[m')
