# Escreva um programa que faça o computador "pensar" num número inteiro entre 0 e 5
# e peça para o utilizador tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o utilizador venceu ou perdeu.

from random import randint
from time import sleep
comp = randint(0, 5)  # Computador sorteia número
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jog = int(input('Adivinhe o número: '))  # Jogador tenta adivinhar número do computador
print('PROCESSANDO...')
sleep(2)
if jog == comp:
    print('Acertou! PARABÉNS!')
else:
    print(f'Perdeu! Eu pensei no número {comp} e não no número {jog}')

