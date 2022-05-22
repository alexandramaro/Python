# Desenvolve um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando 0,50 € por km para viagens até 200Km
# e 0,45 € para viagens mais longas.

dist = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a começar uma viagem de {dist:.2f}Km.')
''' if dist <= 200:
        preço = dist * 0.50
    else:
        preço = dist * 0.45 '''
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print(f'O preço da passagem é de {preço:.2f}€')
