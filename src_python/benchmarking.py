import random
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    
    def __init__(self):
        print("Bench Inicializado")
        self.mOrdenamiento = MetodosOrdenamiento()
        arreglo = self.buildArreglo(10000)

        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMilis = self.contar_con_current_time_milles(tarea)
        tiempoNanos = self.contar_con_nano_time(tarea)
        print(f"Tiempo en milisegundos: {tiempoMilis} ms")
        print(f"Tiempo en nanosegundos: {tiempoNanos} ns")


    def buildArreglo(self, n):
        arreglo = []
        for i in range(n):
            num = random.randint(0, 9999999)
            arreglo.append(num)
        return arreglo
    
    def contar_con_current_time_milles(self, tarea):
        inicio = time.time()
        tarea()
        return (time.time() - inicio)

    def contar_con_nano_time(self, tarea):
        inicio = time.time()
        tarea()
        return (time.time() - inicio) / 1_000_000_000.0