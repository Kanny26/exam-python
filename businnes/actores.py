import os
import json
from .peliculas import guardar_json_peliculas, lista_peliculas


def load_actor_json():
    try:
        with open(os.path.join("data", "actores.json"), 'r') as actores_json:
            lista_actores = json.load(actores_json)
            print("La lista de actores ha sido cargada")
            return lista_actores
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        
        
lista_actores = load_actor_json()


def crear_actores(id_pelicula):
    id_actor = input("Registre el ID del actor: ")
    nombre_actor = input("Ingrese el nombre del actor: ")
    rol = input("Ingrese el rol del actor en la película (Protagonista, Antagonista o Reparto): ")
    
    actor = {
        'Id': id_actor,
        'Nombre Actor': nombre_actor,
        'Rol': rol
    }
    
    lista_actores.append(actor)
    print("Actor registrado exitosamente")
    guardar_json_actores()
    
    if id_pelicula in lista_peliculas:
        lista_peliculas[id_pelicula]["Actores"][id_actor] = actor
        guardar_json_peliculas()
    else:
        print(f"No se encontró la película con ID {id_pelicula}. No se pudo agregar el actor.")
    

def guardar_json_actores():
    try:
        with open(os.path.join("data", "actores.json"), 'w') as actores_json:
            json.dump(lista_actores, actores_json, indent=2)
            print("La lista de actores ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no hayan actores guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
   
        
def listar_actores():
    print("Lista de actores registrados")
    for actor in lista_actores:
        print(actor)
        
        
def eliminar_actor():
 
    id_actor_a_eliminar = input("Ingrese el ID del actor que desea eliminar: ")

    actor_a_eliminar = None
    for actor in lista_actores:
        if actor['Id'] == id_actor_a_eliminar:
            actor_a_eliminar = actor
            break

    if actor_a_eliminar is None:
        print("No se encontró el actor con el ID especificado.")
        return

    confirmacion = input(f"¿Estás seguro de que quieres eliminar al actor '{actor_a_eliminar['Nombre Actor']}'? (Sí/No): ").lower()

    if confirmacion == 'si':
        lista_actores.remove(actor_a_eliminar)

        guardar_json_actores()

        print("El actor ha sido eliminado correctamente.")
    else:
        print("Operación de eliminación cancelada.")