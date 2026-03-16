# Uso de Arreglos Unidimensionales en la solución de problemas reales
from datetime import datetime

pedidos = [[1, "Diego Constante", datetime.now().strftime('%d-%m-%y %H:%M:%S'),  "Producto 1", 10],
           [2, "Saul Rubio", datetime.now().strftime('%d-%m-%y %H:%M:%S'),  "Producto 2", 5],
           [3, "Miguel Angel", datetime.now().strftime('%d-%m-%y %H:%M:%S'),  "Producto 3", 15],]



inventario = [[1, "Producto 1", 10, 5.99],
              [2, "Producto 2", 5, 9.99],
              [3, "Producto 3", 15, 8.99]]

# Función para registrar un nuevo producto o aumentar la cantidad del mismo
def regNuevoProducto():
    print()
    print(("=") * 50 + " REGISTRAR NUEVO PRODUCTOS " + ("=") * 50)

    # Entrada de Datos
    print()
    id_producto = len(inventario)
    producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto entrantes: "))

    # Verificar si el producto ya existe y suma, o agregar nuevo
    for i in range(len(inventario)):
        if inventario[i][1] == producto:
            inventario[i][2] += cantidad
            print(f"Stock actualizado: {inventario[i][2]} unidades de {producto}")
            break
    # Agregar nuevo producto a la lista de productos
    else:
        inventario.append([id_producto, producto, cantidad, precio])
        print()
        print(("-") * 10 + "Producto registrado con exito." + ("-") * 10)
        print()
        print(f"ID: {id_producto} | Producto: {producto}  | precio: {precio} | Cantidad: {cantidad}")

# Funció para registrar un nuevo pedido
def regNuevoPedido():

    print()
    print(("=") * 50 + " REGISTRAR NUEVO PEDIDO " + ("=") * 50)

    # Entrada de Datos
    print()
    id_pedido = len(pedidos) + 1
    cliente = input("Nombre del cliente: ")
    hora_registro = datetime.now().strftime('%d-%m-%y %H:%M:%S')
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad del producto salientes: "))

    # Verificar si el producto existe y veridica si la cantidad de salida no supera el stock disponible
    for i in range(len(inventario)):
        if inventario[i][1] == producto:
            encontrado = True
            if inventario[i][2] >= cantidad:
                inventario[i][2] -= cantidad
                # Si la cantidad de salida es menor al stock disponible, se registra el pedido
                print()
                print(("-") * 10 + "Pedido registrado con exito." + ("-") * 10)
                pedidos.append([id_pedido , cliente, hora_registro, producto, cantidad])
                print()
                print(f"ID: {id_pedido} | Cliente: {cliente} | Hora: {hora_registro} | Producto: {producto} | Cantidad: {cantidad}")
            else:
                # Si la cantidad de salida supera el stock disponible, se muestra un error y se detiene el proceso
                print()
                print(f"ERROR: Stock insuficiente. Disponible: {inventario[i][2]} | Solicitado: {cantidad}")
                break

    # Si el producto no existe, se muestra un error
    if not encontrado:
        print("ERROR: Producto no encontrado.")

# Función para editar un pedido
def editPedido():

    print()
    print(("=") * 50 + " EDITAR PEDIDO " + ("=") * 50)

    # Entrada de Datos
    print()
    id_pedido = int(input("ID del pedido: "))

    # Verificar si el pedido existe
    for i in range(len(pedidos)):
        if pedidos[i][0] == id_pedido:

            # Menu de opciones
            print()
            print("1 = Editar nombre del cliente")
            print("2 = Editar producto")
            print("3 = Editar cantidad")
            print()
            opcion = int(input("Opcion: "))

            # Editar nombre
            if opcion == 1:
                nuevo_cliente = input("Nuevo nombre del cliente: ")
                pedidos[i][1] = nuevo_cliente
            # Editar producto
            elif opcion == 2:
                nuevo_producto = input("Nuevo nombre del producto: ")
                pedidos[i][3] = nuevo_producto
            # Editar cantidad
            elif opcion == 3:
                nueva_cantidad = int(input("Nueva cantidad del producto saliente: "))
                pedidos[i][4] = nueva_cantidad
            else:
                print("ERROR: Opcion no valida.")

            print()
            print(("-") * 10 + "Pedido modificado con exito." + ("-") * 10)
            print()
            print(f"ID: {pedidos[i][0]} | Cliente: {pedidos[i][1]} | Hora: {pedidos[i][2]} | Producto: {pedidos[i][3]} | Cantidad: {pedidos[i][4]}")
            break

    # Si el pedido no existe se muestra un error
    else: print("ERROR: Pedido no encontrado.")

        
# Función para editar un producto
def editProducto():

    print()
    print(("=") * 50 + " EDITAR PRODUCTO " + ("=") * 50)

    # Entrada de Datos
    print()
    id_inventario = int(input("ID del producto: "))

    # Verificar si el producto existe
    for i in range(len(inventario)):
        if inventario[i][0] == id_inventario:
            
            # Menu de opciones
            print()
            print("1 = Editar nombre del producto")
            print("2 = Editar precio")
            print("3 = Editar cantidad")
            print()
            opcion = int(input("Opcion: "))

            # Editar producto
            if opcion == 1:
                nuevo_producto = input("Nuevo nombre del producto: ")
                inventario[i][1] = nuevo_producto
            # Editar precio
            elif opcion == 2:
                nuevo_precio = float(input("Nuevo precio del producto: "))
                inventario[i][3] = nuevo_precio
            # Editar cantidad
            elif opcion == 3:
                nueva_cantidad = int(input("Nueva cantidad del producto: "))
                inventario[i][2] = nueva_cantidad
            else:
                print("ERROR: Opcion no valida.")
        
            print()
            print(("-") * 10 + "Producto modificado con exito." + ("-") * 10)
            print()
            print(f"ID: {inventario[i][0]} | Producto: {inventario[i][1]} | Stock: {inventario[i][2]} | Precio: ${inventario[i][3]:.2f}")
            break

    else: print("ERROR: Producto no encontrado.")
            

# Función para eliminar un pedido
def eliminarPedido():
    print()
    print(("=") * 50 + " ELIMINAR PEDIDO " + ("=") * 50)

    # Entrada de Datos
    print()
    id_pedido = int(input("ID del pedido: "))

    # Verificar si el pedido existe
    for i in range(len(pedidos)):
        if pedidos[i][0] == id_pedido:
            pedidos.pop(i)
            print()
            print(("-" * 10) + "Pedido eliminado con exito." + ("-" * 10))
            break

    else: print("ERROR: Pedido no encontrado.")

# Función para eliminar un producto
def eliminarProducto():
    print()
    print(("=") * 50 + " ELIMINAR PRODUCTO " + ("=") * 50)

    # Entrada de Datos
    print()
    id_inventario = int(input("ID del producto: "))

    # Verificar si el producto existe
    for i in range(len(inventario)):
        if inventario[i][0] == id_inventario:
            inventario.pop(i)
            print(("-" * 10) + "Producto eliminado." + ("-" * 10))
            break

    else: print("ERROR: Producto no encontrado.")

# Procedimiento para mostrar el listado de productos
def listadoProductos():
    for i in range(len(inventario)):
        print(f"ID: {inventario[i][0]} | Producto: {inventario[i][1]} | Stock: {inventario[i][2]} | Precio: {inventario[i][3]}")


# Procedimiento para mostrar el listado de pedidos
def listadoPedidos():
    for i in range(len(pedidos)):
        print(f"ID: {pedidos[i][0]} | Cliente: {pedidos[i][1]} | Hora: {pedidos[i][2]} | Producto: {pedidos[i][3]} | Cantidad: {pedidos[i][4]}")





menu = True
# Sistema principal
while menu ==True:
    print()
    print(("=" * 10), "GESTIÓN DE PEDIDOS", ("=" * 10))
    print()
    print("1 = Registrar nuevo pedido")
    print("2 = Modificar pedido")
    print("3 = Eliminar pedido")
    print("4 = Listado de pedidos")

    print()
    print(("=" * 10), "GESTIÓN DE PRODUCTOS", ("=" * 10))
    print("5 = Registrar nuevo producto")
    print("6 = Modificar producto")
    print("7 = Eliminar producto")
    print("8 = Listado de productos")
    
    print()
    print("9 = Salir")

    opcion = int(input("Ingrese una opció: "))

    if opcion == 1:
        regNuevoPedido()
    elif opcion == 2:
        editPedido()
    elif opcion == 3:
        eliminarPedido()
    elif opcion == 4:
        listadoPedidos()
    elif opcion == 5:
        regNuevoProducto()
    elif opcion == 6:
        editProducto()
    elif opcion == 7:
        eliminarProducto()
    elif opcion == 8:
        listadoProductos()
    elif opcion == 9:
        print("Saliendo del sistema...")
        break

    print()
    menu = input("Desea utilizar otra opción? (S/N): ")
    if menu == "N" or menu == "n":
        menu = False
    else:
        menu = True

