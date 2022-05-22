""" Crie um programa que faça uma matriz de dimensão 3x3 e preencha com valores
lidos do teclado. No final, mostre a matriz na tela, com a formatação correta."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Loops para colocar os valores dentro da matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-=' * 30)

# Loops para mostrar a estrutura (3x3) na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')  # :^5 → 5 casas décimais, centralizado
    print()
