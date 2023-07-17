from random import choice 

palabras = ["otorrinolaringologo", "parabrisas", "desierto", "estudiantes"]
letras_incorrectas = []
letras_correctas = []
intentos = 6 
aciertos = 0 
juego_finalizado = False

def seleccionar_palabra(lista_palabras):
     palabra_seleccionada = choice(lista_palabras)
     letras_unicas = len(set(palabra_seleccionada))
     return palabra_seleccionada, letras_unicas
    
palabra = seleccionar_palabra(palabras)
print(palabra)

def imprimir_nuevo_tablero(palabra_seleccionada):
     lista_oculta = []

     for e in palabra_seleccionada:
          if e in letras_correctas:
               lista_oculta.append(e)

          else:
               lista_oculta.append("-")
          
 
     print(lista_oculta)
