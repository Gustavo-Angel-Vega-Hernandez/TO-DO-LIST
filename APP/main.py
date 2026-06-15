from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def mensajeBienvenida():
    return {"Mensaje": "Bienvenido a la API"}


