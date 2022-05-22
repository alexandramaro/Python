""" 070 - Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o utilizador quer ou não continuar. No final mostre:
a) Qual é o total gasto na compra.
b) Qtos produtos custam mais de 100€
c) Qual o nome do produto mais barato."""

print('-=' * 30)
print('{:-^40}'.format('LOJA SUPER BARATÃO'))
print('-=' * 30)
total = totcem = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = int(input('Preço: €'))
    cont += 1
# Qual é o total gasto na compra?
    total += preco
# Qtos produtos custam mais de 100€?
    if preco > 100:
        totcem +=1
# Qual o nome do produto mais barato?
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S|N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'\033[34mO total\033[m da compra foi \033[31m{total:10.2f}\033[m€\n'
      f'Existe(m) \033[31m{totcem}\033[m produto(s) \033[34mcustando mais de 100€\033[m.\n'
      f'O produto \033[34mmais barato\033[m foi \033[31m{barato}\033[m, que custa \033[31m{menor:.2f}\033[m€')
