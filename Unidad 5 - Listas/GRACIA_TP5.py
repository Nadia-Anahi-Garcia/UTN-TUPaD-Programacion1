#Ejercicio 1
#Crear una lista con las notas de 10 estudiantes.
#Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
#•Mostrar la lista completa.
#•Calcular y mostrar el promedio.
#•Indicar la nota más alta y la más baja.

#Obtenemos la lista de notas
notas = [4, 7, 8, 5, 6, 9, 10, 3, 2, 1]
#Inicializamos las variables
suma= 0
nota_mas_alta = notas[0]
nota_mas_baja = notas[0]
#Mostramos la lista de notas y calculamos la suma, nota más alta y más baja
print("La lista de notas es: ",end="")
for nota in notas:
    suma += nota
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    elif nota < nota_mas_baja:
        nota_mas_baja = nota
    print(nota) 
#calculamos el promedio y mostramos los resultados
promedio = suma / len(notas)
print(f"Promedio de notas: {promedio:.2f}")
print(f"La nota más baja es: {nota_mas_baja}")
print(f"La nota más alta es: {nota_mas_alta}")

#-----------------------------------------------------------------

#Ejercicio 2
#Pedir al usuario que cargue 5 productos en una lista.
#Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#Preguntar al usuario qué producto desea eliminar y actualizar la lista.

#Inicializamos la lista de productos

productos = []

#Cargamos la lista de productos con lo que ingresa el usuario
for contador in range(5):
    producto= input(f"Ingrese el producto {contador+1}: ")
    productos.append(producto)

#Mostramos la lista original
print(f"La lista original de productos es: ")
print(productos)

#Mostramos la lista ordenada alfabéticamente
print("La lista de productos ordenadas es: ")
print(sorted(productos)) 

#Solicitamos el producto a eliminar y actualizamos la lista
producto_eliminar=input("¿Qué producto desea eliminar?: ")

#Verificamos si el producto está en la lista antes de eliminarlo
if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print(f"El producto{producto_eliminar} fue eliminado de la lista.")
else:
    print(f"El producto {producto_eliminar} no se encuentra en la lista.")

#Mostramos la lista actualizada
print(f"La lista actualizada de productos es: {productos}")

#-----------------------------------------------------------------


#Ejercicio 3
#Generar una lista con 15 números enteros al azar entre 1 y 100.
#Crear una lista con los pares y otra con los impares.
#Mostrar cuántos números tiene cada lista.


import random

#Generamos la lista de números aleatorios, previo inicializamos la lista
numeros = []
numeros_pares = []
numeros_impares = []

#Mostramos la lista de números aleatorios
for contador in range(15):
    azar = random.randint(1, 100)
    numeros.append(azar)
print(f"La lista de números aleatorios es: {numeros}")

#Separamos los números pares e impares
for numero in numeros:
    if (numero % 2 == 0):
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

#Mostramos la cantidad de números que tiene cada lista  
print(f"La lista de números pares tiene {len(numeros_pares)} números.")
print(f"Los números pares son {numeros_pares}", end="\n\n")
print(f"La lista de números impares tiene {len(numeros_impares)} números.")         
print(f"La lista de números impares {numeros_impares}", end="\n\n")


#-----------------------------------------------------------------

#Ejercicio 4 
#Dada una lista con valores repetidos:
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3 ]
#Crear una nueva lista sin elementos repetidos.
#• Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3 ]
lista_sin_repetidos = []

for i in datos:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)

#Mostramos la lista sin números repetidos
print("Los números de la lista original son:", end=" " )
for i in datos:
    print(i, end=" ")
print()

#Mostramos la lista sin números repetidos
print("Los números de la lista sin repetidos son:", end=" " )   
for i in lista_sin_repetidos:
    print(i, end=" ")
print()


#-----------------------------------------------------------------


#Ejericio 5
#Crear una lista con los nombres de 8 estudiantes presentes en clase.
#•Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#•Mostrar la lista final actualizada.


estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Pedro"]

print("Lista inicial de estudiantes:")
for i in estudiantes:
    print(i, end=", ")
print("\n") 

agregar_o_eliminar = input("Indique si desea Agregar (A) o Eliminar (E) un nombre: ").strip().upper()

if agregar_o_eliminar == 'A':
    nuevo_estudiante = input("Ingresa el nombre del nuevo estudiante: ").strip().capitalize()
    estudiantes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} ha sido agregado a la lista.")   
elif agregar_o_eliminar == 'E':
        estudiante_a_eliminar = input("Ingresa el nombre del estudiante a eliminar: ").strip().capitalize()
        if estudiante_a_eliminar in estudiantes:
            estudiantes.remove(estudiante_a_eliminar)
            print(f"{estudiante_a_eliminar} ha sido eliminado de la lista.")
        else:
            print(f"{estudiante_a_eliminar} no se encuentra en la lista.")

print("Lista final de estudiantes:")
for i in estudiantes:
    print(i, end=", ")  

#-----------------------------------------------------------------

#Ejericio 6
#Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
# (el último pasa a ser el primero).

lista_numeros = [10, 20, 30, 40, 50, 60, 70]

numero_len = len(lista_numeros)

for i in range((numero_len -1), 0, -1):
    lista_numeros[i], lista_numeros[i-1] = lista_numeros[i-1], lista_numeros[i]

print("Lista rotada hacia la derecha:")
for num in lista_numeros:           
    print(num, end=" ")

#-----------------------------------------------------------------

#Ejercicio 7 
#Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#Calcular el promedio de las mínimas y el de las máximas.
#Mostrar en qué día se registró la mayor amplitud térmica.

matiz_temperaturas = [[15, 25], [17, 27], [14, 30], [20, 35], [18, 28], [16, 26], [19, 29]]

for i in matiz_temperaturas:
    print (i)

suma_minimas = 0
suma_maximas = 0

for i in range(len(matiz_temperaturas)):
    suma_minimas += matiz_temperaturas[i][0]
    suma_maximas += matiz_temperaturas[i][1]

promedio_minimas = suma_minimas / len(matiz_temperaturas)
promedio_maximas = suma_maximas / len(matiz_temperaturas)

print(f"El promedio de las temperaturas mínimas es: {promedio_minimas}")
print(f"El promedio de las temperaturas máximas es: {promedio_maximas}")

#-----------------------------------------------------------------

#Ejercicio 8
#Crear una matriz con las notas de 5 estudiantes en 3 materias.
#Mostrar el promedio de cada estudiante.
#Mostrar el promedio de cada materia.

notas = [
    [85, 90, 78],   #Estudiante 1
    [88, 76, 92],   #Estudiante 2
    [90, 91, 85],   #Estudiante 3
    [70, 80, 75],   #Estudiante 4
    [95, 89, 94]]   #Estudiante 5

#Mostramos la matriz de notas
for fila in notas:
    print(fila, end=" ")
    print()

#Calculamos y mostramos el promedio por estudiante
suma = 0
for i in range(5):  # i son los 5 estudiantes
    for j in range(3): # j son las materias 
        suma += notas[i][j]
        promedio_estudiante = suma / 3
print(f"El promedio del estudiante {i + 1} es: {promedio_estudiante}")

#Calculamos y mostramos el promedio por materia
suma_materia = 0
for j in range(3):
    for i in range(5):
        suma_materia += notas[i][j]
        promedio_materia = suma_materia / 5
print(f"El promedio de la materia {j + 1} es: {promedio_materia}")

#-----------------------------------------------------------------

#Ejercicio 9

#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#Inicializarlo con guiones "-" representando casillas vacías.
#Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#Mostrar el tablero después de cada jugada.

#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
tablero = []

for i in range(3):
    fila = []
    for j in range(3):
        fila.append("-")
    tablero.append(fila)

for fila in tablero:
    for elemento in fila:
        print(elemento, end=" ")
    print()

# Jugadores

jugador = "X"
jugadas = 0 


while jugadas < 9:
    print (f" Turno del jugador {jugador}")

    fila = int(input("Ingrese la fila (0-2): "))
    columna= int(input("Ingrese la columna (0-2): "))
    if (fila <0) or (fila >2) or (columna <0) or (columna >2):
        print ("Fuera de juego")
        continue 

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugadas += 1
    else:
        print ("La casilla está ocupada, intenta de nuevo")
        continue
    for fila in tablero:
        for elemento in fila:
            print(elemento, end=" ")
        print()

    if jugador == "X":
        jugador = "O"
    else: 
        jugador = "X"

#-----------------------------------------------------------------

#Ejercicio 10

#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#Mostrar el total vendido por cada producto.
#Mostrar el día con mayores ventas totales.
#Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [12, 45, 78, 23, 56, 89, 34], # producto 1
    [67, 90, 11, 44, 77, 22, 55], # Producto 2
    [88, 33, 66, 99, 21, 54, 87], # Producto 3 
    [10, 43, 76, 19, 52, 85, 28]  # Producto 4
]

# mostrar el total vendido por producto 
producto_totales= []   #Guardando los totales de cada producto por semana

for i in range (4):     #i son las Filas 
    total_producto = 0
    for j in range (7):  # j son las columnas 
        total_producto += ventas[i][j]
    producto_totales.append (total_producto)   
    print (f"El total del producto {i+1}: {total_producto}")
print ()


#Mostrar el día con mayores ventas totales.

ventas_mayor = 0
dia_mayor = 0

for j in range (7):
    total_del_dia = 0 
    for i in range (4):
        total_del_dia += ventas [i][j]
    print (f"El total del dia {j+1} es : {total_del_dia}")
    if total_del_dia > ventas_mayor: 
        ventas_mayor = total_del_dia
        dia_mayor = j+1
print ()

print(f"El dia con mayores ventas fue {dia_mayor} con {ventas_mayor}")

#Indicar cuál fue el producto más vendido en la semana.

mayor_producto = 0
indice = 0

for i in range (4):
    if producto_totales[i] > mayor_producto:
        mayor_producto = producto_totales[i]
        indice = i+1

print ()

print (f"El producto más vendido fue el {indice}, con {mayor_producto} ventas en la semana.")




