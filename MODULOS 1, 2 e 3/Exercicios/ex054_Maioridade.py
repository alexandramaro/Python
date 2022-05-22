""" Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade
e quantas já são maiores."""

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior +=1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas \033[32mmaiores\033[m de idade \n'
      f'e {totmenor} pessoas \033[31mmenores\033[m de idade')
