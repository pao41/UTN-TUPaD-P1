# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función 
# para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(num_1): # Función recursiva 
    if num_1 == 0 or num_1 == 1:      # Caso base: el factorial de 0 o 1 es 1
        return 1
    else:
        return num_1 * factorial(num_1 - 1)  # Llamada recursiva

num = int(input("Ingrese un número entero positivo: ")) # Se solicita al usuario un número entero positivo

# Se verifica que el número sea mayor o igual a 1
if num < 1:
    print("Debe ingresar un número mayor o igual a 1.")  # Mensaje si el número no es válido
else:
    for i in range(1, num + 1):               # Se recorre desde 1 hasta el número ingresado
        print(f"Factorial de {i} = {factorial(i)}")  # Se muestra el factorial de cada número



# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Función recursiva que calcula el número de Fibonacci en la posición n
def fibonacci(pisicion):
    if pisicion == 0:                 # Caso base 1: fibonacci(0) = 0
        return 0
    elif pisicion == 1:               # Caso base 2: fibonacci(1) = 1
        return 1
    else:
        return fibonacci(pisicion - 1) + fibonacci(pisicion - 2)  # Llamadas recursivas

# Solicita al usuario una posición entera no negativa
pos_ingresada = int(input("Ingrese un número (entero no negativo), correspondiente a la posición para la serie Fibonacci: "))

# Verifica que la posición ingresada sea válida (mayor o igual a 0)
if pos_ingresada < 0:
    print("Por favor, ingrese un número mayor o igual a 0.")
else:
    print(f"Serie de Fibonacci hasta la posición {pos_ingresada}:")
    for i in range(pos_ingresada + 1):                     # Imprime la serie desde 0 hasta pos
        print(fibonacci(i), end=" ")             # Muestra cada valor separado por espacios
    print()                                  



# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). 

# Función recursiva que calcula la potencia de una base elevada a un exponente
def potencia(base, exponente):
    if exponente == 0:                          # Caso base: cualquier número elevado a 0 es 1
        return 1
    else:
        return base * potencia(base, exponente - 1)  # Paso recursivo: base * base^(exponente - 1)

# Solicita al usuario que ingrese la base (puede ser decimal)
base = float(input("Ingrese la base: "))

# Solicita al usuario que ingrese el exponente (entero no negativo)
exponente = int(input("Ingrese el exponente (entero no negativo): "))

# Verifica que el exponente sea válido (mayor o igual a 0)
if exponente < 0:
    print("El exponente debe ser un número entero no negativo.")  # Error si es negativo
else:
    resultado = potencia(base, exponente)  # Calcula la potencia usando recursividad
    print(f"{base} elevado a la {exponente} es {resultado}")  # Muestra el resultado



# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

# Función recursiva que convierte un número decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""  # Al llegar a 0, detiene la recursión y devuelve cadena vacía
    else:
        return decimal_a_binario(n // 2) + str(n % 2) # Divide el número entre 2 y concatena el bit (resto) al final

def convertir_a_binario(n): # Corrige el caso especial para n = 0 devolviendo "0"
    if n == 0:
        return "0"  # Representación binaria de 0
    else:
        return decimal_a_binario(n)

# Solicita un número entero positivo al usuario
numero = int(input("Ingrese un número entero positivo (decimal) para convertir a binario: "))
if numero < 0:
    print("Debe ingresar un número positivo.")  # Validación
else:
    binario = convertir_a_binario(numero)  # Se obtiene la representación binaria
    print(f"El número {numero} en binario es: {binario}")  # Muestra el resultado



# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena 
# de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

# Función recursiva que verifica si una cadena es un palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True  # Caso base: 0 o 1 letras siempre forman un palíndromo
    if palabra[0] != palabra[-1]:
        return False  # Si los extremos no coinciden, no es palíndromo
    return es_palindromo(palabra[1:-1])  # Llamada recursiva sin los extremos

# Solicita al usuario una palabra (sin espacios ni tildes)
texto = input("Ingrese una palabra sin espacios ni tildes: ").lower()

# Verifica si la palabra ingresada es un palíndromo
if es_palindromo(texto):
    print(f"La palabra '{texto}' es un palíndromo.")
else:
    print(f"La palabra '{texto}' NO es un palíndromo.")



# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero 
# positivo y devuelva la suma de todos sus dígitos.

# Función recursiva que suma los dígitos de un número entero positivo
def suma_digitos(n):
    if n < 10:
        return n  # Caso base: si tiene un solo dígito, lo devuelve directamente
    else:
        return (n % 10) + suma_digitos(n // 10)  # Suma el último dígito y llama con el resto

# Solicita al usuario un número entero positivo
numero_ingresado = int(input("Ingrese un número entero positivo: "))

# Valida que el número sea positivo antes de llamar a la función
if numero_ingresado < 0:
    print("Por favor, ingrese un número positivo.")
else:
    resultado = suma_digitos(numero_ingresado)  # Llama a la función recursiva
    print(f"La suma de los dígitos de {numero_ingresado} es: {resultado}")



# 7) Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques 
# que necesita para construir toda la pirámide.

# Función recursiva que calcula el total de bloques en una pirámide
def contar_bloques(n):
    if n == 1:
        return 1  # Caso base: si solo queda un bloque, devuelve 1
    else:
        return n + contar_bloques(n - 1)  # Suma bloques del nivel actual y niveles superiores

# Solicita al usuario el número de bloques en el nivel más bajo
nivel_inferior = int(input("Ingrese el número de bloques del nivel más bajo: "))

# Valida que el número sea positivo antes de calcular
if nivel_inferior <= 0:
    print("Por favor, ingrese un número positivo.")
else:
    total_bloques = contar_bloques(nivel_inferior)  # Calcula el total con la función recursiva
    print(f"Total de bloques para la pirámide: {total_bloques}")



# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero 
# positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

# Función recursiva que cuenta cuántas veces aparece un dígito en un número entero positivo
def contar_digito(numero, digito):
    if numero == 0:
        return 0  # Caso base: si el número es 0, no quedan dígitos por contar
    else:
        cuenta = 1 if (numero % 10) == digito else 0  # Cuenta 1 si el último dígito coincide con el dígito buscado
        return cuenta + contar_digito(numero // 10, digito) # Suma la cuenta actual con la recursión sobre el número sin el último dígito

# Solicita al usuario un número entero positivo y un dígito (para contarlo)
numero_entero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese un dígito (0-9) a contar: "))

# Valida que el número y el dígito estén dentro de los rangos esperados
if numero_entero >= 0 and 0 <= digito <= 9:
    resultado = contar_digito(numero_entero, digito)  # Calcula la cantidad de apariciones
    print(f"El dígito {digito} aparece {resultado} veces en el número {numero_entero}.")
else:
    print("Por favor, ingrese un número positivo y un dígito válido entre 0 y 9.")