""" ex094 Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados de cada pessoa num dicionário e todos os dicionários numa lista. No final, mostre:
a) Quantas pessoas foram registadas?
b) A média da idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da média."""

galera = list()
pessoa = dict()
soma = média = 0    # b) A média da idade do grupo.
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M|F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']     # b) A média da idade do grupo.
    galera.append(pessoa.copy())  # galera recebe cópia de pessoa
    while True:
        resp = str(input('Quer continuar? [S|N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print(galera)
print('-=' * 30)
# a) Quantas pessoas foram registadas?
print(f'A) Ao todo temos {len(galera)} pessoas registadas.')
# b) A média da idade do grupo.
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
# c) Uma lista com todas as mulheres.
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':    # if p['sexo] in 'Ff'
        print(f'{p["nome"]} ', end='')
print()
# d) Uma lista com todas as pessoas com idade acima da média.
print('D) Lista das pessoas que estão acima da média de idades: ')
for p in galera:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
