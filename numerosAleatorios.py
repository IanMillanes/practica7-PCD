import random

def ObtenerCantidad():
    return int(input("Ingrese la cantidad de números a generar: "))

def CrearListaAleatoria(cantidad, inicio=1, fin=100):
    return [random.randint(inicio, fin) for _ in range(cantidad)]

def GenerarDiccionario(numeros):
    return {posicion+1: valor**2 for posicion, valor in enumerate(numeros)}

def MostrarResultados(originales, cuadrados):
    print("\nNúmeros generados:", originales)
    print("\nCuadrados correspondientes:")
    for clave, valor in cuadrados.items():
        print(f"Posición {clave}: {valor}")

def EjecutarPrograma():
    cantidad = ObtenerCantidad()
    lista_aleatoria = CrearListaAleatoria(cantidad)
    diccionario_cuadrados = GenerarDiccionario(lista_aleatoria)
    MostrarResultados(lista_aleatoria, diccionario_cuadrados)

EjecutarPrograma()