# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100, incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea.

print("Los números enteros de 0 a 100 son:")

# Inicia el ciclo for, imprime los números del 0 al 100, uno por línea.
for i in range(0,101):
    print(i)



# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

# Solicitar al usuario un número entero
numero_entero = int(input("Ingrese un número entero: "))

# Convertir los números ingresados en positivos, para contar la cantidad de dígitos.
numero_entero = abs(numero_entero)

# Inicializar contador de dígitos en cero.
contador = 0

# Verificar si el número es igual o mayor a cero.
if numero_entero == 0:
    contador = 1
else:
# Ciclo while.
    while numero_entero > 0:
        numero_entero = numero_entero // 10 # En cada iteración, se divide el número por 10, para eliminar el último dígito.
        contador += 1 # Cada vez que divide se incrementa 1 al contador de dígitos.

# Mostrar la cantidad de dígitos.
print(f"El número tiene {contador} dígito(s)")



# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

# Solicitar al usuario dos números enteros.
num_entero1 = int(input("Ingrese el primer número entero: "))
num_entero2 = int(input("Ingrese el segundo número entero: "))

# Ordenar los números ingresados, de modo que el primero sea menor que el segundo.
if num_entero1 > num_entero2:
    num_entero1, num_entero2 = num_entero2, num_entero1

# Inicializar el contador (sumatoria) en cero.
sumatoria = 0

# Comenzar el ciclo, sumar los valores intermedios excluyendo los extremos ingresados.
for i in range(num_entero1 +1, num_entero2):
    sumatoria += i # En cada iteración sumar el valor de i, para obtener la suma entre los valores.

# Mostra el resultado
print(f"La sumatoria entre {num_entero1} y {num_entero2} (ambos sin incluir) es: {sumatoria}")



# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

# Solicitar al usuario números enteros, e indicarle cuándo detener el programa.
num_enteros = int(input("Ingrese números enteros, se sumarán en secuencia (para detener el programa ingrese 0):\n"))

# Inicializar acumulador 
sum_acu = 0

# Iniciar ciclo while
while num_enteros != 0: # Si el número ingresado es distinto de cero ingresa al ciclo.
    sum_acu += num_enteros # En cada iteración se suma (acumula) el número ingresado.
    num_enteros = int(input("Ingrese otro número entero, (para detener el programa ingrese 0):\n")) # Se solicita al usuario un nuevo número. Si ingresa cero el ciclo se detiene.

print(f"\nLa suma de los números ingresados es: {sum_acu}\n")



# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

# Importar módulo de números aleatorios.
import random

# Crear un número aleatorio, entre 0 y 9 (incluidos).
numero_a_adivinar = random.randint(0, 9)

# Mostrar el mensaje al usuario.
print("\nAdivine un número aleatorio entre 0 y 9:\n")
num_ingresado = int(input("Ingrese un número entre 0 y 9: "))

# Inicializar contador
intentos = 0

# Iniciar el ciclo para adivinar.
while num_ingresado != numero_a_adivinar:
    intentos += 1
    num_ingresado = int(input("Incorrecto, intente nuevamente: "))

# Contabilizar el número de intentos 
intentos += 1

# Mostrar el resultado
print(f"\n¡Correcto! Adivinaste el número: {numero_a_adivinar}\n")
print(f"Número de intentos: {intentos}")



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("Números pares comprendidos entre 0 y 100, en orden decreciente:\n")

# Inicia el ciclo, recorriendo desde 100 a 0, de dos en dos, los números pares.
for i in range(100,0,-2):
    print(i)



# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

# Solicitar al usuario un número positivo.
num_positivo = int(input("Ingrese un número entero positivo (se sumaran los números comprendidos entre 0 y el número ingresado):\n"))

# Inicializar acumulador
acu = 0

# Inicia el ciclo 
if num_positivo != 0:
    # Inicia el ciclo
    for i in range(0,num_positivo+1):
        acu += i
# Mostrar el resultado
print(f"La suma de los números comprendidos entre 0 y {num_positivo} es: {acu}")



# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 

print("\nSe ingresaran 100 números enteros y se indicarán cuántos son pares, impares, positivos y negativos.\n")

# Inicializar contador
par = 0
impar = 0
positivo = 0
negativo = 0

#Iniciar el ciclo
for i in range(100):
    # Solicitar al usuario 100 números
    num_ingresados = int(input("Ingrese 100 números enteros: "))
    # Verificar la cantidad de números pares e impares
    if num_ingresados % 2 == 0:
        par += 1
    else:
        impar += 1
    # Verificar la cantidad de números positivos y negativos
    if num_ingresados > 0:
        positivo += 1
    elif num_ingresados < 0:
        negativo +=1

# Mostrar la cantidad de números mencionados
print("\nResultados:\n")
print(f"Números Pares: {par}\n")
print(f"Números Impares: {impar}\n")
print(f"Números Positivos: {positivo}\n")
print(f"Números Negativos: {negativo}\n")



# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.

print("\nSe ingresaran 100 números enteros y se calculará la media de esos valores.\n")

# Inicializar contador
acumul = 0

# Inicializar ciclo
for i in range(100):
    # Solicitar al usuario 100 números
    num_solicitados = int(input("Ingrese 100 números enteros: "))
    acumul += num_solicitados # En cada iteración se suma el nuevo número ingresado.

# Calcular la media
media = acumul / 100

# Mostrar el resultado
print("\nResultado:")
print(f"La media de los valores ingresados es: {media}\n")



# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

# Solicitar al usuario un número y mostrar el número ingresado.
numer1 = int(input("Ingrese un número: "))
print(f"\nNúmero ingresado: {numer1}")

# Verificar si el número es negativo.
num_negativo = numer1 < 0

# Trabajar con el número en positivo.
numer1 = abs(numer1)

# Inicializar número invertido y dígito.
num_invertido = 0
digito = 0

# Inicia el ciclo
while numer1 != 0:
    digito = numer1 % 10 # Obtener el último dígito.
    num_invertido = (num_invertido * 10) + digito # Agregar dicho digito al número invertido.
    numer1 = numer1 // 10 # Acortar el número (elimina el último dígito del número ingresado).

# En caso de haber ingresado un número negativo, se colocará su signo.
if num_negativo:
    num_invertido = -num_invertido
    
# Mostrar el resultado.
print(f"Número invertido: {num_invertido}\n")