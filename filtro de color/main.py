import random

# Generar una matriz de 12x12 con tonos de gris aleatorios (0-255)
def generar_matriz_grises(tamano=12):
    return [[random.randint(0, 255) for _ in range(tamano)] for _ in range(tamano)]


# Función que busca un tono de gris en la imagen
def busqueda_en_imagen(imagen, tono):
    resultado = {}
    for y, fila in enumerate(imagen):
        for x, pixel in enumerate(fila):
            if pixel == tono:
                resultado[(x, y)] = pixel
    return resultado


# Función principal
def main():
    # Generar la imagen en escala de grises (matriz 12x12)
    imagen = generar_matriz_grises(8)
    
    # Imprimir la matriz de grises
    print("Matriz de tonos de gris:")
    for fila in imagen:
        print(fila)

    # Pedir el tono de gris que el usuario quiere buscar
    tono_buscado = int(input("Introduce el tono de gris que deseas buscar (0-255): "))

    # Buscar el tono en la imagen
    resultado = busqueda_en_imagen(imagen, tono_buscado)

    # Mostrar la cantidad de píxeles encontrados y sus coordenadas
    cantidad_pixeles = len(resultado)
    print(f"\nSe encontraron {cantidad_pixeles} píxeles con el tono {tono_buscado}.")
    
    if cantidad_pixeles > 0:
        print("Coordenadas de los píxeles encontrados:")
        for coordenada in resultado.keys():
            print(coordenada)


# Ejecutar el programa
if __name__ == "__main__":
    main()
