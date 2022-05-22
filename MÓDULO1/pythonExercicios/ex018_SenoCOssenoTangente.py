# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do Seno, Cosseno e Tangente desse ângulo.

from math import sin, cos, tan, radians
ang = float (input('Valor do ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O ângulo {ang:.0f}º \ntem o Seno = {sen:.2f}, \nO Cosseno = {cos:.2f} \nA Tangente = {tan:.2f}')
