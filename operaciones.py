"""Funciones básicas del inventario de bicicletas."""

ESTADOS_VALIDOS = ["Bueno", "Regular", "Dañado", "En reparación"]

def mostrar_inventario(inventario):
    """Muestra las bicicletas en formato de tabla."""
    if len(inventario) == 0:
        print("\nEl inventario está vacío.")
        return
    print("\n" + "=" * 86)
    print(f"{'CÓDIGO':<10} {'NOMBRE':<20} {'CANTIDAD':<10} {'ESTADO':<16} {'UBICACIÓN':<20}")
    print("-" * 86)
    for bicicleta in inventario:
        print(f"{bicicleta['codigo']:<10} {bicicleta['nombre']:<20} {bicicleta['cantidad']:<10} {bicicleta['estado']:<16} {bicicleta['ubicacion']:<20}")
    print("=" * 86)

def pedir_texto(mensaje):
    """Pide un texto que no puede estar vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("Error: este dato no puede quedar vacío.")

def pedir_cantidad(mensaje):
    """Pide una cantidad entera no negativa."""
    while True:
        try:
            cantidad = int(input(mensaje))
            if cantidad >= 0:
                return cantidad
            print("Error: la cantidad no puede ser negativa.")
        except ValueError:
            print("Error: la cantidad debe ser un número entero.")

def pedir_estado():
    """Pide un estado permitido."""
    while True:
        print("Estados: Bueno, Regular, Dañado, En reparación")
        estado = input("Estado: ").strip().lower()
        for estado_valido in ESTADOS_VALIDOS:
            if estado == estado_valido.lower():
                return estado_valido
        print("Error: el estado no es válido.")

def agregar_elemento(inventario):
    """Agrega una bicicleta como diccionario a la lista."""
    print("\n--- Agregar bicicleta ---")
    codigo = pedir_texto("Código: ")
    for bicicleta in inventario:
        if bicicleta["codigo"].lower() == codigo.lower():
            print("Error: ya existe una bicicleta con ese código.")
            return
    bicicleta = {
        "codigo": codigo,
        "nombre": pedir_texto("Nombre o modelo: "),
        "cantidad": pedir_cantidad("Cantidad: "),
        "estado": pedir_estado(),
        "ubicacion": pedir_texto("Ubicación: ")
    }
    inventario.append(bicicleta)
    print("Bicicleta agregada correctamente.")

def buscar_elemento(inventario):
    """Busca por código o nombre sin distinguir mayúsculas."""
    dato = pedir_texto("Código o nombre a buscar: ").lower()
    resultados = []
    for bicicleta in inventario:
        if dato in bicicleta["codigo"].lower() or dato in bicicleta["nombre"].lower():
            resultados.append(bicicleta)
    if len(resultados) == 0:
        print("No se encontró ninguna bicicleta con ese dato.")
    else:
        mostrar_inventario(resultados)

def editar_elemento(inventario):
    """Edita la cantidad o el estado al buscar por código."""
    codigo = pedir_texto("Código de la bicicleta a editar: ")
    for bicicleta in inventario:
        if bicicleta["codigo"].lower() == codigo.lower():
            print("1. Cambiar cantidad")
            print("2. Cambiar estado")
            opcion = input("Opción: ").strip()
            if opcion == "1":
                bicicleta["cantidad"] = pedir_cantidad("Nueva cantidad: ")
                print("Cantidad actualizada.")
            elif opcion == "2":
                bicicleta["estado"] = pedir_estado()
                print("Estado actualizado.")
            else:
                print("Opción no válida. No se realizaron cambios.")
            return
    print("No se encontró una bicicleta con ese código.")

def eliminar_elemento(inventario):
    """Busca y elimina una bicicleta con remove()."""
    codigo = pedir_texto("Código de la bicicleta a eliminar: ")
    for bicicleta in inventario:
        if bicicleta["codigo"].lower() == codigo.lower():
            inventario.remove(bicicleta)
            print("Bicicleta eliminada correctamente.")
            return
    print("No se encontró una bicicleta con ese código.")

def mostrar_estados(inventario):
    """Cuenta bicicletas por estado."""
    contador = {"Bueno": 0, "Regular": 0, "Dañado": 0, "En reparación": 0}
    for bicicleta in inventario:
        contador[bicicleta["estado"]] += 1
    print("\n--- Resumen por estado ---")
    for estado in ESTADOS_VALIDOS:
        print(estado + ":", contador[estado])
