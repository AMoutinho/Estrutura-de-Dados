class Contador:
    
    def __init__(self,vlr,vlrmax):
        self.contador = vlr
        self.maximo = vlrmax

    def set_Inc(self):
        if self.contador < self.maximo:
            self.contador+=1

    def set_Dec(self):
        self.contador-=1

    def get_Contador(self,vlr,vlrmax):
        return self.contador

    def get_Disponiveis(self,vlr,vlrmax):
        return self.maximo - self.contador


    

















        


