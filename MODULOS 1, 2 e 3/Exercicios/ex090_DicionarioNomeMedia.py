""" ex090 Faça um programa que leia nome e média de um aluno, guardando também
a situação num dicionário. No final, mostre o conteúdo da estrutura na tela."""

aluno = dict()
alunos = list()
for count in range(0, 3):
    aluno['nome'] = str(input('Nome do aluno: '))
    aluno['média'] = float(input('Média do aluno: '))
    alunos.append(aluno.copy())
for a in aluno:
    for k, v in alunos:
        print(f'O aluno {k} teve média de {v}]}')
