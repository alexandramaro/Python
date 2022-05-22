galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print('-=' * 30)
for pessoa in galera:
    print(pessoa)
print('-=' * 30)
for pessoa in galera:
    print(pessoa[0])
print('\033[32m-=\033[m' * 30)
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
