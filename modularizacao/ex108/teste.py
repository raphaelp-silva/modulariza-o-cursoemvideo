#Adapte o código do desafio 107, criando uma funcao adicional chamada moeda() que consiga mostrar os numeros
#como um valor monetário formatado.

import moeda


preco = float(input("Digite um preço R$: "))

print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'aumentando em 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'diminuindo em 20%, temos {moeda.moeda(moeda.diminuir(preco, 20))}')