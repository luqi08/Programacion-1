boeing737_800claseEjecutiva = (4, 4)
boeing737_800claseTurista = (28, 6)
airbusA320neoclaseEjecutiva = (3, 4)
airbusA320neoclaseEconomica = (28, 6)


def registrarDatos():
    nombre = ""
    apellido = ""
    dni = ""
    verificador = False
    verificadorNombre = False
    verificadorApellido = False
    verificadordni = False
    while verificador == False:
        print("Ingrese sus datos")
        print("-----------------")
        print(f"[1]Nombre: {nombre}")
        print(f"[2]Apellido: {apellido}")
        print(f"[3]DNI: {dni}")
        print("[4]Realizar cambios (Reestablecera todo a su estado predeterminado)")
        print("[5]Completar")
        print("-----------------")
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            print("Escriba su nombre.")
            while True:
                escribirNombre = input()
                if len(escribirNombre) == 0:
                    print('No puede dejarlo en blanco')
                elif escribirNombre.isdigit():
                    print('El nombre no deben ser numeros')
                else:
                    break
            nombre = escribirNombre
            verificadorNombre == True
        elif opcion == 2:
            print("Escriba su apellido")
            escribirApellido = input()
            while escribirApellido == "":
                print("No es valido dejar espacios en blanco")
                escribirApellido = input("Escribalo nuevamente: ")
            apellido = escribirApellido
            verificadorApellido = True
        elif opcion == 3:
            print("Escriba su DNI")
            while True:
                escribirDni = input()
                if len(escribirDni) == 0:
                    print('No puede dejarlo en blanco')
                elif escribirDni.isnumeric() == False:
                    print('El DNI deben ser numeros')
                else:
                    break
            dni = escribirDni
            verificadordni = True
        elif opcion == 4:
            nombre = ""
            apellido = ""
            dni = ""
            verificadorApellido = False
            verificadorNombre = False
            verificadordni = False
        elif opcion == 5:
            verificador = verificadorApellido + verificadordni + verificadorNombre
            if verificador == 3:
                break
            else:
                print("Aun quedan datos por completar")
        else:
            print("Esa opcion no existe")
    print("Sus datos")
    print("----------------")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"DNI: {dni}")
    print("----------------")


if __name__ == "__main__":  # Para no ejecutar la función al importar el módulo
    registrarDatos()

# Pasajeros: DNI, nombre, apellido
# Pasajes: Numero de pasaje, numero de asiento, clase de asiento, codigo de equipaje
# Aviones: Modelo, asientos
# Vuelos: Destino, fecha, origen
# Pasajeros: DNI, nombre, apellido
# Pasajes: Numero de pasaje, numero de asiento, clase de asiento, codigo de equipaje
# Aviones: Modelo, asientos
# Vuelos: Destino, fecha, origen
