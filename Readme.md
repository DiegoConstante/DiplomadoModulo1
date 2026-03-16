# Reto 2

## Descripción

Sistema para gestionar nuevos pedidos, editar y eliminar pedidos, al igual que gestionar productos con las mismas opciónes

## Estructura General

- Lista productos

ID | Producto | cantidad | precio

productos = [[ 1, "Producto 1", 10 , 5.99], ... ]

- Lista Pedidos

ID | Nombre cliente | Hora | producto | cantidad

productos = [[ 2, "Saul Rubio", datetime.now().strftime('%d-%m-%y %H:%M:%S'), "Producto 2", 5], ... ]

## Función | Procedimiento

## 1. Productos

### regNuevoProducto()
Esta función registra un nuevo producto o aumenta la cantidad de uno existente en el inventario. Solicita al usuario el nombre, el precio y la cantidad del producto, y luego verifica si el producto ya existe en el inventario.

Si existe, actualiza la cantidad.

Si no, agrega un nuevo producto al inventario.

Una vez completada la operación, muestra un mensaje de confirmación y los detalles del producto registrado.

### editProducto()
Esta función permite al usuario editar un producto específico. La función primero solicita al usuario que ingrese el ID del producto que desea editar, Luego, recorre una lista de inventario y verifica si el ID ingresado coincide con alguno.

Si encuentra una coincidencia, la función presenta un menú de opciones: editar el nombre del producto, editar el precio o la cantidad, Según la opción elegida, la función modifica el campo correspondiente en el producto. Si el usuario ingresa una opción no válida, se imprime un mensaje de error, Una vez realizada la edición, la función imprime un mensaje de éxito y muestra el producto actualizado.

Si no se encuentra ningún producto, se imprime un mensaje de error.

###eliminarProducto()
La función primero solicita al usuario que ingrese el ID del producto que desea eliminar.

Luego, recorre la lista de inventario y verifica si el ID de cada pedido coincide con el ingresado por el usuario. Si se encuentra una coincidencia, el producto se elimina de la lista mediante el método (pop()) y se imprime un mensaje de éxito.

Si no se encuentra ninguna coincidencia, se imprime un mensaje de error que indica que el producto no se encontró.

### listadoProductos()
Esta función imprime una lista de productos, itera sobre la lista de inventario y para cada producto, imprime el ID del producto, el nombre, el stock y el precio.

## 2. Pedidos

### regNuevoPedido()
Estafunción verifica si el producto existe en el inventario y si la cantidad solicitada no excede el stock disponible.

Si se cumplen las condiciones, la función resta la cantidad solicitada del inventario, registra el pedido e imprime un mensaje de éxito con los detalles del pedido.

Si no se cumplen las condiciones, se muestra un mensaje de error, al igual que si el producto no existe en el inventario, también se muestra un mensaje de error.

### editPedido()
Esta función permite al usuario editar un pedido específico. La función primero solicita al usuario que ingrese el ID del pedido que desea editar, Luego, recorre una lista de pedidos y verifica si el ID ingresado coincide con alguno.

Si encuentra una coincidencia, la función presenta un menú de opciones: editar el nombre del cliente, editar el producto o editar la cantidad, Según la opción elegida, la función modifica el campo correspondiente en el pedido. Si el usuario ingresa una opción no válida, se imprime un mensaje de error, Una vez realizada la edición, la función imprime un mensaje de éxito y muestra el pedido actualizado.

Si no se encuentra ningún pedido, se imprime un mensaje de error.

### eliminarPedido()
La función primero solicita al usuario que ingrese el ID del pedido que desea eliminar.

Luego, recorre la lista de pedidos y verifica si el ID de cada pedido coincide con el ingresado por el usuario. Si se encuentra una coincidencia, el pedido se elimina de la lista mediante el método (pop()) y se imprime un mensaje de éxito.

Si no se encuentra ninguna coincidencia, se imprime un mensaje de error que indica que el pedido no se encontró.

### listadoPedidos()
  Esta función imprime una lista de pedidos, itera sobre la lista pedidos y para cada pedido, imprime el ID del pedido, el nombre del cliente, la hora, el producto y la cantidad.

# Ejemplo de ejecución del sistema

========== GESTIÓN DE PEDIDOS ==========

1 = Registrar nuevo pedido

2 = Modificar pedido

3 = Eliminar pedido

4 = Listado de pedidos

========== GESTIÓN DE PRODUCTOS ==========
5 = Registrar nuevo producto
6 = Modificar producto
7 = Eliminar producto
8 = Listado de productos

9 = Salir
Ingrese una opció: 1

================================================== REGISTRAR NUEVO PEDIDO ==================================================

Nombre del cliente: Alex
Nombre del producto: Producto 1
Cantidad del producto salientes: 3

----------Pedido registrado con exito.----------

ID: 4 | Cliente: Alex | Hora: 16-03-26 15:49:16 | Producto: Producto 1 | Cantidad: 3

Desea utilizar otra opción? (S/N): s

========== GESTIÓN DE PEDIDOS ==========

(Opciones del menu)

Ingrese una opció: 2

================================================== EDITAR PEDIDO ==================================================

ID del pedido: 2

1 = Editar nombre del cliente
2 = Editar producto
3 = Editar cantidad

Opcion: 3
Nueva cantidad del producto saliente: 2

----------Pedido modificado con exito.----------

ID: 2 | Cliente: Saul Rubio | Hora: 16-03-26 15:49:07 | Producto: Producto 2 | Cantidad: 2

Desea utilizar otra opción? (S/N): s

========== GESTIÓN DE PEDIDOS ==========

(Opciones del menu)

Ingrese una opció: 3

================================================== ELIMINAR PEDIDO ==================================================

ID del pedido: 2

----------Pedido eliminado con exito.----------

Desea utilizar otra opción? (S/N): s

========== GESTIÓN DE PEDIDOS ==========

(Opciones del menu)

Ingrese una opció: 4

ID: 1 | Cliente: Diego Constante | Hora: 16-03-26 15:49:07 | Producto: Producto 1 | Cantidad: 10
ID: 3 | Cliente: Miguel Angel | Hora: 16-03-26 15:49:07 | Producto: Producto 3 | Cantidad: 15
ID: 4 | Cliente: Alex | Hora: 16-03-26 15:49:16 | Producto: Producto 1 | Cantidad: 3

Desea utilizar otra opción? (S/N): N
