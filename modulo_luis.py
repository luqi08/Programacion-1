# Estructura de Datos
pasajeros = {"dni": {"nombre": str, "Apellido": str}}

pasajes = {
    "123456789012345": {
        "clase": "Economica",
        "asiento": "12A",
        "dni": 47307151,  # Juan Perez
        "vuelo": "LV-ABC",
    },
    "123456789012346": {
        "clase": "Primera",
        "asiento": "2B",
        "dni": 40215863,  # Maria Gomez
        "vuelo": "LV-BRD",
    },
    "123456789012347": {
        "clase": "Economica",
        "asiento": "18C",
        "dni": 38901453,  # Carlos Lopez
        "vuelo": "LV-CFT",
    },
    "123456789012348": {
        "clase": "Primera",
        "asiento": "5A",
        "dni": 42758963,  # Ana Martinez
        "vuelo": "LV-DRT",
    },
    "123456789012349": {
        "clase": "Economica",
        "asiento": "22D",
        "dni": 39456821,  # Jose Rodriguez
        "vuelo": "LV-EFP",
    },
    "123456789012350": {
        "clase": "Primera",
        "asiento": "1A",
        "dni": 41874529,  # Laura Fernandez
        "vuelo": "LV-GHT",
    },
    "123456789012351": {
        "clase": "Economica",
        "asiento": "15C",
        "dni": 40125678,  # Sofia Garcia
        "vuelo": "LV-HJK",
    },
    "123456789012352": {
        "clase": "Primera",
        "asiento": "3A",
        "dni": 38501452,  # Diego Sanchez
        "vuelo": "LV-JLM",
    },
    "123456789012353": {
        "clase": "Economica",
        "asiento": "10B",
        "dni": 42896532,  # Camila Diaz
        "vuelo": "LV-KRS",
    },
    "123456789012354": {
        "clase": "Economica",
        "asiento": "17A",
        "dni": 41236547,  # Martin Gonzalez
        "vuelo": "LV-LPQ",
    },
    "123456789012355": {
        "clase": "Primera",
        "asiento": "4B",
        "dni": 43985621,  # Lucia Romero
        "vuelo": "LV-ABC",
    },
    "123456789012356": {
        "clase": "Economica",
        "asiento": "25D",
        "dni": 39874512,  # Mateo Castro
        "vuelo": "LV-BRD",
    },
    "123456789012357": {
        "clase": "Economica",
        "asiento": "21A",
        "dni": 41798543,  # Julieta Suarez
        "vuelo": "LV-CFT",
    },
    "123456789012358": {
        "clase": "Primera",
        "asiento": "2A",
        "dni": 43652189,  # Lucas Mendez
        "vuelo": "LV-DRT",
    },
    "123456789012359": {
        "clase": "Economica",
        "asiento": "30C",
        "dni": 41327856,  # Emilia Vega
        "vuelo": "LV-EFP",
    },
    "123456789012360": {
        "clase": "Economica",
        "asiento": "19B",
        "dni": 42789654,  # Nicolas Cabrera
        "vuelo": "LV-GHT",
    },
    "123456789012361": {
        "clase": "Primera",
        "asiento": "1C",
        "dni": 39452187,  # Valentina Silva
        "vuelo": "LV-HJK",
    },
    "123456789012362": {
        "clase": "Economica",
        "asiento": "27A",
        "dni": 42985612,  # Federico Molina
        "vuelo": "LV-JLM",
    },
    "123456789012363": {
        "clase": "Economica",
        "asiento": "14D",
        "dni": 40312654,  # Agustina Rios
        "vuelo": "LV-KRS",
    },
    "123456789012364": {
        "clase": "Primera",
        "asiento": "6A",
        "dni": 41985463,  # Tomas Ortega
        "vuelo": "LV-LPQ",
    },
    "123456789012365": {
        "clase": "Economica",
        "asiento": "12C",
        "dni": 41258743,  # Milagros Ibarra
        "vuelo": "LV-ABC",
    },
    "123456789012366": {
        "clase": "Primera",
        "asiento": "7B",
        "dni": 43625489,  # Gabriel Reyes
        "vuelo": "LV-BRD",
    },
    "123456789012367": {
        "clase": "Economica",
        "asiento": "24A",
        "dni": 39874532,  # Sol Moreno
        "vuelo": "LV-CFT",
    },
    "123456789012368": {
        "clase": "Economica",
        "asiento": "16D",
        "dni": 42987145,  # Benjamin Paz
        "vuelo": "LV-DRT",
    },
    "123456789012369": {
        "clase": "Primera",
        "asiento": "8A",
        "dni": 40541236,  # Martina Campos
        "vuelo": "LV-EFP",
    },
    "123456789012370": {
        "clase": "Economica",
        "asiento": "22B",
        "dni": 41896325,  # Sebastian Soto
        "vuelo": "LV-GHT",
    },
    "123456789012371": {
        "clase": "Economica",
        "asiento": "18A",
        "dni": 42365471,  # Bianca Villalba
        "vuelo": "LV-HJK",
    },
    "123456789012372": {
        "clase": "Primera",
        "asiento": "9C",
        "dni": 43852147,  # Maximiliano Aguilar
        "vuelo": "LV-JLM",
    },
    "123456789012373": {
        "clase": "Economica",
        "asiento": "26D",
        "dni": 40215698,  # Florencia Pereyra
        "vuelo": "LV-KRS",
    },
    "123456789012374": {
        "clase": "Economica",
        "asiento": "29B",
        "dni": 42589647,  # Leandro Navarro
        "vuelo": "LV-LPQ",
    },
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


# PRECARGADOS
pasajeros = {  # 30 Pasajeros precargados
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

aviones = {
    "LV-ABC": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 20, "economica": 162},
    },
    "LV-BRD": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 20, "economica": 162},
    },
    "LV-CFT": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 20, "economica": 162},
    },
    "LV-DRT": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 20, "economica": 162},
    },
    "LV-EFP": {
        "modelo": "Boeing747-800",
        "Asientos": {"primera": 20, "economica": 162},
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

# VIEJO
# aviones = {
#     "Boeing747-800": {
#         "Matricula": "LV-ABC",
#         "Asientos": {"primera": 20, "economica": 162},
#     },
#     "Boeing747-800": {
#         "Matricula": "LV-BRD",
#         "Asientos": {"primera": 20, "economica": 162},
#     },
#     "Boeing747-800": {
#         "Matricula": "LV-CFT",
#         "Asientos": {"primera": 20, "economica": 162},
#     },
#     "Boeing747-800": {
#         "Matricula": "LV-DRT",
#         "Asientos": {"primera": 20, "economica": 162},
#     },
#     "Boeing747-800": {
#         "Matricula": "LV-EFP",
#         "Asientos": {"primera": 20, "economica": 162},
#     },
#     "AirbusA320Neo": {
#         "Matricula": "LV-GHT",
#         "Asientos": {"primera": 28, "economica": 150},
#     },
#     "AirbusA320Neo": {
#         "Matricula": "LV-HJK",
#         "Asientos": {"primera": 28, "economica": 150},
#     },
#     "AirbusA320Neo": {
#         "Matricula": "LV-JLM",
#         "Asientos": {"primera": 28, "economica": 150},
#     },
#     "AirbusA320Neo": {
#         "Matricula": "LV-KRS",
#         "Asientos": {"primera": 28, "economica": 150},
#     },
#     "AirbusA320Neo": {
#         "Matricula": "LV-LPQ",
#         "Asientos": {"primera": 28, "economica": 150},
#     },
# }


vuelos = {
    # Día 1 - Lunes
    "VU001": {
        "Fecha": "07/10/2024 | 06:00",
        "Origen": "Ciudad Autónoma de Buenos Aires (CABA)",
        "Destino": "La Plata (Buenos Aires)",
        "Avion": "LV-ABC",
    },
    "VU002": {
        "Fecha": "07/10/2024 | 08:00",
        "Origen": "La Plata (Buenos Aires)",
        "Destino": "Paraná (Entre Ríos)",
        "Avion": "LV-BRD",
    },
    "VU003": {
        "Fecha": "07/10/2024 | 10:00",
        "Origen": "Paraná (Entre Ríos)",
        "Destino": "Santa Fe",
        "Avion": "LV-CFT",
    },
    "VU004": {
        "Fecha": "07/10/2024 | 13:00",
        "Origen": "Santa Fe",
        "Destino": "Córdoba",
        "Avion": "LV-DRT",
    },
    "VU005": {
        "Fecha": "07/10/2024 | 16:00",
        "Origen": "Córdoba",
        "Destino": "Santiago del Estero",
        "Avion": "LV-EFP",
    },
    # Día 2 - Martes
    "VU006": {
        "Fecha": "08/10/2024 | 06:00",
        "Origen": "Santiago del Estero",
        "Destino": "San Miguel de Tucumán (Tucumán)",
        "Avion": "LV-GHT",
    },
    "VU007": {
        "Fecha": "08/10/2024 | 08:00",
        "Origen": "San Miguel de Tucumán (Tucumán)",
        "Destino": "San Fernando del Valle de Catamarca",
        "Avion": "LV-HJK",
    },
    "VU008": {
        "Fecha": "08/10/2024 | 10:00",
        "Origen": "San Fernando del Valle de Catamarca",
        "Destino": "La Rioja",
        "Avion": "LV-JLM",
    },
    "VU009": {
        "Fecha": "08/10/2024 | 13:00",
        "Origen": "La Rioja",
        "Destino": "San Juan",
        "Avion": "LV-KRS",
    },
    "VU010": {
        "Fecha": "08/10/2024 | 16:00",
        "Origen": "San Juan",
        "Destino": "Mendoza",
        "Avion": "LV-LPQ",
    },
    # Día 3 - Miércoles
    "VU011": {
        "Fecha": "09/10/2024 | 06:00",
        "Origen": "Mendoza",
        "Destino": "San Luis",
        "Avion": "LV-ABC",
    },
    "VU012": {
        "Fecha": "09/10/2024 | 09:00",
        "Origen": "San Luis",
        "Destino": "Formosa",
        "Avion": "LV-BRD",
    },
    "VU013": {
        "Fecha": "09/10/2024 | 12:00",
        "Origen": "Formosa",
        "Destino": "Resistencia (Chaco)",
        "Avion": "LV-CFT",
    },
    "VU014": {
        "Fecha": "09/10/2024 | 15:00",
        "Origen": "Resistencia (Chaco)",
        "Destino": "Corrientes",
        "Avion": "LV-DRT",
    },
    "VU015": {
        "Fecha": "09/10/2024 | 18:00",
        "Origen": "Corrientes",
        "Destino": "Posadas (Misiones)",
        "Avion": "LV-EFP",
    },
    # Día 4 - Jueves
    "VU016": {
        "Fecha": "10/10/2024 | 06:00",
        "Origen": "Posadas (Misiones)",
        "Destino": "Formosa",
        "Avion": "LV-GHT",
    },
    "VU017": {
        "Fecha": "10/10/2024 | 08:00",
        "Origen": "Formosa",
        "Destino": "Salta",
        "Avion": "LV-HJK",
    },
    "VU018": {
        "Fecha": "10/10/2024 | 10:00",
        "Origen": "Salta",
        "Destino": "San Salvador de Jujuy",
        "Avion": "LV-JLM",
    },
    "VU019": {
        "Fecha": "10/10/2024 | 13:00",
        "Origen": "San Salvador de Jujuy",
        "Destino": "San Fernando del Valle de Catamarca",
        "Avion": "LV-KRS",
    },
    "VU020": {
        "Fecha": "10/10/2024 | 16:00",
        "Origen": "San Fernando del Valle de Catamarca",
        "Destino": "La Rioja",
        "Avion": "LV-LPQ",
    },
    # Día 5 - Viernes
    "VU021": {
        "Fecha": "11/10/2024 | 06:00",
        "Origen": "La Rioja",
        "Destino": "Neuquén",
        "Avion": "LV-ABC",
    },
    "VU022": {
        "Fecha": "11/10/2024 | 09:00",
        "Origen": "Neuquén",
        "Destino": "Viedma (Río Negro)",
        "Avion": "LV-BRD",
    },
    "VU023": {
        "Fecha": "11/10/2024 | 12:00",
        "Origen": "Viedma (Río Negro)",
        "Destino": "Rawson (Chubut)",
        "Avion": "LV-CFT",
    },
    "VU024": {
        "Fecha": "11/10/2024 | 15:00",
        "Origen": "Rawson (Chubut)",
        "Destino": "Río Gallegos (Santa Cruz)",
        "Avion": "LV-DRT",
    },
    "VU025": {
        "Fecha": "11/10/2024 | 18:00",
        "Origen": "Río Gallegos (Santa Cruz)",
        "Destino": "Ushuaia (Tierra del Fuego)",
        "Avion": "LV-EFP",
    },
    # Día 6 - Sábado
    "VU026": {
        "Fecha": "12/10/2024 | 06:00",
        "Origen": "Ushuaia (Tierra del Fuego)",
        "Destino": "Río Gallegos (Santa Cruz)",
        "Avion": "LV-GHT",
    },
    "VU027": {
        "Fecha": "12/10/2024 | 09:00",
        "Origen": "Río Gallegos (Santa Cruz)",
        "Destino": "Rawson (Chubut)",
        "Avion": "LV-HJK",
    },
    "VU028": {
        "Fecha": "12/10/2024 | 12:00",
        "Origen": "Rawson (Chubut)",
        "Destino": "Viedma (Río Negro)",
        "Avion": "LV-JLM",
    },
    "VU029": {
        "Fecha": "12/10/2024 | 14:00",
        "Origen": "Viedma (Río Negro)",
        "Destino": "Neuquén",
        "Avion": "LV-KRS",
    },
    "VU030": {
        "Fecha": "12/10/2024 | 16:00",
        "Origen": "Neuquén",
        "Destino": "Santa Rosa (La Pampa)",
        "Avion": "LV-LPQ",
    },
    # Día 7 - Domingo
    "VU031": {
        "Fecha": "13/10/2024 | 06:00",
        "Origen": "Santa Rosa (La Pampa)",
        "Destino": "La Plata (Buenos Aires)",
        "Avion": "LV-ABC",
    },
    "VU032": {
        "Fecha": "13/10/2024 | 09:00",
        "Origen": "La Plata (Buenos Aires)",
        "Destino": "Ciudad Autónoma de Buenos Aires (CABA)",
        "Avion": "LV-BRD",
    },
}
