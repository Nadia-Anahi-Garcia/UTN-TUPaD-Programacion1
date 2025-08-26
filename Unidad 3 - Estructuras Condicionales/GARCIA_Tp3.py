#Ejercicio 1: 
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingrese su edad:"))
edadlimite=18
if edad >= edadlimite:
    print("Es mayor de edad")

#Ejercicio 2: 
#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Por favor, ingrese su nota (0 a 10): "))
print("Aprobado" if nota >= 6 else "Desaprobado")

#Ejercicio 3: 
#Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 

numero = int(input("Por favor ingrese un número: "))

if numero % 2 == 0:
    print("Ha ingresado un número par.")
else: 
    print("Por favor, ingrese un número par")

