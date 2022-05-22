teste = list()
teste.append('Alexandra')
teste.append(43)
print(teste)
print()
galera = list()
galera.append(teste)  # Lista dentro de outra Lista, mas substitui as 2 listas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)  # Lista dentro de outra Lista, mas substitui as 2 listas
print(galera)

#  ---------------------------------------------

teste = list()
teste.append('Alexandra')
teste.append(43)
print('-=' * 30)
galera = list()
galera.append(teste[:])  # Lista dentro de outra Lista, apenas substitui na 2ª lista
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])  # Lista dentro de outra Lista, apenas substitui na 2ª lista
print(galera)
