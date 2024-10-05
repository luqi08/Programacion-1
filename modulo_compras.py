def comprarBoleto():
    while True:
        opciones = 24
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
            ...
    return
