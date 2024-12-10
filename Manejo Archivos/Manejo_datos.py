nombre = input("Ingrese el nmbre que se almacenara: ")

archivo = open("nombre.txt", "a") #Estoy creando un archivo de texto, si no existe lo crea ya sea con w o r
archivo.write(nombre + "\n") #Escribo en el archivo
archivo.close() #Cierro el archivo


archivo = open("nombre.txt", "r") #Abro el archivo en modo lectura
print(archivo.read()) #Imprimo el contenido del archivo