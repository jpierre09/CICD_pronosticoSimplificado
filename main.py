# External imports
import requests

# Internal imports
from fastapi import FastAPI, HTTPException

app = FastAPI()



# URL API SIATA
url = "http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/?format=json"



# endpoint testing root
@app.get("/")
async def project_root():
    return {"Testing endpoint root": "Integracion y entrega continua de software"}



# todos los pronosticos simplificados en 6 ventanas de tiempo
@app.get("/weather")
async def weather(url: str = None):



    # If URL is not provided is used predeterminated URL

    if url is None:
        url = "http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/?format=json"



    # Validate url browser protocol
    if not url.startswith("http://") and not url.startswith("https://"):
        raise HTTPException(status_code=400, detail='Invalid URL, does not comply with the protocol')
    
    

    response = requests.get(url)
    data = response.json()
    
    return data



