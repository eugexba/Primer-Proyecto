
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

          elif len(letras_incorrectas) > 0:
               print("letra incorrecta: ", *letras_incorrectas)
               print()

          else:
               lista_oculta.append("-")
          
 
     print(lista_oculta)
     return lista_oculta

def pedir_letra(palabra_seleccionada, lista_oculta, letras_incorrectas):
     valida = False 
     while not valida:
          letra = input("Ingrese una letra!: ").lower()
          valida = "a" <= letra <= "z" and len(letra) == 1
          if not valida:
               print("Error. Ingrese una letra!")
          else: 
               valida = letra not in palabra_seleccionada + lista_oculta
               if not valida:
                    print("Letra repetida")
     return letra 

def comprobar_letra(letra, palabra_seleccionada,letras_incorrectas, lista_oculta):
     palabra_seleccionada, letras_unicas = seleccionar_palabra(palabras)
     if letra in palabra_seleccionada:
          print("Acertaste una letra! ")
          actualizar_tablero(letra, palabra_seleccionada,lista_oculta)
     else:
          print("Fallaste!")
          letras_incorrectas.append(letra)

def actualizar_tablero(letra, palabra_seleccionada, lista_oculta)
     for indice, letra_palabra in enumerate (palabra_seleccionada):
          if letra == letra_palabra:
               lista_oculta[indice] = letra 

def comprobar_palabra(palabra_seleccionada):
     return "_" not in palabra_seleccionada

def juego_finalizado(palabra_seleccionada):


     palabra_seleccionada, letras_incorrectas, imprimir_nuevo_tablero = juego_finalizado(palabras)
     while len(letras_incorrectas):
          imprimir_nuevo_tablero(palabra_seleccionada, letras_incorrectas)
          letras = pedir_letra(palabra_seleccionada, letras_incorrectas)
          comprobar_letra(letra, palabra_seleccionada, letras_incorrectas,imprimir_nuevo_tablero)
          if comprobar_palabra(imprimir_nuevo_tablero):
               print("Lo lograste!")
          else:
               print(f"Perdiste! la palabra era: {palabra_seleccionada}")

     imprimir_nuevo_tablero(palabra_seleccionada, letras_incorrectas)