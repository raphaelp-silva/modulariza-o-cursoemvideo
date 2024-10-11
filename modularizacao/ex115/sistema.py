from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Cadastrar pessoas', 'Visualizar cadastros', 'Sair do sistema'])
    if resposta == 1:
        cabecalho("opcao 1")
    elif resposta == 2:
        cabecalho("opcao 2")
    elif resposta == 3:
        cabecalho("Saindo do sistema, até logo!")
        break
    else:
        print("\033[0;31mERRO! Digite uma opção válida!\033[m")
    sleep(1)