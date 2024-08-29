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
   [TP06] Lista de Recursividade - Exercício 7
================================================
'''
)

def pot(x,n):
    if n==0:
        return 1
    elif n<0:
        return 1/pot(x,abs(n))
    elif n>0:
        return x*pot(x,n-1)

print(pot(2,5))
print(pot(3,4))

'''
pot(2,5)= 2*pot(2,4) = 32
pot(2,4)= 2*pot(2,3) = 16
pot(2,3)= 2*pot(2,2) = 8
pot(2,2)= 2*pot(2,1) = 4
pot(2,1)= 2*pot(2,0) = 2
pot(2,0)= 1

----------------------

pot(3,4)= 3*pot(3,3)= 81
pot(3,3)= 3*pot(3,2)= 27
pot(3,2)= 3*pot(3,1)= 9
pot(3,1)= 3*pot(3,0)= 3
pot(3,0)= 1
'''
