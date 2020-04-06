import requests
import datetime

POBLACION_MEXICO = 129.2
POBLACION_PERU = 32.17
POBLACION_ECUADOR = 16.62
POBLACION_BRASIL = 209.3

r = requests.get("https://api.covid19api.com/country/mexico/status/confirmed/live")
datos = r.json()
casos_mexico = []
fechas_mexico = []

for dato in datos:
    casos_mexico.append(dato["Cases"])
    fecha = datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d")
    fechas_mexico.append(fecha)

r = requests.get("https://api.covid19api.com/country/peru/status/confirmed/live")
datos_peru = r.json()
casos_peru = [ dato["Cases"] for dato in datos_peru ]
fechas_peru = [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_peru ]

r = requests.get("https://api.covid19api.com/country/ecuador/status/confirmed/live")
datos_ecuador = r.json()
casos_ecuador = [ dato["Cases"] for dato in datos_ecuador ]
fechas_ecuador = [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_ecuador ]

r = requests.get("https://api.covid19api.com/country/brazil/status/confirmed/live")
datos_brasil = r.json()
casos_brasil = [ dato["Cases"] for dato in datos_brasil ]
fechas_brasil = [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_brasil ] 
