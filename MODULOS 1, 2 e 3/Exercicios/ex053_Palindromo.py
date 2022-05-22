""" Crie um programa que leia uma frase e diga se ela é um políndromo,
desconsidrando os espaços.
Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA"""

frase = str(input('Digite uma frase: ')).strip().upper()  # Retira espaços antes e depois e passa a caixa alta
palavras = frase.split()  # separa as palavras numa lista
junto = ''.join(palavras)  # junta as palavras sem espaços
"""inverso = ''
   for letra in range(len(junto)-1, -1, -1):
        inverso += junto[letra]"""
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
