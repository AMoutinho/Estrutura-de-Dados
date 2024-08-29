##################################################
#                                                #
#         TP06 - LISTA DE RECURSIVIDADE          #
#                                                #
#                André Moutinho                  #
#                                                #
##################################################

print(
    '''
================================================
   [TP06] Lista de Recursividade - Exercício 1
================================================
'''
)

n=5
def fatorial(n):
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)


print("Fatorial de",n,":",fatorial(n))

''' Pilha de Recursão - Fatorial de 5:

fatorial(5) = 5 * fatorial(5-1) = 120
fatorial(4) = 4 * fatorial(4-1) = 24
fatorial(3) = 3 * fatorial(3-1) = 6
fatorial(2) = 2 * fatorial(2-1) = 2
fatorial(1) = 1 * fatorial(1-1) = 1
fatorial(0)                     = 1
'''
