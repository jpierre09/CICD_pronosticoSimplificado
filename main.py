# External imports
import requests

# Internal imports
from fastapi import FastAPI, HTTPException

app = FastAPI()


#URL API SIATA
url = "http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/?format=json"



#Endpoint testing root
@app.get("/")
async def project_root():
    return {"Testing endpoint root": "Integracion y entrega continua de software"}



#Simplified forecast six times
@app.get("/weather")
async def weather(url: str = None):



    #If URL is not provided is used predeterminated URL
    if url is None:
        url = "http://siata.gov.co:8089/pronosticoMunicipiosSimplificado/63882184869634ff91bcf727d3fa210ec6c210bf/?format=json"



    #Validate url browser protocol
    if not url.startswith("http://") and not url.startswith("https://"):
        raise HTTPException(status_code=400, detail='Invalid URL, does not comply with the protocol')
    

    # Make request to the URL
    response = requests.get(url)


    # Check if content is json, if no "remote server error"
    content_type = response.headers.get("Content-Type")
    if not content_type or "application/json" not in content_type:
        raise HTTPException(status_code=500, detail="Unexpected response content type")


    #Response
    data = response.json()
    
    return data



