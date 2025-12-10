from unittest import case
from jsonFileHandler import *
from UtilsFunctions import *
from datetime import datetime
import os
from Utilstuplas import *

PRODUCT_FILE_PATH= "./Database/infoData.json"   #El puente hacia el json con la informacion


# Bucle principal del programa
while True:
     # Menú principal
    choice = menuu("| O R G A N I Z A D O R|" , "--Gastos Diarios--" , options)
    match choice:
        # CASE 1 → Registrar un gasto nuevo
       case 1:
            # Se recopila la información del nuevo gasto
            limpiarpantalla()
            content = {
                "monto": correct_number("¿De cuanto fue el gasto?\n --> ", int , range(1,10000000000 )),
                "category": correct_number("\n1. Comida\n2. Transporte\n3. Entretenimiento\n4. Otros\nSelecciona la categoria del gasto\n --> ", int, range(1, 5)),
                "Description":input("Descripcion del gasto //'Enter' para dejar vacio:\n -->"),
                "time":correct_fecha("Ingrese la fecha del gasto //'DD-MM-YYYY//'\n -->")
                    
            }
            while True:
                sure= input("Ingrese 'S' para guardar o 'C' para cancelar").strip().lower()
                if sure == "c":
                    print("Gasto cancelado")
                    break
                elif sure == "s":
                    # Confirmación visual de datos guardados
                    print("\n* Datos guardados correctamente*")
                    print(f"Monto: ${content['monto']}")
                    print(f"Categoría: {content['category']} , {Diccionario_cat[content['category']]}")
                    print(f"Descripción: {content['Description']}")
                    print(f"Fecha: {content['time']}")

                    datacontent = read_file(PRODUCT_FILE_PATH)  
                    datacontent.append(content)                    #Se abre el json, se ingresa la nueva informacion, se guarda
                    saveFile(PRODUCT_FILE_PATH, datacontent)
                    break
                else:
                    print("Eror, datos no almacenados, intente nuevamente")
       # CASE 2 → Listar gastos registrados
       case 2:
        limpiarpantalla()
        while True:
            choice = menuu("        L I S T A R       ","------- Gastos--------", listar_Gastos )
            match choice:
                case 1:
                    limpiarpantalla()
                    Dates = read_file(PRODUCT_FILE_PATH)
                    if len(Dates) == 0:
                        print("¡No tienes ningun gasto registrado!")
                    else:
                        print("\n                === P R O D U C T O S  R E G I S T R A D O S ===")
                        print("---------------------------------------------------------------------------------")
                        print("\n= MONTO GASTADO         CATEGORIA DEL GASTO          DESCRIPCION          FECHA")
                        print("                                                      DEL GASTO       ")
                        print("---------------------------------------------------------------------------------")
                        for content in Dates:
                            print(f" {content['monto']:<22} {Diccionario_cat[content['category']]:<27}  {content['Description']:<18} {content['time']}")
               # Listar filtrando por categorías
                case 2:
                     limpiarpantalla()
                     choice = menuu("    C A T E G O R I A S     ","(selecciona para ver los gastos)", categorias )
                     match choice:
                        case 1:
                             Dates = read_file(PRODUCT_FILE_PATH)
                             minimenu(Dates, 1, "Comida")
                        case 2:
                             Dates = read_file(PRODUCT_FILE_PATH)
                             minimenu(Dates, 2, "Transporte")
                        case 3:
                             Dates = read_file(PRODUCT_FILE_PATH)
                             minimenu(Dates, 3, "Entretenimiento")           
                        case 4: 
                            Dates = read_file(PRODUCT_FILE_PATH)
                            minimenu(Dates, 4, "Otros")  
                  # Filtrar por fecha                                                                                    
                case 3:
                    limpiarpantalla()
                    print("Filtrar por fechas")
                    try:
                        fecha1 = correct_fecha("Ingrese la fecha del gasto //'DD-MM-YYYY//'\n -->")
                        objDate1 = datetime.strptime(fecha1, "%d-%m-%Y") 
                        fecha2 = correct_fecha("Ingrese la fecha del gasto //'DD-MM-YYYY//'\n -->")
                        objDate2 = datetime.strptime(fecha2, "%d-%m-%Y")
                        dataGasto = read_file(PRODUCT_FILE_PATH)
                        info = filtroFecha(dataGasto, objDate1, objDate2)
                        categories(info)
                    except ValueError:
                            print("Formato de fecha no válido (DIA-MES-AÑO)")
                case 4:
                     limpiarpantalla()
                     break
        # CASE 3 → Calcular montos -diario, semanal, mensual-
       case 3:  
        while True:
         choice = menuu( "    C A L C U L A R", "   (total gastos)", caso3_gastos)
         match choice:
            case 1:
                 limpiarpantalla()
                 Dates = read_file(PRODUCT_FILE_PATH)
                 Monto_diarioo(Dates)
            case 2:
                 limpiarpantalla()
                 Dates = read_file(PRODUCT_FILE_PATH)
                 Monto_semanal(Dates)
            case 3:
                 limpiarpantalla()
                 Dates = read_file(PRODUCT_FILE_PATH)
                 Monto_mensual(Dates)
            case 4:
                 break
        # CASE 4 → Reportes
       case 4:
        while True:
         choice = menuu( "    R E P O R T E S", "   (total gastos)", caso3_gastos)
         match choice:
            case 1:
                limpiarpantalla()
                Dates = read_file(PRODUCT_FILE_PATH)
                menudiario(Dates)
            case 2:
                limpiarpantalla()
                Dates = read_file(PRODUCT_FILE_PATH)
                menusemanal(Dates)
            case 3:
                limpiarpantalla()
                Dates = read_file(PRODUCT_FILE_PATH)
                menumensual(Dates)              
            case 4:
                limpiarpantalla()
                break
        # CASE 5 → Salir del programa
       case 5:
        answer = input("¿Desea salir del programa? (S/N): ")

        if answer.lower() == "s":  
            print("\n\n¡Fue un placer, intenta no derrochar mas!\n\n\n")
            break 
        elif answer.lower() == "n":  
            print()
            limpiarpantalla()
        else:
            limpiarpantalla()
            print("(Eror: continuara el programa)\n\n")         