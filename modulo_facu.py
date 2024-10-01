#FUNCIONES
"""FALTA FUNCION PARA CAMBIAR DE CLASE Y BUCLE PARA ERRORES DE TIPEO AL ELEGIR LETRA Y NUMERO DE ASIENTO"""
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

def mostrarMatriz(matriz):
    longitud = len(matriz[0])
    ancho_columna = 2
    
    print("  " + " ".join(f"{i:>{ancho_columna}}" for i in range(1, longitud + 1)))
    
    for indice, fila in enumerate(matriz):
        letra = chr(65 + indice)  # 65 es el código ASCII de 'A'
        print(f"{letra} " + " ".join(f"{el:>{ancho_columna}}" for el in fila))
        if letra == 'C':
            print('PASILLO'.center(longitud * 3 + 1, '='))
    print('PUNTA DEL AVION A LA IZQUIERDA - COLA DEL AVION A LA DERECHA')

def mostrarPasaje(codigoPasaje):
    for clave, valor in pasajes[codigoPasaje].items():
        print(f'{clave}: {valor}'.title())

def cambiarAsiento(codigoPasaje):
    filaAsiento = input('SELECCIONE LETRA (A,B,C,D,E,F): ')
    filaColumna = input('SELECCIONE NUMERO (1,2,3,ETC.): ')
    pasajes[codigoPasaje]['asiento'] = filaAsiento.capitalize() + filaColumna
    filaAsiento = letraNumero(filaAsiento.capitalize())
    matriz[filaAsiento][int(filaColumna) - 1] = 1

def modificarPasaje(pasajes):
    while True:
        codigoPasaje = int(input('INGRESE EL CODIGO DEL PASAJE: '))
        if codigoPasaje not in pasajes:
            print(f'SU PASAJE {codigoPasaje} NO ESTA REGISTRADO')
            while True:
                print('[1] REINTENTAR')
                print('[2] SALIR')
                opcion = int(input('SELECCIONE UNA OPCION: '))
                if opcion == 1:
                    break
                elif opcion == 2:
                    exit()
                else:
                    print('INGRESE UN VALOR EN EL RANGO')
        else:
            print('--------------------------')
            mostrarPasaje(codigoPasaje)
            print('--------------------------')
            while True:
                print('[1] CAMBIAR ASIENTO')
                print('[2] SALIR')
                opcion = int(input('SELECCIONE UNA OPCION: '))
                if opcion == 1:
                    print()
                    mostrarMatriz(matriz)
                    cambiarAsiento(codigoPasaje)
                    print()
                    print('ASIENTO MODIFICADO CORRECTAMENTE')
                    mostrarMatriz(matriz)
                    break
                elif opcion == 2:
                    exit()
                else:
                    print('INGRESE UN VALOR EN EL RANGO')
            break

#MAIN
pasajes = {000000: {'avion': 4523452, "clase": "primera", "asiento": "G8", "pasajero": 2354323}}
vuelos = {000000: {"Fecha": "20/10/2024", "Origen": "Misiones", 'destino': 'eze'}}
aviones = {"modelo": 'Boeing747'}

matriz = crearMatriz(6,30,0)
modificarPasaje(pasajes)
print()
mostrarPasaje(000000)