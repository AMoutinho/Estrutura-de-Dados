
class Matriz:
    def __init__(self,linha,coluna):
        self.lin=linha
        self.col=coluna
        self.matriz=[]
        for ln in range(self.lin):
            lista=[]
            for cl in range(self.col):
                lista.append("0")
            self.matriz.append(lista)
            
    def Inserir(self,linha,coluna):
        self.matriz[linha][coluna]= "X"

    def Devolver(self,linha,coluna):       
        self.matriz[linha][coluna] = "0"    

    def getLin(self):
        return self.lin
    
    def getCol(self):
        return self.col

    def getValor(self,linha,coluna):
        return self.matriz[linha][coluna]

    def getValidar(self,linha,coluna):
        return self.matriz[linha][coluna] == "0"


