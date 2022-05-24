""" ex092 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
registe-os (com idade) num dicionário. Se a CPTS for difernete de ZERO, o dicionário
receberá também o ano de contratação. Calcule e acrescente, além da idade, com quantos
anos a pessoa se vai aposentar."""

from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc     # → para calcular a idade
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: €'))
    dados['reforma'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print(dados)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k}: {v}')
