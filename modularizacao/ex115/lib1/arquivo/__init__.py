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

def cadastrar(arq, nome = 'desconhecido', idade = 0): #Função para cadastrar novos nomes à lista
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


def apagarcadastro(arq, nome): #Função para apagar um determinado nome da lista
    a = nome
    linha_a_apagar = None

    try:
        #Abrindo o arquivo para leitura
        with open(arq, "r") as file:
            linhas = file.readlines()
    except Exception as exc:
        print(f"Houve um erro na abertura do arquivo: {exc}")
        return #termina a função caso ocorra o erro
    
    # Percorrendo o arquivo para tentar localizar a linha com o nome a ser apagado
    for numerolinha, linha in enumerate(linhas):
        if a in linha:
            linha_a_apagar = numerolinha

    # Verificando se o nome a ser apagado foi encontrado
    if linha_a_apagar is not None:
        try:
            # Reescrevendo o arquivo sem a linha que foi apagada
            with open(arq, "w") as file:
                for numero, linha in enumerate(linhas):
                    if numero != linha_a_apagar:
                        file.write(linha)
            print(f"O nome '{nome}' foi removido com sucesso!")
        except Exception as exc:
            print(f"Houve um erro ao tentar reescrever o arquivo: {exc}")
    else:
        print(f"O nome '{nome}' não foi encontrado na lista.")