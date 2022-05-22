""" Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for impar,
desconsidere-o."""

soma = 0
count = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        count += 1
print(f'Você informou {count} números PARES e a soma foi {soma}')
