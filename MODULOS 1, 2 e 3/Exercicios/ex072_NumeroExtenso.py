""" ex072: Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extensão, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso."""

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezasseis', 'dezassete', 'dezoito',
        'dezanove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'O número digitado foi {cont[num]}.')

resp = ' '
while resp not in 'SN':
    resp = str(input('Quer continuar? [S|N] ')).strip().upper()[0]
    if resp == 'N':
        break
