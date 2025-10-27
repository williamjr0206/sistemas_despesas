from biblioteca import interface,funcoes
interface.limpar_tela()
interface.cabecalho('*** Sistema de Lançamentos - versão: 1.0 ***')
while True:
    n = interface.menu(['Lançar Balanço','Lançar Créditos e Débitos', 'Finalizar'])
    if n ==1:
        funcoes.balanco()
    elif n == 2:
        funcoes.despesas()
    elif n == 3:
       interface.cabecalho('Saindo do Sistema...')
       break
    else:
        print('\033[0;31mErro: Opção Inválida.\033[m')
