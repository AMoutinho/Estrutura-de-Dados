"""
Fatec Rubens Lara
Estrutura de Dados
André Moutinho
"""

'''
Projeto: controle remoto de ar condicionado
'''

'''
A nomeação de classes deve ocorrer
sempre com a primeira letra em maiúscula!
'''

# "self" refere-se à variável de uma classe!

# Ar Condicionado

class ArCondicionado:

    # Características ou Atributos

    def __init__(self):
        self.Ligado = False
        self.Temperatura = 0

    # Funcionalidades ou Métodos

    def ligar(self):
        self.Ligado = True

    def desligar(self):
        self.Ligado = False

    def aumentar(self):
        self.Temperatura += 1

    def diminuir(self):
        self.Temperatura -= 1

    def buscarValorTemperatura(self):
        return self.Temperatura

    def buscarEstadoLigadoDesligado(self):
        return self.Ligado
