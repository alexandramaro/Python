""" ex109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas, vai ou não ser formatado
pela função moeda(), desenvolvida no desafio 108."""


def aumentar(preco=0, taxa=0, formato=False):
    """
    → Calcula o aumento de um determinado preço, retornando o resultado com ou sem formatação.
    :param preco: € o preço que se quer reajustar
    :param taxa: a percentagem do aumento (10% e 13%)
    :param formato: Saída formatada (,00€) ou não?
    :return: o valor reajustado, com ou sem formato.
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='€'):
    return f'{preco:>.2f}{moeda}'.replace('.', ',')
