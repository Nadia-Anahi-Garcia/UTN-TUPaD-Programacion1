#Ejercicio_1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 

print ("Hola Mundo!")

#Ejercicio_2
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
#realizar la impresión por pantalla.

#Solicitamos al usuario que ingrese su nombe y lo guardamos en la variable
nombre = input ("Hola, por favor ingrese su nombre: ")
#Mostramos por pantalla el saludo personalizado. 
print (f"Hola {nombre}!")

#Ejercicio_3
#Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
#la impresión por pantalla. 

# Solicitar datos al usuario
name = input ("Hola, por favor ingrese su nombre: ")
apellido = input     ("Ingrese su apellido: ")
edad = int (input    ("Ingrese su edad: "))
nacionalidad = input ("Por último, ingrese su nacionalidad: ")

# Mostrar el mensaje con todos los datos solicitados. 
print (f"Soy {name} {apellido}, tengo {edad} años y vivo en {nacionalidad}.")

#Ejercicio_4
# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
# su perímetro. 

# Solicitar el radio
radio = float (input ("Ingrese el rádio del circulo para cáluclar área y perímetro: "))

# Constante Pi
import math
valorPi = math .pi

# Cálculos
area = valorPi * radio ** 2
perimetro = 2 * valorPi * radio

#Mostramos los resultados 
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")


#Ejercicio_5
#Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
#cuántas horas equivale. 

print("*** Conversor de Segundos a Horas ***")

# Entrada de datos
segundos = int(input("Ingrese la cantidad de segundos que desea convertir: "))
# Conversión
horas = segundos / 3600
#Mostramos los resultados. 
print (f"{segundos} segundos equivalen a {horas} horas.")


#Ejercicio_6
# Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  

print("*** Tabla de Multiplicar ***")

# Entrada de datos
numeroTabla = int (input ("Ingrese el número para mostrar su tabla: "))
# Tabla de multiplicar
print (f" Tabla del {numeroTabla} : ")
print (f"{numeroTabla} X 1 = ", numeroTabla * 1)
print (f"{numeroTabla} X 2 = ", numeroTabla * 2)
print (f"{numeroTabla} X 3 = ", numeroTabla * 3)
print (f"{numeroTabla} X 4 = ", numeroTabla * 4)
print (f"{numeroTabla} X 5 = ", numeroTabla * 5)
print (f"{numeroTabla} X 6 = ", numeroTabla * 6)
print (f"{numeroTabla} X 7 = ", numeroTabla * 7)
print (f"{numeroTabla} X 8 = ", numeroTabla * 8)
print (f"{numeroTabla} X 9 = ", numeroTabla * 9)
print (f"{numeroTabla} X 10 = ", numeroTabla * 10)

#Ejercicio_7
# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print ("*** Mini Calculadora ***")

# Entrada de datos
numero_1 = int (input ("Por favor ingrese el primer número entero distinto a 0: "))
numero_2 = int (input ("Por favor ingrese el segundo número entero distinto a 0: "))
# Operaciones
print ("*** Los resultados son: ****")
print (f"Suma:              {numero_1} + {numero_2} = ", numero_1 + numero_2)
print (f"División:          {numero_1} / {numero_2} = ", numero_1 / numero_2)
print (f"Multiplicación:    {numero_1} * {numero_2} =", numero_1 * numero_2)
print (f"Resta:             {numero_1} - {numero_2} =", numero_1 - numero_2)

#Ejercicio_8
# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
# de masa corporal.

print ("*** Calculadora de IMC ***")
# Entrada de datos
altura = float (input ("Ingrese su altura en metros (ej: 1.75): "))
peso = float (input ("Ingrese su peso en kilogramos: "))
# Cálculo
imc = peso / (altura ** 2)
#Mostramos el resultado
print(f"Su IMC es de {imc:.2f}")

#Ejercicio_9
#Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#pantalla su equivalente en grados Fahrenheit. 

print ("*** Conversor de Celsius a Fahrenheit***")
#Solicitamos al usuario la temperatura 
temCel = float (input ("Ingrese la temperatura en grados Celsius: "))
#Cálculo de conversión 
temFahr = (temCel * 1.8) + 32
#Mostramos el resultado
print (f"{temCel}°C equivalen a  {temFahr:.2f}°F")

#Ejercicio_10
# Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
# dichos números. 
print ("--- Cálculo de promedio ---")
#Ingreso de los tres números por el usuario
num_1 = float(input ("Ingrese el primer número: "))
num_2 = float(input ("Ingrese el segundo número: "))
num_3 = float(input ("Ingrese el tercer  número: "))
#Cálculo de promedio
promedio=(num_1 + num_2 + num_3)/3
#Mostramos el resultado
print (f"El promedio de los tres números ingresados es de {promedio:.2f}")