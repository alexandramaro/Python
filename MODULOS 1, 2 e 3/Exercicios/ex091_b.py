""" ex091 Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados num dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado.
Outra maneira:"""

from random import randint
from time import sleep
resutados = dict()
jogadores = list()
print('Valores sorteados:')
for c in range(0, 4):
    n = randint(1, 6)
    resutados['Jogador ' + str(c+1)] = n
    jogadores.append(n)
    sleep(1)
    print(f'O {"Jogador " + str(c+1)} tirou {n}')
jogadores.sort(reverse=True)
jogar = 't'
sleep(0.5)
print('Ranking dos jogadores:')
for indice in range(0, 4):
    sleep(1)
    print(f'{indice + 1}º Lugar: ', end='')
    for k, v in resutados.items():
        if v == jogadores[indice] and jogar != k:
            print(k, 'com', v)
            jogar = k
            break
