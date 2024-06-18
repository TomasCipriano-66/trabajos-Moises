from contextlib import contextmanager


@contextmanager
def gestionar_archivo(ruta_archivo, modo):
    archivo = open(ruta_archivo, modo)
    try:
        yield archivo
    finally:
        archivo.close()

    opcion = input("¿Qué función desea activar? (1 para leer archivo, 2 para escribir archivo): ")

    if opcion == '1':
      leer_archivo()
    elif opcion == '2':
      escribir_archivo()
    else:
      print("Opción no válida. Por favor, ingrese 1 o 2.")
      

def leer_archivo():
    ruta_archivo = input("Ingrese el archivo que desea leer(no olvide al .txt): ")
    try:
        with gestionar_archivo(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f'Error: El archivo {ruta_archivo} no fue encontrado.')

def escribir_archivo():
    ruta_archivo = input("Ingrese el archivo en el que desea escribir(no olvide al .txt): ")
    with gestionar_archivo(ruta_archivo, 'w') as archivo:
        archivo.write('Línea 1\n')
        archivo.write('Línea 2\n')
        archivo.write('Línea 3\n')
    print(f'Se han escrito las líneas en el archivo {ruta_archivo}.')


opcion = input("¿Qué función desea activar? (1 para leer archivo, 2 para escribir archivo): ")

if opcion == '1':
  leer_archivo()
elif opcion == '2':
  escribir_archivo()
else:
  print("Opción no válida. Por favor, ingrese 1 o 2.")