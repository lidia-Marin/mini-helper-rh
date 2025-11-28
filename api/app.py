from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Consulta(BaseModel):
    pregunta: str

@app.post("/preguntar")
def preguntar(data: Consulta):
    respuesta = f"Estoy procesando tu pregunta: {data.pregunta}"
    return {"respuesta": respuesta}

@app.get("/")
def root():
    return {"mensaje": "Mini Helper RH API funcionando 🚀"}
