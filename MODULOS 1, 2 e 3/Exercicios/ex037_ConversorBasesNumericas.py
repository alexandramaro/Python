""" Escreva um programa que leia um número inteiro qualquer e
peça para o utilizador escolher qual será a base de conversão:
 1 para binário
 2 para octal
 3 para hexadecimal"""

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n'
      '[ 1 ] converter para BINÁRIO\n'  # 0b...
      '[ 2 ] converter para OCTAL\n'  # 0o...
      '[ 3 ] converter para HEXADECIMAL')  # 0x...
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')  # [2:] para não aparecer os 2 1º digitos (0b,0o,0x
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')  # [2:] para não aparecer os 2 1º digitos (0b,0o,0x
elif opcao == 3:
    print(f'{num}  convertido para HEXADECIMAL é igual a {hex(num)[2:]}')  # [2:] para não aparecer os 2 1º digitos
                                                                           # (0b,0o,0x
else:
    print('Opção inválida! Tente novamente.')
