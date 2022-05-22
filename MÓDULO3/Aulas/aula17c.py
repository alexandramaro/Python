valores = list()
for count in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição \033[34m{c}\033[m encontrei o valor \033[32m{v}\033[m!')
print('Cheguei ao final da lista!')