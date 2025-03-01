class Quicksort():

    def division(self,lista,orden = "asc"):
        #asumimos que el pivote es el primer elemento de la lista 
        pivote = lista[0]
        #declaramos los arreglos para dividri la lista en listas mas pequeñas
        menores, mayores = [], []

        #recorremos la lista desde el elemento arr[1] hasta el final puesto que el primero se asumio que era el pivote
        if(orden == "asc"):
            for i in lista[1:]:
                #buscamos el ordenar de la manera 1,2,3,4,5,6,7,8,9...
                if(i.tamano < pivote.tamano):
                     menores.append(i)
                else:
                    mayores.append(i)
        else:
            for i in lista[1:]:
                #Busamos dejar de la parte derecha del arreglo todos aquellos numeros menores para empezar con los numeros mas grandes de la manera 9,8,7,6,5,4,3,2,1
                if(i.tamano < pivote.tamano):
                    mayores.append(i)
                else:
                     menores.append(i)
        return menores,pivote, mayores
    
    def quicksort(self,lista,orden):
        #si la lista que inggrgese en la funcion solo tiene un elemento o ninguno devuelve el arreglo ya que es su minima expresion
        if len(lista) <= 1:
            return lista
        menores, pivote, mayores = self.division(lista,orden)
        return self.quicksort(menores,orden) + [pivote] + self.quicksort(mayores,orden)