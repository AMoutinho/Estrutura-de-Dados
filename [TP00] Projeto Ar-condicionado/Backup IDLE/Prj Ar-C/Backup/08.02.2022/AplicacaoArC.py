# Aplicação - Controle Remoto Ar-condicionado (Interface do Usuário) #

import classearc

ctrl = classearc.ArCondicionado()

MenuControle = (
'''=======================================
    CONTROLE REMOTO AR-CONDICIONADO
=======================================
1 - Ligar
2 - Aumentar Temperatura
3 - Diminuir Temperatura
4 - Desligar
======================================='''
)

cmd  = 0
while cmd != 4:
      print(MenuControle)
      cmd = int(input("Selecione uma Opção:"))      
      if cmd == 1:
         print("Ligando Ar-condicionado...")
         print("\n")
      elif cmd == 2:
         print("Aumentar Temperatura...")
      elif cmd == 3:
         print("Diminuir Temperatura...")
      elif cmd == 4:
         print("Desligando Ar-condicionado...")
      else:
         print("OPÇÃO INVÁLIDA: Selecione uma opção válida !") 
         

       
              
   



















