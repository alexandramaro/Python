# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar 7,00€ por cada Km acima do limite.

veloc = float(input('Qual é a velocidade atual do carro: '))

if veloc > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (veloc -80) * 7
    print(f'Você deve pagar uma multa de {multa:.2f}€')
else:
    print('Tenha um bom dia! Conduza com segurança!')
