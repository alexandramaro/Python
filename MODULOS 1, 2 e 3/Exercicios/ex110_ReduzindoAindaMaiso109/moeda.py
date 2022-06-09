""" ex110: Adicione ao módulo modeda.py criado nos desafios anteriores, uma função
chamada resumo(), que mostre na tela algumas informações geradas pelas funções que
já temos no módulo criado até aqui."""


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
