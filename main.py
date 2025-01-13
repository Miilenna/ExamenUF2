from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import create
import read
from schema import users_registre
app = FastAPI()

class registre(BaseModel):
    nombre: str
    apellido: str
    correo: str
    descripción: Optional[str]
    curso: int
    año: int
    dirección: str
    codigo_postal: Optional[int]
    contraseña: str

@app.post("/usuari/add", response_model=dict)
async def add(usuari: registre):
    resultat = create.add_user(usuari.nombre, usuari.apellido, usuari.correo, usuari.descripción, usuari.curso, usuari.año, usuari.dirección, usuari.codigo_postal, usuari.contraseña)
    if resultat.get("status") !=1:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer el insert")
    return {
        "message":"Afegit correctament"
    }
@app.get("/usuari/get", response_model=dict)
async def get():
    resultat = read.read_user()
    if not resultat:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer el insert")
    return users_registre(resultat)