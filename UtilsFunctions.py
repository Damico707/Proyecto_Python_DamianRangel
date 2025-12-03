from datetime import datetime

Diccionario_cat = {
        1: "Comida",
        2: "Transporte",
        3: "Entretenimiento",
        4: "Otros"
    }

def correct_number(mensaje, tipo=int, rango=None):
    while True:
        try:
            valor = tipo(input(mensaje))
            if rango and valor not in rango:
                print(f" Error, debes seleccionar una opción valida\n")
                continue
            return valor
        except ValueError:
            print("Error, debes ingresar un número válido\n")

def menuu(titulo, title, options):
    choice = 0
    index = 1
    print("====================================")
    print(f"      {titulo}   ")
    print(f"        {title}   ")
    print("====================================")
    for item in options:
        print(f"{index}. {item}")
        index += 1
    while True:    
        try:
            choice = int(input("¿Opcion? --> "))
            if choice not in range(1, len(options)+1):
                print("Opcion no valida, intente otra vez -->")
            else: 
                break
        except ValueError:
            print("Error, Solo se aceptan numeros")    
    return choice
    
def filtroFecha(datalist, fecha_ini, fecha_fin ):
    results = {"data": []}
    for gasto in datalist:
        fecha_str = gasto["time"]
        try:
            fecha_obj = datetime.strptime(fecha_str, "%d-%m-%Y")
            if fecha_ini <= fecha_obj <= fecha_fin:
                results["data"].append(gasto)
        except ValueError:
            continue
    return results

def categories(info):
    TEMPLATE_TITLE = "{:^0}{:^20}{:^20}{:^20}"
    TEMPLATE = "{:<12}{:<18}{:<20}{:<20}"
    print(TEMPLATE_TITLE.format(" MONTO", "CATEGORIA", "DESCRIPCION", "FECHA" ))
    if len(info["data"]) == 0:
        print("No se encontraron gatos en esta categoria...")
        return

    for item in info["data"]: 
        print(TEMPLATE.format(item['monto'], item['category'], item['Description'], item['time']))

def minimenu (Dates, numerito, categoria):
        Dates
        otros = []
        for content in Dates:                    
            if content["category"] == numerito:         
                otros.append(content)            
        if len(otros)== 0:
            print("¡No haz realizado ningun gasto extra!")
        else:
            
            Dates
            print("=======================================================")
            print("         P R O D U C T O S  R E G I S T R A D O S ")
            print(f"                 Categoria = {categoria}         ")
            print("=======================================================")
            print(" |     MONTO     |     DESCRIPCION    |    ")
            print(" |    GASTADO    |      DEL GASTO     |   FECHA ")
            print("------------------------------------------------------")
            for content in Dates:
                if content ["category"] == numerito:
                     print(f" ${content['monto']:<17} {content['Description']:<19} {content['time']:<}")


#def Monto_diario (Dates, fecha):
#        fechafinal = datetime.strptime(fecha, "%d-%m-%Y")
#        Dates
#        otros = []
#        for content in Dates:                    
#            if content["time"] == fechafinal:         
#                otros.append(content)            
#        if len(otros)== 0:
#            print("No tienes registrados gastos en esta fecha !")
#        else:
#            Dates
#            print("=======================================================")
#            print("         P R O D U C T O S  R E G I S T R A D O S ")
#            print(f"                    fecha : {fecha}                   ")
#            print("=======================================================")
#            print(" |     MONTO     |        CATEGORIA        |   DESCRIPCION     |         ")
#            print(" |    GASTADO    |        DEL GASTO        |    DEL GASTO      |   FECHA ")
#            print("------------------------------------------------------")
#            for content in Dates:
#                if content ["time"] == fechafinal:
#                     print(f" ${content['monto']:<17} {content['category']:<17} {content['Description']:<19} {content['time']:<}")

def Monto_diarioo(Dates, fecha):
    try:
        fecha_validada = datetime.strptime(fecha, "%d-%m-%Y") 
    except ValueError:
        print("Formato de fecha incorrecto. Usa (DD-MM-YYYY)")
        return
    otros = []
    total_gasto = 0

    for content in Dates:                    
        if content["time"] == fecha:  
            otros.append(content)
            total_gasto += content["monto"]
    if len(otros) == 0:
        print(f"\n¡No tienes registrados gastos en la fecha {fecha}!")
    else:
        print("\n=======================================================")
        print("         P R O D U C T O S  R E G I S T R A D O S ")
        print(f"                    Fecha: {fecha}                   ")
        print("=======================================================")
        print(" MONTO GASTADO    CATEGORÍA    DESCRIPCIÓN           FECHA")
        print("---------------------------------------------------------------")
        
        for content in Dates:
            if content ["time"] == fecha:
                print(f" ${content['monto']:<17} {Diccionario_cat[content['category']]:<27} {content['Description']:<19} {content['time']:<}")
        
        print("---------------------------------------------------------------")
        print(f" TOTAL DEL DÍA: ${total_gasto}")