#Ejercicio 1: 
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

#Solicitamos que el usuario ingrese su edad.
edad = int(input("Por favor, ingrese su edad:"))

#Asignamos a una variable la edad limite, también podriamos directamente poner 18 en la condición
#Es más fácil modidificar la variable que buscar en el código. 
edadlimite=18

#Validamos los datos ingresados, luego la condicion si es mayor de edad y lo mostramos por pantalla.
if edad < 0: 
    print("Por favor, ingrese una edad correcta:")
elif edad >= edadlimite:
    print("Es mayor de edad")



#Ejercicio 2: 
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

#Solicitamos que ingrese su nota 
nota = int(input("Por favor, ingrese su nota (0 a 10): "))

#Validamos que los datos ingresados esten en el rango 0 a 10 (el rango de notas), evaluamos la condicion,
#Mostramos por pantalla si esta aprobado o desaprobado.
if (nota < 0) or (nota > 10):
    print("Por favor, ingrese un número del 0 al 10.")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3: 
#Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 

#Solicitamos que se ingrese un número.
numero = int(input("Por favor ingrese un número: "))

#Por meido de la del mod podemos ver si es par o no. Lo mostramos por pantalla.
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else: 
    print("Por favor, ingrese un número par.")



#Ejercicio 4:
#Escribir un programa que solicite al usuario su edad e imprima por pantalla 
# a cuál de las siguientes categorías pertenece:
#  ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años.
#  ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.


#Solicitamos que ingrese la edad.
edad2 = int(input("Por favor, ingrese su edad: "))

#Validamos el ingreso del número, luego a que categoría pertenece y mostramos por pantalla. 
if edad2 < 0:
    print ("Ingrese una edad valida.")
elif edad2 < 12:
    print("Perteneces a la categoría Niño/a.")
elif edad2 < 18:
    print("Perteneces a la categoría Adolescente.")
elif edad2 < 30:
    print("Perteneces a la categoría Adulto/a joven.")
else:
    print("Perteneces a la categoría Adulto/a.")


#Ejercicio 5:
#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
#Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el 
# mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor,
#  ingrese una contraseña de entre 8 y 14 caracteres".

#Solicitamos que ingrese una clave.
clave = input("Por favor ingrese su contraseña (8 a 14 caracteres): ")

#Le asignamos a la variable la cantidad de caracteres que tiene para luego evaluar. 
validacion = len(clave)

#Evaluamos la condición y mostramos por pantalla. 
if (validacion >= 8) and (validacion  <= 14):
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio 6
#Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana
#  y su media y las compare para determinar si hay 
# sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

#Primero importamos la funsión de media, mediana y moda según material provisto. 
from statistics import mean, median, mode
#Importamos los números aleatorios según material provisto.
import random
numeros_aleatorios = [random.randint(1,100)for i in range (50)]

#Cálculamos cada una
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Mostramos por pantalla cada una y también los números aleatorios.
print(f"Los números son: {numeros_aleatorios}")
print(f"La media: {media:.2f}")
print(f"La mediana: {mediana:.2f}")
print(f"La moda: {moda:.2f}")

#Luego comparamos según como estaba en el pdf la definisión de cada sosego. 
if media > mediana > moda:
    print ("Hay sosego positivo o a la derecha.")
elif media < mediana < moda:
    print ("Hay sosego negativo o a la izquierda.")
elif media == mediana == moda:
    print ("No hay sosego.")
else:
    print("El sosego no está definido.")




#Ejercicio 7
#Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

#Solicitamos que ingrese una frase.
palabra = input("Ingrese su frase: ")

#Nos trae la última letra. 
ultima_letra = palabra[-1]

#Lista de las vocales
vocales = ["a","e","i","o","u"]

#Evaluamos y mostramos.
if ultima_letra.lower() in vocales:
    print(f"{palabra}!")
else:
    print (palabra)


#Ejercicio 8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
# dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada 
# por el usuario e imprimir el resultado por pantalla

#Solicitamos que el usuario ingrese su nombre y la opción.
nombre1 = input("Ingrese su nombre:")
num = int(input(
    "Ingrese un número según la opción deseada:\n"
    "1. Nombre en MAYÚSCULAS\n"
    "2. Nombre en minúsculas\n"
    "3. Nombre con la primera letra en mayúscula\n"
    "Opción: "))

#Validamos el ingreso de las opciones pedida y evaluamos la condición, cuando haya ingresado bien el número. 
if (num >= 1)  and (num <= 3):
    if num == 1:
        print(nombre1.upper())
    elif num == 2:
        print (nombre1.lower())
    else:
        print (nombre1.title())
else:
    print("Ingrese un número correcto")


#Ejercicio 9:
#Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según
#  la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

#Solicitamos el ingreso de la magnitud del terremoto
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto: "))

#Validamos que no ingrese un núero negativo y evaluamos la condición en caso de que ingrese 
#Un número correcto. 
if magnitud_terremoto <= 0: 
    print ("Por favor, ingrese un número correcto.")
elif magnitud_terremoto < 3:
    print("Muy leve (imperceptible)")
elif magnitud_terremoto < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud_terremoto < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud_terremoto < 6: 
    print ("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud_terremoto < 7: 
    print ("Muy Fuerte (puede causar daños significativos).")
else: 
    print ("Extremo (puede causar graves daños a gran escala).")


#Ejercicio 10
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), 
# qué mes del año es y qué día es. El programa deberá utilizar esa información 
# para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. 

#Solicitamos a la persona que ingrese en que hemisferio está y lo pasamos todo a mayúscula. 
hemisferio = input("¿En cuál hemisferio se encuentra (N / S)? ").upper()

#Validamos que no ingrese un dato mal y vamos evaluando según lo que ingrese. 
if (hemisferio == "N") or (hemisferio == "S"):
    #Si ingresa bien el hemisferio, le solicita que ingrese el mes y pasamos todo a minúscula. 
    #También creamos una lista con los meses de año válidos. 
    mes = input("Ingrese el mes: ").lower()
    meses_anio = ["enero","febrero","marzo","abril","mayo","junio", "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    #Si ingresa bien el mes (está dentro de la lista creada), solictamos el día. 
    if mes in meses_anio:
        dia = int(input("Ingrese el día del mes: "))
        #Se colocó 1 a 31 ya que si ingresa otro número por fuera de lo tiene máximo un mes el programa le pide
        #que ingrese un día válido. 
        if 1 <= dia <= 31:
            # Si está bien, evaluamos la estación y guardamos en la variable según lo que el usuario ingrese. 
            if ((mes == "diciembre") and (dia >= 21)) or (mes in ["enero", "febrero"]) or ((mes == "marzo") and (dia <= 20)):
                estacion_n = "invierno"
                estacion_s = "verano"
            elif ((mes == "marzo") and (dia >= 21)) or (mes in ["abril", "mayo"]) or ((mes == "junio") and (dia <= 20)):
                estacion_n = "primavera"
                estacion_s = "otoño"
            elif ((mes == "junio")and (dia >= 21)) or (mes in ["julio", "agosto"]) or ((mes == "septiembre") and (dia <= 20)):
                estacion_n = "verano"
                estacion_s = "invierno"
            elif ((mes == "septiembre") and (dia >= 21)) or (mes in ["octubre", "noviembre"]) or ((mes == "diciembre") and (dia <= 20)):
                estacion_n = "otoño"
                estacion_s = "primavera"
                # Mostramos el resultado segúl el hemisferio. 
            if hemisferio == "N":
                print(f"Estás en {estacion_n}")
            else:
                print(f"Estás en {estacion_s}")
        else:
            print(" Ingrese un día válido (1-31).")
    else:
        print("Por favor, ingrese un mes válido.")
else:
    print("Por favor, ingrese Por favor, ingrese S (hemisferio sur) o N (hemisferio norte).")











