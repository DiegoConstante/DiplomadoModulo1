#Gestión de Inventario en un Almacén 

# Lista anidada para simular BDD   (Producto, Precio, Cantidad en Stock)
productos = [
    ["Producto 1", 10.99, 80],
    ["Producto 2", 9.99, 40],
    ["Producto 3", 8.99, 60],
    ["Producto 4", 7.99, 20],
    ["Producto 5", 6.99, 70]
]


# Funcion para ingresar mas productos
def entrada_productos():
    print("========== ENTRADA DE PRODUCTOS EN BDD ==========")

    # Entrada de Datos
    producto = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto entrantes: "))

    # Verificar si el producto ya existe y sumar, o agregar nuevo
    for i in range(len(productos)):
        if productos[i][0] == producto:
            productos[i][2] += cantidad
            print(f"Stock actualizado: {productos[i][2]} unidades de {producto}")
            return producto, precio, cantidad

    # Agregar nuevo producto al arreglo productos
    productos.append([producto, precio, cantidad])
    print(f"Producto '{producto}' agregado al inventario.")
    return producto, precio, cantidad

# Funcion para retirar productos
def salida_productos():
    print("========== SALIDA DE PRODUCTOS ==========")

    # Entrada de Datos
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad del producto salientes: "))

    # Verificar si el producto existe y veridica si la cantidad de salida no supera el stock disponible
    for i in range(len(productos)):
        if productos[i][0] == producto:
            if productos[i][2] >= cantidad:
                productos[i][2] -= cantidad
                # Si la cantidad de salida es menor al stock disponible, se registra la salida
                print(f"Salida registrada. Stock actual: {productos[i][2]}")
            else:
                # Si la cantidad de salida supera el stock disponible, se muestra un error y se detiene el proceso
                print(f"ERROR: Stock insuficiente. Disponible: {productos[i][2]} | Solicitado: {cantidad}")
            return
        
    # Si el producto no existe, se muestra un error
    print("ERROR: Producto no encontrado.")

# Procedimiento para calcular el inventario óptimo
def inventario_optimo(productos):
    print("========== INVENTARIO ÓPTIMO ==========")

    # Bandera para verificar si hay productos con stock menor a 80
    hay_productos = False

    # bucle para recorrer la lista de productos
    for i in range(len(productos)):
        # Verificar si hay productos con stock menor a 80
        if productos[i][2] < 80:
            hay_productos = True
            print()
            print(f"----- {productos[i][0]} -----")
            print(f"Cantidad actual: {productos[i][2]} | Cantidad óptima: 80")
            print()

    if hay_productos == False:
        print("Todos los productos están en nivel óptimo.")

# Funcion para generar alertas de stock
def alerta_stock(productos):
    print("========== ALERTAS DE STOCK ==========")

    # bucle para recorrer la lista de productos
    for i in range(len(productos)):
        print()
        print(f"----- {productos[i][0]} -----")

        # Verificar si el stock de algun producto es menor o igual a 20
        if productos[i][2] <= 20:
            print("ALERTA: Se requiere reabastecimiento inmediato")
            print(f"Cantidad actual: {productos[i][2]} | Cantidad mínima: 20")
        else:
            print("Stock en nivel aceptable")
            print(f"Cantidad actual: {productos[i][2]} | Cantidad mínima: 20")
        print()
        return
    



# Sistema Principal

# Bucle while para mostrar el menu de opciones para permitir al usuario 
# interactuar con la opcion que desee usar
while True:
    print("========== SISTEMA DE INVENTARIO ==========")
    # Menu de opciones
    print("1 = Entrada de productos")
    print("2 = Salida de productos")
    print("3 = Inventario óptimo")
    print("4 = Alertas de stock")
    print("5 = Salir")

    opciones_sistema = input("Opción: ")

    if opciones_sistema == "1":
        entrada_productos()
    elif opciones_sistema == "2": 
        salida_productos()
    elif opciones_sistema == "3":
        inventario_optimo(productos)
    elif opciones_sistema == "4":
        alerta_stock(productos)
    elif opciones_sistema == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")