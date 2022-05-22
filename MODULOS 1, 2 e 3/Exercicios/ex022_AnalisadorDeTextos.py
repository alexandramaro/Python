# Crie um programa que leia o nome completo de uma pessoa e mostre:
nome = str(input('Digite o nome completo: ')).strip()  # já corta a string e os espaços são excluídos
print('Analisando o nome...')

# O nome com todas as letras maiúsculas:
print(f'O nome em maiúsculas: {nome.upper()}')

# O nome com todas as letras minúsculas:
print(f'O nome em minúsculas: {nome.lower()}')

# Quantas letras ao todo (sem espaços)
print(f'O nome tem  {len(nome) - nome.count(" ")} letras')

# Quantas letras tem o primeiro nome?
print(f'O primeiro nome tem  {nome.find(" ")} letras')

#  Separar o nome:
separa = nome.split()
print(separa)
print(f'O primeiro nome é {separa[0]} e tem {len(separa[0])} letras')
