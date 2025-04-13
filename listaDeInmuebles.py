listaInmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

for casa in listaInmuebles:
    año_actual = 2025
    antiguedad = año_actual - casa['año']
    metros = casa['metros']
    habitaciones = casa['habitaciones']
    garaje = 15000 if casa['garaje'] else 0
    zona = casa['zona']


    precio_base = (metros * 1000) + (habitaciones * 5000) + garaje


    if zona == 'A':
        precio = precio_base * (1 - antiguedad / 100)
        
    elif zona == 'B':
        precio = precio_base * (1 - antiguedad / 100) * 1.5


    print(f"Inmueble en Zona {zona}: Precio = ${precio:,.2f}")