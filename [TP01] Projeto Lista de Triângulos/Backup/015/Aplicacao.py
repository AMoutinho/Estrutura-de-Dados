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
            
            T = classeTriangulo.Triangulo(base,altura,ladoA,ladoB,ladoC)
            ListaT.inserir(T)
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

            #for triangulo in tes:
            for i in range(ListaT.getTamanhoAtual()):
                T = ListaT.getValor(i)
                print("==========| Exibindo Listagem |==========")
                print()
                
                #print("Perímetro: ", triangulo.perimetro(ladoA, ladoB, ladoC))
                print("Perímetro: ", T.perimetro(ladoA, ladoB, ladoC))
                             
                #print("Área: ", triangulo.area())
                print("Área: ", T.area())
                
                #print("Lado A: ", triangulo.ladoA)
                #print("Lado B: ", triangulo.ladoB)                
                #print("Lado C: ", triangulo.ladoC)

                print("Lado A: ", T.ladoA)
                print("Lado B: ", T.ladoB)                
                print("Lado C: ", T.ladoC)  
               
                #if triangulo.isTriangulo(ladoA, ladoB, ladoC):
                if T.isTriangulo(ladoA, ladoB, ladoC):      
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
