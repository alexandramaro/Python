""" Aprimorar ex086, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma de todos os valores da 3ª coluna.
c) O maior valor da 2ª linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares = somacoluna = maior = 0
# Loops para colocar os valores dentro da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)

# Loops para mostrar a estrutura (3x3) na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # :^5 → 5 casas décimais, centralizado
# a) A soma de todos os valores pares digitados.
        if matriz[linha][coluna] % 2 == 0:              # se na matriz(l,c) o número for par,
            somapares += matriz[linha][coluna]          # então somar os pares
    print()
print('-=' * 30)
print(f'A soma dos valores pares difitados é {somapares}.')

# b) A soma de todos os valores da 3ª coluna.
for linha in range(0, 3):                       # só pecisa de loop para linha, porque a coluna é sempre [2]
    somacoluna += matriz[linha][2]              # soma tudo da 3ª coluna ([2])
print(f'A soma dos valores da 3ª coluna é {somacoluna}.')

# c) O maior valor da 2ª linha.
for coluna in range(0, 3):                      # só pecisa de loop para linha, porque a coluna é sempre [2]
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
    """elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]"""
print(f'O maior valor da segunda linha é {maior}')
