from git import Repo
import re 
import sys
import signal
import pprint

# Variables globales:
# Ruta del repositorio en el que se van a buscar commits
REPO_DIR = './skale-manager'

# Lista de palabras clave a buscar en los commits
KEY_WORDS = ['credentials', 'password', 'key', 'username', 'private']


def extraer(repo_dir):
    #Extrae los commits del repositorio
    repo = Repo(repo_dir)
    commits = list(repo.iter_commits('develop'))
    return commits

def tranformar(commits):
    # Transforma los commits que nos interesan en un diccionario
    diccionario = dict()
    
    for commit in commits:
        for word in KEY_WORDS:
            if re.search(word, commit.message, re.IGNORECASE):
                # Si la encuentra, añade al diccionario el "id"(versión en la que se hace) 
                # del commit y el mensaje que se hubiera introducido
                diccionario[commit.hexsha] =  commit.message
    return diccionario


def cargar(datos):
    # Carga los datos. En este caso, los cargamos en un archivo json
    with open('datos.json', 'w') as f:
        pprint.pprint(datos, stream=f)



def handler_signal(signal, frame):
    '''
    Función que maneja la señal SIGINT (CTRL + C)
    '''
    # Imprime un mensaje y sale del programa
    print("\n\n[!] Out ............. \n")
    sys.exit(1)



if __name__ == '__main__':
    # Para que el main pueda registrar la señal SIGINT
    signal.signal(signal.SIGINT, handler_signal)

    # Extrae los commits
    commits = extraer(REPO_DIR)

    # Los transforma para imprimirlos
    datos = tranformar(commits)
    
    # Los imprime
    cargar(datos)
