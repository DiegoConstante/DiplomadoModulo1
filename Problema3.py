import numpy as np

# 1. Crear un volumen 3D (3 capas, 10 filas, 10 columnas)
# Llenamos con ceros y ponemos algunos "píxeles" con ruido (valores altos)
volumen = np.zeros((3, 10, 10))

# Añadimos ruido aleatorio en la Capa 0
volumen[0, 2, 2] = 8  # Un píxel muy brillante rodeado de oscuridad
volumen[0, 2, 3] = 7
volumen[0, 5, 5] = 9

def imprimir_capa_consola(capa, titulo):
    """Muestra la matriz en consola usando caracteres para que parezca imagen"""
    print(f"--- {titulo} ---")
    for fila in capa:
        # Si el valor es > 0, ponemos un caracter, si no, un espacio
        linea = "".join([" @ " if val > 1 else " . " for val in fila])
        print(linea)

def filtro_promedio_2d(capa):
    """Aplica un suavizado simple promediando cada píxel con sus vecinos"""
    alto, ancho = capa.shape
    nueva_capa = np.zeros((alto, ancho))
    
    for i in range(1, alto - 1):
        for j in range(1, ancho - 1):
            # Extraemos una ventana de 3x3 alrededor del píxel
            ventana = capa[i-1:i+2, j-1:j+2]
            # El nuevo valor es el promedio de esa ventana
            nueva_capa[i, j] = np.mean(ventana)
            
    return nueva_capa

# --- EJECUCIÓN ---

# Tomamos la primera capa del volumen médico
capa_original = volumen[0]

# Aplicamos el suavizado
capa_suavizada = filtro_promedio_2d(capa_original)

# Resultados
imprimir_capa_consola(capa_original, "IMAGEN ORIGINAL (CON RUIDO)")
imprimir_capa_consola(capa_suavizada, "IMAGEN SUAVIZADA (FILTRADA)")

print("Nota: El suavizado distribuye el valor del ruido entre los vecinos,")
print("haciendo que los puntos brillantes se 'difuminen'.")