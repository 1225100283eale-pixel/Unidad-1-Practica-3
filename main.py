"""
Proyecto: Inventario de bicicletas
Nombre del estudiante: Escribe tu nombre aquí
Grupo: Escribe tu grupo aquí
Descripción: Programa de consola para administrar bicicletas.
"""
import time
from datos import cargar_datos, guardar_datos
from operaciones import mostrar_inventario, agregar_elemento, buscar_elemento, editar_elemento, eliminar_elemento, mostrar_estados

def mostrar_menu():
    """Muestra el menú principal."""
    print("\n**********************************************")
    print("       INVENTARIO DE BICICLETAS")
    print("**********************************************")
    print("1. Agregar bicicleta")
    print("2. Mostrar inventario")
    print("3. Buscar bicicleta")
    print("4. Editar cantidad o estado")
    print("5. Eliminar bicicleta")
    print("6. Mostrar resumen por estado")
    print("7. Guardar datos")
    print("8. Guardar y salir")
    print("9. Salir sin guardar")
    print("**********************************************")

def main():
    """Ejecuta el menú con while, match-case y una pausa."""
    inventario = cargar_datos()
    print("\nBienvenido al inventario de bicicletas.")
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        match opcion:
            case "1":
                agregar_elemento(inventario)
                guardar_datos(inventario)
            case "2":
                mostrar_inventario(inventario)
            case "3":
                buscar_elemento(inventario)
            case "4":
                editar_elemento(inventario)
                guardar_datos(inventario)
            case "5":
                eliminar_elemento(inventario)
                guardar_datos(inventario)
            case "6":
                mostrar_estados(inventario)
            case "7":
                guardar_datos(inventario)
            case "8":
                guardar_datos(inventario)
                print("Gracias por usar el programa.")
                break
            case "9":
                print("Saliendo sin guardar cambios nuevos.")
                break
            case _:
                print("Opción no válida. Intenta otra vez.")
        time.sleep(1)

if __name__ == "__main__":
    main()
