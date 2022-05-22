""" 067 - Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
digitado pelo utilizador. O programa será interrompido quando o número solicitado
for negativo"""

while True:
    n = int(input('Informe um número para ver a tabuada: '))
    print('_' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:^3}= {n * c}')
    print('_' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
