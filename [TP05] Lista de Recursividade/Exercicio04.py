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
   [TP06] Lista de Recursividade - Exercício 4
================================================
'''
)

def soma(m,n):
    if n==m:
        return m
    elif m < n:
        return soma(m, n-1) + n
    

print(f"Soma(10,15) = {soma(10,15)}")





