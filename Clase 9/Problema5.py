import numpy as np

# 1. Definir los puntos originales (un cuadrado de 3x3)
# Cada fila es un punto [x, y]
puntos = np.array([
    [2, 2], [3, 2], [4, 2],
    [2, 3],         [4, 3],
    [2, 4], [3, 4], [4, 4]
])

def dibujar_en_consola(puntos_a_dibujar, titulo):
    """Crea un plano cartesiano de texto para ver la posición de los puntos"""
    print()
    print(f"--- {titulo} ---")
    # Creamos un plano vacío de 15x15
    plano = np.full((15, 15), " . ")
    
    for p in puntos_a_dibujar:
        x, y = int(p[0]), int(p[1])
        # Verificamos que el punto esté dentro del rango del plano para no dar error
        if 0 <= x < 15 and 0 <= y < 15:
            plano[y, x] = " @ "  # Dibujamos el punto
            
    # Imprimir el plano (invertido para que el eje Y crezca hacia arriba)
    for fila in reversed(plano):
        print("".join(fila))

# 2. Definir una Matriz de Transformación
# Ejemplo: Escalado (multiplicar el tamaño por 2)
matriz_escalado = ([
    [2, 0],
    [0, 2]
])

# Ejemplo: Traslación (mover 5 unidades en X y 2 en Y)
vector_traslacion = ([5, 2])

# --- EJECUCIÓN ---

# Dibujar estado original
dibujar_en_consola(puntos, "PUNTOS ORIGINALES (CUADRADO)")

# APLICAR TRANSFORMACIÓN 1: Escalado
# Multiplicamos la matriz de puntos por la matriz de transformación
puntos_escalados = puntos @ matriz_escalado
dibujar_en_consola(puntos_escalados, "PUNTOS ESCALADOS (DOBLE TAMAÑO)")

# APLICAR TRANSFORMACIÓN 2: Traslación
# Simplemente sumamos el vector de movimiento a cada punto
puntos_trasladados = puntos + vector_traslacion
dibujar_en_consola(puntos_trasladados, "PUNTOS TRASLADADOS (+5 en X, +2 en Y)")