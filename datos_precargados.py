#Precarga de aviones
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


#Precarga de pasajeros
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

#Precarga de vuelos
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