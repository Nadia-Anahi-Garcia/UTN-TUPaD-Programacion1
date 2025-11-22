

#EJERCICIO N°1
# Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
#Cada línea debe tener: nombre,precio,cantidad

def crear_archivo_inicial():
    """Crea el archivo productos.txt con productos iniciales."""
    import os
    if not os.path.exists("productos.txt"):
        with open("productos.txt", "w") as archivo:
            archivo.write("mesa,20000,6 \n")
            archivo.write("silla,30000,7\n")
            archivo.write("armario,12000,10\n")


#EJERCICIO N°2
# Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

def mostrar_productos():
    """Muestra los productos almacenados en productos.txt."""
    with open("productos.txt", "r") as archivo:
        for linea in archivo: #Recorremos y leemos cada línea del archivo.
            datos = linea.strip().split(",") #Le quitamos espacios y separamos los datos 
            print(f"Producto: {datos[0]} | Precio: $ {float(datos[1]):.2f} | Cantidad: {datos[2]}") #Mostramos. 

#EJERCICIO N°3
# Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, 
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad)
# y lo agregue al archivo sin borrar el contenido existente.


def agregar_producto():
    """Agrega un nuevo producto al archivo productos.txt."""
    nombre = input("Ingrese el nombre del producto: ").lower().strip()
    
    #Validamos si el producto ya existe
    productos_existentes = cargar_productos()
    for p in productos_existentes:
        if p["nombre"].strip().lower() == nombre:
            print(" El producto ya existe. No se puede agregar.")
            return
    precio = input("Ingrese el precio: ").strip()
    cantidad = input("Ingrese la cantidad: ").strip()
    # Agregamos el nuevo producto al archivo
    with open("productos.txt", "a") as archivo:
        archivo.write (f"{nombre},{precio},{cantidad}\n")

    print(" El producto agregado correctamente.")


#EJERCICIO N°4
# Cargar productos en una lista de diccionarios: Al leer el archivo, 
# cargar los datos en una lista llamada productos, donde cada elemento sea un 
# diccionario con claves: nombre, precio, cantidad.

#Creamos una lista vacia donde luego estarán los datos 

def cargar_productos():
    """Carga los productos desde productos.txt en una lista de diccionarios."""
    productos = []
    with open ("productos.txt", "r") as archivo:
        for linea in archivo: #recorremos 
            datos = linea.strip().split(",") 
            producto = {        #creamos un diccionario con los elemntos. 
                "nombre": datos[0],
                "precio": float(datos[1]),
                "cantidad": int(datos[2]),  
                }
        # Agregarlo a la lista
            productos.append(producto)
    return productos

# Ejerccio N°5
# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
#Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
#Si no existe, mostrar un mensaje de error.

def buscar_producto_por_nombre(productos):
    """Busca un producto por nombre en la lista de productos."""
#Solicitamos al usuario que ingrese el nombre del producto a buscar
    buscar_producto= input("Ingrese el nombre del producto a buscar: ").strip().lower()
    #Buscamos el producto
    busqueda = False
    for i in productos:
        if i["nombre"].strip().lower() == buscar_producto:
            print(f"Producto: {i['nombre']} | Precio: ${i['precio']} | Cantidad: {i['cantidad']}")
            busqueda = True
            break
    #Si el producto ingresado no esta muestra error 
    if not busqueda:
        print("El producto no existe")

#Ejercicio N°6 
# Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

def guardar_productos(productos):
    """Guarda la lista completa de productos en productos.txt."""
    with open("productos.txt", "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    
# Programa principal
crear_archivo_inicial() #Crear el archivo inicial si no existe

while True:
    print("\n------- Menú de opciones ------\n")
    print("1. Mostrar los productos")
    print("2. Agregar un producto")
    print("3. Buscar producto por nombre")
    print("4. Guardar y salir del programa")

    opcion_menu = input("\nSeleccione una opción (1-4): ")
    match opcion_menu:
        case "1":
            mostrar_productos()
        case "2":
            agregar_producto()
        case "3":
            productos = cargar_productos()
            buscar_producto_por_nombre(productos)
        case "4":
            productos = cargar_productos()
            guardar_productos(productos)
            print(" Saliendo del programa.")
            break
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")