import matplotlib.pyplot as plt
import sys
import requests, json
from datetime import datetime

key = '' # u can get ur api key on https://api.openweathermap.org/
weatherURL = 'https://api.openweathermap.org/data/2.5/onecall?'
geoURL = 'http://api.openweathermap.org/geo/1.0/direct?'

def getGeo(city):
    response = requests.get(geoURL + "q=" + city + "&appid=" + key)
    json = response.json()
    return [json[0]["lat"], json[0]["lon"]]

def getWeather(lat, lon):
    response = requests.get(weatherURL + "lat=" + str(lat) + "&lon=" + str(lon) + "&exclude=minutely,daily&appid=" + key + "&units=metric")
    json = response.json()
    return json["hourly"]

def getTime(time, format):
    if format == "hora":
        return datetime.fromtimestamp(time).strftime('%H')
    elif format == "dia":
        return datetime.fromtimestamp(time).strftime('%d')

def drawGraphic():
    ciudad = input("Por favor, ingrese una ciudad: ")
    latitud = getGeo(ciudad)
    datos = getWeather(latitud[0], latitud[1])
    x = []; y = []
    for a in datos:
        if int(getTime(a["dt"], "dia")) == int(datetime.now().strftime('%d')):
            hora = int(str(getTime(a["dt"], "hora")))
            temperatura = int(round(a["temp"]))
            x.append(hora)
            y.append(temperatura)
    plt.plot(x, y)
    plt.xlabel("Hora del Dia")
    plt.ylabel("Temperatura en Celcius")
    plt.title("Clima en: " + ciudad)
    plt.show()

drawGraphic()
