from fastapi import FastAPI
from devmaua.src import models #Importa todos as classes do repositorio https://github.com/Maua-Dev/models-devmaua

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
