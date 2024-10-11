from lib1.interface import *

def arquivoExiste(nome): #função para verificar se o arquivo já existe
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome): #função para criar o arquivo .txt (caso ele não exista)
    try:
        a = open(nome, 'wt+') #criando o arquivo com a função open() e wt+
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def lerArquivo(nome): #Ler o arquivo e exibir as linhas
    try:
        a = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        a.close()

def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro na abertura do arquivo!")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("Houve um erro na hora de escrever os dados")
        else:
            print(f"Novo registro de {nome} adicionado com sucesso!")
        finally:
            a.close()
