# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro: Ana
# último: Souza

n = str(input('Digite nome completo: ')).strip()
nome = n.split()
print(nome)
print(nome[0])
print(('Muito prazer em te conhecer!'))
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[len(nome)-1]}')
