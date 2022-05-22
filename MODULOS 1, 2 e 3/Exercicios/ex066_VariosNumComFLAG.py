"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai
parar quando o utilizador digitar 999, que é a condição de paragem:
No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)"""

soma = cont = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont +=1
    soma += num
print(f'A soma dos {cont} valores foi {soma}.')
