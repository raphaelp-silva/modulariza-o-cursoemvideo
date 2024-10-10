# Crie um módulo chamado moeda.py que tenha as funcoes incorporadas aumentar(), diminuir()
# dobro() e metade()
# Faça um prgorama que importe esses módulos e use algumas dessas funções

import moeda


preco = float(input("Digite um preço R$: "))

print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'aumentando em 10%, temos {moeda.aumentar(preco, 10)}')
print(f'diminuindo em 20%, temos {moeda.diminuir(preco, 20)}')