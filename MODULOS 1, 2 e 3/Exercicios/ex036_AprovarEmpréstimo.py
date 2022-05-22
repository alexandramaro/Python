""" Escreva um programa para aprovar o empréstio bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário,
ou então o empréstimo será negado."""

casa = float(input('Valor da casa: €'))
salario = float(input('Salário do comprador: €'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para pagar uma casa de {casa:.2f}€ em {anos}, a prestação será de {prestacao:.2f}€.')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
