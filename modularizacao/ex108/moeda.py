def aumentar(n=0, taxa=0):
    res = n + (n*taxa/100)
    return res


def metade(n=0):
    res = n /2 
    return res


def dobro(n=0):
    res = n * 2
    return res


def diminuir(n=0, taxa=0):
    res = n - (n*taxa/100)
    return res


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.',',')
