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


def subMenuPasajes():
    while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("MENÚ PASAJES               ")
            print("---------------------------")
            print("[1] Comprar")
            print("[2] Listar")
            print("[3] Modificar")
            print("[4] Cancelar")
            print("---------------------------")
            print("[0] Volver al menú principal")
            print()
            opcion_submenu = input("Seleccione una opción: ")
            if opcion_submenu in [str(i) for i in range(0, opciones)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()
        if opcion_submenu == "0":  # Volver al menú principal
            break  # Volver al ciclo principal, no se termina el programa
        elif opcion_submenu == "1":  # Comprar Pasaje
            dni = modulo_compras.comprarPasaje(datos_precargados.pasajeros)
        elif opcion_submenu == "2":  # Listar Pasajes
            modulo_facu.listarPasajes(datos_precargados.pasajes, datos_precargados.pasajeros)
        elif opcion_submenu == "3":  # Modificar Pasaje
            print("Ingrese el número de boleto: ")
            modulo_facu.modificarPasaje(datos_precargados.pasajeros)
        elif opcion_submenu == "4":  # Eliminar Pasaje
            modulo_facu.eliminarPasajero(datos_precargados.pasajeros, datos_precargados.pasajes)
            #modulo_alvaro.eliminarPasaje(datos_precargados.pasajeros)
    return


def subMenuPasajeros():
    while True:
        opciones = 3
        while True:
            print()
            print("---------------------------")
            print("MENÚ PASAJEROS             ")
            print("---------------------------")
            print("[1] Listar")
            print("[2] Modificar")
            print("---------------------------")
            print("[0] Volver al menú principal")
            print()
            opcion_submenu = input("Seleccione una opción: ")
            if opcion_submenu in [str(i) for i in range(0, opciones)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()
        if opcion_submenu == "0":  # Volver al menú principal
            break  # Volver al ciclo principal
        elif opcion_submenu == "1":  # Listar Pasajeros
            modulo_facu.listarPasajeros(datos_precargados.pasajeros)
        elif opcion_submenu == "2":  # Modificar Pasajero
            dni = int(input("INGRESE DNI: "))
            modulo_facu.modificarPasajero(datos_precargados.pasajeros, dni)
    return


def subMenuVuelos():
    while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("MENÚ VUELOS                ")
            print("---------------------------")
            print("[1] Registrar")
            print("[2] Listar")
            print("[3] Modificar")
            print("[4] Eliminar")
            print("---------------------------")
            print("[0] Volver al menú principal")
            print()
            opcion_submenu = input("Seleccione una opción: ")
            if opcion_submenu in [str(i) for i in range(0, opciones)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()
        if opcion_submenu == "0":  # Volver al menú principal
            break
        elif opcion_submenu == "1":  # Registrar Vuelos
            ...
        elif opcion_submenu == "2":  # Listar Vuelos
            modulo_facu.listarVuelos(datos_precargados.vuelos)
        elif opcion_submenu == "3":  # Modificar Vuelo
            ...
        elif opcion_submenu == "4":  # Eliminar Vuelo
            ...
    return


def subMenuAviones():
    while True:
        opciones = 5
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
            print("[0] Volver al menú principal")
            print()
            opcion_submenu = input("Seleccione una opción: ")
            if opcion_submenu in [str(i) for i in range(0, opciones)]:
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()
        if opcion_submenu == "0":  # Volver al menú principal
            break

        elif opcion_submenu == "1":  # Registrar Avión
            ...
        elif opcion_submenu == "2":  # Listar Aviones
            modulo_facu.listarAviones(datos_precargados.aviones)
        elif opcion_submenu == "3":  # Modificar Aviones
            ...
        elif opcion_submenu == "4":  # Eliminar Aviones
            ...
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
            subMenuPasajes()
        elif opcion == "2":  # SUBMENÚ PASAJEROS
            subMenuPasajeros()
        elif opcion == "3":  # SUBMENÚ VUELOS
            subMenuVuelos()
        elif opcion == "4":  # SUBMENÚ AVIONES
            subMenuAviones()
        print("\n\n")


# Punto de entrada al programa
main()
