""" ex098 Faça um programa que tenha uma função chamada contador(), que receba
três parâmetros: início, fim e passo e realize a contagem.
O programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1.
b) De 10 até 0, de 2 em 2.
c) Uma contagem personalizada."""

from time import sleep


def contador(inicio, fim, passo):
    # se passo 0 ou negativo
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    # Se o início for menor que o fim
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('FIM!')
    # Se o início for maior que o fim
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('FIM!')


# Programa Principal
# a) De 1 até 10, de 1 em 1.
contador(1, 10, 1)
# b) De 10 até 0, de 2 em 2.
contador(10, 0, 2)
# c) Uma contagem personalizada.
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fin = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fin, pas)
