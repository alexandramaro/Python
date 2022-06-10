from ex115c_FinalizarProjeto.lib.interface import *

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
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS REGISTADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def registar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')     # at ☻ append text
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO a escrever os dados!')
        else:
            print(f'Novo registo de {nome} adicionado.')
            a.close()
