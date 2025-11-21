#EJERCICIO 1 
#Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial
#  de todos los números enteros entre 1  y el número que indique el usuario

#Definición de Funciones 

def factorial(numero):
    """Calcula recursivamente el factorial de un número entero no negativo."""
    #Caso base: el factorial de 0 es 1
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)
    
#Programa principal

#Solicitamos que el usuario ingrese el número para calcular su factorial y lo mostramos
numero = int(input("Ingrese un número para calcular su factorial: "))

print(f"El factorial {numero} es : {factorial(numero)}")

#---------------------------------------------------------------------------------------
#EJERCICIO 2
#Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

#Definición de Funciones 
def fibonacci(posicion):
    """Calcula recursivamente el valor correspondiente a una posición de la serie de Fibonacci."""
    # Caso base: las dos primeras posiciones valen 0 y 1 respectivamente
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion -1) + fibonacci (posicion -2)
    
#Programa principal
# Solicitamos al usuario la posición hasta la cual desea obtener la serie
posicion = int(input("Ingrese una posición: "))
# Mostramos la serie completa desde 0 hasta la posición indicada
for i in range (posicion + 1):
    print(f"En la posición {i} obtenemos el {fibonacci(i)}")

#---------------------------------------------------------------------------------------
#EJERCICIO 3
#Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

#Definición de Funciones 
def potencia (base, exponente):
    """Calcula recursivamente la potencia de un número base elevado a un exponente."""
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0 :
        return 1
    else:
        return base * potencia(base, exponente -1)

#Programa principal

# Solicitamos al usuario la base y el exponente
base = int (input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
# Calculamos la potencia utilizando la función recursiva
resultado = potencia (base, exponente)
# Mostramos el resultado en pantalla
print(f"El resultado de la potencia de {base} elevando al exponente {exponente} es : {resultado}")

#---------------------------------------------------------------------------------------
#EJERCICIO 4
#Crear una función recursiva en Python que reciba un número entero positivo en base decimal
#  y devuelva su representación en binario como una cadena de texto.

#Definición de Funciones 
def es_binario (numero):
    """Convierte un número decimal positivo a su representación binaria mediante recursión."""
    # Caso base: cuando el número llega a 0, se detiene la recursión
    if numero == 0:
        return ""
    else:
        return es_binario(numero//2)+ str(numero % 2)

#Programa principal
# Solicitamos al usuario que ingrese un número para convertirlo a binario
numero = int(input("Por favor ingrese el número para su conversión: "))
# Si el número ingresado es 0, lo mostramos directamente
if numero == 0:
    print ("El número binario es 0")
else:
    # Mostramos la conversión del número decimal a binario
    print(f"El número {numero} en biario es: {es_binario(numero)}")

#---------------------------------------------------------------------------------------
#EJERCICIO 5
#Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de 
# texto sin espacios ni tildes,y devuelva True si es un palíndromo o False si no lo es.

#Definición de funciones:

def texto_solo (texto):
    """Convierte el texto a minúsculas y elimina los espacios."""
    texto = texto.lower()
    texto= texto.replace(" ", "")
    return texto

def es_palindromo(palabra):
    """Verifica recursivamente si una palabra o frase es un palíndromo."""
    palabra = texto_solo (palabra)
    #caso base: Si la palabra tiene 0 o 1 letra es palindromo
    if len(palabra)< 1 :
        return True
    #Comparamos primera y última letra
    if palabra[0] == palabra [-1]:
        # Llamada recursiva con la palabra sin la primera y última letra
        return es_palindromo (palabra [1:-1])
    else:
        return False

#Programa principal
# Solicitamos al usuario que ingrese una palabra o frase sin tildes
frase = input("Ingrese una frase sin tíldes: ")
# Mostramos el resultado de la verificación
print(f"La frase/palabra {frase} es palíndromo?: {es_palindromo (frase)}")


#---------------------------------------------------------------------------------------
#EJERCICIO 6
#Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo 
# y devuelva la suma de todos sus dígitos.

#Definición de Funciones
def sumar_digitos(n):
    """Calcula recursivamente la suma de los dígitos de un número entero positivo."""
    # Caso base: si el número tiene un solo dígito, se devuelve ese mismo número
    if n < 10:
        return n 
    else:
        return (n % 10) + sumar_digitos(n // 10)

#Programa principal
# Solicitamos al usuario que ingrese un número entero positivo
numero = int (input("Por favor ingrese un número para sumar sus dígitos: "))
# Mostramos el resultado
print (f"La suma de los dígitos del número {numero} es: {sumar_digitos(numero)}")

#---------------------------------------------------------------------------------------
#EJERCICIO 7
# Un niño está construyendo una pirámide con bloques. }
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1),
#  y así sucesivamente hasta llegar al último nivel con un solo bloque.
#Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.

#Definición de funciones

def contar_bloques(n):
    """Calcula recursivamente el total de bloques necesarios para construir una pirámide de n niveles."""
    # Caso base: si no hay bloques en el nivel, el total es 0
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n-1)

#Programa principal
# Solicitamos al usuario la cantidad de bloques en el nivel más bajo
bloques = int(input("Por favor ingrese la cantidad de bloques que hay en el nivel más bajo: "))
# Mostramos el total de bloques necesarios para construir la pirámide
print(f"La cantidad de bloques que se necesita son : {contar_bloques (bloques)}")

#---------------------------------------------------------------------------------------
#EJERCICIO 8
# #Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) 
# y un dígito (entre 0 y 9),  y devuelva cuántas veces aparece ese dígito dentro del número.

#Definición de funciones

def contar_digito(numero, digito):
    """Cuenta recursivamente cuántas veces aparece un dígito dentro de un número entero positivo."""
    # Caso base: si el número tiene un solo dígito
    if numero == 0:
        return 0
    
    # Si el último dígito coincide con el buscado, sumamos 1
    if numero % 10 == digito:
        return 1 + contar_digito (numero // 10, digito)
    else:
        return contar_digito (numero // 10, digito)
    
# Programa principal
# Solicitamos al usuario el número y el dígito a buscar
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9) para contar: "))
# Mostramos el resultado
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")