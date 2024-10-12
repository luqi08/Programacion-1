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
import modulo_alvaro, modulo_facu, modulo_luis, modulo_compras, time, datos_precargados


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
    # Bloque de menú
    # ----------------------------------------------------------------------------------------------
    while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Pasajes")
            print("[2] Pasajeros")
            print("[3] Vuelos")
            print("[4] Aviones")
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
                modulo_compras.comprarPasaje(datos_precargados.pasajeros)

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
                modulo_facu.modificarPasajero(datos_precargados.pasajeros, modificado)

            elif opcion == "2":  # Modificar Pasajero
                print()
                modulo_facu.listarPasajeros(datos_precargados.pasajeros)

        elif opcion == "3":  # SUBMENÚ VUELOS
            opciones = 4
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

        elif opcion == "4":  # SUBMENÚ VUELOS
            opciones = 5
            while True:
                print()
                print("---------------------------")
                print("MENÚ AVIONES                ")
                print("---------------------------")
                print("[1] Registrar")
                print("[2] Listar")
                print("[3] Modificar")
                print("[4] Eliminar")
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

            elif opcion == "1":  # Listar Aviones
                ...
            elif opcion == "2":  # Listar Aviones
                ...
            elif opcion == "3":  # Modificar Aviones
                ...
            elif opcion == "4":  # Eliminar Aviones
                ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
