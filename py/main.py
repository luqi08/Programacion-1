"""
-----------------------------------------------------------------------------------------------
Título: SISTEMA DE GESTIÓN DE AEROLÍNEAS
Fecha: 24/9/2024
Autor: Facundo Muruchi - Alvaro Beron - Luis Lin
-----------------------------------------------------------------------------------------------
"""

# ----------------------------------------------------------------------------------------------
# MÓDULOS
# ----------------------------------------------------------------------------------------------
import time
import os
import json

import funciones
import datos_precargados

# ----------------------------------------------------------------------------------------------
# ARCHIVOS
# ----------------------------------------------------------------------------------------------
rutaPasajeros = r"pasajeros.json"
rutaAviones = r"aviones.json"
rutaPasajes = r"pasajes.json"
rutaVuelos = r"vuelos.json"
# ----------------------------------------------------------------------------------------------
# DATOS
# ----------------------------------------------------------------------------------------------
f = open(rutaPasajeros, mode="r", encoding="utf-8")
pasajeros = json.load(f)
f.close

f = open(rutaAviones, mode="r", encoding="utf-8")
aviones = json.load(f)
f.close

f = open(rutaPasajes, mode="r", encoding="utf-8")
pasajes = json.load(f)
f.close

f = open(rutaVuelos, mode="r", encoding="utf-8")
vuelos = json.load(f)
f.close


# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------
def limpiarTerminal() -> None:
    if os.name == "nt":
        os.system("cls")  # Windows
    else:
        os.system("clear")  # Mac/Linux
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
            funciones.comprarPasaje(
                pasajeros,
                pasajes,
                vuelos,
            )
        elif opcion_submenu == "2":  # Listar Pasajes
            funciones.listarPasajes(pasajes, pasajeros)
        elif opcion_submenu == "3":  # Modificar Pasaje
            funciones.modificarPasaje(pasajes, vuelos)
        elif opcion_submenu == "4":  # Eliminar Pasaje
            funciones.eliminarPasaje(pasajes)
    return


def subMenuPasajeros():
    while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("MENÚ PASAJEROS             ")
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
            break  # Volver al ciclo principal

        elif opcion_submenu == "1":  # Registrar Pasajero
            funciones.registrarPasajero(pasajeros)
        elif opcion_submenu == "2":  # Listar Pasajeros
            funciones.listarPasajeros(pasajeros)
        elif opcion_submenu == "3":  # Modificar Pasajero
            funciones.modificarPasajero(pasajeros)
        elif opcion_submenu == "4":  # Eliminar Pasajero
            funciones.eliminarPasajero(pasajeros)
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
            funciones.registrarVuelo(vuelos, aviones)
        elif opcion_submenu == "2":  # Listar Vuelos
            funciones.listarVuelos(datos_precargados.vuelos)
        elif opcion_submenu == "3":  # Modificar Vuelo
            funciones.modificarVuelo(vuelos, aviones)
        elif opcion_submenu == "4":  # Eliminar Vuelo
            funciones.eliminarVuelo(vuelos)
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
            funciones.registrarAviones(aviones)
        elif opcion_submenu == "2":  # Listar Aviones
            funciones.listarAviones(aviones)
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
            limpiarTerminal()
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
            #            funciones.guardarCambios()
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
