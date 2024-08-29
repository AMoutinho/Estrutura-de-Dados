class Fila:

    def __init__(self, tam=10):
        self.Tamtam=tam
        self.fila=[]

    def InserirFinal(self, x):
        self.fila.append(x)

    def InserirInicio(self, y):
        self.fila.insert(0, y)

    def RemoverInicio(self):
        self.fila.pop(0)

    def RemoverFinal(self):
        self.fila.pop()    

    def Primeiro(self):
        return self.fila[0]

    def Ultimo(self):
        return self.fila[-1]

    def filaVazia(self):
        return len(self.fila) == 0

    def filaCheia(self):
        return len(self.fila) == self.Tamtam

    def getFila(self):
        return self.fila
    
