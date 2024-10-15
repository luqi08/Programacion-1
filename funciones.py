# ----------------------------------------------------------------------------------------------
# FUNCIONES
# ----------------------------------------------------------------------------------------------
def crearMatriz(filas: int, columnas: int, relleno) -> list[list]:
    """
    Crea una matriz con las dimensiones especificadas y la llena con el valor indicado.

    Args:
    - filas (int): Número de filas de la matriz.
    - columnas (int): Número de columnas de la matriz.
    - relleno (any): Valor con el que se llenará la matriz.

    Returns:
    - list: Matriz creada con las dimensiones y valores especificados.
    """
    return [[relleno] * columnas for fila in range(filas)]


def letraNumero(letra: str) -> int:
    """
    Convierte una letra en su correspondiente número para indexación de matriz.

    Args:
    - letra (str): Letra del abecedario ('A'-'F').

    Returns:
    - int: Número correspondiente (0-5) para 'A'-'F'.
    """
    if letra == "A":
        letra = 0
    elif letra == "B":
        letra = 1
    elif letra == "C":
        letra = 2
    elif letra == "D":
        letra = 3
    elif letra == "E":
        letra = 4
    elif letra == "F":
        letra = 5
    return letra


def mostrarMatriz(matriz: list[list], pasaje: dict, codigo: str) -> None:
    """
    Muestra visualmente la disposición de asientos en una matriz, con indicación de pasillo.

    Args:
    - matriz (list): Matriz que representa el avión con asientos ocupados.
    - pasaje (dict): Información sobre el pasaje y asiento del pasajero.
    - codigo (str): Código identificador del pasaje.
    """
    longitud = len(matriz[0])
    ancho_columna = 2
    filas_totales = len(matriz)
    medio = filas_totales // 2

    if esEjecutiva(pasaje, codigo):
        print("  " + " ".join(f"{i:>{ancho_columna}}" for i in range(1, longitud + 1)))
    else:
        print("  " + " ".join(f"{i:>{ancho_columna}}" for i in range(5, longitud + 5)))

    for indice, fila in enumerate(matriz):
        letra = chr(65 + indice)  # 65 es el código ASCII de 'A'
        print(f"{letra} " + " ".join(f"{el:>{ancho_columna}}" for el in fila))
        if indice == medio - 1:
            print("PASILLO".center(longitud * 3 + 1, "="))
    print("PUNTA DEL AVION A LA IZQUIERDA - COLA DEL AVION A LA DERECHA")
    return

    # def cambiarAsiento(codigoPasaje, matriz):
    """
    Permite cambiar el asiento de un pasajero y actualiza la matriz de asientos ocupados.

    Args:
    - codigoPasaje (str): Código identificador del pasaje.
    - matriz (list): Matriz que representa el avión con asientos ocupados.
    """
    longitud = len(matriz[0])
    listaLetras = []
    for indice, fila in enumerate(matriz):
        letra = chr(65 + indice)
        listaLetras.append(letra)
    while True:
        filaAsiento = input("SELECCIONE LETRA (A,B,C,ETC.): ")
        if filaAsiento.capitalize() not in listaLetras:
            print(f"{filaAsiento} NO ESTÁ EN EL RANGO")
        else:
            break
    while True:
        filaColumna = int(input("SELECCIONE NUMERO (1,2,3,ETC.): "))
        if filaColumna < 1 or filaColumna > longitud:
            print(f"{filaColumna} NO ESTÁ EN EL RANGO")
        else:
            break
    pasajes[codigoPasaje]["asiento"] = filaAsiento.capitalize() + str(filaColumna)
    filaAsiento = letraNumero(filaAsiento.capitalize())
    matriz[filaAsiento][filaColumna - 1] = 1
    return


def esEjecutiva(pasajes: dict, codigo: str) -> bool:
    """
    Verifica si un asiento pertenece a la clase ejecutiva o no.

    Args:
    - pasajes (dict): Información sobre los pasajes y asientos ocupados.
    - codigo (str): Código identificador del pasaje.

    Returns:
    - bool: True si el asiento es ejecutivo, False si no lo es.
    """
    asiento = pasajes[codigo]["asiento"]
    numero_asiento = int(asiento[1:])
    if numero_asiento < 5:
        return True
    else:
        return False


# ----------------------------------------------------------------------------------------------
# PASAJES
# ----------------------------------------------------------------------------------------------
def comprarPasaje(pasajeros: dict, pasajes: dict, vuelos: dict) -> dict:
    """
    Permite seleccionar un destino, elegir un vuelo disponible para ese destino,
    seleccionar una clase y asiento, y registrar los datos del pasajero para crear un pasaje.

    Args:
    - pasajeros (dict): Información sobre los pasajeros.
    - pasajes (dict): Información sobre los pasajes y asientos ocupados.
    - vuelos (dict): Información sobre los vuelos.
    """
    destinos = {
        "1": "Buenos Aires",
        "2": "Catamarca",
        "3": "Chaco",
        "4": "Chubut",
        "5": "Ciudad Autónoma de Buenos Aires",
        "6": "Córdoba",
        "7": "Corrientes",
        "8": "Entre Ríos",
        "9": "Formosa",
        "10": "Jujuy",
        "11": "La Pampa",
        "12": "La Rioja",
        "13": "Mendoza",
        "14": "Misiones",
        "15": "Neuquén",
        "16": "Río Negro",
        "17": "Salta",
        "18": "San Juan",
        "19": "San Luis",
        "20": "Santa Cruz",
        "21": "Santa Fe",
        "22": "Santiago del Estero",
        "23": "Tierra del Fuego",
        "24": "Tucumán",
    }

    # Seleccionar destino
    while True:
        print("---------------------------")
        print("DESTINOS DISPONIBLES")
        print("---------------------------")
        for key, value in destinos.items():
            print(f"[{key}] {value}")
        print("[0] Volver al Menú Principal")
        print()

        opcion_destino = input("Seleccione un destino: ")
        if opcion_destino == "0":
            return  # Volver al menú principal
        elif opcion_destino in destinos:
            destino = destinos[opcion_destino]
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    # Filtrar vuelos disponibles para el destino seleccionado
    vuelos_destino = {
        key: vuelo for key, vuelo in vuelos.items() if vuelo["Destino"] == destino
    }

    if not vuelos_destino:
        print(f"No hay vuelos disponibles para {destino}.")
        return

    # Seleccionar vuelo
    print("\nVuelos disponibles para", destino)
    vuelos_lista = list(
        vuelos_destino.items()
    )  # Convertimos el diccionario en una lista de tuplas

    for idx, (vuelo_id, vuelo_info) in enumerate(vuelos_lista, start=1):
        print(f"[{idx}] {vuelo_info['Fecha']} | Origen: {vuelo_info['Origen']}")

    while True:
        seleccion = input(
            "Seleccione el número del vuelo: "
        )  # Pedimos el número del vuelo

        if seleccion.isdigit():  # Verificamos que la entrada sea un número
            seleccion = int(seleccion)

            if (
                1 <= seleccion <= len(vuelos_lista)
            ):  # Verificamos que el número esté en el rango válido
                vuelo_seleccionado = vuelos_lista[seleccion - 1][
                    0
                ]  # Obtenemos el código del vuelo
                break
            else:
                input("Selección inválida. Presione ENTER para volver a seleccionar.")
        else:
            input("Entrada inválida. Presione ENTER para volver a intentar.")

    # Selección de clase
    while True:
        clase = input("Seleccione la clase del pasaje ([1] Primera, [2] Económica): ")
        if clase == "1":
            clase_seleccionada = "primera"
            break
        elif clase == "2":
            clase_seleccionada = "economica"
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    # Asignación de asiento (simplificado para este ejemplo)
    asiento = input("Seleccione su asiento (Ej: A1, B2): ").upper()

    # Generar nuevo ID de pasaje
    nuevo_id = f"PA{str(len(pasajes) + 1).zfill(3)}"

    # Registrar datos del pasajero
    dni = registrarDatos(pasajeros)

    # Crear el nuevo pasaje
    pasajes[nuevo_id] = {
        "dni": dni,
        "vuelo": vuelo_seleccionado,
        "clase": clase_seleccionada,
        "asiento": asiento,
    }

    print(f"Pasaje registrado con éxito. ID del pasaje: {nuevo_id}")
    return pasajes


def registrarDatos(pasajeros: dict) -> int:
    """
    Registra un nuevo pasajero solicitando su nombre, apellido y DNI, asegurando que no se
    introduzcan caracteres numéricos en los nombres y que el DNI sea numérico. Los datos
    ingresados son almacenados en el diccionario de pasajeros.

    Args:
    - pasajeros (dict): Diccionario donde se almacenan los datos de los pasajeros.

    Returns:
    - dni (int): Numero dni para identificar al pasajero.
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
            escribirNombre = input().capitalize()
            for letra in escribirNombre:
                if letra in prohibidos:
                    bandera = False
                    break
                else:
                    bandera = True
            while escribirNombre == "" or bandera == False:
                print("No es valido dejar el espacio en blanco ni involucrar numeros")
                escribirNombre = input("Escribalo nuevamente: ").capitalize()
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
            escribirApellido = input().capitalize()
            for letra in escribirApellido:
                if letra in prohibidos:
                    bandera = False
                    break
                else:
                    bandera = True
            while escribirApellido == "" or bandera == False:
                print("No es valido dejar el espacio en blanco ni involucrar numeros")
                escribirApellido = input("Escribalo nuevamente: ").capitalize()
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
            dni = int(escribirDni)
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
    return dni


def listarPasajes(pasajes, pasajeros):
    """
    Lista todos los pasajes registrados junto con sus datos

    Args:
    - pasajes (dict): Diccionario que contiene la información de los pasajes.
    """
    for nPasaje, datos in pasajes.items():
        nombre = nombrePasajero(pasajeros, datos["dni"])
        print(
            f"CÓDIGO: {nPasaje},  PASAJERO: {datos['dni']} {nombre},  VUELO: {datos['vuelo']},  CLASE: {datos['clase'].capitalize()},  ASIENTO: {datos['asiento']}"
        )
    return


def nombrePasajero(pasajeros: dict, dni: int) -> str:
    """
    Obtiene el nombre completo de un pasajero a partir de su DNI.

    Esta función busca el pasajero en el diccionario de pasajeros utilizando el DNI
    como clave y devuelve una cadena con el nombre y apellido concatenados.

    Args:
    pasajeros (dict): Un diccionario que contiene la información de los pasajeros.
    dni (int): El DNI del pasajero que se desea buscar.

    Retorna:
    str: El nombre completo del pasajero en formato 'Nombre Apellido' si el DNI existe en el diccionario.

    None: Si el DNI no se encuentra en el diccionario de pasajeros.
    """
    if dni in pasajeros:
        nombre = f"{pasajeros[dni]['nombre']} {pasajeros[dni]['apellido']}"
        return nombre

        #   def modificarPasaje(pasajes):
        """
        Permite modificar un pasaje existente mediante su código, ya sea cambiando el asiento
        dentro de la misma clase o cambiando de clase. Muestra detalles del pasaje actual y
        solicita acciones al usuario.

        Args:
        - pasajes (dict): Diccionario que contiene la información de todos los pasajes.
        """
        while True:
            codigoPasaje = int(input("INGRESE EL CODIGO DEL PASAJE O [2] PARA SALIR: "))
            if codigoPasaje == 2:
                exit()
            elif codigoPasaje not in pasajes:
                print(f"SU PASAJE {codigoPasaje} NO ESTA REGISTRADO. REINTENTE...")
            else:
                print("--------------------------")
                mostrarPasaje(codigoPasaje)
                print("--------------------------")
                while True:
                    print("[1] CAMBIAR ASIENTO DENTRO DE MISMA CLASE")
                    print("[2] CAMBIAR CLASE")
                    print("[3] SALIR")
                    opcion = int(input("SELECCIONE UNA OPCION: "))
                    if opcion == 1:
                        print()
                        print(
                            f"ASIENTO ACTUAL: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}"
                        )
                        if esEjecutiva(pasajes, codigoPasaje):
                            mostrarMatriz(matrizEjecutiva, pasajes, codigoPasaje)
                            cambiarAsiento(codigoPasaje, matrizEjecutiva)
                        else:
                            mostrarMatriz(matrizEconomica, pasajes, codigoPasaje)
                            cambiarAsiento(codigoPasaje, matrizEconomica)
                        print()
                        print(
                            f"NUEVO ASIENTO: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}"
                        )
                        break
                    elif opcion == 2:
                        while True:
                            print("[1] ECONÓMICA")
                            print("[2] EJECUTIVA")
                            opcion = int(input("SELECCIONE UNA OPCION: "))
                            if opcion == 1:
                                ...
                            elif opcion == 2:
                                ...
                            else:
                                print("INGRESE UN VALOR EN EL RANGO")
                    elif opcion == 3:
                        exit()
                    else:
                        print("INGRESE UN VALOR EN EL RANGO")
                break


def eliminarPasaje(dni: int, pasajes: dict) -> None:
    """
    Elimina el pasaje asociado a un pasajero del diccionario de pasajes.

    Args:
    - dni (int): El DNI del pasajero cuyo pasaje será eliminado.
    - pasajes (dict): Diccionario que contiene la información de los pasajes.
    """
    for codigo, datos in list(pasajes.items()):
        if datos["dni"] == dni:
            del pasajes[codigo]
            print(f"El pasaje {codigo} del pasajero con DNI {dni} ha sido eliminado.")
            return


# ----------------------------------------------------------------------------------------------
# PASAJEROS
# ----------------------------------------------------------------------------------------------
def listarPasajeros(pasajeros: dict) -> None:
    """
    Lista todos los pasajeros registrados junto con su DNI y nombre completo.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    """
    for dni, datos in pasajeros.items():
        print(f"DNI: {dni}  PASAJERO: {datos['nombre']} {datos['apellido']}")
    return


def modificarPasajero(pasajeros: dict) -> None:
    """
    Permite modificar los datos de un pasajero identificado por su DNI.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    - dni (int): DNI del pasajero que se desea modificar.
    """
    prohibidos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    while True:
        dni = input("Ingrese DNI o [0] Para volver al Menú Anterior: ")
        if dni.isnumeric() == True:  # Verificar ingreso válido
            dni = int(dni)
            if dni == 0:
                return
            elif dni != 0 and dni not in pasajeros:  # Verificar existencia DNI
                print()
                print(f"El DNI {dni} no se encuentra registrado")
                print()
            else:
                break
        else:
            print("Ingreso Inválido")

    copiaNombre = pasajeros[dni]["nombre"]
    copiaApellido = pasajeros[dni]["apellido"]

    while True:
        print("Ingrese sus datos")
        print("-----------------")
        print(f"[1] Nombre: {pasajeros[dni]['nombre']}")
        print(f"[2] Apellido: {pasajeros[dni]['apellido']}")
        print(f"[3] DNI: {dni}")
        print("[4] Guardar")
        print("[5] Cancelar")
        print("-----------------")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            escribirNombre = input("Ingrese Nombre: ").capitalize()
            for letra in escribirNombre:
                if letra in prohibidos:
                    bandera = False
                    break
                else:
                    bandera = True
            while escribirNombre == "" or bandera == False:
                print("No es valido dejar el espacio en blanco ni involucrar numeros")
                escribirNombre = input("Escribalo nuevamente: ").capitalize()
                for letra in escribirNombre:
                    if letra in prohibidos:
                        bandera = False
                        break
                    else:
                        bandera = True
            pasajeros[dni]["nombre"] = escribirNombre

        elif opcion == "2":
            escribirApellido = input("Ingrese Apellido: ").capitalize()
            for letra in escribirApellido:
                if letra in prohibidos:
                    bandera = False
                    break
                else:
                    bandera = True
            while escribirApellido == "" or bandera == False:
                print("No es valido dejar el espacio en blanco ni involucrar numeros")
                escribirApellido = input("Escribalo nuevamente: ").capitalize()
                for letra in escribirApellido:
                    if letra in prohibidos:
                        bandera = False
                        break
                    else:
                        bandera = True
            pasajeros[dni]["apellido"] = escribirApellido

        elif opcion == "3":
            print()
            print("El DNI no puede modificarse")

        elif opcion == "4":
            break

        elif opcion == "5":  # Cancelar
            pasajeros[dni]["nombre"] = copiaNombre
            pasajeros[dni]["apellido"] = copiaApellido
            break

        else:
            print("OPCIÓN INVÁLIDA")
    print("Sus datos")
    print("----------------")
    print(f"Nombre: {pasajeros[dni]['nombre']}")
    print(f"Apellido: {pasajeros[dni]['apellido']}")
    print(f"DNI: {dni}")
    print("----------------")
    print("Pasajero Modificado Correctamente")
    return


def eliminarPasajero(pasajeros: dict, pasajes: dict) -> None:
    """
    Elimina un pasajero del diccionario de pasajeros y su pasaje asociado del diccionario de pasajes.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    - pasajes (dict): Diccionario que contiene la información de los pasajes.
    """
    while True:
        dni = input(
            "Ingrese DNI de pasajero para eliminar su información o [0] para salir: "
        )
        if dni == "0":
            return
        elif dni == "":
            print("No ha ingresado el DNI")
        elif not dni.isnumeric():
            print("Solo se aceptan números")
        elif int(dni) not in pasajeros.keys():
            print("El pasajero no está registrado")
        else:
            dni = int(dni)
            break

    while True:
        print("¿Está seguro de eliminarlo?")
        print("[1] Si")
        print("[2] Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Eliminar al pasajero
            del pasajeros[dni]
            print(f"El pasajero con DNI {dni} ha sido eliminado.")
            # Eliminar su pasaje asociado
            eliminarPasaje(dni, pasajes)
            return
        elif opcion == "2":
            break
        else:
            print("Ingrese una opción válida")
    return


# ----------------------------------------------------------------------------------------------
# VUELOS
# ----------------------------------------------------------------------------------------------
def listarVuelos(vuelos: dict) -> None:
    """
    Lista todos los vuelos registrados junto con sus datos

    Args:
    - vuelos (dict): Diccionario que contiene la información de los vuelos.
    """
    for nVuelo, datos in vuelos.items():
        print(
            f"VUELO: {nVuelo},  FECHA: {datos['Fecha']},  ORIGEN: {datos['Origen']},  DESTINO: {datos['Destino']},  AVIÓN: {datos['Avion']}"
        )
    return


# ----------------------------------------------------------------------------------------------
# AVIONES
# ----------------------------------------------------------------------------------------------
def listarAviones(aviones: dict) -> None:
    """
    Lista todos los aviones registrados junto con sus datos

    Args:
    - aviones (dict): Diccionario que contiene la información de los aviones.
    """
    for nAvion, datos in aviones.items():
        print(
            f"MATRICULA: {nAvion},  MODELO: {datos['modelo']},  ASIENTOS: PRIMERA CLASE: {datos['Asientos']['primera']}  CLASE ECONÓMICA: {datos['Asientos']['economica']}"
        )
    return
