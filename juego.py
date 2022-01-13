from clases import Jugador,Pregunta,Premio
from datos import banco_jugadores


def juego():
    ronda=1
    premio=Premio()
    jugador=Jugador()
    nombre= input("ESCRIBE TU NOMBRE\n>")
    jugador.set_nombre(nombre)

    

    while ronda<6:
        
        pregunta1 = Pregunta().seleccionar_pregunta(ronda)
        pregunta=pregunta1.get_pregunta()
        print(pregunta)
        
        respuesta = input('ELIJE RESPUESTA :\n ')
        if pregunta1.validar_respuesta(respuesta) :
            if ronda==5:
                
                premio.aumentar_dificultad()
                jugador.set_monto(premio.premio())
                print("FELICIDADES!!! , GANASTE EL JUEGO TU MONTO ES DE: ",jugador.monto )
                break    

            else:
                ronda+=1
                premio.aumentar_dificultad()
                print("GANASTE")
                resq=input("desea continuar y/n:\n> ")
                
                if resq=='y':    
                    continue
                else:
                    jugador.set_monto(premio.premio())
                    print("GRACIAS POR JUGAR TU MONTO ES DE  " ,jugador.monto)  
                    break  
        else:
            jugador.monto=0
            print( ":( PERDISTE TU MONTO ES  ",jugador.monto  )  
            break
    return jugador.guardar_jugador()
  

 


        
       
        
  

             
            
              
            
    
            

