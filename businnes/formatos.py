import os
import json
from .peliculas import guardar_json_peliculas, lista_peliculas

def load_formatos_json():
    try:
        with open(os.path.join("data", "formatos.json"), 'r') as formatos_json:
            lista_formatos = json.load(formatos_json)
            print("La lista de formatos ha sido cargada")
            return lista_formatos
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        
        
lista_formatos = load_formatos_json()


def crear_formatos(id_pelicula):
    id_formato = input("Ingrese el ID del formato: ")
    nombre_formato = input("Escriba el nombre del formato (como DVD etc.): ")
    nro_copias = int(input("Digite el número de copias: "))
    valor_prestamo = float(input("Ingrese el valor del préstamo: "))
    
    formato = {
        'Id': id_formato,
        'Nombre': nombre_formato,
        'Nro de copias': nro_copias,
        'Valor del prestamo': valor_prestamo
    }
    
    lista_formatos.append(formato)
    print("El formato se ha creado exitosamente")
    guardar_json_formatos()
    
    if id_pelicula in lista_peliculas:
        lista_peliculas[id_pelicula]["Formatos"][id_formato] = formato
        guardar_json_peliculas()
    else:
        print(f"No se encontró la película con ID {id_pelicula}. No se pudo agregar el formato.")
    

def guardar_json_formatos():
    try:
        with open(os.path.join("data", "formatos.json"), 'w') as formato_json:
            json.dump(lista_formatos, formato_json, indent=2)
            print("La lista de los formatos ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no hayan actores guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. El formato podría ser incorrecto.")
    except Exception as e:
        print(f"Error desconocido: {e}")
        


def listar_formatos():
    print("Lista de los formatos creados")
    for formato in lista_formatos:
        print(formato)