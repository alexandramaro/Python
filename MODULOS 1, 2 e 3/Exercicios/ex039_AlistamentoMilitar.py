""" Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
Se ele ainda vai se alistar ao serviço militar.
Se é a hora de se alistar
Se já passou o tempo de alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou o prazo"""

from datetime import date
atual = date.today().year
nasc = int(input('Em que ano nasceu? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('Está na hora de se alistar! IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento!')
    print(f'Seu alistamento será em {ano}')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Já deveria ter se alistado há {saldo} ano(s).')
    print(f'Seu alistamento foi em {ano}')
    