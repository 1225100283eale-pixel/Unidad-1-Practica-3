"""Funciones para leer y guardar el inventario."""
import json

ARCHIVO_DATOS = "dispositivos.json"

def cargar_datos():
    """Carga los datos del archivo JSON."""
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            print("El archivo no tiene una lista. Se iniciará vacío.")
    except FileNotFoundError:
        print("No existe el archivo. Se iniciará un inventario vacío.")
    except json.JSONDecodeError:
        print("El JSON está vacío o tiene errores. Se iniciará vacío.")
    except Exception as error:
        print("Error al cargar los datos:", error)
    return []

def guardar_datos(inventario):
    """Guarda la lista del inventario en JSON."""
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(inventario, archivo, indent=4, ensure_ascii=False)
        print("Datos guardados correctamente.")
    except Exception as error:
        print("No fue posible guardar los datos:", error)
