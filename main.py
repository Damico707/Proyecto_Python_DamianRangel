from jsonFileHandler import *
from UtilsFunctions import *

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

while True:
    choice = menuu("| O R G A N I Z A D O R|" , "--Gastos Diarios--" , options)
    match choice:
       case 1:
            content = {
                "monto": correct_number("¿De cuanto fue el gasto?\n --< ",),
                "category": correct_number("\n1. Comida\n2. Transporte\n3. Entretenimiento\n4. Otros\nSelecciona la categoria del gasto\n --> ", int, range(1, 5)),
                "Description":input("Descripcion del gasto //'Enter' para dejar vacio:\n -->")
            }

             
            print("\n*** Datos guardados correctamente***")
            print(f"Monto: ${content['monto']}")

            #if content['category'] == 1:
            #    print("Categoría: 1 - Comida")
            #elif content['category'] == 2:
            #    print("Categoría: 2 - Transporte")
            #elif content['category'] == 3:
            #    print("Categoría: 3 - Entretenimiento")
            #elif content['category'] == 4:
            #    print("Categoría: 4 - Otros")
            # print(f"Descripción: {content['Description']}")
            print(f"Categoría: {content['category']} , {Diccionario_cat[content['category']]}")
            print(f"Descripción: {content['Description']}")

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
                case 4:
                    break
       case 3:
         print(":3")
