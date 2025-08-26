#Ejercicio 1 : 
#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Por favor, ingrese su edad:"))
edadlimite=18
if edad >= edadlimite:
    print("Eres mayor de edad")
