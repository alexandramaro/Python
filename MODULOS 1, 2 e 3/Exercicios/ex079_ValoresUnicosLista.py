""" ex079: Crie um programa onde o utilizador possa digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente."""

numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Quer continuar? [S|N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou os valores: {numeros}')
# ou:
print(f'Valores ordenados: {sorted(numeros)}')
# ou:
numeros.sort()
print(f'Você digitou os valores: {numeros}')

