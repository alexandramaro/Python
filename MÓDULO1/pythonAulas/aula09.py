frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))

print(len(frase))
frase2 = ' Curso em Vídeo Python '
print(len(frase2.strip()))

print(frase.replace('Python', 'Android'))
print(frase)
frase3 = frase.replace('Python', 'Android')
print(frase3)

print('Curso' in frase)
print(frase.find('Curso'))  # posição 0
print(frase.find('Vídeo'))  # posição 9
print(frase.find('vídeo'))  # não existe (-1)
print(frase.lower().find('vídeo'))

print(frase.split())

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2])
print(dividido[2][3])
