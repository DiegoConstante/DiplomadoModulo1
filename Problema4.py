# Optimización de la Producción en una Fábrica

# Iconos tomados de (https://emojidb.org/advertencia-emojis?utm_source=user_search)

# Uso de lsitas para simular datos de las maquinas
maquinas = [
    ["Máquina 1", 86240, 73],
    ["Máquina 2", 131000, 50],
    ["Máquina 3", 65320, 85],
    ["Máquina 4", 43560, 91],
    ["Máquina 5", 1940, 100]]

# Funcion para obtener el estado de una maquina segun las horas de uso
def estadoMaquina(horas_uso):

    # Retorna el estado de una máquina según sus horas de uso
    if horas_uso <= 43830:
        return "Bueno"
    elif horas_uso <= 87660:
        return "Regular"
    else:
        return "Malo"

# Funcion para indicar si una maquina requiere mantenimiento
def mantenimientoMaquina():

    print()
    print("========== INFORMACIÓN DE MANTENIMIENTO ==========")

    # buble for para recorrer las maquinas en la lista maquinas
    for maquina in range(len(maquinas)):

        horas_uso = maquinas[maquina][1]
        rendimiento = maquinas[maquina][2]


        # condicionales para indicar si una maquina requiere mantenimiento segun sus horas de uso
        if horas_uso <= 10000:
            print()
            print("--------- " ,maquinas[maquina][0], "---------")
            print("No requiere mantenimiento, Equipo nuevo ✅")
            print("Horas de uso: ", horas_uso)

        elif 10000 < horas_uso <= 40000:
            print()
            print("--------- " ,maquinas[maquina][0], "---------")
            print("No requiere mantenimiento, Equipo casi nuevo ✅")
            print("Horas de uso: ", horas_uso)
        
        elif 40000 < horas_uso <= 87000:
            print()
            print("--------- " ,maquinas[maquina][0], "---------")
            print("Mantenimiento preventivo Requerido 🛠️")
            print("Equipo en estado regular ⚠️")
            print("Horas de uso: ", horas_uso) 
            
        elif 87000 < horas_uso <= 90000:
            print()
            print("--------- " ,maquinas[maquina][0], "---------")
            print("Mantenimiento prioritario Requerido 🛠️")
            print("Equipo en estado (regular - malo)/ ⚠️")
            print("Horas de uso: ", horas_uso)
        
        if horas_uso > 90000:
            print()
            print("--------- " ,maquinas[maquina][0], "---------")
            print("Mantenimiento urgente Requerido 🛠️")
            print("Equipo en estado malo 🔴")
            print("El rendimeito ha disminuido: ", rendimiento)
            print("Horas de uso: ", horas_uso)

# Funcion para indicar el nivel de rendimiento por maquina
def nivelRendimiento():

    
    print()
    print("========== NIVEL DE RENDIMIENTO ==========")
    
    for i in range(len(maquinas)):

        maquina = maquinas[i][0]
        horas_uso = maquinas[i][1]
        rendimiento = maquinas[i][2]

        print()
        print("--------- " ,maquina, "---------")
        print("Horas de uso: ", horas_uso)
        print("Estado: ", estadoMaquina(horas_uso))
        print("Rendimiento de la maquina: ", rendimiento, "%")

# Funcion para calcular el nivel de produccion segun la demanda
def nivelProduccion():

    print()
    print("========== AJUSTAR NIVEL DE PRODUCCION ==========")

    # Entrada de datos
    ventas_estimadas = int(input("Ventas estimadas: "))
    inventario_actual = int(input("Inventario actual: "))


    if ventas_estimadas > inventario_actual:
        nivel_produccion = ventas_estimadas - inventario_actual
    else:
        nivel_produccion = 0

    ajuste_rendimiento = nivel_produccion / 5

    produccion_total = 0

    for i in range(len(maquinas)):

        maquina = maquinas[i][0]
        horas_uso = maquinas[i][1]

        if horas_uso < 10000: 
            nuevo_rend = ajuste_rendimiento + 20

        elif horas_uso <= 80000:
            nuevo_rend = ajuste_rendimiento

        else:
            nuevo_rend = ajuste_rendimiento - 10
            

        maquinas[i][2] = nuevo_rend
        produccion_total += nuevo_rend

        print()
        print (f"--------- {maquina} ---------")
        print (f"Horas de uso: {horas_uso}")
        print ("Nivel de rendimiento ajustado: ", nuevo_rend, "%")
            


# Sistema principal


while True:
    print()
    print("========== OPTIMIZACIÓN DE PRODUCCIÓN ==========")
    print("1 = Estado de las maquinas")
    print("2 = Informacion de mantenimiento")
    print("3 = Nivel de rendimiento")
    print("4 = Ajustar nivel de produccion segun la demanda")
    print("5 = Salir")

    opciones_sistema = input("Opción: ")

    if opciones_sistema == "1":
        for i in range(len(maquinas)):
 
            horas_uso = maquinas[i][1]
            estado = estadoMaquina(horas_uso)
 
            print()
            print(" --------- ", maquinas[i][0], "---------")
 
            if estado == "Bueno":
                print(" 🟢 Estado: Bueno")
            elif estado == "Regular":
                print(" 🟡 Estado: Regular")
            else:
                print(" 🔴 Estado: Malo")

    elif opciones_sistema == "2": 
        mantenimientoMaquina()
    elif opciones_sistema == "3":
        nivelRendimiento()
    elif opciones_sistema == "4":
        nivelProduccion()
    elif opciones_sistema == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")