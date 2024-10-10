def aumentar(n=0, taxa=0, formato=False):
    res = n + (n*taxa/100)
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n /2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    res = n - (n*taxa/100)
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.',',')
