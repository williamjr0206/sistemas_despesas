def linha(tam=50):
    print('-'*tam)

def cabecalho(msg):
    linha()
    print(msg)
    linha()


def menu(lista):
    cabecalho(' ***  Menu Principal ***'.center(50))
    c = 1
    for l in lista:
        print(f'\033[0;31m{c}\033[m - \033[0;35m{l}\033[m')
        c += 1
    linha()
    opcao = leiaint('\033[0;35mDigite a opção:\033[m ')
    return opcao
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        try:
            valor = int(n)

        except Exception as erro:
            print(f'Ocorreu um erro de: {erro.__class__}')
        except(KeyboardInterrupt):
            print('\n \033[0;31m O usuário não quis informar o valor.\033[m')
            return valor
        else:
            valor = valor
            ok = True
        if ok:
            break
    return valor
