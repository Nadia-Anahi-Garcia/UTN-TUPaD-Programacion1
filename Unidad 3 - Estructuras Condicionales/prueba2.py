
hemisferio = input("¿En cuál hemisferio se encuentra (N / S)? ").upper()

if hemisferio == "n" or hemisferio == "s":
    mes = input("Ingrese el mes: ").lower()
    meses_anio = ["enero","febrero","marzo","abril","mayo","junio", "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    if mes in meses_anio:
        dia = int(input("Ingrese el día del mes: "))
        if 1 <= dia <= 31:
            # Ahora calculamos la estación
            if (mes == "diciembre" and dia >= 21) or (mes in ["enero", "febrero"]) or (mes == "marzo" and dia <= 20):
                estacion_n = "invierno"
                estacion_s = "verano"

            elif (mes == "marzo" and dia >= 21) or (mes in ["abril", "mayo"]) or (mes == "junio" and dia <= 20):
                estacion_n = "primavera"
                estacion_s = "otoño"

            elif (mes == "junio" and dia >= 21) or (mes in ["julio", "agosto"]) or (mes == "septiembre" and dia <= 20):
                estacion_n = "verano"
                estacion_s = "invierno"

            elif (mes == "septiembre" and dia >= 21) or (mes in ["octubre", "noviembre"]) or (mes == "diciembre" and dia <= 20):
                estacion_n = "otoño"
                estacion_s = "primavera"
                #Mostramos el resultado segúl el hemisferio. 
            if hemisferio == "n":
                print(f"Estás en {estacion_n}")
            else:
                print(f"Estás en {estacion_s}")
        else:
            print(" Ingrese un día válido (1-31).")
    else:
        print("Ingrese un mes válido.")
else:
    print("Por favor, ingrese Por favor, ingrese S (hemisferio sur) o N (hemisferio norte).")
