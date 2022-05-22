import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))  # arredonda para cima
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))  # arredonda para baixo
print(f'A raiz de {num} é igual a {raiz}')
print(f'A raiz de {num} é igual a {raiz :.2f}')
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')   # arredonda para cima
print(f'A raiz de {num} é igual a {math.floor(raiz)}')   # arredonda para baixo
