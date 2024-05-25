import os
import json
from utilidades.utils import validar_opcion


def load_peliculas_json():
    try:
        with open(os.path.join("data", "peliculas.json"), 'r') as peliculas_json:
            lista_peliculas = json.load(peliculas_json)
            print("La lista de películas ha sido cargada")
            return lista_peliculas
    except FileNotFoundError:
        print("El archivo no existe. Se inicializará una estructura vacía.")
        return {}
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        
lista_peliculas = load_peliculas_json()

def registrar_pelicula():
    from .actores import lista_actores
    from .formatos import lista_formatos
    from .generos import lista_generos
    
    id_pelicula = input("Ingrese el ID de la película: ")
    nombre_pelicula = input("Escriba el nombre de la película: ")
    duracion = input("Digite la duración de la película (HH:MM): ")
    sinopsis =  input("Escriba un breve resumen o sinopsis de la película: ")
    
    pelicula = {
        'Id': id_pelicula,
        'Nombre pelicula': nombre_pelicula,
        'Duracion': duracion,
        'Sinopsis': sinopsis,
        'Generos': [lista_generos],
        'Actores': [lista_actores],
        'Formato': [lista_formatos]
    }
    
    lista_peliculas.append(pelicula)
    print("Película registrada exitosamente")
    guardar_json_peliculas()
    
    
def guardar_json_peliculas():
    try:
        with open(os.path.join("data", "peliculas.json"), 'w') as peliculas_json:
            json.dump(lista_peliculas, peliculas_json, indent=2)
            print("La lista de películas ha sido guardada")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")
        

def listar_todas_las_peliculas():
    print("Listado de las películas registradas")
    for pelicula in lista_peliculas:
        print(pelicula)
        
        
def editar_pelicula():
    listar_todas_las_peliculas()

    id_pelicula_a_editar = input("Ingrese el ID de la película que desea editar: ")

    pelicula_a_editar = None
    for pelicula in lista_peliculas:
        if pelicula['Id'] == id_pelicula_a_editar:
            pelicula_a_editar = pelicula
            break

    if pelicula_a_editar is None:
        print("No se encontró la película con el ID especificado.")
        return

    print("Información actual de la película:")
    for key, value in pelicula_a_editar.items():
        print(f"{key}: {value}")

    nueva_nombre = input("Nuevo nombre de la película (dejar en blanco para mantener el actual): ")
    nueva_duracion = input("Nueva duración de la película (dejar en blanco para mantener la actual): ")
    nueva_sinopsis = input("Nueva sinopsis de la película (dejar en blanco para mantener la actual): ")

    if nueva_nombre:
        pelicula_a_editar['Nombre pelicula'] = nueva_nombre
    if nueva_duracion:
        pelicula_a_editar['Duracion'] = nueva_duracion
    if nueva_sinopsis:
        pelicula_a_editar['Sinopsis'] = nueva_sinopsis

    guardar_json_peliculas()

    print("La película ha sido editada exitosamente.")
    
    
def eliminar_pelicula():
    
    id_pelicula_a_eliminar = input("Ingrese el ID de la película que desea eliminar: ")

    pelicula_a_eliminar = None
    for pelicula in lista_peliculas:
        if pelicula['Id'] == id_pelicula_a_eliminar:
            pelicula_a_eliminar = pelicula
            break

    if pelicula_a_eliminar is None:
        print("No se encontró la película con el ID especificado.")
        return

    confirmacion = input(f"¿Estás seguro de que quieres eliminar la película '{pelicula_a_eliminar['Nombre pelicula']}'? (Sí/No): ").lower()

    if confirmacion == 'si':
        lista_peliculas.remove(pelicula_a_eliminar)

        guardar_json_peliculas()

        print("La película ha sido eliminada correctamente.")
    else:
        print("Operación de eliminación cancelada.")
        
        
def buscar_peliculas():
    from businnes.generos import lista_generos
    
    print("Opciones de búsqueda:")
    print("1. Por género")
    print("2. Por ID")

    opcion_busqueda = validar_opcion("Seleccione la opción de búsqueda: ", 1, 2)

    if opcion_busqueda == 1:
        tipo_genero = input("Ingrese el tipo de género a buscar: ")
        peliculas_encontradas = [genero for genero in lista_generos if genero.get('Tipo de genero') == tipo_genero]
    elif opcion_busqueda == 2:
        id_pelicula = input("Ingrese el ID de la película a buscar: ")
        peliculas_encontradas = [pelicula for pelicula in lista_peliculas if pelicula.get('Id') == id_pelicula]
    else:
        print("Opción de búsqueda no válida.")
        return

    if peliculas_encontradas:
        print("Películas encontradas:")
        for pelicula in peliculas_encontradas:
            print(pelicula)
    else:
        print("No se encontraron películas que coincidan con los criterios de búsqueda.")