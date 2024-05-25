from businnes.peliculas import lista_peliculas

from businnes.peliculas import lista_peliculas

def listar_peliculas_por_genero():
    tipo_genero = input("Ingrese el tipo de género a buscar: ")

    peliculas_encontradas = []

    for pelicula in lista_peliculas:
        generos_pelicula = pelicula.get("Generos", [])
        for genero_info in generos_pelicula:
            if tipo_genero.lower() in genero_info[0].get('Tipo de genero', '').lower():
                peliculas_encontradas.append(pelicula)
                break

    if peliculas_encontradas:
        print(f"Películas encontradas para el género '{tipo_genero}':")
        for pelicula in peliculas_encontradas:
            print(f"ID: {pelicula['Id']}, Nombre: {pelicula['Nombre pelicula']}")
    else:
        print(f"No se encontraron películas para el género '{tipo_genero}'.")


def listar_peliculas_por_actor():
    nombre_actor = input("Ingrese el nombre del actor a buscar: ")

    peliculas_encontradas = []

    for pelicula in lista_peliculas:
        actores_pelicula = pelicula.get("Actores", [])
        for actor_info in actores_pelicula:
            if nombre_actor.lower() in actor_info[0].get('Nombre Actor', '').lower():
                peliculas_encontradas.append(pelicula)
                break

    if peliculas_encontradas:
        print(f"Películas encontradas para el actor '{nombre_actor}':")
        for pelicula in peliculas_encontradas:
            print(f"ID: {pelicula['Id']}, Nombre: {pelicula['Nombre pelicula']}")
    else:
        print(f"No se encontraron películas para el actor '{nombre_actor}'.")
        
        
def buscar_pelicula_mostrar_info():
    id_pelicula = input("Ingrese el ID de la película a buscar: ")

    pelicula_encontrada = None
    for pelicula in lista_peliculas:
        if pelicula.get('Id') == id_pelicula:
            pelicula_encontrada = pelicula
            break

    if pelicula_encontrada:
        print(f"Información de la película con ID '{id_pelicula}':")
        print(f"Nombre: {pelicula_encontrada.get('Nombre pelicula')}")
        print(f"Duración: {pelicula_encontrada.get('Duracion')}")
        print(f"Sinopsis: {pelicula_encontrada.get('Sinopsis')}")

        actores = pelicula_encontrada.get("Actores", [])
        if actores:
            print("Actores:")
            for actor_info in actores:
                print(f"  - Nombre: {actor_info['Nombre Actor']}, Rol: {actor_info['Rol']}")
    else:
        print(f"No se encontró una película con el ID '{id_pelicula}'.")