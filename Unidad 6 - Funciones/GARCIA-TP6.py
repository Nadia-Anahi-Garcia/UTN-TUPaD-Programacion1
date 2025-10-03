#Ejercicio N° 1

#Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal


#Definición de funciones 

def imprimir_hola_mundo ():
    """ Función que imprima un mensaje.
    Args: lo dejamos sin parametros y solo mostramos el mensaje."""
    print("Hola mundo!")



#Programa principal

imprimir_hola_mundo()

#--------------------------------------------------------------------------------------

#EJERCICIO N° 2

#Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
#“Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.


#Definición de funciones 

def saludar_usuario(nombre):
    """ Función que saludo personalizado.
    Args:
        Nombre: nombre del usuario
    Returns: un string con mensaje personalizado ."""
    return f"Hola {nombre}!"

    


#Programa principal

#Solicitamos el nombre al usuario y luego mostramos el saludo llamando a la función creada.
nombre_usuario = input ("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))

#------------------------------------------------------------------------------------

#EJERCICIO N° 3

#Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
#los datos al usuario y llamar a esta función con los valores ingresados.


#Definición de Función
def informacion_personal(nombre, apellido, edad , residencia):
    """
    Función que muestra la información personal.
    Args:
    nombre: nombre del usuario.
    apellido: apellido del usuario
    edad: edad del usuario.
    residencia: lugar de residencia del usuario
    Returns:un string con  mensaje personalizado.
    """
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."


#Programa principal

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: ")) 
residencia = input("Ingrese su residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))

#-------------------------------------------------------------------------------

#EJERCICIO N° 4

##Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
#como parámetro y devuelva el área del círculo. calcular_perimetro_
#circulo(radio) que reciba el radio como parámetro y devuelva
#el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
#funciones para mostrar los resultados.

import math

#Definición de Función
def calcular_area_circulo(radio:float):
    """
    Función para calcular el área del círculo.
    Args:
    radio: radio del círculo.
    Returns:
    Área del círculo.
    """
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo (radio:float):
    """
    Función para calcular el perímetro del círculo.
    Args:
    Radio: radio del círculo.
    Returns:
    El perímetro del círculo. 
    """
    perimetro = 2* math.pi * radio
    return perimetro

#Programa principal

print ("\n * * * Cálculo de área y perímetro de un círculo * * *")
#Solicitamos al usuario que ingrese el radio del círculo 
radio = float (input("Ingrese el radio del círculo en metros: "))

#Mostramos el mensaje con el cálculo llamando a la función.
print (f"\n El área del círculo es {calcular_area_circulo(radio):.2f} m")
print(f"El perimetro del círculo es {calcular_perimetro_circulo(radio):.2f} m")

#--------------------------------------------------------------------------------

#EJERCICIO 5 

#Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar
#lA resultado usando esta función.


import math

#Definición de Función
def segundos_a_horas(segundos: int): 
    """
    Función para pasar de segundos a horas.
    Args:
        Segundos: segundos a pasar.
    Returns: La conversión de segundos a hora
    """
    horas = math.trunc(segundos / 3600)
    return horas

#Programa principal

print("\n * * * Conversión de segundos a horas * * * \n")

#Solicitamos que ingrese los segundos. 
segundos_ingresados = int(input("Ingrese los segundos para su conversión a horas: "))
#Mostramos el mensaje con los resultados (llamando a la función creada)
print (f"{segundos_ingresados} segundos, equivale a {segundos_a_horas (segundos_ingresados)} hs. ")

#------------------------------------------------------------------------------------------

#EJERCICIO N° 6

# Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.


#Definición de función
def tabla_multiplicar(numero:int):
    """
    Función que muestra la tabla de multiplicar.
    Args:
        Número: dato que ingtresa el usuario.
        Luego mostramos el mensaje.
    """
    for i in range(1, 11): 
        print(f"{numero} X {i} = {numero * i} ")


#Programa principal

print ("\n Tabla de multiplicar \n")
#Pedimos al usuario que ingrese el número para mostrar su tabla.
numero_a_mult = int (input("Ingrese un número para mostrar su tabla: "))
#Mostramos la tabla llamando a al función. 
tabla_multiplicar(numero_a_mult)

#----------------------------------------------------------------------------

#EJERCICIO N° 7

#Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
#de forma clara.


#Definición de función
def operaciones_basicas(a: int, b: int):
    """
    Función que hace operación básicas.
    Args:
        a y b : numeros que debe ingresar.
    Returns:
    Una tupla con los resultados de las operaciones.
    """
    suma = a +b 
    resta = a -b
    multiplicar = a * b
    if b != 0:
        dividir = a / b
    else:
        dividir = None
    return (suma, resta, multiplicar, dividir)
    
    

#Programa principal
a = int (input("Ingrese a : "))
b =  int (input ("Ingrese b: "))

print (operaciones_basicas (a, b))

#------------------------------------------------------------------------------------

#EJERCICIO N° 8 

#Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#para mostrar el resultado con dos decimales.


#Definición de función
def calcular_imc(peso, altura):
    """
    Función que calcula el IMC.
    Args:
        Peso: peso de la persona en kilogramos.
        Altura: de la persona en metros.
    Returns:
    El IMC calculado.
    """
    imc = peso / (altura**2)
    return imc

#Programa principal

print ("\nCalculadora de IMC\n")
peso_persona = float(input("Ingrese su peso en kg (Ej. 55.5): "))
altura_persona = float(input("Ingrese su altura en metros (Ej. 1.70): "))
print (f"El IMC por su peso: {peso_persona:.2f} y su altura : {altura_persona:.2f} es de {calcular_imc(peso_persona, altura_persona):.2f}")

#--------------------------------------------------------------------------------------------

#EJERCICIO N°9

#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.


#Definición de función

def celsius_a_fahrenheit(celsius):
    """
    Función que pide temperatura en celsius y pasa el equivalente a 
    fahrenheit.
    Args:
        Celsius: temperatura en celsius.
    Returns: La temperatura en fahrenheit.
    """
    tem_Fahr = (celsius * 1.8) + 32
    return tem_Fahr

#Programa principal

print ("\n*** Conversor de Celsius a Fahrenheit***\n")
#Solicitamos al usuario que ingrese el la temperatura en celsius y luego mostramos los resultados.
tem_Cel = float (input ("Ingrese la temperatura en grados Celsius: "))
print (f"\n {tem_Cel}°C equivalen a {celsius_a_fahrenheit(tem_Cel):.1f} °F")

#EJERCICIO N° 10
# Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

#Definición de función
def calcular_promedio(a, b, c):
    """
    Función que cálcula el promedio de 3 números.
    Args:
        a, b y c : números que da el usuario.
    Returns: promedio.
    """
    promedio = (a + b + c)/ 3
    return promedio

#Programa principal

print ("\n--- Cálculo de promedio ---\n")

num_1 = float(input ("Ingrese el primer número: "))
num_2 = float(input ("Ingrese el segundo número: "))
num_3 = float(input ("Ingrese el tercer  número: "))

print (f"El promedio de los tres números ingresados es de {calcular_promedio(num_1, num_2, num_3)}")
