import random
import time
import matplotlib.pyplot as plt


def ordenamiento_burbuja(lista):

    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def ordenamiento_seleccion(lista):

    lista = lista.copy()
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


def ordenamiento_insercion(lista):

    lista = lista.copy()
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista


def ordenamiento_rapido(lista):

    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return ordenamiento_rapido(izquierda) + medio + ordenamiento_rapido(
        derecha)


def ordenamiento_fusion(lista):

    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = ordenamiento_fusion(lista[:medio])
    derecha = ordenamiento_fusion(lista[medio:])
    return fusionar(izquierda, derecha)


def fusionar(izquierda, derecha):

    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


def medir_tiempo(algoritmo, lista):

    inicio = time.time()
    algoritmo(lista)
    fin = time.time()
    return fin - inicio


def main():
    # Lista de 30 elementos aleatorios
    lista = [random.randint(0, 100) for _ in range(30)]

    # Mostrar el arreglo original
    print("Arreglo original:")
    print(lista)

    # Elegir método de ordenamiento
    print("Seleccione el método de ordenamiento:")
    print("1. Burbuja")
    print("2. Selección")
    print("3. Inserción")
    print("4. Rápido")
    print("5. Fusión")
    opcion = int(input("Ingrese el número correspondiente: "))

    algoritmos = {
        1: ordenamiento_burbuja,
        2: ordenamiento_seleccion,
        3: ordenamiento_insercion,
        4: ordenamiento_rapido,
        5: ordenamiento_fusion
    }

    if opcion in algoritmos:
        nombre = list(algoritmos.keys())[opcion - 1]

        # Medir el tiempo de ejecución
        tiempo = medir_tiempo(algoritmos[opcion], lista)

        # Mostrar el arreglo ordenado
        lista_ordenada = algoritmos[opcion](lista)
        print(f"Arreglo ordenado con {nombre}:")
        print(lista_ordenada)
        print(
            f"Tiempo de ejecución del método {nombre}: {tiempo:.6f} segundos")

        # Graficar los resultados
        plt.figure(figsize=(12, 6))
        plt.bar(nombre, tiempo, color='skyblue')
        plt.title('Tiempo de Ejecución del Algoritmo de Ordenamiento')
        plt.xlabel('Método de Ordenamiento')
        plt.ylabel('Tiempo de Ejecución (s)')
        plt.grid(axis='y')
        plt.show()
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
