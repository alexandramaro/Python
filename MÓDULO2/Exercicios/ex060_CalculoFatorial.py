""" 060 - Faça um programa que leia um número qualquer e mostre o seu fatorial.
    Ex: fatorial de 5 = 5x4x3x2x1=120"""

from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')
