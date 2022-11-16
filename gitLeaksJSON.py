from git import Repo
import re, sys, signal, pprint



DIR_REPO = './skale-manager'    # Ruta del repositorio en el que se va a buscar
KEY_WORDS = ['credentials', 'password', 'key', 'username', 'private']   # Lista de palabras clave a buscar en los commits


def extraer(dir_repo):
    #Extrae los commits del repositorio

    repo = Repo(dir_repo)
    commits = list(repo.iter_commits('develop'))
    return commits

def tranformar(commits):
    # Transforma los commits que nos interesan en un diccionario

    diccionario = {}
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



def main():
    commits = extraer(DIR_REPO) # Extrae los commits
    datos = tranformar(commits) # Transforma los commits en un diccionario
    
    cargar(datos)   # CArgamos los datos en un archivo JSON

if __name__ == '__main__':
    main()