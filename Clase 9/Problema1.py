# Análisis de Fuerzas en una Estructura
# Leyes de la Estática aplicadas a una matriz 3x3

# REPRESENTACIÓN DE LA ESTRUCTURA
# Cada celda [fila][columna] representa la fuerza aplicada (N)
# en ese nodo de la estructura. Valores positivos = hacia abajo
# Valores negativos = hacia arriba (reacción o fuerza inversa)

# Matriz de fuerzas aplicadas (en Newtons)
estructura = [
    [120,  -80,  200],   # Fila 0 (nodos superiores)
    [-50,  150,  -30],   # Fila 1 (nodos intermedios)
    [300,  -100, 250]    # Fila 2 (nodos inferiores)
]

FILAS    = 3
COLUMNAS = 3


# Funciones de análisis de la estructura
def mostrarEstructura(matriz):
    #Imprime la matriz de fuerzas en formato visual de tabla.

    print()
    print(f"  {'Nodo':>6}  |  Col 0  |  Col 1  |  Col 2  ")
    print("  " + "-" * 38)
    for i in range(FILAS):
        fila_str = f"  Fila {i}  |"
        for j in range(COLUMNAS):
            fila_str += f"  {matriz[i][j]:>5}N |"
        print(fila_str)
    print()


# Función que calcula la fuerza de reacción de un nodo individual en una estructura.
def reaccionPorNodo(fila, col):
    
    # Calcula la reacción de un nodo individual.
    # Según la estática: la reacción es igual y opuesta a la fuerza aplicada.
    return -estructura[fila][col]


def fuerzaResultantePorFila(fila):
 
    # Suma vectorial de fuerzas a lo largo de una fila (eje horizontal).
    # Eje X: equilibrio → ΣFx = 0, por lo que la reacción = -suma de fuerzas.
    suma = 0
    for j in range(COLUMNAS):
        suma += estructura[fila][j]
    return suma


def fuerzaResultantePorColumna(col):
  
    # Suma vectorial de fuerzas a lo largo de una columna (eje vertical).
    # Eje Y: equilibrio → ΣFy = 0, por lo que la reacción = -suma de fuerzas.
    suma = 0
    for i in range(FILAS):
        suma += estructura[i][col]
    return suma


def fuerzaTotalSistema():

    # Suma total de todas las fuerzas aplicadas en la estructura.
    total = 0
    for i in range(FILAS):
        for j in range(COLUMNAS):
            total += estructura[i][j]
    return total


def calcularReacciones():
    """
    Construye y devuelve la matriz de reacciones nodales.
    Reacción en cada nodo = fuerza opuesta (ΣF = 0 → equilibrio).
    """
    reacciones = []
    for i in range(FILAS):
        fila_reacciones = []
        for j in range(COLUMNAS):
            fila_reacciones.append(reaccionPorNodo(i, j))
        reacciones.append(fila_reacciones)
    return reacciones


def verificarEquilibrio():
    """
    Verifica la condición de equilibrio estático global.
    Si ΣF_total = 0 la estructura está en equilibrio.
    La reacción global del apoyo compensa la fuerza neta.
    """
    total = fuerzaTotalSistema()
    return total == 0, total



# Sistema principal

print()
print(("=" * 10), "ANÁLISIS DE FUERZAS EN UNA ESTRUCTURA 3x3", ("=" * 10))

# 1. Mostrar fuerzas aplicadas
print()
print(("-" * 5), "Fuerzas Aplicadas en los Nodos (N)", ("-" * 5))
mostrarEstructura(estructura)

# 2. Resultante por fila (eje horizontal)
print(("-" * 5), "Resultante de Fuerzas por Fila (ΣFx)", ("-" * 5))
print()
for i in range(FILAS):
    resultante = fuerzaResultantePorFila(i)
    reaccion_fila = -resultante
    print(f"  Fila {i}: ΣFx = {resultante}N  ->  Reacción de apoyo = {reaccion_fila}N")
print()

# 3. Resultante por columna (eje vertical)
print(("-" * 5), "Resultante de Fuerzas por Columna (ΣFy)", ("-" * 5))
print()
for j in range(COLUMNAS):
    resultante = fuerzaResultantePorColumna(j)
    reaccion_col = -resultante
    print(f"  Columna {j}: ΣFy = {resultante}N  ->  Reacción de apoyo = {reaccion_col}N")
print()

# 4. Matriz de reacciones nodales
print(("-" * 5), "Matriz de Reacciones Nodales (N)", ("-" * 5))
reacciones = calcularReacciones()
mostrarEstructura(reacciones)

# 5. Fuerza total del sistema
print(("-" * 5), "Fuerza Total del Sistema", ("-" * 5))
print()
total = fuerzaTotalSistema()
reaccion_global = -total
print(f"  ΣF total aplicada   = {total}N")
print(f"  Reacción global     = {reaccion_global}N")
print()

# 6. Verificación de equilibrio
print(("-" * 5), "Verificación de Equilibrio Estático (ΣF = 0)", ("-" * 5))
print()
en_equilibrio, suma = verificarEquilibrio()
if en_equilibrio:
    print("  ✅ La estructura está en EQUILIBRIO ESTÁTICO (ΣF = 0)")
else:
    print(f"  ⚠️  La estructura NO está en equilibrio.")
    print(f"     Fuerza neta resultante = {suma}N")
    print(f"     Se requiere una reacción de apoyo de {-suma}N para lograr equilibrio.")
print()
print(("=" * 62))