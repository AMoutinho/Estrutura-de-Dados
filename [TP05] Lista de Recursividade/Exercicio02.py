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
   [TP06] Lista de Recursividade - Exercício 2
================================================
'''
)

n=6
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print("Fibonacci de",n,":",fib(n))
