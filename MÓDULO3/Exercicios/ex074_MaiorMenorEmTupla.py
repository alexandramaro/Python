""" ex074: Crie um programa que vai gerar 5 numeros aleatóreos e colocar numa tupla.
Depois disso, mostre a listagem de números gerados e indique também o menor e o
maior valor que estão na tupla."""

"""from random import randint
n = randint(1, 10)
print(f'Eu sorteei o valor {n}')"""

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for num in numeros:
    print(f'{num} ', end='')
print(f'\nO \033[31mmaior\033[m valor sorteado foi \033[34m{max(numeros)}\033[m')
print(f'O \033[31mmenor\033[m valor sorteado foi \033[34m{min(numeros)}\033[m')
