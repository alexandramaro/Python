"""cont = 1
while cont <= 10:
    print(cont, end='→ ')
    cont += 1
print('Acabou!')"""

""" LOOP INFINITO
cont = 1
while True:
    print(cont, end='→ ')
    cont += 1
print('Acabou!')"""

num = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
print(f'A soma vale {soma}')
