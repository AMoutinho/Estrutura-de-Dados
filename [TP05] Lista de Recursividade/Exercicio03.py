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
   [TP06] Lista de Recursividade - Exercício 3
================================================
'''
)

x=64
y=14
def mdc(x,y):
    if x==y:
        return x
    elif x < y:
        return mdc(y,x)
    else:
        return mdc(x-y,y)
        


print("MDC(",x,",",y,") =",mdc(x,y))
