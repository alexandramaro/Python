""" 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maio e o menor valores lidos.
O programa deve perguntar ao utilizador se ele quer ou não continuar a digitar valores."""

resp = 'S'
media = soma = quant = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S|N] ')).strip()[0].upper()
media = soma / quant
print(f'Você digitou {num} números e a média foi {media}\n'
      f'O maio valor foi {maior} e o menor foi {menor}')
