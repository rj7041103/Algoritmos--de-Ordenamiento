class HeapSort():
    def heapify(self, arr, n, i):
        largest = i  # Inicializar el nodo raíz como el más grande
        izq = 2 * i + 1  # Hijo izquierdo
        der = 2 * i + 2  # Hijo derecho

        # Si el hijo izquierdo es mayor que el nodo raíz
        if izq < n and arr[i].tamano < arr[izq].tamano:
            largest = izq

        # Si el hijo derecho es mayor que el nodo más grande hasta ahora
        if der < n and arr[largest].tamano < arr[der].tamano:
            largest = der

        # Si el nodo raíz no es el más grande
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
            # Llamada recursiva para garantizar que el subárbol afectado cumpla la propiedad de heap
            self.heapify(arr, n, largest)

    def heapSort(self, list):
        n = len(list)

        # Construir un Max-Heap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(list, n, i)

        # Extraer elementos del heap uno por uno
        for i in range(n - 1, 0, -1):
            list[i], list[0] = list[0], list[i]  # Mover la raíz actual al final
            self.heapify(list, i, 0)  # Llamar a heapify en el heap reducido

        return list