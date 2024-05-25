from utilidades.utils import validar_opcion

def menu_principal():
    print("----------- Menú de gestor de películas BlockBuster-----------")
    print("1. Administrador de géneros")
    print("2. Administrador de actores")
    print("3. Administrador de formatos")
    print("4. Gestor de informes")
    print("5. Gestor de películas")
    print("6. Salir")      
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_generos():
    print("----------- Gestor de géneros-----------")
    print("1. Crear género")
    print("2. listar géneros")
    print("3. Ir al menú principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_actores():
    print("----------- Gestor de actores-----------")
    print("1. Crear actor")
    print("2. Listar actor")
    print("3. Ir al menú principal")
    op=validar_opcion("Opcion: ",1,3)
    return op
    
def menu_formatos():
    print("----------- Gestor de formatos-----------")
    print("1. Crear formatos")
    print("2. Listar formatos")
    print("3. Ir al menú principal")
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_peliculas():
    print("----------- Gestor de películas-----------")
    print("1. Agregar película")
    print("2. Editar película")
    print("3. Eliminar película")
    print("4. Eliminar actor")
    print("5. Buscar película")
    print("6. Listar todas las películas")
    print("7. Ir al menú principal")
    op=validar_opcion("Opcion: ",1,7)
    return op

def menu_informes():
    print("----------- Gestor de informes-----------")
    print("1. Listar las películas de un género específico")
    print("2. Listar películas donde le protagonista sea Silverster Stallone")
    print("3. Buscar películas y mostrar la sinopsis y los actores")
    print("4. Ir al menú principal")
    op=validar_opcion("Opcion: ",1,4)
    return op