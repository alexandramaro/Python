""" 058 - Melhor o jogo do DESAFIO 028 onde o computador vai pensar em um número entre 0 e 10.
 Só que agora, o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
 foram necessários para vencer."""
"""from random import randint
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
    print(f'Perdeu! Eu pensei no número {comp} e não no número {jog}')"""

from random import randint
computador = randint(0, 10)  # Computador sorteia número
print('Sou o seu computador... \nAcabei de pensar num número de 0 a 10.'
      '\n Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Para cima... Tente mais uma vez.')
        else:
            print('Para baixo... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
