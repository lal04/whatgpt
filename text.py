# Abrir un archivo de texto en modo escritura ('w' significa write)
with open("archivo.txt", "a") as archivo:
    # Escribir datos en el archivo
    archivo.write("Hola, este es un ejemplo de texto.\n")
    archivo.write("Esto es otra línea de texto.\n")
    archivo.write("hola.\n")