# Clase 9.

## Problema 1 - Análisis de Fuerzas en una Estructura.

### Solución.

El código modela una estructura como una matriz 3x3 de fuerzas, donde cada valor representa una fuerza aplicada en un nodo. A partir de esta matriz, el programa:

- Calcula las reacciones en cada nodo (fuerzas opuestas).

- Obtiene las fuerzas resultantes por filas y columnas.

- Calcula la fuerza total del sistema.

- Verifica si la estructura cumple con la condición de equilibrio estático (ΣF = 0).

básicamente, simula el comportamiento básico de una estructura aplicando principios de la estática.

### Enfoque.

El enfoque del código es modular y basado en descomposición del problema, lo que significa que se divide el problema en funciones más pequeñas y específicas como:

- Cálculo por nodo.

- Suma total del sistema.

- Verificación de equilibrio.

El uso de este enfoque influye en la eficiencia ya que permite:

- Recorrido estructurado de datos.

- Modularidad.

- Cálculo directo.

- Escalabilidad sencilla.

## Problema 2 - Simulación de Fluido en una Cuadrícula 3D.

### Solución.

El código simula el comportamiento de un fluido dentro de una cuadrícula 3D (3x3x3), donde cada celda contiene:

- Presión.

- Temperatura.

- Velocidad.

El sistema inicializa el fluido con valores base, aplica una perturbación de presión en el centro (como una onda o impulso), propaga esa perturbación a través del volumen en varios pasos y muestra cómo evolucionan los valores del fluido con el tiempo.

### Enfoque

El enfoque es numérico y basado en simulación discreta, específicamente en el uso de una matriz tridimensional (arreglo 3D) para representar el espacio.

- Aplicación de un modelo de difusión:
  Cada celda se actualiza en función del promedio de sus vecinos.

- Uso de actualización simultánea:
  Se crea una nueva cuadrícula para evitar errores al modificar valores en el mismo paso.

- Separación en funciones:
  Inicialización.

Cálculo de vecinos.

Actualización de celdas.

Propagación de la onda.

permitiendo de esta manera un codigo mas simple y al igual que el problema anterior el código es modular por lo que:

- Las funciones estan separadas para cada tarea.

- Facilita el mantenimiento.

- Permite a escalar a volumenes mas grandes.

## Problema 3 - Análisis de Imágenes Médicas en 3D

### Solución

Este código implementa una simulación sencilla de procesamiento de imágenes en un entorno tridimensional, representado mediante un volumen de datos creado con la librería NumPy. El volumen está compuesto por tres capas de 10x10, donde cada valor representa la intensidad de un “píxel”. Inicialmente, todos los valores se establecen en cero, simulando una imagen completamente oscura, y luego se introducen manualmente algunos valores altos en posiciones específicas para representar ruido o puntos brillantes aislados.

### Enfoque

El enfoque se basa en un filtro de promedio, una técnica común en procesamiento de imágenes. Este método recorre la matriz y, para cada píxel (excepto los bordes), calcula el promedio de los valores dentro de una ventana de 3x3 que lo rodea. De esta forma, el valor de cada píxel se reemplaza por uno más representativo de su entorno.

- Se trabaja con ventanas pequeñas (3x3).

- Se evita modificar la matriz original directamente.

- Se aplica un método determinista y fácil de entender.

Este enfoque es eficiente porque utiliza operaciones simples como sumas y promedios, lo que reduce el costo computacional. Al trabajar con ventanas pequeñas, el número de cálculos por píxel es constante, lo que permite que el algoritmo escale de forma predecible a imágenes más grandes.

- Bajo costo computacional por píxel.

- Buen rendimiento incluso si aumenta el tamaño de la imagen.

- Código claro y fácil de mantener.

## Problema 4 - Manejo de Datos en una Tabla de Sensores

### Solución

El programa permite visualizar los datos registrados, así como obtener información estadística relevante tanto por sensor como por instante de tiempo. Además, incluye un resumen global que proporciona una visión general del comportamiento de las temperaturas registradas, lo que ayuda a identificar tendencias, valores extremos o posibles anomalías.

### Enfoque

El código está dividido en funciones específicas, cada una encargada de una tarea concreta, como mostrar los datos o calcular estadísticas. Este enfoque modular facilita la comprensión del programa y permite reutilizar o modificar partes del código sin afectar el resto del sistema.

- Se utiliza una estructura tipo matriz para organizar los datos.

- Se aplican funciones estadísticas como promedio y desviación estándar.

- Se separa el análisis por sensor, por tiempo y a nivel global.

El uso de funciones de NumPy mejora significativamente la eficiencia del programa, ya que estas están optimizadas para trabajar con arreglos numéricos. Esto permite realizar cálculos como promedios, mínimos, máximos y desviaciones estándar de forma rápida y precisa, incluso si el volumen de datos aumenta.

## Problema 5 - Transformación de Coordenadas en un Sistema Cartesiano

### Solución

El programa permite visualizar los puntos antes y después de aplicar transformaciones. Primero se dibuja la figura original en una cuadrícula de texto, y luego se aplican dos transformaciones: un escalado (que aumenta el tamaño de la figura) y una traslación (que desplaza la figura en el plano). Cada resultado se muestra en consola, lo que facilita observar cómo cambian las posiciones de los puntos.

### Enfoque

El enfoque utilizado se basa en el uso de transformaciones matriciales, un método fundamental en geometría computacional y gráficos por computadora. En este caso, los puntos se representan como una matriz, lo que permite aplicar operaciones matemáticas de forma directa y eficiente.

Este enfoque aprovecha la capacidad de trabajar con operaciones vectorizadas, evitando el uso de ciclos explícitos para transformar cada punto individualmente. Además, la visualización en consola mediante una cuadrícula permite interpretar fácilmente los resultados.

- Uso de matrices para representar puntos.

- Aplicación de transformaciones mediante operaciones matemáticas.

- Visualización simple en un plano de texto.
