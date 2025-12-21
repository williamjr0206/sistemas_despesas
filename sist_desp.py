from biblioteca import interface,funcoes
from time import sleep
interface.limpar_tela()
interface.cabecalho('*** Sistema de Lançamentos - versão: 1.0 ***')
while True:
    n = interface.menu(['Lançar Balanço','Lançar Créditos e Débitos em William','Lançar Créditos e Débitos em Zenilda',
                        'Abrir Power BI em Despesas','Abrir Power BI em Cláudia','Finalizar'])
    if n ==1:
        funcoes.balanco()
    elif n == 2:
        funcoes.despesas()
    elif n == 3:
        funcoes.despesas("ZENILDA")
    elif n == 4:
        funcoes.abrePowerBI("DESPESAS")
    elif n == 5:
        funcoes.abrePowerBI("CLAUDIA")
    elif n == 6:
       interface.cabecalho('Saindo do Sistema...')
       sleep(0.9)
       funcoes.limpar_tela()
       break
    else:
        print('\033[0;31mErro: Opção Inválida.\033[m')
