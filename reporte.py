from datetime import datetime
from quicksort import Quicksort
from mergesort import MergeSort
from heapsort import HeapSort
from shellsort import ShellSort
import json
class Reporte:
    def __init__(self, downloads):
        self.downloads = downloads
    
    def mostrar_menu(self):
        
        while True:
           print("Seleccione una opcion:\n" +
           "[1] Listar las descargas completadas de forma descendente por  tamaño (Quicksort)\n" +
           "[2] Listar las descargas que no han sido completadas de forma ascendente por  fecha de inicio (Mergesort)\n" +
           "[3] Listar las descargas a partir de una fecha(YYYY-MM-DD HH:MM) y un dominio dados por el usuario y ordenados de forma ascendente según su tamaño (Heapsort)\n" +
           "[4] Listar las descargar de forma descendente por la longitud de su url y que cumplan con un estado indicado (Shellsort)\n"+
           "[5] Salir\n")

           opcion = int(input("-> "))
           print("\n")
           match opcion:
                case 1:
                    quick = Quicksort().quicksort(self.downloads,"desc")
                    for dato in quick:
                        json_data = json.dumps(dato.to_dict(), indent=4, sort_keys=False)
                        print(json_data+"\n")
                    pass
                case 2:
                    aux = []
                    #Tomamos todas aquellas descargas pendientes, canceladas, entre otros 
                    for dato in self.downloads:
                        if dato.estado != "completada":
                            aux.append(dato)
                    #Pasamos la lista con los objetos de estados incompletos 
                    mergesort = MergeSort().sort(aux)
                    for dato in mergesort:
                        json_data = json.dumps(dato.to_dict(), indent=4, sort_keys=False)
                        print(json_data+"\n")
                    pass
                case 3:
                    fecha = input("Ingrese la fecha de inicio de la manera YYYY-MM-DD HH:MM (2024-10-14 11:00:00) : ")
                    dominio = input("Ingrese el dominio de la descarga:")
                    print() 
                    fecha_usuario = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
                    aux = []
                    #Recolectamos todas aquellas descargas que sean mayores o iguales a las que el usuario haya puesto, marcando el limite de inicio
                    for dato in self.downloads:
                        if dato.fecha_inicio >= fecha_usuario and dato.url.endswith(dominio):
                            aux.append(dato)
                    heapsort = HeapSort().heapSort(aux)
                    for dato in heapsort:
                        json_data = json.dumps(dato.to_dict(), indent=4, sort_keys=False)
                        print(json_data+"\n")
                    pass
           
                case 4:
                    estado = input("Ingrese el estado de la descarga: ")
                    print()
                    aux = []
                    for dato in self.downloads:
                        if dato.estado == estado:
                            aux.append(dato)
                    shellsort = ShellSort().ordenar(aux)
                    for dato in shellsort:
                        json_data = json.dumps(dato.to_dict(), indent=4, sort_keys=False)
                        print(json_data+"\n")
                    pass
                case 5:
                    # Salir
                    break