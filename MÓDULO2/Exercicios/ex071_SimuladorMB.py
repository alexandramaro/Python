""" 070 - Crie um programa que simule o funcionamento de um Multibanco.
No início pergunte ao utilizador qual será o valor a ser levantado e o programa vai
informar quantas notas de cada valor serão entregues.
OBS: Considere que o MB tem notas de 50€, 20€, 10€ e 5€."""

print('\033[34m-=\033[m'*30)
print('{:^60}' .format('\033[33m BANCO ALEXANDRA \033[m'))  # centralizado
print('\033[34m-=\033[m'*30)
valor = int(input('Que valor quer levantar? €'))
total = valor
nota = 50
totnota = 0
while True:
    if total >= nota:
        total -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'Total de {totnota} notas de {nota}€.')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        totnota = 0
        if total == 0:
            break
print('\033[34m-=\033[m'*30)
print('{:^60}' .format('\033[32m Volte sempre ao BANCO ALEXANDRA! \033[m'))  # centralizado
