# Estructura de Datos
"""
pasajeros = {"dni": {"nombre": str, "Apellido": str}}

pasajes = {
    "pasaje": {"dni": int, "vuelo": str, "clase": str, "asiento": str}
}

aviones = {
    "matricula": {
        "modelo": str,
        "Asientos": {"primera": int, "economica": int},
    }
}

vuelos = {
    "Numero de Vuelo": {
        "Fecha": "dd/mm/yyyy | hh:mm",
        "Origen": str,
        "Destino": str,
        "Avion": "Matricula de Avion",
    }
}
"""


# Precarga pasajes
rutaPasajes = {
    "PA001": {"dni": 47307151, "vuelo": "VU003", "clase": "primera", "asiento": "A1"},
    "PA002": {
        "dni": 40215863,
        "vuelo": "VU001",
        "clase": "economica",
        "asiento": "C12",
    },
    "PA003": {"dni": 38901453, "vuelo": "VU001", "clase": "primera", "asiento": "B3"},
    "PA004": {
        "dni": 42758963,
        "vuelo": "VU002",
        "clase": "economica",
        "asiento": "D27",
    },
    "PA005": {"dni": 39456821, "vuelo": "VU004", "clase": "primera", "asiento": "C2"},
    "PA006": {
        "dni": 41874529,
        "vuelo": "VU001",
        "clase": "economica",
        "asiento": "A18",
    },
    "PA007": {"dni": 40125678, "vuelo": "VU003", "clase": "primera", "asiento": "D4"},
    "PA008": {
        "dni": 38501452,
        "vuelo": "VU005",
        "clase": "economica",
        "asiento": "F30",
    },
    "PA009": {"dni": 42896532, "vuelo": "VU002", "clase": "primera", "asiento": "B1"},
    "PA010": {
        "dni": 41236547,
        "vuelo": "VU001",
        "clase": "economica",
        "asiento": "E23",
    },
    "PA011": {"dni": 43985621, "vuelo": "VU001", "clase": "primera", "asiento": "A2"},
    "PA012": {
        "dni": 39874512,
        "vuelo": "VU004",
        "clase": "economica",
        "asiento": "B19",
    },
    "PA013": {"dni": 41798543, "vuelo": "VU001", "clase": "primera", "asiento": "C1"},
    "PA014": {
        "dni": 43652189,
        "vuelo": "VU001",
        "clase": "economica",
        "asiento": "D15",
    },
    "PA015": {"dni": 41327856, "vuelo": "VU004", "clase": "primera", "asiento": "D3"},
    "PA016": {"dni": 42789654, "vuelo": "VU001", "clase": "economica", "asiento": "F9"},
    "PA017": {"dni": 39452187, "vuelo": "VU001", "clase": "primera", "asiento": "B2"},
    "PA018": {
        "dni": 42985612,
        "vuelo": "VU002",
        "clase": "economica",
        "asiento": "A25",
    },
    "PA019": {"dni": 40312654, "vuelo": "VU001", "clase": "primera", "asiento": "C3"},
    "PA020": {
        "dni": 41985463,
        "vuelo": "VU005",
        "clase": "economica",
        "asiento": "E11",
    },
    "PA021": {"dni": 41258743, "vuelo": "VU005", "clase": "primera", "asiento": "D2"},
    "PA022": {
        "dni": 43625489,
        "vuelo": "VU001",
        "clase": "economica",
        "asiento": "C22",
    },
    "PA023": {"dni": 39874532, "vuelo": "VU003", "clase": "primera", "asiento": "A3"},
    "PA024": {
        "dni": 42987145,
        "vuelo": "VU001",
        "clase": "economica",
        "asiento": "B10",
    },
    "PA025": {"dni": 40541236, "vuelo": "VU004", "clase": "primera", "asiento": "B4"},
    "PA026": {"dni": 41896325, "vuelo": "VU001", "clase": "economica", "asiento": "D8"},
    "PA027": {"dni": 42365471, "vuelo": "VU001", "clase": "primera", "asiento": "C4"},
    "PA028": {
        "dni": 43852147,
        "vuelo": "VU002",
        "clase": "economica",
        "asiento": "F20",
    },
    "PA029": {"dni": 40215698, "vuelo": "VU001", "clase": "primera", "asiento": "D1"},
    "PA030": {
        "dni": 42589647,
        "vuelo": "VU003",
        "clase": "economica",
        "asiento": "A17",
    },
}

# Precarga de aviones
rutaAviones = {
    "LV-ABC": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 16, "economica": 120},
    },
    "LV-BRD": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 16, "economica": 120},
    },
    "LV-CFT": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 16, "economica": 120},
    },
    "LV-DRT": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 16, "economica": 120},
    },
    "LV-EFP": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 16, "economica": 120},
    },
    "LV-GHT": {
        "modelo": "AirbusA320Neo",
        "Asientos": {"primera": 28, "economica": 150},
    },
    "LV-HJK": {
        "modelo": "AirbusA320Neo",
        "Asientos": {"primera": 28, "economica": 150},
    },
    "LV-JLM": {
        "modelo": "AirbusA320Neo",
        "Asientos": {"primera": 28, "economica": 150},
    },
    "LV-KRS": {
        "modelo": "AirbusA320Neo",
        "Asientos": {"primera": 28, "economica": 150},
    },
    "LV-LPQ": {
        "modelo": "AirbusA320Neo",
        "Asientos": {"primera": 28, "economica": 150},
    },
}


# Precarga de pasajeros
rutaPasajeros = {
    47307151: {"nombre": "Juan", "apellido": "Perez"},
    40215863: {"nombre": "Maria", "apellido": "Gomez"},
    38901453: {"nombre": "Carlos", "apellido": "Lopez"},
    42758963: {"nombre": "Ana", "apellido": "Martinez"},
    39456821: {"nombre": "Jose", "apellido": "Rodriguez"},
    41874529: {"nombre": "Laura", "apellido": "Fernandez"},
    40125678: {"nombre": "Sofia", "apellido": "Garcia"},
    38501452: {"nombre": "Diego", "apellido": "Sanchez"},
    42896532: {"nombre": "Camila", "apellido": "Diaz"},
    41236547: {"nombre": "Martin", "apellido": "Gonzalez"},
    43985621: {"nombre": "Lucia", "apellido": "Romero"},
    39874512: {"nombre": "Mateo", "apellido": "Castro"},
    41798543: {"nombre": "Julieta", "apellido": "Suarez"},
    43652189: {"nombre": "Lucas", "apellido": "Mendez"},
    41327856: {"nombre": "Emilia", "apellido": "Vega"},
    42789654: {"nombre": "Nicolas", "apellido": "Cabrera"},
    39452187: {"nombre": "Valentina", "apellido": "Silva"},
    42985612: {"nombre": "Federico", "apellido": "Molina"},
    40312654: {"nombre": "Agustina", "apellido": "Rios"},
    41985463: {"nombre": "Tomas", "apellido": "Ortega"},
    41258743: {"nombre": "Milagros", "apellido": "Ibarra"},
    43625489: {"nombre": "Gabriel", "apellido": "Reyes"},
    39874532: {"nombre": "Sol", "apellido": "Moreno"},
    42987145: {"nombre": "Benjamin", "apellido": "Paz"},
    40541236: {"nombre": "Martina", "apellido": "Campos"},
    41896325: {"nombre": "Sebastian", "apellido": "Soto"},
    42365471: {"nombre": "Bianca", "apellido": "Villalba"},
    43852147: {"nombre": "Maximiliano", "apellido": "Aguilar"},
    40215698: {"nombre": "Florencia", "apellido": "Pereyra"},
    42589647: {"nombre": "Leandro", "apellido": "Navarro"},
}
rutaVuelos = {
    "VU001": {
        "Fecha": "07/10/2024",
        "Hora": "06:00",
        "Origen": "Santa Fe",
        "Destino": "La Plata (Buenos Aires)",
        "Avion": "LV-ABC",
        "Asientos": {
            "Primera": [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
            "Economica": [
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            ],
        },
    },
    "VU002": {
        "Fecha": "07/10/2024",
        "Hora": "08:00",
        "Origen": "La Plata (Buenos Aires)",
        "Destino": "Paraná (Entre Ríos)",
        "Avion": "LV-BRD",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU003": {
        "Fecha": "07/10/2024",
        "Hora": "10:00",
        "Origen": "Paraná (Entre Ríos)",
        "Destino": "Santa Fe",
        "Avion": "LV-CFT",
        "Asientos": {
            "Primera": [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0]],
            "Economica": [
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            ],
        },
    },
    "VU004": {
        "Fecha": "07/10/2024",
        "Hora": "13:00",
        "Origen": "Santa Fe",
        "Destino": "Córdoba",
        "Avion": "LV-DRT",
        "Asientos": {
            "Primera": [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
            "Economica": [
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            ],
        },
    },
    "VU005": {
        "Fecha": "07/10/2024",
        "Hora": "16:00",
        "Origen": "Córdoba",
        "Destino": "Santiago del Estero",
        "Avion": "LV-EFP",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    # Día 2 - Martes
    "VU006": {
        "Fecha": "08/10/2024",
        "Hora": "06:00",
        "Origen": "Santiago del Estero",
        "Destino": "San Miguel de Tucumán",
        "Avion": "LV-GHT",
        "Asientos": {
            "Primera": [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0]],
            "Economica": [
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            ],
        },
    },
    "VU007": {
        "Fecha": "08/10/2024",
        "Hora": "08:00",
        "Origen": "San Miguel de Tucumán",
        "Destino": "Catamarca",
        "Avion": "LV-HJK",
        "Asientos": {
            "Primera": [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0]],
            "Economica": [
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            ],
        },
    },
    "VU008": {
        "Fecha": "08/10/2024",
        "Hora": "10:00",
        "Origen": "Catamarca",
        "Destino": "La Rioja",
        "Avion": "LV-JLM",
        "Asientos": {
            "Primera": [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0]],
            "Economica": [
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            ],
        },
    },
    "VU009": {
        "Fecha": "08/10/2024",
        "Hora": "13:00",
        "Origen": "La Rioja",
        "Destino": "San Juan",
        "Avion": "LV-KRS",
        "Asientos": {
            "Primera": [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0]],
            "Economica": [
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            ],
        },
    },
    "VU010": {
        "Fecha": "08/10/2024",
        "Hora": "16:00",
        "Origen": "San Juan",
        "Destino": "Mendoza",
        "Avion": "LV-LPQ",
        "Asientos": {
            "Primera": [[0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0]],
            "Economica": [
                [0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1],
                [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1],
                [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
            ],
        },
    },
    # Día 3 - Miércoles
    "VU011": {
        "Fecha": "09/10/2024",
        "Hora": "06:00",
        "Origen": "Mendoza",
        "Destino": "San Luis",
        "Avion": "LV-ABC",
        "Asientos": {
            "Primera": [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
            "Economica": [
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            ],
        },
    },
    "VU012": {
        "Fecha": "09/10/2024",
        "Hora": "09:00",
        "Origen": "San Luis",
        "Destino": "Formosa",
        "Avion": "LV-BRD",
        "Asientos": {
            "Primera": [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
            "Economica": [
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            ],
        },
    },
    "VU013": {
        "Fecha": "09/10/2024",
        "Hora": "12:00",
        "Origen": "Formosa",
        "Destino": "Resistencia (Chaco)",
        "Avion": "LV-CFT",
        "Asientos": {
            "Primera": [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
            "Economica": [
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            ],
        },
    },
    "VU014": {
        "Fecha": "09/10/2024",
        "Hora": "15:00",
        "Origen": "Resistencia (Chaco)",
        "Destino": "Corrientes",
        "Avion": "LV-DRT",
        "Asientos": {
            "Primera": [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
            "Economica": [
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            ],
        },
    },
    "VU015": {
        "Fecha": "09/10/2024",
        "Hora": "18:00",
        "Origen": "Corrientes",
        "Destino": "Posadas (Misiones)",
        "Avion": "LV-EFP",
        "Asientos": {
            "Primera": [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
            "Economica": [
                [1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            ],
        },
    },
    # Día 4 - Jueves
    "VU016": {
        "Fecha": "10/10/2024",
        "Hora": "06:00",
        "Origen": "Posadas (Misiones)",
        "Destino": "Formosa",
        "Avion": "LV-GHT",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU017": {
        "Fecha": "10/10/2024",
        "Hora": "08:00",
        "Origen": "Formosa",
        "Destino": "Salta",
        "Avion": "LV-HJK",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU018": {
        "Fecha": "10/10/2024",
        "Hora": "10:00",
        "Origen": "Salta",
        "Destino": "San Salvador de Jujuy",
        "Avion": "LV-JLM",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU019": {
        "Fecha": "10/10/2024",
        "Hora": "13:00",
        "Origen": "San Salvador de Jujuy",
        "Destino": "Catamarca",
        "Avion": "LV-KRS",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU020": {
        "Fecha": "10/10/2024",
        "Hora": "16:00",
        "Origen": "Catamarca",
        "Destino": "La Rioja",
        "Avion": "LV-LPQ",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    # Día 5 - Viernes
    "VU021": {
        "Fecha": "11/10/2024",
        "Hora": "06:00",
        "Origen": "La Rioja",
        "Destino": "Neuquén",
        "Avion": "LV-ABC",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU022": {
        "Fecha": "11/10/2024",
        "Hora": "09:00",
        "Origen": "Neuquén",
        "Destino": "Viedma (Río Negro)",
        "Avion": "LV-BRD",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU023": {
        "Fecha": "11/10/2024",
        "Hora": "12:00",
        "Origen": "Viedma (Río Negro)",
        "Destino": "Rawson (Chubut)",
        "Avion": "LV-CFT",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU024": {
        "Fecha": "11/10/2024",
        "Hora": "15:00",
        "Origen": "Rawson (Chubut)",
        "Destino": "Río Gallegos (Santa Cruz)",
        "Avion": "LV-DRT",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU025": {
        "Fecha": "11/10/2024",
        "Hora": "18:00",
        "Origen": "Río Gallegos (Santa Cruz)",
        "Destino": "Ushuaia (Tierra del Fuego)",
        "Avion": "LV-EFP",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    # Día 6 - Sábado
    "VU026": {
        "Fecha": "12/10/2024",
        "Hora": "06:00",
        "Origen": "Ushuaia (Tierra del Fuego)",
        "Destino": "Río Gallegos (Santa Cruz)",
        "Avion": "LV-GHT",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU027": {
        "Fecha": "12/10/2024",
        "Hora": "09:00",
        "Origen": "Río Gallegos (Santa Cruz)",
        "Destino": "Rawson (Chubut)",
        "Avion": "LV-HJK",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU028": {
        "Fecha": "12/10/2024",
        "Hora": "12:00",
        "Origen": "Rawson (Chubut)",
        "Destino": "Viedma (Río Negro)",
        "Avion": "LV-JLM",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU029": {
        "Fecha": "12/10/2024",
        "Hora": "14:00",
        "Origen": "Viedma (Río Negro)",
        "Destino": "Neuquén",
        "Avion": "LV-KRS",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU030": {
        "Fecha": "12/10/2024",
        "Hora": "16:00",
        "Origen": "Neuquén",
        "Destino": "Santa Rosa (La Pampa)",
        "Avion": "LV-LPQ",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    # Día 7 - Domingo
    "VU031": {
        "Fecha": "13/10/2024",
        "Hora": "06:00",
        "Origen": "Santa Rosa (La Pampa)",
        "Destino": "La Plata (Buenos Aires)",
        "Avion": "LV-ABC",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
            ],
        },
    },
    "VU032": {
        "Fecha": "13/10/2024",
        "Hora": "09:00",
        "Origen": "La Plata (Buenos Aires)",
        "Destino": "Santa Fe",
        "Avion": "LV-BRD",
        "Asientos": {
            "Primera": [[0, 1, 1, 0], [1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 0, 1]],
            "Economica": [
                [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1],
                [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
            ],
        },
    },
}
