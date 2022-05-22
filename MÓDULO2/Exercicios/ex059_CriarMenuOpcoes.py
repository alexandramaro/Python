""" 059 - Crie um programa que leia dois valores r mostre um menu na tela:
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso"""

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa ''')
    opcao = int(input('\033[31m>>>>>\033[m Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'\033[34mA soma entre {n1} e {n2} é {soma}\033[m')
    elif opcao == 2:
        produto = n1 * n2
        print(f'\033[34mO resultado entre {n1} e {n2} é {produto}\033[m')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\033[34mEntre {n1} e {n2} o maior valor é {maior}\033[m')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\033[34mFinalizando...\033[m')
    else:
        print('Opção inválida, tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
