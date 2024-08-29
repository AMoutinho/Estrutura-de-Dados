##################################################
#                                                #
#          Interface de Usuário (UI)             #
#              Projeto Dicionário                #
#                                                #
#        Desenvolvido por André Moutinho         #
#                                                #
##################################################

print(
    '''
================================================
            TP04 - PROJETO DICIONÁRIO
================================================
'''
)

Opcao = 5
DC = {}
DF = {}

print()
Menu = (
    '''================================================
                 MENU DICIONÁRIO
================================================
[1] - Cadastrar
[2] - Pesquisar
[3] - Alterar
[4] - Excluir
[5] - Listar por nome 
[0] - Finalizar Aplicação
======================================='''
)

while (Opcao != 0):
    print(Menu)
    Opcao = int(input("Informe a opção desejada do menu: "))    

    if (Opcao == 1):
        print(
    '''
================================================
                  Cadastrar
================================================
'''
)
        Telefone = str(input('Informe o Número do Telefone: '))

        if DC.get(Telefone):
            print("O número " + Telefone + " de telefone informado já está cadastrado, tente novamente !")
        else:
            Nome     = input("Informe o Nome: ")
            Endereco = input("Informe o Endereço: ")
            Cidade   = input("Informe a Cidade: ")
            Estado   = input("Informe o Estado: ")
            DC.update({Telefone: {"Nome":Nome, "Endereço":Endereco, "Cidade":Cidade, "Estado":Estado}})
            if len(DF) == 0:
                DF.update({1:Telefone})
            else:
                for ch, vlr in DF.items():
                    DF.update({ch+1:Telefone})
                    break
            print()    
            print("Cadastro realizado com êxito no sistema !")
            print() 


    elif (Opcao == 2):
        print(
    '''
================================================
                    Pesquisar
================================================
'''
)
        if len(DC) == 0:
            print("A lista de cadastros encontra-se vazia para pesquisar !")
        else:
            Telefone = input("Informe o número de telefone para pesquisar: ")
            print()
            if DC.get(Telefone):
                print(f"Nome:     {DC[Telefone]['Nome']}\nEndereço: {DC[Telefone]['Endereço']}\nCidade:   {DC[Telefone]['Cidade']}\nEstado:   {DC[Telefone]['Estado']}")
                print()
            else:
                print("O número de telefone informado, não consta cadastrado !")
             
        
    elif (Opcao == 3):
        print(
    '''
================================================
                    Alterar
================================================
'''
)
        if len(DC) == 0:
            print("A lista de cadastros encontra-se vazia para alterar !")
        else:
            Telefone = input("Informe o número de telefone para alterar: ")
            if DC.get(Telefone):
                Nome     = input("Informe o Nome: ")
                Endereco = input("Informe o Endereço: ")
                Cidade   = input("Informe a Cidade: ")
                Estado   = input("Informe o Estado: ")
                DC.update({Telefone: {"Nome":Nome, "Endereço":Endereco, "Cidade":Cidade, "Estado":Estado}})
                print()
                print("O cadastro foi alterado com êxito no sistema !")
                print()
            else:
                print("O número de telefone informado, não consta cadastrado !")
                
                
    elif (Opcao == 4):
        print(
    '''
================================================
                    Excluir
================================================
'''
)
        if len(DC) == 0:
             print("Não a registros de cadastros para exclusão !")
        else:
            Telefone = input("Informe o número de telefone para excluir: ")
            if DC.get(Telefone):
                del DC[Telefone]
                for ch, vlr in DF.items():
                    if vlr == Telefone:
                        del DF[ch]
                        break
                print()    
                print("O número de telefone do cadastro informado foi excluído com êxito !")
                print()
            else:
                print("O número de telefone informado, não consta cadastrado !")
                print()                


    elif (Opcao == 5):
        print(
    '''
================================================
                    Listar
================================================
'''
)
        if len(DC) == 0:
            print("Não existem cadastros para serem listados !")
        else:
            for ch, vlr in DF.items():                
                print("================================================")
                print(f"Telefone: {vlr}\nNome:     {DC[vlr]['Nome']}\nEndereço: {DC[vlr]['Endereço']}\nCidade:   {DC[vlr]['Cidade']}\nEstado:   {DC[vlr]['Estado']}")
                print("================================================")
                print()

                
    elif (Opcao == 0):
        print(
            '''
================================================
           Finalizar Aplicação 
================================================
'''
)
        print("Aplicação finalizada, obrigado por utilizar !!!")

    else:
        print()
        print("[OPÇÃO INVÁLIDA] Selecione uma opção válida para continuar por favor...")
        print()




