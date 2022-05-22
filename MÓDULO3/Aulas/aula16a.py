a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(f'\033[34md = b + a → \033[31m{d}')
print(f'\033[34mc = a + b → \033[31m{c}')
print(f'\033[34mComprimento de c → \033[31m{len(c)}')
print(f'\033[34mQuantas vezes aparece o 5 → \033[31m{c.count(5)}')
print(d)
print(f'\033[34mEm que posição está o 8? → \033[31m{d.index(8)}')
print(f'\033[34mEm que posição está o 4? → \033[31m{d.index(4)}')
print(f'\033[34mEm que posição está o 2? → \033[31m{d.index(5, 1)}')


