class Contador:
    
    def __init__(self, valor=0, valormax=10):
        self.contador = valor
        self.max = valormax

    def set_Inc(self):
        if self.contador < self.max:
            self.contador+=1

    def set_Dec(self):
        self.contador-=1

    def get_Contador(self):
        return self.contador

















        


