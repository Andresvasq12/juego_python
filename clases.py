import random
from datos import banco_jugadores,banco_preguntas
class Pregunta():
    def __init__(self):
        self.pregunta=""
    def seleccionar_pregunta(self,ronda):
        n=random.randint(1,5)
        self.pregunta=banco_preguntas[ronda][n]
        return self
    def get_pregunta(self):  
        return self.pregunta['pregunta']
   
    def get_respuesta(self):  
        return self.pregunta['respuesta'] 
   
    def validar_respuesta(self,respuesta):
        if self.get_respuesta() == respuesta:
            return True      
         
        
class Jugador():
    def __init__(self):
        self.nombre=''
        
    def set_nombre(self,nombre):
        self.nombre=nombre
        return self.nombre
    
    def set_monto(self,monto):
        self.monto=monto
        return self.monto    

    def guardar_jugador(self):
        banco_jugadores.append({'nombre':self.nombre,'monto':self.monto})


class Premio():
    def __init__(self):
        self.dificultad=0
        
    def aumentar_dificultad(self):
        self.dificultad+=1

    def premio(self):
       
   
       
        if self.dificultad==5:
             self.premio=1000000 
        if self.dificultad==4:
             self.premio=100000   
        if self.dificultad==3:
            self.premio=10000   
        if self.dificultad==2:
             self.premio=1000 
        if self.dificultad==1:
             self.premio=100            
       
        return self.premio                       
        
