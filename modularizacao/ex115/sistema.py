from lib1.interface import *
from lib1.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Cadastrar pessoas', 'Visualizar cadastros', 'Sair do sistema'])
    if resposta == 1:
        #opção de cadastrar uma nova pessoa
        cabecalho("Novo Cadastro")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrar(arq,nome,idade)
    elif resposta == 2:
        #opção de visualizar os cadastros
        lerArquivo(arq)
    elif resposta == 3:
        cabecalho("Saindo do sistema, até logo!")
        break
    else:
        print("\033[0;31mERRO! Digite uma opção válida!\033[m")
    sleep(1)