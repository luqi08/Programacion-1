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
import modulo_alvaro, modulo_facu, modulo_luis


# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------
def comprarBoleto():
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
    aviones = {"boeing737":{"asientos":},"airbusA320":{"asientos":}}
    # -------------------------------------------------
    # Bloque de menú
    # ----------------------------------------------------------------------------------------------
    while True:
        opciones = 3
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Comprar Boleto")
            print("[2] Modificar Boleto")
            print("[3] Cancelar Boleto")
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
            print()
            print("---------------------------")
            print("DESTINO                    ")
            print("---------------------------")
            print("[1] Buenos Aires")
            print("[2] Catamarca")
            print("[3] Chaco")
            print("[4] Chubut")
            print("[5] Ciudad Autónoma de Buenos Aires (CABA)")
            print("[6] Córdoba")
            print("[7] Corrientes")
            print("[8] Entre Ríos")
            print("[9] Formosa")
            print("[10] Jujuy")
            print("[11] La Pampa")
            print("[12] La Rioja")
            print("[13] Mendoza")
            print("[14] Misiones")
            print("[15] Neuquén")
            print("[16] Río Negro")
            print("[17] Salta")
            print("[18] San Juan")
            print("[19] San Luis")
            print("[20] Santa Cruz")
            print("[21] Santa Fe")
            print("[22] Santiago del Estero")
            print("[23] Tierra del Fuego")
            print("[24] Tucumán")
            print("---------------------------")
            print("[0] Salir del programa")
            print()
            comprarBoleto()
            
        elif opcion == "2":  # Opción 2
            print()
            print("Ingrese el número de boleto: ")
            modificarBoleto()

        elif opcion == "3":  # Opción 3
            print()
            print("Ingrese el número de boleto: ")
            cancelarBoleto()

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
