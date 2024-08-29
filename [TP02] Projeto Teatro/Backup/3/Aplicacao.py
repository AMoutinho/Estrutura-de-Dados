##################################################
#                                                #
#          Interface de Usuário (UI)             #
#                Projeto Teatro                  #
#                                                #
#        Desenvolvido por André Moutinho         #
#                                                #
##################################################

import classeMatriz
import classeContadorv2

print(
    '''
================================================
             TP02 - PROJETO TEATRO
================================================
'''
)

linha = int(input("Informe a quantidade de Fileiras do Teatro: "))
coluna = int(input("Informe a quantidade de poltronas por fileira: "))

Teatro = classeMatriz.Matriz(linha, coluna)

vlrmax = linha * coluna
vlr = 0
Contador = classeContadorv2.Contador(vlr,vlrmax)

opcao = 0

print(
    '''
================================================
    DISPOSIÇÃO ATUAL DE POLTRONAS DO TEATRO
================================================
'''
)

for i in range(Teatro.getLin()):
    for j in range(Teatro.getCol()):
        print(Teatro.getValor(i, j), end="  ")
    print()

print()
Menu = (
    '''=======================================
              MENU TEATRO
=======================================
[1] - Vender Ingresso 
[2] - Devolução de Ingresso
[3] - Exibir Situação do Teatro
[9] - Finalizar Aplicação
======================================='''
)

while (opcao != 9):
    print(Menu)
    opcao = int(input("Informe a opção desejada do menu: "))

    if (opcao == 1):
        print(
            '''
================================================
              VENDA DE INGRESSOS 
================================================
'''
        )
        Fileira = int(input("Informe o número da Fileira desejada: "))
        Poltrona = int(input("Informe o número da Poltrona desejada: "))

        if Fileira < Teatro.getLin() and Poltrona < Teatro.getCol():
            if Teatro.getValidar(Fileira, Poltrona) == True:
                Teatro.Inserir(Fileira, Poltrona)
                print()
                print("Compra do ingresso realizada com êxito !")
                print()
                Contador.set_Inc()
            else:
                print()
                print("A poltrona informada está ocupada !")
                print()
        else:
            print()
            print("Os parâmetros informados da poltrona são inválidos !")
            print()

    elif (opcao == 2):
        print(
            '''
================================================
            DEVOLUÇÃO DE INGRESSOS 
================================================
'''
        )
        for i in range(Teatro.getLin()):
            for j in range(Teatro.getCol()):
                print(Teatro.getValor(i, j), end="  ")
            print()

        print()

        Fileira = int(input("Informe a fileira desejada para devolução: "))
        Poltrona = int(
            input("Informe o número da poltrona desejada para devolução: "))

        if Fileira < Teatro.getLin() and Poltrona < Teatro.getCol():
            if Teatro.getValidar(Fileira, Poltrona) == False:
                Teatro.Devolver(Fileira, Poltrona)
                print()
                print("Devolução do ingresso realizada com êxito !")
                print()
                Contador.set_Dec()
            else:
                print("Ingresso não vendido !")
                print()
        else:
            print("Os parâmetros informados do assento são inválidos !")
            print()

    elif (opcao == 3):
        print(
            '''
================================================
           EXIBIR SITUAÇÃO DO TEATRO 
================================================
'''
        )
        for i in range(Teatro.getLin()):
            for j in range(Teatro.getCol()):
                print(Teatro.getValor(i, j), end="  ")
            print()

        print()
        print(f"Lugares Ocupados: {Contador.get_Contador(vlr,vlrmax)}")
        print()
        print(f"Lugares Livres: {Contador.get_Disponiveis(vlr,vlrmax)}")
        print()
        print(f"Quantidade Vendida: {Contador.get_Contador(vlr,vlrmax)}")
        print()

    elif (opcao == 9):
        print(
            '''
================================================
           APLICAÇÃO FINALIZADA 
================================================
'''
        )
        print("Aplicação finalizada, obrigado por utilizar...")

    else:
        print()
        print("[OPÇÃO INVÁLIDA] Selecione uma opção válida para continuar por favor...")
        print()
