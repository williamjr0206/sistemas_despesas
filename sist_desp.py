from biblioteca import interface,funcoes
from time import sleep
interface.limpar_tela()
interface.cabecalho('*** Sistema de Lançamentos - versão: 1.0 ***')
while True:
    n = interface.menu(['Lançar Créditos e Débitos em João Vitor','Lançar Créditos e Débitos em Heytor','Lançar Créditos e Débitos em Érika','Lançar Créditos e Débitos em Pastor João' 'Finalizar'])
    if n ==1:
        funcoes.despesas()
    elif n == 2:
        funcoes.despesas("HEYTOR")
    elif n == 3:
        funcoes.despesas("ERIKA")
    elif n == 4:
        funcoes.despesas("JOAO")
    elif n == 5:
       interface.cabecalho('Saindo do Sistema...')
       sleep(0.9)
       funcoes.limpar_tela()
       break
    else:
        print('\033[0;31mErro: Opção Inválida.\033[m')
