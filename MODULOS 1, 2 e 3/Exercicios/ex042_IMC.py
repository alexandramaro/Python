""" Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: abaixo do Peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
Acima de 40: Obesidade mórbida"""

peso = float(input('Qual o seu peso? (Kg) '))
alt = float(input('Qual a sua altura? (m) '))
imc = peso / (alt ** 2)  # peso a dividir por altura ao quadrado
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Está ABAIXO DO PESO normal')
elif 18.5 <= imc  < 25:
    print('PARABÉNS! Está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Está em SOBREPESO')
elif 30 <= imc < 40:
    print('Está em OBESIDADE, cuidado!')
else:
    print('Está em  OBESIDADE MÓRBIDA, cuidado!')
