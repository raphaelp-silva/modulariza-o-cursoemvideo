def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip() #trocando as , por . enquanto a 'entrada' ainda é string, tirando os espacos.
        if entrada.isalpha() or entrada == '': #validando se a entrada é alfanumerico ou continua vazio.
            print(f"\033[0;31mERRO! {entrada} é um preço inválido!\033[m")
        else:
            valido = True
            return float(entrada)


def leiaInt(msg):
    ok = False  # criando uma flag com o padrão False
    valor = 0  # criando uma variável valor com o valor 0
    while True:
        n = str(
            input(msg)
        )  # criando uma variável n que recebe o que foi digitado pelo usuário
        if n.isnumeric():  # validando se o valor recebido é um número
            valor = int(n)
            ok = True  # caso seja um número e tenha sido convertido a inteiro, a flag passa a ser True
        else:
            print(
                "\033[0;31mERRO! Digite um valor inteiro válido!\033[m"
            )  # caso não seja um valor inteiro, é exibido uma mensagem de erro ao usuário
        if ok:
            break
    return valor