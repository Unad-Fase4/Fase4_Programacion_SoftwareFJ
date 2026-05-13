from abc import ABC, abstractmethod

# Abstracción: Clase base para entidades generales 
class Entidad(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad

# Encapsulación: Clase Cliente con datos privados 
class Cliente(Entidad):
    def __init__(self, cedula, nombre, correo):
        super().__init__(cedula)
        self.__nombre = nombre  # 
        self.__correo = correo  # 

    def obtener_datos(self):
        return f"Cliente: {self.__nombre} (ID: {self.id_entidad})"

# Clase Reserva que integra cliente y servicio 
class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo(horas=self.duracion)
            self.estado = "Confirmada"
            return f"Reserva confirmada. Total: ${costo}"
        except Exception as e:
            self.estado = "Fallida"
            raise e