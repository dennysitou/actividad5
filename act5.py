while True:
    print("Menu Principal")
    print("1. Ingresar ventas")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular venta mas alta y mas baja")
    print("4. Calcular promedio de ventas")
    print("5. Dias que superaron los Q1000")
    print("6. Buscar venta especifica")
    print("7. Calcular cada venta")
    print("8. Salir")

    opcion = input("Seleccione una opcion del menu: ")
    ventas = []
    sumaventas = 0
    promventas = 0
    contdias = 0


    match opcion:
        case "1":
            veces = int(input("Ingrese cuantas ventas quiere ingresar: "))
            for i in range(0, veces):
                venta = int(input("Ingrese venta: "))
                ventas.append(venta)
        case "2":
            print(f"Ventas ingresadas: {ventas}")
        case "3":
            print("Venta mas alta: ")
        case "4":
            print("Promedio de ventas: ")
        case "5":
            print("Dias que superaron los Q1000: ")
        case "6":
            print("Buscar venta especifica: ")
        case "7":
            print("Calcular cada venta")
        case "8":
            print("Saliendo......")
            break
        case _:
            print("Opcion invalida, vuelva a intentarlo")