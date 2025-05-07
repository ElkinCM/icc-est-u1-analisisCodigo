import benchmarking as Be
import metodos_ordenamiento as Met
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Hello World")
    
    benchmark = Be.Benchmarking()
    metodos = Met.MetodosOrdenamiento()

    tamanios = [500, 1000, 2000]
    
    tiemposbymetodo = {
        "1 - clave": [],
        "2 - seleccion": []
    }

    for tam in tamanios:
        arreglo = benchmark.buildArreglo(tam)
        
        metodos_dict = {
            "1 - clave": metodos.sortByBubble,
            "2 - seleccion": metodos.sort_seleccion,
        }

        for nombre, metodo in metodos_dict.items():
            tiempo = benchmark.medir_tiempo(metodo, arreglo)
            tiemposbymetodo[nombre].append(tiempo)
            print(f"Arreglo de {tam} elementos ordenado por {nombre} en {tiempo:.6f} segundos")

    plt.figure(figsize=(10, 6))

    for nombre, tiempos in tiemposbymetodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker='o')
    
    plt.xlabel('Tamaño del arreglo')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Tiempo de ordenamiento por método')
    plt.legend()
    plt.grid(True)
    plt.show()
