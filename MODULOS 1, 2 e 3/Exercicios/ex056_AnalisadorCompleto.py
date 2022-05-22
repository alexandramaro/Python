""" Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
 A média de idade do grupo
 Qual é o nome do homem mais velho
 Quantas mulheres têm menos de 20 anos"""

somaidade = 0
mediaidade = 0
maioridadehomem= 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print(f'----- {p} PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M|F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idades do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulhere(s) com menos de 20 anos.')
