class MetodosOrdenamiento:

    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range (i + 1, n):
                if arreglo[i] > arreglo[j]:
                    aux = arreglo[i]
                    arreglo[i] = arreglo[j]
                    arreglo[j] = aux
        return arreglo

    def sort_seleccion(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j
                    temp = arreglo[i]
                    arreglo[i] = arreglo[min_index]
                    arreglo[min_index] = temp
        return arreglo
    
                    