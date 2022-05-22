# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um trinângulo rectângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

catOpo = float(input('Valor do cateto oposto: '))
catAdj = float(input('Valor do cateto adjacente: '))
print(f'O comprimento da hipotenusa é de: {hypot(catOpo, catAdj):.2f}')
# forma matemática:
hi = (catOpo ** 2 + catAdj ** 2) ** (1 / 2)
print(f'O comprimento da hipotenusa é de: {hi:.2f}')
