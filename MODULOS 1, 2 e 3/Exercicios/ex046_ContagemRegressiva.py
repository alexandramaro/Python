""" Faça um programa que mostre na tela uma contagem regressiva para o estouro
de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre elas"""

from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print(f'BOOOM!!!')
sleep(1)
