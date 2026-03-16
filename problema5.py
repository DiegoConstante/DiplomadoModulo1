# Función para leer datos de sensores de humedad del suelo
def leer_humedad_suelo():
    # Simulación de sensor (0 a 100 % de humedad)
    print()
    humedad = int(input("Humedad del suelo (20% - 80%): "))
    return humedad


# Función para consultar las previsiones meteorológicas
def consultar_clima():
    # Simulación de previsión
    clima = input("Clima (Soleado, Nublado, Lluvia): ")
    return clima


# Procedimiento para calcular la cantidad óptima de riego
def calcular_riego(humedad, clima):

    # Base de riego según clima
    if clima == "Lluvia":
        riego_base = 0.5 
    elif clima == "Soleado":
        riego_base = 1.5 
    else:
        riego_base = 1.0 

    # Ajuste según humedad del suelo
    if humedad > 60:
        factor_humedad = 0.5 
    elif humedad < 40:
        factor_humedad = 2.0
    else:
        factor_humedad = 1.5

    riego = riego_base * factor_humedad
    return riego


# Función para controlar las válvulas de riego
def controlar_valvulas(zona_riego):

    print()
    print("========== CONTROL DE VALVULAS ==========")
    
    # Comprobación de zona de riego
    if zona_riego == "A" or zona_riego == "B" or zona_riego == "C" or zona_riego == "D":

        # Calculo de riego segun la humedad y clima de la zona ingresada
        riego = calcular_riego(humedad, clima)

        # Estado de las valvulas de riego
        if riego > 0:
            print()
            print("Valvula de riego abierta")
            print("Cantidad de riego:", riego, "litros")
        else:
            print()
            print("Valvula de riego cerrada")

    # Si la zona de riego ingresada no es alguna: (A, B, C, D)
    else:
        print
        print("Zona de riego no valida")

# Programa principal
humedad = leer_humedad_suelo()
clima = consultar_clima()

zona_riego = input("Zona de riego (A, B, C, D): ")

print()
print("========== INFORMACIÓN DE RIEGO ==========")
    
print()
print("Cantidad de riego recomendada:", calcular_riego(humedad, clima), "litros")

controlar_valvulas(zona_riego)
