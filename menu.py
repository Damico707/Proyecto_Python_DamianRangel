def menuu(title, options):
    choice = 0
    index = 1
    print("====================================")
    print("        O R G A N I Z A D O R       ")
    print("    -------"  "Gastos Diarios-"  "-----")
    print("====================================")
    for item in options:
        print(f"{index}, {item}")
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
