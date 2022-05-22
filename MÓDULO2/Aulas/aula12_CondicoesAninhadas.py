"""# ESTRUTURA CONDICIONAL SIMPLES:
nome = str(input('Qual é o seu nome? '))
if nome == 'Alexandra':
    print('Que nome bonito!')
print(f'Tenha um bom dia, {nome}!')

# ESTRUTURA CONDICIONAL COMPOSTA:
nome = str(input('Qual é o seu nome? '))
if nome == 'Alexandra':
    print('Que nome bonito!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')"""

# ESTRUTURA CONDICIONAL ANINHADA:
nome = str(input('Qual é o seu nome? '))
if nome == 'Alexandra':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum em Portugal.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:                                   # o else é opcional
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')
