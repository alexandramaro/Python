""" ex081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) quantos números foram digitados.
b) A lista de valores ordenada de forma decrescente.
c) Se o valor 5 foi digitado e está ou não na lista."""

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S|N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
# a) quantos números foram digitados.
print(f'Você digitou {len(valores)} elementos.')
# b) A lista de valores ordenada de forma decrescente.
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente: {valores}')
# c) Se o valor 5 foi digitado e está ou não na lista.
if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 NÃO faz parte da lista.')
