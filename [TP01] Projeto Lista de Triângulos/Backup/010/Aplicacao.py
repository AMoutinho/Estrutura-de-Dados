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
            print("[LISTA CHEIA] Impossível inserir mais elementos !")
            print()
        else:
            print()
            base = int(input("Informe a Base: "))
            altura = int(input("Informe a Altura: "))
            ladoA = int(input("Informe o valor do lado A: "))
            ladoB = int(input("Informe o valor do lado B: "))
            ladoC = int(input("Informe o valor do lado C: "))
            
            t = classeTriangulo.Triangulo(base,altura,ladoA,ladoB,ladoC)
            ListaT.inserir(t)
            print()
            print("Inserção de elemento(s) realizada com êxito !")
            print()
    elif (opcao == 2):
        if ListaT.isEmpty():
            print()
            print("[LISTA VAZIA] Impossível remover itens inexistentes !")
            print()
        else:
            ListaT.remover()
            print()
            print("Remoção de elemento(s) realizada com êxito !")
            print()
    elif (opcao == 3):
        if ListaT.isEmpty():
            print()
            print("LISTA VAZIA - Não a elementos para serem mostrados !")
            print()
        else:
            tes = ListaT.getLista()

            print()
            #print("Para calcular o perímetro dos triângulos, precisamos que sejam informados abaixo os valores das medidas de cada lado destes polígonos.")
            print()
            
            #ladoA = int(input("Informe o valor do lado A: "))
            #ladoB = int(input("Informe o valor do lado B: "))
            #ladoC = int(input("Informe o valor do lado C: "))

            print()

            for triang in tes:
            #for i in range(ListaT.getTamanhoAtual()):
                #x = ListaT.getValor(i)
                print("==========| Exibindo Listagem |==========")
                print()
                print("BASE : ", triang.base)
                #print("BASE : ", x.base)
                #print("ALTURA : ", x.altura)
                print("ALTURA : ", triang.altura)
                print("PERÍMETRO : ", triang.perimetro(ladoA, ladoB, ladoC))
                #print("PERÍMETRO : ", x.perimetro(ladoA, ladoB, ladoC))                
                print("ÁREA : ", triang.area())
                #print("ÁREA : ", x.area())
                print("LADO A : ", triang.ladoA)
                print("LADO B : ", triang.ladoB)                
                print("LADO C : ", triang.ladoC)
                
                #print("LADO A : ", x.ladoA)
                #print("LADO B : ", x.ladoB)                
                #print("LADO C : ", x.ladoC)
                #if x.isTriangulo(ladoA, ladoB, ladoC):
                if triang.isTriangulo(ladoA, ladoB, ladoC):     
                    print()
                    print("Formam um Triângulo !")
                    print() 
                print("=======================================")
                print()
    elif (opcao == 9):
        print()
        print("Aplicação finalizada !")

    else:
        print()
        print("[OPÇÃO INVÁLIDA] Selecione uma opção válida para continuar por favor...")
        print()
