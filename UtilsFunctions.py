from datetime import datetime

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

def minimenu (Dates, categoria, numerito):
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