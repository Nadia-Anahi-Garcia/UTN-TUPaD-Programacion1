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
else: 
    print("Aprobado" if nota >= 6 else "Desaprobado")

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
elif (edad2 >=12) and (edad2 < 18):
    print("Perteneces a la categoría Adolescente.")
elif (edad2 >= 18) and (edad2 < 30):
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
if ultima_letra.lowe() in vocales:
    print(f"{palabra}!")
else:
    print (palabra)


#Ejercicio 8
#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla

nombree = input("Ingrese su nombre:")
numeroo = int(input("Ingrese un número del 1 al 3:"))

if (numeroo >= 1)  and (numeroo <= 3):
    if numeroo == 1:
        print(nombree.upper())
    elif numeroo == 2:
        print (nombree.lowe())
    else:
        print (nombree.title ())
else:
    print("Ingrese un número correcto")




