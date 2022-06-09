def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()     # corrige "," e retira os espaços
        if entrada.isalpha() or entrada == '':
            print(f'\033[031mERRO: \"{entrada}\" é um preço válido!\033[m')
        else:
            valido = True
            return float(entrada)
