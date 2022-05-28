""" ex096 Faça um programa que tenha uma função chamada área(), que receba
as dimensões de um terreno retangular (largura e comprimento) e mostre a
área do terreno."""


def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg:.2f}m x {comp:.2f}m é de {a:.2f}m².')


print('Controle de Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)
