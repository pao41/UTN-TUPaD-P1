# 1) Dado el diccionario precios_frutas. Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300

# Diccionario original con los precios de algunas frutas
precios_frutas = {
    "Banana": 1200,
    "Ananá": 2500,
    "Melón": 3000,
    "Uva": 1450
}

# Se añaden las nuevas frutas
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

# Se muestra el diccionario actualizado
print("\nDiccionario actualizado con la incorporación de nuevas frutas:")
print(precios_frutas)



# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# actualizar los precios de las siguientes frutas: Banana = 1330, Manzana = 1700, Melón = 2800

# Actualización de los precios
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

# Se muestra el diccionario actualizado
print("\nDiccionario con su respectiva actualización de precios en determinadas frutas (banana, manzana, melón):")
print(precios_frutas)



# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios.

# Se crea una lista con los keys (claves)
lista_de_frutas = list(precios_frutas.keys())

# Se muestra la lista
print(f"\nLista de frutas: \n{lista_de_frutas}\n")



# 4) Escribí un programa que permita almacenar y consultar números telefónicos.

# Crear un diccionario vacio
agenda = {}

# Permitir al usuario cargar 5 contactos con su nombre como clave y número como valor
print("\nPor favor, ingresa 5 contactos:")
for i in range(5): # Este bucle se ejecuta 5 veces 
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ") # El nombre ingresado se guarda en la variable nombre
    numero = input(f"Ingresá el número de {nombre}: ") #  Se pide el número asociado a cada nombre ingresado.
    agenda[nombre] = numero  # Se guarda en el diccionario

# Mostrar la agenda
print(f"\nAgenda: {agenda}")

# Solicitar un nombre y mostrale el número asociado, si existe.
nombre_contacto = input("\nConsultá un contacto:\nIngresá el nombre del contacto que querés buscar: ")

# Verificar si el nombre existe en la agenda
if nombre_contacto in agenda: # Busca el contacto en la agenda
    print(f"El número de {nombre_contacto} es: {agenda[nombre_contacto]}") # Imprime el mensaje con nombre y número 
else:
    print(f"No se encontró el contacto '{nombre_contacto}' en la agenda.")



# 5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.

# Solicitar al usuario una frase
frase = input("\nIngrese una frase: ")

palabras = frase.split() # Convierte la frase en una lista de palabras separadas por espacios.

# Palabras únicas
print("\nLista de palabras únicas")
print(set(palabras)) # Se obtiene las palabras únicas usando un set

# Contar palabras
# Crear un diccionario vacío para contar
diccionario_unicas = {}

for palabra in palabras: # Recorre cada palabra 
    if palabra in diccionario_unicas:
        diccionario_unicas[palabra] += 1  # Si ya existe, se suma 1
    else:
        diccionario_unicas[palabra] = 1   # Si no existe, se agrega con valor 1

# Mostrar resultados
print(f"\nCantidad de veces que aparece cada palabra:\n{diccionario_unicas}")



# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno.

# Crear un diccionario vacío para guardar los datos de los alumnos (clave: nombre y valor: tupla con notas)
alumnos = {}

# Permitir al usuario cargar 3 nombres de alumnos y para cada uno 3 notas.
for i in range(3): # Este bucle se ejecuta 3 veces 
    nombre_alumno = input(f"\nIngrese el nombre del alumno {i+1}: ")
    
    print(f"Ingrese 3 notas para {nombre_alumno}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

# Guardar las notas como una tupla y asociar al nombre en el diccionario   
    alumnos[nombre_alumno] = (nota1, nota2, nota3) 

# Mostrar el diccionario
print("\nDiccionario de alumnos y sus notas:")
print(alumnos)

# Mostrar los promedios
# Recorre el diccionario para calcular y mostrar el promedio de cada alumno
print("\nPromedios:")
for nombre_alumno, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre_alumno} tiene un promedio de {promedio:.2f}\n")



# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

# Definir dos sets con números que representan a los estudiantes que aprobaron los parciales 1 y 2.
parcial1 = {5, 8, 11, 13, 14}
parcial2 = {1, 8, 9, 14, 15}
print(f"\nEstudiantes que aprobaron el parcial 1: {parcial1}")
print(f"Estudiantes que aprobaron el parcial 2: {parcial2}")

# Mostrar los que aprobaron ambos parciales.
ambos = parcial1.intersection(parcial2) # Intersección de sets: los que están en ambos sets al mismo tiempo
print("\nEstudiantes que aprobaron ambos parciales:", ambos)

# Mostrar los que aprobaron solo uno de los dos.
solo_uno = parcial1.symmetric_difference(parcial2) # Diferencia simétrica: los que están en uno u otro set, pero no en ambos.
print("Estudiantes que aprobaron solo uno de los parciales:", solo_uno)

# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
total = parcial1.union(parcial2) # Unión de los sets: todos sin repetir
print("Estudiantes que aprobaron al menos un parcial:", total)



# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# Consultar el stock de un producto ingresado.
# Agregar unidades al stock si el producto ya existe.
# Agregar un nuevo producto si no existe.

# Diccionario inicial con productos y su stock
diccionario_stock = {
    "azúcar": 10,
    "harina": 5,
    "fideo": 9,
    "té": 7,
    "manteca": 15,
    "arroz": 10,
    "galleta": 7,
    "jugo": 8,
    "mermelada": 5,
    "mayonesa": 4
}

# Mostrar menú de opciones
print("\nOpciones:")
print("1. Consultar stock de un producto")
print("2. Agregar unidades a un producto existente")
print("3. Agregar un nuevo producto")

# Solicitar una opción al usuario
opcion = input("Ingrese una opción (1-3): ")

# Opción 1
if opcion == "1":
    producto = input("Ingrese el nombre del producto para consultar su stock: ").lower()
    if producto in diccionario_stock:
        print(f"Stock de {producto}: {diccionario_stock[producto]} unidades")
    else:
        print(f"El producto '{producto}' no está en el stock.")

# Opción 2
elif opcion == "2":
    producto = input("Ingrese el nombre del producto al que desea agregar unidades: ").lower()
    if producto in diccionario_stock:
        try:
            cantidad = int(input("Ingrese la cantidad a agregar: "))
            if cantidad > 0:
                diccionario_stock[producto] += cantidad
                print(f"Nuevo stock de {producto}: {diccionario_stock[producto]} unidades")
            else:
                print("La cantidad debe ser mayor a cero.")
        except ValueError:
            print("Debe ingresar un número válido.")
    else:
        print(f"El producto '{producto}' no existe. Debe agregarlo como nuevo producto.")

# Opción 3
elif opcion == "3":
    producto = input("Ingrese el nombre del nuevo producto: ").lower()
    if producto in diccionario_stock:
        print(f"El producto '{producto}' ya existe con stock {diccionario_stock[producto]}.")
    else:
        try:
            cantidad = int(input("Ingrese la cantidad inicial: "))
            if cantidad >= 0:
                diccionario_stock[producto] = cantidad
                print(f"Producto '{producto}' agregado con un stock de {cantidad} unidades.")
            else:
                print("La cantidad debe ser 0 o mayor.")
        except ValueError:
            print("Debe ingresar un número válido.")

else:
    print("Opción inválida. Por favor, ingrese una opción del 1 al 3.")



# 9) Creá una agenda donde las actividads sean tuplas de (día, hora) y los valores sean eventos.

# Agenda: actividad: tupla (día, hora) y valor: evento
print("\nAgenda de actividades")
agenda1 = {
    ("lunes", "09:00"): "Clase de inglés",
    ("martes", "19:00"): "Clase de matemática",
    ("miercoles", "18:00"): "Turno médico",
    ("jueves", "20:00"): "Gimnasio",
    ("viernes", "08:00"): "Reunión de trabajo",
    ("sabado", "15:00"): "Ajedrez",
    ("domingo", "16:00"): "Cumpleaños"
}

# Consultar actividad
dia = input("\nIngresá el día: ")
hora = input("Ingresá la hora (HH:MM): ")
actividad = (dia, hora)

# Mostrar evento si existe
if actividad in agenda1:
    print(f"Actividad programada: {agenda1[actividad]}")
else:
    print("No hay actividad en ese horario.")



# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.

# Diccionario original país -> capital
diccionario_original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Perú": "Lima"}
print("\nPaises y capitales")
print("\nDiccionario original:")
print(diccionario_original)

# Nuevo diccionario (invertido): capital -> país
nuevo_diccionario = {}
for pais, capital in diccionario_original.items():
    nuevo_diccionario[capital] = pais

# Mostrar el resultado
print("\nNuevo diccionario:")
print(nuevo_diccionario)