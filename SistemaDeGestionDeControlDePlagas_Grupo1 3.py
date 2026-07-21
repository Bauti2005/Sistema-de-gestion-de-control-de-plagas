def registrarClientes(baseDeDatos):
    """
    Objetivo: Solicitar los datos de ubicación, tipo de contrato y tratamientos para uno o varios departamentos,
              calcular el costo total (con descuentos y estado Premium) y agregar el nuevo registro a la base de datos.
    Entrada: baseDeDatos — lista principal donde se almacenan todos los registros del sistema.
    Salida: ninguno
    """
    print("\n--- REGISTRO DE NUEVO SERVICIO ---")

    barrio = input("Barrio: ").title()
    while barrio == "":
        print("El barrio no puede estar vacío.")
        barrio = input("Barrio: ").title()
    calle = input("Calle: ").title()
    while calle == "":
        print("La calle no puede estar vacía.")
        calle = input("Calle: ").title()
    dptos = int(input("Cantidad de departamentos a fumigar: "))
    while dptos <= 0:
        print("Ingresá un número mayor a 0.")
        dptos = int(input("Cantidad de departamentos a fumigar: "))

    for i in range(dptos):
        print(f"--- Ingresando datos del Dpto {i+1} de {dptos} ---")
        piso = input("Piso: ").upper()
        while piso == "":
            print("El piso no puede estar vacío.")
            piso = input("Piso: ").upper()
        dpto = input("Departamento: ").upper()
        while dpto == "":
            print("El departamento no puede estar vacío.")
            dpto = input("Departamento: ").upper()
        print("Tipo de contrato:")
        print("  1 - Trimestral (10% de descuento)")
        print("  2 - Puntual")
        opcion_contrato = input("Seleccione una opción (1-2): ")
        while opcion_contrato != "1" and opcion_contrato != "2":
            print("Opción inválida. Ingresá 1 o 2.")
            opcion_contrato = input("Seleccione una opción (1-2): ")
        if opcion_contrato == "1":
            contrato = "Trimestral"
        else:
            contrato = "Puntual"

        precio_acumulado_depto = 0
        lista_tratamientos = []
        agregar_otro = "S"
        while agregar_otro == "S":
            print("Tipo de tratamiento:")
            print("  1 - Roedores   ($10.000/depto)")
            print("  2 - Cucarachas ($12.000/depto)")
            print("  3 - Hormigas   ($11.000/depto)")
            print("  4 - Generales  ($20.000/depto)")
            print("  5 - Todos      ($30.000/depto)")
            opcion_tratamiento = input("Seleccione una opción (1-5): ")
            while opcion_tratamiento != "1" and opcion_tratamiento != "2" and opcion_tratamiento != "3" and opcion_tratamiento != "4" and opcion_tratamiento != "5":
                print("Opción inválida. Ingresá un número del 1 al 5.")
                opcion_tratamiento = input("Seleccione una opción (1-5): ")
            if opcion_tratamiento == "1":
                tratamiento = "Roedores"
                precio_base = 10000
            elif opcion_tratamiento == "2":
                tratamiento = "Cucarachas"
                precio_base = 12000
            elif opcion_tratamiento == "3":
                tratamiento = "Hormigas"
                precio_base = 11000
            elif opcion_tratamiento == "4":
                tratamiento = "Generales"
                precio_base = 20000
            elif opcion_tratamiento == "5":
                tratamiento = "Todos"
                precio_base = 30000

            precio_acumulado_depto += precio_base
            lista_tratamientos.append(tratamiento)

            if tratamiento == "Todos":
                agregar_otro = "N"
            else:
                agregar_otro = input("¿Desea agregar otro tratamiento a este depto? (S/N): ").upper()

        if contrato == "Trimestral":
            precio_acumulado_depto = precio_acumulado_depto * 0.90

        cliente_premium = False
        if precio_acumulado_depto >= 25000:
            cliente_premium = True

        nuevo_registro = [barrio, calle, piso, dpto, contrato, lista_tratamientos, precio_acumulado_depto, cliente_premium]
        baseDeDatos.append(nuevo_registro)
        print(f"Registro exitoso. Total a cobrar a este depto: ${precio_acumulado_depto}")
        if cliente_premium:
            print("*** ¡Servicio clasificado como Premium! ***")


def verEstadisticas(baseDeDatos):
    """
    Objetivo: Calcular y mostrar la recaudación total y el promedio de cobro por departamento del día.
    Entrada: baseDeDatos — lista principal donde se almacenan todos los registros.
    Salida: ninguno
    """
    if len(baseDeDatos) == 0:
        print("No hay registros cargados.")
        return

    contador = 0
    acumulador = 0

    for cliente in baseDeDatos:
        acumulador += cliente[6]
        contador += 1

    promedio = acumulador / contador

    print("\n--- ESTADÍSTICAS DEL DÍA ---")
    print(f"Total de servicios registrados: {contador}")
    print(f"Recaudación total:              ${acumulador:,.0f}")
    print(f"Promedio por departamento:      ${promedio:,.0f}")



def verExtremos(baseDeDatos):
    """
    Objetivo: Encontrar y mostrar el departamento con el mayor y el menor pago registrado.
    Entrada: baseDeDatos — lista principal donde se almacenan todos los registros.
    Salida: ninguno
    """
    if len(baseDeDatos) == 0:
        print("No hay registros cargados.")
        return

    precioMax = baseDeDatos[0][6]
    registroMax = baseDeDatos[0]
    precioMin = baseDeDatos[0][6]
    registroMin = baseDeDatos[0]

    for i in range(1, len(baseDeDatos)):
        if baseDeDatos[i][6] > precioMax:
            precioMax = baseDeDatos[i][6]
            registroMax = baseDeDatos[i]
        if baseDeDatos[i][6] < precioMin:
            precioMin = baseDeDatos[i][6]
            registroMin = baseDeDatos[i]

    print(f"Mayor pago: {registroMax[1]} Piso {registroMax[2]} Dpto {registroMax[3]} — ${precioMax:,.0f}")
    print(f"Menor pago: {registroMin[1]} Piso {registroMin[2]} Dpto {registroMin[3]} — ${precioMin:,.0f}")


def buscar_cliente(baseDeDatos):
    """
    Objetivo: Buscar un cliente por calle/piso/dpto, por barrio o por monto exacto, con opción de agregar servicios.
    Entrada: baseDeDatos — lista principal donde se almacenan todos los registros.
    Salida: ninguno
    """
    if len(baseDeDatos) == 0:
        print("No hay registros en el sistema.")
        return

    while True:
        print("\n--- BUSCAR CLIENTE ---")
        print("1. Buscar por Calle, Piso y Dpto (Permite agregar servicios)")
        print("2. Buscar por Barrio")
        print("3. Buscar por Monto exacto")
        print("0. Volver al menú principal")
        opcion = input("Seleccione una opción (0-3): ")
        while opcion != "1" and opcion != "2" and opcion != "3" and opcion != "0":
            print("Opción inválida. Ingresá 0, 1, 2 o 3.")
            opcion = input("Seleccione una opción (0-3): ")

        if opcion == "0":
            break
        elif opcion == "1":
            calle_buscada = input("Calle: ").title()
            piso_buscado = input("Piso: ").upper()
            dpto_buscado = input("Departamento: ").upper()
            encontrado = False

            for cliente in baseDeDatos:
                if cliente[1] == calle_buscada and cliente[2] == piso_buscado and cliente[3] == dpto_buscado:
                    encontrado = True
                    print(f"\nCliente: {cliente[1]} | Piso: {cliente[2]} | Dpto: {cliente[3]}")
                    print(f"Tratamientos actuales: {cliente[5]}")
                    print(f"Total a cobrar: ${cliente[6]}")

                    agregar = input("\n¿Desea agregar un nuevo servicio? (S/N): ").upper()
                    while agregar != "S" and agregar != "N":
                        print("Opción inválida. Ingresá S o N.")
                        agregar = input("¿Desea agregar otro tratamiento a este depto? (S/N): ").upper()
                        
                    if agregar == "S":
                        print("Tipo de tratamiento:")
                        print("  1 - Roedores   ($10.000/depto)")
                        print("  2 - Cucarachas ($12.000/depto)")
                        print("  3 - Hormigas   ($11.000/depto)")
                        print("  4 - Generales  ($20.000/depto)")
                        print("  5 - Todos      ($30.000/depto)")
                        opcion_tratamiento = input("Seleccione una opción (1-5): ")
                        while opcion_tratamiento != "1" and opcion_tratamiento != "2" and opcion_tratamiento != "3" and opcion_tratamiento != "4" and opcion_tratamiento != "5":
                            print("Opción inválida. Ingresá un número del 1 al 5.")
                            opcion_tratamiento = input("Seleccione una opción (1-5): ")
                        if opcion_tratamiento == "1":
                            tratamiento = "Roedores"
                            precio_base = 10000
                        elif opcion_tratamiento == "2":
                            tratamiento = "Cucarachas"
                            precio_base = 12000
                        elif opcion_tratamiento == "3":
                            tratamiento = "Hormigas"
                            precio_base = 11000
                        elif opcion_tratamiento == "4":
                            tratamiento = "Generales"
                            precio_base = 20000
                        elif opcion_tratamiento == "5":
                            tratamiento = "Todos"
                            precio_base = 30000

                        if cliente[4] == "Trimestral":
                            precio_base = precio_base * 0.90

                        cliente[5].append(tratamiento)
                        cliente[6] += precio_base

                        if cliente[6] >= 25000:
                            cliente[7] = True
                            print("*** ¡Por este monto el cliente ahora es Premium! ***")

                        print(f"\n¡Servicio agregado! Nuevo total a cobrar: ${cliente[6]}")
                    break

            if encontrado == False:
                print("No se encontró ningún cliente con esa dirección.")

        elif opcion == "2":
            barrio_buscado = input("Ingrese el Barrio a buscar: ").title()
            print("\nResultados:")
            encontrado_barrio = False
            for cliente in baseDeDatos:
                if cliente[0] == barrio_buscado:
                    print(f"- Calle: {cliente[1]} | Piso: {cliente[2]} | Dpto: {cliente[3]} | Total: ${cliente[6]}")
                    encontrado_barrio = True
            if encontrado_barrio == False:
                print("No se encontraron clientes en ese barrio.")

        elif opcion == "3":
            monto_buscado = float(input("Ingrese el monto a buscar: $"))
            print("\nResultados:")
            encontrado_monto = False

            for cliente in baseDeDatos:
                if int(cliente[6]) == int(monto_buscado):
                    print(f"- Barrio: {cliente[0]} | Cliente: {cliente[1]} | Piso: {cliente[2]} | Dpto: {cliente[3]} | Total: ${cliente[6]}")
                    encontrado_monto = True

            if encontrado_monto == False:
                print("No se encontraron clientes con ese monto.")


def ordenar_clientes(baseDeDatos):
    """
    Objetivo: Ordenar los registros de mayor a menor por precio acumulado usando burbujeo con bandera, y mostrar el ranking.
    Entrada: baseDeDatos — lista principal donde se almacenan todos los registros.
    Salida: ninguno
    """
    if len(baseDeDatos) == 0:
        print("No hay registros cargados.")
        return

    desordenada = True
    while desordenada:
        desordenada = False
        for i in range(len(baseDeDatos) - 1):
            if baseDeDatos[i][6] < baseDeDatos[i+1][6]:
                aux = baseDeDatos[i]
                baseDeDatos[i] = baseDeDatos[i+1]
                baseDeDatos[i+1] = aux
                desordenada = True

    print("Lista ordenada de mayor a menor:")
    for i in range(len(baseDeDatos)):
        print(f"{i+1}. {baseDeDatos[i][1]} Piso {baseDeDatos[i][2]} Dpto {baseDeDatos[i][3]} — ${baseDeDatos[i][6]:,.0f}")


def main():
    """
    Objetivo: Controlar el flujo principal del programa mostrando el menú y despachando cada opción a la función correspondiente.
    Entrada: ninguno
    Salida: ninguno
    """
    baseDeDatos = []

    while True:
        print("\n=== SISTEMA DE GESTION DE CONTROL DE PLAGAS ===\n")
        print("1. Registrar nuevo servicio")
        print("2. Ver estadísticas del día")
        print("3. Reporte de cobros (Máximo y Mínimo)")
        print("4. Buscar cliente (por barrio, calle o monto)")
        print("5. Ranking de clientes por facturación ")
        print("6. Salir del sistema")
        print("7. [PRUEBA] Cargar 5 departamentos de ejemplo")

        opcion = input("Seleccione una opcion (1-7): ")

        if opcion == "1":
            registrarClientes(baseDeDatos)
        elif opcion == "2":
            verEstadisticas(baseDeDatos)
        elif opcion == "3":
            verExtremos(baseDeDatos)
        elif opcion == "4":
            buscar_cliente(baseDeDatos)
        elif opcion == "5":
            ordenar_clientes(baseDeDatos)
        elif opcion == "6":
            print("Cerrando el sistema. ¡Hasta la proxima!")
            break
        elif opcion == "7":
            baseDeDatos.append(["Palermo",   "Thames 1234",    "3", "A", "Trimestral", ["Roedores"],              9000.0,  False])
            baseDeDatos.append(["Belgrano",  "Cabildo 500",    "2", "B", "Puntual",    ["Todos"],                30000.0,  True ])
            baseDeDatos.append(["Palermo",   "Santa Fe 200",   "1", "C", "Trimestral", ["Cucarachas","Hormigas"], 20700.0,  False])
            baseDeDatos.append(["San Telmo", "Defensa 100",    "4", "D", "Puntual",    ["Generales"],            20000.0,  False])
            baseDeDatos.append(["Belgrano",  "Juramento 300",  "5", "E", "Puntual",    ["Cucarachas"],           12000.0,  False])
            print("5 departamentos de prueba cargados correctamente.")
        else:
            print("Opcion invalida. Por favor, ingrese un numero del 1 al 7")

main()