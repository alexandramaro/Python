""" ex108: adapte o código do desafio 107, criando uma função adicional chamada moeda(),
que consiga mostrar os valores como um valor monetário formatado."""


def aumentar(preco, taxa):
    res = preco + (preco * taxa / 100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa / 100)
    return res


def dobro(preco):
    res = preco * 2
    return res


def metade(preco):
    res = preco / 2
    return res
