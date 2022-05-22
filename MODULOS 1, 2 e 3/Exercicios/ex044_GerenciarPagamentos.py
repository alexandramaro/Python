"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
à vista dinheiro/cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros"""

print(f'{" LOJAS ALEXANDRA ":=^40}')
preco = float(input('Preço das compras: € '))
print('FORMAS DE PAGAMENTO'
      '[ 1 ] à vista dinheiro/cheque'
      '[ 2 ] à vista cartão'
      '[ 3 ] 2x no cartão'
      '[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print(f'Sua compra será parelada em 2x de {parcela:.2f} €, SEM JUROS.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parelada em {totparc}x de {parcela:.2f} €, COM JUROS')
else:
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
print(f'Sua compra de {preco:.2f} €, vai custar {total:.2f} € no final.')



