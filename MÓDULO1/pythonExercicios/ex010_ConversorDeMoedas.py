real = float(input('Quanto dinheiro tem na carteira?: R$'))
print('Com R${:.2f}, pode comprar US${:.2f}'.format(real, real/3.27))
print(f'Com R${real:.2f}, pode comprar US${real/3.27:.2f}')
