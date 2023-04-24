TITULO DEL PROYECTO
CI-CD pronostico simplificado

comando para instalar las dependencias:
pip install -r requirements.txt

comando para correr el proyecto:
uvicorn main:app --reload

Endpoints:
root http://localhost:8000/

pronostico completo http://localhost:8000/weather/

recomendaciones:
Para evitar problemas con dependencias de librerias crear un entorno virtual venv u otros, yo omití el archivo en este caso con .gitignore 
