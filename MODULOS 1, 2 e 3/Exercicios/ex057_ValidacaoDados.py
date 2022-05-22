""" 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input('Informe o seu sexo: [M|F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, por favor informe o seu sexo: [M|F] ')).strip().upper()[0]
print(f'Sexo {sexo} registado com sucesso.')
