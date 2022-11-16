from git import Repo
import re, pprint

dir_repo = "./directorio_repo"
key_words = ["credentials", "password", "key", "username", "private"]

def extraer(dir_repo):
    # Extraemos todos los commits del repositorio
    repo = Repo(dir_repo)
    commits = list(repo.iter_commits('develop'))
    return commits

def transformar(commits):
    # Transformamos los datos, y guardamos los commits que nos interesan en un diccionario
    dict_commits = {}
    for commit in commits:
        for word in key_words:
            if re.search(word, commit.message, re.IGNORECASE):
                # Guardamos en el diccionario el id del commit y el mensaje que se hubiera introducido
                dict_commits[commit.hexsha] = commit.message
    return dict_commits

def cargar(datos):
    # Cargamos los datos. En este caso, los escribimos en un fichero JSON
    with open('datos.json', 'w') as f:
        pprint.pprint(datos, stream=f)

def main():
    commits = extraer(dir_repo)
    datos = transformar(commits)
    cargar(datos)


if __name__ == "__main__":
    main()