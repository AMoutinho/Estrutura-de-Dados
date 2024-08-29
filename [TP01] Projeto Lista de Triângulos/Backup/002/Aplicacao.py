##################################################
#                                                #
#         Interface de Usuário (UI)              #
#   Projetada para consumir a classeTriangulo    #
#                    e a                         #
#              classeListaLinear                 #  
#                                                #
#        Desenvolvida por André Moutinho         #
#                                                #
##################################################

import classeTriangulo
import classeListaLinear


tamanho = int(input("Informe o tamanho da lista desejada: "))

ListaT = classeListaLinear.ListaLinear(tamanho)

opcao = 0

print()

Menu = (
    '''=======================================
    PROJETO LISTA DE TRIÂNGULOS
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
            print("LISTA VAZIA - Impossível remover itens dela !")

        else:
            ListaT.remover()
            print()
            print("Remoção de elemento(s) realizada com êxito !")

    elif (opcao == 3):
        if ListaT.isEmpty():
            print()
            print("LISTA VAZIA - Nada a Exibir !")

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
                print("------------------------")
                print("Base.: ", triang.base)
                print("Altura.: ", triang.altura)
                print("Perímetro.: ", triang.perimetro(ladoA, ladoB, ladoC))
                print("Área.: ", triang.area())
                if triang.isTriangulo(ladoA, ladoB, ladoC):
                    print("Temos triângulos na lista!")
                print("------------------------")

    elif (opcao == 9):
        print()
        print("Programa Finalizado !")

    else:
        print()
        print("[Opção Inválida] Selecione uma opção válida para continuar...")
