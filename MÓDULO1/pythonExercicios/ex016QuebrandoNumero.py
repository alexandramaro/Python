# Crie um programa q leia 1 número real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# EX: 6.127 a parte inteira é 6
from math import trunc
num = float(input('Digite um número: '))
print(f'A porção inteira de {num} é {trunc(num)}')
# ou
print(f'A porção inteira de {num} é {int(num)}')
