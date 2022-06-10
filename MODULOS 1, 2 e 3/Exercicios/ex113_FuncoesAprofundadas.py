""" ex113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
possibilidade da digitação d um número de tipo inválido. Aproveite e crie também uma
função leiaFloat() com a mesma funcionalidade."""


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mUtilizador não digitou valor.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: Digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print(f'\033[31mUtilizador não digitou valor.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')
