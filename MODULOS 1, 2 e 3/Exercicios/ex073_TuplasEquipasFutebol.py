""" ex073: Crie uma tupla totalmente preenchida com os 20 primeiros classificados
na Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. depois mostre:
a) Apenas os 5 primeiros classificados.
b) Os últimos 4 classificados.
c) Uma lista com as equipas em ordem alfabética
d) Em que posição na tabela está a equipa do Chapecoense?"""

equipas = ('Corinthians', 'Palmeiras', 'Santos',  'Grêmio',
               'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
               'Atlético Mineiro', 'Botafogo', 'Atlético-PR', 'Bahia',
               'São Paulo', 'Fluminense', 'Sport Recife',
                'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('\033[35m-=\033[m' * 75)
print(f'Lista das equipas: {equipas}')
"""for equipa in equipas:
    print(equipa)"""
print('\033[35m-=\033[m' * 75)
# a) Apenas os 5 primeiros classificados.
print(f'As 5 primeiras equipas são: \033[34m{equipas[0:5]}\033[m')
print('\033[33m-=\033[m' * 45)
# b) Os últimos 4 classificados.
print(f'Os últimos 4 classificados são: \033[32m{equipas[-4:]}\033[m')
print('\033[33m-=\033[m' * 45)
#c) Uma lista com as equipas em ordem alfabética
print(f'Equipas na ordem alfabética: \033[32m{sorted(equipas)}\033[m')
print('\033[33m-=\033[m' * 75)
# d) Em que posição na tabela está a equipa do Chapecoense?
print(f'Chapecoense está na \033[32m{equipas.index("Chapecoense")+1}ª\033[m posição.')
print('\033[33m-=\033[m' * 16)
