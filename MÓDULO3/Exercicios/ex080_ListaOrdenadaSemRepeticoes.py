""" ex080: Crie um programa onde o utilizador possa digitar 5 valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela."""

lista = list()
for count in range(0, 5):
    num = int(input('Digite um valor: '))
    if count == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista...')
    # elif num > lista[-1]:  # se o num for maior que o último elemento da lista
        # lista.append(num)
    else:
        pos = 0
        while pos < len(lista):  # enquanto a posição for menor que o comprimento da lista
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
