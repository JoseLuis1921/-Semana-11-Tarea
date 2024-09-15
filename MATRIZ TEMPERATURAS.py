from gettext import textdomain

temperatures = [
    [  # Ciudad 1_Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 58},
            {"day": "Martes", "temp": 60},
            {"day": "Miércoles", "temp": 84},
            {"day": "Jueves", "temp": 78},
            {"day": "Viernes", "temp": 60},
            {"day": "Sábado", "temp": 80},
            {"day": "Domingo", "temp": 88}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 89}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 80},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 89}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 74},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 82},
            {"day": "Domingo", "temp": 70}
        ]
    ],
    [  # Ciudad 2_Ambato
        [   # Semana 1
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 65},
            {"day": "Jueves", "temp": 75},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 71},
            {"day": "Domingo", "temp": 69}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 72},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 69},
            {"day": "Miércoles", "temp": 64},
            {"day": "Jueves", "temp": 75},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 78}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 70},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 79},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 72}
        ]
    ],
    [    # Ciudad 3_Santo Domingo
        [   # Semana 1
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 75},
            {"day": "Miércoles", "temp": 74},
            {"day": "Jueves", "temp": 61},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 72},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 79},
            {"day": "Martes", "temp": 81},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 74},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 51},
            {"day": "Martes", "temp": 63},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 73}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 80},
            {"day": "Miércoles", "temp": 72},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 66},
            {"day": "Sábado", "temp": 83},
            {"day": "Domingo", "temp": 79}
        ]
    ]
]
# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperatures:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)

