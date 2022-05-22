""" ex077: Crie um programa que tenha uma tupla com várias palavras (sem acentos).
Depois disso, deve mostrar para cada palavra, quais são as suas vogais."""

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra \033[35m{p.upper()}\033[m temos vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            