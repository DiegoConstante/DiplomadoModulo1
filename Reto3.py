# Clase 15 - Reto 3 - Optimizar el sistema previamente desarrollado

from collections import deque
from datetime import datetime

# --- CLASE PARA MANEJO DE INVENTARIO ---
class Productos:
    def __init__(self, inventario_inicial):
        # Se inicializa la lista de productos con los datos iniciales
        self.lista_productos = inventario_inicial

    def agregar_producto(self, nombre, stock, precio):
        # Buscamos si el producto ya existe (ignorando mayúsculas)
        for p in self.lista_productos:
            if p[1].lower() == nombre.lower():
                p[2] += stock # Aumentamos el stock existente
                print(f"Stock actualizado: {p[2]} unidades de {p[1]}")
                return
        
        # Si no existe, calculamos el nuevo ID basándonos en el último elemento
        nuevo_id = self.lista_productos[-1][0] + 1 if self.lista_productos else 1
        self.lista_productos.append([nuevo_id, nombre, stock, precio])
        print(f"Producto '{nombre}' registrado con éxito.")

    def editar_producto(self, id_prod):
        # Buscamos el producto por su ID único
        for p in self.lista_productos:
            if p[0] == id_prod:
                print()
                print("Seleccione una de las siguientes opciones:")
                print()
                print("1 = Nombre | 2 = Precio | 3 = Stock")
                op = input("¿Qué desea editar?: ")
                if op == "1": p[1] = input("Nuevo nombre: ")
                elif op == "2": p[3] = float(input("Nuevo precio: "))
                elif op == "3": p[2] = int(input("Nuevo stock: "))
                print("Producto modificado.")
                return
        print("Error: Producto no encontrado.")

    def eliminar_producto(self, id_prod):
        # Filtramos la lista para eliminar el producto por ID
        for i, p in enumerate(self.lista_productos):
            if p[0] == id_prod:
                self.lista_productos.pop(i)
                print("Producto eliminado con éxito.")
                return
        print("Error: Producto no encontrado.")

    def mostrar_inventario(self):
        # Formateo visual del inventario en consola
        print("="*25 + " INVENTARIO " + "="*25)
        for p in self.lista_productos:
            print(f"ID: {p[0]} | Producto: {p[1]:<15} | Stock: {p[2]:<5} | Precio: ${p[3]:.2f}")

# --- CLASE PARA MANEJO DE PEDIDOS ---
class Pedidos:
    def __init__(self):
        # Se utiliza deque para un manejo eficiente de colas (FIFO)
        self.cola_pedidos = deque()

    def registrar_pedido(self, inventario_obj):
        print("-"*10 + " REGISTRAR PEDIDO " + "-"*10)
        nombre_prod = input("Producto solicitado: ")
        cantidad = int(input("Cantidad: "))
        
        # Validamos si el producto existe y si hay stock suficiente
        for p in inventario_obj.lista_productos:
            if p[1].lower() == nombre_prod.lower():
                if p[2] >= cantidad:
                    p[2] -= cantidad # Descontamos del stock físico
                    cliente = input("Nombre del cliente: ")
                    id_pedido = len(self.cola_pedidos) + 1
                    hora = datetime.now().strftime('%d-%m-%y %H:%M:%S')
                    # Guardamos el pedido en la cola
                    self.cola_pedidos.append([id_pedido, cliente, hora, p[1], cantidad])
                    print(f"¡Pedido {id_pedido} registrado!")
                    return
                else:
                    print(f"Error: Stock insuficiente (Disponible: {p[2]})")
                    return
        print("Error: Producto no encontrado.")

    def editar_pedido(self, id_pedido, inventario_obj):
        # Buscamos el pedido en la cola
        for ped in self.cola_pedidos:
            if ped[0] == id_pedido:
                print(f"Editando Pedido ID: {id_pedido} (Cliente: {ped[1]})")
                print("1. Cambiar Cliente | 2. Cambiar Cantidad | 3. Cambiar Producto")
                op = input("Seleccione opción: ")

                if op == "1":
                    ped[1] = input("Nuevo nombre del cliente: ")
                    print("Nombre actualizado.")

                elif op == "2":
                    nueva_cant = int(input(f"Nueva cantidad (actual {ped[4]}): "))
                    for p in inventario_obj.lista_productos:
                        if p[1] == ped[3]:
                            # Devolvemos stock anterior al inventario y validamos el nuevo
                            stock_proyectado = p[2] + ped[4]
                            if stock_proyectado >= nueva_cant:
                                p[2] = stock_proyectado - nueva_cant
                                ped[4] = nueva_cant
                                print("Cantidad actualizada y stock ajustado.")
                            else:
                                print(f"Error: No hay suficiente stock.")
                            break
                elif op == "3":
                    print("Sugerencia: Cancele este pedido y cree uno nuevo para asegurar stock.")
                return
        print("Error: Pedido no encontrado.")

    def eliminar_pedido(self, id_pedido):
        # Buscamos y eliminamos de la cola usando rotación para no perder el orden
        for i, ped in enumerate(self.cola_pedidos):
            if ped[0] == id_pedido:
                print(f"Pedido {id_pedido} eliminado.")
                self.cola_pedidos.rotate(-i)
                self.cola_pedidos.popleft()
                self.cola_pedidos.rotate(i)
                return
        print("Error: Pedido no encontrado.")

    def mostrar_pedidos(self):
        print("="*25 + " LISTA DE PEDIDOS " + "="*25)
        if not self.cola_pedidos:
            print("No hay pedidos pendientes.")
        for ped in self.cola_pedidos:
            print(f"ID: {ped[0]} | Cliente: {ped[1]:<15} | Hora: {ped[2]} | Prod: {ped[3]} | Cant: {ped[4]}")

# --- SISTEMA PRINCIPAL (MAIN LOOP) ---

# Inventario base
inv_inicial = [[1, "Producto 1", 10, 5.99],
               [2, "Producto 2", 5, 9.99],
               [3, "Producto 3", 15, 8.99]]

# Instanciación de objetos
gestion_inv = Productos(inv_inicial)
gestion_ped = Pedidos()

while True:
    print()
    print("-"*5 + " GESTIÓN INTEGRAL " + "-"*5)
    print("  PEDIDOS           |   INVENTARIO")
    print("1. Ver pedidos      | 5. Ver Productos")
    print("2. Nuevo Pedido     | 6. Nuevo Producto")
    print("3. Editar Pedido    | 7. Editar Producto")
    print("4. Eliminar Pedido  | 8. Eliminar Producto")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        gestion_ped.mostrar_pedidos()
    elif opcion == "2":
        gestion_ped.registrar_pedido(gestion_inv)
    elif opcion == "3":
        id_p = int(input("ID del pedido a editar: "))
        gestion_ped.editar_pedido(id_p, gestion_inv)
    elif opcion == "4":
        id_p = int(input("ID del pedido a eliminar: "))
        gestion_ped.eliminar_pedido(id_p)
    elif opcion == "5":
        gestion_inv.mostrar_inventario()
    elif opcion == "6":
        nom = input("Nombre: "); stk = int(input("Stock: ")); pre = float(input("Precio: "))
        gestion_inv.agregar_producto(nom, stk, pre)
    elif opcion == "7":
        id_prod = int(input("ID del producto a editar: "))
        gestion_inv.editar_producto(id_prod)
    elif opcion == "8":
        id_prod = int(input("ID del producto a eliminar: "))
        gestion_inv.eliminar_producto(id_prod)
    elif opcion == "9":
        print("Saliendo..."); break
    else:
        print("Opción no válida.")