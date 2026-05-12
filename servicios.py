from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        """Método abstracto que implementarán las subclases"""
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas=1):
        # Polimorfismo: cálculo específico para salas
        return self.precio_base * horas

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias=1):
        return self.precio_base * dias