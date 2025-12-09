from json import dumps, load

def read_file(filePath):
    try:
        fileData = None
        with open(filePath) as f:
            fileData = load(f)
            f.close()
        return fileData
    except:
        return[]

def saveFile(fileName, data):
    jsonFile = open(fileName, "w")     #la w es la que crea el archivo desde 0, como renovando la informacion
    jsonFile.write(dumps(data))  #convierte la info en texto json con dumps
    jsonFile.close()
    print("Datos guardados correctamente")