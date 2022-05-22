preço = float(input('Qual é o preço do produto?: €'))
novo = preço - (preço * 5 / 100)
print(f'O produto que custava €{preço:.2f}, na promoção com 5% de desconto vai custar €{novo:.2f}')
