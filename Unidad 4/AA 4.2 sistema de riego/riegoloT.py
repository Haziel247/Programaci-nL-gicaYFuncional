def get_sensor_data():
    return {
        'humedad_suelo': 'baja',  # Puede ser: baja, media, critica
        'temperatura_area1': 33,   # Temperatura en área principal (grados)
        'hora_actual': 9,          # Hora actual (formato 24h)
        'pronostico_lluvia': False,
        'humedad_area2': 'media',  # Puede ser: baja, media, critica
        'temperatura_area2': 20    # Temperatura en área secundaria
    }

def es_hora_adecuada(data):
    hora = data['hora_actual']
    temp = data['temperatura_area1']
    
    if temp > 30:
        return hora <= 8 or hora >= 19  # Horas para regar optimas
    else:
        return hora <= 10 or hora >= 18  # Horario normal

def necesita_riego_principal(humedad, temp):
    if humedad == 'critica' or humedad == 'baja':
        return True
    elif humedad == 'media':
        return temp > 28
    return False

def necesita_riego_secundario(humedad, temp, humedad_principal):
    if humedad == 'critica' or humedad == 'baja':
        return True
    elif humedad == 'media':
        return temp > 25 and humedad_principal != 'critica'
    return False


def activar_riego_principal(data):
    return (
        necesita_riego_principal(data['humedad_suelo'], data['temperatura_area1']) and
        not data['pronostico_lluvia'] and
        es_hora_adecuada(data)
    )

def activar_riego_secundario(data):
    return (
        necesita_riego_secundario(
            data['humedad_area2'], 
            data['temperatura_area2'], 
            data['humedad_suelo']
        ) and
        not data['pronostico_lluvia'] and
        es_hora_adecuada(data)
    )


def generar_recomendaciones(data):
    recomendaciones = []
    
    # Recomendaciones generales de riego
    if activar_riego_principal(data) or activar_riego_secundario(data):
        if data['temperatura_area2'] > 30:
            recomendaciones.append('Recomendación: Regar por la noche o temprano en la mañana')
        else:
            recomendaciones.append('Recomendación: Puede regar en el horario establecido')

    
    # Recomendaciones específicas para humedad media
    if data['humedad_suelo'] == 'media' and not activar_riego_principal(data):
        recomendaciones.append('Recomendación: Monitorear área principal - Humedad media detectada')
    
    if data['humedad_area2'] == 'media' and not activar_riego_secundario(data):
        recomendaciones.append('Recomendación: Monitorear área secundaria - Humedad media detectada')

    if recomendaciones == [] :
        recomendaciones.append('Recomendación: Puede regar en el horario establecido')
        
    return recomendaciones


def mostrar_estado_riego(data):
    print(f"Área principal: Riego {'ACTIVADO' if activar_riego_principal(data) else 'desactivado'}")
    print(f"Área secundaria: Riego {'ACTIVADO' if activar_riego_secundario(data) else 'desactivado'}")

def mostrar_alertas(data):
    if data['temperatura_area1'] > 32:
        print('Alerta: Temperatura alta en área principal')
    elif data['temperatura_area1'] < 32:
        print('Alerta: Temperatura normal en área principal')
    
    if data['temperatura_area2'] > 32:
        print('Alerta: Temperatura alta en área secundaria')
    elif data['temperatura_area2'] < 32:
        print('Alerta: Temperatura normal en área secundaria')
    
    if data['humedad_suelo'] == 'critica':
        print('Alerta: Humedad CRÍTICA en área principal')
    
    if data['humedad_area2'] == 'critica':
        print('Alerta: Humedad CRÍTICA en área secundaria')


def main():
    # Obtener datos de los sensores (inmutables)
    sensor_data = get_sensor_data()
    
    # Mostrar estado y alertas
    print("\n------- ESTADO DEL SISTEMA -------")
    mostrar_estado_riego(sensor_data)
    
    print("\n------- ALERTAS -------")
    mostrar_alertas(sensor_data)
    
    print("\n------- RECOMENDACIONES -------")
    for recomendacion in generar_recomendaciones(sensor_data):
        print(recomendacion)

main()