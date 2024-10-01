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
    aviones = {"boeing737":{},"airbusA320":{}}
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
            print("[2] Cancelar Boleto")
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
            comprarBoleto()
        elif opcion == "2":  # Opción 2
            cancelarBoleto()

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
