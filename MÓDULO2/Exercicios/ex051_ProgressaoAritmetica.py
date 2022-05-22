""" Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética).
No final, mostre os 10 primeiros termos dessa progressão."""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimoTermo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimoTermo + razao, razao):
    print(f'{c}', end=' → ')
print('ACABOU')

