# 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definición de la función 
def imprimir_hola_mundo():
    print("Hola Mundo!") 

# Programa principal
imprimir_hola_mundo()



# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. 
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

# Definición de función
def saludar_usuario(nombre):
    return f"Hola {nombre}!" # La función devuelve una cadena de texto con el saludo personalizado

# Programa Principal
nom_usuario = input("Ingrese su nombre: ") # Solicitar al usuario que ingrese su nombre

saludo = saludar_usuario(nom_usuario) # Llamar a la función saludar_usuario, y guardar en una variable

print(saludo) 



# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definición de función
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}" # La función devuelve una cadena de texto con la información personal

# Programa Principal
nombre = input("Ingrese su nombre: ") # Solicitar al usuario que ingrese su nombre
apellido = input("Ingrese su apellido: ") # Solicitar al usuario que ingrese su apellido
edad = input("Ingrese su edad: ") # Solicitar al usuario que ingrese su edad
residencia = input("Ingrese su residencia: ") # Solicitar al usuario que ingrese su residencia

info_personal = informacion_personal(nombre, apellido, edad, residencia) # Llamar a la función y guardar en una variable

print(info_personal) 



# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math # Importar el modulo math para usar el número pi

# Definición de las funciones

# Defnición de la función para calcular el área de un circulo
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2) # Devuelve el área del círculo

# Defnición de la función para calcular el perímetro de un circulo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio # Devuelve el perímetro del círculo

# Programa principal
radio = float(input("Ingrese el radio del circulo: ")) # Solicitar al usuario el radio del circulo

area = calcular_area_circulo(radio) # Llamar a la función y guardar en una variable
perimetro = calcular_perimetro_circulo(radio) # Llamar a la función y guardar en una variable

# Imprimir los resultados (con dos decimales) 
print(f"El área del circulo es {area:.2f}")
print(f"El perímetro del circulo es {perimetro:.2f}")



# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definición de la función

def segundos_a_horas(segundos):
    return segundos / 3600 # Devuelve cantidad de horas

# Programa principal
segundos= float(input("Ingrese la cantidad de segundos: ")) # Solicitar al usuario la cantidad de segundos

horas = segundos_a_horas(segundos) # Llamar a la función y guardar en una variable

# Imprimir resultado
print(f"La cantidad de segundos ingresados corresponde a {horas} hora/s")



# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro 
# y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definición de la función

def tabla_multiplicar(numero):
    for i in range(1,11): # Recorre los números del 1 al 10
        print(f"{numero} * {i} = {numero * i}") # Imprime la multiplicación del número ingresado

# Programa principal
num1= int(input("Ingrese un número: ")) # Solicitar al usuario un número

# Imprimir resultado
print(f"La tabla de multiplicar (del 1 al 10) del número {num1} es:" )
tabla_multiplicar(num1) # Llamar a la función para imprimir la tabla de multiplicar 



# 7) Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros 
# y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

# Definición de la función

def operaciones_basicas(a, b):
    # Operaciones
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Aspectos a considerar en la división
    if b != 0:
        división = a / b # Si b no es cero, calcula la división
    else:
        división = "Error (división por cero)" # Si b es cero, mensaje error
 
    return(suma, resta, multiplicacion, división) # Devuelve los resultados como una tupla

# Programa principal
numer1= int(input("Ingrese el primer número: ")) # Solicitar al usuario el número a
numer2= int(input("Ingrese el segundo número: ")) # Solicitar al usuario el número b

resultados = operaciones_basicas(numer1, numer2)  # Llamar a la función y guardar los resultados en una tupla

# Imprimir resultados
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")



# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, 
# y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Definición de la función

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2) # Calculo de IMC
    return imc # Devuelve el IMC calculado

# Programa principal
peso= float(input("Ingrese su peso (en kg): ")) # Solicitar al usuario el peso
altura= float(input("Ingrese su altura (en metros): ")) # Solicitar al usuario la altura

indice_de_masa_corporal = calcular_imc(peso, altura) # Llamar a la función y guardar en una variable

# Imprimir resultado (con dos decimales)
print(f"El índice de masa corporal (IMC) es: {indice_de_masa_corporal:.2f}")



# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius 
# y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

# Definición de la función

def celsius_a_fahrenheit(celsius):
    fahrenheit= (celsius * 9/5) + 32 # Calculo de fahrenheit
    return fahrenheit # Devuelve el equivalente en Fahrenheit

# Programa principal
grado_celsius= float(input("Ingrese la temperatura en grados celsius: "))# Solicitar al usuario la temperatura en Celsius

grados_f= celsius_a_fahrenheit(grado_celsius) # Llamar a la función y guardar en una variable

# Imprimir resultado
print(f"Temperatura ingresada: {grado_celsius} Grados Celcius")
print(f"Temperatura equivalente: {grados_f:.2f} Grados Fahrenheit")



# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros 
# y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definición de la función

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3 # Calculo de promedio de 3 números
    return promedio  # Devuelve el promedio

# Programa principal
nro_a= int(input("Ingrese el primer número: ")) # Solicitar al usuario el número a
nro_b= int(input("Ingrese el segundo número: ")) # Solicitar al usuario el número b
nro_c= int(input("Ingrese el tercer número: ")) # Solicitar al usuario el número c

promed = calcular_promedio(nro_a, nro_b, nro_c) # Llamar a la función y guardar en una variable

# Imprimir resultado
print(f"El promedio de los números ingresados es: {promed:.2f}")