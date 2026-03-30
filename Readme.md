# Sistema de Gestión de Inventario y Pedidos (Optimizado)

Este proyecto es una solución desarrollada para el Reto 3 de la Clase 15, enfocada en la optimización de un sistema de gestión comercial. El sistema permite administrar productos en un inventario y procesar pedidos de clientes en tiempo real, asegurando la integridad de los datos de stock.

## Funcionalidades Implementadas

### 1. Gestión de Inventario (Clase Productos)

- Visualización: Listado detallado de productos con ID, nombre, stock actual y precio.

- Registro inteligente: Permite añadir nuevos productos. Si el nombre ya existe, el sistema actualiza automáticamente el stock en lugar deduplicar la entrada.

- Edición selectiva: Modificación de campos específicos (nombre, precio o stock) mediante el ID del producto.

- Eliminación: Remoción de productos del catálogo por ID.

### 2. Gestión de Pedidos (Clase Pedidos)

- Registro con Validación: Al crear un pedido, el sistema verifica la existencia del producto y la disponibilidad de stock. Si es exitosodescuenta automáticamente las unidades del inventario.

- Cola de Atención: Los pedidos se almacenan siguiendo el orden de llegada.

- Edición Dinámica: Permite cambiar el cliente o la cantidad solicitada. Si se cambia la cantidad, el sistema reajusta el stock del inventario(devuelve el stock anterior y descuenta el nuevo).

- Cancelación de Pedidos: Elimina pedidos de la cola y permite gestionar la salida sin perder el orden de los demás registros.

## Estructuras de Datos Utilizadas

1. list (Listas de Python)

Uso: Almacenamiento de la base de datos de productos (lista_productos).

Justificación: Se utiliza una lista de listas porque el acceso a los productos para edición y eliminación es frecuente a través de iteraciones. Permite mantener un orden secuencial y es flexible para agregar o quitar elementos mediante índices o filtros.

2. collections.deque (Double-Ended Queue)Uso

Manejo de la fila de pedidos (cola_pedidos).

Justificación: Un pedido representa un proceso que debe ser atendido en orden. deque es mucho más eficiente que una lista convencional para
operaciones de "cola" (FIFO - First In, First Out).

Permite usar el método .popleft() para despachar pedidos y .rotate() para eliminar elementos específicos sin necesidad de reconstruir toda la
lista en memoria, optimizando la complejidad temporal a O(1) en operaciones de extremos.

3. datetimeUso

Registro de la hora del pedido.Justificación: Proporciona trazabilidad temporal automática, esencial para cualquier sistema de auditoría o logística.
