# Crie um programa que leia o nome de uma pessoa e
# diga se ela tem "Silva"

nome = str(input('Digite um nome: ')).strip()
print(f'O nome tem Silva? {"SILVA" in nome.upper()}')
