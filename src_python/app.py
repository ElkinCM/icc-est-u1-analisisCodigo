import benchmarking as Be
import metodos_ordenamiento as Met
if __name__ == "__main__":
	print("Hello World")
	Be.Benchmarking()

	metodos = Met.MetodosOrdenamiento()
	benchmark = Be.Benchmarking()
	
	tam= 1000
	arreglo = benchmark.buildArreglo(tam)

	metodos = {
		"1 - clave" :  metodos.sortByBubble,
		"2 - seleccion" : metodos.sort_seleccion,
	}

	resultados = []

	for nombre, metodo in metodos.items():
		tiempo = benchmark.medir_tiempo(metodo, arreglo)
		tuplaResult = (tam, nombre, tiempo)
		resultados.append(tuplaResult)

	for resultado in resultados:
		tam, nombre, tiempo = resultado
		print(f"Arreglo de {tam} elementos ordenado por {nombre} en {tiempo:.6f} segundos")
