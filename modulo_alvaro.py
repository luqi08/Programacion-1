boeing737_800claseEjecutiva = (4, 4)
boeing737_800claseTurista = (28, 6)
airbusA320neoclaseEjecutiva = (3, 4)
airbusA320neoclaseEconomica = (28, 6)


def registrarDatos(pasajeros):
    """
    Registra un nuevo pasajero solicitando su nombre, apellido y DNI, asegurando que no se
    introduzcan caracteres numéricos en los nombres y que el DNI sea numérico. Los datos
    ingresados son almacenados en el diccionario de pasajeros.

    Args:
    - pasajeros (dict): Diccionario donde se almacenan los datos de los pasajeros.
    """
    prohibidos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    nombre = ""
    apellido = ""
    dni = ""
    verificador = False
    verificadorNombre = False
    while verificador == False:
        print("Ingrese sus datos")
        print("-----------------")
        print(f"[1]Nombre: {nombre}")
        print(f"[2]Apellido: {apellido}")
        print(f"[3]DNI: {dni}")
        print("[4]Realizar cambios (Reestablecera todo a su estado predeterminado)")
        print("[5]Completar")
        print("-----------------")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            print("Escriba su nombre.")
            escribirNombre = input()
            for letra in escribirNombre:
                if letra in prohibidos:
                    bandera = False
                    break
                else:
                    bandera = True
            while escribirNombre == "" or bandera == False:
                print("No es valido dejar el espacio en blanco ni involucrar numeros")
                escribirNombre = input("Escribalo nuevamente: ")
                for letra in escribirNombre:
                    if letra in prohibidos:
                        bandera = False
                        break
                    else:
                        bandera = True
            nombre = escribirNombre
            verificadorNombre == True
        elif opcion == "2":
            print("Escriba su apellido")
            escribirApellido = input()
            for letra in escribirApellido:
                if letra in prohibidos:
                    bandera = False
                    break
                else:
                    bandera = True
            while escribirApellido == "" or bandera == False:
                print("No es valido dejar el espacio en blanco ni involucrar numeros")
                escribirApellido = input("Escribalo nuevamente: ")
                for letra in escribirApellido:
                    if letra in prohibidos:
                        bandera = False
                        break
                    else:
                        bandera = True
            apellido = escribirApellido
        elif opcion == "3":
            print("Escriba su DNI")
            escribirDni = input()
            while escribirDni == "" or escribirDni.isnumeric() == False:
                print("No es valido dejar espacion en blanco ni involucrar letras")
                escribirDni = input("Intentelo nuevamente: ")
            dni = escribirDni
        elif opcion == "4":
            nombre = ""
            apellido = ""
            dni = ""
            verificadorNombre = False
        elif opcion == "5":
            if nombre == "" or apellido == "" or dni == "":
                print("Aun quedan datos por completar")
            else:
                break
        else:
            print("Esa opcion no existe")
    print("Sus datos")
    print("----------------")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"DNI: {dni}")
    print("----------------")
    pasajeros[dni] = {"nombre": nombre, "apellido": apellido}
    print("Pasajero registrado")
    return


def eliminarPasaje(pasajeros):
    """
    Elimina la información de un pasajero del sistema mediante su DNI, verificando
    previamente si el pasajero existe en el diccionario de pasajeros.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    """
    eliminar = False
    while eliminar == False:
        print("Desea eliminar el pasaje junto a la informacion del pasajero?")
        print("--------------------")
        print("[1] Eliminar pasajero")
        print("[2] Volver al menu anterior")
        print("--------------------")
        opcion = input("Seleccione una opcion")
        if opcion == "1":
            verificador = False
            print("Coloque el DNI del pasajero a eliminar")
            dni = int(input("DNI: "))
            print(
                "Aun esta seguro de que desea eliminar a dicho pasajero del diccionario?"
            )
            print("------------------")
            print("[1] Eliminar pasajero")
            print("[2] Volver al menu anterior")
            print("------------------")
            opcion = input()
            if opcion == "1":
                del pasajeros[int(dni)]
                print(f"El pasajero {dni} ha sido eliminado")
        elif opcion == "2":
            break
        else:
            print("Esa opcion no existe")
    return


# Pasajeros: DNI, nombre, apellido
# Pasajes: Numero de pasaje, numero de asiento, clase de asiento, codigo de equipaje
# Aviones: Modelo, asientos
# Vuelos: Destino, fecha, origen
# Pasajeros: DNI, nombre, apellido
# Pasajes: Numero de pasaje, numero de asiento, clase de asiento, codigo de equipaje
# Aviones: Modelo, asientos
# Vuelos: Destino, fecha, origen
