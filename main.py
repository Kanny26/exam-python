from utilidades.utils import limpiar_pantalla
from utilidades.menus import *
from businnes.generos import crear_genero, listar_generos
from businnes.actores import crear_actores, listar_actores, eliminar_actor
from businnes.formatos import crear_formatos, listar_formatos
from businnes.peliculas import registrar_pelicula, editar_pelicula, eliminar_pelicula, buscar_peliculas, listar_todas_las_peliculas
from businnes.informes import *


def generos():      
    limpiar_pantalla()
    op=menu_generos()
    if op==1:
        id_pelicula = input("Ingrese el ID de la película a la que desea agregar un género: ")
        crear_genero(id_pelicula)
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        listar_generos()
        input("Presiona cualquier tecla para continuar: ")

def actores():      
    limpiar_pantalla()
    op=menu_actores()
    if op==1:
        id_pelicula = input("Ingrese el ID de la película a la que desea agregar un género: ")
        crear_actores(id_pelicula)
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        listar_actores()
        input("Presiona cualquier tecla para continuar: ")

def formatos():      
    limpiar_pantalla()
    op=menu_formatos()
    if op==1:
        id_pelicula = input("Ingrese el ID de la película a la que desea agregar un género: ")
        crear_formatos(id_pelicula)
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        listar_formatos()
        input("Presiona cualquier tecla para continuar: ")


def informes():      
    limpiar_pantalla()
    op=menu_informes()
    if op==1:
        listar_peliculas_por_genero()
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        listar_peliculas_por_actor()
        input("Presiona cualquier tecla para continuar: ")
    if op==3:
        buscar_pelicula_mostrar_info()
        input("Presiona cualquier tecla para continuar: ")
        

def peliculas():      
    limpiar_pantalla()
    op=menu_peliculas()
    if op==1:
        registrar_pelicula()
        input("Presiona cualquier tecla para continuar: ")
    if op==2:
        editar_pelicula()
        input("Presiona cualquier tecla para continuar: ")
    if op==3:
        eliminar_pelicula()
        input("Presiona cualquier tecla para continuar: ")
    if op==4:
        eliminar_actor()
        input("Presiona cualquier tecla para continuar: ")
    if op==5:
        buscar_peliculas()
        input("Presiona cualquier tecla para continuar: ")
    if op==6:
        listar_todas_las_peliculas()
        input("Presiona cualquier tecla para continuar: ")
        
       
        

while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       generos()
   elif op==2:
       actores()
   elif op==3:
       formatos()
   elif op==4:
       informes()
   elif op==5:
       peliculas()
   elif op==6:
       print("Saliendo del programa, ¡Hasta luego!")
       break