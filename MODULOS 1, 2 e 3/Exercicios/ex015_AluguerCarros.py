dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km percorridos? '))
total = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de {total:.2f}€')
