# Control de Temperatura en un Edificio Inteligente

# Funcion para obtener los datos del sensor
def datos_sensor():

    print("========== SISTEMA DE CONTROL DE TEMPERATURA ==========")

    # Entrada de Datos
    zona = input("Zona del edificio: ")
    ocupacion = int(input("ocupacion actual (%): "))
    temperatura = float(input("Temperatura actual: "))
    hora = int(input("Hora actual (6-18): "))
    clima = input("clima actual (Soleado, Nublado, Lluvioso): ")

    return zona, ocupacion, temperatura, hora, clima


def calcular_tem_optima( hora, clima, ocupacion):

    temp_optima = 22

    if clima == "Soleado" and 6 <= hora <= 12 and ocupacion <= 50:
        temp_optima: float = 25
    elif clima == "Soleado" and 6 <= hora <= 12 and ocupacion > 50:
        temp_optima: float = 23
    elif clima == "Soleado" and 13 <= hora <= 18 and ocupacion <= 50:
        temp_optima: float = 13
    elif clima == "Soleado" and 13 <= hora <= 18 and ocupacion > 50:
        temp_optima: float = 10
    elif (clima == "Nublado" or clima == "Lluvioso") and 6 <= hora <= 12 and ocupacion <= 50:
        temp_optima: float = 28
    elif (clima == "Nublado" or clima == "Lluvioso") and 6 <= hora <= 12 and ocupacion > 50:
        temp_optima: float = 25
    elif (clima == "Nublado" or clima == "Lluvioso") and 13 <= hora <= 18 and ocupacion <= 50:
        temp_optima: float = 22
    elif (clima == "Nublado" or clima == "Lluvioso") and 13 <= hora <= 18 and ocupacion > 50:
        temp_optima: float = 20

    return temp_optima

def ajustar_temperatura(temperatura, temp_optima, zona):

    print("========== AJSUTE DE TEMPERATURA ==========")

    if temperatura < temp_optima:
        print()
        print("Activar calefaccion en: ", zona)
        print("Temperatura optima: ", temp_optima, "°C  |  Temperatura actual: ", temperatura, "°C")
        print()
    elif temperatura > temp_optima:
        print()
        print("Activar la refrigeracion en: ", zona)
        print("Temperatura optima: ", temp_optima, "°C  |  Temperatura actual: ", temperatura, "°C")
        print()
    else:    
        print()
        print("Temperatura adecuada")
        print()


def consumo_energetico(temperatura):

    print("========== CONSUMO ENERGETICO ==========")

    if temperatura < 15:
        consumo = "Bajo"
        print()
    elif 15 <= temperatura <= 25:
        consumo = "Normal"
        print()
    elif temperatura > 25:
        consumo = "Alto"
        print()

    return consumo


zona, ocupacion, temperatura, hora, clima = datos_sensor()
temp_optima = calcular_tem_optima(hora, clima, ocupacion)
ajustar_temperatura(temperatura, temp_optima, zona)
consumo = consumo_energetico(temperatura)
print(f"El consumo energetico es: {consumo}")
print()