from modelos import Cliente, Reserva
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from excepciones import ErrorReservaInvalida, ServicioNoDisponible
from logger import registrar_log

def simular_operaciones():
    # 1. Creamos algunos datos base
    cliente_valido = Cliente("1010", "Brayan Silva", "brayan@correo.com")
    sala = ReservaSala("Sala de Juntas", 50000)
    laptop = AlquilerEquipo("MacBook Pro", 120000)
    
    operaciones = [
        # Operaciones que deberían servir
        {"cliente": cliente_valido, "servicio": sala, "duracion": 2, "tipo": "Éxito"},
        {"cliente": cliente_valido, "servicio": laptop, "duracion": 3, "tipo": "Éxito"},
        {"cliente": cliente_valido, "servicio": sala, "duracion": 5, "tipo": "Éxito"},
        {"cliente": cliente_valido, "servicio": laptop, "duracion": 1, "tipo": "Éxito"},
        {"cliente": cliente_valido, "servicio": sala, "duracion": 1, "tipo": "Éxito"},
        
        # Operaciones que deberían fallar, como simulisacion 
        {"cliente": None, "servicio": sala, "duracion": 2, "tipo": "Fallo: Sin Cliente"},
        {"cliente": cliente_valido, "servicio": None, "duracion": 3, "tipo": "Fallo: Sin Servicio"},
        {"cliente": cliente_valido, "servicio": sala, "duracion": -1, "tipo": "Fallo: Tiempo Negativo"},
        {"cliente": cliente_valido, "servicio": laptop, "duracion": 0, "tipo": "Fallo: Tiempo Cero"},
        {"cliente": "Invalido", "servicio": sala, "duracion": 2, "tipo": "Fallo: Tipo Dato Erróneo"}
    ]

    print("--- INICIANDO SIMULACIÓN DE 10 OPERACIONES ---")
    
    for i, op in enumerate(operaciones, 1):
        try:
            print(f"\nOperación {i}: {op['tipo']}")
            
            # Validaciones estrictas antes de procesar
            if op['cliente'] is None or not isinstance(op['cliente'], Cliente):
                raise ErrorReservaInvalida("Cliente no válido o no registrado.")
            
            if op['servicio'] is None:
                raise ServicioNoDisponible("El servicio solicitado no existe.")
                
            if op['duracion'] <= 0:
                raise ErrorReservaInvalida("La duración debe ser mayor a cero.")

            # Si pasa las validaciones, creamos la reserva
            reserva = Reserva(op['cliente'], op['servicio'], op['duracion'])
            resultado = reserva.confirmar()
            print(f"RESULADO: {resultado}")

        except (ErrorReservaInvalida, ServicioNoDisponible) as e:
            error_msg = f"ERROR CONTROLADO en Op {i}: {e}"
            print(error_msg)
            registrar_log(error_msg) # Se registra en el archivo de logs 
            
        except Exception as e:
            error_msg = f"ERROR INESPERADO en Op {i}: {type(e).__name__} - {e}"
            print(error_msg)
            registrar_log(error_msg)
            
        finally:
            print("Estado: Sistema estable y operando...") # El sistema sigue funcionando 

if __name__ == "__main__":
    simular_operaciones()