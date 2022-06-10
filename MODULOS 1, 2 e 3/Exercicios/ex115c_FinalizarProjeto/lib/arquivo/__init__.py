from ex115b_Arquivos.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')        # rt → read text
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')       # wt → write text   + → cria ficheiro
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS REGISTADAS')
        print(a.read())
