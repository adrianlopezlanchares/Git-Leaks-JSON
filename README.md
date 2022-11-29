# Git-Leaks-JSON
Adquisicion de Datos:    Bloque 3 Practica 1

!!!

Necesaria una carpeta llamada "directorio_repo" (con algun commit hecho) en el mismo directorio que gitLeaksJSON.py al ejecutar

# Funcionamiento
De un repositorio local, el programa recoge todos los commits que se han hecho y busca por palabras clave, como "password" o "private". Si encuentra algún commit con una de esas palabras, guarda el commit en un diccionario. Todo este procedimiento se lleva a cabo con una ETL, y al final del programa carga los datos resultantes (el diccionarion de commits)
En esta práctica, los datos resultantes se cargan en un fichero JSON
