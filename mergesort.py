
class MergeSort():
    def sort(self,lista):
        if len(lista) <= 1:
            return lista
        #dividimos a la mitad para obtner el pivote 
        mid = len(lista) // 2
        #usamos la recursion para la division de la lista general en sublistas hasta que solo quede un elemento dentro de la lista
        left = self.sort(lista[:mid])
        right = self.sort(lista[mid:])
        #pasamos las listas resultantes a la funcion merge para que se ordenen de mayor a menor
        return self.merge(left, right)
    
    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            #Convertimos a fechas los strings que hay en el json de prueba
            if left[i].fecha_inicio < right[j].fecha_inicio:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        """
        Si hay elementos de la lista tanto de la parte izquierda como de la derecha que no se alcanzaron a comparar , los
        que quedaron por comparar se agregan al arreglo de result para terminar de ordenar el arreglo despues
        
        """
        result += left[i:]
        result += right[j:]
        return result