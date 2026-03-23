# Manejo de Datos en una Tabla de Sensores
 
import numpy as np
 
# Tabla de temperaturas 5x5
# Filas = momentos en el tiempo | Columnas = sensores
 
datos = ([22.1, 21.8, 23.5, 20.9, 22.4],
         [23.0, 22.5, 24.1, 21.5, 23.0],
         [24.5, 23.8, 26.0, 22.8, 24.5],
         [23.8, 23.1, 25.2, 22.0, 23.9],
         [22.9, 22.4, 24.8, 21.3, 23.2]
         )
 
sensores = ["Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4", "Sensor 5"]
tiempos  = ["08:00", "10:00", "12:00", "14:00", "16:00"]
 
 
def mostrarTabla():
    print("Temperaturas registradas (°C):")
    for i in range(5):
        for j in range(5):
            print(f"  {tiempos[i]} | {sensores[j]}: {datos[i][j]}°C")
        print()
 
 
def estadisticasPorSensor():
    print("Estadísticas por Sensor:")
    for j in range(5):
        prom = np.mean(datos[j])
        desv = np.std(datos[j], ddof=1)
        print(f"  {sensores[j]} -> Promedio: {prom:.2f}°C | Desv. estándar: {desv:.2f}°C")
    print()
 
 
def estadisticasPorTiempo():
    print("Estadísticas por Momento en el Tiempo:")
    for i in range(5):
        prom = np.mean(datos[i])
        desv = np.std(datos[i], ddof=1)
        print(f"  {tiempos[i]} -> Promedio: {prom:.2f}°C | Desv. estándar: {desv:.2f}°C")
    print()
 
 
def resumenGlobal():
    print("Resumen Global:")
    print(f"  Mínima   : {np.min(datos):.2f}°C")
    print(f"  Máxima   : {np.max(datos):.2f}°C")
    print(f"  Promedio : {np.mean(datos):.2f}°C")
    print(f"  Mediana  : {np.median(datos):.2f}°C")
    print(f"  Desv. Est: {np.std(datos, ddof=1):.2f}°C")
    print()

 
# Sistema principal
 
print()
print(("=" * 10), "MANEJO DE DATOS EN UNA TABLA DE SENSORES", ("=" * 10))
print()
 
mostrarTabla()
estadisticasPorSensor()
estadisticasPorTiempo()
resumenGlobal()