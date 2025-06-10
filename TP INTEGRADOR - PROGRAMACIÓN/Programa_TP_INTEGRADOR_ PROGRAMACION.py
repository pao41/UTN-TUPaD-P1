import csv
import time
import matplotlib.pyplot as plt

# Función para cargar productos desde un archivo CSV
def cargar_productos_csv(nombre_archivo):
    inventario = []
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["precio"] = float(fila["precio"])  # Convertir precio a número
            inventario.append(fila)
    return inventario

# Ordenar por nombre con sorted() y lambda
def ordenar_por_nombre(lista):
    return sorted(lista, key=lambda x: x["nombre"])

# Merge Sort por precio
def merge_sort_precio(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort_precio(lista[:medio])
    derecha = merge_sort_precio(lista[medio:])

    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]["precio"] <= derecha[j]["precio"]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Búsqueda binaria por ID (requiere lista ya ordenada)
def busqueda_binaria_id(lista_ordenada, id_buscado):
    bajo = 0
    alto = len(lista_ordenada) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista_ordenada[medio]["id"] == id_buscado:
            return lista_ordenada[medio]
        elif lista_ordenada[medio]["id"] < id_buscado:
            bajo = medio + 1
        else:
            alto = medio - 1
    return None

# Búsqueda lineal por ID
def busqueda_lineal_id(lista, id_buscado):
    for producto in lista:
        if producto["id"] == id_buscado:
            return producto
    return None

# ------------------------------
# Programa principal
# ------------------------------

print("Bienvenido al sistema de inventario.\n")

# Cargar inventario desde CSV
nombre_csv = input("Ingrese el nombre del archivo CSV (ej: productos.csv): ")
inventario = cargar_productos_csv(nombre_csv)

# Ordenar una sola vez por ID para usar en búsqueda binaria
inventario_ordenado_por_id = sorted(inventario, key=lambda x: x["id"])

# Ordenamiento
opcion = input("¿Desea ordenar los productos por (1) nombre o (2) precio? Ingrese 1 o 2: ")
if opcion == "1":
    ordenados = ordenar_por_nombre(inventario)
    print("\nProductos ordenados por nombre:")
    for prod in ordenados[:50]:  # Muestra solo los primeros 50
        print(prod)
elif opcion == "2":
    inventario = merge_sort_precio(inventario)
    print("\nProductos ordenados por precio:")
    for prod in inventario[:50]:  # Muestra solo los primeros 50
        print(prod)
else:
    print("Opción inválida.")

# Búsqueda por ID
id_buscado = input("\nIngrese el ID del producto que desea buscar (ej: P002): ")

repeticiones = 100
tiempos_binaria = []
tiempos_lineal = []

# Medir tiempos por repetición
for _ in range(repeticiones):
    inicio_bin = time.perf_counter()
    busqueda_binaria_id(inventario_ordenado_por_id, id_buscado)
    fin_bin = time.perf_counter()
    tiempos_binaria.append(fin_bin - inicio_bin)

    inicio_lin = time.perf_counter()
    busqueda_lineal_id(inventario, id_buscado)
    fin_lin = time.perf_counter()
    tiempos_lineal.append(fin_lin - inicio_lin)

# Calcular tiempo promedio
promedio_binaria = sum(tiempos_binaria) / repeticiones
promedio_lineal = sum(tiempos_lineal) / repeticiones

# Mostrar últimos resultados de búsqueda (última iteración)
resultado_bin = busqueda_binaria_id(inventario_ordenado_por_id, id_buscado)
resultado_lin = busqueda_lineal_id(inventario, id_buscado)

print("\nResultado de búsqueda binaria:")
if resultado_bin:
    print(resultado_bin)
else:
    print("No encontrado.")

print(f"Tiempo promedio búsqueda binaria: {promedio_binaria:.10f} segundos")

print("\nResultado de búsqueda lineal:")
if resultado_lin:
    print(resultado_lin)
else:
    print("No encontrado.")

print(f"Tiempo promedio búsqueda lineal: {promedio_lineal:.10f} segundos")

# Gráfico lineal comparativo
plt.figure(figsize=(10,6))
plt.plot(tiempos_binaria, label="Búsqueda Binaria", color='blue')
plt.plot(tiempos_lineal, label="Búsqueda Lineal", color='orange')
plt.xlabel('Número de repeticiones')
plt.ylabel('Tiempo por repetición (segundos)')
plt.title('Comparación de tiempos de búsqueda')
plt.legend()
plt.grid(True)
plt.show()
