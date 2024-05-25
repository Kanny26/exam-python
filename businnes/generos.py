import os
import json
from .peliculas import guardar_json_peliculas, lista_peliculas


def load_genero_json():
    try:
        with open(os.path.join("data", "generos.json"), 'r') as generos_json:
            lista_generos = json.load(generos_json)
            print("La lista de géneros ha sido cargada")
            return lista_generos
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        

lista_generos = load_genero_json()

def crear_genero(id_pelicula):
    #nombre_genero = input("Ingrese el nombre del género: ")
    id_genero = input("Ingrese el ID del género: ")
    tipo_genero = input("Escriba el tipo de género (Acción, Comedia, romance etc.): ")
    
    genero = {
        #'Nombre del género': nombre_genero,
        'Id': id_genero,
        'Tipo de genero': tipo_genero
    }
    
    lista_generos.append(genero)
    print("Género creado exitosamente")
    guardar_json_generos()
    
    if id_pelicula in lista_peliculas:
        lista_peliculas[id_pelicula]["Generos"][id_genero] = genero
        guardar_json_peliculas()
    else:
        print(f"No se encontró la película con ID {id_pelicula}. No se pudo agregar el género.")
    
    
def guardar_json_generos():
    try:
        with open(os.path.join("data", "generos.json"), 'w') as genero_json:
            json.dump(lista_generos, genero_json, indent=2)
            print("La lista de géneros ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no hayan géneros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        

def listar_generos():
    print("Lista de géneros")
    for genero in lista_generos:
        print(genero)
    