# Simulación de Fluido en una Cuadrícula 3D
# Propagación de ondas de presión en un volumen 3x3x3
 
# ============================================================
# ESTRUCTURA DEL FLUIDO
# Arreglo tridimensional [x][y][z]
# Cada celda = [presion (Pa), temperatura (°C), velocidad (m/s)]
#              [  indice 0   ,    indice 1     ,   indice 2    ]
# ============================================================
 
TAMANIO    = 3
PASOS_SIM  = 5       # Número de iteraciones de la simulación
 
# Constantes físicas simplificadas del modelo
FACTOR_DIFUSION   = 0.15   # Qué tan rápido se propaga la presión a vecinos
FACTOR_TEMP       = 0.10   # Influencia de presión en temperatura
FACTOR_VEL        = 0.05   # Influencia de presión en velocidad
PRESION_BASE      = 101.3  # Presión atmosférica base (kPa)
TEMP_BASE         = 25.0   # Temperatura base (°C)
VEL_BASE          = 0.0    # Velocidad base (m/s)
 
 
# -----------------------------------------------------------
# Inicialización del fluido: arreglo 3D con listas anidadas
# Formato por celda: [presion, temperatura, velocidad]
# -----------------------------------------------------------
 
def inicializarFluido():
    # Crea la cuadrícula 3x3x3 con condiciones iniciales base.
    fluido = []
    for x in range(TAMANIO):
        capa_x = []
        for y in range(TAMANIO):
            fila_y = []
            for z in range(TAMANIO):
                # Celda: [presion, temperatura, velocidad]
                fila_y.append([PRESION_BASE, TEMP_BASE, VEL_BASE])
            capa_x.append(fila_y)
        fluido.append(capa_x)
    return fluido
 
 
def aplicarFuentePresion(fluido, x, y, z, magnitud):

    # Aplica una perturbación de presión en una celda específica.
    # Simula el origen de una onda (ej: golpe de ariete, explosión).
    fluido[x][y][z][0] += magnitud
    fluido[x][y][z][2] += magnitud * FACTOR_VEL   # La velocidad reacciona al impulso
 
 
# -----------------------------------------------------------
# Funciones de acceso y cálculo sobre el arreglo 3D
# -----------------------------------------------------------
 
def obtenerVecinos(x, y, z):

    # Devuelve las coordenadas de las celdas vecinas ortogonales.
    # Un nodo interior tiene hasta 6 vecinos (±x, ±y, ±z).
    # Los nodos en borde tienen menos vecinos (no se sale del cubo).
    vecinos = []
    for dx, dy, dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < TAMANIO and 0 <= ny < TAMANIO and 0 <= nz < TAMANIO:
            vecinos.append((nx, ny, nz))
    return vecinos
 
 
def presionPromedioVecinos(fluido, x, y, z):

    # Calcula la presión promedio de todas las celdas vecinas.
    # Base del modelo de diferencias finitas para difusión.
    vecinos = obtenerVecinos(x, y, z)
    if len(vecinos) == 0:
        return fluido[x][y][z][0]
 
    suma = 0
    for nx, ny, nz in vecinos:
        suma += fluido[nx][ny][nz][0]
    return suma / len(vecinos)
 
 
def actualizarCelda(fluido, nueva_cuadricula, x, y, z):
    
    # Actualiza los valores de una celda según la difusión de presión.
 
    # Modelo de propagación:
    #  - La nueva presión es un promedio ponderado entre la presión
    #    actual y la presión promedio de sus vecinos (difusión).
    #  - La temperatura sube levemente si hay alta presión (gas ideal).
    #  - La velocidad se actualiza por el gradiente de presión local.
    presion_actual   = fluido[x][y][z][0]
    temp_actual      = fluido[x][y][z][1]

    vel_actual       = fluido[x][y][z][2]
 
    p_vecinos        = presionPromedioVecinos(fluido, x, y, z)
 
    # Difusión: la presión de la celda tiende hacia el promedio de vecinos
    nueva_presion    = presion_actual + FACTOR_DIFUSION * (p_vecinos - presion_actual)
 
    # Relación presión-temperatura (gas ideal simplificado: T ∝ P)
    delta_presion    = nueva_presion - presion_actual
    nueva_temp       = temp_actual + FACTOR_TEMP * delta_presion
 
    # La velocidad se genera por diferencia de presión (gradiente)
    nueva_vel        = vel_actual + FACTOR_VEL * abs(p_vecinos - presion_actual)
 
    nueva_cuadricula[x][y][z][0] = round(nueva_presion, 2)
    nueva_cuadricula[x][y][z][1] = round(nueva_temp, 2)
    nueva_cuadricula[x][y][z][2] = round(nueva_vel, 4)
 
 
def propagarOnda(fluido):
 
    # Ejecuta un paso completo de propagación sobre todo el volumen 3x3x3.
    # Se usa una cuadrícula auxiliar para no mezclar valores del mismo paso.
    # (Método de actualización simultánea — evita sesgo de orden de recorrido)

    # Crear copia profunda de la cuadrícula
    nueva = inicializarFluido()
 
    for x in range(TAMANIO):
        for y in range(TAMANIO):
            for z in range(TAMANIO):

                # Copiar valor actual antes de modificar
                nueva[x][y][z] = [
                    fluido[x][y][z][0],
                    fluido[x][y][z][1],
                    fluido[x][y][z][2]
                ]
 
    # Aplicar la difusión sobre la copia
    for x in range(TAMANIO):
        for y in range(TAMANIO):
            for z in range(TAMANIO):
                actualizarCelda(fluido, nueva, x, y, z)
 
    return nueva
 
 

# Procedimientos de visualización
def mostrarCapa(fluido, capa_x, propiedad, nombre_prop, unidad):
    """Muestra una capa (plano XY a z fijo) de una propiedad del fluido."""
    idx = {"presion": 0, "temperatura": 1, "velocidad": 2}[propiedad]
    print(f"  Capa X={capa_x} | {nombre_prop}")
    print(f"  {'':>8}  Col 0       Col 1       Col 2")
    print("  " + "-" * 40)
    for y in range(TAMANIO):
        fila = f"  Fila Y={y} |"
        for z in range(TAMANIO):
            val = fluido[capa_x][y][z][idx]
            fila += f"  {val:>7.2f}{unidad}"
        print(fila)
    print()
 
 
def mostrarEstadoCompleto(fluido, paso):
    """Muestra el estado de las 3 capas del fluido en un paso dado."""
    print()
    print(f"{'=' * 10} PASO {paso} {'=' * 10}")
    for x in range(TAMANIO):
        mostrarCapa(fluido, x, "presion",     "PRESIÓN (kPa)",    "kPa")
        mostrarCapa(fluido, x, "temperatura", "TEMPERATURA (°C)", "°C ")
        mostrarCapa(fluido, x, "velocidad",   "VELOCIDAD (m/s)",  "m/s")
    print("-" * 35)
 
 
def reporteResumen(fluido, paso):
    """Muestra solo un resumen rápido: mínimo, máximo y promedio de presión."""
    valores = []
    for x in range(TAMANIO):
        for y in range(TAMANIO):
            for z in range(TAMANIO):
                valores.append(fluido[x][y][z][0])
 
    minimo  = min(valores)
    maximo  = max(valores)
    promedio = sum(valores) / len(valores)
 
    print(f"  Paso {paso} → Presión mín: {minimo:.2f} kPa | "
          f"máx: {maximo:.2f} kPa | prom: {promedio:.2f} kPa")
 
 


# -----------------------------------------------------------
# Sistema principal
print()
print(("=" * 10), "SIMULACIÓN DE FLUIDO EN CUADRÍCULA 3D (3x3x3)", ("=" * 10))
 
# 1. Inicializar el fluido
fluido = inicializarFluido()
print()
print(("-" * 5), "Estado inicial del fluido", ("-" * 5))
mostrarEstadoCompleto(fluido, 0)
 
# 2. Aplicar fuente de perturbación (onda de presión en el nodo central)
print(("-" * 5), "Aplicando perturbación de presión en el nodo central [1][1][1]", ("-" * 5))
aplicarFuentePresion(fluido, 1, 1, 1, magnitud=50.0)   # +50 kPa en el centro
print(f"  Presión en [1][1][1] después del impulso: {fluido[1][1][1][0]:.2f} kPa")
print()
 
# 3. Simular propagación paso a paso
print(("-" * 5), "Simulación de propagación de onda", ("-" * 5))
print()
print("  Resumen de evolución de presión:")
reporteResumen(fluido, 0)
 
for paso in range(1, PASOS_SIM + 1):
    fluido = propagarOnda(fluido)
    reporteResumen(fluido, paso)
 
# 4. Estado final detallado
print()
print(("-" * 5), "Estado final del fluido (tras propagación)", ("-" * 5))
mostrarEstadoCompleto(fluido, PASOS_SIM)
 
print(("=" * 62))