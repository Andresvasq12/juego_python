from juego import juego 
from datos import banco_jugadores
import os
def menu():
     while True:  
          print("-----------")
          print("BIENVENIDO")
          
          print("-----------")
          print("SELECCIONA UNA OPCION")
          print("-----------")
          print("[1] Ver Puntajes\n[2] Iniciar juego")
          n=input("> ")
           
          if n=="1":
               if banco_jugadores==[]:
                    print("AUN NO HAY REGISTROS")
               for jugador in banco_jugadores:
                   print(f"NOMBRE {jugador['nombre']}: PUNTAJE{jugador['monto']} ")
               

               

          if n=="2":
               juego()

          input("\nPresiona ENTER para continuar...")     
               
      
menu()       
                  
              




           
