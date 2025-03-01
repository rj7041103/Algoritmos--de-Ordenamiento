import json
from datetime import datetime

class Download:
    def __init__(self, url, tamano, fecha_inicio, estado):
        self.url = url
        self.tamano = tamano
        self.fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d %H:%M:%S")
        self.estado = estado

    def to_dict(self):
        return {
            "url": self.url,
            "tamano": self.tamano,
            "fecha_inicio": self.fecha_inicio.isoformat() if isinstance(self.fecha_inicio, datetime) else self.fecha_inicio,
            "estado": self.estado,
        }

class DataLoader:
    @staticmethod
    def load_downloads(json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
        return [Download(**item) for item in data]