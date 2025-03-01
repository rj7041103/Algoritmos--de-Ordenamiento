class ShellSort:
    def ordenar(self,arr):
        copia_arr = arr.copy() #creamos una copia y trabajamos con esa copia
        longitud = len(copia_arr)
        gap = longitud // 2  # Inicializamos el intervalo

        while gap > 0:
            # Realizamos inserción con gap para este intervalo
            for indice_actual in range(gap, longitud):
                valor_actual = copia_arr[indice_actual]
                posicion_actual = indice_actual

                # Desplazamos elementos menores hacia la derecha
                while posicion_actual >= gap and len(copia_arr[posicion_actual - gap].url) < len(valor_actual.url):
                    copia_arr[posicion_actual] = copia_arr[posicion_actual - gap]
                    posicion_actual -= gap
                #sino encuentra numeros mayores deja el mismo valor o si lo encontro la posicion actual se resta en uno va de derecha a izquierda buscando valores menores al valor actual que se obtuvo para ubicarlos mas a la izquierda 
                copia_arr[posicion_actual] = valor_actual

            gap //= 2  # Reducimos el intervalo a la mitad

        return copia_arr