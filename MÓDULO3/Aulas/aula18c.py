galera = list()
dado = list()
totmaior = totmenor = 0
for contador in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é \033[32mmaior\033[m de idade.')
        totmaior += 1
    else:
        print(f'{pessoa[0]} é \033[34mmenor\033[m de idade.')
        totmenor += 1
print(f'Temos {totmaior} \033[32mmaiores\033[m e {totmenor} \033[34mmenores\033[m de idade.')