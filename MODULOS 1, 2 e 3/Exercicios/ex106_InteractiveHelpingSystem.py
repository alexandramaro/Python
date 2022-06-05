""" Ex106: Faça um mini-sistema que utilize o Interactive Help do Python. O utilizador vai
digitar o comando e o manual vai aparecer. Quando o utilizador escrever a palavra 'FIM',:keywordprograma encerra.
OBS: usar cores."""
from time import sleep
c = ('\033[m',          # 0 → sem cor
     '\033[041m',       # 1 → fundo vermelho
     '\033[042m',       # 2 → fundo verde
     '\033[043m',       # 3 → fundo amarelo
     '\033[044m',       # 4 → fundo azul
     '\033[045m',       # 5 → fundo roxo
     '\033[7m')       # 6 → fundo branco


def ajuda(com):
    título(f'Acedendo o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
