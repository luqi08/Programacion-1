def registrarAviones(aviones: dict) -> int:
    """
    Registra un nuevo pasajero solicitando su nombre, apellido y DNI, asegurando que no se
    introduzcan caracteres numéricos en los nombres y que el DNI sea numérico. Los datos
    ingresados son almacenados en el diccionario de pasajeros.

    Args:
    - pasajeros (dict): Diccionario donde se almacenan los datos de los pasajeros.

    Returns:
    - dni (int): Numero dni para identificar al pasajero.
    """
    modelo = ""
    matricula = ""
    primeraClase = ""
    claseEconomica = ""
    verificador = False
    while verificador == False:
        print("Ingrese sus datos")
        print("-----------------")
        print(f"[1]Modelo: {modelo}")
        print(f"[2]Matricula: {matricula}")
        print(f"[3]Asientos de primera clase: {primeraClase}")
        print(f"[4]Asientos de clase economica: {claseEconomica}")
        print("[5]Realizar cambios (Reestablecera todo a su estado predeterminado)")
        print("[6]Completar")
        print("-----------------")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            print("Escriba el nombre del modelo.")
            escribirModelo = input().capitalize()
            while escribirModelo == "":
                print("No es valido dejar el espacio en blanco")
                escribirModelo = input("Escribalo nuevamente: ")
            modelo = escribirModelo
        elif opcion == "2":
            print("Escriba su apellido")
            escribirMatricula = input().upper()
            while escribirMatricula == "":
                print("No es valido dejar el espacio en blanco")
                escribirMatricula = input("Escribalo nuevamente: ")
            matricula = escribirMatricula
        elif opcion == "3":
            print("Escriba los asientos totales de la primera clase")
            escribirPrimeraClase = input()
            while escribirPrimeraClase == "":
                print("No es valido dejar espacion en blanco ni involucrar letras")
                escribirPrimeraClase = input("Intentelo nuevamente: ")
            primeraClase = escribirPrimeraClase
            print("Ahora coloque la cantidad de asientos por fila.")
            porFilaPC = int(input())
            print("Ahora coloque la cantidad de asientos por columna")
            porColumnaPC = int(input())
            while (porFilaPC * porColumnaPC) != primeraClase:
                print("ERROR!")
                print("La cantidad asientos debe coincidir con la dicha anteriormente.")
                print("Coloque la cantidad de asientos por fila.")
                porFilaPC = int(input())
                print("Coloque la cantidad de asientos por columna")
                porColumnaPC = int(input())
        elif opcion == "4":
            print("Escriba los asientos totales de la clase economica.")
            escribirClaseEconomica = input()
            while escribirClaseEconomica == "":
                print("No es valido dejar espacios en blanco")
                print("Intentelo nuevamente")
                escribirClaseEconomica = input()
            claseEconomica = escribirClaseEconomica
            print("Ahora escriba los asientos por fila")
            porFilaCE = int(input())
            print("Ahora escriba la cantidad de asientos por columna")
            porColumnaCE = int(input())
            while (porFilaCE * porColumnaCE) == claseEconomica:
                print(
                    "Los datos otorgados son incorrectos y la cantidad de asientos por fila y columna debe coincidir"
                )
                print("Intentelo nuevamente")
                print("Ahora escriba los asientos por fila")
                porFilaCE = int(input())
                print("Ahora escriba la cantidad de asientos por columna")
                porColumnaCE = int(input())
        elif opcion == "5":
            modelo = ""
            apellido = ""
            dni = ""
        elif opcion == "6":
            if (
                modelo == ""
                or matricula == ""
                or claseEconomica == ""
                or primeraClase == ""
            ):
                print("Aun quedan datos por completar")
            else:
                break
        else:
            print("Esa opcion no existe")
    print("Los datos")
    print("----------------")
    print(f"Modelo: {modelo}")
    print(f"Matricula: {matricula}")
    print(f"Asientos en primera clase: {primeraClase}")
    print(f"Asientos en clase economica: {claseEconomica}")
    print("----------------")
    aviones[matricula] = {
        "modelo": modelo,
        "asientos en primera clase": int(primeraClase),
        "asientos en clase economica": int(claseEconomica),
    }
    print("Avion registrado")
    return (porFilaPC, porColumnaPC, porFilaCE, porColumnaCE)
