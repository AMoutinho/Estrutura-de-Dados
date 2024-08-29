# Aplicação - Controle Remoto Ar-condicionado (Interface do Usuário) #

import classearc

ctrl = classearc.ArCondicionado()

MenuControle = (
'''=======================================
    CONTROLE REMOTO AR-CONDICIONADO
=======================================
[1] - Ligar
[+] - Aumentar Temperatura
[-] - Diminuir Temperatura
[0] - Desligar
======================================='''
)

cmd  = 0
while cmd != 4:
      Temp = ctrl.buscarValorTemperatura()
      print(f"Temperatura Atual: {Temp}")
      Estado = ctrl.buscarEstadoLigadoDesligado()
      print(f"Estado atual: {Estado}")
      print("\n")
      print(MenuControle)            
      cmd = input("Selecione uma Opção:")      
      if cmd == '1':            
         print("Ligando Ar-condicionado...")
         ctrl.ligar()
         print("\n")
      elif cmd == '+':
         print("Aumentar Temperatura...")
         ctrl.aumentar()
      elif cmd == '-' and ctrl.buscarValorTemperatura()>0:
         print("Diminuir Temperatura...")
         ctrl.diminuir()
      elif cmd == '0':
         print("Desligando Ar-condicionado...")         
         ctrl.desligar()
      else:
         print("OPÇÃO INVÁLIDA: Selecione uma opção válida !") 
         

       
              
   



















