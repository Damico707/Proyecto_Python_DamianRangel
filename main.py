from menu import menuu
from jsonFileHandler import *

PRODUCT_FILE_PATH= "./Database/products.json"
options = ("Registrar un nuevo gasto",
"Listar gastos",
"Calcular total de gastos",
"Generar reporte de gastos",
"Finalizar programa",)


while True:
    choice = menuu("O R G A N I Z A D O R", options)
    match choice:
        case 1:
            content = {
                "monto": input("¿De cuanto fue el gasto?"),
                "category": input("\n1. Comida\n2. Transporte\n3. Entretenimiento\n4. otros\nSelecciona la categoria del gasto\n -->"),
                "Description": input("Descripcion del gasto: ")
            }
            
            print(f("monto"))  #QUe especifique que se guardo
            datacontent = read_file(PRODUCT_FILE_PATH)
            datacontent.append(content)
            saveFile(PRODUCT_FILE_PATH,datacontent)