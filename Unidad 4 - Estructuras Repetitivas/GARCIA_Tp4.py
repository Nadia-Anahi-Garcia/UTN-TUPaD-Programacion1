#Ejercicio N° 1
#Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

#Utilizamos el bucle for ya que esta definido su inicio y su fin. 

for i in range(101):
    print(i)


#Ejericio N° 2
#Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

#Solicitamos que el usuario ingrese un número:
numero = int(input("Por favor ingrese un número entero: "))

#Nos permite tomar el valor absoluto si la persona ingresa un número negativo. 
numero = abs(numero)

#Inicializamos
contador = 0 

#Si el número que ingresa es 0 ya la dice que tiene 1 digito. 
#De otra manera ya cuenta.
if (numero == 0):
    print ("El número ingresado tiene 1 digito.")
else:
    while (numero != 0):
        contador = contador +  1
        numero = numero // 10

#Muestra el mensaje por pantalla 
print (f"El número ingresado tiene {contador} dígitos.")


#Ejercicio N° 3
#Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores

#Primero solicitamos que el usuario ingrese los números
num_1 = int(input("Por favor ingrese el primer núero entero: "))
num_2 = int(input("Por favor ingrese el segundo núero entero: "))

#Con la función min y max nos aseguramos recorrer siempre del menor al mayor 
#Esto es para el caso en que el usuario ingrese primero un número más grande. 
num_min = min(num_1,num_2)
num_max = max(num_1,num_2)

#Inizialiamos la suma 
suma=0 

#Con el bucle for sumamos excluyendo el primero (num_min + 1) 
# y el último, la función range no lo incluye. 

for contador in range ((num_min +1), num_max):
    suma += contador
#Mostramos el mensaje en pantalla del total de la suma.    
print(f"El total de la suma es de {suma}")


#Ejercicio 4
#Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
#El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

#Inicializamos la suma
suma = 0 

#Preferí pedir el primer número afuera, en caso de no querer sumar se muestra el mensaje directo. 
#y si el usuario ingresa el primer número como es distinto que 0, entra al bucle while 
num = int(input("Ingrese el primer número (0 para cortar): "))

#Ingresa el primer número y lo suma, luego le pide el resto de los números. 
while (num != 0):
    suma += num
    num = int(input("Ingrese otro número (0 para cortar): "))

print (f"El total de la suma es {suma}")


#Ejercicio N°5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

#Imporatamos la función random
import random 

#Guardamos el número para adivinar. 
numero_para_adivinar = random.randint(0,9)

#Solicitamos que ingrese un número. 
numero_ingresado = int(input("Ingrese el número: "))
contador = 1

#Si el primer número que ingreso no es, entra al bucle y le pide nuevamente 
#hasta adivinar, contanto las vueltas que le llevó. 
#En el caso de que el sea el primer núemero ya cuanta el intento. 
#Se repite dos veces el input, pero esto me  permite personalizar el mensaje al ingresar el número incorrecto. 
while (numero_ingresado != numero_para_adivinar):
    numero_ingresado = int(input("Incorrecto! Ingresa otro número: "))
    contador += +1

print(f"Adivinaste!!, el número era {numero_para_adivinar} y te llevo {contador} intentos. ")


#Ejercicio N°6
#Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

#Se puede hacer que el for cuente en -2, pero opte por que cuente en -1 
# y  compruebe por medio del mod si es par o no. 
for i in range(100,-1,-1):
    if i % 2 == 0:
        print(i,end=" - ")


#Ejercicio N°7
#Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

#Pedimos al usuario que ingrese un número.
numero_usuario = int(input("Ingrese un número: "))
#Inicializamos la suma
sumatoria = 0

#Validamos que ingrese un número positivo. 
while (numero_usuario < 0):
    numero_usuario = int(input("Por favor ingrese un número positivo: "))

# con el ciclo for vamos sumando.
for itera in range (numero_usuario + 1):
    sumatoria += itera

#Mostramos en pantalla
print (f"La suma de los números es {sumatoria}")


#Ejercicio N°8
#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Nos permite cambiar la cantidad de números a ingresar, de manera mas fácil de encontrar. 
cantidad_numeros = 100

#Inicializamos
pares = 0
impar = 0
negativo = 0 
positivo = 0

#con el for pedimos los números y también vamos guardando en las variables la cantidad de números 
#(pares, impar, negativo y positivo).

for contadores in range (cantidad_numeros):
    num_usuario = int(input(f"Ingrese número {contadores +1}: "))
    if (num_usuario % 2 == 0):
        pares = pares + 1
    else:
        impar = impar + 1
    if (num_usuario > 0):
        positivo = positivo +1
    elif (num_usuario < 0): 
        negativo = negativo +1

#Los mostramos por pantalla 
print (f"Los números pares son: {pares}")    
print (f"Los números impares son: {impar}")
print (f"Los números negativos son: {negativo}")
print (f"Los números positivos son: {positivo}")


#Ejercicio N°9
#Elabora un programa que permita al usuario ingresar 100 números enteros
#  y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

#Nos permite cambiar la cantidad de números a ingresar, de manera mas fácil de encontrar. 
cantidad_de_numeros = 100

#Inicializamos suma 
suma = 0 

#Con el for solicitamos los números y lo vamos sumando
for j in range(cantidad_de_numeros):
    numeros_enteros = int(input(f"Ingrese número {j +1}."))
    suma  += numeros_enteros

#Mostramos la cantidad de números y cálculamos la media (promedio). 
print (f"La media de {cantidad_de_numeros} números es {suma/cantidad_de_numeros}")


#Ejercicio N° 10
#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Solicitamos al usuario que ingrese un número.
nro = int(input("Ingrese un número: "))

#Guardamos el signo en el caso de que la persona ingrese un número negativo
if (nro < 0):
    signo = -1
else:
    signo = 1

#Con el abs trabajamos con el valor absoluto.
nro = abs(nro)

#Inicializamos la variables.
digito = 0
inverso = 0

#Con el while consultamos si el número ingresado es distinto que 0
#Luego con el el operador mod vamos sacando los digitos y lo guardamos 
#En la variable digito. El segundo paso tuncamos el número para quedarnos 
#solo con la parte entera y en inverso justamente vamos guardando el número. 
while (nro != 0):
    digito = nro % 10
    nro = nro // 10
    inverso = (inverso * 10) + digito

#Luego si el número fue negativo lo multimplicamos por el signo.
inverso *= signo

#Mostramos el número por pantalla.
print (f"El número inverso es: {inverso}")


