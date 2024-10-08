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
   [TP06] Lista de Recursividade - Exercício 6
================================================
'''
)

def dig(n):
    if abs(n)>9:
        return 1+dig(n/10)
    elif abs(n)<=9:
        return 1

print(dig(53223))
print(dig(100011))

'''
dig(53223/10)=1+dig(5322.3/10)=5
dig(5322.3/10)=1+dig(532.23/10)=4
dig(532.23/10)=1+dig(53.223/10)=3
dig(53.223/10)=1+dig(5.3223)=2
dig(5.3223)=1

---------------------------------

dig(100011/10)=1+dig(10001.1)=6
dig(10001.1/10)=1+dig(1000.11)=5
dig(1000.11/10)=1+dig(100.011)=4
dig(100.011/10)=1+dig(10.0011)=3
dig(10.0011/10)=1+dig(1.00011)=2
dig(1.00011)=1
'''
