##################################################
#                                                #
#         Interface de Usuário (UI)              #
#   Projetada para consumir a classeTriangulo    #
#                    e a                         #
#              classeListaLinear                 #  
#                                                #
#        Desenvolvido por André Moutinho         #
#                                                #
##################################################

import classeTriangulo
import classeListaLinear

print(
'''
================================================
ESTRUTURA DE DADOS - PROJETO LISTA DE TRIÂNGULOS
================================================
'''
)

tamanho = int(input("Informe o tamanho da lista desejada: "))

ListaT = classeListaLinear.ListaLinear(tamanho)

opcao = 0

print()

Menu = (
    '''=======================================
           LISTA DE TRIÂNGULOS
=======================================
[1] - Inserir na Lista
[2] - Remover da Lista
[3] - Exibir Listagem
[9] - Finalizar Aplicação
======================================='''
)

while (opcao != 9):
    print(Menu)
    opcao = int(input("Informe a opção desejada do menu: "))

    if (opcao == 1):
        if ListaT.isFull():
            print()
            print("LISTA CHEIA - Impossível inserir mais elementos !")
            
        else:
            print()
            base = int(input("Informe a Base: "))
            altura = int(input("Informe a Altura: "))
            t = classeTriangulo.Triangulo(base, altura)
            ListaT.inserir(t)
            print()
            print("Inserção de elemento(s) realizada com êxito !")
            print()
    elif (opcao == 2):
        if ListaT.isEmpty():
            print()
            print("LISTA VAZIA - Impossível remover itens inexistentes !")
            print()
        else:
            ListaT.remover()
            print()
            print("Remoção de elemento(s) realizada com êxito !")

    elif (opcao == 3):
        if ListaT.isEmpty():
            print()
            print("LISTA VAZIA - Não a elementos para serem mostrados !")
            print()
        else:
            tes = ListaT.getLista()

            print()
            print("Para calcular o perímetro dos triângulos, precisamos que sejam informados abaixo os valores das medidas de cada lado destes polígonos.")
            print()
            
            ladoA = int(input("Informe o valor do lado A: "))
            ladoB = int(input("Informe o valor do lado B: "))
            ladoC = int(input("Informe o valor do lado C: "))

            print()

            for triang in tes:
                print("========== Exibindo Listagem ==========")
                print()
                print("BASE : ", triang.base)
                print("ALTURA : ", triang.altura)
                print("PERÍMETRO : ", triang.perimetro(ladoA, ladoB, ladoC))
                print("ÁREA : ", triang.area())
                if triang.isTriangulo(ladoA, ladoB, ladoC):                    
                    print()    
                print("=======================================")
                print()
    elif (opcao == 9):
        print()
        print("Aplicação finalizada !")

    else:
        print()
        print("[Opção Inválida] Selecione uma opção válida para continuar...")
        print()
