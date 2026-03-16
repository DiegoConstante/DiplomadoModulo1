# Problema 1 - Control de Temperatura en un Edificio Inteligente.

## Descripción

Sistema para optimizar el consumo energético ajustando temperaturas según hora, ocupación y clima externo.

## Estructura general

### Función

1. datos_sensor()
   Simula entrada de datos

2. calcular_tem_optima(hora, clima, ocupacion)
   Calcula temperatura ideal

3. consumo_energetico(temp_optima)
   Evalúa consumo temp_optima

### Procedimiento

1. ajustar_temperatura(temperatura, temp_optima, zona)
   Ajusta la temperatura actual

## Funciones - procedimientos

### datos_sensor()

Función para leer los datos de sensores de temperatura de las diferentes zonas del edificio.

### calcular_tem_optima()

Función para calcular la temperatura optima en cada zona del edificio, teniendo en cuenta la hora, clima y ocupación.

### ajustar_temperatura()

Procedimiento para aumentar o disminuir la temperatura según los valores de la función anterior.

### consumo_energetico()

Función para calcular en consumo energético

# Problema 2 - Gestión de Inventario en un Almacén

## Descripción

Sistema para gestionar entrada y salida de productos y optimizar el reabastecimiento de los mismo minimizando exceso de inventario

## Estructura General

- Lista productos para simular BDD

  Producto | Precio | cantidad

productos = [
["Producto 1", 10.99, 80],
["Producto 2", 9.99, 40],
["Producto 3", 8.99, 60],
["Producto 4", 7.99, 20],
["Producto 5", 6.99, 70]
]

### Función

1. entrada_productos()
   Simula entrada de productos

2. salida_productos()
   Simular salida de productos

3. alerta_stock()
   Generar alertas de stock

### Procedimiento

1. inventario_optimo(productos)
   Calcular inventario optimo

## Funciones - procedimientos

### entrada_productos()

Función para registrar nuevos productos o aumentar la cantidad de productos ya existentes y añadirlos a la lista productos[]

### salida_productos()

Función para registrar salida de productos restando la cantidad del mismo

### inventario_optimo()

Función para calcular el inventario optimo de los productos en la lista en caso de haber alguno con poco stock

### alerta_stock()

Función que muestra una alerta en caso de que un producto exceda el límite mínimo de stock

# Problema 3 - Sistema de Navegación para un Vehículo Autónomo

## Descripción

Sistema de navegación para un vehículo autónomo que planifique rutas, evite obstáculos y optimice el tiempo de viaje.

## Estructura general

### Función

1. datos_sensor_camara()
   Simula datos de cámara y sensores

2. evitar_obstaculo(dat_sensor_distancia)
   Decide frenado por distancia

3. ajustar_velocidad(dat_camara_trafico, dat_sensor_velocidad)
   Ajusta velocidad por tráfico

### Procedimiento

1. ruta_optima(dat_camara_trafico)  
   Selecciona ruta según tráfico

## Funciones - procedimientos

### datos_sensor_camara()

Función principal para obtener datos simulados de sensores.

Pide al usuario: nivel de tráfico ("Alto", "Medio", "Bajo"), distancia al obstáculo (en metros) y velocidad actual (km/h).

### ruta_optima()

Evalúa el nivel de tráfico y selecciona la ruta óptima:

### evitar_obstaculo()

Analiza la distancia al obstáculo y activa frenado:

### ajustar_velocidad()

Define límites máximos: 90 km/h (Bajo), 70 km/h (Medio), 50 km/h (Alto) y los ajusta según el tráfico.

# Problema 4 - Optimización de la Producción en una Fábrica

## Descripción

Sistema que optimiza el proceso de producción en una fábrica, minimizando el tiempo de inactividad y maximizando la eficiencia de sus máquinas.

## Estructura general

### Función

1. estadoMaquina(horas_uso)
   Determina estado técnico de máquina (Bueno, Regular, Malo)

### Procedimiento

1. mantenimientoMaquina()
   Genera alertas de mantenimiento preventivo o urgente

2. nivelRendimiento()
   Muestra rendimiento máquinas según sus horas de uso

3. nivelProduccion()
   Calcula producción óptima

## Funciones - procedimientos

### estadoMaquina(horas_uso)

Función auxiliar que clasifica estado máquina según horas uso

Retorna: "Bueno", "Regular", "Malo"

### mantenimientoMaquina()

Procedimiento recorre lista maquinas[] evaluando cada máquina

Clasifica por rangos horas:
<= 10000h (nuevo ✅)
10000-40000h (casi nuevo ✅)
40000-87000h (preventivo 🛠️)
87000-90000h (prioritario 🛠️)
90000h (urgente 🔴)

### nivelRendimiento()

Procedimiento muestra tabla completa de todas las máquinas

### nivelProduccion()

Procedimiento pide ventas estimadas e inventario actual

Calcula producción necesaria: ventas_estimadas - inventario_actual

Distribuye carga: +20% máquinas <10000h, normal ≤80000h, -10% >80000h

Actualiza rendimientos en maquinas[] y muestra ajustes

# Problema 5 - Sistema de Riego Automatizado para Agricultura

## Descripción

Sistema de riego automatizado que optimiza el uso de agua en función de las condiciones del suelo, las previsiones meteorológicas

## Estructura General

### Función

1. leer_humedad_suelo()
   Simula sensor humedad suelo

2. consultar_clima()
   Obtiene previsión meteorológica

3. calcular_riego(humedad, clima)
   Calcula cantidad óptima riego

### Procedimiento

1. controlar_valvulas(zona_riego)
   Activa/desactiva válvulas

## Funciones - procedimientos

### leer_humedad_suelo()

Función para simular lectura sensor humedad (0-100%), solicita al usuario valor entre 20%-80%

### consultar_clima()

Función para simular previsión meteorológica ("Soleado", "Nublado", "Lluvia")

### calcular_riego(humedad, clima)

Función calcula el riego optimo según clima y humedad del suelo

### controlar_valvulas(zona_riego)

Procedimiento calcula el estado de las válvulas según la función:

calcular_riego()

define si la válvula se abre o se cierra
