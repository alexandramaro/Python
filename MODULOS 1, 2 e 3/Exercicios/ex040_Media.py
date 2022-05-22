""" Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: REPROVADO
Média ENTRE 5.0 E 6.9: RECUPERAÇÃO
Média 7.0 ou superior: APROVADO"""

nota1 = float(input('Digite 1ª nota: '))
nota2 = float(input('Digite 2ª nota: '))
media = (nota1 + nota2) / 2
if 7 > media <= 5:
    print(f'Com as notas {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}.\nO aluno está RECUPERAÇÃO')
elif media < 5:
    print(f'Com as notas {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}.\nO aluno está REPROVADO')
else:
    print(f'Com as notas {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}.\nO aluno está APROVADO')
