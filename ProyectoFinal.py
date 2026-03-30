# Proyecto Final - Inventario de Flores

from collections import deque

class InventarioFlores:
    # Inventario inicial con datos predefinidos de flores
    INVENTARIO_INICIAL = [
        {"id": 1,  "nombre": "Rosa Roja",        "precio": 3.99,  "stock": 20},
        {"id": 2,  "nombre": "Tulipán Amarillo", "precio": 2.99,  "stock": 10},
        {"id": 3,  "nombre": "Girasol",          "precio": 4.99,  "stock": 30},
        {"id": 4,  "nombre": "Orquídea Blanca",  "precio": 8.99,  "stock": 20},
        {"id": 5,  "nombre": "Lirio Rosado",     "precio": 4.99,  "stock": 8 },
        {"id": 6,  "nombre": "Margarita",        "precio": 1.99,  "stock": 19},
        {"id": 7,  "nombre": "Lavanda",          "precio": 3.99,  "stock": 5 },
        {"id": 8,  "nombre": "Clavel Rojo",      "precio": 1.99,  "stock": 25},
        {"id": 9,  "nombre": "Peonia",           "precio": 6.99,  "stock": 15},
        {"id": 10, "nombre": "Hortensia Azul",   "precio": 7.99,  "stock": 8 },
    ]

    def __init__(self):
        # Carga el inventario inicial en una deque y calcula el siguiente ID disponible
        self.productos = deque(self.INVENTARIO_INICIAL)
        self._next_id = self.productos[-1]["id"] + 1

    def buscar_flor_por_id(self, id_prod):
        # Recorre el inventario y retorna el producto cuyo ID coincida
        for producto in self.productos:
            if producto["id"] == id_prod:
                return producto

    def buscar_flor_por_nombre(self, nombre_prod):
        # Búsqueda sin distinción de mayúsculas/minúsculas por nombre de flor
        for p in self.productos:
            if p["nombre"].lower() == nombre_prod.lower():
                return p
            
    def listar_flores(self):
        # Muestra nombre, precio y stock de cada flor (vista simplificada para pedidos)
        for producto in self.productos:
            print(f"{producto['nombre']:<20} | $ {producto['precio']:<5} | Stock: {producto['stock']:<5} ")

    def listar_inventario_flores(self):
        # Muestra el inventario completo con ID y alerta visual si el stock es menor a 10
        for producto in self.productos:
            print(f"ID: {producto['id']:<3} | {producto['nombre']:<20} | $ {producto['precio']:<5} | Stock: {producto['stock']:<5} | {'⚠️  Stock Bajo' if producto['stock'] < 10 else ''}")

    def agregar_producto(self, nombre, precio, cantidad):
        # Si la flor ya existe, suma la cantidad al stock existente en lugar de duplicarla
        existente = self.buscar_flor_por_nombre(nombre)
        if existente is not None:
            existente["stock"] += cantidad
            print(f"📢  '{nombre}' ya existe. Stock actualizado a {existente['stock']}.")
        else:
            # Si es nueva, la agrega al final de la deque con un ID autoincremental
            self.productos.append({"id": self._next_id, "nombre": nombre, "precio": precio, "stock": cantidad})
            self._next_id += 1
            print(f"✅  Producto registrado: {nombre} | $ {precio} | Stock: {cantidad}")

    def editar_producto(self, id_prod, nombre, precio, cantidad):
        # Sobreescribe los campos del producto encontrado con los nuevos valores
        producto = self.buscar_flor_por_id(id_prod)
        producto["nombre"] = nombre
        producto["precio"] = precio
        producto["stock"]  = cantidad
        print(f"✅  Producto ID {id_prod} actualizado con éxito!")

    def eliminar_producto(self, id_producto):
        # Busca el producto por ID y lo elimina de la deque
        producto = self.buscar_flor_por_id(id_producto)
        self.productos.remove(producto)
        print(f"✅  Producto '{producto['nombre']}' eliminado con éxito!")


# ============================================================
# PEDIDOS
# ============================================================

class GestionPedidos:

    def __init__(self):
        self.cola_pedidos = deque()

    # Etiquetas de prioridad asociadas a un número del 1 al 3
    PRIORIDADES = {1: "🔴 Alta", 2: "🟡 Media", 3: "🟢 Baja"}

    # Tipos de ramillete con su nombre y cantidad de flores incluidas
    RAMILLETES = {
        1: ("Premium",  24),
        2: ("Clásico",  18),
        3: ("Pequeño",  12),
        4: ("Mini",      6),
    }

    # Pedido de ejemplo para inicializar la cola con datos de prueba
    EJEMPLO_PEDIDOS = [
        {"id": 1, "cliente": "John Doe", "correo": "john@email.com", "telefono": "0991234567",
         "pais": "Ecuador", "direccion": "Av. Amazonas 123",
         "flores": [{"producto": "Lirio Rosado", "cantidad": 5}],
         "prioridad": 1, "total_pedido": 24.95, "estado": "🚚 Enviado"},
    ]

    def __init__(self):
        # Carga los pedidos de ejemplo y calcula el siguiente ID disponible
        self.cola_pedidos = deque(self.EJEMPLO_PEDIDOS)
        self._next_id = self.cola_pedidos[-1]["id"] + 1

    def buscar_pedido_por_id(self, id_pedido):
        # Recorre la cola y retorna el pedido cuyo ID coincida
        for pedido in self.cola_pedidos:
            if pedido["id"] == id_pedido:
                return pedido

    def formato_flores(self, flores):
        # Formatea la lista de flores: Ramillete - Rosa Roja - 5 + Ramillete - Lavanda - 3
        return " + ".join(
            f"Ramillete de {f['producto']} | Cantidad {f['cantidad']}"
            for f in flores
        )

    def listar_pedidos(self):
        print()
        print("="*25 + " LISTA DE PEDIDOS " + "="*25)
        print()
        if not self.cola_pedidos:
            print("No hay pedidos en la cola.")
            return
        # Ordena los pedidos por prioridad antes de mostrarlos (1=Alta primero)
        pedidos_ordenados = sorted(self.cola_pedidos, key=lambda p: p["prioridad"])
        for pedido in pedidos_ordenados:
            print("-"*90)
            print(f"#CP: {pedido['id']} - {pedido['cliente']} - {pedido['correo']} - Tel: {pedido['telefono']}")
            print()
            print(f"País: {pedido['pais']} - Dir: {pedido['direccion']:<20}"
                  f"Prioridad: {self.PRIORIDADES[pedido['prioridad']]} - Estado: {pedido['estado']}")
            print()
            print(f"Flores: {self.formato_flores(pedido['flores'])} - Total=  ${pedido['total_pedido']:<8.2f} ")
            print("-"*90)
            print()

    def agregar_pedido(self, cliente, correo, telefono, pais, direccion, flores, prioridad, estado, inventario):
        """flores = [{"producto": "Rosa Roja", "cantidad": 5}, ...]"""
        total = 0
        # Valida existencia y stock suficiente antes de confirmar el pedido
        for item in flores:
            producto = inventario.buscar_flor_por_nombre(item["producto"])
            if producto is None:
                raise ValueError(f"El producto '{item['producto']}' no existe en el inventario.")
            if item["cantidad"] > producto["stock"]:
                raise ValueError(f"Stock insuficiente para '{item['producto']}'. Disponible: {producto['stock']}")
            total += round(producto["precio"] * item["cantidad"], 2)

        # Descuenta el stock de cada flor incluida en el pedido
        for item in flores:
            inventario.buscar_flor_por_nombre(item["producto"])["stock"] -= item["cantidad"]

        # Registra el nuevo pedido en la cola con ID autoincremental
        self.cola_pedidos.append({
            "id": self._next_id, "cliente": cliente, "correo": correo,
            "telefono": telefono, "pais": pais, "direccion": direccion,
            "flores": flores, "prioridad": prioridad,
            "total_pedido": round(total, 2), "estado": estado
        })
        self._next_id += 1
        return round(total, 2)

    def eliminar_pedido(self, id_pedido, inventario):
        pedido = self.buscar_pedido_por_id(id_pedido)
        if pedido is None:
            raise ValueError(f"Pedido con ID {id_pedido} no encontrado.")
        # Devuelve el stock de las flores al inventario antes de eliminar el pedido
        for item in pedido["flores"]:
            producto = inventario.buscar_flor_por_nombre(item["producto"])
            if producto:
                producto["stock"] += item["cantidad"]
        self.cola_pedidos.remove(pedido)


# ============================================================
# MENÚ — captura inputs y maneja excepciones
# ============================================================

# Instancias globales compartidas entre el inventario y la gestión de pedidos
inventario = InventarioFlores()
pedidos    = GestionPedidos()

def menu_principal():
    # Imprime el menú principal con las opciones disponibles
    menu = f"""
    {' FLORISTERÍA EC ':=^40}
    
    PRODUCTOS              PEDIDOS
    {"-"*12: <22} {"-"*12}
    1. Listar flores                 5. Listar pedidos
    2. Registrar producto            6. Agregar pedido
    3. Editar producto               7. Editar pedido
    4. Eliminar producto             8. Eliminar pedido
    
    0. Salir
    {'='*40}
    """
    print(menu)

# Bucle principal que mantiene el programa activo hasta que el usuario elija salir
while True:
    menu_principal()

    opcion = input("Seleccione una opción: ")

    # ── INVENTARIO ──────────────────────────────────────────
    if opcion == "1":
        # Muestra el inventario completo con advertencias de stock bajo
        print()
        print("="*30 + " INVENTARIO " + "="*30)
        inventario.listar_inventario_flores()
        print("="*73)

    elif opcion == "2":
        # Registra un nuevo producto validando que los datos sean correctos
        try:
            print()
            nombre   = input("Nombre de la flor: ").strip()
            if not nombre: raise ValueError("El nombre no puede estar vacío.")
            precio   = float(input("Precio: "))
            if precio < 0: raise ValueError("El precio no puede ser negativo.")
            cantidad = int(input("Cantidad: "))
            if cantidad < 0: raise ValueError("La cantidad no puede ser negativa.")
            inventario.agregar_producto(nombre, precio, cantidad)
        except ValueError as e:
            # Distingue errores de conversión de tipo de errores de negocio
            if "could not convert" in str(e) or "float" in str(e) or "int" in str(e):
                print("Error: El precio y la cantidad deben ser números.")
            else:
                print(f"Error: {e}")

    elif opcion == "3":
        # Permite editar un producto existente; los campos en blanco conservan el valor actual
        try:
            print()
            entrada_id = input("ID del producto a editar: ").strip()
            if not entrada_id: raise ValueError("El ID no puede estar vacío.")
            id_prod  = int(entrada_id)
            producto = inventario.buscar_flor_por_id(id_prod)
            if producto is None: raise ValueError("Producto no encontrado.")

            print(f"Producto encontrado: {producto}")
            print("Deje en blanco para mantener el valor actual:")

            nuevo_nombre = input(f"Nombre [{producto['nombre']}]: ").strip() or producto["nombre"]

            entrada_precio = input(f"Precio [{producto['precio']}]: ").strip()
            # Usa el valor ingresado o conserva el precio actual si se deja en blanco
            precio = float(entrada_precio) if entrada_precio else producto["precio"]
            if precio < 0: raise ValueError("El precio no puede ser negativo.")

            entrada_cantidad = input(f"Stock [{producto['stock']}]: ").strip()
            # Usa el valor ingresado o conserva el stock actual si se deja en blanco
            cantidad = int(entrada_cantidad) if entrada_cantidad else producto["stock"]
            if cantidad < 0: raise ValueError("La cantidad no puede ser negativa.")

            inventario.editar_producto(id_prod, nuevo_nombre, precio, cantidad)
        except ValueError as e:
            if "could not convert" in str(e):
                print("Error: Debes ingresar un número válido.")
            else:
                print(f"Error: {e}")

    elif opcion == "4":
        # Solicita confirmación antes de eliminar definitivamente un producto
        try:
            print()
            entrada_id = input("ID del producto a eliminar: ").strip()
            if not entrada_id: raise ValueError("El ID no puede estar vacío.")
            id_producto = int(entrada_id)
            producto = inventario.buscar_flor_por_id(id_producto)
            if producto is None: raise ValueError("Producto no encontrado.")

            confirmar = input(f"¿Eliminar '{producto['nombre']}'? (s/n): ").strip().lower()
            if confirmar == "s":
                inventario.eliminar_producto(id_producto)
            else:
                print("Eliminación cancelada.")
        except ValueError as e:
            print(f"Error: {e}")

    # ── PEDIDOS ─────────────────────────────────────────────
    elif opcion == "5":
        # Muestra todos los pedidos ordenados por prioridad
        pedidos.listar_pedidos()

    elif opcion == "6":
        # Registra un nuevo pedido recopilando datos del cliente, flores y prioridad
        try:
            print()
            print("="*25 + " AGREGAR PEDIDO " + "="*25)

            # — Datos del cliente —
            cliente = input("Cliente: ").strip()
            if not cliente: raise ValueError("El nombre no puede estar vacío.")

            correo = input("Correo: ").strip()
            if not correo: raise ValueError("El correo no puede estar vacío.")
            if "@" not in correo: raise ValueError("El correo debe tener un '@'.")

            telefono = input("Teléfono: ").strip()
            if not telefono: raise ValueError("El teléfono no puede estar vacío.")

            if not telefono.isdigit():
                raise ValueError("El teléfono debe ser un número.")
            
            if len(telefono) != 10:
                raise ValueError("El teléfono debe tener 10 dígitos.")

            pais = input("País de envío: ").strip()
            if not pais: raise ValueError("El país no puede estar vacío.")

            direccion = input("Dirección: ").strip()
            if not direccion: raise ValueError("La dirección no puede estar vacía.")

            # — Selección de flores —
            print()
            print("── Flores disponibles ──")
            inventario.listar_flores()
            print()

            flores = []
            # Bucle para agregar múltiples flores al pedido; ENTER vacío finaliza la selección
            while True:
                nombre_flor = input("Nombre de la flor (o ENTER para terminar): ").strip()
                if not nombre_flor:
                    if not flores:
                        raise ValueError("Debe agregar al menos una flor al pedido.")
                    break

                producto = inventario.buscar_flor_por_nombre(nombre_flor)
                if producto is None:
                    print(f"📢  '{nombre_flor}' no existe en el inventario. Intente de nuevo.")
                    continue

                cantidad = int(input(f"Cantidad de '{nombre_flor}': "))
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor a 0.")

                # Si la flor ya fue agregada, acumula la cantidad en lugar de duplicarla
                existente = next((f for f in flores if f["producto"].lower() == nombre_flor.lower()), None)
                if existente:
                    existente["cantidad"] += cantidad
                else:
                    flores.append({"producto": producto["nombre"], "cantidad": cantidad})

                print(f"  ✅ {producto['nombre']} x{cantidad} agregado.")

            # — Prioridad y estado —
            prioridad = int(input("Prioridad (1=Alta, 2=Media, 3=Baja): "))
            if prioridad not in pedidos.PRIORIDADES: raise ValueError("Prioridad inválida.")

            # Estado inicial fijo para todos los pedidos nuevos
            estado = "🎫  Preparando el pedido"

            total = pedidos.agregar_pedido(cliente, correo, telefono, pais, direccion,
                                        flores, prioridad, estado, inventario)

            print()
            print(f"✅  Pedido registrado con éxito!")
            print(f"    Cliente : {cliente} | {correo} | {telefono}")
            print(f"    Envío   : {pais} — {direccion}")
            print(f"    Flores  : {pedidos.formato_flores(flores)}")
            print(f"    Total   : ${total}")

        except ValueError as e:
            if "could not convert" in str(e) or "int" in str(e):
                print("Error: La cantidad y prioridad deben ser números.")
            else:
                print(f"📢  Error: {e}")

    elif opcion == "7":
        # Permite modificar los datos de un pedido existente, incluyendo las flores
        try:
            print()
            print("="*25 + " EDITAR PEDIDO " + "="*25)
            entrada_id = input("ID del pedido a editar: ").strip()
            if not entrada_id: raise ValueError("El ID no puede estar vacío.")
            id_pedido = int(entrada_id)

            pedido = pedidos.buscar_pedido_por_id(id_pedido)
            if pedido is None: raise ValueError(f"Pedido con ID {id_pedido} no encontrado.")

            print()
            print(f"Pedido encontrado:")
            print(f"  Cliente  : {pedido['cliente']} | {pedido['correo']} | {pedido['telefono']}")
            print(f"  Envio    : {pedido['pais']} - {pedido['direccion']}")
            print(f"  Flores   : {pedidos.formato_flores(pedido['flores'])}")
            print(f"  Total    : ${pedido['total_pedido']} | {pedidos.PRIORIDADES[pedido['prioridad']]} | {pedido['estado']}")
            print()
            print("Deje en blanco para mantener el valor actual:")

            # — Datos del cliente —
            cliente  = input(f"Cliente [{pedido['cliente']}]: ").strip()   or pedido["cliente"]

            correo   = input(f"Correo [{pedido['correo']}]: ").strip()     or pedido["correo"]
            if "@" not in correo: raise ValueError("El correo debe tener un '@'.")

            telefono = input(f"Telefono [{pedido['telefono']}]: ").strip() or pedido["telefono"]
            if not telefono.isdigit():   raise ValueError("El telefono debe ser un numero.")
            if len(telefono) != 10:      raise ValueError("El telefono debe tener 10 digitos.")

            pais     = input(f"Pais [{pedido['pais']}]: ").strip()         or pedido["pais"]
            direccion = input(f"Direccion [{pedido['direccion']}]: ").strip() or pedido["direccion"]

            # — Re-selección de flores —
            print()
            print(f"Flores actuales: {pedidos.formato_flores(pedido['flores'])}")
            reemplazar = input("Desea cambiar las flores? (s/n): ").strip().lower()

            if reemplazar == "s":
                print()
                print("── Flores disponibles ──")
                inventario.listar_flores()
                print()

                # Restaura el stock de las flores anteriores antes de asignar las nuevas
                for item in pedido["flores"]:
                    prod = inventario.buscar_flor_por_nombre(item["producto"])
                    if prod: prod["stock"] += item["cantidad"]

                flores = []
                # Bucle para seleccionar las nuevas flores del pedido editado
                while True:
                    nombre_flor = input("Nombre de la flor (o ENTER para terminar): ").strip()
                    if not nombre_flor:
                        if not flores: raise ValueError("Debe agregar al menos una flor.")
                        break

                    prod = inventario.buscar_flor_por_nombre(nombre_flor)
                    if prod is None:
                        print(f"  '{nombre_flor}' no existe. Intente de nuevo.")
                        continue

                    cantidad = int(input(f"Cantidad de '{nombre_flor}': "))
                    if cantidad <= 0: raise ValueError("La cantidad debe ser mayor a 0.")

                    # Acumula cantidad si la flor ya fue ingresada en esta edición
                    existente = next((f for f in flores if f["producto"].lower() == nombre_flor.lower()), None)
                    if existente:
                        existente["cantidad"] += cantidad
                    else:
                        flores.append({"producto": prod["nombre"], "cantidad": cantidad})
                    print(f"  {prod['nombre']} x{cantidad} agregado.")
            else:
                # Conserva las flores originales del pedido sin cambios
                flores = pedido["flores"]

            # — Prioridad y estado —
            entrada_prioridad = input(f"Prioridad [{pedido['prioridad']}] (1=Alta, 2=Media, 3=Baja): ").strip()
            # Usa el valor ingresado o mantiene la prioridad actual si se deja en blanco
            prioridad = int(entrada_prioridad) if entrada_prioridad else pedido["prioridad"]
            if prioridad not in pedidos.PRIORIDADES: raise ValueError("Prioridad invalida.")

            estados_validos = ["Preparando el pedido", "Enviado", "Entregado", "Cancelado"]
            print(f"Estados: {' | '.join(estados_validos)}")
            nuevo_estado = input(f"Estado [{pedido['estado']}]: ").strip() or pedido["estado"]

            # — Aplica cambios —
            # Recalcula el total con las flores seleccionadas (nuevas o actuales)
            total = 0
            for item in flores:
                prod = inventario.buscar_flor_por_nombre(item["producto"])
                if prod is None: raise ValueError(f"'{item['producto']}' no existe en el inventario.")
                # Solo valida stock disponible si se reemplazaron las flores
                if reemplazar == "s" and item["cantidad"] > prod["stock"]:
                    raise ValueError(f"Stock insuficiente para '{item['producto']}'. Disponible: {prod['stock']}")
                total += round(prod["precio"] * item["cantidad"], 2)

            # Descuenta el stock solo si se seleccionaron flores nuevas
            if reemplazar == "s":
                for item in flores:
                    prod = inventario.buscar_flor_por_nombre(item["producto"])
                    prod["stock"] -= item["cantidad"]

            # Actualiza todos los campos del pedido con los nuevos valores
            pedido["cliente"]      = cliente
            pedido["correo"]       = correo
            pedido["telefono"]     = telefono
            pedido["pais"]         = pais
            pedido["direccion"]    = direccion
            pedido["flores"]       = flores
            pedido["prioridad"]    = prioridad
            pedido["total_pedido"] = round(total, 2)
            pedido["estado"]       = nuevo_estado

            print(f"\n✅  Pedido ID {id_pedido} actualizado con exito!")
            print(f"    Flores : {pedidos.formato_flores(flores)}")
            print(f"    Total  : ${round(total, 2)}")

        except ValueError as e:
            if "could not convert" in str(e) or "int" in str(e):
                print("Error: Debes ingresar un numero valido.")
            else:
                print(f"\nError: {e}")

    elif opcion == "8":
        # Solicita confirmación antes de eliminar el pedido y restaurar el stock
        try:
            print()
            print("="*25 + " ELIMINAR PEDIDO " + "="*25)
            entrada_id = input("ID del pedido a eliminar: ").strip()
            if not entrada_id: raise ValueError("El ID no puede estar vacío.")
            id_pedido = int(entrada_id)

            pedido = pedidos.buscar_pedido_por_id(id_pedido)
            if pedido is None: raise ValueError(f"Pedido con ID {id_pedido} no encontrado.")

            print()
            print(f"Pedido encontrado:")
            print(f"  Cliente  : {pedido['cliente']} | {pedido['correo']} | {pedido['telefono']}")
            print(f"  Envio    : {pedido['pais']} - {pedido['direccion']}")
            print(f"  Flores   : {pedidos.formato_flores(pedido['flores'])}")
            print(f"  Total    : ${pedido['total_pedido']} | {pedidos.PRIORIDADES[pedido['prioridad']]} | {pedido['estado']}")
            print()

            confirmar = input("¿Confirmar eliminación? (s/n): ").strip().lower()
            if confirmar == "s":
                # Elimina el pedido y devuelve automáticamente el stock al inventario
                pedidos.eliminar_pedido(id_pedido, inventario)
                print("Pedido eliminado con exito.")
            else:
                print("Eliminación cancelada.")
        except ValueError as e:
            print(f"Error: {e}")

    elif opcion == "0":
        # Termina el bucle principal y cierra el programa
        print("Saliendo..."); break

    else:
        print("Opción no válida.")