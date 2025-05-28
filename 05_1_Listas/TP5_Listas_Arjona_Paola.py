# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# Lista de numeros del 1 al 100 multiplos de 4.
multiplos_de_4 = list(range(4,101,4))

# Mostrar resultado.
print(multiplos_de_4)



# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.

# Crear una lista de 5 elementos.
lista1 = [3, 25, "arbol", "sur", 100]

# Ubicar el penúltimo elemento (-2 corresponde al penúltimo elemento).
penultima_posicion = lista1[-2]

# Mostrar el penúltimo elemento.
print(f"Lista: {lista1}")
print(f"La penúltima posición en la lista es: {penultima_posicion}")



# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

# Crear lista vacia.
lista2 = []

# Agregar 3 palabras usando append.
lista2.append("perro")
lista2.append("sol")
lista2.append("estrella")

# Mostrar resultado.
print(f"La lista resultantes es: {lista2}")



# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla.

# Lista animales
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo y último valor de la lista por “loro” y “oso”, respectivamente. (-1 corresponde al último elemento de la lista).
animales[1] = "loro"
animales[-1] = "oso"

# Resultado.
print(f"La lista resultante es: {animales}")



# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

# Programa
numeros = [8, 15, 3, 22, 7] # Crea una lista llamada numeros.
numeros.remove(max(numeros)) # Encuentra el máximo valor de la lista usando la función max, y elimina ese valor usando remove.
print(numeros) # Muestra la lista actualizada (sin el valor máximo).

# Explicación: El programa busca el valor máximo en la lista "numeros" con la función max (en este caso es el 22), y lo elimina usando remove. 
# Posterirormente muestra la lista sin dicho valor.



# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

# Crear lista del 10 al 30 (incluido), saltos de 5.
lista_numeros = list(range(10,31,5))

# Identificar y extraer los dos primeros números usando slicing (:2 extrae los 2 primeros elementos).
primeros_dos = lista_numeros[:2]


# Mostrar los dos primeros números.
print(f"Lista de números del 10 al 30, haciendo saltos de 5 en 5:\n {lista_numeros}")
print(f"Los dos primeros números son: {primeros_dos[0]} y {primeros_dos[1]}")



# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

# Lista autos
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los valores del índice 1 y 2 por corsa y  clio respectivamente.
autos[1] = "corsa"
autos[2] = "clio"

# Mostrar lista actualizada.
print(f"La lista de autos actualizada es:\n {autos}")



# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

# Crear lista vacia.
dobles = []

# Agregar el doble de 5, 10 y 15 usando append.
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Mostrar la lista resultante.
print(f"La lista resultante es:\n {dobles}")



# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

# Lista compras (posee 3 elementos)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append. (posición [2] de compras).
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. (posición [1] de compras y posición [1] del segundo elemento).
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente usando remove. (posición [0] de compras)
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(f"La lista resultante es:\n {compras}")



# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False

# Crear lista anidada (posee 4 elemtos)
lista_anidada = [
    15,                     # posición 0
    True,                   # posición 1
    [25.5, 57.9, 30.6],     # posición 2
    False                   # posición 3
    ]

# Imprimir la lista resultante por pantalla.
print(f"La lista resultante es:\n {lista_anidada}")