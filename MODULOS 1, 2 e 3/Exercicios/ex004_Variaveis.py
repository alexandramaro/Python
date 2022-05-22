a = input('Digite algo: ')  # retorna sempre string se não mencionar o tipo
print('O tipo primitivo desse valor é ', type(a))  # ou com format:
print(f'O tipo primitivo desse valor é {type(a)}')
print('Só tem espaços em branco?', a.isspace())  # ou com format:
print(f'Só tem espaços em branco? {a.isspace()}')
print('É um número?', a.isnumeric())  # ou com format:
print(f'É um número? {a.isnumeric()}')
print('É alfabético?', a.isalpha())  # ou com format:
print(f'É alfabético? {a.isalpha()}')
print('É alfanumérico?', a.isalnum())  # ou com format:
print(f'É alfanumérico? {a.isalnum()}')
print('É todo em maiúsculo?', a.isupper())  # ou com format:
print(f'É todo em maiúsculo? {a.isupper()}')
print('É todo em minúsculo?', a.islower())  # ou:
print(f'É todo em minúsculo? {a.islower()}')
print('É capitalizada?', a.istitle())  # ou:
print(f'É capitalizada? {a.istitle()}')


