""" ex095 Aprimore o ex093, para que funcione com vários jogadores, incluindo um sistema
de visualização de detalhes de aproveitamento de cada jodador."""

equipa = list()
jogador = dict()
partidas = list()
# Ler Dados
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for count in range(0, tot):
        partidas.append(int(input(f'    Quantos golos na partida {count + 1}? ')))
    jogador['golos'] = partidas[:]
    jogador['total'] = sum(partidas)
    equipa.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S|N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
# Mostrar resultados
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(equipa):
    print(f'{k:>3} ', end='')
    for dado in v.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 40)
# Escolher os dados a ver na tela
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(equipa):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {equipa[busca]["nome"]}: ')
        for indice, gols in enumerate(equipa[busca]['golos']):
            print(f'    No jogo {indice + 1} fez {gols} golos.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
