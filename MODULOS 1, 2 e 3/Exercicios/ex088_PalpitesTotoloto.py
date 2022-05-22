""" Faça um programa que ajude um jogador do Totoloto (Mega Sena), a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, registando tudo em uma lista composta."""

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print(f'{"JOGA NO TOTOLOTO":^30}')
print('-' * 30)
quant = int(input('Quantos jogos quer sortear? '))
tot = 1
while tot <= quant:
    count = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            count += 1
        if count >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
# aparece lista de jogos ordenados verticalmente
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice + 1}: {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
