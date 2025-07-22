ventas = []
sumaventas = 0
promventas = 0
contdias = 0

while True:
    print("Menu Principal")
    print("1. Ingresar ventas")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular venta mas alta y mas baja")
    print("4. Calcular promedio de ventas")
    print("5. Dias que superaron los Q1000")
    print("6. Calcular cada venta")
    print("7. Salir")

    opcion = input("Seleccione una opcion del menu: ")

    match opcion:
        case "1":
            veces = int(input("Ingrese cuantas ventas quiere ingresar: "))
            for i in range(0, veces):
                venta = int(input("Ingrese venta: "))
                if venta >= 0:
                    ventas.append(venta)
                elif venta < 0:
                    print("No puede ingresar numeros negativos a las ventas")
        case "2":
            print(f"Ventas ingresadas: {ventas}")
        case "3":
            if not ventas:
                print("No hay nada en la lista de ventas")
            else:
                vmin = vmax = ventas[0]

                for num in ventas[1:]:
                    if num > vmax:
                        vmax = num
                    elif num < vmin:
                        vmin = num
                    print(f"El valor mas alto de la lista es:{vmax}")
                    print(f"El valor mas bajo de la lista es:{vmin}")
        case "4":
            sumaventas = sum(ventas)
            promventas = sumaventas/len(ventas)
            print(f"El promedio de las ventas es: {promventas}")

        case "5":
            sumaventas = sum(ventas)
            if sumaventas >= 1000:
                contdias += 1

            print(f"La cantidad de dias qus superaron los Q1000 fueron: {contdias}")

        case "6":
            print(ventas)
            for h in ventas:
                print(f"Venta: {h}")
                if h > 1000:
                    print("Es una venta alta")
                elif 500 <= h <= 1000:
                    print("Es una venta media")
                elif h < 500:
                    print("Es una venta baja")

        case "7":
            print("Saliendo el programa.......")
            print("Gracias por su visita :)")
            break

        case _:
            print("Opcion incorrecta, vuelva a intentarlo")





