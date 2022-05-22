# Faça um programa que leia três números e mostre qual o MAIOR e o MENOR.

n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
n3 = int(input('Digite terceiro número: '))
# Verificar o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificar o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
