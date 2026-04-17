# Gestor de Compras
# Programa para gestionar una lista de artículos de compra

def agregar_articulo(lista_compras):
    """Solicita los datos del producto y lo agrega a la lista"""
    producto = input("Nombre del producto: ").strip()
    
    # Validar que el precio sea un número
    try:
        precio = float(input("Precio del producto: $"))
    except ValueError:
        print("❌ Error: El precio debe ser un número")
        return
    
    # Validar que la cantidad sea un número positivo
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("❌ Error: La cantidad debe ser mayor a 0")
            return
    except ValueError:
        print("❌ Error: La cantidad debe ser un número entero")
        return
    
    # Crear diccionario y agregarlo a la lista
    articulo = {
        "producto": producto,
        "precio": precio,
        "cantidad": cantidad
    }
    lista_compras.append(articulo)
    print(f"✅ '{producto}' agregado a la lista\n")


def ver_lista_compras(lista_compras):
    """Muestra todos los artículos de la lista de compras"""
    if not lista_compras:
        print("📋 La lista de compras está vacía\n")
        return
    
    print("\n" + "="*60)
    print("📋 LISTA DE COMPRAS")
    print("="*60)
    
    for i, articulo in enumerate(lista_compras, 1):
        for clave, valor in articulo.items():
            if clave == "precio":
                print(f"  {clave.capitalize()}: ${valor:.2f}")
            else:
                print(f"  {clave.capitalize()}: {valor}")
        print("-" * 60)
    print()


def calcular_total(lista_compras):
    """Calcula el total de la compra sumando precio × cantidad"""
    if not lista_compras:
        print("❌ La lista está vacía. No hay nada que calcular\n")
        return
    
    total = 0
    print("\n" + "="*60)
    print("💰 DESGLOSE DE COSTOS")
    print("="*60)
    
    for articulo in lista_compras:
        subtotal = articulo["precio"] * articulo["cantidad"]
        print(f"{articulo['producto']}: ${articulo['precio']:.2f} × {articulo['cantidad']} = ${subtotal:.2f}")
        total += subtotal
    
    print("="*60)
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("="*60 + "\n")


def eliminar_articulo(lista_compras):
    """Busca y elimina un artículo de la lista por nombre"""
    if not lista_compras:
        print("❌ La lista de compras está vacía\n")
        return
    
    producto_a_eliminar = input("Nombre del producto a eliminar: ").strip()
    
    # Buscar y eliminar el artículo
    for articulo in lista_compras:
        if articulo["producto"].lower() == producto_a_eliminar.lower():
            lista_compras.remove(articulo)
            print(f"✅ '{producto_a_eliminar}' ha sido eliminado\n")
            return
    
    print(f"❌ Producto '{producto_a_eliminar}' no encontrado en la lista\n")


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*60)
    print("🛒 GESTOR DE COMPRAS")
    print("="*60)
    print("1. Agregar artículo")
    print("2. Ver lista de compras")
    print("3. Calcular total")
    print("4. Eliminar artículo")
    print("5. Salir")
    print("="*60)


def main():
    """Función principal del programa"""
    lista_compras = []
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_articulo(lista_compras)
        elif opcion == "2":
            ver_lista_compras(lista_compras)
        elif opcion == "3":
            calcular_total(lista_compras)
        elif opcion == "4":
            eliminar_articulo(lista_compras)
        elif opcion == "5":
            print("👋 ¡Gracias por usar el Gestor de Compras!")
            break
        else:
            print("❌ Opción no válida. Por favor, selecciona una opción del 1 al 5\n")


if __name__ == "__main__":
    main()
