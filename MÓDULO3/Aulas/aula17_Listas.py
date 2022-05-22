num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.pop()
print(num)
num.pop(2)
print(num)
num.insert(2, 2)
print(num)
num.remove(2)  # remove primeiro elemento com valor 2
print(num)
if 4 in num:
    num.pop(4)
else:
    print('Não achei o número 4.')
print(num)
