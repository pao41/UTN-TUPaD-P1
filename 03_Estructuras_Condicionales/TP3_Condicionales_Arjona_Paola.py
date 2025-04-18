# 1) Escribir un programa que solicite la edad del usuario.Si el usuario es mayor de 18 años, 
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
#condicionales
if edad >= 18:
    print(f"Es mayor de edad")
else:
    print(f"No es mayor de edad")


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
#condicionales
if nota >= 6:
    print(f"Aprobado")
else:
    print(f"Desaprobado")


# 3) Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".

numero = int(input("Ingrese un número: "))
# para evaluar si el numero es par o impar usar modulo o residuo (%): numero % 2 == 0
if numero % 2 == 0:
    print(f"Ha ingresado un número par")
else:
    print(f"Por favor, ingrese un número par")


# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a que categorías pertenece.
edad1 = int(input("Ingrese su edad: "))
# Limites de categorias
LIMITE_EDAD_NINO = 12
LIMITE_EDAD_ADOLESC = 18 
LIMITE_EDAD_ADUL_JOVEN = 30
# condicionales
if edad1 < LIMITE_EDAD_NINO:
    print(f"Su edad corresponde a la categoria: Niños")
elif edad1 < LIMITE_EDAD_ADOLESC:
    print(f"Su edad corresponde a la categoria: Adolescente")
elif edad1 < LIMITE_EDAD_ADUL_JOVEN:
    print(f"Su edad corresponde a la categoria: Adulto Joven")
else:
    print(f"Su edad corresponde a la categoria: Adultos")


# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; 
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".

contraseña = input("Ingrese una contraseña: ")
# limites de la longitud de caracteres:
limite_inferior = 8
limite_superior = 14
# uso de funcion len() que indica cantidad de caracteres, longitud de una cadena. 
# condicionales
if limite_inferior <= len(contraseña) <= limite_superior:
    print(f"Ha ingresado una contraseña correcta.")
else:
    print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")


# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media 
# y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

# Importar el modulo statistics, que contiene funciones para calculos estadisticos
import statistics

# Del modulo statistics solo importar las funciones de mode, median y mean
from statistics import mode, median, mean

# Importar numeros aleatorios
import random 

# Crear una lista con 50 números aleatorios, entre 1 y 100 (incluidos).
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Mostrar lista
print("Se mostrara una lista de 50 números aleatorios.")
print("La lista de números aleatorios es: ")
print(numeros_aleatorios)

# Calcular modo, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Mostrar los valores de modo, mediana y media
print(f"La Moda es: {moda}")
print(f"La Mediana es: {mediana}")
print(f"La Media es: {media}")

# Determinar tipo de sesgo. Uso de condicionales
if media > mediana > moda:
    print(f"Hay sesgo POSITIVO") 
elif media < mediana < moda:
    print(f"Hay sesgo NEGATIVO")
elif media == mediana == moda:
    print(f"No hay sesgo")
else:
    print(f"No se puede determinar el tipo de sesgo. Los valores de media, mediana y moda no siguen un patrón de sesgo definido.")


# 7) Escribir un programa que solicite una frase o palabra al usuario. 
# Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto = input("Ingrese una frase o palabra: ")

# Verificar si el string termina en vocal (mayuscula o minuscula)
if texto[-1].lower() in "aeiou":
    texto += "!" # En caso de terminar en vocal se añade al texto el signo de exclamación 
    print(f"Resultado: {texto}")
else:
    print(f"Resultado: {texto}")


# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee

# Solicitar el nombre al usuario
nombre = input("Ingrese su nombre: ")

# Opciones
print(f"Opciones:")
print (f"1: Quiere su nombre en mayúsculas \n2: Quiere su nombre en minusculas \n3: Quiere su nombre con la primera letra en mayúscula")

# Solicitar el numero dependiendo de la opción deseada
opcion = input("Indique el número de acuerdo a la opción elegida: ")

# Comparar según opción deseada. Uso de condicionales
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción no válida")


# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud según la escala de Richter e imprima el resultado por pantalla.

try: 
    # Solicitar al usuario la magnitud del terremoto
    magnitud_terremoto = float(input("Ingrese la magnitud de un terremoto: "))

    # Limite superior de categorias
    mleve = 3
    leve = 4 
    moderado = 5
    fuerte = 6
    mfuerte = 7

    # Verificar la categoria segun la escala de Richter
    if magnitud_terremoto < mleve:
        print("Magnitud: Muy leve (imperceptible)")
    elif magnitud_terremoto < leve:
        print("Magnitud: Leve (ligeramente perceptible)")
    elif magnitud_terremoto < moderado:
        print("Magnitud: Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud_terremoto < fuerte:
        print("Magnitud: Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud_terremoto < mfuerte:
        print("Magnitud: Muy Fuerte (puede causar daños significativos)")  
    else:
        print("Magnitud: Extremo (puede causar graves daños a gran escala)")

# Si ocurre un error, el usuario digita caracteres invalidos, se le informará.
except ValueError:
    print("Ha ingresado un valor no válido")


# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

# Solicitar hemisferio en que se encuentra: N (norte) o S (sur).
print("De acuerdo a las siguientes opciones: \nN: Hemisferio Norte \nS: Hemisferio Sur")
hemisferio_usuario = input("Ingrese en qué hemisferio se encuentra: ").upper() # Uso de función .upper(). Letra válida si ingresa minúsculas.

# Solicitar día y mes
dia_usuario = int(input("Ingrese el número del día: "))
mes_usuario = int(input("Ingrese el número del mes: "))

# Crear una tupla con el  mes y día ingresados.
fecha = (mes_usuario, dia_usuario)

# Validar la fecha ingresada:
if (1 <= mes_usuario <= 12) and (1 <= dia_usuario <= 31):
    print(f"Día: {dia_usuario} y Mes: {mes_usuario}")

# Según hemisferio y fecha, determinar la estación del año:
    if hemisferio_usuario == "N":
        # Se encuentra en el Hemisferio Norte
        print("Usted se encuentra en el Hemisferio Norte")

        # Estaciones del Hemisferio Norte:
        # Periodo de estacion invierno
        if (fecha >= (12,21)) or (fecha <= (3, 20)): # or porque comprende diferentes años
            print("Estación invierno")
        # Periodo de estación primavera
        elif (fecha >= (3,21)) and (fecha <= (6,20)):
            print("Estación Primavera")
        # Periodo de estación verano
        elif (fecha >= (6,21)) and (fecha <= (9,20)):
            print("Estación Verano")
        # Periodo de estación otoño
        elif (fecha >= (9,21)) and (fecha <= (12,20)):
            print("Estación Otoño")

    elif hemisferio_usuario == "S":
        # Se encuentra en el Hemisferio Sur
        print("Usted se encuentra en el Hemisferio Sur") 

        # Estaciones del Hemisferio Sur:
        #Periodo de estación verano
        if (fecha >= (12,21)) or (fecha <= (3,20)): # or porque comprende diferentes años
            print("Estación Verano")
        # Periodo de estación otoño
        elif (fecha >= (3,21)) and (fecha <= (6,20)):
            print("Estación Otoño")
        # Periodo de estación invierno
        elif (fecha >= (6,21)) and (fecha <= (9,20)):
            print("Estación Invierno")
        # Periodo de estación primavera
        elif (fecha >= (9,21)) and (fecha <= (12,20)):
            print("Estación Primavera")
    else:
        print("Ingrese datos válidos: N/S")
else:
    print("El día y/o mes ingresado no es válido")



  