#EJERCICIO N° 1

# Dado el diccionario precios_frutas:  precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios:
#● Naranja = 1200
#● Manzana = 1500
#● Pera = 2300

#Definimos el diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(f"\n Frutas (diccionario original): {precios_frutas} \n")

#Agregamos las frutas con sus precios (keys y value)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Mostramos el diccionario de frutas con lo que agregamos. 
print(f"Diccionario de frutas actualizado: {precios_frutas}\n")

#EJERCICIO N° 2 

#Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas:
#● Banana = 1330
#● Manzana = 1700
#● Melón = 2800

#Actualizamos los valores de las frutas (actualizamos los value y no los keys)
precios_frutas['Banana']= 1330
precios_frutas['Manzana']= 1700
precios_frutas['Melón']= 2800

print(f"Los precios actualizados de las frutas son: {precios_frutas}\n")

#EJERCICIO 3 

# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior,
# crear una lista que contenga únicamente las frutas sin los precios.

print(f"Listado de frutas: {precios_frutas.keys()}")


# EJERCICIO N° 4

#  Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.

#Definición de funciones
def agregar_contacto (nombre , telefono):
    contactos[nombre] = telefono

#Creamos un diccionario vacio 
contactos = {}

print("\n Guia de contactos telefónicos \n")

#Permitimos al usuario cargar 5 contactos validamos las entradas 

for _ in range (5):
    nombre= input("Ingrese el nombre: ")
    while nombre.isdigit():
        print ("Error, el nombre no puede contener números: \n")
        nombre= input("Ingrese el nombre: ")

    telefono = input("Ingrese el número de teléfono (sin espacios, ni guiones: )\n")
    while not (telefono.isdigit()):
        print ("Error, el número de teléfono debe contener solo dígitos: \n")
        telefono = input ("Ingrese el número de teléfono (sin espacios, ni guiones: )\n")

    agregar_contacto(nombre, telefono)

#Buscamos el contactos

nombre_buscar= input("Ingrese el nombre para mostrar su número telefonico: ")

if nombre_buscar in contactos:
    print (f"El núemro de telefono de {nombre_buscar} es: {contactos[nombre_buscar]}")
else: 
    print(f"El contacto {nombre_buscar} no se encuentra en la guia de teléfonos.")

#EJERCICIO N°5
#Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.


#Solicitamos al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

#Separamos la frease en palabras y crea una lista 

palabras = frase.split()

# Creamos un conjunto con las palabras separadas pero no repetidas

palabras_separadas = set(palabras)

# Creamos un diccionario
recuento = {}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] +=1
    else:
        recuento[palabra] = 1

#Mostramos 

print (f"\n Palabras únicas: {palabras_separadas}")
print (f"\n Recuento: {recuento}")

#EJERCICIO N°6

# EJERCICIO N° 6
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. Ejemplo:

#Creamos un diccionario que mostrará el alumno y su promedio.
alumnos = {}


for i in range (3):
    nombres = input (f"Ingrese el nombre {i + 1}: ")
    listas_notas = []

    for contador in range (3):

        notas = int(input(f"Ingrese la nota N° {contador + 1} de {nombres}: "))
        listas_notas.append(notas)

        #guardamos en el diccionario.
    alumnos[nombres] = tuple(listas_notas)

        
# Mostramos los alumnos con sus notas
print("\n Diccionario de alumnos y sus notas: ")
print(alumnos)

# Mostramos los promedios
print("\n Los promedios: \n")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")


#EJERCICIO N° 7
#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


parcial_1= {1, 2, 3, 4, 5}
parcial_2 = {4, 5, 6, 7, 8}

#• Mostrá los que aprobaron ambos parciales.
ambos= parcial_1 & parcial_2

#• Mostrá los que aprobaron solo uno de los dos.
solo_uno= parcial_1 ^ parcial_2

#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

almenos_uno = parcial_1| parcial_2


#Mostramos los resultados

print(f"Alumnos que aprobaron ambos parciales: {ambos}\n")
print(f"Alumnos que aprobaron solo uno de los parciales: {solo_uno}")
print(f"Alumnos totales que aprobaron almenos uno: {almenos_uno}")

#EJERICIO N° 8

# Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#• Consultar el stock de un producto ingresado.
#• Agregar unidades al stock si el producto ya existe.
#• Agregar un nuevo producto si no existe.



#Definición de funciones para validar
def validar_entero_positivo(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        else:
            print("Ingrese un número válido mayor que 0.")

def validar_nombre_producto(mensaje):
    while True:
        nombre = input(mensaje).strip().lower()
        # .replace(" ", "") permite productos con espacios como "agua mineral"
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print("El nombre no puede contener números ni símbolos. Intente de nuevo.")


#Diccionario de productos 
productos={
    'detergente': 10, 
    'arroz': 6, 
    'papas': 12
    }

#Solicitamos que ingrese el nombre del producto
producto= validar_nombre_producto("Ingresa el nombre del producto: ")
    

# Si el producto se encuentra en productos mostramos stock - agregamos al stock 
# Si no está agregos producto nuevo.

if producto in productos:
        print(f"El stock de {producto} es: {productos[producto]} unidades.")
        print("Actualizar stock: ")
        
        cantidad = validar_entero_positivo("Por favor ingrese la cantidad para actualizar: ")
        productos[producto] += cantidad
        print(f"El nuevo stock de {producto} es: {productos[producto]} unidades.")
else: 
        print("El producto no se encuentra en el stock")
        stock_nuevo = validar_entero_positivo("Producto nuevo. Por favor ingrese la cantidad de unidades: ")
        productos[producto]= stock_nuevo
        print(f"El producto {producto} agregrado con {stock_nuevo} unidades.")


#EJERCICIO N° 9
#  Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:
#Permití consultar qué actividad hay en cierto día y hora.

#Diccionario de agenda

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "18:00"): "Dentista",
    ("viernes", "14:00"): "Clase de inglés"
    }

dia = input("Ingresa el día a consultar: ").lower()
hora = input("Ingresa la hora a consultar (ej. 12:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"La actividad es: {agenda[clave]}")
else:
    print("No hay actividades programadas para ese día.")
    
#EJERCICIO N°10
#Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#• Las capitales sean las claves.
#• Los países sean los valores.

#Creamos el diccionario
pasies_capitales = {
    "Argentina": "Buenos Aires",
    "Canadá": "Ottawa",
    "España": "Madrid"
}

#Creamos un diccionario vacio donde vamos a guardar el invertido
capitales_paises={}

#Recorremos con un for el diccionario 
for pais, capital in pasies_capitales.items():
    capitales_paises[capital]=pais

#Mostramos el nuevo diccionario invertido
print(f"\n Original {pasies_capitales}\n")
print(f"\nInvertido: {capitales_paises}\n")


    



















