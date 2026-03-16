# Sistema de Navegación para un Vehículo Autónomo

def datos_sensor_camara():
    dat_camara_trafico = input("Nivel de Trafico (Alto, Medio, Bajo): ")
    dat_sensor_distancia = int(input("Distancia al obstaculo (10m, 20m, 30m): "))
    dat_sensor_velocidad = float(input("Velocidad del vehiculo (Km/h): "))

    return dat_camara_trafico, dat_sensor_distancia, dat_sensor_velocidad

def ruta_optima(dat_camara_trafico):
    if dat_camara_trafico == "Alto":
        print("Ruta 1")
    elif dat_camara_trafico == "Medio":
        print("Ruta 2")
    elif dat_camara_trafico == "Bajo":
        print("Ruta 3")

def evitar_obstaculo(dat_sensor_distancia):
    if dat_sensor_distancia < 10:
        print("Frenado de emergencia. Evitar obstaculo")
    elif 10 <= dat_sensor_distancia < 20:
        print("Frenado progresivo. Evitar obstaculo")
    elif dat_sensor_distancia >= 20:
        print("Frenado normal. Evitar obstaculo")    

def ajustar_velocidad(dat_camara_trafico, dat_sensor_velocidad):

    VELOCIDAD_MAX_TRAFICO_BAJO = 120
    VELOCIDAD_MAX_TRAFICO_MEDIO = 60
    VELOCIDAD_MAX_TRAFICO_ALTO = 30

    if dat_camara_trafico == "Bajo":
        if dat_sensor_velocidad < VELOCIDAD_MAX_TRAFICO_BAJO:
            print()
            print("Tráfico bajo: Aumentando velocidad progresivamente.")
        else:
            print(f"Tráfico bajo: Velocidad óptima alcanzada ({VELOCIDAD_MAX_TRAFICO_BAJO} km/h).")

    elif dat_camara_trafico == "Medio":
        if dat_sensor_velocidad > VELOCIDAD_MAX_TRAFICO_MEDIO:
            print(f"Tráfico medio: Reduciendo velocidad a {VELOCIDAD_MAX_TRAFICO_MEDIO} km/h.")
        elif dat_sensor_velocidad < VELOCIDAD_MAX_TRAFICO_MEDIO:
            print("Tráfico medio: Manteniendo velocidad actual.")
        else:
            print(f"Tráfico medio: Velocidad óptima ({VELOCIDAD_MAX_TRAFICO_MEDIO} km/h).")

    elif dat_camara_trafico == "Alto":
        if dat_sensor_velocidad > VELOCIDAD_MAX_TRAFICO_ALTO:
            print(f"Tráfico alto: Reduciendo velocidad a {VELOCIDAD_MAX_TRAFICO_ALTO} km/h.")
        else:
            print("Tráfico alto: Velocidad bajo control.")

# Sistema principal

dat_camara_trafico, dat_sensor_distancia, dat_sensor_velocidad = datos_sensor_camara()
ruta_optima(dat_camara_trafico)
evitar_obstaculo(dat_sensor_distancia)
ajustar_velocidad(dat_camara_trafico, dat_sensor_velocidad) 