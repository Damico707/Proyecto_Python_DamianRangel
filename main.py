from jsonFileHandler import *
from UtilsFunctions import *
from datetime import datetime

PRODUCT_FILE_PATH= "./Database/infoData.json"
options = ("Registrar un nuevo gasto",
"Listar gastos",
"Calcular total de gastos",
"Generar reporte de gastos",
"Finalizar programa",)

listar_Gastos = ("Ver todos los gastos",
"Filtrar por categoria",
"Filtrar por rango de fechas",
"Regresar al menu principal")

Diccionario_cat = {
        1: "Comida",
        2: "Transporte",
        3: "Entretenimiento",
        4: "Otros"
    }

categorias= (" Comida.",
" Transporte.",
" Entretenimiento.",
" Otros.")

while True:
    choice = menuu("| O R G A N I Z A D O R|" , "--Gastos Diarios--" , options)
    match choice:
       case 1:
            content = {
                "monto": correct_number("¿De cuanto fue el gasto?\n --< ",),
                "category": correct_number("\n1. Comida\n2. Transporte\n3. Entretenimiento\n4. Otros\nSelecciona la categoria del gasto\n --> ", int, range(1, 5)),
                "Description":input("Descripcion del gasto //'Enter' para dejar vacio:\n -->"),
                "time":input("Ingrese la fecha del gasto\n formato 'DIA-MES-AÑO'\n -->")
            }

             
            print("\n*** Datos guardados correctamente***")
            print(f"Monto: ${content['monto']}")
            print(f"Categoría: {content['category']} , {Diccionario_cat[content['category']]}")
            print(f"Descripción: {content['Description']}")
            print(f"Fecha: {content['time']}")

            datacontent = read_file(PRODUCT_FILE_PATH)
            datacontent.append(content)
            saveFile(PRODUCT_FILE_PATH, datacontent)
     
       case 2:
        while True:
            choice = menuu("        L I S T A R       ","------- Gastos--------", listar_Gastos )
            match choice:
                case 1:
                    Dates = read_file(PRODUCT_FILE_PATH)
                    if len(Dates) == 0:
                        print("¡No tienes ningun gasto registrado!")
                    else:
                        print("\n=== P R O D U C T O S  R E G I S T R A D O S ===")
                        print("---------------------------------------------------------------------------------")
                        print("= MONTO GASTADO         CATEGORIA DEL GASTO          DESCRIPCION DEL GASTO \n")
                        for content in Dates:
                            print(f" {content['monto']:<22} {Diccionario_cat[content['category']]:<12}  {content['Description']:<13}")
               
                case 2:
                     choice = menuu("    C A T E G O R I A S     ","(selecciona para ver los gastos)", categorias )
                     match choice:
                         case 1:
                            Dates = read_file(PRODUCT_FILE_PATH)
                            otros = []
                            for content in Dates:                    
                                if content["category"] == 1:         
                                    otros.append(content)            
                            if len(otros)== 0:
                                print("¡No haz realizado ningun gasto extra!")
                            else:
                                Dates = read_file(PRODUCT_FILE_PATH)
                                print("\n=== P R O D U C T O S  R E G I S T R A D O S ===")
                                print("===             Categoria = Entretenimiento             ===")
                                print("---------------------------------------------------------------------------------")
                                print("= MONTO GASTADO         DESCRIPCION DEL GASTO \n")
                                for content in Dates:
                                    if content ["category"] == 1:
                                         print(f" ${content['monto']:<14} {content['Description']:<40}")       
                         case 2:
                            Dates = read_file(PRODUCT_FILE_PATH)
                            otros = []
                            for content in Dates:                    
                                if content["category"] == 2:         
                                    otros.append(content)            
                            if len(otros)== 0:
                                print("¡No haz realizado ningun gasto extra!")
                            else:
                                Dates = read_file(PRODUCT_FILE_PATH)
                                print("\n=== P R O D U C T O S  R E G I S T R A D O S ===")
                                print("===             Categoria = Entretenimiento             ===")
                                print("---------------------------------------------------------------------------------")
                                print("= MONTO GASTADO         DESCRIPCION DEL GASTO \n")
                                for content in Dates:
                                    if content ["category"] == 2:
                                         print(f" ${content['monto']:<14} {content['Description']:<40}")     
                         case 3:
                            Dates = read_file(PRODUCT_FILE_PATH)
                            otros = []
                            for content in Dates:                    
                                if content["category"] == 3:         
                                    otros.append(content)            
                            if len(otros)== 0:
                                print("¡No haz realizado ningun gasto extra!")
                            else:
                                Dates = read_file(PRODUCT_FILE_PATH)
                                print("\n=== P R O D U C T O S  R E G I S T R A D O S ===")
                                print("===             Categoria = Entretenimiento             ===")
                                print("---------------------------------------------------------------------------------")
                                print("= MONTO GASTADO         DESCRIPCION DEL GASTO \n")
                                for content in Dates:
                                    if content ["category"] == 3:
                                         print(f" ${content['monto']:<14} {content['Description']:<40}")           
                         case 4:
                            Dates = read_file(PRODUCT_FILE_PATH)
                            otros = []
                            for content in Dates:                    
                                if content["category"] == 4:         
                                    otros.append(content)            
                            if len(otros)== 0:
                                print("¡No haz realizado ningun gasto extra!")
                            else:
                                Dates = read_file(PRODUCT_FILE_PATH)
                                print("\n=== P R O D U C T O S  R E G I S T R A D O S ===")
                                print("===             Categoria = Entretenimiento             ===")
                                print("---------------------------------------------------------------------------------")
                                print("= MONTO GASTADO         DESCRIPCION DEL GASTO \n")
                                for content in Dates:
                                    if content ["category"] == 4:
                                         print(f" ${content['monto']:<14} {content['Description']:<40}")                                                                          
                   
                case 3:
                    print("Filtrar por fechas")
                    try:
                        fecha1 = input("Ingrese la fecha de inicio (DIA-MES-AÑO) -> ")
                        objDate1 = datetime.strptime(fecha1, "%d-%m-%Y") 
                        fecha2 = input("Ingrese la fecha límite (DIA-MES-AÑO) -> ")
                        objDate2 = datetime.strptime(fecha2, "%d-%m-%Y")
                        dataGasto = read_file(PRODUCT_FILE_PATH)
                        info = filtroFecha(dataGasto, objDate1, objDate2)
                        categories(info)
                    except ValueError:
                            print("Formato de fecha no válido (DIA-MES-AÑO)")
                case 4:
                     break
       case 3:  #calcular total
         print(":3")
