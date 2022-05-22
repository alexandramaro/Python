larg = float(input('Qual a largura da parede?: '))
alt = float(input('Qual a altura da parede?: '))
area = larg * alt
print(f'A parede tem a dimensão de {larg}x{alt} a área é: {area}m². \n')  # m² == Alt+0178 m
tinta = area / 2
print(f'Para pintar essa parede, precisa de {tinta}l de tinta.')
