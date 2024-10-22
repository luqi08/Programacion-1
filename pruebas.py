def registrarAviones(aviones):
    """
    Esta función sirve para registrar aviones adquiridos dentro del programa. Funciona bastante parecido a crear pasajes
    solo que se reemplazan los datos del pasajero con los del avión.
    """

    modelo = ""
    matricula = ""
    primeraClase = ""
    claseEconomica = ""
    while True:
        print("-------------------------------------")
        print("Ingrese los datos del avion adquirido")
        print("-------------------------------------")
        print(f"[1]Modelo: {modelo}")
        print(f"[2]Matricula: {matricula}")
        print(f"[3]Asientos en primera clase: {primeraClase}")
        print(f"[4]Asientos en clase economica: {claseEconomica}")
        print("[5]Reestablecer todo a sus valores predeterminados")
        print("[6]Completar")
        print("-------------------------------------")
        print(f"[0]Volver al menu anterior")
        print("-------------------------------------")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            print("Escriba el modelo del avion.")
            modelo = input()
            print("Modelo ingresado.")
        elif opcion == "2":
            print("Escriba la matricula del avion")
            matricula = input()
            while matricula in aviones.keys():
                print("Dicha matricula ya ha sido ingresada.")
                matricula = input("Intentelo nuevamente: ")
            print("Matricula ingresada")
        elif opcion == "3":
            print("Indique con cuantos asientos de primera clase contara el avion")
            primeraClase = int(input())
            columnas = int(input("Indique la cantidad de columnas: "))
            filas = int(input("Indique la cantidad de filas: "))
            while (columnas * filas) != int(primeraClase):
                print(
                    "ERROR! La cantidad de asientos no coincide con la propuesta anteriormente."
                )
                print("Intentelo nuevamente")
                primeraClase = int(input("Indique los asientos de primera clase: "))
                columnas = int(input("Indique la cantidad de columnas: "))
                filas = int(input("Indique la cantidad de filas: "))
            matriz = []

            for asiento in range(filas):
                matriz.append([])
                for asientos in range(columnas):
                    matriz[asiento].append(0)
        elif opcion == "4":
            print("Indique con cuantos asientos de primera clase contara el avion")
            claseEconomica = int(input())
            columnas = int(input("Indique la cantidad de columnas: "))
            filas = int(input("Indique la cantidad de filas: "))
            while (columnas * filas) != int(claseEconomica):
                print(
                    "ERROR! La cantidad de asientos no coincide con la propuesta anteriormente."
                )
                print("Intentelo nuevamente")
                claseEconomica = int(input("Indique los asientos de primera clase: "))
                columnas = int(input("Indique la cantidad de columnas: "))
                filas = int(input("Indique la cantidad de filas: "))
            matriz = []

            for asiento in range(filas):
                matriz.append([])
                for asientos in range(columnas):
                    matriz[asiento].append(0)

        elif opcion == "4":
            modelo = ""
            matricula = ""
            primeraClase = ""
            claseEconomica = ""

        elif opcion == "5":
            aviones[matricula] = {
                "modelo": modelo,
                "asientos": {"primera": primeraClase, "econocmica": claseEconomica},
            }

        else:
            print("Esa opcion no existe")
