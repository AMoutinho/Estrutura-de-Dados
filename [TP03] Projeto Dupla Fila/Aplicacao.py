import classeFilaS

print(
    '''
================================================
            TP03 - PROJETO DUPLA FILA
================================================
'''
)

Tamtam = int(input("Informe o tamanho da fila desejada: "))
Fila = classeFilaS.Fila(Tamtam)

opc=1

print()
Menu = (
    '''=======================================
             MENU DUPLA FILA
=======================================
[1] - Insere no Final
[2] - Insere no Início
[3] - Remove do Início
[4] - Remove do Final
[5] - Primeiro da Fila 
[6] - Último da Fila
[7] - Exibe a Fila
[9] - Finalizar Aplicação
======================================='''
)

while opc != 9:
    print(Menu)
    opc = int(input("Informe a opção desejada do menu: "))
    
    if opc == 1:
        print(
            '''
================================================
                INSERE NO FINAL 
================================================
'''
)
        if Fila.filaCheia():
            print()
            print("A Fila está cheia !")
            print()
        else:
            x = int(input("Informe um valor para inserir no final da fila: "))
            Fila.InserirFinal(x)
            print()
            print("O valor",x,"informado foi inserido com sucesso ao final da fila !")
            print()

    elif opc == 2:
        print(
            '''
================================================
             INSERE NO INÍCIO 
================================================
'''
)
        if Fila.filaCheia():
            print()
            print("A Fila está cheia !")
        else:
            y = int(input("Informe um valor para inserir no início da fila:"))
            Fila.InserirInicio(y)
            print()
            print("Valor",y,"informado foi inserido com sucesso ao início da fila !")
            print()
    
    elif opc == 3:
        print(
            '''
================================================
                REMOVE DO INÍCIO 
================================================
'''
)
        if Fila.filaVazia():
            print("A Fila está vazia !")
            print()
        else:
            Fila.RemoverInicio()
            print("Removido com sucesso do início da fila !")
            print()

    elif opc == 4:
        print(
            '''
================================================
                REMOVE DO FINAL 
================================================
'''
    )
        if Fila.filaVazia():
            print("A Fila está vazia !")
            print()
        else:
            Fila.RemoverFinal()
            print("Removido com sucesso do final da fila !")
            print()

    elif opc == 5:
        print(
            '''
================================================
                PRIMEIRO DA FILA 
================================================
'''
)
        if Fila.filaVazia():
            print()
            print("A Fila está vazia !")
            print()
        else:
            print("Primeiro da fila é:", Fila.Primeiro())
            print()
    elif opc == 6:
        print(
            '''
================================================
                ÚLTIMO DA FILA 
================================================
'''
)
        if Fila.filaVazia():
            print("A Fila está vazia !")
            print()
        else:
            print("Último da fila é:", Fila.Ultimo())
            print()
    
    elif opc == 7:
        print(
            '''
================================================
                EXIBE A FILA 
================================================
'''
)
        if Fila.filaVazia():
            print()
            print("A Fila está vazia !")
            print()
        else:
            print("Exibindo a Fila:", Fila.getFila())
            print()        
    elif opc == 9:
        print(
            '''
================================================
             FINALIZAR APLICAÇÃO 
================================================
'''
)
        print("Aplicação finalizada, obrigado por utilizar !!!")

    else:
        print()
        print("[OPÇÃO INVÁLIDA] Selecione uma opção válida para continuar por favor...")
        print()
