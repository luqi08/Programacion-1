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
    if numero_asiento < 5 and letra in ['A', 'B', 'C', 'D']:
        return True
    else:
        return False
    
def mostrarPasaje(pasajes, codigoPasaje):
    print(f"DNI: {pasajes[codigoPasaje]['dni']}")
    print(f"Vuelo: {pasajes[codigoPasaje]['vuelo']}")
    print(f"Clase: {pasajes[codigoPasaje]['clase']}")
    print(f"Asiento: {pasajes[codigoPasaje]['asiento']}")
    
def modificarPasaje(pasajes, vuelos):
    """
    Permite modificar un pasaje existente mediante su código, ya sea cambiando el asiento
    dentro de la misma clase o cambiando de clase. Muestra detalles del pasaje actual y
    solicita acciones al usuario.

    Args:
    - pasajes (dict): Diccionario que contiene la información de todos los pasajes.
    """
    while True:
        codigoPasaje = "PA" + input("INGRESE EL CODIGO DEL PASAJE O [0] PARA SALIR: ")
        if codigoPasaje == 'PA0':
            exit()
        elif codigoPasaje not in pasajes:
            print(f"SU PASAJE {codigoPasaje} NO ESTA REGISTRADO. REINTENTE...")
        else:
            print("--------------------------")
            mostrarPasaje(pasajes, codigoPasaje)
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
                        matrizAsientos = vuelos[pasajes[codigoPasaje]['vuelo']]['Asientos']['primera']
                        mostrarMatriz(matrizAsientos, pasajes, codigoPasaje)
                        cambiarAsiento(codigoPasaje, matrizAsientos, pasajes)
                    else:
                        matrizAsientos = vuelos[pasajes[codigoPasaje]['vuelo']]['Asientos']['economica']
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
                    exit()
                else:
                    print("INGRESE UN VALOR EN EL RANGO")
            break

#MAIN
matrizEconomica = crearMatriz(6,20,0)
matrizPrimera = crearMatriz(4,4,0)

vuelos = {
"VU001": {
        "Fecha": "07/10/2024 | 06:00",
        "Origen": "Santa Fe",
        "Destino": "La Plata (Buenos Aires)",
        "Avion": "LV-ABC",
        "Asientos" : {"primera": [[1,1,0,0],
                                  [1,0,0,0],
                                  [0,1,0,0],
                                  [0,0,0,1]],
                      "economica": [[1,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0],
                                    [1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0],
                                    [0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0],
                                    [1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0],
                                    [1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0],
                                    [0,1,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,0]]}
    }
}

pasajes = {
    "PA001": {"dni": 47307151, "vuelo": "VU001", "clase": "primera", "asiento": "D5"}
}

modificarPasaje(pasajes, vuelos)