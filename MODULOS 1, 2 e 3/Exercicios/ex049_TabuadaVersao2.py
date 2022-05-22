""" Refaça o DESAFIO 009, mostrando a tabuada de um número que o utilizador
escolher, só que agora usando o laço for."""

n = int(input('Informe um número para ver a tabuada: '))
print('_' * 12)
for c in range(1, 11):
    print(f'{n} x {c:^3}= {n * c}')
print('_' * 12)
