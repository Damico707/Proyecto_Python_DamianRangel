from json import dumps, load

# Lee un archivo JSON y devuelve su contenido como lista o diccionario.
# Si el archivo no existe o está vacío, devuelve una lista vacía.

def read_file(filePath):
    try:
        fileData = None
        with open(filePath) as f:
            fileData = load(f)
            f.close()
        return fileData
    except:
        return[]

# Guarda en formato JSON la data proporcionada en `data`
# Sobrescribe completamente el contenido del archivo.
def saveFile(fileName, data):
    jsonFile = open(fileName, "w")     
    jsonFile.write(dumps(data))  
    jsonFile.close()
    print("Datos guardados correctamente")

