""" ex091 Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados num dicionário. No final, coloque esse dicionário
em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'\033[32m{k}\033[m tirou \033[34m{v}\033[m no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # colocar em ordem decrescente
print(ranking)
sleep(1)
# ------------------------------
print('\033[33m-=\033[m' * 30)
print('  == RANKING DOS JOGADORES ==')
sleep(1)
for indice, valor in enumerate(ranking):
    print(f'\033[32m{indice + 1}º\033[m lugar: {valor[0]} com \033[34m{valor[1]}\033[m.')
    sleep(1)
