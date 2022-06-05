""" Ex104: Crie um programa que tenha uma função leiaInt(), que vai funcionar de forma
semelhante à função input do Python, porém fazendo a validação para aceitar apenas
um valor numérico.
Ex: n = leiaInt('Digite um nº: ')"""


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[031mERRO! Escreva um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa Principal
n = leiaInt('Escreva um número:')  # n = int(input('Escreva um número:'))
print(f'Você acabou de escrever o número {n}.')
