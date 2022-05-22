# lanche = ('tupla') [lista] {dicionário}
# lanche = ('Hambúrguer', 'Sumo', 'Pizza', 'Pudim') → pode tirar os parentises
#       TUPLAS SÃO IMUTÁVEIS!
lanche = 'Hambúrguer', 'Sumo', 'Pizza', 'Pudim'
"""print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(lanche)"""

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra Caramba!')

print('-=' * 20)
print(len(lanche))
print('-=' * 20)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra Caramba!')

print('-=' * 20)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra Caramba!')

print('-=' * 20)

lanche = ('Hambúrguer', 'Sumo', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche))
print(lanche)
