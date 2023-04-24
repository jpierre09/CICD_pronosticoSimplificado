# External imports
import requests

# Internal imports
from fastapi import FastAPI

app = FastAPI()


# endpoint testing root
@app.get("/")
async def project_root():
    return {"Testing endpoint root": "Integracion y entrega continua de software"}


# URL API SIATA
url = f"http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/?format=json"

# answer = requests.get(url)
# sending_answer = answer.json()


# municipios = []
# pronos = []
# for municipio in sending_answer['datos']:
#     nombre = municipio['nombreMunicipio'].strip()
#     municipios.append(nombre)

# for prono in sending_answer['datos']:
#     ventanas = prono['pronosticos'].strip()
#     pronos.append(ventanas)

# print(municipios)
# print(pronos)



# todos los pronosticos simplificados en 6 ventanas de tiempo
@app.get("/weather")
async def weather():

    response = requests.get(url)
    data = response.json()
    
    return data


# obtener pronostico por municipio
# @app.get("/pronostico/{codigo_municipio}")
# async def obtener_pronostico_por_municipio(codigo_municipio: str):
#     # código para obtener el pronóstico correspondiente al municipio
#     # ...
#     # construir el objeto Pronostico con los datos obtenidos
#     pronostico = Pronostico(municipio="Municipio Ejemplo", temperatura=25.6, humedad=0.85)
#     return pronostico



