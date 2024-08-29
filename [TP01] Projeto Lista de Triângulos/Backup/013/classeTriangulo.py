##################################################
#                                                #
#        Classe Abstração de Triângulos          #
#                                                #
#        Desenvolvido por André Moutinho         #
#                                                #
##################################################

class Triangulo:
    def __init__(self, base, altura, ladoA, ladoB, ladoC):
        self.base = base
        self.altura = altura
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def perimetro(self, ladoA, ladoB, ladoC):
        p = ladoA + ladoB + ladoC       
        return p

    def area(self):
        A = (self.base * self.altura) / 2
        return A

    def isTriangulo(self, ladoA, ladoB, ladoC):
        if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoB + ladoA):
            return "Forma um Triângulo !"

        else:
            return "Não forma um Triângulo !"
