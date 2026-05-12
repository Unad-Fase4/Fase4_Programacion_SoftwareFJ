import datetime

def registrar_log(mensaje):
    with open("errores.log", "a") as archivo:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] - {mensaje}\n")