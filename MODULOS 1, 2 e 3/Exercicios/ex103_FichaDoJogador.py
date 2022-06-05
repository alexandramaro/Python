""" Ex103: Crie um programa que tenha uma função chamada ficha() que receba dois parâmetros
opcionais: o nome de um jogador e quantos golos ele marcou.
O programa deverá conseguir mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente."""


def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} golo(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de golos: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
