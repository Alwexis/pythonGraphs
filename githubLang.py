import matplotlib.pyplot as plt
import requests, json

def getLanguagesFromRepositories(user):
    repoResp = requests.get("https://api.github.com/users/" + user + "/repos")
    if repoResp.status_code == 200:
        repoJson = repoResp.json()
        languages = {}
        for x in repoJson:
            langResp = requests.get(x["languages_url"])
            if langResp.status_code == 200:
                langJson = langResp.json()
                if len(langJson) > 0:
                    for y in langJson:
                        if y not in languages.keys():
                            languages[y] = langJson[y]
                        else:
                            languages[y] += langJson[y]
            else:
                return f"Ha fallado la petición GET al servidor ({langResp.status_code})"
        return languages
    else:
        return f"Ha fallado la petición GET al servidor ({repoResp.status_code})"

def drawGraphic():
    user = input("Por favor, ingrese un usuario: ")
    langs = getLanguagesFromRepositories(user)
    if type(langs) == dict:
        porcentajes = []; lenguajes = []; total = 0
        for a in langs:
            total += langs[a]
        for a in langs:
            porcentajes.append(round(langs[a] * 100 / total, 1))
            lenguajes.append(f"{a}: {round(langs[a] * 100 / total, 1)}%")
        plt.pie(porcentajes, labels = lenguajes)
        plt.title(f"Lenguajes usados por {user}")
        plt.show()
    else:
        print("Ha ocurrido un error: " + langs)

drawGraphic()
