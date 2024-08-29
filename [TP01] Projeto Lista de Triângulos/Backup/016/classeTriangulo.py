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

    def perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def area(self):
        return (self.base * self.altura) / 2        

    def isTriangulo(self,ladoA,ladoB,ladoC):
        if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoB + ladoA):
            return "Forma um Triângulo !"

        else:
            return "Não forma um Triângulo !"
