def correct_number(mensaje, tipo=float, rango=None):
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