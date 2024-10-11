"""
-----------------------------------------------------------------------------------------------
Título: SISTEMA DE COMPRA DE PASAJES DE AVION
Fecha: 24/9/2024
Autor: Facundo Muruchi - Alvaro Beron - Luis Lin
-----------------------------------------------------------------------------------------------
"""

# ----------------------------------------------------------------------------------------------
# MÓDULOS
# ----------------------------------------------------------------------------------------------
import modulo_alvaro, modulo_facu, modulo_luis, modulo_compras, time


# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------
def preGenerarPasajes():
    return


def cancelarBoleto():
    return


# ----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
# ----------------------------------------------------------------------------------------------
def main():
    # -------------------------------------------------
    # Inicialización de variables
    # ----------------------------------------------------------------------------------------------
    aviones = {  # 10 Aviones
        "Boeing747-800": {
            "Matricula": "LV-ABC",
            "Asientos": {"primera": 20, "economica": 162},
        },
        "Boeing747-800": {
            "Matricula": "LV-BRD",
            "Asientos": {"primera": 20, "economica": 162},
        },
        "Boeing747-800": {
            "Matricula": "LV-CFT",
            "Asientos": {"primera": 20, "economica": 162},
        },
        "Boeing747-800": {
            "Matricula": "LV-DRT",
            "Asientos": {"primera": 20, "economica": 162},
        },
        "Boeing747-800": {
            "Matricula": "LV-EFP",
            "Asientos": {"primera": 20, "economica": 162},
        },
        "AirbusA320Neo": {
            "Matricula": "LV-GHT",
            "Asientos": {"primera": 28, "economica": 150},
        },
        "AirbusA320Neo": {
            "Matricula": "LV-HJK",
            "Asientos": {"primera": 28, "economica": 150},
        },
        "AirbusA320Neo": {
            "Matricula": "LV-JLM",
            "Asientos": {"primera": 28, "economica": 150},
        },
        "AirbusA320Neo": {
            "Matricula": "LV-KRS",
            "Asientos": {"primera": 28, "economica": 150},
        },
        "AirbusA320Neo": {
            "Matricula": "LV-LPQ",
            "Asientos": {"primera": 28, "economica": 150},
        },
    }

    pasajeros = {  # 30 Pasajeros precargados
        47307151: {"nombre": "Juan", "apellido": "Perez"},
        40215863: {"nombre": "Maria", "apellido": "Gomez"},
        38901453: {"nombre": "Carlos", "apellido": "Lopez"},
        42758963: {"nombre": "Ana", "apellido": "Martinez"},
        39456821: {"nombre": "Jose", "apellido": "Rodriguez"},
        41874529: {"nombre": "Laura", "apellido": "Fernandez"},
        40125678: {"nombre": "Sofia", "apellido": "Garcia"},
        38501452: {"nombre": "Diego", "apellido": "Sanchez"},
        42896532: {"nombre": "Camila", "apellido": "Diaz"},
        41236547: {"nombre": "Martin", "apellido": "Gonzalez"},
        43985621: {"nombre": "Lucia", "apellido": "Romero"},
        39874512: {"nombre": "Mateo", "apellido": "Castro"},
        41798543: {"nombre": "Julieta", "apellido": "Suarez"},
        43652189: {"nombre": "Lucas", "apellido": "Mendez"},
        41327856: {"nombre": "Emilia", "apellido": "Vega"},
        42789654: {"nombre": "Nicolas", "apellido": "Cabrera"},
        39452187: {"nombre": "Valentina", "apellido": "Silva"},
        42985612: {"nombre": "Federico", "apellido": "Molina"},
        40312654: {"nombre": "Agustina", "apellido": "Rios"},
        41985463: {"nombre": "Tomas", "apellido": "Ortega"},
        41258743: {"nombre": "Milagros", "apellido": "Ibarra"},
        43625489: {"nombre": "Gabriel", "apellido": "Reyes"},
        39874532: {"nombre": "Sol", "apellido": "Moreno"},
        42987145: {"nombre": "Benjamin", "apellido": "Paz"},
        40541236: {"nombre": "Martina", "apellido": "Campos"},
        41896325: {"nombre": "Sebastian", "apellido": "Soto"},
        42365471: {"nombre": "Bianca", "apellido": "Villalba"},
        43852147: {"nombre": "Maximiliano", "apellido": "Aguilar"},
        40215698: {"nombre": "Florencia", "apellido": "Pereyra"},
        42589647: {"nombre": "Leandro", "apellido": "Navarro"},
    }

    vuelos = {
        # Día 1 - Lunes
        "VU001": {
            "Fecha": "07/10/2024 | 06:00",
            "Origen": "Ciudad Autónoma de Buenos Aires (CABA)",
            "Destino": "La Plata (Buenos Aires)",
            "Avion": "LV-ABC",
        },
        "VU002": {
            "Fecha": "07/10/2024 | 08:00",
            "Origen": "La Plata (Buenos Aires)",
            "Destino": "Paraná (Entre Ríos)",
            "Avion": "LV-BRD",
        },
        "VU003": {
            "Fecha": "07/10/2024 | 10:00",
            "Origen": "Paraná (Entre Ríos)",
            "Destino": "Santa Fe",
            "Avion": "LV-CFT",
        },
        "VU004": {
            "Fecha": "07/10/2024 | 13:00",
            "Origen": "Santa Fe",
            "Destino": "Córdoba",
            "Avion": "LV-DRT",
        },
        "VU005": {
            "Fecha": "07/10/2024 | 16:00",
            "Origen": "Córdoba",
            "Destino": "Santiago del Estero",
            "Avion": "LV-EFP",
        },
        # Día 2 - Martes
        "VU006": {
            "Fecha": "08/10/2024 | 06:00",
            "Origen": "Santiago del Estero",
            "Destino": "San Miguel de Tucumán (Tucumán)",
            "Avion": "LV-GHT",
        },
        "VU007": {
            "Fecha": "08/10/2024 | 08:00",
            "Origen": "San Miguel de Tucumán (Tucumán)",
            "Destino": "San Fernando del Valle de Catamarca",
            "Avion": "LV-HJK",
        },
        "VU008": {
            "Fecha": "08/10/2024 | 10:00",
            "Origen": "San Fernando del Valle de Catamarca",
            "Destino": "La Rioja",
            "Avion": "LV-JLM",
        },
        "VU009": {
            "Fecha": "08/10/2024 | 13:00",
            "Origen": "La Rioja",
            "Destino": "San Juan",
            "Avion": "LV-KRS",
        },
        "VU010": {
            "Fecha": "08/10/2024 | 16:00",
            "Origen": "San Juan",
            "Destino": "Mendoza",
            "Avion": "LV-LPQ",
        },
        # Día 3 - Miércoles
        "VU011": {
            "Fecha": "09/10/2024 | 06:00",
            "Origen": "Mendoza",
            "Destino": "San Luis",
            "Avion": "LV-ABC",
        },
        "VU012": {
            "Fecha": "09/10/2024 | 09:00",
            "Origen": "San Luis",
            "Destino": "Formosa",
            "Avion": "LV-BRD",
        },
        "VU013": {
            "Fecha": "09/10/2024 | 12:00",
            "Origen": "Formosa",
            "Destino": "Resistencia (Chaco)",
            "Avion": "LV-CFT",
        },
        "VU014": {
            "Fecha": "09/10/2024 | 15:00",
            "Origen": "Resistencia (Chaco)",
            "Destino": "Corrientes",
            "Avion": "LV-DRT",
        },
        "VU015": {
            "Fecha": "09/10/2024 | 18:00",
            "Origen": "Corrientes",
            "Destino": "Posadas (Misiones)",
            "Avion": "LV-EFP",
        },
        # Día 4 - Jueves
        "VU016": {
            "Fecha": "10/10/2024 | 06:00",
            "Origen": "Posadas (Misiones)",
            "Destino": "Formosa",
            "Avion": "LV-GHT",
        },
        "VU017": {
            "Fecha": "10/10/2024 | 08:00",
            "Origen": "Formosa",
            "Destino": "Salta",
            "Avion": "LV-HJK",
        },
        "VU018": {
            "Fecha": "10/10/2024 | 10:00",
            "Origen": "Salta",
            "Destino": "San Salvador de Jujuy",
            "Avion": "LV-JLM",
        },
        "VU019": {
            "Fecha": "10/10/2024 | 13:00",
            "Origen": "San Salvador de Jujuy",
            "Destino": "San Fernando del Valle de Catamarca",
            "Avion": "LV-KRS",
        },
        "VU020": {
            "Fecha": "10/10/2024 | 16:00",
            "Origen": "San Fernando del Valle de Catamarca",
            "Destino": "La Rioja",
            "Avion": "LV-LPQ",
        },
        # Día 5 - Viernes
        "VU021": {
            "Fecha": "11/10/2024 | 06:00",
            "Origen": "La Rioja",
            "Destino": "Neuquén",
            "Avion": "LV-ABC",
        },
        "VU022": {
            "Fecha": "11/10/2024 | 09:00",
            "Origen": "Neuquén",
            "Destino": "Viedma (Río Negro)",
            "Avion": "LV-BRD",
        },
        "VU023": {
            "Fecha": "11/10/2024 | 12:00",
            "Origen": "Viedma (Río Negro)",
            "Destino": "Rawson (Chubut)",
            "Avion": "LV-CFT",
        },
        "VU024": {
            "Fecha": "11/10/2024 | 15:00",
            "Origen": "Rawson (Chubut)",
            "Destino": "Río Gallegos (Santa Cruz)",
            "Avion": "LV-DRT",
        },
        "VU025": {
            "Fecha": "11/10/2024 | 18:00",
            "Origen": "Río Gallegos (Santa Cruz)",
            "Destino": "Ushuaia (Tierra del Fuego)",
            "Avion": "LV-EFP",
        },
        # Día 6 - Sábado
        "VU026": {
            "Fecha": "12/10/2024 | 06:00",
            "Origen": "Ushuaia (Tierra del Fuego)",
            "Destino": "Río Gallegos (Santa Cruz)",
            "Avion": "LV-GHT",
        },
        "VU027": {
            "Fecha": "12/10/2024 | 09:00",
            "Origen": "Río Gallegos (Santa Cruz)",
            "Destino": "Rawson (Chubut)",
            "Avion": "LV-HJK",
        },
        "VU028": {
            "Fecha": "12/10/2024 | 12:00",
            "Origen": "Rawson (Chubut)",
            "Destino": "Viedma (Río Negro)",
            "Avion": "LV-JLM",
        },
        "VU029": {
            "Fecha": "12/10/2024 | 14:00",
            "Origen": "Viedma (Río Negro)",
            "Destino": "Neuquén",
            "Avion": "LV-KRS",
        },
        "VU030": {
            "Fecha": "12/10/2024 | 16:00",
            "Origen": "Neuquén",
            "Destino": "Santa Rosa (La Pampa)",
            "Avion": "LV-LPQ",
        },
        # Día 7 - Domingo
        "VU031": {
            "Fecha": "13/10/2024 | 06:00",
            "Origen": "Santa Rosa (La Pampa)",
            "Destino": "La Plata (Buenos Aires)",
            "Avion": "LV-ABC",
        },
        "VU032": {
            "Fecha": "13/10/2024 | 09:00",
            "Origen": "La Plata (Buenos Aires)",
            "Destino": "Ciudad Autónoma de Buenos Aires (CABA)",
            "Avion": "LV-BRD",
        },
    }

    # -------------------------------------------------
    # Bloque de menú
    # ----------------------------------------------------------------------------------------------
    while True:
        opciones = 4
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Pasajes")
            print("[2] Pasajeros")
            print("[3] Vuelos")
            print("---------------------------")
            print("[0] Salir del programa")
            print()

            opcion = input("Seleccione una opción: ")
            if opcion in [
                str(i) for i in range(0, opciones)
            ]:  # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":  # Opción salir del programa
            exit()

        elif opcion == "1":  # SUBMENÚ BOLETOS
            opciones = 4
            while True:
                print()
                print("---------------------------")
                print("MENÚ PASAJES               ")
                print("---------------------------")
                print("[1] Comprar")
                print("[2] Modificar")
                print("[3] Cancelar")
                print("---------------------------")
                print("[0] Volver al MENÚ PRINCIPAL")
                print()

                opcion = input("Seleccione una opción: ")
                if opcion in [
                    str(i) for i in range(0, opciones)
                ]:  # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion == "0":
                exit()

            elif opcion == "1":  # Comprar Pasaje
                modulo_compras.comprarPasaje(pasajeros)

            elif opcion == "2":  # Modificar Pasaje
                print()
                print("Ingrese el número de boleto: ")
                modulo_facu.modificarPasaje()

            elif opcion == "3":
                ...

        elif opcion == "2":  # SUBMENÚ PASAJEROS
            opciones = 3
            while True:
                print()
                print("---------------------------")
                print("MENÚ PASAJEROS             ")
                print("---------------------------")
                print("[1] Listar")
                print("[2] Modificar")
                print("---------------------------")
                print("[0] Volver al MENÚ PRINCIPAL")
                print()

                opcion = input("Seleccione una opción: ")
                if opcion in [
                    str(i) for i in range(0, opciones)
                ]:  # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion == "0":
                exit()
            elif opcion == "1":  # Listar Pasajeros
                print()
                print("Ingrese el número de boleto: ")
                modificado = int(input("INGRESE DNI: "))
                modulo_facu.modificarPasajero(pasajeros, modificado)

            elif opcion == "2":  # Modificar Pasajero
                print()
                modulo_facu.listarPasajeros(pasajeros)

        elif opcion == "3":  # SUBMENÚ VUELOS
            opciones = 3
            while True:
                print()
                print("---------------------------")
                print("MENÚ VUELOS                ")
                print("---------------------------")
                print("[1] Listar")
                print("[2] Modificar")
                print("[3] Eliminar")
                print("---------------------------")
                print("[0] Volver al MENÚ PRINCIPAL")
                print()

                opcion = input("Seleccione una opción: ")
                if opcion in [
                    str(i) for i in range(0, opciones)
                ]:  # Sólo continua si se elije una opcion de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion == "0":
                exit()

            elif opcion == "1":  # Listar Vuelos
                ...
            elif opcion == "2":  # Modificar Vuelo
                ...
            elif opcion == "3":  # Eliminar Vuelo
                ...

        elif opcion == "4":  # Eliminar Pasajero
            print()
            print("Ingrese el número de boleto: ")
            modulo_alvaro.eliminarPasajero(pasajeros)

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
