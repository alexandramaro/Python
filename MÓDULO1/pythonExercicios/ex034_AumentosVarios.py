# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a 1.250,00€, calcule aumento de 10%.
# Para salários inferiores ou iguais a 1.250,00€, calcule aumento de 15%.

sal = float(input('Qual o salário do funcionário? € '))
if sal <= 1250:
    novoSal = sal + (sal * 15 / 100)
else:
    novoSal = sal + (sal * 10 / 100)
print(f'Quem ganhava {sal:.2f} € passa a ganhar {novoSal:.2f} €')