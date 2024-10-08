#FUNCIONES
"ARREGLAR CREACION DE MATRICES AL USAR LA SEGUNDA OPCION DE CAMBIAR DE CLASE"
def crearMatriz(filas,columnas,relleno):
    return [[relleno] * columnas for fila in range(filas)]

def letraNumero(letra):
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

def mostrarPasaje(codigoPasaje):
    for clave, valor in pasajes[codigoPasaje].items():
        print(f'{clave}: {valor}'.title())

def cambiarAsiento(codigoPasaje, matriz):
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

def esEjecutiva(pasajes, codigo):
    asiento = pasajes[codigo]['asiento']
    numero_asiento = int(asiento[1:])
    if numero_asiento < 5:
        return True
    else:
        return False

def modificarPasaje(pasajes):
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

matrizEconomica = crearMatriz(6,26,0)
matrizEjecutiva = crearMatriz(4,4,0)
modificarPasaje(pasajes)