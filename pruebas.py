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
            while escribirNombre == "":
                print("No es valido dejar el espacio en blanco")
                escribirNombre = input("Escribalo nuevamente: ").capitalize()
            nombre = escribirNombre
        elif opcion == "2":
            print("Escriba su apellido")
            escribirMatricula = input()
            while escribirMatricula == "":
                print("No es valido dejar el espacio en blanco")
                escribirMatricula = input("Escribalo nuevamente: ").capitalize()
            matricula = escribirMatricula
        elif opcion == "3":
            print("Escriba su DNI")
            escribirDni = input()
            while escribirDni == "" or escribirDni.isnumeric() == False:
                print("No es valido dejar espacion en blanco ni involucrar letras")
                escribirDni = input("Intentelo nuevamente: ")
            dni = int(escribirDni)
        elif opcion == "4":
            nombre = ""
            apellido = ""
            dni = ""
        elif opcion == "5":
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
    aviones[matricula] = {"nombre": nombre, "apellido": apellido}
    print("Pasajero registrado")
    return
