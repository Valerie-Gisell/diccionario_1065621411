# Directorio de Contactos
# Programa para gestionar un directorio de contactos usando diccionarios anidados

def agregar_contacto(directorio):
    """Solicita los datos del contacto y lo agrega al directorio"""
    nombre = input("Nombre del contacto: ").strip()
    
    # Validar que el nombre no esté vacío
    if not nombre:
        print("❌ Error: El nombre no puede estar vacío\n")
        return
    
    # Verificar si el contacto ya existe
    if nombre in directorio:
        print(f"⚠️ El contacto '{nombre}' ya existe en el directorio\n")
        return
    
    email = input("Email: ").strip()
    if not email or "@" not in email:
        print("❌ Error: Por favor ingresa un email válido\n")
        return
    
    telefono = input("Teléfono: ").strip()
    if not telefono:
        print("❌ Error: El teléfono no puede estar vacío\n")
        return
    
    ciudad = input("Ciudad: ").strip()
    if not ciudad:
        print("❌ Error: La ciudad no puede estar vacía\n")
        return
    
    # Crear entrada anidada en el diccionario
    directorio[nombre] = {
        "email": email,
        "teléfono": telefono,
        "ciudad": ciudad
    }
    print(f"✅ Contacto '{nombre}' agregado exitosamente\n")


def ver_todos_contactos(directorio):
    """Itera sobre el directorio e imprime todos los contactos con sus datos"""
    if not directorio:
        print("📋 El directorio está vacío\n")
        return
    
    print("\n" + "="*70)
    print("📋 DIRECTORIO DE CONTACTOS")
    print("="*70)
    
    for nombre, datos in directorio.items():
        print(f"\n👤 {nombre}")
        print("-" * 70)
        for campo, valor in datos.items():
            campo_formateado = campo.capitalize()
            print(f"   {campo_formateado}: {valor}")
    
    print("\n" + "="*70 + "\n")


def buscar_por_nombre(directorio):
    """Busca un contacto por nombre usando .get() para evitar errores"""
    nombre = input("Nombre del contacto a buscar: ").strip()
    
    # Usar .get() para evitar KeyError
    contacto = directorio.get(nombre)
    
    if contacto is None:
        print(f"❌ El contacto '{nombre}' no se encuentra en el directorio\n")
        return
    
    print("\n" + "="*70)
    print(f"👤 DATOS DE {nombre.upper()}")
    print("="*70)
    for campo, valor in contacto.items():
        campo_formateado = campo.capitalize()
        print(f"   {campo_formateado}: {valor}")
    print("="*70 + "\n")


def actualizar_telefono(directorio):
    """Actualiza el teléfono de un contacto existente"""
    nombre = input("Nombre del contacto a actualizar: ").strip()
    
    # Verificar que el contacto existe
    if nombre not in directorio:
        print(f"❌ El contacto '{nombre}' no se encuentra en el directorio\n")
        return
    
    nuevo_telefono = input("Nuevo teléfono: ").strip()
    
    if not nuevo_telefono:
        print("❌ Error: El teléfono no puede estar vacío\n")
        return
    
    # Actualizar el teléfono en el diccionario anidado
    directorio[nombre]["teléfono"] = nuevo_telefono
    print(f"✅ Teléfono de '{nombre}' actualizado a: {nuevo_telefono}\n")


def eliminar_contacto(directorio):
    """Elimina un contacto del directorio usando .pop()"""
    nombre = input("Nombre del contacto a eliminar: ").strip()
    
    # Usar .pop() para eliminar el contacto de forma segura
    contacto_eliminado = directorio.pop(nombre, None)
    
    if contacto_eliminado is None:
        print(f"❌ El contacto '{nombre}' no se encuentra en el directorio\n")
        return
    
    print(f"✅ Contacto '{nombre}' ha sido eliminado del directorio\n")


def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*70)
    print("📞 DIRECTORIO DE CONTACTOS")
    print("="*70)
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar por nombre")
    print("4. Actualizar teléfono")
    print("5. Eliminar contacto")
    print("6. Salir")
    print("="*70)


def main():
    """Función principal del programa"""
    directorio = {}
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            agregar_contacto(directorio)
        elif opcion == "2":
            ver_todos_contactos(directorio)
        elif opcion == "3":
            buscar_por_nombre(directorio)
        elif opcion == "4":
            actualizar_telefono(directorio)
        elif opcion == "5":
            eliminar_contacto(directorio)
        elif opcion == "6":
            print("👋 ¡Gracias por usar el Directorio de Contactos!")
            break
        else:
            print("❌ Opción no válida. Por favor, selecciona una opción del 1 al 6\n")


if __name__ == "__main__":
    main()
