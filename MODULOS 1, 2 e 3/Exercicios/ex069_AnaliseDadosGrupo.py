""" 069 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o utilizador quer ou não continuar. No final mostre:
a) qtas pessoas tem mais de 18 anos.
b) qtos homens foram cadastrados
c) qtas mulhers tem menos de 20 anos."""

tot18 = totH = totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M|F] ')).strip().upper()[0]
# qtas pessoas tem mais de 18 anos?
    if idade >= 18:
        tot18 += 1
# qtos homens foram cadastrados?
    if sexo == 'M':
        totH += 1
#qtas mulhers tem menos de 20 anos?
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S|N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos : {tot18}\n'
      f'Total de homens cadastrados: {totH}\n'
      f'Total de mulheres cadastradas com menos de 20 anos: {totM20}')
