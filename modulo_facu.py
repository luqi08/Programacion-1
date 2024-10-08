#FUNCIONES
"""FALTA FUNCION PARA CAMBIAR DE CLASE"""
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
    filas_totales = len(matriz)
    medio = filas_totales // 2

    print("  " + " ".join(f"{i:>{ancho_columna}}" for i in range(1, longitud + 1)))

    for indice, fila in enumerate(matriz):
        letra = chr(65 + indice)  # 65 es el código ASCII de 'A'
        print(f"{letra} " + " ".join(f"{el:>{ancho_columna}}" for el in fila))
        if indice == medio - 1:
            print('PASILLO'.center(longitud * 3 + 1, '='))
    print('PUNTA DEL AVION A LA IZQUIERDA - COLA DEL AVION A LA DERECHA')

def mostrarPasaje(codigoPasaje):
    for clave, valor in pasajes[codigoPasaje].items():
        print(f'{clave}: {valor}'.title())

def cambiarAsiento(codigoPasaje):
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
                print('[1] CAMBIAR ASIENTO')
                print('[2] SALIR')
                opcion = int(input('SELECCIONE UNA OPCION: '))
                if opcion == 1:
                    print()
                    print(f'ASIENTO ACTUAL: {pasajes[codigoPasaje]['asiento']}')
                    mostrarMatriz(matriz)
                    cambiarAsiento(codigoPasaje)
                    print()
                    print(f'NUEVO ASIENTO: {pasajes[codigoPasaje]['asiento']}')
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

matriz = crearMatriz(4,30,0)

# if __name__ == "__main__": # Para no ejecutar la función al importar el módulo
#     modificarPasaje(pasajes)

pasajeros = {
    47307151: {'nombre': 'Juan', 'apellido': 'Perez'},
    40215863: {'nombre': 'Maria', 'apellido': 'Gomez'},
    38901453: {'nombre': 'Carlos', 'apellido': 'Lopez'},
    42758963: {'nombre': 'Ana', 'apellido': 'Martinez'},
    39456821: {'nombre': 'Jose', 'apellido': 'Rodriguez'},
    41874529: {'nombre': 'Laura', 'apellido': 'Fernandez'},
    40125678: {'nombre': 'Sofia', 'apellido': 'Garcia'},
    38501452: {'nombre': 'Diego', 'apellido': 'Sanchez'},
    42896532: {'nombre': 'Camila', 'apellido': 'Diaz'},
    41236547: {'nombre': 'Martin', 'apellido': 'Gonzalez'},
    43985621: {'nombre': 'Lucia', 'apellido': 'Romero'},
    39874512: {'nombre': 'Mateo', 'apellido': 'Castro'},
    41798543: {'nombre': 'Julieta', 'apellido': 'Suarez'},
    43652189: {'nombre': 'Lucas', 'apellido': 'Mendez'},
    41327856: {'nombre': 'Emilia', 'apellido': 'Vega'},
    42789654: {'nombre': 'Nicolas', 'apellido': 'Cabrera'},
    39452187: {'nombre': 'Valentina', 'apellido': 'Silva'},
    42985612: {'nombre': 'Federico', 'apellido': 'Molina'},
    40312654: {'nombre': 'Agustina', 'apellido': 'Rios'},
    41985463: {'nombre': 'Tomas', 'apellido': 'Ortega'},
    41258743: {'nombre': 'Milagros', 'apellido': 'Ibarra'},
    43625489: {'nombre': 'Gabriel', 'apellido': 'Reyes'},
    39874532: {'nombre': 'Sol', 'apellido': 'Moreno'},
    42987145: {'nombre': 'Benjamin', 'apellido': 'Paz'},
    40541236: {'nombre': 'Martina', 'apellido': 'Campos'},
    41896325: {'nombre': 'Sebastian', 'apellido': 'Soto'},
    42365471: {'nombre': 'Bianca', 'apellido': 'Villalba'},
    43852147: {'nombre': 'Maximiliano', 'apellido': 'Aguilar'},
    40215698: {'nombre': 'Florencia', 'apellido': 'Pereyra'},
    42589647: {'nombre': 'Leandro', 'apellido': 'Navarro'}
}

def modificarPasajero(pasajeros: dict, dni: int):
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