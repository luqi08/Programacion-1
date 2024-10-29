from datetime import datetime
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

def contarAsientosDisponibles(vuelos, codigo_vuelo):
    """
    Calcula la cantidad de asientos disponibles (0) en la matriz de asientos de un vuelo.

    Args:
    - vuelos (dict): Diccionario que contiene la información de los vuelos.
    - codigo_vuelo (str): Código del vuelo en el cual contar asientos disponibles.

    Returns:
    - int: Cantidad total de asientos disponibles.
    """
    asientos_disponibles = 0
    if codigo_vuelo in vuelos:
        # Recorre cada clase
        for clase, matriz_asientos in vuelos[codigo_vuelo]["Asientos"].items():
            for fila in matriz_asientos:
                asientos_disponibles += fila.count(0)
    else:
        print(f"El vuelo con código {codigo_vuelo} no existe.")
    
    return asientos_disponibles

def ingresoTexto(palabra: str) -> str:
    """
    Recibe un str para el mensaje de ingreso de dato
    Filtra todo lo que no sea caracteres alfabéticos
    """
    print()
    ingreso = input(f"Ingrese {palabra}: ")
    while ingreso.isalpha() == False:
        print()
        print("INGRESO INVÁLIDO")
        print()
        ingreso = input(f"Ingrese {palabra}: ")
    return ingreso


def ingresoEntero(palabra: str) -> int:
    """
    Recibe un str para el mensaje de ingreso de dato
    Filtra todo lo que no sea caracteres numéricos enteros
    """
    print()
    ingreso = input(f"Ingrese {palabra} o [0] para regresar: ")
    while ingreso.isnumeric() == False:
        print()
        print("INGRESO INVÁLIDO")
        print()
        ingreso = input(f"Ingrese {palabra}: ")
    return int(ingreso)


def mostrarPasaje(pasajes, codigoPasaje):
    print(f"DNI: {pasajes[codigoPasaje]['dni']}")
    print(f"Vuelo: {pasajes[codigoPasaje]['vuelo']}")
    print(f"Clase: {pasajes[codigoPasaje]['clase'].capitalize()}")
    print(f"Asiento: {pasajes[codigoPasaje]['asiento']}")


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
    letra = asiento[0]
    numero_asiento = int(asiento[1:])
    if numero_asiento < 5 and letra in ["A", "B", "C", "D"]:
        return True
    else:
        return False


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


def mostrarMatrizCambiarClase(matriz: list[list], pasaje: dict, codigo: str) -> None:
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
        print("  " + " ".join(f"{i:>{ancho_columna}}" for i in range(5, longitud + 5)))
    else:
        print("  " + " ".join(f"{i:>{ancho_columna}}" for i in range(1, longitud + 1)))

    for indice, fila in enumerate(matriz):
        letra = chr(65 + indice)  # 65 es el código ASCII de 'A'
        print(f"{letra} " + " ".join(f"{el:>{ancho_columna}}" for el in fila))
        if indice == medio - 1:
            print("PASILLO".center(longitud * 3 + 1, "="))
    print("PUNTA DEL AVION A LA IZQUIERDA - COLA DEL AVION A LA DERECHA")
    return


def estaOcupado(fila, columna, matriz):
    if matriz[fila][columna - 5] == 1:
        return True
    else:
        return False


def cambiarAsiento(codigoPasaje, matriz, pasajes):
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

    # Guardar asiento anterior antes de actualizarlo
    asientoAnterior = pasajes[codigoPasaje]["asiento"]
    letraAnterior = asientoAnterior[0]
    numero_asientoAnterior = int(asientoAnterior[1:])
    filaAnterior = letraNumero(letraAnterior.capitalize())

    # SELECCIONAR NUEVO ASIENTO
    while True:
        while True:
            filaAsiento = input("SELECCIONE LETRA (A,B,C,ETC.): ")
            if filaAsiento.capitalize() not in listaLetras:
                print(f"{filaAsiento} NO ESTÁ EN EL RANGO")
            else:
                fila = letraNumero(filaAsiento.capitalize())
                break

        while True:
            filaColumna = int(input("SELECCIONE NUMERO (1,2,3,ETC.): "))
            if 1 > filaColumna > longitud:
                print(f"{filaColumna} NO ESTÁ EN EL RANGO")
            else:
                break

        if estaOcupado(fila, filaColumna, matriz):
            print("Asiento ocupado... Reintente")
        else:
            break

    # MODIFICAR DICCIONARIO Y MATRIZ
    pasajes[codigoPasaje]["asiento"] = filaAsiento.capitalize() + str(filaColumna)
    filaAsiento = letraNumero(filaAsiento.capitalize())
    matriz[filaAsiento][filaColumna - 5] = 1

    # Ahora poner en 0 el asiento anterior
    matriz[filaAnterior][numero_asientoAnterior - 5] = 0
    return


# ----------------------------------------------------------------------------------------------
# PASAJES
# ----------------------------------------------------------------------------------------------


def buscarAsiento(matriz, selecto):
    """
    Esta función se encarga de buscar el asiento selecto  entre los asientos disponibles entre todos los disponibles en la matriz de asientos.
    Utiliza un iterable while para recorrer la matriz hasta encontrar el asiento. En caso de estar vacío devuelve True y se compra dicho asiento,
    en caso contrario, devolverá False y se le pedirá otro asiento al comprador.
    """

    contador = 0
    for asiento in matriz:
        for asiento in matriz[contador]:
            if asiento == selecto:
                return True
        contador = contador + 1
    return False


def comprarPasaje(pasajeros: dict, pasajes: dict, vuelos: dict) -> dict:
    """
    Permite seleccionar un destino, elegir un vuelo disponible para ese destino,
    seleccionar una clase y asiento, y registrar los datos del pasajero para crear un pasaje.

    Args:
    - pasajeros (dict): Información sobre los pasajeros.
    - pasajes (dict): Información sobre los pasajes y asientos ocupados.
    - vuelos (dict): Información sobre los vuelos.
    """
    # Ingreso/Registro Pasajero
    bandera = True
    while bandera:
        dni = ingresoEntero("DNI")
        if dni == 0:
            return
        if dni in pasajeros.keys():
            bandera = False
        elif dni not in pasajeros.keys():
            print()
            print(f"El DNI: {dni}, no se encuentra registrado.")
            while True:
                print()
                print("¿Desea registrarlo?")
                print("[1] Si")
                print("[2] No")
                opcion = input("Ingrese opción: ")
                if opcion == "1":
                    if registrarPasajero(pasajeros, dni) == True:
                        bandera = False
                        break
                    else:
                        break
                elif opcion == "2":
                    break
                else:
                    print()
                    print("Ingreso Inválido")

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
        for clave, destino in destinos.items():
            print(f"[{clave}] {destino}")
        print("[0] Volver al Menú Principal")
        print()

        opcionDestino = input("Seleccione un destino: ")
        if opcionDestino == "0":
            return  # Volver al menú principal
        elif opcionDestino in destinos:
            destino = destinos[opcionDestino]
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    # Filtrar vuelos disponibles para el destino seleccionado
    vuelosDestino = {
        clave: vuelo for clave, vuelo in vuelos.items() if vuelo["Destino"] == destino
    }

    if not vuelosDestino:
        print(f"No hay vuelos disponibles para {destino}.")
        return

    # Seleccionar vuelo
    print("\nVuelos disponibles para", destino)
    vuelosLista = list(
        vuelosDestino.items()
    )  # Convertimos el diccionario en una lista de tuplas

    for indice, (vueloId, vueloInfo) in enumerate(vuelosLista, start=1):
        print(f"[{indice}] {vueloInfo['Fecha']} | Origen: {vueloInfo['Origen']}")

    while True:
        seleccion = input(
            "Seleccione el número del vuelo: "
        )  # Pedimos el número del vuelo

        if seleccion.isdigit():  # Verificamos que la entrada sea un número
            seleccion = int(seleccion)

            if (
                1 <= seleccion <= len(vuelosLista)
            ):  # Verificamos que el número esté en el rango válido
                vueloSeleccionado = vuelosLista[seleccion - 1][
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
            claseSeleccionada = "primera"
            break
        elif clase == "2":
            claseSeleccionada = "economica"
            break
        else:
            input("Opción inválida. Presione ENTER para volver a seleccionar.")

    # Asignación de asiento (simplificado para este ejemplo)
    asiento = input("Seleccione su asiento (Ej: A1, B2): ").upper()

    # Generar nuevo ID de pasaje
    nuevo_id = f"PA{str(len(pasajes) + 1).zfill(3)}"

    # Crear el nuevo pasaje
    pasajes[nuevo_id] = {
        "dni": dni,
        "vuelo": vueloSeleccionado,
        "clase": claseSeleccionada,
        "asiento": asiento,
    }

    print(f"Pasaje registrado con éxito. ID del pasaje: {nuevo_id}")
    return pasajes


def listarPasajes(pasajes, pasajeros):
    """
    Lista todos los pasajes registrados junto con sus datos

    Args:
    - pasajes (dict): Diccionario que contiene la información de los pasajes.
    """
    # Encabezado de la tabla
    print(f"{'CÓDIGO':<6} | {'PASAJERO':<20} | {'DNI':<10} | {'VUELO':<5} | {'CLASE':<9} | {'ASIENTO':<10}")
    print("-" * 75)

    # Filas de la tabla
    for nPasaje, datos in pasajes.items():
        nombre = nombrePasajero(pasajeros, datos["dni"])
        print(
            f"{nPasaje:<6} | {nombre:<20} | {datos['dni']:<10} | {datos['vuelo']:<5} | {datos['clase'].capitalize():<9} | {datos['asiento']:<10}"
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


def modificarPasaje(pasajes, vuelos):
    """
    Permite modificar un pasaje existente mediante su código, ya sea cambiando el asiento
    dentro de la misma clase o cambiando de clase. Muestra detalles del pasaje actual y
    solicita acciones al usuario.

    Args:
    - pasajes (dict): Diccionario que contiene la información de todos los pasajes.
    """
    while True:
        codigoPasaje = "PA" + input("Ingrese el codigo del pasaje o [0] para salir: ")
        if codigoPasaje == 'PA0':
            return
        elif codigoPasaje not in pasajes:
            print(f"El pasaje {codigoPasaje} no esta registrado. Reintente...")
        else:
            print("--------------------------")
            mostrarPasaje(pasajes, codigoPasaje)
            print("--------------------------")
            while True:
                print("[1] Cambiar asiento dentro de la misma clase")
                print("[2] Cambiar clase")
                print("[3] Volver a Pasajes")
                opcion = int(input("Selecciona una opcion: "))

                if opcion == 1:
                    print()
                    print(
                        f"ASIENTO ACTUAL: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}"
                    )
                    if esEjecutiva(pasajes, codigoPasaje):
                        matrizAsientos = vuelos[pasajes[codigoPasaje]['vuelo']]['Asientos']['Primera']
                        mostrarMatriz(matrizAsientos, pasajes, codigoPasaje)
                        cambiarAsiento(codigoPasaje, matrizAsientos, pasajes)
                    else:
                        matrizAsientos = vuelos[pasajes[codigoPasaje]['vuelo']]['Asientos']['Economica']
                        mostrarMatriz(matrizAsientos, pasajes, codigoPasaje)
                        cambiarAsiento(codigoPasaje, matrizAsientos, pasajes)
                    print()
                    print(
                        f"NUEVO ASIENTO: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}"
                    )
                    mostrarMatriz(matrizAsientos, pasajes, codigoPasaje)
                    break

                elif opcion == 2:
                    print()
                    print(
                        f"ASIENTO ACTUAL: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}"
                    )
                    if esEjecutiva(pasajes, codigoPasaje):
                        matrizAsientos = vuelos[pasajes[codigoPasaje]['vuelo']]['Asientos']['economica']
                        mostrarMatrizCambiarClase(matrizAsientos, pasajes, codigoPasaje)
                        cambiarAsiento(codigoPasaje, matrizAsientos, pasajes)
                    else:
                        matrizAsientos = vuelos[pasajes[codigoPasaje]['vuelo']]['Asientos']['primera']
                        mostrarMatrizCambiarClase(matrizAsientos, pasajes, codigoPasaje)
                        cambiarAsiento(codigoPasaje, matrizAsientos, pasajes)
                    print()
                    print(
                        f"NUEVO ASIENTO: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}"
                    )
                    mostrarMatriz(matrizAsientos, pasajes, codigoPasaje)
                    break

                elif opcion == 3:
                    break
                else:
                    print("Ingrese un valor en el rango")
            break


def eliminarPasaje(pasajes: dict) -> None:
    """
    Elimina el pasaje asociado a un pasajero del diccionario de pasajes.

    Args:
    - dni (int): El DNI del pasajero cuyo pasaje será eliminado.
    - pasajes (dict): Diccionario que contiene la información de los pasajes.
    """
    while True:
        pasaje = "PA" + input("Ingrese número de pasaje o [0] para salir: ")
        if pasaje == "0":
            return
        elif pasaje == "":
            print("No ha ingresado el número de pasaje")
        elif pasaje not in pasajes.keys():
            print("No se encontró ningún pasaje con el número ingresado")
        else:
            del pasajes[pasaje]
            print()
            print(f"Pasaje número: {pasaje}, eliminado")
            return


# ----------------------------------------------------------------------------------------------
# PASAJEROS
# ----------------------------------------------------------------------------------------------
def registrarPasajero(pasajeros: dict, dni="") -> None:
    """
    Registra un nuevo pasajero solicitando su nombre, apellido y DNI, asegurando que no se
    introduzcan caracteres numéricos en los nombres y que el DNI sea numérico. Los datos
    ingresados son almacenados en el diccionario de pasajeros.

    Args:
    - pasajeros (dict): Diccionario donde se almacenan los datos de los pasajeros.

    Returns:
    - dni (int): Numero dni para identificar al pasajero.
    """
    nombre = ""
    apellido = ""
    verificador = False
    while verificador == False:
        print()
        print("Ingrese sus datos")
        print("-----------------")
        print(f"[1] Nombre: {nombre}")
        print(f"[2] Apellido: {apellido}")
        print(f"[3] DNI: {dni}")
        print("[4] Guardar")
        print("[5] Cancelar")
        print("-----------------")
        opcion = input("Seleccione una opcion: ")
        # Ingreso Nombre
        if opcion == "1":
            print()
            nombre = ingresoTexto("Nombre").capitalize()
            print()

        # Ingreso Apellido
        elif opcion == "2":
            print()
            apellido = ingresoTexto("Apellido").capitalize()
            print()
        # Ingreso DNI
        elif opcion == "3":
            print()
            dni = ingresoEntero("DNI")
            print()
        elif opcion == "4":
            if nombre == "" or apellido == "" or dni == "":
                print()
                print("Aun quedan datos por completar")
            else:
                break
        elif opcion == "5":
            nombre = ""
            apellido = ""
            dni = ""
            return
        else:
            print("OPCIÓN INVÁLIDA")
    print("Sus datos")
    print("----------------")
    print(f"Nombre: {nombre}")
    print(f"Apellido: {apellido}")
    print(f"DNI: {dni}")
    print("----------------")
    pasajeros[dni] = {"nombre": nombre, "apellido": apellido}
    print("Pasajero registrado")
    return True


def listarPasajeros(pasajeros: dict) -> None:
    """
    Lista todos los pasajeros registrados junto con su DNI y nombre completo.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    """
    # Encabezado de la tabla
    print(f"{'DNI':<10} | {'NOMBRE COMPLETO':<30}")
    print("-" * 28)

    # Filas de la tabla
    for dni, datos in pasajeros.items():
        nombre_completo = f"{datos['nombre']} {datos['apellido']}"
        print(f"{dni:<10} | {nombre_completo:<30}")
    return



def modificarPasajero(pasajeros: dict) -> None:
    """
    Permite modificar los datos de un pasajero identificado por su DNI.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    - dni (int): DNI del pasajero que se desea modificar.
    """
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
            nombre = ingresoTexto("Nombre").capitalize()
            pasajeros[dni]["nombre"] = nombre

        elif opcion == "2":
            apellido = ingresoTexto("Apellido").capitalize()
            pasajeros[dni]["apellido"] = apellido

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


def eliminarPasajero(pasajeros: dict) -> None:
    """
    Elimina un pasajero del diccionario de pasajeros y su pasaje asociado del diccionario de pasajes.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    - pasajes (dict): Diccionario que contiene la información de los pasajes.
    """
    while True:
        print()
        dni = input("Ingrese DNI del pasajero o [0] para salir: ")
        if dni == "0":
            return
        elif dni == "":
            print("No ha ingresado el DNI")
        elif not dni.isnumeric():
            print("Solo se aceptan números")
        elif int(dni) not in pasajeros.keys():
            print()
            print("El DNI {dni} no se encuentra registrado")
        else:
            dni = int(dni)
            nombre = pasajeros[dni]["nombre"]
            apellido = pasajeros[dni]["apellido"]
            break

    while True:
        print()
        print(f"Pasajero: {nombre} {apellido} | {dni}")
        print()
        print("¿Está seguro de eliminarlo?")
        print("[1] Si")
        print("[2] Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Eliminar al pasajero
            del pasajeros[dni]
            print()
            print(f"El pasajero con DNI {dni} ha sido eliminado.")
            return
        elif opcion == "2":
            break
        else:
            print("Opción inválida")
    return


# ----------------------------------------------------------------------------------------------
# VUELOS
# ----------------------------------------------------------------------------------------------
def listarVuelos(vuelos: dict) -> None:
    """
    Lista todos los vuelos registrados junto con sus datos.

    Args:
    - vuelos (dict): Diccionario que contiene la información de los vuelos.
    """
    # Encabezado de la tabla
    print(f"{'VUELO':<5} | {'FECHA':<10} | {'HORA':<5} | {'ORIGEN':<26} | {'DESTINO':<26} | {'AVIÓN':<10} | {'DISPONIBILIDAD':<10}")
    print("-" * 115)

    # Filas de la tabla
    for nVuelo, datos in vuelos.items():
        asientosDisponibles = contarAsientosDisponibles(vuelos, nVuelo)
        print(
            f"{nVuelo:<5} | {datos['Fecha']:<10} | {datos['Hora']:<5} | {datos['Origen']:<26} | {datos['Destino']:<26} | {datos['Avion']:<10} | {asientosDisponibles:<10}"
        )
    return

def registrarVuelo(vuelos: dict, aviones:dict):
    codigo = 'VU0' + str(len(vuelos) + 1)
    fecha = ''
    hora = ''
    origen = ''
    destino = ''
    avion = ''

    while True:
        print("Registre datos del vuelo")
        print("-----------------")
        print(f"[1] Codigo: {codigo}")
        print(f"[2] Fecha: {fecha}")
        print(f"[3] Hora: {hora}")
        print(f"[4] Origen: {origen}")
        print(f"[5] Destino: {destino}")
        print(f"[6] Avion: {avion}")
        print("[7] Guardar")
        print("[8] Cancelar")
        print("-----------------")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print('El código no puede modificarse')

        elif opcion == "2":
            while True:
                fecha = input("Ingrese la fecha (dd/mm/yyyy): ")
                try:
                    # Intenta convertir la entrada a formato de fecha
                    fechaFormateada = datetime.strptime(fecha, "%d/%m/%Y")
                    # Si es válida, la almacena en el diccionario y sale del bucle
                    fecha = fechaFormateada.strftime("%d/%m/%Y")
                    break
                except ValueError:
                    # Mensaje de error si el formato es incorrecto
                    print("Formato de fecha inválido. Ingrese la fecha en formato dd/mm/yyyy.")

        elif opcion == "3":
            while True:
                hora = input("Ingrese la hora (hh:mm): ")
                try:
                    horaFormateada = datetime.strptime(hora, "%H:%M")
                    hora = horaFormateada.strftime("%H:%M")
                    break
                except ValueError:
                    print("Formato de hora inválido. Ingrese la hora en formato hh:mm.")

        elif opcion == "4":
            origen = input().title()

        elif opcion == "5":
            destino = input().title()

        elif opcion == "6":
            while True:
                matricula = input().upper()
                if matricula not in aviones.keys():
                    print('El avion no esta registrado')
                else:
                    avion = matricula
                    break

        elif opcion == "7":
            if fecha == '' or hora == '' or origen == '' or destino == '' or avion == '':
                print('Quedan dantos sin completar')
            else:
                break
        else:
            print("OPCIÓN INVÁLIDA")

    matrizPrimera = crearMatriz(4,4,0)
    matrizEconomica = crearMatriz(6,20,0)

    vuelos[codigo] = {
        "Fecha" : fecha,
        "Hora" : hora,
        "Origen" : origen,
        "Destino" : destino,
        "Avion" : avion,
        "Asientos" : {
            "Primera" : matrizPrimera,
            "Economica" : matrizEconomica
                      }
    }

    print("Sus datos")
    print("-----------------")
    print(f"[1] Codigo: {codigo}")
    print(f"[2] Fecha: {vuelos[codigo]['Fecha']}")
    print(f"[3] Hora: {vuelos[codigo]['Hora']}")
    print(f"[4] Origen: {vuelos[codigo]['Origen']}")
    print(f"[5] Destino: {vuelos[codigo]['Destino']}")
    print(f"[6] Avion: {vuelos[codigo]['Avion']}")
    print("-----------------")
    print("Vuelo registrado correctamente")
    return

def modificarVuelo(vuelos: dict, aviones:dict):
    while True:
        print()
        codigo = "VU" + input('Ingrese codigo de vuelo o [0] para salir: ')
        if codigo == "VU0":
            return
        elif codigo not in vuelos.keys():
            print()
            print(f"El Vuelo {codigo} no se encuentra registrado")
        else:
            break
    
    copiaFecha = vuelos[codigo]['Fecha']
    copiaHora = vuelos[codigo]['Hora']
    copiaOrigen = vuelos[codigo]['Origen']
    copiaDestino = vuelos[codigo]['Destino']
    copiaAvion = vuelos[codigo]['Avion']

    while True:
        print("Modifique sus datos")
        print("-----------------")
        print(f"[1] Codigo: {codigo}")
        print(f"[2] Fecha: {vuelos[codigo]['Fecha']}")
        print(f"[3] Hora: {vuelos[codigo]['Hora']}")
        print(f"[4] Origen: {vuelos[codigo]['Origen']}")
        print(f"[5] Destino: {vuelos[codigo]['Destino']}")
        print(f"[6] Avion: {vuelos[codigo]['Avion']}")
        print("[7] Guardar")
        print("[8] Cancelar")
        print("-----------------")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print('El código no puede modificarse')

        elif opcion == "2":
            while True:
                fecha = input("Ingrese la fecha (dd/mm/yyyy): ")
                try:
                    # Intenta convertir la entrada a formato de fecha
                    fechaFormateada = datetime.strptime(fecha, "%d/%m/%Y")
                    # Si es válida, la almacena en el diccionario y sale del bucle
                    vuelos[codigo]['Fecha'] = fechaFormateada.strftime("%d/%m/%Y")
                    break
                except ValueError:
                    # Mensaje de error si el formato es incorrecto
                    print("Formato de fecha inválido. Ingrese la fecha en formato dd/mm/yyyy.")

        elif opcion == "3":
            while True:
                hora = input("Ingrese la hora (hh:mm): ")
                try:
                    horaFormateada = datetime.strptime(hora, "%H:%M")
                    vuelos[codigo]['Hora'] = horaFormateada.strftime("%H:%M")
                    break
                except ValueError:
                    print("Formato de hora inválido. Ingrese la hora en formato hh:mm.")

        elif opcion == "4":
            vuelos[codigo]['Origen'] = input().title()

        elif opcion == "5":
            vuelos[codigo]['Destino'] = input().title()

        elif opcion == "6":
            while True:
                matricula = input().upper()
                if matricula not in aviones.keys():
                    print('El avion no esta registrado')
                else:
                    vuelos[codigo]['Avion'] = matricula
                    break

        elif opcion == "7":
            return

        elif opcion == "8":  # Cancelar
            vuelos[codigo]["Fecha"] = copiaFecha
            vuelos[codigo]["Hora"] = copiaHora
            vuelos[codigo]["Origen"] = copiaOrigen
            vuelos[codigo]["Destino"] = copiaDestino
            vuelos[codigo]["Avion"] = copiaAvion
            break

        else:
            print("OPCIÓN INVÁLIDA")
    print("Sus datos")
    print("-----------------")
    print(f"[1] Codigo: {codigo}")
    print(f"[2] Fecha: {vuelos[codigo]['Fecha']}")
    print(f"[3] Hora: {vuelos[codigo]['Hora']}")
    print(f"[4] Origen: {vuelos[codigo]['Origen']}")
    print(f"[5] Destino: {vuelos[codigo]['Destino']}")
    print(f"[6] Avion: {vuelos[codigo]['Avion']}")
    print("-----------------")
    print("Vuelo modificado correctamente")
    return

def eliminarVuelo(vuelos: dict) -> None:
    """
    Elimina un vuelo del diccionario de pasajeros y su pasaje asociado del diccionario de pasajes.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    - pasajes (dict): Diccionario que contiene la información de los pasajes.
    """
    while True:
        print()
        codigo = "VU" + input('Ingrese codigo de vuelo o [0] para salir: ')
        if codigo == "VU0":
            return
        elif codigo not in vuelos.keys():
            print()
            print(f"El Vuelo {codigo} no se encuentra registrado")
        else:
            break

    while True:
        print()
        print(f"Vuelo: {codigo}")
        print()
        print("¿Está seguro de eliminarlo?")
        print("[1] Si")
        print("[2] Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            # Eliminar al vuelo
            del vuelos[codigo]
            print()
            print(f"El vuelo {codigo} ha sido eliminado.")
            return
        elif opcion == "2":
            break
        else:
            print("Opción inválida")
    return

# ----------------------------------------------------------------------------------------------
# AVIONES
# ----------------------------------------------------------------------------------------------
def listarAviones(aviones: dict) -> None:
    """
    Lista todos los aviones registrados junto con sus datos.

    Args:
    - aviones (dict): Diccionario que contiene la información de los aviones.
    """
    # Encabezado de la tabla
    print(f"{'MATRICULA':<9} | {'MODELO':<13} | {'PRIMERA CLASE':<13} | {'CLASE ECONÓMICA':<15}")
    print("-" * 60)

    # Filas de la tabla
    for nAvion, datos in aviones.items():
        print(
            f"{nAvion:<9} | {datos['modelo']:<12} | {datos['Asientos']['primera']:<13} | {datos['Asientos']['economica']:<15}"
        )
    return



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

        elif opcion == "5":
            modelo = ""
            matricula = ""
            primeraClase = ""
            claseEconomica = ""

        elif opcion == "6":
            if (
                modelo != ""
                and matricula != ""
                and primeraClase != ""
                and claseEconomica != ""
            ):
                print("Aun quedan datos por completar")
            else:
                aviones[matricula] = {
                    "modelo": modelo,
                    "asientos": {"primera": primeraClase, "econocmica": claseEconomica},
                }
                break
        elif opcion == 0:
            break

        else:
            print("Esa opcion no existe")
