""" ex093 Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de golos feitos em cada partida.
No final, tudo isso será guardado num dicionário, incluindo o total de golos feitos
durante o campeonato."""

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for count in range(0, tot):
    partidas.append(int(input(f'    Quantos golos na partida {count + 1}? ')))
jogador['golos'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
# print(partidas)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["golos"])} partidas.')
for indice, v in enumerate(jogador['golos']):
    print(f'    → Na partida {indice + 1}, fez {v} golos.')
print(f'Foi um total de {jogador["total"]} golos.')
