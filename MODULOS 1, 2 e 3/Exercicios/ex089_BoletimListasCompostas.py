""" Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um e
permita que o utilizador possa mostrar as notas de cada aluno individualmente."""

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input('Quer continuar? [S|N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(ficha)
