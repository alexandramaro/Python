valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
"""for v in valores:
    print(f'{v}...', end='')"""
for c, v in enumerate(valores):
    print(f'Na posição \033[34m{c}\033[m encontrei o valor \033[32m{v}\033[m!')
print('Cheguei ao final da lista!')
