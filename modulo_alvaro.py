boeing737_800claseEjecutiva = (4, 4)
boeing737_800claseTurista = (28, 6)
airbusA320neoclaseEjecutiva = (3, 4)
airbusA320neoclaseEconomica = (28, 6)


def registrarDatos():
    nombre = "Nombre: "
    apellido = "Apellido: "
    dni = "DNI: "
    verificador = False
    verificadorNombre = False
    verificadorApellido = False
    verificadordni = False
    while verificador == False:
        print("Ingrese sus datos")
        print("-----------------")
        print(f"[1]{nombre}")
        print(f"[2]{apellido}")
        print(f"[3]{dni}")
        print(f"[4]Completar")
        print("-----------------")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            print("Escriba su nombre.")
            escribirNombre = input()
            while escribirNombre == "":
                print("No es valido dejar el espacio en blanco")
                escribirNombre = input("Escribalo nuevamente: ")
            nombre = nombre + escribirNombre
            verificadorNombre == True
        elif opcion == 2:
            print("Escriba su apellido")
            escribirApellido = input()
            while escribirApellido == "":
                print("No es valido dejar espacios en blanco")
                escribirApellido = input("Escribalo nuevamente: ")
            apellido = apellido + escribirApellido
            verificadorApellido = True
        elif opcion == 3:
            print("Escriba su DNI")
            escribirDni = input()
            while escribirDni == "":
                print("No es valido dejar espacion en blanco")
                escribirDni = input("Intentelo nuevamente: ")
            dni = dni + escribirDni
            verificadordni = True
        elif opcion == 4:
            if (
                verificadorApellido == True
                and verificadorNombre == True
                and verificadordni == True
            ):
                verificador == True
            else:
                print("Aun quedan datos por completar")
                opcion = input("Seleccione otra opcion: ")
        else:
            print("Esa opcion no existe")
            opcion = input("INtente nuevamente: ")
    print("Sus datos")
    print("----------------")
    print(f"{nombre}")
    print(f"{apellido}")
    print(f"{dni}")
    print("----------------")


registrarDatos()

# Pasajeros: DNI, nombre, apellido
# Pasajes: Numero de pasaje, numero de asiento, clase de asiento, codigo de equipaje
# Aviones: Modelo, asientos
# Vuelos: Destino, fecha, origen
# Pasajeros: DNI, nombre, apellido
# Pasajes: Numero de pasaje, numero de asiento, clase de asiento, codigo de equipaje
# Aviones: Modelo, asientos
# Vuelos: Destino, fecha, origen
