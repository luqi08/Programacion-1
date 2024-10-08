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
import modulo_alvaro, modulo_facu, modulo_luis, modulo_compras


# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------
def cancelarBoleto():
    return


# ----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
# ----------------------------------------------------------------------------------------------
def main():
    # -------------------------------------------------
    # Inicialización de variables
    # ----------------------------------------------------------------------------------------------
    aviones = {
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

    pasajeros = {
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

    # -------------------------------------------------
    # Bloque de menú
    # ----------------------------------------------------------------------------------------------
    while True:
        opciones = 6
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Comprar Boleto")
            print("[2] Eliminar Pasajero")
            print("[3] Cancelar Boleto")
            print("[4] Modificar Pasajero")
            print("[5] Listar pasajeros")
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
            exit()  # También puede ser sys.exit() para lo cual hay que importar el módulo sys

        elif opcion == "1":  # Opción 1
            modulo_compras.comprarBoleto()
            modulo_alvaro.registrarDatos(pasajeros)

        elif opcion == "2":  # Opción 2
            print()
            print("Ingrese el número de boleto: ")
            modulo_alvaro.eliminarPasajero(pasajeros)

        elif opcion == "3":  # Opción 3
            print()
            print("Ingrese el número de boleto: ")
            modulo_facu.modificarPasaje()

        elif opcion == "4":  # Opción 3
            print()
            print("Ingrese el número de boleto: ")
            modificado = int(input('INGRESE DNI: '))
            modulo_facu.modificarPasajero(pasajeros, modificado)

        elif opcion == "5":  # Opción 3
            print()
            modulo_facu.listarPasajeros(pasajeros)

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
