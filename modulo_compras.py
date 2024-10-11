import time, modulo_alvaro, modulo_facu


def comprarPasaje(pasajeros: dict) -> dict:
    """
    elegir destino -> elegir fecha disponible -> elegir asiento disponible -> registrar datos personales
    """
    destino = ""
    while True:
        opciones = 25
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
        print("[0] Volver al Menú Principal")
        print()

        opcion = input("Seleccione un destino: ")
        if opcion in [
            str(i) for i in range(0, opciones)
        ]:  # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == 0:
            break

        elif opcion == 1:
            destino = "Buenos Aires"

        elif opcion == 2:
            destino = "Catamarca"

        elif opcion == 3:
            destino = "Chaco"

        elif opcion == 4:
            destino = "Chubut"

        elif opcion == 5:
            destino = "Ciudad Autónoma de Buenos Aires"

        elif opcion == 6:
            destino = "Córdoba"

        elif opcion == 7:
            destino = "Corrientes"

        elif opcion == 8:
            destino = "Entre Rios"

        elif opcion == 9:
            destino = "Formosa"

        elif opcion == 10:
            destino = "Jujuy"

        elif opcion == 11:
            destino = "La Pampa"

        elif opcion == 12:
            destino = "La Rioja"

        elif opcion == 13:
            destino = "Mendoza"

        elif opcion == 14:
            destino = "Misiones"

        elif opcion == 15:
            destino = "Neuquén"

        elif opcion == 16:
            destino = "Río Negro"

        elif opcion == 17:
            destino = "Salta"

        elif opcion == 18:
            destino = "San Juan"

        elif opcion == 19:
            destino = "San Luis"

        elif opcion == 20:
            destino = "Santa Cruz"

        elif opcion == 21:
            destino = "Santa Fe"

        elif opcion == 22:
            destino = "Santiago del Estero"

        elif opcion == 23:
            destino = "Tierra del Fuego"

        elif opcion == 24:
            destino = "Tucumán"

        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()
    modulo_alvaro.registrarDatos(pasajeros)

    return


if __name__ == "__main__":  # Para no ejecutar la función al importar el módulo
    comprarBoleto()
