class ErrorSoftwareFJ(Exception):
    """Clase base para excepciones del sistema"""
    pass

class ErrorReservaInvalida(ErrorSoftwareFJ):
    """Se lanza cuando los datos de la reserva no son consistentes"""
    pass

class ServicioNoDisponible(ErrorSoftwareFJ):
    """Se lanza cuando un servicio no puede ser procesado"""
    pass