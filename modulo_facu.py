#FUNCIONES
"ARREGLAR CREACION DE MATRICES AL USAR LA SEGUNDA OPCION DE CAMBIAR DE CLASE"
def crearMatriz(filas, columnas, relleno):
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

def letraNumero(letra):
    """
    Convierte una letra en su correspondiente número para indexación de matriz.

    Args:
    - letra (str): Letra del abecedario ('A'-'F').

    Returns:
    - int: Número correspondiente (0-5) para 'A'-'F'.
    """
    if letra == 'A':
        letra = 0
    elif letra == 'B':
        letra = 1
    elif letra == 'C':
        letra = 2
    elif letra == 'D':
        letra = 3
    elif letra == 'E':
        letra = 4
    elif letra == 'F':
        letra = 5
    return letra

def mostrarMatriz(matriz, pasaje, codigo):
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
            print('PASILLO'.center(longitud * 3 + 1, '='))
    print('PUNTA DEL AVION A LA IZQUIERDA - COLA DEL AVION A LA DERECHA')
    return

def mostrarPasaje(codigoPasaje):
    """
    Muestra los detalles del pasaje especificado.

    Args:
    - codigoPasaje (str): Código identificador del pasaje.
    """
    for clave, valor in pasajes[codigoPasaje].items():
        print(f'{clave}: {valor}'.title())
    return

def cambiarAsiento(codigoPasaje, matriz):
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
        filaAsiento = input('SELECCIONE LETRA (A,B,C,ETC.): ')
        if filaAsiento.capitalize() not in listaLetras:
            print(f'{filaAsiento} NO ESTÁ EN EL RANGO')
        else:
            break
    while True:
        filaColumna = int(input('SELECCIONE NUMERO (1,2,3,ETC.): '))
        if filaColumna < 1 or filaColumna > longitud:
            print(f'{filaColumna} NO ESTÁ EN EL RANGO')
        else:
            break
    pasajes[codigoPasaje]['asiento'] = filaAsiento.capitalize() + str(filaColumna)
    filaAsiento = letraNumero(filaAsiento.capitalize())
    matriz[filaAsiento][filaColumna - 1] = 1
    return

def esEjecutiva(pasajes, codigo):
    """
    Verifica si un asiento pertenece a la clase ejecutiva o no.

    Args:
    - pasajes (dict): Información sobre los pasajes y asientos ocupados.
    - codigo (str): Código identificador del pasaje.

    Returns:
    - bool: True si el asiento es ejecutivo, False si no lo es.
    """
    asiento = pasajes[codigo]['asiento']
    numero_asiento = int(asiento[1:])
    if numero_asiento < 5:
        return True
    else:
        return False

def modificarPasaje(pasajes):
    """
    Permite modificar un pasaje existente mediante su código, ya sea cambiando el asiento 
    dentro de la misma clase o cambiando de clase. Muestra detalles del pasaje actual y 
    solicita acciones al usuario.

    Args:
    - pasajes (dict): Diccionario que contiene la información de todos los pasajes.
    """
    while True:
        codigoPasaje = int(input('INGRESE EL CODIGO DEL PASAJE O [2] PARA SALIR: '))
        if codigoPasaje == 2:
            exit()
        elif codigoPasaje not in pasajes:
            print(f'SU PASAJE {codigoPasaje} NO ESTA REGISTRADO. REINTENTE...')
        else:
            print('--------------------------')
            mostrarPasaje(codigoPasaje)
            print('--------------------------')
            while True:
                print('[1] CAMBIAR ASIENTO DENTRO DE MISMA CLASE')
                print('[2] CAMBIAR CLASE')
                print('[3] SALIR')
                opcion = int(input('SELECCIONE UNA OPCION: '))
                if opcion == 1:
                    print()
                    print(f'ASIENTO ACTUAL: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}')
                    if esEjecutiva(pasajes, codigoPasaje):
                        mostrarMatriz(matrizEjecutiva, pasajes, codigoPasaje)
                        cambiarAsiento(codigoPasaje, matrizEjecutiva)
                    else:
                        mostrarMatriz(matrizEconomica, pasajes, codigoPasaje)
                        cambiarAsiento(codigoPasaje, matrizEconomica)
                    print()
                    print(f'NUEVO ASIENTO: {pasajes[codigoPasaje]['asiento']}, CLASE: {pasajes[codigoPasaje]['clase']}')
                    break
                elif opcion == 2:
                    while True:
                        print('[1] ECONÓMICA')
                        print('[2] EJECUTIVA')
                        opcion = int(input('SELECCIONE UNA OPCION: '))
                        if opcion == 1:
                            ...
                        elif opcion == 2:
                            ...
                        else:
                            print('INGRESE UN VALOR EN EL RANGO')
                elif opcion == 3:
                    exit()
                else:
                    print('INGRESE UN VALOR EN EL RANGO')
            break

#MAIN
pasajes = {000000: {'avion': 4523452, "clase": "primera", "asiento": "D4", "pasajero": 2354323}}
vuelos = {000000: {"Fecha": "20/10/2024", "Origen": "Misiones", 'destino': 'eze'}}
aviones = {"modelo": 'Boeing747'}

matrizEjecutiva = crearMatriz(6,30,0)
matrizEconomica = crearMatriz(4,4,0)

# if __name__ == "__main__": # Para no ejecutar la función al importar el módulo
#     modificarPasaje(pasajes)

def modificarPasajero(pasajeros: dict, dni: int):
    """
    Permite modificar los datos de un pasajero identificado por su DNI.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    - dni (int): DNI del pasajero que se desea modificar.
    """
    prohibidos = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    verificador = False
    while verificador == False:
        print("Ingrese sus datos")
        print("-----------------")
        print(f"[1]Nombre: {pasajeros[dni]['nombre']}")
        print(f"[2]Apellido: {pasajeros[dni]['apellido']}")
        print(f"[3]DNI: {dni}")
        print("[4]Realizar cambios (Reestablecera todo a su estado predeterminado)")
        print("[5]Completar")
        print("-----------------")
        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
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
            pasajeros[dni]['nombre'] = escribirNombre
            verificadorNombre == True
        elif opcion == '2':
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
            pasajeros[dni]['apellido'] = escribirApellido
        elif opcion == '3':
            print('El DNI no puede modificarse')
        elif opcion == '4':
            pasajeros[dni]['nombre'] = ""
            pasajeros[dni]['apellido'] = ""
            verificadorNombre = False
        elif opcion == '5':
            if pasajeros[dni]['nombre'] == '' or pasajeros[dni]['apellido'] == '' or dni == '':
                print("Aun quedan datos por completar")
            else:
                break
        else:
            print("Esa opcion no existe")
    print("Sus datos")
    print("----------------")
    print(f"Nombre: {pasajeros[dni]['nombre']}")
    print(f"Apellido: {pasajeros[dni]['apellido']}")
    print(f"DNI: {dni}")
    print("----------------")
    print("Pasajero Modificado Correctamente")
    return

def listarPasajeros(pasajeros: dict):
    """
    Lista todos los pasajeros registrados junto con su DNI y nombre completo.

    Args:
    - pasajeros (dict): Diccionario que contiene la información de los pasajeros.
    """
    for dni, datos in pasajeros.items():
        print(f'DNI: {dni}  PASAJERO: {datos['nombre']} {datos['apellido']}')
        return