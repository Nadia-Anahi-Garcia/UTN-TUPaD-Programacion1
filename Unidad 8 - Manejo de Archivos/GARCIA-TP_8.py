#EJERCICIO N°1
# Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
#Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("mesa,20000,6 \n")
    archivo.write("silla,30000,7\n")
    archivo.write("armario,12000,10\n")


#EJERCICIO N°2
# Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt", "r") as archivo:
    for linea in archivo: #Recorremos y leemos cada línea del archivo.
        datos = linea.strip().split(",") #Le quitamos espacios y separamos los datos 
        print(f"Producto: {datos[0]} | Precio: {datos[1]} | Cantidad: {datos[2]}") #Mostramos. 

#EJERCICIO N°3
# Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, 
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad)
# y lo agregue al archivo sin borrar el contenido existente.

#Solicitamos que el usuario ingrese los datos.
print("Nuevos productos")
nombre = input("Ingrese el nombre del producto: ").lower
precio = input("Ingrese el precio: ")
cantidad = input("Ingrese la cantidad: ")

#Luego los agregamos al archivo 
with open("productos.txt", "a") as archivo:
    archivo.write (f"{nombre},{precio},{cantidad}\n")

#EJERCICIO N°4
# Cargar productos en una lista de diccionarios: Al leer el archivo, 
# cargar los datos en una lista llamada productos, donde cada elemento sea un 
# diccionario con claves: nombre, precio, cantidad.

#Creamos una lista vacia donde luego estarán los datos 
productos = []

with open ("productos.txt", "r") as archivo:
    for linea in archivo: #recorremos 
        datos = linea.strip().split(",") 
        producto = {        #creamos un diccionario con los elemntos. 
            "nombre": datos[0],
            "precio": float(datos[1]),
            "cantidad": int(datos[2])
            }
        # Agregarlo a la lista
        productos.append(producto)

# Ejerccio N°5
# Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
#Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. 
#Si no existe, mostrar un mensaje de error.

#Solicitamos al usuario que ingrese el nombre del producto a buscar
buscar_producto= input("Ingrese el nombre del producto a buscar: ").strip().lower()

#Buscamos el producto
busqueda = False
for i in productos:
    if i["nombre"].strip().lower() == buscar_producto:
        print(f"Producto:  {i["nombre"]} | Precio: ${i["precio"]} | Cantidad: {i["cantidad"]}")
        busqueda = True
#Si el producto ingresado no esta muestra error 
if not busqueda:
    print("El producto no existe")

#Ejercicio N°6 
# Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

with open("productos.txt", "w") as archivo: 
    for p in productos:
        linea = (f"{i["nombre"]},{i["precio"]},{i["cantidad"]}")
        archivo.write(linea)



