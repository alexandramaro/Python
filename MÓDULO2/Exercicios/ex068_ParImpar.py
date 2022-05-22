""" 068 - Faça um programa que jogue PAR ou IMPAR com o computador. O jogo será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no
final do jogo."""

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P|I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end=''
          f'DEU PAR ' if total % 2 == 0 else 'DEU IMPAR ')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
