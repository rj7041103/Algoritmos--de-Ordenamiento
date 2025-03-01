
from dataloader import DataLoader
from reporte import Reporte

def main():
    downloads = DataLoader.load_downloads('descargas.json')
    reporte = Reporte(downloads)
    reporte.mostrar_menu()

if __name__ == "__main__":
    main()