##################################################
#                                                #
#                                                #
#      Abstração Lista Linear de Triângulos      #
#                                                #
#                   Pré-Definida                 #
#                                                #
##################################################

class ListaLinear:
    
    def __init__(self, tamanho):
        self.lista = []
        self.tamanho = tamanho

    def inserir(self, x):
        self.lista.append(x)

    def remover(self):
        self.lista.pop()

    def getValor(self,indice):
        return self.lista[indice]
    
    def getTamanhoAtual(self):
        return len(self.lista)

    def isFull(self):
        return self.tamanho == len(self.lista)

    def isEmpty(self):
        return len(self.lista) == 0

    def getLista(self):
        return self.lista
