def aumentar(n=0, taxa=0, formato=False):
    res = n + (n * taxa / 100)
    return res if formato is False else moeda(res)


def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    res = n - (n * taxa / 100)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda="R$"):
    return f"{moeda}{preco:>8.2f}".replace(".", ",")


def resumo(preco=0, aum=0, dim=0):
    print("-=" * 15)
    print("RESUMO DO VALOR".center(30))
    print("-=" * 15)
    print(f"Analisando o valor: \t{moeda(preco)}")
    print(f"O dobro é:    \t\t{dobro(preco, True)}")
    print(f"A metade é:   \t\t{metade(preco, True)}")
    print(f"Aumentando em {aum}%: \t{aumentar(preco, aum, True)}")
    print(f"Diminuindo em {dim}%: \t{diminuir(preco, dim, True)}")
