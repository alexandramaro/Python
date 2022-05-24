""" ex090 Faça um programa que leia nome e média de um aluno, guardando também
a situação (aprovado, reprovado, recuperação) num dicionário.
No final, mostre o conteúdo da estrutura na tela."""

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['média'] >= 10:
    aluno['situação'] = 'Aprovado'
elif 9.5 <= aluno['média'] < 10:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'    - {k} é igual a \033[34m{v}\033[m')
