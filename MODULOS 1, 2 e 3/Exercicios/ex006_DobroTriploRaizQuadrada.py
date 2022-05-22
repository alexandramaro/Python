n = int(input('Digite um número: '))
print(f'O dobro de {n} é {n * 2}')
print(f'O triplo de {n} é {n * 3}')
print(f'A raíz quadrada de {n} é {n ** (1 / 2):.2f}\n')
# ou
print(f'O dobro de {n} é {n * 2}. \nO triplo de {n} é {n * 3}. \nA raíz quadrada de {n} é {pow(n, (1/2)):.2f}.')
