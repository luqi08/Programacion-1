def comprarBoleto():
    destino = ""
    while True:
        destinos = 24
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
            str(i) for i in range(0, destinos)
        ]:  # Sólo continua si se elije una opcion de menú válida
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == 0:
            break

        elif opcion == 1:
            ...
        elif opcion == 2:
            ...
        elif opcion == 3:
            ...
        elif opcion == 4:
            ...
        elif opcion == 5:
            ...
        elif opcion == 6:
            ...
        elif opcion == 7:
            ...
        elif opcion == 8:
            ...
        elif opcion == 9:
            ...
        elif opcion == 10:
            ...
        elif opcion == 11:
            ...
        elif opcion == 12:
            ...
        elif opcion == 13:
            ...
        elif opcion == 14:
            ...
        elif opcion == 15:
            ...
        elif opcion == 16:
            ...
        elif opcion == 17:
            ...
        elif opcion == 18:
            ...
        elif opcion == 19:
            ...
        elif opcion == 20:
            ...
        elif opcion == 21:
            ...
        elif opcion == 22:
            ...
        elif opcion == 23:
            ...
        elif opcion == 24:
            ...

    return

if __name__ == "__main__": # Para no ejecutar la función al importar el módulo
    comprarBoleto()