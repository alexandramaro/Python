# O mesmo professor do desafio anterior, quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Digite o nome do aluno 1: '))
n2 = str(input('Digite o nome do aluno 2: '))
n3 = str(input('Digite o nome do aluno 3: '))
n4 = str(input('Digite o nome do aluno 4: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'O nome escolhido foi: {lista}')
