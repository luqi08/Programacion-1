Boeing747 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]


def verificarDisponibilidad(Boeing747):
    verificar = True
    if verificar == True:
        print(Boeing747)
    else:
        print("Este vuelo ya no cuenta con asientos disponibles")


def mostrarAsientos():
    return


pasajeros = {"dni": "Nombre Apellido"}
pasajes = {000000: {"clase": "primera", "asiento": "G8", "dni": 0000000}}
aviones = {"Boeing747": Boeing747}
vuelos = {"EZE": {"Fecha": "20/10/2024", "Origen": "Misiones", "avion": "Boeing747"}}


# Pasajeros: DNI, nombre, apellido
# Pasajes: Numero de pasaje, numero de asiento, clase de asiento, codigo de equipaje
# Aviones: Modelo, asientos
# Vuelos: Destino, fecha, origen
