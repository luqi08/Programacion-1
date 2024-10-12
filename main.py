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
            if opcion in [str(i) for i in range(0, opciones)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":  # Opción salir del programa
            print("Saliendo del programa...")
            break  # Salir del ciclo principal

        elif opcion == "1":  # SUBMENÚ PASAJES
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

                opcion_submenu = input("Seleccione una opción: ")
                if opcion_submenu in [str(i) for i in range(0, 4)]:
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion_submenu == "0":  # Volver al menú principal
                continue  # Volver al ciclo principal, no se termina el programa

            elif opcion_submenu == "1":  # Comprar Pasaje
                modulo_compras.comprarPasaje(datos_precargados.pasajeros)

            elif opcion_submenu == "2":  # Modificar Pasaje
                print("Ingrese el número de boleto: ")
                modulo_facu.modificarPasaje(datos_precargados.pasajes)

            elif opcion_submenu == "3":
                modulo_alvaro.eliminarPasajero(datos_precargados.pasajeros)

        elif opcion == "2":  # SUBMENÚ PASAJEROS
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

                opcion_submenu = input("Seleccione una opción: ")
                if opcion_submenu in [str(i) for i in range(0, 3)]:
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion_submenu == "0":  # Volver al menú principal
                continue  # Volver al ciclo principal

            elif opcion_submenu == "1":  # Listar Pasajeros
                modulo_facu.listarPasajeros(datos_precargados.pasajeros)

            elif opcion_submenu == "2":  # Modificar Pasajero
                modificado = int(input("INGRESE DNI: "))
                modulo_facu.modificarPasajero(datos_precargados.pasajeros, modificado)

        elif opcion == "3":  # SUBMENÚ VUELOS
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

                opcion_submenu = input("Seleccione una opción: ")
                if opcion_submenu in [str(i) for i in range(0, 4)]:
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion_submenu == "0":  # Volver al menú principal
                continue

            elif opcion_submenu == "1":  # Listar Vuelos
                ...
            elif opcion_submenu == "2":  # Modificar Vuelo
                ...
            elif opcion_submenu == "3":  # Eliminar Vuelo
                ...

        elif opcion == "4":  # SUBMENÚ AVIONES
            while True:
                print()
                print("---------------------------")
                print("MENÚ AVIONES               ")
                print("---------------------------")
                print("[1] Registrar")
                print("[2] Listar")
                print("[3] Modificar")
                print("[4] Eliminar")
                print("---------------------------")
                print("[0] Volver al MENÚ PRINCIPAL")
                print()

                opcion_submenu = input("Seleccione una opción: ")
                if opcion_submenu in [str(i) for i in range(0, 5)]:
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
            print()

            if opcion_submenu == "0":  # Volver al menú principal
                continue

            elif opcion_submenu == "1":  # Registrar Avión
                ...
            elif opcion_submenu == "2":  # Listar Aviones
                ...
            elif opcion_submenu == "3":  # Modificar Aviones
                ...
            elif opcion_submenu == "4":  # Eliminar Aviones
                ...

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()
